# Package 3 — Employment validation

Date: 2026-10-24 (snapshot: ads published in the last 60 days). Data: `vacancies/2026-W43.csv` (152 entry-level rows), `vacancies/2026-W43-metrics.json`. Code: `scripts/ba_collect.py`, `scripts/analyze_vacancies.py`. Sources S031–S038.

## Bottom line

1. **German level decides working-student access, not the programme.** Across the six campus regions we found **139 entry-level infrastructure or bridge ads** (student, internship, junior). **Outside Berlin, none was written in English or said German was optional.** In Berlin, 7 of 43 were, and only **2** of those 7 were infrastructure roles. On this evidence, a B1 candidate has close to zero advertised working-student infrastructure options anywhere except Berlin, and very few there.
2. **Entry-level demand is thin everywhere.** The big regions show 600–700 infrastructure ads at all seniority levels (Rhine-Main 678, Berlin 638) but only **25–43 entry-level ads** per 60 days. Juniors compete for a small slice.
3. **What employers ask for at entry level is classic systems work, not cloud certifications.** Security (60 of 139 ads), networking (45), Linux (36), Windows/Active Directory (35), Python (30). Kubernetes (10), Terraform (5) and AWS (2) barely appear at entry level. This should shape preparation (see "Implications").
4. **Saarbrücken and Fulda have no meaningful local market:** 0 and 1 entry-level ads. Saarland Cybersecurity's visa-timing advantage does not make up for that.

## Method and its limits

- **Sources used:** the Federal Employment Agency (BA) Jobsuche API (official) and the Arbeitnow public job API (aggregator of company job-system listings, skewed to startups).
- **Sources not used:** LinkedIn and StepStone respond to automated requests, but their terms forbid scraping. Indeed blocks access. These are the main channels for English-language startup jobs, so **the sample under-counts English-accessible roles**, especially in Berlin and Munich.
- **The BA is not where working-student jobs are advertised.** It shows only 54 working-student ads *in any field* in Berlin over 60 days (S033). Absolute student-job counts here are therefore a floor, not a market size. The **German vs. English share** is the more robust signal: it is consistent across both sources and every region.
- **Classification:** job titles were sorted into A (cloud/DevOps/platform/SRE), B (Linux/sysadmin/network/security/IT operations), C (software/backend bridge) and seniority by keyword rules, with non-IT titles excluded. Ad language and German requirements were detected heuristically from the full ad text. Expect some misclassification. The CSV is there for spot checks.
- This is one snapshot. The Market Tracker routine should repeat it weekly so trends replace single counts.

## Regional comparison

| Region | Infra ads, all levels (BA, A+B) | Entry-level infra/bridge ads (both sources) | Of which English / German optional | IT ads in English (Arbeitnow) | Programmes |
|---|---|---|---|---|---|
| Berlin (+Potsdam) | 638 | 43 | **7 (2 infra)** | 104 / 141 | TU Berlin, HPI, BHT |
| Rhine-Main | **678** | 35 | 0 | 4 / 22 | TU Darmstadt, Bingen (Fulda ~1h) |
| Cologne/Bonn | 488 | 26 | 0 | 4 / 20 | TH Köln CSN, Digital Sciences |
| Ruhr | 267 | 25 | 0 | 0 / 5 | Bochum, Rhine-Waal (edge) |
| Dresden | 190 | 9 | 0 | 1 / 4 | TU Dresden |
| Saarbrücken | 70 | 0 | – | 0 / 0 | Saarland |
| Fulda (local) | 17 | 1 | 0 | – | Fulda |
| *Reference: Munich* | – | 9 (Arbeitnow only) | 7 | 66 / 89 | (none affordable) |
| *Reference: Hamburg* | – | 4 (Arbeitnow only) | 0 | 13 / 25 | (reach only) |

**Reading it:** Rhine-Main has the most infrastructure work and Berlin the most English-friendly ecosystem. Cologne and the Ruhr are mid-sized and German-gated. In the working-student and junior segment, the German-language share is 100% outside Berlin and 84% inside Berlin.

## Skills in entry-level ads (139 ads, campus regions)

| Skill | Ads | | Skill | Ads |
|---|---|---|---|---|
| Security | 60 | | Docker/containers | 16 |
| Networking | 45 | | Monitoring | 15 |
| Linux | 36 | | CI/CD | 14 |
| Windows / Active Directory | 35 | | Virtualisation | 11 |
| Python | 30 | | Kubernetes | 10 |
| SQL / databases | 22 | | Ansible | 6 |
| Azure | 16 | | Terraform | 5 / AWS 2 / GCP 1 |

