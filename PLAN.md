# Research plan

**Objective:** find the best risk-adjusted route into infrastructure employment in Germany.
**Primary outcome:** relevant employment experience during study (or during transition).
**Long-term outcome:** qualified infrastructure employment.
**Decision constraint:** affordable without relying on immediate employment.
**Evidence standard:** official documents, live vacancies, direct verification.

Job groups used throughout:
- **A — direct:** cloud engineering, DevOps, platform engineering, SRE, infrastructure automation, cloud security.
- **B — adjacent:** Linux/systems administration, systems/network engineering, cloud operations, SecOps.
- **C — bridge:** software/backend roles with substantial deployment automation, IaC, observability or on-call/production ownership. A pure SWE role with no infra exposure is not C.

---

## Package 1 — Feasibility and Route B test

1. Resolve `UNKNOWN` fields in `profile.md` that can be checked from official sources (e.g. recognition rules, uni-assist/APS requirements by nationality, current blocked-account amount, semester fee ranges, tuition by state). Fields only the candidate knows go to `STATE.md` as questions.
2. Build a cost model: per-semester and total cost for 3- and 4-semester programmes in tuition-free vs. tuition-charging states, against current funds. Favourable / expected / adverse.
3. **Route B test (moved forward from Phase 6):** using current official criteria, assess employment-first routes for this profile — Chancenkarte (Opportunity Card), EU Blue Card / skilled-worker visa with a job offer, remote-to-relocation. Requirements, costs, timelines, what fails. Sample 15–20 live English-accessible Group A/B/C junior–mid roles in Germany to check whether ~3 years SWE is competitive.
4. Output `reports/01-feasibility.md`: hard filters confirmed, cost model, Route B verdict (viable / conditional / not viable), and whether Route A (master's) is still justified enough to continue.

**Stop condition:** report written. If Route B is clearly superior, say so and recommend whether Packages 2–4 are still worth running.

## Package 2 — Programme discovery

1. Search Hochschulkompass and DAAD International Programmes — not "best cloud master's" lists. Include CS, applied CS, distributed systems, IT security, communications/network engineering, cloud/infrastructure programmes, at HAWs and universities.
2. Build 20–30 entries in `programmes.csv` from official pages: admission rules, ECTS requirement (note 3-semester/210-ECTS options), language, intake, non-EU deadline, uni-assist, tuition, fees, practical semester, company-thesis rules.
3. Apply hard filters. Mark `status` = shortlisted / eliminated (with reason) / unknown.
4. For shortlisted programmes, read module handbooks: real Linux, networking, distributed systems, cloud, security, IaC content — not titles.
5. Output `reports/02-programmes.md`.

**Stop condition:** inventory complete with 6–10 shortlisted programmes, or a documented reason why fewer qualify.

## Package 3 — Employment validation

1. For each region hosting shortlisted programmes, collect 20–30 unique vacancies into `vacancies/YYYY-WW.csv` (schema in `vacancies/SCHEMA.csv`). Sources: BA Jobsuche (prefer its API), employer career pages, accessible job boards. Note which sources were blocked — sample bias matters.
2. Classify A/B/C. Record German requirement, experience requirement, student eligibility. Compute per region: counts by group and type, share accessible at B1 vs. B2, top requested skills.
3. For the top 6–8 programmes: evidence of company theses, internships, career services, job fairs, timetable constraints (mandatory labs), graduate outcomes. Distinguish documented examples from marketing.
4. Forum research (Reddit, German career forums) to surface risks only. Produce a list of current students/alumni to contact and the interview questions; the candidate conducts the interviews and logs notes in `reports/interviews/`.
5. Output `reports/03-employment.md`.

**Stop condition:** regional comparison and programme-level employment-access assessment written, with uncertainty explicit.

## Package 4 — Decision

1. Requires `weights.md` LOCKED. Score each surviving programme with score + confidence + reason.
2. Compare Route A (best programme), Route B (employment-first), Route C (best non-HAW university option) on total cost, time, job-market access, technical growth, immigration feasibility, downside if employment takes longer.
3. Favourable / expected / adverse scenarios with the assumptions that flip the outcome. No fabricated probabilities.
4. Output `reports/04-decision.md`: recommendation (a programme, another route, or "insufficient evidence — do X first"), application priorities with deadlines, unresolved risks.

**Stop condition:** decision memo written.
