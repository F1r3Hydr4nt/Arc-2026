# Prediction v2

Script: `predictor.py` in this folder (run `python3 predictor.py`).

## What this version is
Corrected ages/trainers/odds (Kalpana 5yo, Friendly Soul ~25/1 and 5yo+, Bay City Roller = G Scott, Varandir = Graffard, Saddadd = Varian). Added fast/soft ground scores, stall-draw rule (--draw) and trend adjustments (5yo+ penalty, defending-colt penalty, Japanese no-prep penalty). Still uses bookmaker odds (35%).

## Output (draw NOT applied)
```

== going: fast  |  draw: NOT applied ==
 1. Daryz              9.25
 2. Maltese Cross      7.25
 3. Kalpana            6.55
 4. Diamond Necklace   5.72
 5. Benvenuto Cellini  5.47
 6. Minnie Hauk        5.36
 7. Friendly Soul      5.02
 8. Varandir           5.01
 9. Bay City Roller    4.87

== going: soft  |  draw: NOT applied ==
 1. Daryz              9.25
 2. Maltese Cross      6.95
 3. Kalpana            6.35
 4. Diamond Necklace   5.72
 5. Benvenuto Cellini  5.47
 6. Minnie Hauk        5.36
 7. Bay City Roller    5.17
 8. Friendly Soul      5.02
 9. Varandir           5.01
```

## Output with UNCONFIRMED rumoured draw (Daryz 1, Kalpana 9, Maltese Cross 13), fast ground
```

== going: fast  |  draw: applied ==
 1. Daryz              10.05
 2. Maltese Cross      6.55
 3. Kalpana            6.35
 4. Diamond Necklace   5.72
 5. Benvenuto Cellini  5.47
 6. Minnie Hauk        5.36
 7. Friendly Soul      5.02
 8. Varandir           5.01
 9. Bay City Roller    4.87
```