Azure leads AWS by a wide margin, which reflects the Microsoft-heavy German mid-market. Entry roles are mostly "Junior IT-Administrator / Systemadministrator / System Engineer" (group B, 62 ads) rather than DevOps/cloud (group A, 15 ads).

## Programme-level employment access (Tier 1)

Industry links are graded **documented** (official page), **claimed** (marketing wording) or **UNKNOWN**. Company-thesis rates, graduate destinations and timetable clashes were not found for any programme. They need the student and alumni interviews below.

| Programme | Regional access at B1 | Regional access at B2 | Industry integration evidence | Assessment |
|---|---|---|---|---|
| TU Berlin CS | **Best available, still weak** (2 English infra entry ads) | Good (largest English and German mix) | Internship recommended, no credits (documented); career service (claimed) | Strongest location. Admission and timing are the problems, not jobs |
| HPI / Potsdam CS | As Berlin | As Berlin | Projects with partners (documented); HPI industry network (claimed) | Strong location; C1 English and selectivity are the problems |
| TU Darmstadt CS | Very weak (0 English entry ads in Rhine-Main) | **Best volume** (678 infra ads) | None documented | Pays off only with German B2+ |
| Bingen CS | Very weak | Good (Rhine-Main edge; Mainz/Wiesbaden ~30–45 min) | UNKNOWN | Same as Darmstadt |
| Fulda GSD | Very weak | Weak locally; Frankfurt ~1h each way, hard to combine with a 20h job | Optional 20-week internship in Germany (documented) | Downgrade: commute penalty |
| TH Köln CSN | Very weak | Medium-good (488 infra ads) | R&D projects, often with companies (documented, unquantified) | Good if German B2; admission risk low (open admission) |
| Bochum CS | Very weak | Medium (Ruhr 267); security is the top skill demand in the Ruhr (15/25) | UNKNOWN | Security fit is real; market mid-sized |
| TU Dresden CS (DSE track) | Very weak | Weak-medium (190) | UNKNOWN | Small market |
| Saarland Cybersecurity | **None** | **None** (0 entry ads) | Optional internships (documented) | **Downgrade to Tier 2**: no local market |

## Implications for the decision

1. **German is the highest-return investment, ahead of any programme choice.** At B1, Berlin is the only region with any English-accessible entry-level infrastructure ads, and there were 2 in the sample. At certified B2, Rhine-Main and Cologne open up, and those are the largest markets in the sample. A2 → B2 by September 2027 should be treated as the plan, not a stretch goal. It also reopens THI's German-taught cloud master's (Package 2).
2. **Berlin is the best fallback if German stalls at B1,** but every Berlin programme has an admission problem: TU Berlin's theory-credit gate and timing, HPI's C1 and selectivity, BHT's possible EE background. Fixing at least one of them (transcript check, IELTS 7, GRE where useful) is worth doing now.
3. **Prepare for the jobs that exist,** not for the job titles you want: Linux and Windows/AD administration, networking (TCP/IP, DNS, routing, firewalls), security fundamentals, Python and Bash, then Docker and CI/CD, then one cloud with **Azure first**. A home lab plus 2–3 public projects (an automated Linux server build with Ansible, a containerised service with CI/CD, a small Azure deployment with Terraform) matches the demand profile far better than a cloud certificate alone.
4. **Expect your first job to be group B (sysadmin / IT operations / system engineering), not DevOps.** That is the realistic entry point; DevOps and platform roles come after.

## Student and alumni interviews (for the candidate)

Where to find people: LinkedIn search `"<programme name>" "<university>"` filtered to current students and graduates of the last 3 years. University subreddits (r/tuberlin, r/TUDarmstadt, r/Koeln for TH Köln). DAAD Kamerun alumni network. Programme coordinators (ask to be put in touch with current international students). Aim for 2–3 people per Tier 1 programme, including at least one who struggled.

Questions (from PLAN.md, adapted):
1. How did you find your first relevant working-student job, how long did it take, and what was your German level?
2. Roughly how many classmates work in infrastructure-related roles versus unrelated jobs?
3. Did any employer accept English only? Which companies?
4. Did the programme help you get interviews, an internship or a company thesis? How common are company theses?
5. Are there mandatory labs or attendance that clash with a 20h/week job?
6. If your goal were cloud/infrastructure employment, what would you change about the programme?

Log notes in `reports/interviews/<programme>-<date>.md`.

## Open items

- Company-thesis rates and graduate outcomes: UNKNOWN for all programmes (interviews).
- English-language startup channel (LinkedIn/StepStone) missing from the sample. The candidate can do a manual spot check: search "Working Student DevOps / IT Operations / Cloud" per city on LinkedIn and count English ads.
- Unverified Package 2 leads (Frankfurt UAS General CS, Uni Stuttgart CS, etc.) are not yet assessed.
