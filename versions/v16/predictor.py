"""Rules-based finishing-order predictor: 2026 Qatar Prix de l'Arc de Triomphe (v16, lessons from the Arc applied; odds-free).

Each runner gets 0-10 scores from hand-written rules; a weighted sum ranks them.
Ground and draw are scenarios because both were unconfirmed at the time of writing.
Run:  python3 arc_2026_predictor.py                          (both ground scenarios, no draw)
      python3 arc_2026_predictor.py --draw "Daryz=1,Kalpana=9"   (once stalls are official)
      python3 arc_2026_predictor.py --going soft
"""
import argparse

# form: quality of 2026 results   dist: proven at 12f / Longchamp
# fast / soft: suitability for good-to-firm / good-to-soft-or-softer ground
# conn: trainer big-race record (jockey scored separately).
R = {
 "Daryz":            dict(age=4, sex="C", trainer="F-H Graffard", form=10,  dist=10, fast=9, soft=9, conn=8),   # 2026: won Prix Ganay (G1) + Prix d'Ispahan (G1), 3rd Prince of Wales's (virus/travel excuses), won Prix Foy; 2025 Arc winner on very soft
 "Maltese Cross":    dict(age=3, sex="C", trainer="W Haggas",     form=9.0, dist=8,  fast=8, soft=5, conn=8),   # Derby 2nd (soft), Grand Prix de Paris, Gt Voltigeur (RPR 124); soft-ground doubts per Racing Post summary
 "Kalpana":          dict(age=5, sex="F", trainer="A Balding",    form=9.5, dist=8,  fast=9, soft=7, conn=8),   # King George (GF, beat Calandagan 1.5L) + Yorkshire Oaks (soft blunted speed); fast theory 'blown apart'
 "Thundering On":    dict(age=3, sex="F", trainer="J O'Brien",    form=8.5, dist=8,  fast=7, soft=7, conn=7),   # Epsom Oaks winner 2026 (attheraces), G2 Blandford; 4th Pretty Polly (coughed); Boudot rides
 "Diamond Necklace": dict(age=3, sex="F", trainer="A O'Brien",    form=9.5, dist=5,  fast=8, soft=6, conn=9),   # AUDIT: unbeaten in 6 before Romanet, 4 G1s incl. French Guineas + an Oaks, beat older horses in Nassau; first defeat on bad patchy ground; 12f unproven
 "Benvenuto Cellini":dict(age=3, sex="C", trainer="A O'Brien",    form=7.0, dist=8,  fast=7, soft=7, conn=9),   # Chester Vase, Derby 10th after stalls incident (not form), Irish Derby, 3rd King George, 5th Prix Niel
 "Friendly Soul":    dict(age=5, sex="F", trainer="J&T Gosden",   form=7.5, dist=8,  fast=6, soft=8, conn=9),   # AUDIT: Vermeille (made all, first 12f); 2nd to Diamond Necklace at Goodwood; 'doesn't want rattling firm ground'; won 2024 Opera on testing ground
 "Minnie Hauk":      dict(age=4, sex="F", trainer="A O'Brien",    form=7.0, dist=9,  fast=7, soft=7, conn=9),   # AUDIT: 2025 won Epsom, Irish and Yorkshire Oaks, 2nd Arc by a head; 2026: 2nd Prince of Wales's (4L), 8th King George, 3rd Yorkshire Oaks
 "Bay City Roller":  dict(age=4, sex="C", trainer="G Scott",      form=7.5, dist=8,  fast=7, soft=9, conn=6),   # v16: fast 5->7 (his own 2026 Prix Foy 2nd was on good-to-firm and he 'lost little in defeat'; I had wrongly leaned on the trainer's ground comments), form 7.0->7.5 (Coronation Cup G1 at 12f + Foy 2nd)
 "Varandir":         dict(age=3, sex="C", trainer="F-H Graffard", form=6.5, dist=8,  fast=7, soft=7, conn=7),   # Prix Hocquart G3, 4th Grand Prix de Paris, Prix Niel G2 (11-2) beating Alam
 "Saddadd":          dict(age=4, sex="C", trainer="R Varian",     form=6.5, dist=7,  fast=7, soft=6, conn=7),   # Grosser Preis von Baden G1 (good, 12f), Gordon Richards G3; Pinatubo colt
 "Meisho Tabaru":    dict(age=5, sex="C", trainer="M Ishibashi",  form=8.0, dist=6,  fast=7, soft=6, conn=5),   # AUDIT: won 2026 Takarazuka Kinen on YIELDING ground (so soft 4 -> 6); 2200m; no prep
 "Admire Terra":     dict(age=5, sex="C", trainer="Y Tomomichi",  form=6.5, dist=4,  fast=7, soft=5, conn=5),   # AUDIT: Hanshin Daishoten is a G2 (3000m), not G1; 3rd Tenno Sho Spring G1 (3200m) beaten 0.1s; a stayer; no prep
 "Bright Light":     dict(age=3, sex="C", trainer="A Suborics",   form=6.5, dist=7,  fast=6, soft=6, conn=5),   # AUDIT: age 3 (was 4); 2nd Grosser Preis von Berlin G1 (neck), 3rd Baden G1; rating 114
 "Arrow Eagle":      dict(age=5, sex="C", trainer="J-C Rouget",   form=5.5, dist=7,  fast=6, soft=6, conn=8),   # AUDIT: age 5 (was 4); 2025 Prix Royal-Oak G1, 6th in 2025 Arc at 105/1; Rouget's final runner; 2026 form not found
 "Chestnut Rocket":  dict(age=4, sex="C", trainer="A Karkosa",    form=5.0, dist=6,  fast=6, soft=6, conn=4),   # AUDIT: rating 113, Polish Derby winner, Listed winner, 2nd Grand Prix de Deauville G2
}

