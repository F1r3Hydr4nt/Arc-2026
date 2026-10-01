# Prediction history — every iteration (reconstructed 2026-10-01 14:08 UTC)

Each version's script is saved in `history/` and was re-run to reproduce these numbers.
The draw-announcement revision (v4) is the one expected to move things most; see the bottom.

| Version | When | What changed | Script |
|---|---|---|---|
| v1 | 13:5x UTC | First model: form 30 / market 35 / distance 15 / ground 10 / connections 10; guessed odds; no ground or draw scenarios | `history/predictor_v1.py` |
| v2 | 13:57 UTC | Corrected ages/trainers/odds (Kalpana 5yo, Friendly Soul ~25/1 and 5yo+, Bay City Roller = G Scott, Varandir = Graffard); added fast/soft ground and draw rule | `history/predictor_v2.py` |
| v3 | ~14:00 UTC | User ordered bookmaker odds removed: weights form 46 / distance 23 / ground 15 / connections 15; form tie-break | `history/predictor_v3.py` (= current `arc_2026_predictor.py`) |
| v4 | due 19:55 UTC | Official draw + going applied | pending |

## Top 7 by version (draw NOT applied unless stated)

| Pos | v1 | v2 fast | v2 soft | v3 fast | v3 soft |
|---|---|---|---|---|---|
| 1 | Daryz 9.55 | Daryz 9.25 | Daryz 9.25 | Daryz 8.92 | Daryz 8.92 |
| 2 | Maltese Cross 7.25 | Maltese Cross 7.25 | Maltese Cross 6.95 | Maltese Cross 8.38 | Kalpana 8.06 |
| 3 | Kalpana 6.85 | Kalpana 6.55 | Kalpana 6.35 | Kalpana 8.36 | Maltese Cross 7.93 |
| 4 | Friendly Soul 5.79 | Diamond Necklace 5.72 | Diamond Necklace 5.72 | Benvenuto Cellini 7.46 | Benvenuto Cellini 7.46 |
| 5 | Diamond Necklace 5.72 | Benvenuto Cellini 5.47 | Benvenuto Cellini 5.47 | Minnie Hauk 7.46 | Minnie Hauk 7.46 |
| 6 | Benvenuto Cellini 5.47 | Minnie Hauk 5.36 | Minnie Hauk 5.36 | Friendly Soul 7.29 | Bay City Roller 7.31 |
| 7 | Minnie Hauk 5.36 | Friendly Soul 5.02 | Bay City Roller 5.17 | Diamond Necklace 6.97 | Friendly Soul 7.29 |
| 8th | Bay City Roller 5.27 | Varandir 5.01 | Friendly Soul 5.02 | Varandir 6.93 | Diamond Necklace 6.97 |

## Rumoured draw test (UNCONFIRMED: Daryz 1, Kalpana 9, Maltese Cross 13; fast ground)
- v2 + rumour: Daryz 10.05, Maltese Cross 6.55, Kalpana 6.35, Diamond Necklace 5.72, Cellini 5.47, Minnie Hauk 5.36, Friendly Soul 5.02
- v3 + rumour: Daryz 9.72, **Kalpana 8.16, Maltese Cross 7.68** (swap), Cellini 7.46, Minnie Hauk 7.46, Friendly Soul 7.29, Diamond Necklace 6.97
Under v3 the rumoured wide draw (13) for Maltese Cross is enough to drop him below Kalpana.

## Biggest movers across versions
- Friendly Soul: 4th (v1) -> 7th (v2) -> 6th/7th (v3). Cause: guessed 13/1 replaced by ~25/1, 5yo+ penalty, then odds removed.
- Diamond Necklace: 5th -> 4th -> 7th/8th. Cause: her 12f ability is unproven; the market had been propping her up.
- Minnie Hauk: 7th -> 6th -> 5th. Own score fell/rose only relative to others (5.36 in v1/v2).
- Maltese Cross vs Kalpana: swap on soft ground in v3 and under the rumoured draw.

## v4: draw-announcement revision (TO FILL IN after 19:45 GMT Thu 1 Oct)
- Official stalls: _pending_
- Official going: _pending_
- Command: `python3 arc_2026_predictor.py --draw "Name=stall,..."` for fast and soft
- Result and what moved: _pending_
