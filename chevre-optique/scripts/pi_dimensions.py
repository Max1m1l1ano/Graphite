"""
Partie III : π, √2 et les dimensions. Calculs et figure.

    python3 scripts/pi_dimensions.py

Écrit resultats/pi_dimensions.md et figures/c1_pi_dimensions.png.
"""

import os
import sys

import matplotlib.pyplot as plt
import mpmath as mp

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties I et II)

mp.mp.dps = 40
ICI = os.path.dirname(os.path.abspath(__file__))
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, d=10):
    return mp.nstr(x, d).replace(".", ",")


PI = mp.pi
V = lambda n: PI ** (mp.mpf(n) / 2) / mp.gamma(mp.mpf(n) / 2 + 1)  # boule unité de dimension n

# ---------------------------------------------------------------------------
# 1. La suite proposée : 3 + √2/10 + √3/100 + …
# ---------------------------------------------------------------------------
ligne("## 1. La suite 3 + √2/10 + √3/100 + √4/1000 + …\n")
ligne("| étape | somme partielle | écart à π |")
ligne("|---:|---|---:|")
suite, s = [], mp.mpf(3)
for n in range(1, 11):
    if n >= 2:
        s += mp.sqrt(n) / mp.mpf(10) ** (n - 1)
    suite.append(s)
    ligne(f"| {n} | {fr(s, 14)} | {mp.nstr(s - PI, 3)} |")
S = 3 + 10 * (mp.polylog(-0.5, mp.mpf(1) / 10) - mp.mpf(1) / 10)
ligne(f"\nLimite : 3 + 10·(Li₋₁/₂(1/10) − 1/10) = {fr(S, 25)} (π = {fr(PI, 25)}, écart {mp.nstr(S - PI, 6)})")

# ---------------------------------------------------------------------------
# 2. Retenues gloutonnes : on force la convergence vers une cible
# ---------------------------------------------------------------------------
ligne("\n## 2. Retenues gloutonnes 3 + Σ c_k √k / 10^(k−1)\n")


def gloutonne(cible, K=20):
    reste, chiffres, approx = cible - 3, [], []
    for k in range(2, K + 1):
        w = mp.sqrt(k) / mp.mpf(10) ** (k - 1)
        c = int(mp.floor(reste / w))
        chiffres.append(c)
        reste -= c * w
        approx.append(cible - reste)
    return chiffres, approx


for nom, cible in [("π", PI), ("√10", mp.sqrt(10)), ("e + 0,42", mp.e + mp.mpf("0.42"))]:
    ligne(f"- {nom} : retenues {gloutonne(cible)[0]}")

# ---------------------------------------------------------------------------
# 3. Les vraies formules qui partent de 3 ou de √2
# ---------------------------------------------------------------------------
ligne("\n## 3. Archimède (hexagone), Viète (√2 imbriquées), Nilakantha (3 + corrections), Wallis (dimensions)\n")
arch, a, b, n = [], 2 * mp.sqrt(3), mp.mpf(3), 6
for _ in range(10):
    arch.append((n, b, a))
    a = 2 * a * b / (a + b)
    b = mp.sqrt(a * b)
    n *= 2
viete, x, prod = [], mp.sqrt(2), mp.sqrt(2) / 2
for _ in range(12):
    viete.append(2 / prod)
    x = mp.sqrt(2 + x)
    prod *= x / 2
nila, s = [], mp.mpf(3)
for k in range(1, 13):
    s += (-1) ** (k + 1) * mp.mpf(4) / ((2 * k) * (2 * k + 1) * (2 * k + 2))
    nila.append(s)
wallis, p = [], mp.mpf(2)
for k in range(1, 13):
    p *= mp.mpf(2 * k) ** 2 / ((2 * k - 1) * (2 * k + 1))
    wallis.append(p)
ligne("| étape | Archimède (inscrit) | Viète | Nilakantha | Wallis |")
ligne("|---:|---|---|---|---|")
for i in range(8):
    ligne(f"| {i + 1} | {fr(arch[i][1], 9)} ({arch[i][0]} côtés) | {fr(viete[i], 9)} | {fr(nila[i], 9)} | {fr(wallis[i], 9)} |")
ligne(f"\n96 côtés : {fr(arch[4][1], 7)} < π < {fr(arch[4][2], 7)}")
ligne("Échelle des dimensions : n·V_n / (2·V_(n−2)) = " + " ; ".join(f"n = {k} : {fr(k * V(k) / (2 * V(k - 2)), 16)}" for k in (3, 5, 7)))

# ---------------------------------------------------------------------------
# 4. Les sphères sur toutes les dimensions
# ---------------------------------------------------------------------------
ligne("\n## 4. Sommes sur toutes les dimensions\n")
tot = mp.e ** PI * (1 + mp.erf(mp.sqrt(PI)))
ligne(f"- Σ V_n (n ≥ 0) = e^π(1 + erf √π) = {fr(tot, 20)}")
ligne(f"- dimensions paires : Σ π^k/k! = e^π = {fr(mp.e ** PI, 20)}")
ligne(f"- dimensions impaires : e^π·erf √π = {fr(mp.e ** PI * mp.erf(mp.sqrt(PI)), 20)}")
ligne(f"- rayon de la boule de volume 1 : R_n·√(2πe/n) → 1 ; V_n^(1/n)·√n → √(2πe) = {fr(mp.sqrt(2 * PI * mp.e), 10)}")

