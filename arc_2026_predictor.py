"""Rules-based finishing-order predictor: 2026 Qatar Prix de l'Arc de Triomphe (v3, no bookmaker odds).

Each runner gets 0-10 scores from hand-written rules; a weighted sum ranks them.
Ground and draw are scenarios because both were unconfirmed at the time of writing.
Run:  python3 arc_2026_predictor.py                          (both ground scenarios, no draw)
      python3 arc_2026_predictor.py --draw "Daryz=1,Kalpana=9"   (once stalls are official)
      python3 arc_2026_predictor.py --going soft
"""
import argparse

# form: quality of 2026 results   dist: proven at 12f / Longchamp
# fast / soft: suitability for good-to-firm / good-to-soft-or-softer ground
# conn: trainer/jockey big-race record. Bookmaker odds are deliberately NOT used.
R = {
 "Daryz":            dict(age=4, sex="C", trainer="F-H Graffard", form=9.5, dist=10, fast=9, soft=9, conn=8,),   # 2025 Arc winner (very soft), 2026 Foy on good-to-firm by 1.5L
 "Maltese Cross":    dict(age=3, sex="C", trainer="W Haggas",     form=9.0, dist=8,  fast=8, soft=5, conn=8),   # Derby 2nd, GP Paris, Gt Voltigeur (RPR 124); lost twice when soft in going
 "Kalpana":          dict(age=5, sex="F", trainer="A Balding",    form=9.5, dist=8,  fast=9, soft=7, conn=8),   # King George (beat Calandagan 1.5L, GF) + Yorkshire Oaks
 "Diamond Necklace": dict(age=3, sex="F", trainer="A O'Brien",    form=7.5, dist=4,  fast=7, soft=7, conn=9),   # first defeat last time; first try at 12f; money coming
 "Friendly Soul":    dict(age=5, sex="F", trainer="J&T Gosden",   form=7.5, dist=8,  fast=7, soft=7, conn=9,),   # Prix Vermeille (made all), 2024 Prix de l'Opera: course form
 "Benvenuto Cellini":dict(age=3, sex="C", trainer="A O'Brien",    form=7.0, dist=8,  fast=7, soft=7, conn=9,),   # Irish Derby, 3rd King George, 5th Niel
 "Minnie Hauk":      dict(age=4, sex="F", trainer="A O'Brien",    form=6.5, dist=9,  fast=7, soft=7, conn=9,),   # 2025 Arc head 2nd; mixed 2026
 "Bay City Roller":  dict(age=4, sex="C", trainer="G Scott",      form=7.0, dist=8,  fast=6, soft=9, conn=6,),   # 2nd to Daryz in Foy; both G1 wins on soft; 75% to run, wants rain
 "Varandir":         dict(age=3, sex="C", trainer="F-H Graffard", form=6.5, dist=8,  fast=7, soft=7, conn=7,), # Prix Niel winner
 "Saddadd":          dict(age=4, sex="C", trainer="R Varian",     form=6.0, dist=7,  fast=7, soft=7, conn=7,), # Grosser Preis von Baden
 "Meisho Tabaru":    dict(age=5, sex="C", trainer="Japan",        form=8.0, dist=6,  fast=7, soft=4, conn=5,), # 2x Takarazuka; no prep
 "Admire Terra":     dict(age=5, sex="C", trainer="Japan",        form=7.0, dist=5,  fast=7, soft=4, conn=5,), # Hanshin Daishoten; no prep
 "Bright Light":     dict(age=4, sex="C", trainer="A Suborics",   form=5.5, dist=6,  fast=6, soft=6, conn=5,), # multiple G1-placed
 "Thundering On":    dict(age=4, sex="C", trainer="J O'Brien",    form=5.0, dist=6,  fast=6, soft=6, conn=5,),
 "Arrow Eagle":      dict(age=4, sex="C", trainer="J-C Rouget",   form=5.0, dist=6,  fast=6, soft=6, conn=6,),
 "Chestnut Rocket":  dict(age=4, sex="C", trainer="A Karkosa",    form=4.5, dist=5,  fast=6, soft=6, conn=4,),
}

W = dict(form=0.46, dist=0.23, ground=0.15, conn=0.15)   # v2 weights with market removed, rescaled to 1.0
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
    s = (W["form"] * r["form"] + W["dist"] * r["dist"] + W["ground"] * r[going]
         + W["conn"] * r["conn"])
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
        print(f"\n== going: {going}  |  draw: {'applied' if draw else 'NOT applied'} ==")
        for i, n in enumerate(rank(going, draw)[:9], 1):
            print(f"{i:>2}. {n:<18} {score(n, going, draw):.2f}")
