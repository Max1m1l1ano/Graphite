"""
Tous les calculs numériques de l'analyse, avec vérifications.

    python3 scripts/calculs.py

Écrit resultats/resultats.md (tableaux lisibles) et resultats/resultats.json.
Chaque bloc imprime aussi ses contrôles (résidus, nombre de zéros, etc.).
"""

import json
import os
import sys

import math

import mpmath as mp
import sympy as sp
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(__file__))
import chevre as ch  # noqa: E402

mp.mp.dps = 50
ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "..", "resultats")
md = []  # lignes du rapport markdown
res = {}  # valeurs clés (JSON)


def titre(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)
    md.append(f"\n## {t}\n")


def ligne(t=""):
    print(t)
    md.append(t)


def s(x, d=15):
    return mp.nstr(x, d)


# ---------------------------------------------------------------------------
titre("1. Chèvre plane : la formule d'Ullisch (quotient de deux intégrales de contour)")
# ---------------------------------------------------------------------------
f = lambda z: mp.sin(z) - z * mp.cos(z) - mp.pi / 2
beta = mp.findroot(f, 1.9)
r2 = 2 * mp.cos(beta / 2)
c, rho = 3 * mp.pi / 4, mp.pi / 4
nz = ch.nombre_de_zeros(f, c, rho)
ligne(f"Équation : sin β − β cos β = π/2 ; corde r = 2 cos(β/2)")
ligne(f"- β (racine, findroot 50 chiffres) = {s(beta, 40)}")
ligne(f"- β en degrés = {s(mp.degrees(beta), 20)}")
ligne(f"- r/R = {s(r2, 40)}")
ligne(f"- corde des intersections à x0 = 1 − r²/2 = {s(1 - r2**2 / 2, 15)} R du centre")
ligne(f"- zéros de f dans |z − 3π/4| = π/4 (principe de l'argument) : {s(nz, 6)}")
nz_err = ch.nombre_de_zeros(f, 3 * mp.pi / 8, mp.pi / 4)
q_err = ch.racine_par_quotient(f, 3 * mp.pi / 8, mp.pi / 4, 256).real
ligne(f"- contour imprimé par erreur en 2020, |z − 3π/8| = π/4 : {s(nz_err, 6)} zéro, quotient = {s(q_err, 25)} (même β)")
ligne("")
ligne("| nœuds N (trapèzes) | β approché par le quotient | erreur |")
ligne("|---:|:---|---:|")
conv = []
for N in [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]:
    q = ch.racine_par_quotient(f, c, rho, N)
    err = abs(q - beta)
    conv.append((N, float(err)))
    ligne(f"| {N} | {s(q.real, 30)} | {s(err, 3)} |")
res["chevre2d"] = {"beta": float(beta), "r": float(r2), "x0": float(1 - r2**2 / 2), "convergence": conv}

# ---------------------------------------------------------------------------
titre("2. Chèvre en dimension n : W_n(2α) − (2cos α)^n W_n(α) = W_n(π)/2, r = 2cos α")
# ---------------------------------------------------------------------------
mp.mp.dps = 30
ligne("Contrôle : la même « division d'intégrales complexes » marche en toute dimension")
ligne("(contour |α − 7π/24| = π/16, qui entoure l'intervalle [π/4, π/3]) :")
ligne("")
ligne("| n | zéros dans le contour | r_n par le quotient (N = 256) | r_n par recherche directe | écart |")
ligne("|---:|---:|:---|:---|---:|")
for n in [2, 3, 4, 5, 6, 8]:
    F = ch.equation_chevre(n)
    cc, rr = 7 * mp.pi / 24, mp.pi / 16
    nzn = ch.nombre_de_zeros(F, cc, rr)
    a_q = ch.racine_par_quotient(F, cc, rr, 256).real
    r_dir = ch.corde_moitie_mp(n)
    ligne(f"| {n} | {s(nzn, 4)} | {s(2 * mp.cos(a_q), 20)} | {s(r_dir, 20)} | {s(abs(2 * mp.cos(a_q) - r_dir), 2)} |")