# ---------------------------------------------------------------------------
# 5. φ, ρ et la chèvre
# ---------------------------------------------------------------------------
rho = mp.findroot(lambda t: t ** 3 - t - 1, 1.3)
phi = (1 + mp.sqrt(5)) / 2
r7 = mp.mpf("1.32467963586841591522614")
ligne("\n## 5. Nombre d'or, nombre plastique\n")
ligne(f"- ρ (x³ = x + 1) = {fr(rho, 15)} ; corde de la chèvre en dimension 7 : r₇ = {fr(r7, 15)} ;"
      f" écart {mp.nstr(rho - r7, 4)} ; r₇³ − r₇ − 1 = {mp.nstr(r7 ** 3 - r7 - 1, 4)} ≠ 0")
ligne(f"- φ (x² = x + 1) = {fr(phi, 15)} : croisement sphère/paraboloïde en z = R/φ ; sommets de l'icosaèdre (0, ±1, ±φ)")
ligne(f"- π − 3 = {fr(PI - 3, 12)} ; √2/10 = {fr(mp.sqrt(2) / 10, 12)}")

with open(os.path.join(ICI, "..", "resultats", "pi_dimensions.md"), "w") as fh:
    fh.write("# Résultats de la partie III (générés par scripts/pi_dimensions.py)\n\n" + "\n".join(md) + "\n")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(16, 4.9), gridspec_kw={"wspace": 0.3})
ax = axs[0]
series = [
    ("ta suite : plafonne à 0,0194", [abs(v - PI) for v in suite], F.ORANGE),
    ("retenues gloutonnes (n'importe quel nombre)", [abs(v - PI) for v in gloutonne(PI)[1][:10]], F.MUTED),
    ("Archimède, depuis l'hexagone", [PI - t[1] for t in arch], F.BLEU),
    ("Viète, racines de 2", [abs(v - PI) for v in viete[:10]], "#104281"),
    ("Nilakantha, 3 + corrections", [abs(v - PI) for v in nila[:10]], F.AQUA),
    ("Wallis, paires de dimensions", [abs(v - PI) for v in wallis[:10]], F.INK),
]
for nom, err, c in series:
    ax.semilogy(range(1, len(err) + 1), [float(max(e, mp.mpf(10) ** -20)) for e in err], "-o", color=c, lw=1.8, ms=4,
                mec=F.SURF, mew=1, label=nom)
ax.set_xlabel("étape")
ax.set_ylabel("|approximation − π|")
ax.set_title("a)  Qui converge vers π ?")
ax.legend(fontsize=8.5, loc="lower left")
ax = axs[1]
cordes = [1.0, 1.15872847301812, 1.22854486373522, 1.26807925667342, 1.29359799636023, 1.31146181902716,
          1.32467963586842, 1.33486242915791, 1.34295179853544, 1.34953543999843, 1.35499938927709,
          1.35960781711644, 1.36354767323759, 1.36695502304279, 1.3699312822237]
ns = range(1, len(cordes) + 1)
ax.plot(ns, cordes, "-o", color=F.BLEU, lw=1.8, ms=5, mec=F.SURF)
ax.axhline(float(mp.sqrt(2)), color=F.INK, lw=1.2, ls=(0, (4, 3)))
ax.axhline(float(rho), color=F.ORANGE, lw=1.2)
F.point(ax, 7, cordes[6], F.ORANGE, 9)
ax.text(1.2, float(mp.sqrt(2)) + 0.008, "√2", fontsize=9.5, color=F.INK)
ax.text(1.2, float(rho) + 0.008, "nombre plastique ρ = 1,324718", fontsize=9, color=F.INK)
ax.annotate("n = 7 : r₇ = 1,324680\nécart 3,8·10⁻⁵ (coïncidence)", xy=(7, cordes[6]), xytext=(8.3, 1.2), fontsize=9,
            color=F.INK, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlabel("dimension n")
ax.set_ylabel("corde de la chèvre r_n / R")
ax.set_title("b)  La corde frôle ρ en dimension 7")
ax.set_ylim(0.97, 1.46)
ax = axs[2]
N = list(range(0, 31))
cum, cum_p, cum_i = [], [], []
a_, p_, i_ = mp.mpf(0), mp.mpf(0), mp.mpf(0)
for n in N:
    a_ += V(n)
    if n % 2 == 0:
        p_ += V(n)
    else:
        i_ += V(n)
    cum.append(float(a_))
    cum_p.append(float(p_))
    cum_i.append(float(i_))
ax.plot(N, cum, color=F.BLEU, lw=2.2, label="toutes → 45,9993")
ax.plot(N, cum_p, color=F.ORANGE, lw=1.8, label="paires → e^π")
ax.plot(N, cum_i, color=F.AQUA, lw=1.8, label="impaires → e^π·erf √π")
for n in (5, 7):
    F.point(ax, n, cum[n], F.INK, 7)
ax.annotate("pics des volumes et des aires\n(n = 5 et 7, pour R = 1)", xy=(7, cum[7]), xytext=(14.5, 9), fontsize=9,
            color=F.INK2, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlabel("dimension n (somme jusqu'à n)")
ax.set_ylabel("somme des volumes des boules unités")
ax.set_title("c)  Toutes les dimensions ensemble")
ax.legend(fontsize=9, loc="center right", bbox_to_anchor=(1.0, 0.66))
ax.set_ylim(-1, 52)
F.sauver(fig, "c1_pi_dimensions.png")
