# Prediction v3

Script: `predictor.py` in this folder (run `python3 predictor.py`).

## What this version is
User instruction: disregard bookmaker odds. Odds and 35% market weight removed; weights rescaled to form 46 / distance 23 / ground 15 / connections 15; ties broken by 2026 form score. Ground and draw scenarios retained.

## Output (draw NOT applied)
```

== going: fast  |  draw: NOT applied ==
 1. Daryz              8.92
 2. Maltese Cross      8.38
 3. Kalpana            8.36
 4. Benvenuto Cellini  7.46
 5. Minnie Hauk        7.46
 6. Friendly Soul      7.29
 7. Diamond Necklace   6.97
 8. Varandir           6.93
 9. Bay City Roller    6.86

== going: soft  |  draw: NOT applied ==
 1. Daryz              8.92
 2. Kalpana            8.06
 3. Maltese Cross      7.93
 4. Benvenuto Cellini  7.46
 5. Minnie Hauk        7.46
 6. Bay City Roller    7.31
 7. Friendly Soul      7.29
 8. Diamond Necklace   6.97
 9. Varandir           6.93
```

## Output with UNCONFIRMED rumoured draw (Daryz 1, Kalpana 9, Maltese Cross 13), fast ground
```

== going: fast  |  draw: applied ==
 1. Daryz              9.72
 2. Kalpana            8.16
 3. Maltese Cross      7.68
 4. Benvenuto Cellini  7.46
 5. Minnie Hauk        7.46
 6. Friendly Soul      7.29
 7. Diamond Necklace   6.97
 8. Varandir           6.93
 9. Bay City Roller    6.86
```