# Jockey 0-10: my judgement (Ballydoyle trio confirmed 1-2 Oct per Racing Post/AOL/Irish Examiner via search; v10 had them unknown)
# original note: my judgement of big-race / Arc / Longchamp pedigree and current form. Bookings per Racing Post/Sporting Life
# search summaries (1 Oct 2026). The three Ballydoyle rides (Minnie Hauk, Benvenuto Cellini, Diamond Necklace) were NOT yet
# announced (Ryan Moore had a choice), so they score None = the average of the known jockeys (no boost, no penalty).
# Even the known bookings are provisional: the booking deadline was extended until after the draw.
JOCKEY = {
 "Daryz": ("M Barzalona", 8),            # rode Daryz to the 2025 Arc
 "Maltese Cross": ("T Marquand", 8),
 "Kalpana": ("C Keane", 7),
 "Thundering On": ("P-C Boudot", 8),     # Arc-winning jockey (Racing Post headline)
 "Diamond Necklace": ("C Soumillon", 8),   # confirmed 1-2 Oct: ten-time French champion; Moore (Prix de Diane rider) switched to Cellini after stall 16,
 "Benvenuto Cellini": ("R Moore", 9),     # confirmed 1-2 Oct: Moore chose Cellini (stall 1) over Diamond Necklace,
 "Minnie Hauk": ("W Buick", 8),          # confirmed 1-2 Oct: seeking first Arc win,
 "Friendly Soul": ("J Doyle", 8),        # front-ran her to the Vermeille at Longchamp
 "Bay City Roller": ("O Murphy", 8),     # 'live chance'; Coronation Cup partner
 "Varandir": ("C Lecoeuvre", 6),
 "Saddadd": ("R Dawson", 5),             # NB Baden win was ridden by a different jockey per one summary
 "Meisho Tabaru": ("Y Take", 7),         # Japan's most decorated; 57yo G1 record holder
 "Admire Terra": ("C Demuro", 9),        # two Arc wins (Sottsass, Ace Impact)
 "Bright Light": ("B Marie", 6),
 "Arrow Eagle": ("I Mendizabal", 6),
 "Chestnut Rocket": ("M Grandin", 6),
}

# Best figure found per horse, on a roughly RPR/Timeform/IFHA scale (search summaries; systems are MIXED and some are unclear,
# so treat as approximate). None = no figure found -> field average (no boost, no penalty).
RATING = {
 "Daryz": (138, "RPR per racecard summary (Timeform 131 for 2025 Arc)"),
 "Thundering On": (124, "v16: Timeform 124 for the Oaks, to match the scale used for the others (v1-v15 used an RPR 132 figure)"),
 "Varandir": (128, "RPR"),
 "Saddadd": (128, "RPR"),
 "Arrow Eagle": (128, "RPR"),
 "Diamond Necklace": (126, "Nassau Stakes rating, system unclear (OR 115)"),
 "Bay City Roller": (125, "RPR Coronation Cup (another source 128)"),
 "Kalpana": (125, "Yorkshire Oaks mark, system unclear; Balding says her King George mark was higher, so likely UNDERSTATED"),
 "Benvenuto Cellini": (124, "Timeform 124p Irish Derby"),
 "Maltese Cross": (124, "RPR Great Voltigeur (TS 126)"),
 "Meisho Tabaru": (123, "IFHA/Longines rating to 6 Sep"),
 "Bright Light": (114, "rating, system unclear"),
 "Chestnut Rocket": (113, "rating, system unclear"),
 "Minnie Hauk": (None, "no figure found"),
 "Friendly Soul": (None, "no figure found"),
 "Admire Terra": (None, "no figure found"),
}
_RK = [v[0] for v in RATING.values() if v[0] is not None]
RATING_AVG = sum(_RK) / len(_RK)


