# Lessons from the Arc 2026 (written 4 Oct 2026, after the race)

## What the result showed (one race, 16 runners: noise-level, so treat as diagnostics, not proof)
Spearman correlation of each pre-race input with finishing order (positive = predictive; 9th-16th unknown, set to a tie):
form +0.69, ground rating +0.71, market price +0.65, distance +0.43, rating +0.34, trainer +0.34, jockey +0.28, trend adjustments +0.14, draw rule -0.07 (actual stall vs finish: -0.11). My composite (+0.53) did WORSE than form or ground alone: the extras (ratings on mixed scales, jockey and trainer judgements, trend and draw adjustments) diluted the stronger inputs.

## Errors that were visible BEFORE the race, now fixed in v16
1. Bay City Roller's fast-ground rating (5): his own Prix Foy run was 2nd on good-to-firm and 'lost little in defeat'; I let his trainer's ground comments override that. Now fast 7, form 7.5.
2. Mixed rating scales: Thundering On used an RPR 132 figure while the other horses used Timeform or other figures; now Timeform 124 like the others.
3. Draw rule: 'stalls 1-8 won 19 of 24 Arcs' is about winners, but I applied a full-strength penalty to every wide runner; stalls 15 and 16 filled 2nd and 3rd. Adjustment halved (+/-0.4/0.25/-0.1/-0.35).

## Things I deliberately did NOT change (a single race is not enough)
Factor weights; the 5yo+ penalty (Kalpana and Friendly Soul, both 5, ran 5th and 4th: could be too harsh, but one race); the defending-colt penalty on Daryz (he won); jockey and trainer scores; the Thundering On form score (she finished 8th: could be over-rated, but nothing in the pre-race evidence was wrong).

## Did it help? Barely (in-sample, so not independent evidence)
| Version | Going | Actual top 7 in my top 7 | Avg model rank of actual 1st-7th | Thundering On rank | Ranks of actual 1st..7th |
|---|---|---|---|---|---|
| v14 | good | 4/7 | 6.3 | 2 | 1 / 11 / 9 / 5 / 3 / 7 / 8 |
| v14 | fast | 4/7 | 6.4 | 2 | 1 / 12 / 9 / 7 / 3 / 5 / 8 |
| v14 | soft | 4/7 | 6.1 | 2 | 1 / 10 / 9 / 5 / 3 / 8 / 7 |
| v16 | good | 4/7 | 6.1 | 3 | 1 / 10 / 6 / 8 / 2 / 7 / 9 |
| v16 | fast | 4/7 | 5.9 | 3 | 1 / 10 / 6 / 9 / 2 / 5 / 8 |
| v16 | soft | 4/7 | 6.3 | 2 | 1 / 10 / 6 / 7 / 3 / 8 / 9 |
Bay City Roller (28/1, 2nd) is still ranked 10th: he was a genuine outsider, and no defensible pre-race input makes him a top-7 pick. Some misses are just racing.

## How to genuinely learn (next steps)
- Freeze each version BEFORE a race (commits are time-stamped) and score it afterwards, across many races, not one.
- Prefer fewer inputs of higher quality: form, ground, distance and market looked most useful here; test dropping the noisy extras on other races.
- Use one consistent rating scale or none; make draw effects race-specific rather than a blanket rule.
- Confirm result facts with two sources (a search summary wrongly reported a winner today).
- Candidates to test out-of-sample: raise form/ground weights, drop the trend adjustments, lighter jockey/trainer weights.
