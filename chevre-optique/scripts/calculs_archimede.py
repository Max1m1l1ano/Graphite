"""
Calculs de la partie II (Archimède, cube qui tourne, ménisque, chèvres dans les solides).

    python3 scripts/calculs_archimede.py      # ≈ 1 min (les polyèdres géodésiques sont les plus longs)

Écrit resultats/archimede.md et resultats/archimede.json.
"""

import json
import os
import sys
from math import acos, cos, factorial, pi, sqrt

import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(__file__))
import archimede as ar  # noqa: E402
import chevre as ch  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "..", "resultats")
md, res = [], {}


def titre(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)
    md.append(f"\n## {t}\n")


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, d=6):
    return f"{x:.{d}f}".replace(".", ",")


PHI = (1 + sqrt(5)) / 2

# ---------------------------------------------------------------------------
titre("1. Archimède : tranches, croisements, demi-volumes")
# ---------------------------------------------------------------------------
ligne("Rayon R = 1. Hémisphère z ∈ [0, 1] ; cylindre de hauteur 1 ; cône pointe en bas (rayon de tranche = z) ;")
ligne("paraboloïde-bol z = ρ² (rayon de tranche √z).")
ligne("")
ligne("| hauteur z | hémisphère π(1−z²) | cône πz² | cylindre − cône π(1−z²) | bol π z |")
ligne("|---:|---:|---:|---:|---:|")
for z in [0, 0.25, 0.5, 1 / sqrt(2), 1 / PHI, 0.75, 1]:
    ligne(f"| {fr(z, 4)} | {fr(pi * (1 - z * z), 4)} | {fr(pi * z * z, 4)} | {fr(pi * (1 - z * z), 4)} | {fr(pi * z, 4)} |")
ligne("")
ligne(f"- Sphère ∩ cône : z = 1/√2 = {fr(1 / sqrt(2))} ; les deux tranches valent π/2, la moitié de la tranche du cylindre.")
ligne(f"- Sphère ∩ paraboloïde : z² + z − 1 = 0, z = 1/φ = {fr(1 / PHI)} (nombre d'or), rayon de tranche 1/√φ = {fr(1 / sqrt(PHI))}.")
ligne("- Cône ∩ paraboloïde : z = 0 et z = 1 seulement.")
ligne("- Volumes : hémisphère 2π/3, cône π/3, cylindre π, bol π/2 (le paraboloïde est la moitié du cylindre).")
# plans qui coupent chaque solide en deux volumes égaux
z_hemi = brentq(lambda z: z - z ** 3 / 3 - 1 / 3, 0, 1)
ligne("")
ligne("Plan horizontal qui coupe chaque solide en deux volumes égaux (volume compté depuis z = 0) :")
ligne(f"- hémisphère (et cylindre − cône, par Archimède) : z³ − 3z + 1 = 0 → z = 2 cos 80° = {fr(z_hemi)} "
      f"(contrôle {fr(2 * cos(np.radians(80)))}) — cas irréductible : 3 racines réelles, radicaux complexes obligatoires")
ligne(f"- cône pointe en bas : z = 2^(−1/3) = {fr(2 ** (-1 / 3))} ; bol paraboloïde : z = 1/√2 = {fr(1 / sqrt(2))} ; cylindre : 1/2")
res["archimede"] = {"z_sphere_cone": 1 / sqrt(2), "z_sphere_parab": 1 / PHI, "z_demi_hemisphere": z_hemi}

# ---------------------------------------------------------------------------
titre("2. Le cube et ses trois sphères ; le cube en dimension n")
# ---------------------------------------------------------------------------
ligne("Cube d'arête 2 : sphère inscrite R = 1 (6 contacts : centres des faces), sphère médiane √2 (12 contacts : milieux")
ligne("des arêtes), sphère circonscrite √3 (8 contacts : sommets).")
ligne(f"- Volumes rapportés au cube : π/6 = {fr(pi / 6, 4)} ; π√2/3 = {fr(pi * sqrt(2) / 3, 4)} ; π√3/2 = {fr(pi * sqrt(3) / 2, 4)}")
ligne("")
ligne("| n | boule inscrite / cube = V_n/2^n | demi-diagonale √n | centres de facettes à distance √2 d'un centre donné |")
ligne("|---:|---:|---:|---:|")
for n in [1, 2, 3, 4, 5, 6, 8, 10, 20]:
    frac = ch.volume_boule(n) / 2 ** n
    ligne(f"| {n} | {fr(frac, 5)} | {fr(sqrt(n), 4)} | {2 * n - 2} sur {2 * n - 1} ({(2 * n - 2) / (2 * n - 1):.0%}) |".replace("%", " %"))
