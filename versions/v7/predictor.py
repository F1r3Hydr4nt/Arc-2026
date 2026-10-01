"""Rules-based finishing-order predictor: 2026 Qatar Prix de l'Arc de Triomphe (v7, audited inputs + market prices).

Each runner gets 0-10 scores from hand-written rules; a weighted sum ranks them.
Ground and draw are scenarios because both were unconfirmed at the time of writing.
Run:  python3 arc_2026_predictor.py                          (both ground scenarios, no draw)
      python3 arc_2026_predictor.py --draw "Daryz=1,Kalpana=9"   (once stalls are official)
      python3 arc_2026_predictor.py --going soft
"""
import argparse

# form: quality of 2026 results   dist: proven at 12f / Longchamp
# fast / soft: suitability for good-to-firm / good-to-soft-or-softer ground
# conn: trainer/jockey big-race record.
R = {
 "Daryz":            dict(age=4, sex="C", trainer="F-H Graffard", form=10,  dist=10, fast=9, soft=9, conn=8),   # 2026: won Prix Ganay (G1) + Prix d'Ispahan (G1), 3rd Prince of Wales's (virus/travel excuses), won Prix Foy; 2025 Arc winner on very soft
 "Maltese Cross":    dict(age=3, sex="C", trainer="W Haggas",     form=9.0, dist=8,  fast=8, soft=5, conn=8),   # Derby 2nd (soft), Grand Prix de Paris, Gt Voltigeur (RPR 124); soft-ground doubts per Racing Post summary
 "Kalpana":          dict(age=5, sex="F", trainer="A Balding",    form=9.5, dist=8,  fast=9, soft=7, conn=8),   # King George (GF, beat Calandagan 1.5L) + Yorkshire Oaks (soft blunted speed); fast theory 'blown apart'
 "Thundering On":    dict(age=3, sex="F", trainer="J O'Brien",    form=8.5, dist=8,  fast=7, soft=7, conn=7),   # Epsom Oaks winner 2026 (attheraces), G2 Blandford; 4th Pretty Polly (coughed); Boudot rides
 "Diamond Necklace": dict(age=3, sex="F", trainer="A O'Brien",    form=9.5, dist=5,  fast=8, soft=6, conn=9),   # AUDIT: unbeaten in 6 before Romanet, 4 G1s incl. French Guineas + an Oaks, beat older horses in Nassau; first defeat on bad patchy ground; 12f unproven
 "Benvenuto Cellini":dict(age=3, sex="C", trainer="A O'Brien",    form=7.0, dist=8,  fast=7, soft=7, conn=9),   # Chester Vase, Derby 10th after stalls incident (not form), Irish Derby, 3rd King George, 5th Prix Niel
 "Friendly Soul":    dict(age=5, sex="F", trainer="J&T Gosden",   form=7.5, dist=8,  fast=6, soft=8, conn=9),   # AUDIT: Vermeille (made all, first 12f); 2nd to Diamond Necklace at Goodwood; 'doesn't want rattling firm ground'; won 2024 Opera on testing ground
 "Minnie Hauk":      dict(age=4, sex="F", trainer="A O'Brien",    form=7.0, dist=9,  fast=7, soft=7, conn=9),   # AUDIT: 2025 won Epsom, Irish and Yorkshire Oaks, 2nd Arc by a head; 2026: 2nd Prince of Wales's (4L), 8th King George, 3rd Yorkshire Oaks
 "Bay City Roller":  dict(age=4, sex="C", trainer="G Scott",      form=7.0, dist=8,  fast=5, soft=9, conn=6),   # 2 G1s both with soft in going (incl. Coronation Cup); 2nd Foy by ~1.5-2L; Scott: won't run if watered ground
 "Varandir":         dict(age=3, sex="C", trainer="F-H Graffard", form=6.5, dist=8,  fast=7, soft=7, conn=7),   # Prix Hocquart G3, 4th Grand Prix de Paris, Prix Niel G2 (11-2) beating Alam
 "Saddadd":          dict(age=4, sex="C", trainer="R Varian",     form=6.5, dist=7,  fast=7, soft=6, conn=7),   # Grosser Preis von Baden G1 (good, 12f), Gordon Richards G3; Pinatubo colt
 "Meisho Tabaru":    dict(age=5, sex="C", trainer="M Ishibashi",  form=8.0, dist=6,  fast=7, soft=6, conn=5),   # AUDIT: won 2026 Takarazuka Kinen on YIELDING ground (so soft 4 -> 6); 2200m; no prep
 "Admire Terra":     dict(age=5, sex="C", trainer="Y Tomomichi",  form=6.5, dist=4,  fast=7, soft=5, conn=5),   # AUDIT: Hanshin Daishoten is a G2 (3000m), not G1; 3rd Tenno Sho Spring G1 (3200m) beaten 0.1s; a stayer; no prep
 "Bright Light":     dict(age=3, sex="C", trainer="A Suborics",   form=6.5, dist=7,  fast=6, soft=6, conn=5),   # AUDIT: age 3 (was 4); 2nd Grosser Preis von Berlin G1 (neck), 3rd Baden G1; rating 114
 "Arrow Eagle":      dict(age=5, sex="C", trainer="J-C Rouget",   form=5.5, dist=7,  fast=6, soft=6, conn=8),   # AUDIT: age 5 (was 4); 2025 Prix Royal-Oak G1, 6th in 2025 Arc at 105/1; Rouget's final runner; 2026 form not found
 "Chestnut Rocket":  dict(age=4, sex="C", trainer="A Karkosa",    form=5.0, dist=6,  fast=6, soft=6, conn=4),   # AUDIT: rating 113, Polish Derby winner, Listed winner, 2nd Grand Prix de Deauville G2
}

