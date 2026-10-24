"""Collect and classify infrastructure-relevant vacancies from the BA Jobsuche API.

Usage: python3 scripts/ba_collect.py OUT_DIR
Writes OUT_DIR/raw_<region>.json, OUT_DIR/details/<refnr>.json and OUT_DIR/summary.json.
"""
import base64, json, os, re, sys, time, urllib.parse, urllib.request

API = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
HDR = {"X-API-Key": "jobboerse-jobsuche", "User-Agent": "germany-infra-research"}

REGIONS = {  # search centre, radius km; chosen to cover the shortlisted campuses
    "berlin": ("Berlin", 30),          # TU Berlin, BHT, HPI Potsdam
    "rhine-main": ("Frankfurt am Main", 45),  # TU Darmstadt, Bingen edge, Mainz
    "fulda": ("Fulda", 40),
    "dresden": ("Dresden", 25),
    "ruhr": ("Bochum", 30),            # Bochum, Essen, Dortmund, Duisburg edge
    "cologne-bonn": ("Köln", 30),      # TH Köln, Bonn
    "saarbruecken": ("Saarbrücken", 30),
}

# Single terms: the BA free-text search ANDs multi-word queries too strictly ("Werkstudent DevOps" -> ~0 hits).
TERMS = ["DevOps", "Cloud", "Kubernetes", "Linux", "Systemadministrator", "IT-Administrator",
         "Netzwerkadministrator", "Netzwerktechnik", "IT-Sicherheit", "Cyber Security", "Platform Engineer",
         "Site Reliability", "Systemingenieur", "System Engineer", "IT-Infrastruktur", "Rechenzentrum", "Backend"]
QUERIES = ([("all", t, 1) for t in TERMS] + [("all", "Werkstudent", 1), ("all", "Working Student", 1)] +
           [("praktikum", t, 34) for t in TERMS])

GROUP_A = re.compile(r"devops|cloud|kubernetes|k8s|platform|site reliability|\bsre\b|infrastructure as code|terraform|"
                     r"infrastruktur.*automat|cloud security|container", re.I)
GROUP_B = re.compile(r"linux|system ?admin|systemadmin|systemengineer|system engineer|systemtechnik|netzwerk|network|"
                     r"it[- ]?sicherheit|it[- ]?security|cyber|soc\b|security operations|it[- ]?operations|it[- ]?betrieb|"
                     r"rechenzentrum|data ?center|infrastruktur|infrastructure|administrat|it[- ]?support|client|"
                     r"windows|active directory|firewall|monitoring", re.I)
GROUP_C = re.compile(r"backend|software|entwickl|developer|engineer|python|golang|\bgo\b|java", re.I)
NON_IT = re.compile(r"\bhr\b|personal|kommunikation|communication|sales|vertrieb|marketing|buchhalt|accounting|"
                    r"account manager|account executive|finanz|finance|einkauf|recruit|steuer|\btax\b|legal|jurist|"
                    r"logistik|lager|verkäufer|kassierer|pflege|arzt|medizin|elektriker|elektroniker|mechatroniker|"
                    r"monteur|kaufm|presales|pre-sales|consultant sap|sap |controlling|produktion|bau|gebäude|"
                    r"haustechnik|fahrzeug|kfz|lehrer|dozent|trainer", re.I)
INTERN = re.compile(r"praktik|intern\b|internship|trainee|abschlussarbeit|thesis|masterarbeit|bachelorarbeit", re.I)
STUDENT = re.compile(r"werkstudent|working student|studentische|student assistant|student job", re.I)
JUNIOR = re.compile(r"junior|einsteiger|absolvent|graduate|berufseinsteiger|entry", re.I)
SENIOR = re.compile(r"senior|lead|head of|principal|leitung|leiter|architekt|architect|teamlead|manager", re.I)

SKILLS = {k: re.compile(v, re.I) for k, v in {
    "linux": r"linux|unix|bash|shell", "windows/ad": r"windows|active directory|\bad\b|microsoft 365|m365|intune",
    "networking": r"netzwerk|network|tcp/ip|routing|switching|firewall|vpn|dns|cisco",
    "docker/containers": r"docker|container|podman", "kubernetes": r"kubernetes|k8s|openshift|helm",
    "aws": r"\baws\b|amazon web services", "azure": r"azure", "gcp": r"\bgcp\b|google cloud",
    "terraform/iac": r"terraform|infrastructure as code|\biac\b|pulumi|cloudformation|bicep",
    "ansible/config": r"ansible|puppet|chef|saltstack", "ci/cd": r"ci/cd|cicd|gitlab ci|github actions|jenkins|argo",
    "python": r"python", "go": r"\bgolang\b|\bgo\b", "monitoring": r"prometheus|grafana|monitoring|observability|elk|splunk",
    "security": r"security|sicherheit|siem|iso 27001|bsi", "sql/db": r"\bsql\b|postgres|mysql|datenbank|database",
    "virtualisation": r"vmware|hyper-v|proxmox|virtualisier|virtualiz"}.items()}
GERMAN_REQ = re.compile(r"(sehr gute|gute|fließend|verhandlungssicher|fliessend)\w*\s+(deutsch|deutschkenntnisse)|"
                        r"deutsch(kenntnisse)?\s*(\(|in wort und schrift|auf (c1|c2|b2|muttersprach)|c1|c2|b2)|"
                        r"(fluent|excellent|very good|good)\s+(command of\s+)?german|german\s*\(?(c1|c2|b2|native|fluent)|"
                        r"deutsch (und|sowie) englisch|german and english", re.I)