ligne("")
ligne("| n | r_n / R | angle α_n (°) | √(2n/(n+1)) | écart | x0 = 1 − r²/2 | 1/(n+1) | fraction broutée avec corde √2 |")
ligne("|---:|:---|---:|:---|---:|:---|:---|:---|")
table_n = []
for n in list(range(1, 21)) + [30, 50, 100, 1000, 10000]:
    r = ch.corde_moitie_mp(n)
    a = mp.acos(r / 2)
    approx = mp.sqrt(2 * mp.mpf(n) / (n + 1))
    x0 = 1 - r**2 / 2
    frac2 = ch.fraction_broutee_mp(n, mp.sqrt(2)) if n > 1 else mp.sqrt(2) / 2
    table_n.append({"n": n, "r": float(r), "alpha_deg": float(mp.degrees(a)), "approx": float(approx),
                    "x0": float(x0), "frac_sqrt2": float(frac2)})
    ligne(f"| {n} | {s(r, 12)} | {s(mp.degrees(a), 7)} | {s(approx, 10)} | {s(r - approx, 3)} | {s(x0, 6)} | {s(mp.mpf(1) / (n + 1), 6)} | {s(frac2, 6)} |")
res["dimensions"] = table_n

ligne("")
ligne("Développement asymptotique (vérifié numériquement) :")
for n in [100, 1000, 10000]:
    r = ch.corde_moitie_mp(n)
    ligne(f"- n = {n} : (r² − 2n/(n+1))·n² = {s((r**2 - 2 * mp.mpf(n) / (n + 1)) * n**2, 8)}  (→ 2/3) ; "
          f"(√2 − r)·n = {s((mp.sqrt(2) - r) * n, 8)}  (→ 1/√2 = 0.70711)")

# ---------------------------------------------------------------------------
titre("3. Dimensions impaires : polynômes, radicaux et groupes de Galois")
# ---------------------------------------------------------------------------
x, rr_ = sp.symbols("x r")
polys = {}
for n in [1, 3, 5, 7, 9]:
    Wn = lambda C: sp.integrate((1 - x**2) ** sp.Rational(n - 1, 2), (x, C, 1))  # W_n(t), C = cos t
    Wpi = sp.integrate((1 - x**2) ** sp.Rational(n - 1, 2), (x, -1, 1))
    cc = rr_ / 2  # cos α = r/2, cos 2α = r²/2 − 1
    expr = sp.expand(Wn(rr_**2 / 2 - 1) - rr_**n * Wn(cc) - Wpi / 2)
    num = sp.Poly(sp.numer(sp.together(expr)), rr_)
    prim = sp.Poly(num.primitive()[1], rr_)
    if prim.LC() < 0:
        prim = -prim
    polys[n] = prim
    racine = [z for z in prim.nroots(n=25) if z.is_real and 0.9 < z < 1.5]
    ligne(f"- n = {n} : {sp.sstr(prim.as_expr())} = 0  (degré {prim.degree()}, racine utile {racine[0] if racine else '—'})")


def preuve_galois_Sd(P, pmax=2000):
    """Types de cycles de Frobenius (P mod p) : un d-cycle + un (d−1)-cycle + un type
    'transposition' (un seul 2-cycle, le reste impair) prouvent que Gal = S_d."""
    d = P.degree()
    D = sp.discriminant(P)
    trouve = {"d": None, "d-1": None, "transposition": None}
    for p in sp.primerange(3, pmax):
        if D % p == 0 or P.LC() % p == 0:
            continue
        facteurs = sp.Poly(P.as_expr(), rr_, modulus=p).factor_list()[1]
        t = sorted(sp.Poly(g, rr_, modulus=p).degree() for g, m in facteurs for _ in range(m))
        if t == [d] and trouve["d"] is None:
            trouve["d"] = p
        if t == [1, d - 1] and trouve["d-1"] is None:
            trouve["d-1"] = p
        if t.count(2) == 1 and all(v % 2 == 1 for v in t if v != 2) and trouve["transposition"] is None:
            trouve["transposition"] = p
        if all(trouve.values()):
            break
    return trouve


ligne("")
ligne("Groupes de Galois (critère de Jordan via les réductions modulo p) :")
for n in [3, 5, 7, 9]:
    P = polys[n]
    t = preuve_galois_Sd(P)
    ok = all(t.values())
    ligne(f"- n = {n} : degré {P.degree()}, d-cycle mod {t['d']}, (d−1)-cycle mod {t['d-1']}, "
          f"transposition mod {t['transposition']} ⇒ Gal = S_{P.degree()} : {'prouvé' if ok else 'non établi'}"
          f" ⇒ résoluble par radicaux : {'oui' if P.degree() <= 4 else 'non'}")

