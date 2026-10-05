"""
Partie IV : la suite des trois solides. Calculs et figure.

    python3 scripts/trois_solides.py

Écrit resultats/trois_solides.md et figures/d1_trois_solides.png.

Conventions : en dimension n, l'hémisphère de rayon 1, le cylindre qui le
contient (rayon 1, hauteur 1) et le cône inscrit dans ce cylindre (sommet O,
le centre de la base). On compare tout au cylindre :
    h_n = hémisphère / cylindre = W_n / 2,    c_n = cône / cylindre = 1/n,
et l'« anneau » d'Archimède est cylindre − cône (rapport 1 − c_n).
"""

import os
import sys
from fractions import Fraction
from math import comb

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(__file__))
import chevre as ch  # noqa: E402
import figures as F  # noqa: E402  (style et palette des parties I à III)

mp.mp.dps = 40
ICI = os.path.dirname(os.path.abspath(__file__))
PI = mp.pi
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, d=10):
    return mp.nstr(x, d).replace(".", ",")


def h(n):
    """Hémisphère / cylindre en dimension n : V_n / (2 V_(n−1)) = W_n / 2."""
    return ch.W_pi(n) / 2


def c(n):
    """Cône / cylindre en dimension n."""
    return mp.mpf(1) / n


def h_exact(n):
    """h_n exact : une fraction (n impair) ou une fraction de π (n pair)."""
    if n % 2:
        v = Fraction(1)
        for m in range(3, n + 1, 2):
            v *= Fraction(m - 1, m)
        return str(v)
    v = Fraction(comb(n, n // 2), 2 ** (n + 1))
    return f"{v.numerator}π/{v.denominator}" if v.numerator > 1 else f"π/{v.denominator}"


# ---------------------------------------------------------------------------
# 1. Les trois solides, dimension par dimension
# ---------------------------------------------------------------------------
ligne("## 1. Les trois solides en dimension n (rapports au cylindre)\n")
ligne("| n | hémisphère | cône | anneau = cylindre − cône | hémisphère − ½ cylindre | hémisphère − ½ anneau |")
ligne("|---:|---|---|---|---:|---:|")
for n in range(1, 13):
    ligne(f"| {n} | {h_exact(n)} = {fr(h(n), 6)} | 1/{n} | {fr(1 - c(n), 6)} | {fr(h(n) - mp.mpf(1) / 2, 4)} |"
          f" {fr(h(n) - (1 - c(n)) / 2, 4)} |")
ligne("\nBalance d'Archimède (hémisphère = cylindre − cône), écart h_n + c_n − 1 : "
      + " ; ".join(f"n = {n} → {fr(h(n) + c(n) - 1, 4)}" for n in range(1, 7)))

ligne("\n## 2. Équations dimensionnelles (résidus, 40 chiffres)\n")
r1 = max(abs(h(n - 1) * h(n) - PI / 2 * c(n)) for n in range(2, 40))
r2 = max(abs(h(n) - (1 - c(n)) * h(n - 2)) for n in range(2, 40))
ligne(f"- h_(n−1)·h_n = (π/2)·c_n, n = 2…39 : résidu max {mp.nstr(r1, 3)}")
ligne(f"- h_n = (1 − c_n)·h_(n−2), n = 2…39 : résidu max {mp.nstr(r2, 3)}")
ligne("- volume des boules unités : V_n / V_(n−1) = 2·h_n ; aire des sphères : S_n / S_(n−1) = 2·h_n / (1 − c_n)")

# ---------------------------------------------------------------------------
# 3. La suite des trois solides
# ---------------------------------------------------------------------------


def suite(N, facon, K):
    """Sommes partielles de π = (polygone à N côtés) × Σ_k (trois solides en dim 2k+1) × s^(2k)."""
    th = PI / N
    s2 = mp.sin(th) ** 2
    if facon == "aire":  # aire du polygone inscrit × Σ h_(2k+1) s^(2k)
        base, terme = N * mp.sin(th) * mp.cos(th), lambda k: h(2 * k + 1) * s2 ** k
    elif facon == "perimetre":  # demi-périmètre inscrit × Σ c²/h · s^(2k)
        base, terme = N * mp.sin(th), lambda k: c(2 * k + 1) ** 2 / h(2 * k + 1) * s2 ** k
    elif facon == "exterieur":  # polygone circonscrit × (1 − Σ c_(2k+1) h_(2k−1) s^(2k))
        base, terme = N * mp.tan(th), lambda k: 1 if k == 0 else -c(2 * k + 1) * h(2 * k - 1) * s2 ** k
    elif facon == "alternee":  # Madhava–Gregory : Σ (−1)^k c_(2k+1) tan^(2k)
        t2 = mp.tan(th) ** 2
        base, terme = N * mp.tan(th), lambda k: (-1) ** k * c(2 * k + 1) * t2 ** k
    sommes, acc = [], mp.mpf(0)
    for k in range(K):
        acc += terme(k)
        sommes.append(base * acc)
    return sommes


ligne("\n## 3. La suite des trois solides\n")
ligne("### 3.1 Depuis le carré : π = 2 + ⅓(2 + ⅖(2 + 3/7(2 + …)))\n")
emboite = []
for K in range(0, 41):
    x = mp.mpf(2)
    for k in range(K, 0, -1):
        x = 2 + mp.mpf(k) / (2 * k + 1) * x
    emboite.append(x)
carre = suite(4, "aire", 41)
ligne(f"Contrôle : forme emboîtée = somme Σ 2·h_(2k+1)/2^k (écart max {mp.nstr(max(abs(a - b) for a, b in zip(emboite, carre)), 3)})\n")
ligne("| étages | dimension atteinte | valeur | écart à π |")
ligne("|---:|---:|---|---:|")
for K in (0, 1, 2, 3, 4, 5, 10, 20, 30, 40):
    ligne(f"| {K} | {2 * K + 1} | {fr(emboite[K], 15)} | {mp.nstr(emboite[K] - PI, 3)} |")

ligne("\n### 3.2 Depuis l'hexagone (Newton, arc sinus de 1/2)\n")
termes, tot = [], Fraction(0)
for k in range(7):
    n = 2 * k + 1
    t = 3 * Fraction(1, 4 ** k) / (n * n * Fraction(h_exact(n)))
    tot += t
    termes.append(f"{t}")
ligne("π = " + " + ".join(termes) + " + …")
ligne(f"Somme de ces 7 termes : {fr(mp.mpf(tot.numerator) / tot.denominator, 15)} (écart {mp.nstr(mp.mpf(tot.numerator) / tot.denominator - PI, 3)})")
aire6 = [Fraction(h_exact(2 * k + 1)) / 4 ** k for k in range(6)]
u = 2 - mp.sqrt(3)  # dodécagone inscrit : aire exactement 3, s² = sin²15° = (2 − √3)/4
coef12 = [3 * Fraction(h_exact(2 * k + 1)) / 4 ** k for k in range(8)]  # π = Σ coef_k · (2 − √3)^k
som12, acc = [], mp.mpf(0)
for k, q in enumerate(coef12):
    acc += mp.mpf(q.numerator) / q.denominator * u ** k
    som12.append(acc)
ligne("Version aire : π = (3√3/2) × (" + " + ".join(str(t) for t in aire6) + " + …) = (3√3/2) Σ 1/((2k+1)·C(2k,k))")
ligne("\n### 3.3 Depuis le dodécagone (aire exactement 3)\n")
ligne("π = " + " + ".join(f"({q})·(2 − √3)^{k}" for k, q in enumerate(coef12)) + " + …")
ligne("| retenues | valeur | écart à π |")
ligne("|---:|---|---:|")
for k, v in enumerate(som12):
    ligne(f"| {k} | {fr(v, 15)} | {mp.nstr(v - PI, 3)} |")

ligne("\n### 3.4 Tous les polygones (raison s² = sin²(π/N))\n")
ligne("| N | s² | intérieur, aire (départ) | intérieur, demi-périmètre (départ) | extérieur (départ) |"
      " termes pour 10 chiffres (int. périmètre) |")
ligne("|---:|---|---|---|---|---:|")
for N in (3, 4, 5, 6, 8, 12, 96):
    p = suite(N, "perimetre", 80)
    K10 = next(k + 1 for k, v in enumerate(p) if abs(v - PI) < 1e-10)
    ligne(f"| {N} | {fr(mp.sin(PI / N) ** 2, 6)} | {fr(suite(N, 'aire', 1)[0], 8)} | {fr(p[0], 8)} |"
          f" {fr(suite(N, 'exterieur', 1)[0], 8)} | {K10} |")
ligne(f"\nPentagone : s² = (3 − φ)/4 = {fr((3 - (1 + mp.sqrt(5)) / 2) / 4, 12)} ; sin²36° = {fr(mp.sin(PI / 5) ** 2, 12)}")
p96, p48 = 96 * mp.sin(PI / 96), 48 * mp.sin(PI / 48)
s = mp.sin(PI / 96)
ligne(f"96 côtés (Archimède) : {fr(p96, 12)} (écart {mp.nstr(p96 - PI, 3)}) ; + retenue de dimension 3 : "
      f"{fr(96 * (s + s ** 3 / 6), 12)} (écart {mp.nstr(96 * (s + s ** 3 / 6) - PI, 3)}) ; + dimension 5 : "
      f"écart {mp.nstr(96 * (s + s ** 3 / 6 + 3 * s ** 5 / 40) - PI, 3)}")
ligne(f"Huygens–Richardson (4·P96 − P48)/3 = {fr((4 * p96 - p48) / 3, 12)} (écart {mp.nstr((4 * p96 - p48) / 3 - PI, 3)})")
leib = suite(4, "alternee", 1000)
ligne(f"Carré par l'extérieur, série alternée (Leibniz) : écart après 10, 100, 1000 termes : "
      f"{mp.nstr(leib[9] - PI, 3)} ; {mp.nstr(leib[99] - PI, 3)} ; {mp.nstr(leib[999] - PI, 3)}")
ligne(f"Hexagone par l'extérieur, série alternée (Madhava) : écart après 10 termes : {mp.nstr(suite(6, 'alternee', 10)[-1] - PI, 3)}")
ligne(f"Babylone 3 + 1/8 = {fr(mp.mpf(25) / 8, 6)} ; Égypte 4·(8/9)² = 256/81 = {fr(mp.mpf(256) / 81, 8)} ;"
      f" limite de la suite 3 + √2/10 + √3/100 + … = 3,160992928 (écart à 256/81 : {fr(mp.mpf('3.160992928') - mp.mpf(256) / 81, 3)})")

# ---------------------------------------------------------------------------
# 4. Les partages : la corde qui prend la moitié de chaque solide depuis O
# ---------------------------------------------------------------------------
sig = lambda n, t: ch.W(n - 2, t) / ch.W_pi(n - 2)  # part de la sphère S^(n−1) à moins de t de l'axe


def fraction_solide(solide, n, r):
    """Part du solide (dimension n) à distance ≤ r de O ; intégrale sur la hauteur z (scipy)."""
    m, zmax = (n - 1) / 2, min(1.0, r)
    if solide == "cylindre":
        f, vol = (lambda z: min(1.0, r * r - z * z) ** m), 1.0
    elif solide == "cone":
        f, vol = (lambda z: max(0.0, min(z * z, r * r - z * z)) ** m), 1.0 / n
    else:  # anneau = cylindre − cône
        f, vol = (lambda z: max(0.0, min(1.0, r * r - z * z) ** m - z ** (n - 1)) if r * r > 2 * z * z else 0.0), 1 - 1.0 / n
    coupures = [p for p in (np.sqrt(max(r * r - 1, 0)), r / np.sqrt(2)) if 0 < p < zmax]
    return quad(f, 0, zmax, points=coupures or None, limit=400, epsabs=1e-14, epsrel=1e-12)[0] / vol


def corde_solide(solide, n):
    if solide == "hemisphere":
        return 2.0 ** (-1.0 / n)
    return brentq(lambda r: fraction_solide(solide, n, r) - 0.5, 1e-6, 2.5, xtol=1e-14)


def corde_close(solide, n):
    """Formes closes, valables tant que la corde reste ≤ R (la boule ne touche pas la paroi)."""
    if solide == "hemisphere":
        return mp.mpf(2) ** (-mp.mpf(1) / n)
    if solide == "cylindre":
        return ch.W_pi(n) ** (-mp.mpf(1) / n)
    if solide == "cone":
        return (1 / (2 * n * ch.W_pi(n) * sig(n, PI / 4))) ** (mp.mpf(1) / n)
    return ((1 - mp.mpf(1) / n) / (2 * ch.W_pi(n) * (mp.mpf(1) / 2 - sig(n, PI / 4)))) ** (mp.mpf(1) / n)


SOLIDES = ["hemisphere", "cylindre", "cone", "anneau"]
NOMS = {"hemisphere": "hémisphère", "cylindre": "cylindre", "cone": "cône", "anneau": "anneau", "chevre": "chèvre"}
LIM = {"hemisphere": 1.0, "cylindre": np.sqrt(5) / 2, "cone": np.sqrt(2), "anneau": np.sqrt(5) / 2, "chevre": np.sqrt(2)}
KAPPA = {"hemisphere": ("ln 2", np.log(2)), "cylindre": ("4/5", 0.8), "cone": ("ln(2+√2)", np.log(2 + np.sqrt(2))),
         "anneau": ("1", 1.0), "chevre": ("1/2", 0.5)}
NS = list(range(2, 16))
cordes = {s: {n: corde_solide(s, n) for n in NS} for s in SOLIDES}
cordes["chevre"] = {n: float(ch.corde_moitie_mp(n)) for n in NS}

ligne("\n## 4. Les partages : corde de moitié depuis O (R = 1)\n")
ligne("| n | hémisphère | cylindre | cône | anneau | chèvre (piquet au bord) |")
ligne("|---:|---|---|---|---|---|")
for n in NS:
    ligne(f"| {n} | " + " | ".join(f"{cordes[s][n]:.6f}".replace(".", ",") for s in SOLIDES + ["chevre"]) + " |")
ecart_close = max(abs(float(corde_close(s, n)) - cordes[s][n]) for s in SOLIDES for n in NS if corde_close(s, n) <= 1)
ligne(f"\nFormes closes (tant que la corde ≤ R) contre calcul direct : écart max {ecart_close:.1e}")
for s in ("cylindre", "cone", "anneau"):
    n0 = next(n for n in NS if cordes[s][n] > 1)
    ligne(f"- {NOMS[s]} : corde ≤ R jusqu'à n = {n0 - 1}, > R dès n = {n0}")
ligne("- 2D : hémisphère 1/√2 ; cylindre, cône et anneau √(2/π) = " + f"{np.sqrt(2 / np.pi):.10f}".replace(".", ","))
ligne("- 3D : 2^(−1/3) ; (3/4)^(1/3) ; ((2+√2)/4)^(1/3) ; 2^(−1/6)")


def richardson(a, ns):
    A = np.array([[1, 1 / k, 1 / k ** 2][:len(ns)] for k in ns])
    return np.linalg.solve(A, np.array([a[k] for k in ns]))[0]


ligne("\n| solide | limite | n = 7 | extrapolé depuis 5, 7 | depuis 5, 7, 9 | κ prévu | n(1 − r_n/L) à n = 1000 | à n = 2000 |")
ligne("|---|---|---|---|---|---|---|---|")
rich = {}
for s in SOLIDES + ["chevre"]:
    L = LIM[s]
    r2, r3 = richardson(cordes[s], [5, 7]), richardson(cordes[s], [5, 7, 9])
    rich[s] = r3
    k1000, k2000 = [n * (1 - (corde_solide(s, n) if s != "chevre" else ch.corde_moitie(n)) / L) for n in (1000, 2000)]
    ligne(f"| {NOMS[s]} | {L:.6f} | {cordes[s][7]:.6f} | {r2:.6f} ({(r2 - L) / L:+.2%}) | {r3:.6f} ({(r3 - L) / L:+.2%}) |"
          f" {KAPPA[s][0]} = {KAPPA[s][1]:.4f} | {k1000:.4f} | {k2000:.4f} |".replace(".", ","))

# ---------------------------------------------------------------------------
# 5. Convergences comparées à la division des intégrales
# ---------------------------------------------------------------------------
f_u = lambda z: mp.sin(z) - z * mp.cos(z) - PI / 2
beta = mp.findroot(f_u, 1.9)
cU, rhoU = 3 * PI / 4, PI / 4
I1 = 2j * PI / (beta * mp.sin(beta))  # ∮ 1/f = 2πi / f'(β), f'(z) = z sin z


def ullisch(N):
    num, den = mp.mpc(0), mp.mpc(0)
    for j in range(N):
        w = mp.expjpi(2 * mp.mpf(j) / N)
        fz = f_u(cU + rhoU * w)
        num += (cU + rhoU * w) * w / fz
        den += w / fz
    den *= 2j * PI * rhoU / N
    return abs(num * 2j * PI * rhoU / N / den / beta - 1), abs(den / I1 - 1)


PAS = list(range(1, 33))
erreurs = {}
uq = {N: ullisch(N) for N in range(3, 33)}
erreurs["ullisch"] = {N: uq[N][0] for N in uq}
erreurs["ullisch_seule"] = {N: uq[N][1] for N in uq}
erreurs["carre"] = {k + 1: abs(v / PI - 1) for k, v in enumerate(suite(4, "aire", 32))}
erreurs["hexagone"] = {k + 1: abs(v / PI - 1) for k, v in enumerate(suite(6, "perimetre", 32))}
erreurs["pentagone"] = {k + 1: abs(v / PI - 1) for k, v in enumerate(suite(5, "perimetre", 32))}
erreurs["madhava"] = {k + 1: abs(v / PI - 1) for k, v in enumerate(suite(6, "alternee", 32))}
arch, a, b = {}, 2 * mp.sqrt(3), mp.mpf(3)  # Archimède : a circonscrit, b inscrit (demi-périmètres)
for k in PAS:
    arch[k] = abs(b / PI - 1)
    a = 2 * a * b / (a + b)
    b = mp.sqrt(a * b)
erreurs["archimede"] = arch
erreurs["leibniz"] = {k + 1: abs(v / PI - 1) for k, v in enumerate(leib[:32])}
erreurs["wallis"] = {k: abs(2 * h(2 * k + 1) ** 2 / c(2 * k + 1) / PI - 1) for k in PAS}
erreurs["chevre"] = {n: abs(ch.corde_moitie_mp(n) / mp.sqrt(2) - 1) for n in PAS}
erreurs["polygone"] = {N: abs(N * mp.sin(PI / N) / PI - 1) for N in range(3, 33)}
NOMS_CV = {
    "ullisch": "division d'Ullisch (quotient), par point",
    "ullisch_seule": "une seule intégrale d'Ullisch, par point",
    "carre": "trois solides depuis le carré, par étage",
    "pentagone": "trois solides depuis le pentagone (φ), par étage",
    "hexagone": "trois solides depuis l'hexagone, par étage",
    "madhava": "hexagone extérieur alterné (Madhava), par terme",
    "archimede": "Archimède, par doublement",
    "leibniz": "Leibniz (carré extérieur alterné), par terme",
    "wallis": "Wallis : 2·h²/c, par paire de dimensions",
    "chevre": "corde de la chèvre → √2, par dimension",
    "polygone": "polygone inscrit, par côté",
}


def taux(e):
    """Raison géométrique mesurée entre les pas 16 et 32, et pente log-log."""
    r = float((e[32] / e[16]) ** (mp.mpf(1) / 16))
    p = float(mp.log(e[32] / e[16]) / mp.log(2))
    return r, p


ligne("\n## 5. Erreurs relatives comparées\n")
ligne("| méthode | pas 4 | pas 8 | pas 16 | pas 32 | raison mesurée (16 → 32) | pente log-log |")
ligne("|---|---|---|---|---|---|---|")
for cle, nom in NOMS_CV.items():
    e = erreurs[cle]
    r, p = taux(e)
    ligne(f"| {nom} | " + " | ".join(mp.nstr(e[k], 2) for k in (4, 8, 16, 32)) + f" | {r:.3f} | {p:.2f} |".replace(".", ","))
ligne(f"\nPrévisions : (ρ/d) = {fr(rhoU / (mp.findroot(f_u, 4.09) - cU), 6)} ; |β − c|/ρ = {fr(abs(beta - cU) / rhoU, 6)} ;"
      " sin²45° = 0,5 ; sin²36° = 0,3455 ; sin²30° = 0,25 ; tan²30° = 1/3")
ligne(f"Gain de la division au pas 32 : une intégrale seule {mp.nstr(erreurs['ullisch_seule'][32], 3)},"
      f" le quotient {mp.nstr(erreurs['ullisch'][32], 3)}")

ligne("\n## 6. La balance d'Archimède en tranches (3D, règle du point milieu)\n")
ligne("| tranches | erreur sur l'hémisphère | hémisphère − (cylindre − cône), tranche par tranche |")
ligne("|---:|---|---|")
for N in (4, 16, 64, 256):
    zs = [(j + mp.mpf(1) / 2) / N for j in range(N)]
    H = sum(PI * (1 - z * z) for z in zs) / N
    K = sum(PI * z * z for z in zs) / N
    ligne(f"| {N} | {mp.nstr(H - 2 * PI / 3, 3)} | {mp.nstr(H - (PI - K), 3)} |")

with open(os.path.join(ICI, "..", "resultats", "trois_solides.md"), "w") as fh:
    fh.write("# Résultats de la partie IV (générés par scripts/trois_solides.py)\n\n" + "\n".join(md) + "\n")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(15.5, 11), gridspec_kw={"wspace": 0.22, "hspace": 0.3})

# a) les trois solides par dimension
ax = axs[0, 0]
ns = np.arange(1, 13)
hv = np.array([float(h(int(n))) for n in ns])
cv = 1 / ns
ax.axhline(0.5, color=F.MUTED, lw=1.1, ls=(0, (4, 3)))
ax.plot(ns, (1 - cv) / 2, color=F.AQUA, lw=1.2, ls=(0, (1, 2.5)))
ax.plot(ns, 1 - cv, "-o", color=F.AQUA, ms=5, mec=F.SURF, label="anneau = cylindre − cône")
ax.plot(ns, cv, "-o", color=F.ORANGE, ms=5, mec=F.SURF, label="cône")
ax.plot(ns, hv, "-o", color=F.BLEU, ms=6, mec=F.SURF, lw=2.2, label="hémisphère")
F.point(ax, 1, 1, F.INK, 9)
F.point(ax, 3, 2 / 3, F.INK, 9)
ax.text(1.25, 1.235, "n = 1 : les trois solides sont le même segment", fontsize=9, color=F.INK2, va="top")
ax.annotate("n = 3 : hémisphère = cylindre − cône\n(la balance d'Archimède)", xy=(3, 2 / 3), xytext=(2.3, 1.15),
            fontsize=9, color=F.INK, va="top",
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8, relpos=(0.12, 0.0)))
ax.axvspan(5, 6, color=F.BLEU, alpha=0.08, lw=0)
ax.axvspan(7, 8, color=F.AQUA, alpha=0.1, lw=0)
ax.text(5.5, 0.775, "5 → 6\nhémisphère\n< ½ cylindre\n= pic du\nvolume", ha="center", va="top", fontsize=8.5, color=F.INK2, linespacing=1.05)
ax.text(7.5, 0.775, "7 → 8\nhémisphère\n< ½ anneau\n= pic de\nl'aire", ha="center", va="top", fontsize=8.5, color=F.INK2, linespacing=1.05)
ax.text(12.2, 0.505, "½ cylindre", fontsize=8.5, color=F.MUTED, va="bottom", ha="right")
ax.text(12.2, (1 - 1 / 12) / 2 - 0.01, "½ anneau", fontsize=8.5, color=F.AQUA, va="top", ha="right")
ax.set_xticks(ns)
ax.set_xlabel("dimension n")
ax.set_ylabel("volume / volume du cylindre")
ax.set_ylim(-0.02, 1.25)
ax.set_title("a)  Les trois solides, dimension par dimension")
ax.legend(fontsize=9, loc="lower right", bbox_to_anchor=(1.0, 0.12))

