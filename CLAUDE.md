# Germany infrastructure-career research

Evidence-led decision campaign: find the best risk-adjusted route into cloud/infrastructure employment in Germany. Read `PLAN.md` for the method, `STATE.md` for where the campaign stands, `profile.md` for the candidate's constraints.

## Rules for every session and scheduled run

- Do only the work package named as next in `STATE.md`. Stop at its stop condition.
- If `profile.md` has a required field marked `UNKNOWN` that the current package depends on, or `weights.md` is not `LOCKED` when scoring is required, stop and write the blocking questions to `STATE.md`.
- Admissions, tuition, deadlines and visa rules: official sources only (university pages, module handbooks, admission regulations, DAAD, Hochschulkompass, make-it-in-germany.com, auswaertiges-amt.de, BAMF). Third-party blogs are leads, not evidence.
- Log every material claim in `sources.csv` with URL, access date, evidence type (official / vacancy / forum / interview / data), confidence (high / medium / low) and limitation.
- Unknown stays `UNKNOWN`. Never fill a gap with a plausible guess. Never invent employment probabilities.
- Forum posts identify risks to investigate; they are not base rates.
- Timestamp every deadline and vacancy. Both go stale.
- Be blunt in reports. Flag weak programmes and weak assumptions directly, including the candidate's.
- Commit work with a clear message and push to `main` at the end of each run.