ligne("")
ligne("n³ − n = (n−1)n(n+1) et n² − n = (n−1)n : des factorielles seulement si (n−2)! = 1, donc n = 2 ou 3.")
for n in [2, 3, 4, 5]:
    ligne(f"- n = {n} : n² − n = {n * n - n}, n³ − n = {n ** 3 - n}"
          + (f" = {n + 1}!" if n ** 3 - n == factorial(n + 1) else "")
          + (f" ; n² − n = {n}!" if n * n - n == factorial(n) else ""))
ligne("- Le cube a 2n = 6 faces en dimension 3, et 2n = n! seulement pour n = 3. Son groupe de symétries a 2ⁿ·n! = 48 éléments.")

# ---------------------------------------------------------------------------
titre("3. Le cube qui tourne autour de sa grande diagonale (arête 1)")
# ---------------------------------------------------------------------------
L = sqrt(3)
V_num = quad(lambda s: pi * ar.rayon2_balayé(s), 0, L, points=[1 / L, 2 / L], limit=200)[0]
V_form = quad(lambda s: pi * ar.profil_balayé(s), 0, L, points=[1 / L, 2 / L], limit=200)[0]
ecart_profil = max(abs(ar.rayon2_balayé(s) - ar.profil_balayé(s)) for s in np.linspace(0, L, 2001))
V_cyl = pi * (2 / 3) * L
V_bicone = 2 * pi * (3 / 2) * (L / 2) / 3
V_circ = 4 / 3 * pi * (L / 2) ** 3
h = 1 / (2 * L)
V_men_cyl = pi * quad(lambda u: 2 / 3 - (0.5 + 2 * u * u), -h, h)[0]
V_men_sph = pi * quad(lambda u: 3 * u * u, -h, h)[0]
R_mid = sqrt(2) / 2
s_t = (L / 2) / 3
dedans = all(R_mid ** 2 - (s - L / 2) ** 2 <= ar.rayon2_balayé(s) + 1e-12 for s in np.linspace(L / 2 - R_mid, L / 2 + R_mid, 1201))
ligne(f"- Profil : cônes r² = 2s² (demi-angle arctan √2 = {fr(np.degrees(np.arctan(sqrt(2))), 4)}°, l'« angle magique »,"
      f" cos = 1/√3), hyperboloïde r² = 1/2 + 2(s − √3/2)² au milieu ; écart formule / calcul direct = {ecart_profil:.1e}")
ligne(f"- Volume balayé : {fr(V_num, 10)} (calcul direct) = {fr(V_form, 10)} (formule) = π/√3 = {fr(pi / sqrt(3), 10)}")
ligne(f"- Cylindre circonscrit (rayon √(2/3), longueur √3) : {fr(V_cyl, 6)} → rapport {fr(V_num / V_cyl, 10)} : la moitié, comme le paraboloïde")
ligne(f"- Losange (bicône des cônes prolongés) : volume {fr(V_bicone, 8)} = sphère circonscrite au cube {fr(V_circ, 8)} ;"
      f" solide balayé = {fr(V_num / V_bicone, 8)} du bicône (2/3)")
ligne(f"- Losange : angles {fr(2 * np.degrees(np.arctan(sqrt(2))), 4)}° et {fr(180 - 2 * np.degrees(np.arctan(sqrt(2))), 4)}°,"
      f" diagonales √3 et √6 (rapport √2), côté 3/2 : la face du dodécaèdre rhombique")
ligne(f"- Asymptotes de l'hyperboloïde : r = ±√2 (s − √3/2), parallèles aux cônes des bouts")
ligne(f"- Ménisque central (entre le cylindre des sommets et l'hyperboloïde, tiers du milieu) : {fr(V_men_cyl, 8)}"
      f" = π/(9√3) = {fr(pi / (9 * L), 8)}, soit {fr(V_men_cyl / V_num, 6)} du solide (1/9)")
ligne(f"  épaisseur max √(2/3) − √(1/2) = {fr(sqrt(2 / 3) - sqrt(0.5), 6)}, longueur 1/√3 = {fr(1 / L, 6)}")
ligne(f"- Sphère médiane (rayon √2/2, centre au milieu) : tangente aux cônes en s = √3/6 = {fr(s_t, 6)} et s = 5√3/6,"
      f" cercles de rayon 1/√6 = {fr(sqrt(2) * s_t, 6)}, et au col (rayon √2/2) ; à l'intérieur du solide : {dedans}")