# b) la suite : π par l'intérieur et par l'extérieur
ax = axs[0, 1]
K = 10
dims = 2 * np.arange(K) + 1
courbes = [
    ("carré inscrit (côté √2) : 2 + ⅓(2 + ⅖(2 + …))", suite(4, "aire", K), F.BLEU, "-o"),
    ("hexagone inscrit : 3 + 1/8 + 9/640 + …", suite(6, "perimetre", K), F.AQUA, "-o"),
    ("hexagone circonscrit : 2√3 × (1 − …)", suite(6, "exterieur", K), F.ORANGE, "-o"),
    ("carré circonscrit : 4 × (1 − …)", suite(4, "exterieur", K), F.JAUNE, "-o"),
]
ax.plot(dims, [float(v) for v in leib[:K]], "-", color=F.MUTED, lw=1.1, label="Leibniz (carré circonscrit, alternée) : lent")
for nom, vals, coul, st in courbes:
    ax.plot(dims, [float(v) for v in vals], st, color=coul, ms=5, mec=F.SURF, label=nom)
ax.axhline(float(PI), color=F.INK, lw=1.3)
ax.text(19.3, float(PI) + 0.03, "π", fontsize=12, color=F.INK, ha="right", va="bottom")
ax.annotate("3 + 1/8 = 3,125\n(valeur babylonienne)", xy=(3, 3.125), xytext=(5.2, 2.55), fontsize=9, color=F.INK,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xticks(dims)
ax.set_xlabel("dimension de la dernière retenue (2k + 1)")
ax.set_ylabel("somme partielle")
ax.set_ylim(1.9, 4.1)
ax.set_title("b)  La suite des trois solides : π par l'intérieur et par l'extérieur")
ax.legend(fontsize=8.5, loc="upper right")

# c) les partages
ax = axs[1, 0]
styles = {"hemisphere": (F.BLEU, "-o"), "cylindre": (F.AQUA, "-o"), "anneau": (F.JAUNE, "-o"), "cone": (F.ORANGE, "-o"),
          "chevre": (F.INK, "--s")}
for val, txt in ((1.0, "1 = R"), (np.sqrt(5) / 2, "√5/2"), (np.sqrt(2), "√2")):
    ax.axhline(val, color=F.BASE, lw=1.1)
    ax.text(17.4, val, txt, fontsize=9.5, color=F.INK2, va="center")
for s, (coul, st) in styles.items():
    lab = {"chevre": "chèvre (boule entière, piquet au bord)", "anneau": "anneau (cylindre − cône)"}.get(s, NOMS[s])
    ax.plot(NS, [cordes[s][n] for n in NS], st, color=coul, ms=4.5, mec=F.SURF, lw=1.8, label=lab)
    ax.plot([16.4], [rich[s]], "*", color=coul, ms=12, mec=F.SURF, mew=0.8, zorder=7)
ax.text(16.4, 0.965, "extrapolé\ndepuis\n5, 7, 9", fontsize=8.5, color=F.INK2, ha="center", va="top")
F.point(ax, 5.5, 1.0, F.AQUA, 7)
F.point(ax, 7.5, 1.0, F.JAUNE, 7)
ax.text(6.0, 0.70, "la corde dépasse R : cylindre entre 5 et 6 (exactement au pic du volume)\n"
        "anneau entre 7 et 8 (même seuil que le pic de l'aire)", fontsize=9, color=F.INK2, va="bottom")
for x0, x1 in ((5.5, 6.4), (7.5, 8.6)):
    ax.annotate("", xy=(x0, 1.0), xytext=(x1, 0.77), arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xticks(list(NS) + [16.4])
ax.set_xticklabels([str(n) for n in NS] + ["∞"])
ax.set_xlim(1.5, 18.6)
ax.set_ylim(0.66, 1.56)
ax.set_xlabel("dimension n")
ax.set_ylabel("corde de moitié / R")
ax.set_title("c)  Les partages : la corde qui prend la moitié de chaque solide")
ax.legend(fontsize=8.5, loc="upper left", ncol=2)

# d) convergences comparées
ax = axs[1, 1]
traces = [
    ("ullisch", F.INK, "-", 2.4, "division d'Ullisch : 0,453 par point"),
    ("ullisch_seule", F.INK2, "--", 1.4, "une seule de ses intégrales : 0,574"),
    ("carre", F.BLEU, "-", 2.0, "trois solides, carré : ½ par étage"),
    ("hexagone", F.AQUA, "-", 2.0, "trois solides, hexagone : ¼ par étage"),
    ("archimede", "#104281", ":", 2.2, "Archimède : ¼ par doublement"),
    ("wallis", F.JAUNE, "-", 1.8, "Wallis : en 1/n"),
    ("chevre", F.ORANGE, "-", 1.8, "corde de la chèvre → √2 : en 1/n"),
    ("leibniz", F.MUTED, "-", 1.4, "Leibniz : en 1/n"),
]
for cle, coul, st, lw, lab in traces:
    e = erreurs[cle]
    ks = sorted(e)
    ax.semilogy(ks, [float(e[k]) for k in ks], st, color=coul, lw=lw, ms=3.5, mec=F.SURF, label=lab)
ax.set_xlabel("étape (points sur le contour, étages, doublements, dimensions)")
ax.set_ylabel("erreur relative")
ax.set_ylim(1e-21, 3)
ax.set_xlim(0, 33)
ax.set_title("d)  Qui converge comme la division des intégrales ?")
ax.legend(fontsize=8.5, loc="lower left")
ax.text(32.5, 2e-3, "en 1/n : les lentes\n(singularité au bord)", fontsize=9, color=F.INK2, ha="right", va="top")
F.sauver(fig, "d1_trois_solides.png")
