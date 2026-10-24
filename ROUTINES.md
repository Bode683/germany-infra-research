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
Read CLAUDE.md and programmes.csv. For each region with a status=shortlisted programme, collect 20–30 current vacancies from BA Jobsuche (prefer its API) and employer career pages.
Classify each as group A/B/C per PLAN.md; record German level, experience requirement, student eligibility, URL and posting date, using vacancies/SCHEMA.csv.
Deduplicate against earlier vacancies/*.csv files. Write vacancies/YYYY-WW.csv.
Re-check application deadlines and admission pages of shortlisted programmes; record any change in STATE.md under "Watch dates" with the source URL.
Note which sources were blocked. Commit and push to main.
```