mp.mp.dps = 40
u = mp.cbrt(1 + mp.sqrt(2))
w = (u + 1 / u) / mp.sqrt(2)
r3 = 2 / (mp.sqrt(w) + mp.sqrt(2 / mp.sqrt(w) - w))
ligne("")
ligne("Forme close en 3D (Ferrari) : avec u = ∛(1+√2) et w = (u + 1/u)/√2,")
ligne(f"r₃ = 2 / (√w + √(2/√w − w)) = {s(r3, 35)}")
ligne(f"contrôle 3r⁴ − 8r³ + 8 = {s(3 * r3**4 - 8 * r3**3 + 8, 3)}")
res["r3_radicaux"] = float(r3)

ligne("")
ligne("Dimensions paires : W_n(θ) = c_n·θ + P_n(θ) (P_n trigonométrique), l'équation devient")
ligne("c_n(2 − rⁿ)·α + T = c_n·π/2 avec T = P_n(2α) − rⁿP_n(α). Si r était algébrique, T, cos α, sin α et e^{iα}")
ligne("le seraient aussi : relation linéaire T + (algébrique)·log e^{iα} + (algébrique)·log(−1) = 0 avec T ≠ 0,")
ligne("interdite par le théorème de Baker (1966). Il suffit donc de vérifier T ≠ 0 :")
for n in [2, 4, 6, 8, 10, 20]:
    r = ch.corde_moitie_mp(n)
    a = mp.acos(r / 2)
    cn = mp.mpf(1)
    for j in range(2, n + 1, 2):
        cn *= mp.mpf(j - 1) / j
    T = (ch.W(n, 2 * a) - cn * 2 * a) - r**n * (ch.W(n, a) - cn * a)
    ligne(f"- n = {n} : c_n = {s(cn, 8)}, T(α_n) = {s(T, 10)} ≠ 0 ⇒ r_{n} transcendant")

# ---------------------------------------------------------------------------
titre("4. Tous les paramètres : piquet à la distance δ, courbe des 50 %")
# ---------------------------------------------------------------------------
mp.mp.dps = 25
ligne("k_n(δ) = corde qui donne la moitié du champ ; comparaison avec k² ≈ δ² + (n−1)/(n+1) et la limite √(1+δ²)")
ligne("")
ligne("| n | δ | k_n(δ) exact | √(δ²+(n−1)/(n+1)) | limite n→∞ √(1+δ²) | régime |")
ligne("|---:|---:|:---|:---|:---|:---|")
courbes = {}
for n in [1, 2, 3, 10, 100]:
    pts = []
    for d in [0, 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 5]:
        k = ch.corde_moitie_mp(n, d)
        approx = mp.sqrt(d**2 + mp.mpf(n - 1) / (n + 1))
        regime = "corde dans le champ" if d + k <= 1 + mp.mpf(10) ** -20 else ("piquet au bord" if d == 1 else ("piquet dedans" if d < 1 else "piquet dehors"))
        pts.append((d, float(k)))
        if d in (0, 0.25, 1, 2, 5):
            ligne(f"| {n} | {d} | {s(k, 10)} | {s(approx, 10)} | {s(mp.sqrt(1 + d**2), 10)} | {regime} |")
    courbes[n] = pts
res["courbes50"] = courbes
ligne("")
ligne(f"- Piquet au centre : k = 2^(−1/n) (n = 2 : 1/√2 = {s(1 / mp.sqrt(2), 8)}, c'est le « diaphragme d'un stop »).")
ligne("- La corde reste inscrite dans le champ tant que δ ≤ 1 − 2^(−1/n) (n = 2 : δ ≤ 0,2929) : tangence intérieure à la fin.")
ligne("- Piquet très loin : k ≈ δ + (n−1)/(2(n+1)δ) (n = 2 : δ + 1/(6δ)).")

# ---------------------------------------------------------------------------
titre("5. Volume et surface de la boule unité selon la dimension")
# ---------------------------------------------------------------------------
ligne("| n | V_n | S_{n−1} = n·V_n | part du volume à moins de 0,1 R de l'« équateur » | part du volume dans la coquille extérieure de 0,1 R |")
ligne("|---:|---:|---:|---:|---:|")
vs = []
for n in range(1, 21):
    V, S = ch.volume_boule(n), ch.surface_sphere(n)
    tranche = 1 - 2 * float(ch.fraction_calotte(n, mp.acos(0.1)))
    vs.append({"n": n, "V": V, "S": S, "tranche": tranche, "coquille": 1 - 0.9**n})
    ligne(f"| {n} | {V:.6f} | {S:.6f} | {tranche:.1%} | {1 - 0.9**n:.1%} |")
