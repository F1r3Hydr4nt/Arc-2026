# PLAN — Arc 2026 predictor

## Done
- [x] Identify field and market via web search
- [x] v1 rules-based scorer (`arc_2026_predictor.py`): weights form 30%, market 35%, distance 15%, ground 10%, connections 10%; age/sex trend and Japanese-no-prep adjustments
- [x] v1 prediction produced; move work and memory to this repo

## Next
- [ ] Delete old repo (NOT done: branch delete refused; user to delete repo in GitHub settings)
- [x] Draw rule added (stall<=3 +0.8, <=8 +0.5, 9-12 -0.2, 13+ -0.7); use `--draw "Name=stall,..."`
- [x] Official draw applied (v4), pushed
- [x] Per-horse going scores added (`--going fast|soft`)
- [ ] Confirm official going on Sunday morning and re-run (1 Oct check: dry, good to good-to-firm likely; fast scenario favoured)
- [ ] Replace estimated odds/trainers with real data (needs racecard text; Racing Post is blocked from this environment)
- [ ] Add jockey and trainer Group 1 strike-rate rules
- [ ] Sensitivity test: vary weights, report how stable places 4–7 are
- [ ] After the race, record result in MEMORY.md and score the model

- [x] Saved first prediction (PREDICTION_v1.md) and session log (SESSION_LOG.md)

- [x] v3: bookmaker odds removed, weights rescaled
- [ ] Replace judgement scores with sourced figures (RPRs/Timeform, trainer G1 strike rates) once a racecard is available

- [ ] Clarify with user which Minnie Hauk discrepancy they mean (position change logged in MEMORY.md)

- [x] Standing rule written to CLAUDE.md: update all files + append SESSION_LOG after every exchange

- [x] Reconstructed every prediction iteration (PREDICTION_HISTORY.md + versions/v1..v3)
- [x] Filled in v4 section of PREDICTION_HISTORY.md; fill versions/v4/PREDICTION.md and save versions/v4/predictor.py

- [x] v5 built with Paddy Power prices (Betfair suspended); versions/v5 and v4b saved
- [ ] Replace Paddy Power prices with Betfair back prices when market reopens
- [x] Full audit of all 16 runners (AUDIT.md); v6 and v7 built
- [x] Found Arrow Eagle / Chestnut Rocket / Bright Light 2026 form; jockeys added (v8, v9)
- [x] v10: unknown jockeys neutral, --no-jockey switch
- [x] Ballydoyle jockeys confirmed; v11 built (2 Oct)
- [ ] Find more Arrow Eagle 2026 runs
- [x] Diamond Necklace's Oaks = Prix de Diane (French Oaks)
- [ ] Re-check going: weather evidence conflicting; use official France Galop update Fri/Sat

- [x] 2 Oct 15:00 UTC jockey check done (v11)
- [x] Race-day going and jockeys checked (4 Oct 10:58 UTC): bon souple, dry, fast scenario; jockeys unchanged
- [x] Race-morning prices refreshed (v13)
- [ ] After the race: record result in MEMORY.md and score the model (all versions)

- [ ] 1 Oct 21:30 UTC: Betfair price re-check (trig_01AndsB93dHaoRXSd8J9wr3b); Betfair URL is blocked, needs user screenshot

- [x] v12: ratings + head-to-heads
- [ ] Find ratings for Minnie Hauk, Friendly Soul, Admire Terra; Kalpana's King George figure; any speed figures/sectionals

- [x] v14: odds-free race-morning model

## Workflow rule
Update MEMORY.md and PLAN.md and push to this repo after every change.

## New phase (4 Oct): learning + retarget (awaiting user's choice)
- [x] Learn from Arc misses: LESSONS.md and v16 (in-sample)
- [x] Forêt attempt: not testable (result known, data thin); scored profiles on the Arc instead (SCORE_LOG.md)
- [ ] Out-of-sample test on a FUTURE race: obtain full racecard before the off, freeze all profiles by commit, score after, append to SCORE_LOG.md; update hypotheses ledger
- [ ] Clarify target: the user's '3.50' race has been run (True Love won per user; likely the Prix de la Foret). Ask what they want next (post-race backtest, or a different race)
- [ ] Fix known weaknesses before reuse: ground ratings not to rely on trainer comments (Bay City Roller), softer stall-16 penalty, include more places evidence
- [x] Arc result recorded and models scored (RESULT_arc_2026.md)

- [ ] Score 18:05 Longchamp handicap frozen predictions after the race (second-source result).
