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

## v8 and v9: jockeys added (21:0x UTC, 1 Oct 2026)
| Pos | v6 fast | v8 fast (+jockeys, no odds) | v7 fast | v9 fast (+jockeys, odds) | v8 soft | v9 soft |
|---|---|---|---|---|---|---|
| 1 | Daryz 9.65 | Daryz 9.60 | Daryz 9.76 | Daryz 9.73 | Daryz 9.60 | Daryz 9.73 |
| 2 | Kalpana 8.86 | Thundering On 8.96 | Kalpana 8.02 | Thundering On 7.98 | Thundering On 8.96 | Thundering On 7.98 |
| 3 | Thundering On 8.85 | Kalpana 8.75 | Thundering On 7.89 | Kalpana 7.95 | Kalpana 8.47 | Kalpana 7.73 |
| 4 | Benvenuto Cellini 8.26 | Benvenuto Cellini 8.35 | Maltese Cross 7.42 | Maltese Cross 7.46 | Benvenuto Cellini 8.35 | Benvenuto Cellini 7.26 |
| 5 | Maltese Cross 8.18 | Maltese Cross 8.22 | Benvenuto Cellini 7.19 | Benvenuto Cellini 7.26 | Friendly Soul 8.00 | Maltese Cross 7.13 |
| 6 | Friendly Soul 7.64 | Friendly Soul 7.72 | Varandir 6.54 | Varandir 6.51 | Maltese Cross 7.80 | Friendly Soul 6.68 |
| 7 | Diamond Necklace 7.57 | Diamond Necklace 7.61 | Diamond Necklace 6.46 | Diamond Necklace 6.49 | Minnie Hauk 7.56 | Varandir 6.51 |
Effect of jockeys: small. Thundering On (Boudot, an Arc winner) edges ahead of Kalpana (Keane) in both new versions; otherwise the order is unchanged. Jockey scores are judgement-based, and three Ballydoyle rides are unconfirmed.

## v10: unknown jockeys neutral (user correction: jockeys not yet known)
| Pos | v9 fast | v10 fast | v10 fast, no jockey | v10 soft |
|---|---|---|---|---|
| 1 | Daryz 9.73 | Daryz 9.73 | Daryz 9.65 | Daryz 9.73 |
| 2 | Thundering On 7.98 | Thundering On 7.98 | Kalpana 7.95 | Thundering On 7.98 |
| 3 | Kalpana 7.95 | Kalpana 7.95 | Thundering On 7.90 | Kalpana 7.73 |
| 4 | Maltese Cross 7.46 | Maltese Cross 7.46 | Maltese Cross 7.37 | Benvenuto Cellini 7.18 |
| 5 | Benvenuto Cellini 7.26 | Benvenuto Cellini 7.18 | Benvenuto Cellini 7.18 | Maltese Cross 7.13 |
| 6 | Varandir 6.51 | Varandir 6.51 | Varandir 6.61 | Friendly Soul 6.68 |
| 7 | Diamond Necklace 6.49 | Friendly Soul 6.46 | Diamond Necklace 6.41 | Varandir 6.51 |
Effect: removing the assumed 8s for the Ballydoyle trio costs Diamond Necklace and Cellini a little; Friendly Soul edges back into the top 7 on fast ground. Thundering On vs Kalpana is a 0.05 coin-flip once jockeys are removed.

