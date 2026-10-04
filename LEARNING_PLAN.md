# Plan to learn properly (saved 4 Oct 2026; mirrors the section in MEMORY.md)
1. Freeze predictions for several model profiles before the race, commit and push first, never edit afterwards.
2. Score afterwards: winner, overlap of actual top 3/4 with my top 3/4, average rank of the placed horses; compare with baselines (market-only, form-only, ground-only).
3. One race is noise: keep SCORE_LOG.md across races; change a weight or rule only with support from several races plus a pre-race reason.
4. Confirm results with two sources.
5. Consistent inputs: one rating scale, ground ratings from the horse's own runs, race-specific draw effects.
6. Keep data honest: label judgements, record unknowns, note leakage.
7. Test candidate simplifications on every race (no age/trend adjustments, no draw, no jockey/trainer, reweighted form/ground).

## Status after the Forêt attempt (4 Oct 2026)
- Step 1-2 (freeze, score) can only be done properly for a race whose result is unknown when I build the model AND whose inputs I can get for every runner. The Forêt failed both tests (result known, data thin), so no Forêt test was run.
- Delivered instead: `learning/score_profiles.py` (re-scores simplified profiles and baselines against a known order) and SCORE_LOG.md with a hypotheses ledger. First entry: the Arc.
- Next real test: pick a future race, paste in or fetch the full racecard BEFORE the off, freeze all profiles (market-only, form-only, ground-only, core, core+market, full, no-extras) by committing, then score and append to SCORE_LOG.md.