W = dict(form=0.368, dist=0.184, ground=0.12, conn=0.12, market=0.20)   # v4 weights x0.8, plus 20% market

# Paddy Power "Final Decs" fixed odds, Thu 1 Oct 2026 20:05 (user screenshot), post-draw. Fractional -> decimal.
# NOTE: a bookmaker price, not the exchange. The Betfair screenshot (20:04) was suspended with no prices.
ODDS = {"Daryz": 7/4, "Kalpana": 5, "Maltese Cross": 5, "Thundering On": 8, "Diamond Necklace": 10,
        "Varandir": 10, "Benvenuto Cellini": 12, "Minnie Hauk": 20, "Saddadd": 20, "Friendly Soul": 20,
        "Bay City Roller": 25, "Meisho Tabaru": 33, "Admire Terra": 66, "Bright Light": 100,
        "Arrow Eagle": 100, "Chestnut Rocket": 150}
IMPLIED = {n: 1 / (f + 1) for n, f in ODDS.items()}
OVERROUND = sum(IMPLIED.values())   # >1 is the bookmaker margin; scaling by the favourite cancels it out
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
    """19 of the last 24 winners came from stalls 1-8; stalls 1-3 filled the places in 2025."""
    if stall is None:
        return 0.0
    if stall <= 3:
        return 0.8
    if stall <= 8:
        return 0.5
    if stall <= 12:
        return -0.2
    return -0.7


def score(name, going, draw):
    r = R[name]
    market = 10 * IMPLIED[name] / max(IMPLIED.values())   # favourite = 10
    s = (W["form"] * r["form"] + W["dist"] * r["dist"] + W["ground"] * r[going]
         + W["conn"] * r["conn"] + W["market"] * market)
    return round(s + trend_adjust(name, r) + draw_adjust(draw.get(name)), 2)


def rank(going, draw):
    # ties broken by 2026 form score
    return sorted(R, key=lambda n: (score(n, going, draw), R[n]["form"]), reverse=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--going", choices=["fast", "soft"], help="default: print both")
    ap.add_argument("--draw", default="", help='e.g. "Daryz=1,Kalpana=9"')
    a = ap.parse_args()
    draw = {k: int(v) for k, v in (p.split("=") for p in a.draw.split(",") if p)}
    for going in ([a.going] if a.going else ["fast", "soft"]):
        print(f"\n== going: {going}  |  draw: {'applied' if draw else 'NOT applied'}  |  book overround {OVERROUND:.3f} ==")
        for i, n in enumerate(rank(going, draw)[:9], 1):
            print(f"{i:>2}. {n:<18} {score(n, going, draw):.2f}")
