# Prediction v10: unknown jockeys neutral (draw applied). CURRENT MODEL
User correction: "we don't know the jockeys yet". v9 had given the three unannounced Ballydoyle rides (Minnie Hauk, Benvenuto Cellini, Diamond Necklace) a provisional 8, which was an assumption. v10 scores them as the average of the known jockeys (7.08): no boost, no penalty. Even the 13 known bookings are provisional because the booking deadline was extended until after the draw. `--no-jockey` removes the jockey factor altogether.
Weights: form 34 / distance 17 / ground 11 / trainer 9 / jockey 9 / market 20 (Paddy Power Final Decs 20:05 1 Oct; Betfair suspended).

## Default
```

== going: fast  |  draw: applied  |  book overround 1.319 ==
 1. Daryz              9.73
 2. Thundering On      7.98
 3. Kalpana            7.95
 4. Maltese Cross      7.46
 5. Benvenuto Cellini  7.18
 6. Varandir           6.51
 7. Friendly Soul      6.46
 8. Diamond Necklace   6.41
 9. Minnie Hauk        6.19

== going: soft  |  draw: applied  |  book overround 1.319 ==
 1. Daryz              9.73
 2. Thundering On      7.98
 3. Kalpana            7.73
 4. Benvenuto Cellini  7.18
 5. Maltese Cross      7.13
 6. Friendly Soul      6.68
 7. Varandir           6.51
 8. Diamond Necklace   6.19
 9. Minnie Hauk        6.19
```
## With --no-jockey (fast, top rows)
```

== going: fast  |  draw: applied  |  book overround 1.319 ==
 1. Daryz              9.65
 2. Kalpana            7.95
 3. Thundering On      7.90
 4. Maltese Cross      7.37
 5. Benvenuto Cellini  7.18
 6. Varandir           6.61
 7. Diamond Necklace   6.41
 8. Friendly Soul      6.38
 9. Minnie Hauk        6.19
```