res["volume_surface"] = vs
nV = max(vs, key=lambda e: e["V"])["n"]
nS = max(vs, key=lambda e: e["S"])["n"]
ligne("")
ligne(f"- Volume maximal en n = {nV} (V₅ = 8π²/15 = {float(8 * mp.pi**2 / 15):.6f}) ; surface maximale en n = {nS} (S₆ = 16π³/15 = {float(16 * mp.pi**3 / 15):.6f}).")
ligne("- Coquille extérieure d'épaisseur 1 % : fraction du volume = 1 − 0,99ⁿ → "
      + ", ".join(f"n={n}: {1 - 0.99**n:.1%}" for n in [2, 3, 10, 100, 1000]))

# ---------------------------------------------------------------------------
titre("6. Optique : la même machine (quotient d'intégrales de contour)")
# ---------------------------------------------------------------------------
mp.mp.dps = 30
# FTM50 : ψ − sin ψ = π/2 (équation de Kepler avec e = 1), s = cos(ψ/2)
g = lambda z: z - mp.sin(z) - mp.pi / 2
psi = ch.racine_par_quotient(g, mp.mpf("2.3"), mp.mpf("0.5")).real
s50 = mp.cos(psi / 2)
ligne(f"- FTM50 d'une pupille circulaire parfaite : ψ − sin ψ = π/2 → ψ = {s(psi, 15)} ; ν50 = cos(ψ/2)·ν_c = {s(s50, 10)} ν_c "
      f"(zéros dans le contour : {s(ch.nombre_de_zeros(g, mp.mpf('2.3'), mp.mpf('0.5')), 3)})")
for N_ in [4, 8, 11, 16]:
    nuc = 1 / (550e-6 * N_)
    ligne(f"    f/{N_}, λ = 550 nm : coupure {nuc:.0f} cycles/mm, FTM50 = {float(s50) * nuc:.0f} cycles/mm")
ligne(f"- FTM au décalage d'un rayon (vesica piscis) : {s((2 * mp.pi / 3 - mp.sqrt(3) / 2) / mp.pi, 8)}")
# Airy : énergie encerclée 50 %
h = lambda z: mp.besselj(0, z) ** 2 + mp.besselj(1, z) ** 2 - mp.mpf(1) / 2
x50 = ch.racine_par_quotient(h, mp.mpf("1.6"), mp.mpf("0.5")).real
ligne(f"- Tache d'Airy, 50 % de l'énergie : J0² + J1² = 1/2 → x = {s(x50, 12)} → rayon = {s(x50 / mp.pi, 6)} λN "
      f"(1er anneau noir : {s(mp.besseljzero(1, 1) / mp.pi, 6)} λN, qui contient {s(1 - mp.besselj(0, mp.besseljzero(1, 1)) ** 2, 4)} de l'énergie)")
# Fente : maxima secondaires tan x = x, i.e. sin x − x cos x = 0 (la « fonction de la chèvre » au niveau 0)
gf = lambda z: mp.sin(z) - z * mp.cos(z)
xm = ch.racine_par_quotient(gf, mp.mpf("4.5"), mp.mpf("0.6")).real
ligne(f"- Diffraction par une fente : 1er maximum secondaire où sin x − x cos x = 0 → x = {s(xm, 12)} (≈ 1,4303 π)")
# Kepler
for e, nom in [(mp.mpf("0.0167"), "Terre/Soleil"), (mp.mpf("0.0549"), "Lune")]:
    M = mp.mpf(1)
    kf = lambda z: z - e * mp.sin(z) - M
    E = ch.racine_par_quotient(kf, M, mp.mpf("0.6")).real
    ligne(f"- Kepler ({nom}, e = {e}, M = 1 rad) : E = {s(E, 15)}, résidu {s(kf(E), 2)}")
res["optique"] = {"s50": float(s50), "x50_airy_lambdaN": float(x50 / mp.pi), "max_fente": float(xm)}

