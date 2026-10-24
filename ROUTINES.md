# Scheduled tasks (routines)

Both need: this repository attached, and either the Firecrawl/TinyFish connectors or an environment with Custom/Full network access (the Default "Trusted" network blocks university sites, arbeitsagentur.de and job boards).

## 1. Campaign Runner — Run now only

```
You are executing one work package of an evidence-led research campaign in this repository.
Read CLAUDE.md, STATE.md, profile.md, weights.md and PLAN.md.
Execute ONLY the package STATE.md marks as NEXT, following PLAN.md and the rules in CLAUDE.md.
If a required profile.md field the package depends on is UNKNOWN, or scoring is required and weights.md is not LOCKED, do what you can without it, then write the blocking questions to STATE.md and stop.
Write the package report to reports/, update programmes.csv / vacancies / sources.csv as applicable, update STATE.md (mark the package done, set the next one as NEXT, list open questions), commit and push to main.
Do not start the next package.
```

## 2. Market Tracker — weekly (create only after Package 2 has a shortlist)

```
Read CLAUDE.md, programmes.csv and reports/03-employment.md.
Run: python3 scripts/ba_collect.py /tmp/ba && python3 scripts/ba_collect.py /tmp/ba enrich
Download the Arbeitnow feed (https://www.arbeitnow.com/api/job-board-api, all pages) to /tmp/an.json.
Run: python3 scripts/analyze_vacancies.py /tmp/ba /tmp/an.json vacancies/YYYY-Www.csv vacancies/YYYY-Www-metrics.json (week label defaults to the current ISO week).
Do not scrape LinkedIn, StepStone or Indeed (terms of service).
Compare with the previous week's metrics: per region, entry-level counts, English-accessible counts, top skills. Append a short dated trend note to reports/market-tracker.md.
Re-check application deadlines and admission pages of shortlisted programmes; record any change in STATE.md under "Watch dates" with the source URL.
Note which sources were blocked. Commit and push to main.
```
