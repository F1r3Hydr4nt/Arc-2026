# Rules for Claude working in this repo

## Rule 1: update everything after every exchange
After EVERY user prompt -> assistant response, before giving the final reply:
1. Append the exchange to `SESSION_LOG.md` (user message verbatim; assistant work and reply condensed; most recent last).
2. Update `MEMORY.md` (facts, decisions, corrections, current prediction) and `PLAN.md` (tick done items, add new ones) if anything changed.
3. Update any other affected file (`arc_2026_predictor.py`, `README.md`, prediction files).
4. Commit and push to `main` of this repo, and confirm the push succeeded.
Do this even for questions or small clarifications. If a push fails, say so in the reply.

## Rule 2: no bookmaker odds
The user told me to disregard bookmakers' odds. Do not use odds as a model input.

## Rule 3: record every prediction iteration
Each model or input change that alters the prediction gets a new `versions/vN/` folder (`predictor.py` + `PREDICTION.md`) and a row in `PREDICTION_HISTORY.md`.

## Rule 4: pending
Confirm the official Arc draw (due 19:45 GMT Thu 1 Oct 2026) and going, then rerun `arc_2026_predictor.py --draw "Name=stall,..."`.