# Éclipses
ligne("")
ligne("Éclipses (disques Soleil R = 1, Lune k, distance des centres d) :")
for kk in [0.90, 0.95, 1.00, 1.05, 1.08]:
    ob = ch.aire_lentille(1.0, kk, 1.0) / mp.pi
    ligne(f"- k = {kk:.2f}, centre lunaire sur le bord du Soleil : obscuration {float(ob):.1%}, magnitude {kk / 2:.3f}")
for kk in [0.92, 1.00, 1.05]:
    d50 = brentq(lambda d: float(ch.aire_lentille(1.0, kk, d)) / math.pi - 0.5, abs(1 - kk) + 1e-9, 1 + kk - 1e-9)
    ligne(f"- k = {kk:.2f} : 50 % d'obscuration quand d = {float(d50):.4f} R, soit une magnitude {float((1 + kk - d50) / 2):.3f}")
Rs, Rm, D = mp.mpf(695700), mp.mpf("1737.4"), mp.mpf("149597870.7")
Lu, Lp = D * Rm / (Rs - Rm), D * Rm / (Rs + Rm)
fr = lambda v, fmt=",.0f": format(v, fmt).replace(",", " ")
ligne(f"- Longueur du cône d'ombre (tangentes extérieures communes) : {fr(float(Lu))} km ; "
      f"sommet du cône de pénombre (tangentes intérieures) à {fr(float(Lp))} km de la Lune, côté Soleil")
for dm in [356400, 384400, 406700]:
    ligne(f"    Lune à {fr(dm)} km du centre de la Terre : la pointe de l'ombre est à {fr(float(Lu) - dm, '+,.0f')} km du centre de la Terre (rayon 6 371 km)")

# Anneaux de Newton
ligne("")
lam = 589.3e-9
ligne("Anneaux de Newton (λ = 589,3 nm, lentille R1 = 1 m) : ρ_m = √(m λ R_eff), 1/R_eff = 1/R1 ∓ 1/R2")
for R2, nom in [(None, "sur un plan"), (1.5, "dans un concave R2 = 1,5 m (contact intérieur)"),
                (-1.5, "sur un convexe R2 = 1,5 m (contact extérieur)"), (1.01, "dans un calibre concave R2 = 1,01 m")]:
    Reff = 1.0 if R2 is None else (1 / (1 - 1 / R2) if R2 > 0 else 1 / (1 + 1 / -R2))
    r1 = (lam * Reff) ** 0.5
    ligne(f"- {nom} : R_eff = {Reff:.4g} m, ρ1 = {r1 * 1e3:.3f} mm, ρ2 = {r1 * 2**0.5 * 1e3:.3f} mm (= √2·ρ1), aire par anneau {3.14159265 * lam * Reff * 1e6:.3f} mm²")
N_fr = (0.05**2 / (4 * 546.07e-9)) * (1e-5 / (0.1 * 0.10001))
ligne(f"- Calibre : pièce Ø 50 mm, R = 100 mm, erreur de rayon 10 µm → {N_fr:.2f} frange(s)")

# Lentilles
ligne("")
ligne("Lentilles :")
r3f = float(r3)
ligne(f"- Chèvre 3D = lentille biconvexe (épaisseur {r3f:.4f} R, diamètre {2 * r3f * (1 - r3f**2 / 4) ** 0.5:.4f} R) "
      f"de même volume que le ménisque restant ; plan des intersections à {1 - r3f**2 / 2:.4f} R du centre")
for n_ in [1.333, 1.5, 2.0]:
    ligne(f"- Boule {'d’eau' if n_ < 1.4 else 'de verre'} d'indice {n_} : focale effective {n_ / (2 * (n_ - 1)):.3f} R (comptée du centre), foyer à {n_ / (2 * (n_ - 1)) - 1:.3f} R de la surface")
c4 = math.cos(math.radians(67.5)) ** 4
ligne(f"- Loi en cos⁴ au bord d'un champ de 135° (67,5°) : {c4:.4f}, soit {-math.log2(c4):.2f} diaphragmes perdus")

# ---------------------------------------------------------------------------
os.makedirs(SORTIE, exist_ok=True)
with open(os.path.join(SORTIE, "resultats.md"), "w") as fh:
    fh.write("# Résultats numériques (générés par scripts/calculs.py)\n")
    fh.write("\n".join(md) + "\n")
with open(os.path.join(SORTIE, "resultats.json"), "w") as fh:
    json.dump(res, fh, indent=1, ensure_ascii=False)
print("\nÉcrit :", os.path.join(SORTIE, "resultats.md"))