## v11: Ballydoyle jockeys confirmed (2 Oct 15:00 UTC routine)
| Pos | v10 fast | v11 fast | v11 fast, no jockey | v10 soft | v11 soft |
|---|---|---|---|---|---|
| 1 | Daryz 9.73 | Daryz 9.73 | Daryz 9.67 | Daryz 9.73 | Daryz 9.73 |
| 2 | Thundering On 7.98 | Thundering On 7.98 | Kalpana 7.97 | Thundering On 7.98 | Thundering On 7.98 |
| 3 | Kalpana 7.95 | Kalpana 7.95 | Thundering On 7.92 | Kalpana 7.73 | Kalpana 7.73 |
| 4 | Maltese Cross 7.46 | Maltese Cross 7.46 | Maltese Cross 7.39 | Benvenuto Cellini 7.18 | Benvenuto Cellini 7.35 |
| 5 | Benvenuto Cellini 7.18 | Benvenuto Cellini 7.35 | Benvenuto Cellini 7.20 | Maltese Cross 7.13 | Maltese Cross 7.13 |
| 6 | Varandir 6.51 | Varandir 6.51 | Varandir 6.63 | Friendly Soul 6.68 | Friendly Soul 6.68 |
| 7 | Friendly Soul 6.46 | Diamond Necklace 6.49 | Diamond Necklace 6.43 | Varandir 6.51 | Varandir 6.51 |
Effect: Moore on Cellini lifts him a little; Soumillon puts Diamond Necklace back to 7th on fast ground only. With Racing Post/Coral's post-jockey 14/1s for DN and Cellini, Friendly Soul retakes 7th on fast ground.

## Rank tracker: Thundering On and Minnie Hauk across versions (user question, 2 Oct)
Official draw applied from v4 on; v1-v3 had no draw. Fast / soft ground. v1 had no ground scenarios (Minnie Hauk 7th, Thundering On 12th, from the original run).
| Ver | Uses odds? | Thundering On | Minnie Hauk |
|---|---|---|---|
| v1 | yes (guessed) | 12th | 7th |
| v2 | yes | outside top 9 | 6th / 6th |
| v3 | no | outside top 9 | 5th / 5th |
| v4 | no | outside top 9 (mis-specified) | 7th / 7th |
| v4b | no | **3rd / 2nd** (data error fixed) | 8th / 8th |
| v5 | yes | 3rd / 3rd | 8th / 8th |
| v6 | no | 3rd / 2nd | 8th / 7th |
| v7 | yes | 3rd / 2nd | 9th / 9th |
| v8 | no | 2nd / 2nd | 8th / 7th |
| v9-v11 | yes | 2nd / 2nd | 9th / 9th |
Reading: Thundering On entered the top 7 at v4b, a no-odds version, because her inputs were corrected (3yo Oaks-winning filly, form 8.5), not because of the market weight. The 8/1 price on the Paddy Power screenshot is what tipped me off that I had mis-modelled her. Minnie Hauk left the top 7 on fast ground at v4b (pushed down by Thundering On's correction and by Varandir's stall 4) and on soft ground once the market (20/1) was added in v7+. Her own score never changed after v3.

