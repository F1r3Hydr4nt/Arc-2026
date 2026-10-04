"""Score simplified model 'profiles' and baselines against a known finishing order (Arc 2026).

Inputs are the PRE-RACE v13/v14 data (frozen before the race): my 0-10 judgement scores, ratings, jockeys and the race-morning prices.
Only 1st-8th are known, so every other runner is treated as tied behind them. ONE race: diagnostics, not proof.
Run: python3 learning/score_profiles.py
"""
import importlib.util as u
import math

DRAW = {"Benvenuto Cellini": 1, "Chestnut Rocket": 2, "Thundering On": 3, "Varandir": 4, "Daryz": 5, "Kalpana": 6, "Friendly Soul": 7,
        "Bright Light": 8, "Saddadd": 9, "Minnie Hauk": 10, "Maltese Cross": 11, "Admire Terra": 12, "Meisho Tabaru": 13,
        "Arrow Eagle": 14, "Bay City Roller": 15, "Diamond Necklace": 16}
RESULT = ["Daryz", "Bay City Roller", "Diamond Necklace", "Friendly Soul", "Kalpana", "Maltese Cross", "Varandir", "Thundering On"]


def load(v):
    sp = u.spec_from_file_location(v, f"versions/{v}/predictor.py"); m = u.module_from_spec(sp); sp.loader.exec_module(m); return m


v13, v14 = load("v13"), load("v14")
names = list(v14.R)
G = "good"


def comp(m, n):  # per-horse components on the 'good' ground setting
    r = m.R[n]
    return dict(form=r["form"], dist=r["dist"], ground=(r["fast"] + r["soft"]) / 2, conn=r["conn"], jockey=m.jockey_score(n),
                rating=m.rating_score(n), market=10 * v13.IMPLIED[n] / max(v13.IMPLIED.values()),
                trend=m.trend_adjust(n, r), draw=m.draw_adjust(DRAW[n]), h2h=m.H2H_STEP * m.H2H_WINS.get(n, 0))


C = {n: comp(v14, n) for n in names}


def combo(weights, extras=("trend", "draw", "h2h")):
    tot = sum(weights.values())
    return {n: sum(w * C[n][k] for k, w in weights.items()) / tot + sum(C[n][e] for e in extras) for n in names}


W14 = dict(form=0.275, rating=0.2125, dist=0.1875, ground=0.125, conn=0.10, jockey=0.10)
W13 = dict(form=0.22, rating=0.17, dist=0.15, ground=0.10, conn=0.08, jockey=0.08, market=0.20)
PROFILES = {
    "market only (race-morning prices)": {n: C[n]["market"] for n in names},
    "form only": {n: C[n]["form"] for n in names},
    "ground only": {n: C[n]["ground"] for n in names},
    "rating only": {n: C[n]["rating"] for n in names},
    "distance only": {n: C[n]["dist"] for n in names},
    "core: form+distance+ground": combo(dict(form=.275, dist=.1875, ground=.125), extras=()),
    "core + market": combo(dict(form=.22, dist=.15, ground=.10, market=.20), extras=()),
    "v14 full (odds-free)": combo(W14),
    "v14 without age/trend adj": combo(W14, extras=("draw", "h2h")),
    "v14 without draw": combo(W14, extras=("trend", "h2h")),
    "v14 without any extras": combo(W14, extras=()),
    "v14 without jockey+trainer": combo({k: v for k, v in W14.items() if k not in ("conn", "jockey")}),
    "v13 full (with prices)": combo(W13),
}


def ranks(score):
    order = sorted(names, key=lambda n: (-score[n], -C[n]["form"]))
    return {n: i + 1 for i, n in enumerate(order)}, order


def spearman(score):
    pos = {n: (RESULT.index(n) + 1 if n in RESULT else 12.5) for n in names}
    def rk(d):
        s = sorted(d.items(), key=lambda kv: kv[1]); out = {}; i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and s[j + 1][1] == s[i][1]: j += 1
            for k in range(i, j + 1): out[s[k][0]] = (i + j) / 2 + 1
            i = j + 1
        return out
    a, b = rk({n: -score[n] for n in names}), rk(pos)
    ma, mb = sum(a.values()) / len(a), sum(b.values()) / len(b)
    cov = sum((a[n] - ma) * (b[n] - mb) for n in names)
    return cov / math.sqrt(sum((a[n] - ma) ** 2 for n in names) * sum((b[n] - mb) ** 2 for n in names))


def table():
    rows = ["| Profile | Winner | Actual top 3 in my top 3 | Actual top 4 in my top 4 | Actual 1st-7th in my top 7 | Avg rank of actual 1st-7th | Spearman |", "|---|---|---|---|---|---|---|"]
    for name, s in PROFILES.items():
        r, order = ranks(s)
        w = "yes" if order[0] == RESULT[0] else "no"
        t3 = len(set(order[:3]) & set(RESULT[:3])); t4 = len(set(order[:4]) & set(RESULT[:4])); t7 = len(set(order[:7]) & set(RESULT[:7]))
        avg = sum(r[n] for n in RESULT[:7]) / 7
        rows.append(f"| {name} | {w} | {t3}/3 | {t4}/4 | {t7}/7 | {avg:.1f} | {spearman(s):+.2f} |")
    return "\n".join(rows)


if __name__ == "__main__":
    print(table())
