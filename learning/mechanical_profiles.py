"""Mechanical, judgement-free profiles for a race card (v1 of the 'learn properly' framework).
Every profile is computed only from numbers on the racecard, so the result cannot bias it.
Usage: python3 learning/mechanical_profiles.py races/<race>/card.py [RESULT as comma list of horses 1st,2nd,...]"""
import importlib.util, sys, math

FORM_PTS = {"1": 10, "2": 8, "3": 6, "4": 4, "5": 3, "6": 2, "7": 1}   # 0, 8, 9 and others score 0


def load(path):
    sp = importlib.util.spec_from_file_location("card", path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m.RUNNERS


def recent_form(f):
    last = [c for c in f if c.isdigit()][-3:][::-1]         # latest first
    w = [0.5, 0.3, 0.2][:len(last)]
    return sum(wi * FORM_PTS.get(c, 0) for wi, c in zip(w, last)) / (sum(w) or 1)


def z(d):
    v = list(d.values()); mu = sum(v) / len(v); sd = math.sqrt(sum((x - mu) ** 2 for x in v) / len(v)) or 1
    return {k: (x - mu) / sd for k, x in d.items()}


def profiles(R):
    n = len(R)
    mkt = {h: 1 / (r["fc"] + 1) for h, r in R.items()}
    rpr = {h: r["RPR"] for h, r in R.items()}
    orr = {h: r["OR"] for h, r in R.items()}
    frm = {h: recent_form(r["form"]) for h, r in R.items()}
    edge = {h: r["RPR"] - r["OR"] for h, r in R.items()}      # how far the horse's best figure is above its handicap mark
    drw = {h: -r["stall"] for h, r in R.items()}
    zm, zr, zf, ze, zd = z(mkt), z(rpr), z(frm), z(edge), z(drw)
    P = {
        "market only (forecast)": mkt,
        "RPR only": rpr,
        "official rating only": orr,
        "recent form only (last 3)": frm,
        "handicap edge (RPR - OR)": edge,
        "low stall only": drw,
        "composite A: market+RPR+form+edge": {h: zm[h] + zr[h] + zf[h] + ze[h] for h in R},
        "composite B: A + draw": {h: zm[h] + zr[h] + zf[h] + ze[h] + zd[h] for h in R},
        "composite C: market+form": {h: zm[h] + zf[h] for h in R},
    }
    return P


def order(score):
    return [h for h, _ in sorted(score.items(), key=lambda kv: -kv[1])]


if __name__ == "__main__":
    R = load(sys.argv[1]); P = profiles(R)
    res = sys.argv[2].split(",") if len(sys.argv) > 2 else None
    for name, s in P.items():
        o = order(s)
        line = f"{name:38} top5: " + ", ".join(o[:5])
        if res:
            r1 = o[0] == res[0]; t3 = len(set(o[:3]) & set(res[:3])); t4 = len(set(o[:4]) & set(res[:4]))
            ranks = [o.index(h) + 1 for h in res[:4]]
            line += f"  | winner {'Y' if r1 else 'n'}, top3 overlap {t3}/3, top4 overlap {t4}/4, ranks of actual 1-4: {ranks}"
        print(line)