ENGLISH_ONLY_OK = re.compile(r"german (is )?(a plus|nice to have|not required|is an advantage)|no german (required|needed)|"
                             r"deutschkenntnisse (sind )?(von vorteil|wünschenswert|nicht erforderlich)", re.I)
EN_WORDS = re.compile(r"\b(the|and|you|your|with|we|our|for|experience|team)\b", re.I)
DE_WORDS = re.compile(r"\b(und|die|der|wir|sie|mit|für|bei|unser|ihre|erfahrung)\b", re.I)


def get(path, params=None):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            if attempt == 3:
                print("ERR", url, e, file=sys.stderr)
                return None
            time.sleep(2 ** attempt)


def classify(title):
    t = title or ""
    if NON_IT.search(t):
        group = "-"
    else:
        group = "A" if GROUP_A.search(t) else "B" if GROUP_B.search(t) else "C" if GROUP_C.search(t) else "-"
    kind = ("student" if STUDENT.search(t) else "internship" if INTERN.search(t) else "junior" if JUNIOR.search(t)
            else "senior" if SENIOR.search(t) else "other")
    return group, kind


def main(out):
    os.makedirs(os.path.join(out, "details"), exist_ok=True)
    summary = {"collected": time.strftime("%Y-%m-%d"), "regions": {}}
    for region, (wo, radius) in REGIONS.items():
        jobs, totals = {}, {}
        for bucket, was, art in QUERIES:
            results = []
            for page in (1, 2, 3):
                params = {"was": was, "wo": wo, "umkreis": radius, "angebotsart": art, "size": 100, "page": page,
                          "veroeffentlichtseit": 60}
                d = get("/pc/v6/jobs", params)
                time.sleep(0.3)
                if not d:
                    break
                if page == 1:
                    totals[was + ("" if art == 1 else " [Praktikum]")] = d.get("maxErgebnisse", 0)
                results += d.get("ergebnisliste", [])
                if len(results) >= d.get("maxErgebnisse", 0):
                    break
            for j in results:
                ref = j["referenznummer"]
                if ref not in jobs:
                    g, k = classify(j.get("stellenangebotsTitel"))
                    if bucket == "praktikum" and k not in ("student", "internship"):
                        k = "internship"
                    jobs[ref] = {"ref": ref, "title": j.get("stellenangebotsTitel"), "employer": j.get("firma"),
                                 "city": (j.get("stellenlokationen") or [{}])[0].get("adresse", {}).get("ort"),
                                 "published": j.get("datumErsteVeroeffentlichung"), "group": g, "kind": k,
                                 "zeitarbeit": j.get("istZeitarbeit"), "query": was}
        json.dump({"totals": totals, "jobs": list(jobs.values())}, open(os.path.join(out, f"raw_{region}.json"), "w"),
                  ensure_ascii=False, indent=1)
        summary["regions"][region] = {"unique": len(jobs)}
        print(region, len(jobs), flush=True)
    json.dump(summary, open(os.path.join(out, "summary.json"), "w"), indent=1)


def enrich(out, per_region_cap=40):
    """Fetch details for relevant student/junior/internship ads and extract language + skills."""
    for f in sorted(os.listdir(out)):
        if not f.startswith("raw_"):
            continue
        data = json.load(open(os.path.join(out, f)))
        for j in data["jobs"]:
            g, k = classify(j["title"])
            j["group"] = g
            j["kind"] = k if (k != "other" or j["kind"] != "internship") else "internship"
        picked = [j for j in data["jobs"] if j["group"] in "ABC" and j["kind"] in ("student", "junior", "internship")]
        picked.sort(key=lambda j: ("ABC".index(j["group"]), j["published"] or ""), reverse=False)
        for j in picked[:per_region_cap * 3]:  # cap keeps API load polite
            p = os.path.join(out, "details", re.sub(r"[^A-Za-z0-9_-]", "_", j["ref"]) + ".json")
            if os.path.exists(p):
                d = json.load(open(p))
            else:
                d = get("/pc/v4/jobdetails/" + base64.b64encode(j["ref"].encode()).decode())
                time.sleep(0.3)
                if d:
                    json.dump(d, open(p, "w"), ensure_ascii=False)
            if not d:
                continue
            text = " ".join(str(d.get(k) or "") for k in ("stellenangebotsBeschreibung", "stellenangebotsTitel"))
            j["detail"] = True
            j["ad_language"] = "en" if len(EN_WORDS.findall(text)) > len(DE_WORDS.findall(text)) else "de"
            j["german_required"] = bool(GERMAN_REQ.search(text)) and not ENGLISH_ONLY_OK.search(text)
            j["german_optional_stated"] = bool(ENGLISH_ONLY_OK.search(text))
            j["skills"] = [k for k, rx in SKILLS.items() if rx.search(text)]
            j["external_url"] = d.get("allianzpartnerUrl")
            j["agency"] = bool(d.get("istArbeitnehmerUeberlassung") or d.get("istPrivateArbeitsvermittlung"))
        json.dump(data, open(os.path.join(out, f), "w"), ensure_ascii=False, indent=1)
        print(f, sum(1 for j in data["jobs"] if j.get("detail")), flush=True)


if __name__ == "__main__":
    main(sys.argv[1]) if len(sys.argv) < 3 else enrich(sys.argv[1])
