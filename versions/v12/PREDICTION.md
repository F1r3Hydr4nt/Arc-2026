# Prediction v12: ratings + 2026 Group 1 head-to-heads added (draw applied). CURRENT MODEL
User asked for speed/time form ratings, and pointed out that Minnie Hauk beat Daryz at Ascot (correct: 2026 Prince of Wales's Stakes, Ombudsman won by 4L from Minnie Hauk, Daryz 3rd, about 1.75L behind her; Daryz had virus/travel excuses; Daryz had beaten her by a head in the 2025 Arc).

Weights: form 22 / rating 17 / distance 15 / ground 10 / trainer 8 / jockey 8 / market 20. Rating score = (figure - 100)/4 clamped 0-10 (138 -> 9.5, 125 -> 6.25). Head-to-head: +0.2 per 2026 Group 1 win over another Arc runner (Minnie Hauk 1 [beat Daryz], Kalpana 2 [beat Minnie Hauk, Cellini], Diamond Necklace 1 [beat Friendly Soul], Saddadd 1 [beat Bright Light]).

Rating figures found (mixed systems, approximate): Daryz 138 (RPR; Timeform 131 for 2025 Arc), Thundering On 132 (RPR; Timeform 124 Oaks), Varandir 128, Saddadd 128, Arrow Eagle 128, Diamond Necklace 126 (Nassau), Bay City Roller 125, Kalpana 125 (likely understated), Cellini 124 (Timeform 124p), Maltese Cross 124 (TS 126), Meisho Tabaru 123 (IFHA), Bright Light 114, Chestnut Rocket 113. NO figure found: Minnie Hauk, Friendly Soul, Admire Terra (field average 125.2 used). True speed figures/sectionals NOT modelled (only a qualitative note that Daryz has the best closing sectionals).

```

== going: fast  |  draw: applied  |  book overround 1.319 ==
 1. Daryz              9.70
 2. Thundering On      7.94
 3. Kalpana            7.87
 4. Benvenuto Cellini  7.12
 5. Maltese Cross      7.00
 6. Varandir           6.56
 7. Diamond Necklace   6.30
 8. Minnie Hauk        6.28
 9. Friendly Soul      6.24

== going: soft  |  draw: applied  |  book overround 1.319 ==
 1. Daryz              9.70
 2. Thundering On      7.94
 3. Kalpana            7.67
 4. Benvenuto Cellini  7.12
 5. Maltese Cross      6.70
 6. Varandir           6.56
 7. Friendly Soul      6.44
 8. Minnie Hauk        6.28
 9. Diamond Necklace   6.10
```

## Sensitivity (fast, top 9)
- H2H off: Daryz 9.70, Thundering On 7.94, Kalpana 7.47, Cellini 7.12, Maltese Cross 7.00, Varandir 6.56, Friendly Soul 6.24, Diamond Necklace 6.10, Minnie Hauk 6.08
- Minnie Hauk rating 130 instead of average: she moves to 7th (6.49), ahead of Diamond Necklace
- Rating off: Daryz 9.78, Kalpana 8.42, Thundering On 8.03, Maltese Cross 7.51, Cellini 7.29, Diamond Necklace 6.81, Varandir 6.48, Friendly Soul 6.45, Minnie Hauk 6.40
- No market (ad hoc weights): fast Daryz, Thundering On, Kalpana, Cellini, Maltese Cross, Minnie Hauk 7.45, Varandir 7.44, Friendly Soul 7.41; soft Daryz, Thundering On, Kalpana, Cellini, Friendly Soul, Minnie Hauk, Varandir