ligne(f"  → 3 cercles de contact, 6 points dans la coupe ; volume de la sphère / solide = {fr(4 / 3 * pi * R_mid ** 3 / V_num, 6)} = √(2/3)")
ligne(f"- Vide entre l'hyperboloïde et la sphère médiane (tiers du milieu) : {fr(V_men_sph, 8)} = π/(12√3)")
ligne("- Ombre du cube vue le long de la diagonale : hexagone régulier de côté √(2/3) = 3 losanges de 60°/120°")
res["cube_tournant"] = {"volume": V_num, "rapport_cylindre": V_num / V_cyl, "bicone": V_bicone,
                        "menisque": V_men_cyl, "vide_sphere": V_men_sph}

# ---------------------------------------------------------------------------
titre("4. Le ménisque réel dans un tube")
# ---------------------------------------------------------------------------
ligne("Ménisque en calotte sphérique (valable si le rayon a du tube est petit devant la longueur capillaire).")
ligne("Volume oublié en lisant au point extrême = π a³ (1 − S)(1 + 2S) / (3C(1 + S)), S = sin θ, C = |cos θ|.")
ligne("")
ligne("| angle de contact θ | flèche / a | volume oublié / (π a³) | hauteur équivalente / a |")
ligne("|---:|---:|---:|---:|")
for th in [0, 10, 20, 30, 40, 60, 80, 100, 120, 140, 160, 180]:
    if th == 90:
        continue
    v = float(ar.anneau_menisque(th))
    ligne(f"| {th}° | {fr(float(ar.profondeur_menisque(th)), 4)} | {fr(v, 4)} | {fr(v, 4)} |")
ligne("")
ligne("θ = 0 (eau sur verre propre) : ménisque hémisphérique, l'anneau oublié est cylindre − hémisphère = le cône : π a³/3.")
for liq in ["eau", "mercure"]:
    lc = ar.longueur_capillaire(liq)
    ligne(f"- {liq} : longueur capillaire {fr(lc * 1000, 2)} mm ; Jurin : "
          + " ; ".join(f"a = {a} mm → {fr(ar.jurin(liq, a / 1000) * 1000, 1)} mm" for a in [0.25, 0.5, 1.0]))
ligne("  (signe − : dépression ; Jurin et la calotte ne valent que pour a petit devant la longueur capillaire)")
ligne("")
ligne("Liquide en rotation (seau de Newton) : surface z = ω²ρ²/(2g), le centre descend et le bord monte de ω²a²/(4g) ;")
ligne("miroir liquide : focale f = g/(2ω²).")
for f_ in [1.0, 4.0, 9.0]:
    w = sqrt(ar.G / (2 * f_))
    ligne(f"- f = {fr(f_, 0)} m → ω = {fr(w, 3)} rad/s, une rotation en {fr(2 * pi / w, 1)} s")
res["menisque"] = {"theta0": float(ar.anneau_menisque(0)), "theta140": float(ar.anneau_menisque(140))}

# ---------------------------------------------------------------------------
titre("5. Découper l'aire de la chèvre : bandes (Riemann), niveaux (coaire), contour")
# ---------------------------------------------------------------------------
r2 = 1.1587284730181215
ligne("Erreur sur la corde r quand l'aire est calculée avec N subdivisions :")
ligne("")
ligne("| N | bandes verticales | niveaux de distance (milieu) | niveaux (Gauss) | contour d'Ullisch |")
ligne("|---:|---:|---:|---:|---:|")
mp.mp.dps = 30
fz = lambda z: mp.sin(z) - z * mp.cos(z) - mp.pi / 2
decoupe = {}
for N in [4, 8, 16, 32, 64, 128, 256, 512, 1024]:
    e1 = abs(brentq(lambda r: ar.aire_riemann(r, N) - pi / 2, 0.8, 1.6, xtol=1e-15) - r2)
    e2 = abs(brentq(lambda r: ar.aire_niveaux(r, N) - pi / 2, 0.8, 1.6, xtol=1e-15) - r2)
    e3 = abs(brentq(lambda r: ar.aire_niveaux(r, N, True) - pi / 2, 0.8, 1.6, xtol=1e-15) - r2) if N <= 64 else 0.0
    q = ch.racine_par_quotient(fz, 3 * mp.pi / 4, mp.pi / 4, N).real
    e4 = float(abs(2 * mp.cos(q / 2) - mp.mpf("1.1587284730181215178282335")))
    decoupe[N] = (e1, e2, e3, e4)
    f = lambda e: f"{e:.1e}" if e > 1e-16 else "< 1e-16"
    ligne(f"| {N} | {f(e1)} | {f(e2)} | {f(e3) if N <= 64 else '—'} | {f(e4)} |")