## v12: ratings + head-to-heads (2 Oct)
| Pos | v11 fast | v12 fast | v12 soft |
|---|---|---|---|
| 1 | Daryz 9.73 | Daryz 9.70 | Daryz 9.70 |
| 2 | Thundering On 7.98 | Thundering On 7.94 | Thundering On 7.94 |
| 3 | Kalpana 7.95 | Kalpana 7.87 | Kalpana 7.67 |
| 4 | Maltese Cross 7.46 | Benvenuto Cellini 7.12 | Benvenuto Cellini 7.12 |
| 5 | Benvenuto Cellini 7.35 | Maltese Cross 7.00 | Maltese Cross 6.70 |
| 6 | Varandir 6.51 | Varandir 6.56 | Varandir 6.56 |
| 7 | Diamond Necklace 6.49 | Diamond Necklace 6.30 | Friendly Soul 6.44 |
Effect: Maltese Cross and Cellini swap on fast ground (his Timeform 124p equals Maltese Cross's rating, and stall 1 vs 11 counts); Minnie Hauk stays 8th. Her missing rating is the main uncertainty (130 would put her 7th).

## v13: race-day refresh (4 Oct 11:45 UTC), going GOOD
| Pos | v12 fast | v13 fast | v13 good | v13 soft |
|---|---|---|---|---|
| 1 | Daryz 9.70 | Daryz 9.70 | Daryz 9.70 | Daryz 9.70 |
| 2 | Thundering On 7.94 | Kalpana 8.05 | Kalpana 7.95 | Thundering On 7.94 |
| 3 | Kalpana 7.87 | Thundering On 7.94 | Thundering On 7.94 | Kalpana 7.85 |
| 4 | Benvenuto Cellini 7.12 | Benvenuto Cellini 7.02 | Benvenuto Cellini 7.02 | Benvenuto Cellini 7.02 |
| 5 | Maltese Cross 7.00 | Maltese Cross 6.77 | Maltese Cross 6.62 | Varandir 6.56 |
| 6 | Varandir 6.56 | Varandir 6.56 | Varandir 6.56 | Maltese Cross 6.47 |
| 7 | Diamond Necklace 6.30 | Minnie Hauk 6.35 | Minnie Hauk 6.35 | Minnie Hauk 6.35 |
Changes: Kalpana's shortening to 4/1 takes her back above Thundering On on fast/good ground; Minnie Hauk returns to 7th on all three (16/1 from 20/1); Diamond Necklace (14/1, stall 16) drops to 8th-9th.

## v14: v13 without prices (4 Oct)
| Pos | v13 good (with prices) | v14 good (no prices) | v14 fast | v14 soft |
|---|---|---|---|---|
| 1 | Daryz 9.70 | Daryz 9.57 | Daryz 9.57 | Daryz 9.57 |
| 2 | Kalpana 7.95 | Thundering On 8.91 | Thundering On 8.91 | Thundering On 8.91 |
| 3 | Thundering On 7.94 | Kalpana 8.44 | Kalpana 8.57 | Kalpana 8.32 |
| 4 | Benvenuto Cellini 7.02 | Benvenuto Cellini 8.18 | Benvenuto Cellini 8.18 | Benvenuto Cellini 8.18 |
| 5 | Maltese Cross 6.62 | Friendly Soul 7.58 | Maltese Cross 7.65 | Friendly Soul 7.70 |
| 6 | Varandir 6.56 | Minnie Hauk 7.53 | Minnie Hauk 7.53 | Minnie Hauk 7.53 |
| 7 | Minnie Hauk 6.35 | Maltese Cross 7.46 | Friendly Soul 7.45 | Varandir 7.45 |
Without prices: Thundering On ranks 2nd on every going (Kalpana's shortening to 4/1 no longer lifts her); Friendly Soul (33/1) and Minnie Hauk climb; Maltese Cross (7/1, stall 11) falls to 5th-8th depending on ground; Varandir slips. Places 5-9 are within ~0.5 points.

## v15: betting-without prices (4 Oct)
| Pos | v13 good | v14 good (no prices) | v15 good | v15 fast | v15 soft |
|---|---|---|---|---|---|
| 1 | Daryz 9.70 | Daryz 9.57 | Daryz 9.70 | Daryz 9.70 | Daryz 9.70 |
| 2 | Kalpana 7.95 | Thundering On 8.91 | Kalpana 7.95 | Kalpana 8.05 | Thundering On 7.86 |
| 3 | Thundering On 7.94 | Kalpana 8.44 | Thundering On 7.86 | Thundering On 7.86 | Kalpana 7.85 |
| 4 | Benvenuto Cellini 7.02 | Benvenuto Cellini 8.18 | Benvenuto Cellini 6.94 | Benvenuto Cellini 6.94 | Benvenuto Cellini 6.94 |
| 5 | Maltese Cross 6.62 | Friendly Soul 7.58 | Maltese Cross 6.48 | Maltese Cross 6.63 | Varandir 6.40 |
| 6 | Varandir 6.56 | Minnie Hauk 7.53 | Varandir 6.40 | Varandir 6.40 | Minnie Hauk 6.35 |
| 7 | Minnie Hauk 6.35 | Maltese Cross 7.46 | Minnie Hauk 6.35 | Minnie Hauk 6.35 | Friendly Soul 6.34 |
Betting-without prices make almost no difference versus v13: the converted win-equivalent prices are only a little longer, Cellini still holds 4th on his stall 1, Moore and rating 124p despite a 9/1 BW (about 22/1 win-equivalent) price.
