# Prediction history — every iteration (reconstructed 2026-10-01 14:08 UTC)

Each version has its own folder in `versions/` (predictor.py + PREDICTION.md) and was re-run to reproduce these numbers.
The draw-announcement revision (v4) is the one expected to move things most; see the bottom.

| Version | When | What changed | Script |
|---|---|---|---|
| v1 | 13:5x UTC | First model: form 30 / market 35 / distance 15 / ground 10 / connections 10; guessed odds; no ground or draw scenarios | `versions/v1/predictor.py` |
| v2 | 13:57 UTC | Corrected ages/trainers/odds (Kalpana 5yo, Friendly Soul ~25/1 and 5yo+, Bay City Roller = G Scott, Varandir = Graffard); added fast/soft ground and draw rule | `versions/v2/predictor.py` |
| v3 | ~14:00 UTC | User ordered bookmaker odds removed: weights form 46 / distance 23 / ground 15 / connections 15; form tie-break | `versions/v3/predictor.py` (= current `arc_2026_predictor.py`) |
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

## v4: draw-announcement revision (DONE, 19:48 GMT 1 Oct 2026). Full detail: versions/v4/PREDICTION.md
Official draw: 1 Benvenuto Cellini, 2 Chestnut Rocket, 3 Thundering On, 4 Varandir, 5 Daryz, 6 Kalpana, 7 Friendly Soul, 8 Bright Light, 9 Saddadd, 10 Minnie Hauk, 11 Maltese Cross, 12 Admire Terra, 13 Meisho Tabaru, 14 Arrow Eagle, 15 Bay City Roller, 16 Diamond Necklace.

| Pos | v3 fast (no draw) | v4 fast (draw) | v4 soft (draw) |
|---|---|---|---|
| 1 | Daryz 8.92 | Daryz 9.42 | Daryz 9.42 |
| 2 | Maltese Cross 8.38 | Kalpana 8.86 | Kalpana 8.56 |
| 3 | Kalpana 8.36 | Benvenuto Cellini 8.26 | Benvenuto Cellini 8.26 |
| 4 | Benvenuto Cellini 7.46 | Maltese Cross 8.18 | Friendly Soul 7.79 |
| 5 | Minnie Hauk 7.46 | Friendly Soul 7.79 | Maltese Cross 7.73 |
| 6 | Friendly Soul 7.29 | Varandir 7.43 | Varandir 7.43 |
| 7 | Diamond Necklace 6.97 | Minnie Hauk 7.26 | Minnie Hauk 7.26 |

Biggest changes: Maltese Cross falls from 2nd to 4th/5th (stall 11); Kalpana is promoted to 2nd; Cellini rises to 3rd (stall 1); Varandir (stall 4) enters the top 7; Diamond Necklace (stall 16) drops out.

## v4b and v5 (added 20:1x UTC, 1 Oct 2026)
Top 7 with the official draw:

| Pos | v4 fast | v4b fast | v5 fast | v4b soft | v5 soft |
|---|---|---|---|---|---|
| 1 | Daryz 9.42 | Daryz 9.42 | Daryz 9.58 | Daryz 9.42 | Daryz 9.58 |
| 2 | Kalpana 8.86 | Kalpana 8.86 | Kalpana 8.02 | Thundering On 8.62 | Kalpana 7.78 |
| 3 | Benvenuto Cellini 8.26 | Thundering On 8.62 | Thundering On 7.71 | Kalpana 8.56 | Thundering On 7.71 |
| 4 | Maltese Cross 8.18 | Benvenuto Cellini 8.26 | Maltese Cross 7.42 | Benvenuto Cellini 8.26 | Benvenuto Cellini 7.19 |
| 5 | Friendly Soul 7.79 | Maltese Cross 8.18 | Benvenuto Cellini 7.19 | Friendly Soul 7.79 | Maltese Cross 7.06 |
| 6 | Varandir 7.43 | Friendly Soul 7.79 | Varandir 6.54 | Maltese Cross 7.73 | Varandir 6.54 |
| 7 | Minnie Hauk 7.26 | Varandir 7.43 | Friendly Soul 6.51 | Varandir 7.43 | Friendly Soul 6.51 |

Biggest change of this round: a data error, not the market. Thundering On had been mis-specified (colt, form 5.0, never researched); corrected she jumps into the top 3. The market then pushes Maltese Cross up (stall 11 matters less when priced 5/1) and Friendly Soul/Minnie Hauk down (20/1).

## v6 and v7: full input audit (20:3x UTC, 1 Oct 2026). Detail in AUDIT.md
| Pos | v5 fast | v6 fast (audited, no odds) | v7 fast (audited + odds) | v6 soft | v7 soft |
|---|---|---|---|---|---|
| 1 | Daryz 9.58 | Daryz 9.65 | Daryz 9.76 | Daryz 9.65 | Daryz 9.76 |
| 2 | Kalpana 8.02 | Kalpana 8.86 | Kalpana 8.02 | Thundering On 8.85 | Thundering On 7.89 |
| 3 | Thundering On 7.71 | Thundering On 8.85 | Thundering On 7.89 | Kalpana 8.56 | Kalpana 7.78 |
| 4 | Maltese Cross 7.42 | Benvenuto Cellini 8.26 | Maltese Cross 7.42 | Benvenuto Cellini 8.26 | Benvenuto Cellini 7.19 |
| 5 | Benvenuto Cellini 7.19 | Maltese Cross 8.18 | Benvenuto Cellini 7.19 | Friendly Soul 7.94 | Maltese Cross 7.06 |
| 6 | Varandir 6.54 | Friendly Soul 7.64 | Varandir 6.54 | Maltese Cross 7.73 | Friendly Soul 6.63 |
| 7 | Friendly Soul 6.51 | Diamond Necklace 7.57 | Diamond Necklace 6.46 | Minnie Hauk 7.49 | Varandir 6.54 |
Effect of the audit: the top of the order held (Daryz, Kalpana/Thundering On, then Cellini/Maltese Cross); the bottom of the top 7 moved. Diamond Necklace re-enters the top 7 on fast ground despite stall 16; Friendly Soul's soft/fast split widened; Varandir slips out of the top 7 without the market.
