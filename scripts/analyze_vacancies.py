"""Merge BA Jobsuche and Arbeitnow data into the weekly vacancy CSV and regional metrics.

Usage: python3 scripts/analyze_vacancies.py BA_DIR ARBEITNOW_JSON OUT_CSV OUT_METRICS_JSON
"""
import collections, csv, html, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from ba_collect import (classify, SKILLS, GERMAN_REQ, ENGLISH_ONLY_OK, EN_WORDS, DE_WORDS, STUDENT, INTERN,
                        JUNIOR)

AN_REGIONS = {
    "berlin": r"berlin|potsdam",
    "rhine-main": r"frankfurt|darmstadt|mainz|wiesbaden|offenbach|eschborn|bad homburg|rüsselsheim|hanau|bingen|"
                  r"langen|neu-isenburg|oberursel|dreieich",
    "fulda": r"fulda",
    "dresden": r"dresden",
    "ruhr": r"bochum|essen|dortmund|duisburg|gelsenkirchen|herne|oberhausen|mülheim|witten|recklinghausen|hagen",
    "cologne-bonn": r"köln|koeln|cologne|bonn|leverkusen|hürth|bergisch gladbach|sankt augustin|troisdorf",
    "saarbruecken": r"saarbrücken|saarbruecken",
    # reference markets with no shortlisted campus
    "ref-munich": r"münchen|munich|muenchen",
    "ref-hamburg": r"hamburg",
}
AN_ENTRY = re.compile(r"internship|working student|student|entry|berufseinstieg|hilfstätigkeit|praktikum|werkstudent",
                      re.I)


def text_features(text):
    return {
        "ad_language": "en" if len(EN_WORDS.findall(text)) > len(DE_WORDS.findall(text)) else "de",
        "german_required": bool(GERMAN_REQ.search(text)) and not ENGLISH_ONLY_OK.search(text),
        "german_optional_stated": bool(ENGLISH_ONLY_OK.search(text)),
        "skills": [k for k, rx in SKILLS.items() if rx.search(text)],
    }


def main(ba_dir, an_path, out_csv, out_metrics):
    rows, metrics = [], {}
    week = os.environ.get("WEEK") or __import__("datetime").date.today().strftime("%G-W%V")
    # --- BA
    for f in sorted(os.listdir(ba_dir)):
        if not f.startswith("raw_"):
            continue
        region = f[4:-5]
        data = json.load(open(os.path.join(ba_dir, f)))
        jobs = data["jobs"]
        rel = [j for j in jobs if j["group"] in "ABC"]
        m = metrics.setdefault(region, {})
        m["ba_unique_ads_matched"] = len(jobs)
        m["ba_infra_ads_all_levels"] = dict(collections.Counter(j["group"] for j in rel))
        m["ba_entry_level_by_kind"] = dict(collections.Counter(j["kind"] for j in rel
                                                               if j["kind"] in ("student", "internship", "junior")))
        m["ba_werkstudent_all_fields_total"] = data["totals"].get("Werkstudent")
        for j in rel:
            if j["kind"] not in ("student", "internship", "junior"):
                continue
            rows.append({"id": "BA-" + j["ref"], "week": week, "region": region, "job_title": j["title"],
                         "employer": j["employer"], "employment_type": j["kind"], "group": j["group"],
                         "technical_requirements": ";".join(j.get("skills", [])),
                         "german_level": ("required" if j.get("german_required") else
                                          "optional-stated" if j.get("german_optional_stated") else
                                          "unstated" if j.get("detail") else "not-checked"),
                         "english_ok": ("yes" if j.get("ad_language") == "en" or j.get("german_optional_stated")
                                        else "unclear" if j.get("detail") else "not-checked"),
                         "experience_years": "", "student_eligible": "yes" if j["kind"] == "student" else "",
                         "location": j["city"], "commute_from_campus_min": "", "posting_date": j["published"],
                         "url": "https://www.arbeitsagentur.de/jobsuche/jobdetail/" + j["ref"],
                         "source": "BA Jobsuche API", "duplicate_of": ""})
    # --- Arbeitnow
    an = json.load(open(an_path))
    for j in an:
        loc = (j.get("location") or "").lower()
        region = next((r for r, rx in AN_REGIONS.items() if re.search(rx, loc)), None)
        if not region:
            continue
        g, k = classify(j["title"])
        types = " ".join(j.get("job_types", []))
        if k not in ("student", "internship", "junior") and AN_ENTRY.search(types):
            k = ("student" if re.search(r"student", types, re.I) and not re.search(r"intern|praktik|stage", types, re.I)
                 else "internship" if re.search(r"intern|praktik|stage", types, re.I) else "junior")
        text = html.unescape(re.sub(r"<[^>]+>", " ", j.get("description") or ""))
        feat = text_features(text)
        m = metrics.setdefault(region, {})
        an_m = m.setdefault("arbeitnow", {"ads": 0, "infra_all_levels": 0, "infra_entry": 0, "it_ads_english": 0,
                                          "it_ads": 0})
        an_m["ads"] += 1
        if g in "ABC":
            an_m["it_ads"] += 1
            an_m["it_ads_english"] += feat["ad_language"] == "en"
        if g in "AB":
            an_m["infra_all_levels"] += 1
        if g in "ABC" and k in ("student", "internship", "junior"):
            an_m["infra_entry"] += g in "AB"
            rows.append({"id": "AN-" + j["slug"], "week": week, "region": region, "job_title": j["title"],
                         "employer": j["company_name"], "employment_type": k, "group": g,
                         "technical_requirements": ";".join(feat["skills"]),
                         "german_level": ("required" if feat["german_required"] else
                                          "optional-stated" if feat["german_optional_stated"] else "unstated"),
                         "english_ok": "yes" if feat["ad_language"] == "en" or feat["german_optional_stated"]
                         else "unclear", "experience_years": "", "student_eligible": "yes" if k == "student" else "",
                         "location": j.get("location"), "commute_from_campus_min": "",
                         "posting_date": "", "url": j["url"], "source": "Arbeitnow API", "duplicate_of": ""})
    # --- entry-level language / skills per region (both sources, detail-checked rows only)
    for region in metrics:
        rr = [r for r in rows if r["region"] == region and r["german_level"] != "not-checked"]
        m = metrics[region]
        m["entry_rows_checked"] = len(rr)
        m["entry_german_required"] = sum(r["german_level"] == "required" for r in rr)
        m["entry_english_ad_or_german_optional"] = sum(r["english_ok"] == "yes" for r in rr)
        m["entry_skills"] = dict(collections.Counter(s for r in rr for s in r["technical_requirements"].split(";")
                                                     if s).most_common())
    hdr = open(os.path.join(os.path.dirname(out_csv), "SCHEMA.csv")).readline().strip().split(",")
    with open(out_csv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=hdr)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    json.dump(metrics, open(out_metrics, "w"), indent=1, ensure_ascii=False)
    print(len(rows), "rows")


if __name__ == "__main__":
    main(*sys.argv[1:5])
