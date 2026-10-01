# PLAN — Arc 2026 predictor

## Done
- [x] Identify field and market via web search
- [x] v1 rules-based scorer (`arc_2026_predictor.py`): weights form 30%, market 35%, distance 15%, ground 10%, connections 10%; age/sex trend and Japanese-no-prep adjustments
- [x] v1 prediction produced; move work and memory to this repo

## Next
- [ ] Delete old repo (NOT done: branch delete refused; user to delete repo in GitHub settings)
- [ ] Confirm official draw (stalls) and add a draw rule (stall <= 8 bonus)
- [ ] Confirm going on the day; add per-horse going rule
- [ ] Replace estimated odds/trainers with real data (needs racecard text; Racing Post is blocked from this environment)
- [ ] Add jockey and trainer Group 1 strike-rate rules
- [ ] Sensitivity test: vary weights, report how stable places 4–7 are
- [ ] After the race, record result in MEMORY.md and score the model

## Workflow rule
Update MEMORY.md and PLAN.md and push to this repo after every change.
