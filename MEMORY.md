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

## Log
- Old repo F1r3Hydr4nt/daily-sports held only my branch claude/jolly-hawking-cyrmx5 (one file, already copied here). User asked to delete the old repo. Branch deletion via git push was refused (remote hung up), so the branch still exists; the repo itself cannot be deleted with available tools. User must delete the repo in GitHub settings (Settings > Danger Zone).

## Update 2026-10-01 13:56 UTC — model v2 (draw confirmation due 19:45 GMT Thu 1 Oct)
Corrections to earlier inputs: Kalpana is a 5yo mare (only nine 5yo Arc winners ever); Friendly Soul is 5yo+ (won 2024 Prix de l'Opera), ~25/1; Bay City Roller trained by George Scott (both G1 wins on soft; ~75% to run, wants rain); Varandir trained by Graffard; Saddadd by Roger Varian; Thundering On J O'Brien; Arrow Eagle Rouget; Bright Light Suborics; Chestnut Rocket Karkosa.
Ground: sources still conflict (clerk: dry, good/good-to-firm; later report: close to good-to-soft). Maltese Cross has lost twice when soft is in the going; Bay City Roller needs soft; Daryz handles both.
Daryz risks: no colt has won back-to-back Arcs since Alleged (1978).

### Prediction v2 (draw not applied)
| Pos | Fast ground | Soft ground |
|---|---|---|
| 1 | Daryz | Daryz |
| 2 | Maltese Cross | Maltese Cross |
| 3 | Kalpana | Kalpana |
| 4 | Diamond Necklace | Diamond Necklace |
| 5 | Benvenuto Cellini | Benvenuto Cellini |
| 6 | Minnie Hauk | Minnie Hauk |
| 7 | Friendly Soul | Bay City Roller |
Next just outside: Varandir, Friendly Soul/Bay City Roller.
Unconfirmed draw rumour (Daryz 1, Kalpana 9, Maltese Cross 13) only widens Daryz's lead and drops Maltese Cross/Kalpana a little; top order is unchanged.

### Still unverified
Official stalls, official going, odds for Varandir/Saddadd/Japanese/outsiders (estimates), jockeys for Minnie Hauk/Benvenuto Cellini/Diamond Necklace.

- 2026-10-01: Saved PREDICTION_v1.md (original first prediction), predictor_v1_original.py and SESSION_LOG.md (condensed session copy).

## Update 2026-10-01 — model v3: BOOKMAKER ODDS REMOVED (user instruction)
User: disregard bookmakers' odds. Odds field and 35% market weight deleted; remaining weights rescaled: form 46%, distance 23%, ground 15%, connections 15%. Ties broken by 2026 form score. Odds listed in earlier sections of this file are historical only and are no longer used.

### Prediction v3 (draw not applied)
| Pos | Fast ground | Soft ground |
|---|---|---|
| 1 | Daryz (8.92) | Daryz (8.92) |
| 2 | Maltese Cross (8.38) | Kalpana (8.06) |
| 3 | Kalpana (8.36) | Maltese Cross (7.93) |
| 4 | Benvenuto Cellini (7.46) | Benvenuto Cellini (7.46) |
| 5 | Minnie Hauk (7.46) | Minnie Hauk (7.46) |
| 6 | Friendly Soul (7.29) | Bay City Roller (7.31) |
| 7 | Diamond Necklace (6.97) | Friendly Soul (7.29) |
Next: Varandir 6.93, Bay City Roller 6.86 (fast) / Diamond Necklace 6.97 (soft 8th).
What changed vs v2: Diamond Necklace falls from 4th to 7th/8th (her 12f ability is unproven, and market had been propping her up); Friendly Soul and Minnie Hauk rise. Maltese Cross and Kalpana swap on soft ground. Cellini/Minnie Hauk tie on score; Cellini placed ahead on form tie-break.
Caveat: the 0-10 form/distance/ground/connection scores are my own judgements from search summaries, some of which quote market views, so independence from odds is not total.
Unconfirmed draw rumour (Daryz 1, Kalpana 9, Maltese Cross 13), fast ground: Daryz, Kalpana, Maltese Cross, Cellini, Minnie Hauk, Friendly Soul, Diamond Necklace.

## Discrepancy log: Minnie Hauk's position
- v1 (saved in PREDICTION_v1.md): 7th (5.36), behind Friendly Soul (4th), Diamond Necklace (5th), Benvenuto Cellini (6th).
- v2: 6th (5.36 unchanged). She only moved up because Friendly Soul fell (guessed odds 13/1 -> ~25/1, and 5yo+ penalty applied), not because of any change to Minnie Hauk's own inputs.
- v3 (odds removed): 5th (7.46), level with Benvenuto Cellini, who is placed ahead on the form tie-break.
- Flagged by the user as a discrepancy that I had not recorded; recorded here. OPEN: user may mean a different discrepancy (e.g. in her form or ground data); to be clarified.

## Standing rules (also in CLAUDE.md)
- After every user prompt -> assistant response: append to SESSION_LOG.md, update MEMORY.md, PLAN.md and any affected files, commit and push to this repo.
- Never use bookmaker odds as model input.

## Prediction history
Full record of every iteration (v1, v2, v3, rumoured-draw tests, and a v4 draw-revision slot) is in PREDICTION_HISTORY.md; runnable snapshots in versions/v1/predictor.py, v2, v3. All three were re-run and reproduce the original numbers. v4 (official draw) is the revision expected to matter most and is still pending.
- 2026-10-01: Per-version folders created: versions/v1, v2, v3 (each predictor.py + PREDICTION.md with notes and captured output), versions/v4 placeholder (draw revision, pending). Replaces the earlier history/ folder.

## Weather/going check (2026-10-01 ~14:15 UTC, user asked for the most reliable forecast)
- Could not fetch Météo-France, yr.no, Open-Meteo or France Galop (blocked); search summaries only.
- Best-sourced item (Racing Post via search, dated 1 Oct 2026): ~4mm Wed + 3.5mm overnight; penetrometer 3.7 ("souple", no worse than good to soft on GoingStick); dry weather forecast well into next week, so Arc on ground no slower than good, perhaps good to firm. Earlier in the week: no rain since 8 Sep, going good to soft 3.3 on 25 Sep, watered to good (3.2).
- Generic Paris forecast sites: Sun 4 Oct partly cloudy, ~11-21C, ~0mm, ~5% rain (long-range, low reliability).
- Some Racing Post headlines in results ("very soft", "testing ground after Saturday rain") look like other years; ignored.
- Reading: dry Sunday, going likely good, possibly good to firm. The FAST scenario is now the more likely one; soft is the minority case. v3 fast: Daryz, Maltese Cross, Kalpana, Benvenuto Cellini, Minnie Hauk, Friendly Soul, Diamond Necklace. No model change made.

## Draw read attempt (user gave Racing Post live-blog URL)
- Racing Post page is blocked from this environment (cannot read it). The page title says stalls are "to be revealed" and the draw is due 19:45 GMT Thu 1 Oct; at the time of the attempt it was still before 19:45 UTC.
- Search summary returned two mutually contradictory "draws": (a) Daryz 5, Kalpana 6, Maltese Cross 11; (b) a 1-16 list that is simply the declared-runner order (Daryz 1, Saddadd 2, ... Diamond Necklace 16), which matches the runner list order from the confirmed-runners article, not a real draw. An earlier summary gave Daryz 1, Kalpana 9, Maltese Cross 13. Three conflicting versions = NONE verified. Not applied to the model.
- Action: wait for the real draw (scheduled check 19:55 UTC) or for the user to paste the table.

## OFFICIAL DRAW (19:45-19:48 GMT, 1 Oct 2026; pasted by user from Racing Post live blog) and v4 prediction
1 Benvenuto Cellini, 2 Chestnut Rocket, 3 Thundering On, 4 Varandir, 5 Daryz, 6 Kalpana, 7 Friendly Soul, 8 Bright Light, 9 Saddadd, 10 Minnie Hauk, 11 Maltese Cross, 12 Admire Terra, 13 Meisho Tabaru, 14 Arrow Eagle, 15 Bay City Roller, 16 Diamond Necklace.
All earlier "draws" from search summaries were wrong (superseded).
v4 top 7 (fast, the favoured going): Daryz, Kalpana, Benvenuto Cellini, Maltese Cross, Friendly Soul, Varandir, Minnie Hauk. Soft: Daryz, Kalpana, Cellini, Friendly Soul, Maltese Cross, Varandir, Minnie Hauk. Files: versions/v4/.
Scheduled 19:55 UTC draw-check reminder deleted (no longer needed).

## Weather re-check and Betfair odds attempt (user: double-check no rain; could v5 use Betfair odds?)
- Weather re-check is INCONCLUSIVE, and my earlier "dry Sunday, fast likely" was too confident. A Racing Post summary says rain Friday evening (~5mm) and Saturday morning (3-5mm), wind 25-30kph, estimates good-to-soft to soft; the earlier summary said 7.5mm Wed/Thu then dry into next week. Articles are undated in the summaries and some may be from the 2025 Arc (which ran very soft). Official sources (France Galop, Météo-France, yr.no) are blocked. Treat BOTH fast and soft scenarios as live until the official Friday/Saturday going update.
- Betfair: betfair.com is blocked from this environment; Exchange API would need the user's account, app key and session token and a reachable network. Search summaries quote conflicting "Betfair" prices (Daryz 7/2 vs 7/4; Maltese Cross 9/1 vs 9/2), all pre-draw. None usable.
- Proposed v5 (not built yet): add exchange-implied probability (overround removed, post-draw) as a modest weight (~20%) alongside v4 factors; keep v4 odds-free for comparison. Needs user-pasted Betfair prices after the draw.

## v4b and v5 (user pasted Betfair + Paddy Power screenshots, 20:04-20:05 UTC 1 Oct 2026)
- Betfair Exchange screenshot: market SUSPENDED, no prices (listed runners only). Paddy Power Final Decs usable (prices in versions/v5/PREDICTION.md); EW 1/5, 4 places; book overround 1.319.
- ERROR FOUND: Thundering On was modelled as an unresearched 4yo colt (form 5.0). She is a filly (J O'Brien), reported Oaks winner (UNVERIFIED, search hedged) and G2 Blandford winner, ridden by Boudot, stall 3, priced 8/1. Corrected in v4b. Other outsiders (Bright Light, Arrow Eagle, Chestnut Rocket, Admire Terra) still have thin, mostly guessed inputs; market has them 66/1-150/1, consistent with that.
- v4b (no odds), top 7 fast: Daryz, Kalpana, Thundering On, Benvenuto Cellini, Maltese Cross, Friendly Soul, Varandir. Soft: Daryz, Thundering On, Kalpana, Cellini, Friendly Soul, Maltese Cross, Varandir.
- v5 (v4b + 20% market), top 7 fast: Daryz, Kalpana, Thundering On, Maltese Cross, Benvenuto Cellini, Varandir, Friendly Soul. Soft: Daryz, Kalpana, Thundering On, Cellini, Maltese Cross, Varandir, Friendly Soul.
- Top 3 identical in v4b/v5 apart from order of Kalpana vs Thundering On on soft in v4b.

## INPUT AUDIT (user: 'if you made such an elemental error maybe you need to recheck all entries')
Re-searched all 16 runners; full table of corrections + sources in AUDIT.md. Earlier facts in this file that were WRONG and are superseded: Thundering On colt/4yo/unresearched; Admire Terra 'Gr1 Hanshin Daishoten / 3rd Osaka Hai' (actually G2 Daishoten; 3rd Tenno Sho Spring G1); Bright Light age 4 (is 3); Arrow Eagle age 4 (is 5); Diamond Necklace form understated (unbeaten in 6, four G1s before Romanet); Meisho Tabaru soft-ground assumption (won Takarazuka on yielding); Friendly Soul ground (dislikes firm).
New models: v6 (audited, no odds) and v7 (audited + 20% Paddy Power prices; now the root arc_2026_predictor.py).
v6 fast top 7: Daryz, Kalpana, Thundering On, Benvenuto Cellini, Maltese Cross, Friendly Soul, Diamond Necklace. v6 soft: Daryz, Thundering On, Kalpana, Cellini, Friendly Soul, Maltese Cross, Minnie Hauk.
v7 fast top 7: Daryz, Kalpana, Thundering On, Maltese Cross, Cellini, Varandir, Diamond Necklace. v7 soft: Daryz, Thundering On, Kalpana, Cellini, Maltese Cross, Friendly Soul, Varandir.
Lesson: error came from not researching low-profile runners and from generic assumptions (e.g. 'Japanese horses hate soft'); fixed by searching each runner individually.

## Round 2: jockeys and missing form (see AUDIT.md 'Round 2')
- NOT Japanese: Arrow Eagle (French, Rouget), Chestnut Rocket (Karkosa, French-based), Bright Light (German, Suborics). Japanese runners are only Meisho Tabaru and Admire Terra.
- Oaks: Diamond Necklace won the PRIX DE DIANE (French Oaks) + Poule d'Essai des Pouliches; 2026 EPSOM Oaks winner is Thundering On. User thought the Oaks was this year's; Diamond Necklace's was the French Oaks.
- Missing form found: Arrow Eagle 4th Prix Ganay 2026 (only 2026 run found); Chestnut Rocket Listed win + 2nd Grand Prix de Deauville G2; Bright Light 2nd Gr Preis von Berlin G1, 3rd Baden G1.
- Jockeys added to the model (JOCKEY dict). Ballydoyle trio rides unannounced at time of writing: provisional 8 each.
- v8 (jockeys, no odds) fast top 7: Daryz, Thundering On, Kalpana, Benvenuto Cellini, Maltese Cross, Friendly Soul, Diamond Necklace. v9 (jockeys + odds; root script) fast: Daryz, Thundering On, Kalpana, Maltese Cross, Benvenuto Cellini, Varandir, Diamond Necklace.

## v10 (user: 'we don't know the jockeys yet')
Unknown Ballydoyle rides (Minnie Hauk, Benvenuto Cellini, Diamond Necklace) now score the average of known jockeys (7.08) instead of an assumed 8; `--no-jockey` switch added; all jockey bookings regarded as provisional (deadline extended past the draw). v10 (root script) fast top 7: Daryz, Thundering On, Kalpana, Maltese Cross, Benvenuto Cellini, Varandir, Friendly Soul. Soft: Daryz, Thundering On, Kalpana, Cellini, Maltese Cross, Friendly Soul, Varandir. With no jockey factor, Kalpana (7.95) edges Thundering On (7.90).
Lesson: do not insert assumed values as inputs; use neutral values and flag them.

## Scheduled check: jockey declarations
One-shot routine trig_015cMdMaq1scoKkVRyEodTvj fires 2026-10-02 15:00 UTC (= 4pm UK time, BST assumed from the user's phone clock) into this session: find final jockeys, build versions/v11, rerun, push, report. It is a one-off run, not a repeating cron. If the declarations are not out by then, rerun later (Saturday). Cancel with delete_trigger.

## Notifications and Betfair (user requests, 1 Oct ~19:46 UTC)
- Jockey routine trig_015cMdMaq1scoKkVRyEodTvj (2 Oct 15:00 UTC) now also sends a PushNotification when it finishes (one line: Ballydoyle jockeys confirmed or not, new top 3). Notification only reaches the user if the session is alive and notifications are enabled/connected.
- Betfair re-check scheduled via send_later trig_01AndsB93dHaoRXSd8J9wr3b for 21:30 UTC tonight (22:30 UK).
- User supplied Betfair market URL: https://www.betfair.com/exchange/plus/en/horse-racing/parislongchamp-4th-oct-betting-35193074 . WebFetch of it is BLOCKED (egress proxy), same as all betfair.com. The page also likely needs JavaScript. Only route to Betfair prices: user pastes a screenshot/text, or runs the Betfair API locally.

## Betfair re-check 21:30 UTC 1 Oct 2026 (scheduled routine fired)
- betfair.com still blocked; searches returned NO Betfair Exchange prices. Post-draw bookmaker moves in the press agree with the Paddy Power card already used in v5-v10 (Daryz 7/4; Kalpana cut from 7/1 to 5/1; Maltese Cross 5/1 with some firms, as short as 7/2 elsewhere; Thundering On 8/1; Diamond Necklace drifted from 7/1 to 10/1 after stall 16). No model change; no new version.
- Still need: user-pasted Betfair back prices (screenshot) when the market is open.

## 2 Oct 2026 15:00 UTC: jockey declarations check (scheduled routine fired)
Confirmed Ballydoyle rides: Benvenuto Cellini - Ryan Moore (picked after the draw; Moore left Diamond Necklace), Diamond Necklace - Christophe Soumillon, Minnie Hauk - William Buick. Others unchanged (13 earlier bookings; no change reports). Markets after draw/jockeys: Cellini 25/1 -> 14/1 (biggest mover), Diamond Necklace 8/1 -> 14/1 (Coral), Minnie Hauk 20/1.
Going: penetrometer 3.5 'souple' (~good to soft) Fri 2 Oct; dry forecast so good, maybe good to firm Sunday (search summaries).
v11 (root script) top 7 fast: Daryz, Thundering On, Kalpana, Maltese Cross, Benvenuto Cellini, Varandir, Diamond Necklace. Soft: Daryz, Thundering On, Kalpana, Benvenuto Cellini, Maltese Cross, Friendly Soul, Varandir. With post-jockey 14/1 prices for DN/Cellini: fast 7th becomes Friendly Soul.
Betfair prices still unavailable (blocked).

## User challenge (2 Oct): 'Thundering On did not feature in the first 7 until bookmaker odds were taken into account; Minnie Hauk has left the rankings'
Checked by re-running every version (rank tracker in PREDICTION_HISTORY.md). Thundering On: absent v1-v4, top 3 from v4b, a NO-ODDS version, so the claim is half right: the odds prompted me to find my data error but did not cause her ranking. Minnie Hauk: out of top 7 on fast ground from v4b (no odds), on soft ground only from v7 (market 20/1). Both are subject to my judgement-based scores.

## v12 (user: model with speed/time ratings; Minnie Hauk beat Daryz at Ascot)
User right: Minnie Hauk beat Daryz in the 2026 Prince of Wales's (2nd v 3rd, ~1.75L). Added rating factor (17%) and 2026 G1 head-to-heads (+0.2 per win). Weights: form 22 / rating 17 / dist 15 / ground 10 / trainer 8 / jockey 8 / market 20. v12 (root script) fast top 7: Daryz, Thundering On, Kalpana, Benvenuto Cellini, Maltese Cross, Varandir, Diamond Necklace; soft: Daryz, Thundering On, Kalpana, Cellini, Maltese Cross, Varandir, Friendly Soul. Minnie Hauk 8th both; with a rating of 130 she would be 7th on fast ground. Ratings missing for Minnie Hauk, Friendly Soul, Admire Terra. True speed figures/sectionals not available.

## RACE DAY (Sun 4 Oct 2026, checked 10:58 UTC; race 15:05 UK / 14:05 UTC)
- Jockeys re-confirmed, no changes: Daryz Barzalona; Maltese Cross Marquand; Kalpana Keane; Thundering On Boudot (Dylan Browne McMonagle still injured); Benvenuto Cellini Ryan Moore; Minnie Hauk William Buick; Diamond Necklace Christophe Soumillon; Friendly Soul Doyle; Bay City Roller Murphy; Varandir Lecoeuvre; Saddadd R Dawson; Meisho Tabaru Take; Admire Terra Demuro; Bright Light Marie; Arrow Eagle Mendizabal; Chestnut Rocket Grandin. One summary listed 'A.P. O'Brien' as jockey on two horses: trainer column mix-up, disregarded (three other sources agree on Moore/Buick/Soumillon).
- Bay City Roller is CONFIRMED to run (Scott had said he would not run on watered ground; ground is dry/quick but he stays in).
- Official going: 'bon souple' (~good), Turftrax: mix of good and good to firm (GoingStick 8.2 per summary); only 0.1mm rain overnight; sunny intervals, high ~24-25C. => FAST scenario is the right one; soft is now very unlikely.
- Correction to earlier note: race off 14:05 UTC (15:05 UK), not 13:05.
- Prediction unchanged (v12, fast): Daryz, Thundering On, Kalpana, Benvenuto Cellini, Maltese Cross, Varandir, Diamond Necklace. Prices in the model (Paddy Power, Thursday 20:05) are stale; race-day prices not yet refreshed.

## v13 race-day refresh (4 Oct ~11:45 UTC)
Prices refreshed (Oddschecker/Racing Post via search; mixed): Daryz 7/4, Kalpana 4/1, Maltese Cross 7/1, Thundering On 8/1, Varandir 10/1, DN 14/1, Cellini 16/1 (conflicting: 10/1, 14s), Minnie Hauk 16/1, Saddadd/Meisho Tabaru/Friendly Soul 33/1; Bay City Roller, Admire Terra, Bright Light, Arrow Eagle, Chestnut Rocket NOT refreshed. Jockeys unchanged. Official going GOOD (jockeys: 'a bit of give'); dry. Added 'good' going = midpoint of fast and soft ground ratings.
v13 'good' top 7: Daryz, Kalpana, Thundering On, Benvenuto Cellini, Maltese Cross, Varandir, Minnie Hauk. Fast: same order but Maltese Cross 5th. Soft: Daryz, Thundering On, Kalpana, Cellini, Varandir, Maltese Cross, Minnie Hauk.

## v14 (user: 'make v14 without prices') - odds-free, race-morning inputs
Weights: form 27.5 / rating 21.25 / distance 18.75 / ground 12.5 / trainer 10 / jockey 10. Top 7 (good going): Daryz, Thundering On, Kalpana, Benvenuto Cellini, Friendly Soul, Minnie Hauk, Maltese Cross. Fast: Daryz, Thundering On, Kalpana, Cellini, Maltese Cross, Minnie Hauk, Friendly Soul. Soft: Daryz, Thundering On, Kalpana, Cellini, Friendly Soul, Minnie Hauk, Varandir. Root script is now v14.

## v13 vs v14 comparison saved: versions/COMPARE_v13_v14.md
Same top 4 on every going (only Kalpana/Thundering On swap on good/fast); 6 of 7 top-7 overlap; Daryz's lead falls from ~1.7 to 0.66 without prices; Friendly Soul +2/3, Minnie Hauk +1, Maltese Cross -2, Varandir -2 when prices are removed.

## User paste (4 Oct): 'Betting Without Daryz and Kalpana' (EW 1/5, 3 places)
Form figures cross-checked and consistent with my inputs: Daryz 1-1131, Kalpana 71-1211, Maltese Cross 1-11211, Thundering On 2-21141, Varandir 11141, Diamond Necklace 11-1112, Cellini 13-1135. Jockeys re-confirmed (Barzalona, Keane, Marquand, Boudot, Lecoeuvre, Soumillon, R L Moore). Prices ambiguous (bookmaker columns merged; one block unassigned): if prices follow each horse: Maltese Cross 10/3, 16/5, 10/3; Thundering On 10/3, 7/2; Varandir 6/1, 5/1; Diamond Necklace 6/1, 13/2; Cellini none (paste likely cut off). Not used in the model. Main disagreement with v14: Cellini (model 2nd of the five, market apparently last) and Maltese Cross (model 3rd, market joint-favourite). Awaiting user: build v15 from this market, or supply Cellini price.
