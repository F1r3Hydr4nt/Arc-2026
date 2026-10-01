# MEMORY — Arc 2026 project

Standing instruction from the user: **save memory (this file) and plan (PLAN.md) and push every update to this repo.**

## Task
Predict the first 6–7 places of the 2026 Qatar Prix de l'Arc de Triomphe (Longchamp, Sun 4 Oct 2026, Racing Post race 921493) using a simple, transparent rules-based decision system built from first principles.

## Facts gathered (via web search only; page fetches were blocked)
- 16 runners declared: Daryz, Saddadd, Chestnut Rocket, Admire Terra, Meisho Tabaru, Arrow Eagle, Bay City Roller, Minnie Hauk, Kalpana, Friendly Soul, Varandir, Benvenuto Cellini, Bright Light, Maltese Cross, Thundering On, Diamond Necklace.
- Odds (approx): Daryz 7/4, Maltese Cross 9/2, Kalpana 7/1, Diamond Necklace 8/1, Benvenuto Cellini 16/1, Minnie Hauk 16–20/1, Bay City Roller 16–25/1.
- Daryz: 2025 Arc winner (trainer Graffard), won 2026 Prix Foy, beat Bay City Roller; only one defeat since (3rd Prince of Wales's).
- Maltese Cross (Haggas): Derby 2nd, Grand Prix de Paris, Great Voltigeur.
- Kalpana (Balding): King George, Yorkshire Oaks; gets 3lb from Daryz.
- Diamond Necklace (O'Brien): first defeat in Prix Jean Romanet; first try at 12f.
- Minnie Hauk (O'Brien): head second in 2025 Arc; 2nd Prince of Wales's, 8th King George, 3rd Yorkshire Oaks.
- Benvenuto Cellini (O'Brien): Irish Derby, 3rd King George, 5th Prix Niel.
- Friendly Soul (Gosden): Prix Vermeille winner, supplementary entry.
- Varandir: Prix Niel winner. Saddadd: Grosser Preis von Baden winner.
- Japanese pair (no prep, no Japanese-trained Arc winner ever): Meisho Tabaru (2x Takarazuka Kinen), Admire Terra (Hanshin Daishoten).
- Trend: 19 of last 24 winners drew stall 8 or lower.

## Unverified / conflicting
- Draw: one search summary said Daryz 1, Kalpana 9, Maltese Cross 13; another said the draw was not yet made. UNCONFIRMED, not used in model.
- Going: sources conflict (good/good-to-firm vs "at least soft"). Model assumes good to firm.
- Odds for Friendly Soul, Varandir, Saddadd, Japanese runners and outsiders are ESTIMATES. Several trainers unknown.

## Current prediction (model v1)
1 Daryz, 2 Maltese Cross, 3 Kalpana, 4 Friendly Soul, 5 Diamond Necklace, 6 Benvenuto Cellini, 7 Minnie Hauk (next: Bay City Roller, Varandir).
Places 4–8 are within ~0.5 points: a coin-flip cluster.

## Repos
- Original work: F1r3Hydr4nt/daily-sports, branch claude/jolly-hawking-cyrmx5 (file arc_2026_predictor.py).
- This repo: F1r3Hydr4nt/Arc-2026 (was empty; initialised with this commit).
