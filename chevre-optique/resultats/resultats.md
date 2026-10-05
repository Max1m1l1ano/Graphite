# Résultats numériques (générés par scripts/calculs.py)

## 1. Chèvre plane : la formule d'Ullisch (quotient de deux intégrales de contour)

Équation : sin β − β cos β = π/2 ; corde r = 2 cos(β/2)
- β (racine, findroot 50 chiffres) = 1.905695729309883894882666437160966703495
- β en degrés = 109.18832232556171784
- r/R = 1.158728473018121517828233509933509149688
- corde des intersections à x0 = 1 − r²/2 = 0.328674162908546 R du centre
- zéros de f dans |z − 3π/4| = π/4 (principe de l'argument) : 1.0
- contour imprimé par erreur en 2020, |z − 3π/8| = π/4 : 1.0 zéro, quotient = 1.905695729309883894882666 (même β)

| nœuds N (trapèzes) | β approché par le quotient | erreur |
|---:|:---|---:|
| 4 | 1.94204174477597588892458500311 | 0.0363 |
| 8 | 1.90777203111540297120264851034 | 0.00208 |
| 12 | 1.90578380388998638197517668013 | 8.81e-5 |
| 16 | 1.90569943584935422926134029766 | 3.71e-6 |
| 24 | 1.90569573587280654173724427375 | 6.56e-9 |
| 32 | 1.90569572932150249372334658611 | 1.16e-11 |
| 48 | 1.90569572930988393129642759819 | 3.64e-17 |
| 64 | 1.90569572930988389488278056125 | 1.14e-22 |
| 96 | 1.90569572930988389488266643716 | 1.12e-33 |
| 128 | 1.90569572930988389488266643716 | 1.1e-44 |

## 2. Chèvre en dimension n : W_n(2α) − (2cos α)^n W_n(α) = W_n(π)/2, r = 2cos α

Contrôle : la même « division d'intégrales complexes » marche en toute dimension
(contour |α − 7π/24| = π/16, qui entoure l'intervalle [π/4, π/3]) :

| n | zéros dans le contour | r_n par le quotient (N = 256) | r_n par recherche directe | écart |
|---:|---:|:---|:---|---:|
| 2 | 1.0 | 1.1587284730181215178 | 1.1587284730181215178 | 2.2e-30 |
| 3 | 1.0 | 1.2285448637352209034 | 1.2285448637352209034 | 2.4e-31 |
| 4 | 1.0 | 1.2680792566734182335 | 1.2680792566734182335 | 4.6e-31 |
| 5 | 1.0 | 1.2935979963602277668 | 1.2935979963602277668 | 1.5e-31 |
| 6 | 1.0 | 1.3114618190271589105 | 1.3114618190271589105 | 3.8e-31 |
| 8 | 1.0 | 1.3348624291579096201 | 1.3348624291579096201 | 1.9e-30 |

| n | r_n / R | angle α_n (°) | √(2n/(n+1)) | écart | x0 = 1 − r²/2 | 1/(n+1) | fraction broutée avec corde √2 |
|---:|:---|---:|:---|---:|:---|:---|:---|
| 1 | 1.0 | 60.0 | 1.0 | -9.4e-38 | 0.5 | 0.5 | 0.707107 |
| 2 | 1.15872847302 | 54.59416 | 1.154700538 | 0.00403 | 0.328674 | 0.333333 | 0.68169 |
| 3 | 1.22854486374 | 52.10093 | 1.224744871 | 0.0038 | 0.245339 | 0.25 | 0.664214 |
| 4 | 1.26807925667 | 50.65121 | 1.264911064 | 0.00317 | 0.195987 | 0.2 | 0.651174 |
| 5 | 1.29359799636 | 49.69931 | 1.290994449 | 0.0026 | 0.163302 | 0.166667 | 0.640927 |
| 6 | 1.31146181903 | 49.02491 | 1.309307341 | 0.00215 | 0.140034 | 0.142857 | 0.632582 |
| 7 | 1.32467963587 | 48.52143 | 1.322875656 | 0.0018 | 0.122612 | 0.125 | 0.625604 |
| 8 | 1.33486242916 | 48.13089 | 1.333333333 | 0.00153 | 0.109071 | 0.111111 | 0.619651 |
| 9 | 1.34295179854 | 47.81892 | 1.341640786 | 0.00131 | 0.0982402 | 0.1 | 0.61449 |
| 10 | 1.34953544 | 47.56389 | 1.348399725 | 0.00114 | 0.089377 | 0.0909091 | 0.609957 |
| 11 | 1.35499938928 | 47.35143 | 1.354006401 | 0.000993 | 0.0819883 | 0.0833333 | 0.605933 |
| 12 | 1.35960781712 | 47.17168 | 1.358732441 | 0.000875 | 0.0757333 | 0.0769231 | 0.602327 |
| 13 | 1.36354767324 | 47.01759 | 1.362770288 | 0.000777 | 0.0703689 | 0.0714286 | 0.599072 |
| 14 | 1.36695502304 | 46.88401 | 1.366260102 | 0.000695 | 0.065717 | 0.0666667 | 0.596114 |
| 15 | 1.36993128222 | 46.76709 | 1.369306394 | 0.000625 | 0.0616441 | 0.0625 | 0.593408 |
| 16 | 1.37255360198 | 46.6639 | 1.371988681 | 0.000565 | 0.0580483 | 0.0588235 | 0.590922 |
| 17 | 1.37488172634 | 46.57213 | 1.374368542 | 0.000513 | 0.0548501 | 0.0555556 | 0.588626 |
| 18 | 1.37696264599 | 46.48999 | 1.376494403 | 0.000468 | 0.0519869 | 0.0526316 | 0.586498 |
| 19 | 1.37883383329 | 46.41603 | 1.378404875 | 0.000429 | 0.0494086 | 0.05 | 0.584517 |
| 20 | 1.38052553916 | 46.34909 | 1.380131119 | 0.000394 | 0.0470746 | 0.047619 | 0.582668 |
| 30 | 1.39141487508 | 45.91638 | 1.391216687 | 0.000198 | 0.0319823 | 0.0322581 | 0.569086 |
| 50 | 1.40035933802 | 45.55858 | 1.400280084 | 7.93e-5 | 0.0194969 | 0.0196078 | 0.554594 |
| 100 | 1.40721663872 | 45.28278 | 1.407195089 | 2.15e-5 | 0.00987067 | 0.00990099 | 0.539224 |
| 1000 | 1.41350721901 | 45.02861 | 1.413506985 | 2.34e-7 | 0.000998671 | 0.000999001 | 0.512594 |
| 10000 | 1.41414285935 | 45.00286 | 1.414142857 | 2.35e-9 | 9.99867e-5 | 9.999e-5 | 0.503989 |

Développement asymptotique (vérifié numériquement) :
- n = 100 : (r² − 2n/(n+1))·n² = 0.60648475  (→ 2/3) ; (√2 − r)·n = 0.69969237  (→ 1/√2 = 0.70711)
- n = 1000 : (r² − 2n/(n+1))·n² = 0.66018956  (→ 2/3) ; (√2 − r)·n = 0.70634336  (→ 1/√2 = 0.70711)
- n = 10000 : (r² − 2n/(n+1))·n² = 0.6660139  (→ 2/3) ; (√2 − r)·n = 0.7070302  (→ 1/√2 = 0.70711)

## 3. Dimensions impaires : polynômes, radicaux et groupes de Galois

- n = 1 : r - 1 = 0  (degré 1, racine utile 1.000000000000000000000000)
- n = 3 : 3*r**4 - 8*r**3 + 8 = 0  (degré 4, racine utile 1.228544863735220903448994)
- n = 5 : 5*r**8 - 80*r**6 + 128*r**5 - 128 = 0  (degré 8, racine utile 1.293597996360227766755081)
- n = 7 : 7*r**12 - 112*r**10 + 840*r**8 - 1024*r**7 + 1024 = 0  (degré 12, racine utile 1.324679635868415915226147)
- n = 9 : 45*r**16 - 864*r**14 + 6720*r**12 - 32256*r**10 + 32768*r**9 - 32768 = 0  (degré 16, racine utile 1.342951798535436973578277)

Groupes de Galois (critère de Jordan via les réductions modulo p) :
- n = 3 : degré 4, d-cycle mod 13, (d−1)-cycle mod 5, transposition mod 19 ⇒ Gal = S_4 : prouvé ⇒ résoluble par radicaux : oui
- n = 5 : degré 8, d-cycle mod 13, (d−1)-cycle mod 3, transposition mod 7 ⇒ Gal = S_8 : prouvé ⇒ résoluble par radicaux : non
- n = 7 : degré 12, d-cycle mod 47, (d−1)-cycle mod 17, transposition mod 281 ⇒ Gal = S_12 : prouvé ⇒ résoluble par radicaux : non
- n = 9 : degré 16, d-cycle mod 41, (d−1)-cycle mod 13, transposition mod 7 ⇒ Gal = S_16 : prouvé ⇒ résoluble par radicaux : non

Forme close en 3D (Ferrari) : avec u = ∛(1+√2) et w = (u + 1/u)/√2,
r₃ = 2 / (√w + √(2/√w − w)) = 1.2285448637352209034489944976852935
contrôle 3r⁴ − 8r³ + 8 = -1.84e-40

Dimensions paires : W_n(θ) = c_n·θ + P_n(θ) (P_n trigonométrique), l'équation devient
c_n(2 − rⁿ)·α + T = c_n·π/2 avec T = P_n(2α) − rⁿP_n(α). Si r était algébrique, T, cos α, sin α et e^{iα}
le seraient aussi : relation linéaire T + (algébrique)·log e^{iα} + (algébrique)·log(−1) = 0 avec T ≠ 0,
interdite par le théorème de Baker (1966). Il suffit donc de vérifier T ≠ 0 :
- n = 2 : c_n = 0.5, T(α_n) = 0.4722216891 ≠ 0 ⇒ r_2 transcendant
- n = 4 : c_n = 0.375, T(α_n) = 0.7832295597 ≠ 0 ⇒ r_4 transcendant
- n = 6 : c_n = 0.3125, T(α_n) = 1.316530923 ≠ 0 ⇒ r_6 transcendant
- n = 8 : c_n = 0.2734375, T(α_n) = 2.285651593 ≠ 0 ⇒ r_8 transcendant
- n = 10 : c_n = 0.24609375, T(α_n) = 4.071507695 ≠ 0 ⇒ r_10 transcendant
- n = 20 : c_n = 0.17619705, T(α_n) = 90.10857187 ≠ 0 ⇒ r_20 transcendant

## 4. Tous les paramètres : piquet à la distance δ, courbe des 50 %

k_n(δ) = corde qui donne la moitié du champ ; comparaison avec k² ≈ δ² + (n−1)/(n+1) et la limite √(1+δ²)

| n | δ | k_n(δ) exact | √(δ²+(n−1)/(n+1)) | limite n→∞ √(1+δ²) | régime |
|---:|---:|:---|:---|:---|:---|
| 1 | 0 | 0.5 | 0.0 | 1.0 | corde dans le champ |
| 1 | 0.25 | 0.5 | 0.25 | 1.030776406 | corde dans le champ |
| 1 | 1 | 1.0 | 1.0 | 1.414213562 | piquet au bord |
| 1 | 2 | 2.0 | 2.0 | 2.236067977 | piquet dehors |
| 1 | 5 | 5.0 | 5.0 | 5.099019514 | piquet dehors |
| 2 | 0 | 0.7071067812 | 0.5773502692 | 1.0 | corde dans le champ |
| 2 | 0.25 | 0.7071067812 | 0.6291528696 | 1.030776406 | corde dans le champ |
| 2 | 1 | 1.158728473 | 1.154700538 | 1.414213562 | piquet au bord |
| 2 | 2 | 2.082249857 | 2.081665999 | 2.236067977 | piquet dehors |
| 2 | 5 | 5.033262103 | 5.033222957 | 5.099019514 | piquet dehors |
| 3 | 0 | 0.793700526 | 0.7071067812 | 1.0 | corde dans le champ |
| 3 | 0.25 | 0.7964019672 | 0.75 | 1.030776406 | piquet dedans |
| 3 | 1 | 1.228544864 | 1.224744871 | 1.414213562 | piquet au bord |
| 3 | 2 | 2.121915781 | 2.121320344 | 2.236067977 | piquet dehors |
| 3 | 5 | 5.04979352 | 5.049752469 | 5.099019514 | piquet dehors |
| 10 | 0 | 0.9330329915 | 0.9045340337 | 1.0 | corde dans le champ |
| 10 | 0.25 | 0.9502140155 | 0.9384464919 | 1.030776406 | piquet dedans |
| 10 | 1 | 1.34953544 | 1.348399725 | 1.414213562 | piquet au bord |
| 10 | 2 | 2.195226568 | 2.195035721 | 2.236067977 | piquet dehors |
| 10 | 5 | 5.081173068 | 5.081159495 | 5.099019514 | piquet dehors |
| 100 | 0 | 0.9930924954 | 0.9900495037 | 1.0 | corde dans le champ |
| 100 | 0.25 | 1.021488482 | 1.021125859 | 1.030776406 | piquet dedans |
| 100 | 1 | 1.407216639 | 1.407195089 | 1.414213562 | piquet au bord |
| 100 | 2 | 2.231639189 | 2.231635727 | 2.236067977 | piquet dehors |
| 100 | 5 | 5.097077644 | 5.0970774 | 5.099019514 | piquet dehors |

- Piquet au centre : k = 2^(−1/n) (n = 2 : 1/√2 = 0.70710678, c'est le « diaphragme d'un stop »).
- La corde reste inscrite dans le champ tant que δ ≤ 1 − 2^(−1/n) (n = 2 : δ ≤ 0,2929) : tangence intérieure à la fin.
- Piquet très loin : k ≈ δ + (n−1)/(2(n+1)δ) (n = 2 : δ + 1/(6δ)).

## 5. Volume et surface de la boule unité selon la dimension

| n | V_n | S_{n−1} = n·V_n | part du volume à moins de 0,1 R de l'« équateur » | part du volume dans la coquille extérieure de 0,1 R |
|---:|---:|---:|---:|---:|
| 1 | 2.000000 | 2.000000 | 10.0% | 10.0% |
| 2 | 3.141593 | 6.283185 | 12.7% | 19.0% |
| 3 | 4.188790 | 12.566371 | 14.9% | 27.1% |
| 4 | 4.934802 | 19.739209 | 16.9% | 34.4% |
| 5 | 5.263789 | 26.318945 | 18.6% | 41.0% |
| 6 | 5.167713 | 31.006277 | 20.2% | 46.9% |
| 7 | 4.724766 | 33.073362 | 21.7% | 52.2% |
| 8 | 4.058712 | 32.469697 | 23.0% | 57.0% |
| 9 | 3.298509 | 29.686580 | 24.3% | 61.3% |
| 10 | 2.550164 | 25.501640 | 25.5% | 65.1% |
| 11 | 1.884104 | 20.725143 | 26.6% | 68.6% |
| 12 | 1.335263 | 16.023153 | 27.7% | 71.8% |
| 13 | 0.910629 | 11.838174 | 28.7% | 74.6% |
| 14 | 0.599265 | 8.389703 | 29.7% | 77.1% |
| 15 | 0.381443 | 5.721649 | 30.7% | 79.4% |
| 16 | 0.235331 | 3.765290 | 31.6% | 81.5% |
| 17 | 0.140981 | 2.396679 | 32.5% | 83.3% |
| 18 | 0.082146 | 1.478626 | 33.4% | 85.0% |
| 19 | 0.046622 | 0.885810 | 34.2% | 86.5% |
| 20 | 0.025807 | 0.516138 | 35.0% | 87.8% |

- Volume maximal en n = 5 (V₅ = 8π²/15 = 5.263789) ; surface maximale en n = 7 (S₆ = 16π³/15 = 33.073362).
- Coquille extérieure d'épaisseur 1 % : fraction du volume = 1 − 0,99ⁿ → n=2: 2.0%, n=3: 3.0%, n=10: 9.6%, n=100: 63.4%, n=1000: 100.0%

## 6. Optique : la même machine (quotient d'intégrales de contour)

- FTM50 d'une pupille circulaire parfaite : ψ − sin ψ = π/2 → ψ = 2.30988146001006 ; ν50 = cos(ψ/2)·ν_c = 0.4039727533 ν_c (zéros dans le contour : 1.0)
    f/4, λ = 550 nm : coupure 455 cycles/mm, FTM50 = 184 cycles/mm
    f/8, λ = 550 nm : coupure 227 cycles/mm, FTM50 = 92 cycles/mm
    f/11, λ = 550 nm : coupure 165 cycles/mm, FTM50 = 67 cycles/mm
    f/16, λ = 550 nm : coupure 114 cycles/mm, FTM50 = 46 cycles/mm
- FTM au décalage d'un rayon (vesica piscis) : 0.39100222
- Tache d'Airy, 50 % de l'énergie : J0² + J1² = 1/2 → x = 1.68022474619 → rayon = 0.534832 λN (1er anneau noir : 1.21967 λN, qui contient 0.8378 de l'énergie)
- Diffraction par une fente : 1er maximum secondaire où sin x − x cos x = 0 → x = 4.49340945791 (≈ 1,4303 π)
- Kepler (Terre/Soleil, e = 0.0167, M = 1 rad) : E = 1.01417908716471, résidu -2.0e-31
- Kepler (Lune, e = 0.0549, M = 1 rad) : E = 1.04755459241863, résidu -3.9e-31

Éclipses (disques Soleil R = 1, Lune k, distance des centres d) :
- k = 0.90, centre lunaire sur le bord du Soleil : obscuration 32.6%, magnitude 0.450
- k = 0.95, centre lunaire sur le bord du Soleil : obscuration 35.8%, magnitude 0.475
- k = 1.00, centre lunaire sur le bord du Soleil : obscuration 39.1%, magnitude 0.500
- k = 1.05, centre lunaire sur le bord du Soleil : obscuration 42.5%, magnitude 0.525
- k = 1.08, centre lunaire sur le bord du Soleil : obscuration 44.5%, magnitude 0.540
- k = 0.92 : 50 % d'obscuration quand d = 0.7037 R, soit une magnitude 0.608
- k = 1.00 : 50 % d'obscuration quand d = 0.8079 R, soit une magnitude 0.596
- k = 1.05 : 50 % d'obscuration quand d = 0.8701 R, soit une magnitude 0.590
- Longueur du cône d'ombre (tangentes extérieures communes) : 374 532 km ; sommet du cône de pénombre (tangentes intérieures) à 372 666 km de la Lune, côté Soleil
    Lune à 356 400 km du centre de la Terre : la pointe de l'ombre est à +18 132 km du centre de la Terre (rayon 6 371 km)
    Lune à 384 400 km du centre de la Terre : la pointe de l'ombre est à -9 868 km du centre de la Terre (rayon 6 371 km)
    Lune à 406 700 km du centre de la Terre : la pointe de l'ombre est à -32 168 km du centre de la Terre (rayon 6 371 km)

Anneaux de Newton (λ = 589,3 nm, lentille R1 = 1 m) : ρ_m = √(m λ R_eff), 1/R_eff = 1/R1 ∓ 1/R2
- sur un plan : R_eff = 1 m, ρ1 = 0.768 mm, ρ2 = 1.086 mm (= √2·ρ1), aire par anneau 1.851 mm²
- dans un concave R2 = 1,5 m (contact intérieur) : R_eff = 3 m, ρ1 = 1.330 mm, ρ2 = 1.880 mm (= √2·ρ1), aire par anneau 5.554 mm²
- sur un convexe R2 = 1,5 m (contact extérieur) : R_eff = 0.6 m, ρ1 = 0.595 mm, ρ2 = 0.841 mm (= √2·ρ1), aire par anneau 1.111 mm²
- dans un calibre concave R2 = 1,01 m : R_eff = 101 m, ρ1 = 7.715 mm, ρ2 = 10.910 mm (= √2·ρ1), aire par anneau 186.985 mm²
- Calibre : pièce Ø 50 mm, R = 100 mm, erreur de rayon 10 µm → 1.14 frange(s)

Lentilles :
- Chèvre 3D = lentille biconvexe (épaisseur 1.2285 R, diamètre 1.9389 R) de même volume que le ménisque restant ; plan des intersections à 0.2453 R du centre
- Boule d’eau d'indice 1.333 : focale effective 2.002 R (comptée du centre), foyer à 1.002 R de la surface
- Boule de verre d'indice 1.5 : focale effective 1.500 R (comptée du centre), foyer à 0.500 R de la surface
- Boule de verre d'indice 2.0 : focale effective 1.000 R (comptée du centre), foyer à 0.000 R de la surface
- Loi en cos⁴ au bord d'un champ de 135° (67,5°) : 0.0214, soit 5.54 diaphragmes perdus
