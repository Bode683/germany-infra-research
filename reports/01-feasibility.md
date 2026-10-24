# Package 1 — Feasibility and Route B test

Date: 2026-10-24. Source IDs refer to `sources.csv`.

## Bottom line

1. **Route A (master's in Germany) is the main route. Route B (employment-first) is not viable now.** Route B fails on experience (3 months, zero infra), on the embassy's queue (Chancenkarte appointments in Yaoundé: over 1 year, S006) and on access: Chancenkarte holders cannot take working-student jobs, the main entry door for juniors.
2. **The binding constraint is visa timing, not money or admission.** Yaoundé lists regular student-visa appointments at **up to one year**, waitlist only (S006), with staffing-related processing delays on top (S007). For an October 2027 start, the waitlist registration has to happen now, not after admission.
3. **Money is no longer a binding constraint** — unless the programme charges TUM-level tuition. Savings plus the brother's possible Verpflichtungserklärung cover a 3- or 4-semester programme in a tuition-free state without relying on a job.
4. **Admission is borderline on grade.** 3.0/4.0 with a 2.0 pass mark converts to exactly **2.5** on the German scale. Programmes with a 2.5 cut-off are just reachable; anything stricter, or ranked competitively, is a real risk.

## 1. Grade conversion

Modified Bavarian formula (S012): `1 + 3 × (4.0 − 3.0) / (4.0 − 2.0) = 2.5`.

- 2.5 is the most common cut-off at HAW master's programmes ("2.5 or better") → eligible, with zero margin.
- If a university or uni-assist computes from a weighted module average, or uses a different Nmin for the Cameroonian system, the result could move either way. **UNKNOWN until uni-assist or a university issues a VPD or evaluation.**
- Programmes with competitive selection (TUM aptitude assessment, ranked lists) will weigh 2.5 against stronger applicants. Treat them as reach options.
- **Not yet verified: anabin status of the University of Bamenda (H+?) and of the degree type.** anabin is a JavaScript app that could not be queried from here. The candidate should check it directly (anabin.kmk.org → Institutionen → Kamerun). If not H+, admission and every visa route get harder.

## 2. Credits

~257 credits, ~100 in CS. If the Cameroonian credit is ECTS-equivalent (LMD systems usually are, unverified for this transcript), this exceeds both 210 and 240 → **3-semester master's programmes are open.** Confirm with the first uni-assist evaluation.

## 3. Visa from Cameroon

| Item | Finding | Source |
|---|---|---|
| Visa needed | Yes, national visa | Auswärtiges Amt |
| Appointment wait, regular study | up to 1 year, waitlist only | S006 |
| Appointment wait, Chancenkarte | over 1 year | S006 |
| Appointment wait, skilled-worker job | up to 1 month | S006 |
| Processing | delays due to staffing; no remonstration since 1 Jul 2025 → a refusal means a new application or a lawsuit | S007 |
| Channel | Auslandsportal; VFS Global from Dec 2025 (low confidence) | S008 |
| Funds | €11,904/year (2026) blocked account, **or** Verpflichtungserklärung from a person resident in Germany | S001, S005 |

**Implication:** for an October 2027 intake, the appointment has to come by roughly July–August 2027 at the latest. A one-year queue means **registering on the Yaoundé waitlist (category "Studium – Regulär") now.** Whether you can register before having an admission letter, and what happens if the appointment comes before the admission letter, must be confirmed on the embassy site or through the contact form. Register only once, in the right category: wrong-category bookings are cancelled, and a cancellation can trigger a 3-month block (S006, S007).

**Fallback if the visa misses October 2027:** defer to summer semester 2028 where programmes allow it, or reapply for winter 2028. That costs 6–12 months. Prefer programmes with both summer and winter intakes.

## 4. Cost model

Assumptions (expected scenario): living costs €1,150/month (official minimum €992/month; mid-sized city reality is higher); semester contribution ~€300 (assumption, range ~€150–400); one-off setup €2,500 (flight, deposit, furniture, visa); savings continue at €600/month during study (candidate-stated). Funds at arrival ≈ €18,000 + 11 × €600 ≈ **€24,600**.

Net monthly burn without any job = living − €600.

| Scenario | Programme | Tuition | Net need over programme | Covered by €24.6k? |
|---|---|---|---|---|
| Expected, €1,150/mo | 3 sem (18 mo), tuition-free | €0 | 18 × 550 + 900 + 2,500 ≈ **€13,300** | Yes, ~€11k left for job search |
| Expected | 4 sem (24 mo), tuition-free | €0 | 24 × 550 + 1,200 + 2,500 ≈ **€16,900** | Yes, ~€7.7k left |
| Adverse, €1,400/mo (Munich/Frankfurt) | 4 sem, tuition-free | €0 | 24 × 800 + 1,200 + 2,500 ≈ **€22,900** | Barely; no buffer for job search |
| Expected | 4 sem, Baden-Württemberg | €6,000 | ≈ **€22,900** | Barely |
| Expected | 4 sem, TUM | €16,000–24,000 | ≈ **€33,000–41,000** | **No** — needs sponsor cash |

**Blocked account vs. Verpflichtungserklärung:** a blocked account locks €11,904 of the €24.6k and releases it monthly, so the cash still pays for living costs, it just isn't liquid. A Verpflichtungserklärung from the brother keeps the savings free. It is a legally binding commitment for him: it covers your living costs and can include public costs such as deportation, typically for up to 5 years. His local Ausländerbehörde decides whether his income qualifies. Likely for a physician's income, but that is an assumption until they decide. **He should understand the liability before signing.**

**Verdict:** under expected assumptions, any tuition-free programme is fundable without a job. Cost stops being a differentiator except for TUM-type tuition. **Recommendation: cut the "cost" weight in `weights.md` from 20% to 10% and move 10% to job access or industry integration.** TUM-type tuition becomes a filter, not a score.

## 5. Route B — employment-first

| Route | Requirements vs. profile | Verdict |
|---|---|---|
| Chancenkarte (S009, S010) | Points: German B1 = 2 (once certified), native English = 1, age ≤35 = 2 (**age UNKNOWN**), shortage occupation = 1 (CS likely, unverified), experience = 0 (needs 2+ years), partial recognition = 0 unless applied for. Reaches 6 points only if every conditional item holds. Yaoundé wait: **over 1 year**. One-year card, 20 h/week side jobs, **no working-student status**. | **Not viable as a primary route.** Legally possible, practically weak: slower to get than a student visa and gives worse job access. |
| EU Blue Card, new-entrant rate €45,934 (S011) | Needs a job offer from Germany before leaving Cameroon. 3 months full-stack, no infra, no German job history. | **Not viable now.** No evidence that German employers hire juniors with this profile from abroad. Package 3's vacancy data will test this indirectly. |
| Skilled-worker visa §18b | Same problem: needs an offer. | Not viable now. |
| Remote job abroad → relocation | Possible in theory; no evidence base. | Speculative. Not a plan. |

**Why Route A wins structurally, not just by elimination:** a student permit gives 20 h/week of legal work, access to working-student jobs (the main junior entry point), a German degree that skips recognition problems, and then an **18-month job-search permit** with unrestricted work (S003). Route B offers none of that to someone with 3 months' experience.

**Deviation from PLAN.md:** the planned 15–20-vacancy sample for Route B was skipped. Route B fails on structural grounds (queue, experience, no student status), so a vacancy sample would not change the verdict. Also, the BA Jobsuche API is blocked by this environment's network policy (S015). Vacancy sampling moves to Package 3, which will need the network allowlist fixed.

## 6. Preparation gaps the candidate controls

1. **Register on the Yaoundé student-visa waitlist now** (after confirming the rules for registering before admission).
2. **Check anabin** for the University of Bamenda and the degree (H+ / degree entry).
3. **German:** book a recognised B1 exam (Goethe, telc, ÖSD) for no later than ~spring 2027. An uncertified level counts for nothing on applications or for Chancenkarte points.
4. **English:** the EMI letter is accepted by many programmes, not all. Decide in Package 2 whether an IELTS is needed.
5. **Infra skills:** 3 months full-stack with no infra makes working-student infra roles hard. Before arrival: Linux administration, networking fundamentals, one cloud provider's basics, Docker, CI/CD, Terraform, 2–3 public projects. German still comes first.

## Is Route A justified enough to continue?

Yes. Continue to Package 2 with these updated hard filters:
- Non-EU tuition ≤ €1,500/semester (Baden-Württemberg is OK; TUM-type tuition excluded unless the sponsor commits cash).
- Grade requirement ≤ 2.5 accepted; flag programmes with competitive ranking as reach.
- Prefer 3-semester programmes (cheaper, faster) and programmes with a summer intake as a visa-delay fallback.
- English-taught, or German-taught at B1 or below.