res["decoupes"] = decoupe

# ---------------------------------------------------------------------------
titre("6. Dimensions 5 et 7, et la place de la 3D")
# ---------------------------------------------------------------------------
ligne("| rayon R | dimension du volume max | dimension de l'aire max | 2πR² − 1 |")
ligne("|---:|---:|---:|---:|")
for R in [0.5, 1, 1.5, 2, 3]:
    ligne(f"| {fr(R, 1)} | {ar.dimension_du_maximum(R)} | {ar.dimension_du_maximum(R, 'surface')} | {fr(2 * pi * R * R - 1, 1)} |")
ligne("")
ligne("Projection de l'aire de la sphère sur un axe : densité ∝ (1 − z²)^((n−3)/2) ; uniforme seulement pour n = 3.")
for n in [2, 3, 4, 10]:
    ligne(f"- n = {n} : densité en z = 0 : {fr(float(ar.densite_projection(n, 0.0)), 4)} ; en z = 0,9 : {fr(float(ar.densite_projection(n, 0.9)), 4)}")
ligne("")
ligne(f"- π − 3 = {fr(pi - 3, 8)} ; √2/10 = {fr(sqrt(2) / 10, 8)} ; écart {fr(pi - 3 - sqrt(2) / 10, 8)}")
ligne(f"- Encadrement d'Archimède (96-gones) : 10/71 = {fr(10 / 71, 6)} < π − 3 < 1/7 = {fr(1 / 7, 6)}")

# ---------------------------------------------------------------------------
titre("7. Entre la 2D et la 3D : des chèvres dans les solides d'Archimède")
# ---------------------------------------------------------------------------
ligne("Piquet T = (1, 0, 0) : contact de la sphère, du cylindre et du cube. Corde qui broute la moitié :")
ligne("")
ligne("| forme | dimension | volume | corde de la moitié |")
ligne("|---|---:|---:|---:|")
cordes = {}
cordes["disque"] = r2
cordes["carre"] = ar.corde_moitie_polygone(ar.CARRE, (1, 0))
for s_ in ["boule", "anneau", "cylindre", "cube"]:
    cordes[s_] = ar.corde_moitie_solide(s_)
noms = {"boule": "boule", "anneau": "cylindre − double cône", "cylindre": "cylindre (hauteur 2)", "cube": "cube"}
ligne(f"| disque | 2 | π | {fr(cordes['disque'])} |")
ligne(f"| carré (piquet au milieu d'un côté) | 2 | 4 | {fr(cordes['carre'])} |")
for s_ in ["boule", "anneau", "cylindre", "cube"]:
    ligne(f"| {noms[s_]} | 3 | {fr(ar.VOLUMES[s_], 4)} | {fr(cordes[s_])} |")
res["cordes_T"] = cordes
ligne("")
ligne("Quart, moitié, trois quarts (piquet sur le bord) :")
for f_ in [0.25, 0.5, 0.75]:
    b = mp.findroot(lambda x: mp.sin(x) - x * mp.cos(x) - mp.pi * (1 - f_), 1.9)
    r_2d = float(2 * mp.cos(b / 2))
    r_3d = brentq(lambda r: r ** 3 * (8 - 3 * r) / 16 - f_, 0.1, 2.0)
    ligne(f"- {int(f_ * 100)} % : plan r = {fr(r_2d)} (sin β − β cos β = {fr(1 - f_, 2)}π) ; boule r = {fr(r_3d)} (3r⁴ − 8r³ + {fr(16 * f_, 0)} = 0)")

