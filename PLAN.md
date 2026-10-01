# PLAN — Arc 2026 predictor

## Done
- [x] Identify field and market via web search
- [x] v1 rules-based scorer (`arc_2026_predictor.py`): weights form 30%, market 35%, distance 15%, ground 10%, connections 10%; age/sex trend and Japanese-no-prep adjustments
- [x] v1 prediction produced; move work and memory to this repo

## Next
- [ ] Delete old repo (NOT done: branch delete refused; user to delete repo in GitHub settings)
- [x] Draw rule added (stall<=3 +0.8, <=8 +0.5, 9-12 -0.2, 13+ -0.7); use `--draw "Name=stall,..."`
- [ ] AT 19:45 GMT THU 1 OCT: confirm official draw and run with `--draw`; push result
- [x] Per-horse going scores added (`--going fast|soft`)
- [ ] Confirm official going on Sunday morning and re-run
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
- [ ] Fill in v4 section of PREDICTION_HISTORY.md after the draw; fill versions/v4/PREDICTION.md and save versions/v4/predictor.py

## Workflow rule
Update MEMORY.md and PLAN.md and push to this repo after every change.