def rating_score(name):
    r = RATING[name][0]
    r = RATING_AVG if r is None else r
    return max(0.0, min(10.0, (r - 100) / 4))   # 100 -> 0, 125 -> 6.25, 138 -> 9.5

# 2026 Group 1 head-to-heads between Arc runners (winner ahead of loser on the day), +H2H_STEP per win. G2 results excluded.
#   Prince of Wales's (Ascot): Minnie Hauk 2nd, Daryz 3rd (1.75L behind her; Daryz had virus/travel excuses)
#   Yorkshire Oaks: Kalpana won, Minnie Hauk 3rd.  King George: Kalpana won, Benvenuto Cellini 3rd (Minnie Hauk 8th)
#   Nassau Stakes: Diamond Necklace won, Friendly Soul 2nd.  Grosser Preis von Baden: Saddadd won, Bright Light 3rd.
H2H_STEP = 0.2
H2H_WINS = {"Minnie Hauk": 1, "Kalpana": 2, "Diamond Necklace": 1, "Saddadd": 1}

_KNOWN = [v[1] for v in JOCKEY.values() if v[1] is not None]
JOCKEY_AVG = sum(_KNOWN) / len(_KNOWN)
USE_JOCKEY = True   # --no-jockey turns the whole factor into the field average (no effect)


def jockey_score(name):
    sc = JOCKEY[name][1]
    return JOCKEY_AVG if (sc is None or not USE_JOCKEY) else sc

W = dict(form=0.275, rating=0.2125, dist=0.1875, ground=0.125, conn=0.10, jockey=0.10)   # v13 weights with the 20% market removed, rescaled to 1.0

# v14: bookmaker prices deliberately NOT used.
JAPAN = ("Meisho Tabaru", "Admire Terra")


def trend_adjust(name, r):
    """5yo+ rarely win (9 five-year-old winners ever); a colt defending the title is hard
    (none since Alleged, 1978); 3yo fillies get a weight allowance; Japan has no prep run."""
    adj = 0.0
    if r["age"] >= 5:
        adj -= 0.4
    if name == "Daryz":
        adj -= 0.3
    if r["age"] == 3 and r["sex"] == "F":
        adj += 0.2
    if name in JAPAN:
        adj -= 0.5
    return adj


def draw_adjust(stall):
    """v16: halved. The 19-of-24 statistic is about WINNERS from a low stall, not placings, and applying it at full strength to every runner was too strong (in the 2026 Arc stalls 15 and 16 filled 2nd and 3rd)."""
    if stall is None:
        return 0.0
    if stall <= 3:
        return 0.4
    if stall <= 8:
        return 0.25
    if stall <= 12:
        return -0.1
    return -0.35


def score(name, going, draw):
    r = R[name]
    ground = (r["fast"] + r["soft"]) / 2 if going == "good" else r[going]   # official going 'Good' = midpoint of the two scenarios
    s = (W["form"] * r["form"] + W["rating"] * rating_score(name) + W["dist"] * r["dist"] + W["ground"] * ground
         + W["conn"] * r["conn"] + W["jockey"] * jockey_score(name))
    return round(s + trend_adjust(name, r) + draw_adjust(draw.get(name)) + H2H_STEP * H2H_WINS.get(name, 0), 2)


def rank(going, draw):
    # ties broken by 2026 form score
    return sorted(R, key=lambda n: (score(n, going, draw), R[n]["form"]), reverse=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--going", choices=["fast", "good", "soft"], help="default: print fast, good and soft")
    ap.add_argument("--no-jockey", action="store_true", help="ignore jockeys entirely")
    ap.add_argument("--draw", default="", help='e.g. "Daryz=1,Kalpana=9"')
    a = ap.parse_args()
    USE_JOCKEY = not a.no_jockey
    draw = {k: int(v) for k, v in (p.split("=") for p in a.draw.split(",") if p)}
    for going in ([a.going] if a.going else ["fast", "good", "soft"]):
        print(f"\n== going: {going}  |  draw: {'applied' if draw else 'NOT applied'} ==")
        for i, n in enumerate(rank(going, draw)[:9], 1):
            print(f"{i:>2}. {n:<18} {score(n, going, draw):.2f}")