# ---------------------------------------------------------------------------
titre("8. Glisser le disque de la moitié : constructions et événements")
# ---------------------------------------------------------------------------
ligne("Champ : disque unité ; piquet P = (δ, 0) ; corde k(δ) des 50 %.")
ligne("")
ligne("| δ | k | corde commune x₀ | demi-corde y₀ | angle QPQ' | secteur PQQ' | rectangle des tangentes y = ±k |")
ligne("|---:|---:|---:|---:|---:|---:|---|")
d_star = 1 - 1 / sqrt(2)
d_eq = brentq(lambda d: ch.corde_moitie(2, d) - 1.0, 0.5, 1.0)
d_p = brentq(lambda d: ch.corde_moitie(2, d) ** 2 + d * d - 1, 0.4, 0.8, xtol=1e-14)  # corde commune par P
for d in [0.0, 0.15, d_star, 0.5, d_p, 0.7, d_eq, 1.0, 1.5, 2.0, 3.0]:
    k = ch.corde_moitie(2, d)
    if d > abs(1 - k) + 1e-9:
        x0 = (1 + d * d - k * k) / (2 * d)
        y0 = sqrt(max(0.0, 1 - x0 * x0))
        alpha = acos(max(-1, min(1, (d - x0) / k)))
        sect = k * k * alpha
        cr = f"{fr(x0, 4)} | {fr(y0, 4)} | {fr(2 * np.degrees(alpha), 2)}° | {fr(sect, 4)}"
    else:
        cr = "— | — | — | —"
    rect = (f"{fr(2 * sqrt(1 - k * k), 4)} × {fr(2 * k, 4)}" + (" (carré)" if abs(k - 1 / sqrt(2)) < 1e-9 else "")) if k < 1 - 1e-12 else "aucun (k ≥ 1)"
    ligne(f"| {fr(d, 4)} | {fr(k, 4)} | {cr} | {rect} |")
ligne("")
ligne(f"Événements : plateau tant que δ ≤ 1 − 1/√2 = {fr(d_star, 4)} (tangence intérieure, Q = Q' naît en (1, 0)) ;"
      f" k = 1 en δ = {fr(d_eq, 5)} (cercles égaux : chaque disque couvre la moitié de l'autre, c'est la FTM50) ;"
      " δ = 1 : piquet sur la clôture ; au-delà, la corde commune tend vers un diamètre (x₀ ≈ 1/(3δ)).")
psi = 2 * acos(d_p)
ligne(f"Corde commune passant par le piquet en δ = {fr(d_p, 6)} (k = {fr(ch.corde_moitie(2, d_p), 6)}) : "
      f"ψ − sin ψ = (π/2)(1 + cos ψ) avec ψ = 2 arccos δ ; résidu {abs(psi - np.sin(psi) - pi / 2 * (1 + np.cos(psi))):.1e}")
res["evenements"] = {"plateau_fin": d_star, "corde_par_P": d_p, "cercles_egaux": d_eq}

# ---------------------------------------------------------------------------
titre("9. L'erreur des polygones et des polyèdres")
# ---------------------------------------------------------------------------
ligne("Polygone régulier inscrit (piquet sur un sommet) et circonscrit (piquet au milieu d'un côté) :")
ligne("")
ligne("| n côtés | inscrit : corde | écart × n² | circonscrit : corde | écart × n² |")
ligne("|---:|---:|---:|---:|---:|")
poly2 = []
for n in [3, 4, 6, 8, 12, 24, 48, 96, 192]:
    ri = ar.corde_moitie_polygone(ar.polygone_regulier(n), (1, 0))
    rc = ar.corde_moitie_polygone(ar.polygone_regulier(n, 1 / cos(pi / n), pi / n), (1, 0))
    poly2.append((n, ri, rc))
    ligne(f"| {n} | {fr(ri, 8)} | {fr((ri - r2) * n * n, 3)} | {fr(rc, 8)} | {fr((rc - r2) * n * n, 3)} |")
ligne("")
ligne("Polyèdres inscrits dans la sphère (piquet sur un sommet), chèvre 3D exacte : 1,228545")
ligne("")
ligne("| polyèdre | sommets | faces (triangles) | volume / volume de la boule | corde | écart | écart × faces |")
ligne("|---|---:|---:|---:|---:|---:|---:|")
r3 = 1.2285448637352209
poly3 = []
for nom in ["tetra", "octa", "cube", "icosa", "dodeca", "geo2", "geo4", "geo8"]:
    r, nv, nf, vol = ar.corde_moitie_polyedre(nom)
    poly3.append((nom, nv, nf, vol, r))
    ligne(f"| {nom} | {nv} | {nf} | {fr(vol / (4 * pi / 3), 4)} | {fr(r, 6)} | {fr(r - r3, 5)} | {fr((r - r3) * nf, 3)} |")
res["polygones"] = poly2
res["polyedres"] = poly3

os.makedirs(SORTIE, exist_ok=True)
with open(os.path.join(SORTIE, "archimede.md"), "w") as fh:
    fh.write("# Résultats numériques de la partie II (générés par scripts/calculs_archimede.py)\n")
    fh.write("\n".join(md) + "\n")
with open(os.path.join(SORTIE, "archimede.json"), "w") as fh:
    json.dump(res, fh, indent=1, ensure_ascii=False, default=float)
print("\nÉcrit :", os.path.join(SORTIE, "archimede.md"))
