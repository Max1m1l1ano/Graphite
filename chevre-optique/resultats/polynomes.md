# Résultats de la partie VII (générés par scripts/polynomes.py)

## 1. Dimensions impaires : des polynômes entiers

| n | degré | polynôme (normalisé) | h_n | terme constant | racine | corde (partie I) |
|---:|---:|---|---|---|---|---|
| 3 | 4 | 3 r^4 − 8 r^3 + 8 | 2/3 | +2^3 | 1,22854486373522 | 1,22854486373522 |
| 5 | 8 | 5 r^8 − 80 r^6 + 128 r^5 − 128 | 8/15 | −2^7 | 1,29359799636023 | 1,29359799636023 |
| 7 | 12 | 7 r^12 − 112 r^10 + 840 r^8 − 1024 r^7 + 1024 | 16/35 | +2^10 | 1,32467963586842 | 1,32467963586842 |
| 9 | 16 | 45 r^16 − 864 r^14 + 6720 r^12 − 32256 r^10 + 32768 r^9 − 32768 | 128/315 | −2^15 | 1,34295179853544 | 1,34295179853544 |
| 13 | 24 | 273 r^24 − 7280 r^22 + … + 2^22 r^13 − 2^22 (degré 24) | 1024/3003 | −2^22 | 1,36354767323759 | 1,36354767323759 |

Forme d'Archimède : h_n·(rⁿ − 1) = G_n(r²), polynôme pair en r. Exemples :
- n = 3 : (2/3)·(r^3 − 1) = r^4/4
- n = 5 : (8/15)·(r^5 − 1) = -r^8/48 + r^6/3
- n = 7 : (16/35)·(r^7 − 1) = r^12/320 - r^10/20 + 3·r^8/8

Dimension 13 (degré 24) : irréductible sur Q = True ; modulo 19, facteurs de degrés [1, 3, 3, 17] → un 17-cycle (Jordan : le groupe contient A₂₄) ; modulo 5, degrés [24] → permutation impaire ; groupe de Galois = S₂₄

## 2. Dimensions paires : κ_n·[π/2 − (2 − rⁿ)·α] = √(4 − r²)·Π_n(r), α = arccos(r/2)

| n | κ_n = C(2m, m)/4^m | Π_n (degré) | résidu à la corde de la partie I |
|---:|---|---|---|
| 2 | 1/2 | r/4 | 0.0 |
| 6 | 5/16 | -r^9/128 + 13·r^7/128 + r^5/192 + 5·r^3/192 + 5·r/32 | -3.9e-31 |
| 12 | 231/1024 | degré 21 | 1.6e-30 |
| 24 | 676039/4194304 | degré 45 | 1.0e-28 |

## 3. Réciprocité : κ_(2m)·h_(2m+1) = 1/(2m+1)

| paire ↔ impaire | κ_(2m) | h_(2m+1) | produit |
|---|---|---|---|
| 2 ↔ 3 | 1/2 | 2/3 | 1/3 |
| 4 ↔ 5 | 3/8 | 8/15 | 1/5 |
| 6 ↔ 7 | 5/16 | 16/35 | 1/7 |
| 12 ↔ 13 | 231/1024 | 1024/3003 | 1/13 |
| 24 ↔ 25 | 676039/4194304 | 4194304/16900975 | 1/25 |

## 4. Les facteurs 2 comptent les retenues de la base 2 (Kummer)

| n pair | m = n/2 en binaire | retenues (nombre de 1) | dénominateur de κ_n |
|---:|---|---:|---|
| 2 | 1 | 1 | 2^1 = 2^(2 − 1) |
| 4 | 10 | 1 | 2^3 = 2^(4 − 1) |
| 6 | 11 | 2 | 2^4 = 2^(6 − 2) |
| 8 | 100 | 1 | 2^7 = 2^(8 − 1) |
| 10 | 101 | 2 | 2^8 = 2^(10 − 2) |
| 12 | 110 | 2 | 2^10 = 2^(12 − 2) |
| 14 | 111 | 3 | 2^11 = 2^(14 − 3) |
| 16 | 1000 | 1 | 2^15 = 2^(16 − 1) |
| 18 | 1001 | 2 | 2^16 = 2^(18 − 2) |
| 20 | 1010 | 2 | 2^18 = 2^(20 − 2) |
| 22 | 1011 | 3 | 2^19 = 2^(22 − 3) |
| 24 | 1100 | 2 | 2^22 = 2^(24 − 2) |
| 26 | 1101 | 3 | 2^23 = 2^(26 − 3) |
| 28 | 1110 | 3 | 2^25 = 2^(28 − 3) |
| 30 | 1111 | 4 | 2^26 = 2^(30 − 4) |
| 32 | 10000 | 1 | 2^31 = 2^(32 − 1) |

| n impair | degré 2(n−1) | (n−1)/2 en binaire | terme constant | dénominateur de κ en dimension 2(n−1) |
|---:|---:|---|---|---|
| 3 | 4 | 1 | +2^3 | 2^3 = le même |
| 5 | 8 | 10 | −2^7 | 2^7 = le même |
| 7 | 12 | 11 | +2^10 | 2^10 = le même |
| 9 | 16 | 100 | −2^15 | 2^15 = le même |
| 11 | 20 | 101 | +2^18 | 2^18 = le même |
| 13 | 24 | 110 | −2^22 | 2^22 = le même |
| 15 | 28 | 111 | +2^25 | 2^25 = le même |
| 17 | 32 | 1000 | −2^31 | 2^31 = le même |
| 19 | 36 | 1001 | +2^34 | 2^34 = le même |
| 21 | 40 | 1010 | −2^38 | 2^38 = le même |
| 23 | 44 | 1011 | +2^41 | 2^41 = le même |
| 25 | 48 | 1100 | −2^46 | 2^46 = le même |
| 27 | 52 | 1101 | +2^49 | 2^49 = le même |
| 29 | 56 | 1110 | −2^53 | 2^53 = le même |
| 31 | 60 | 1111 | +2^56 | 2^56 = le même |

## 5. La preuve : F/h n'a que des fractions binaires finies

- formule fermée F/h = (rⁿ − 1) − Σ (−1)^k B(m,k) r^(2(m+1+k)) / 2^(2m+2k+1) identique au polynôme exact, n = 3 à 31 : True
- étude de cas de Legendre (q impair ≤ 301, toutes les valeurs de α et β) : contribution ≥ 0 partout : True
- B(m, k) entier pour m ≤ 400 : True
- exposant du terme constant = 4m − (nombre de 1 de m), m ≤ 400 (n ≤ 801) : True ; B(m, m−1) = (2m+1)·Catalan(m−1) : True

| n | h_n | période binaire de h_n | périodes des coefficients de F | toutes divisent celle de h_n |
|---:|---|---:|---|---|
| 3 | 2/3 | 2 | [2, 0] | True |
| 5 | 8/15 | 4 | [4, 2, 2] | True |
| 7 | 16/35 | 12 | [12, 0, 4, 4] | True |
| 9 | 128/315 | 12 | [12, 4, 2, 12, 3] | True |
| 13 | 1024/3003 | 60 | [60, 3, 0, 2, 3, 10, 10] | True |

« Cercle de confusion » de 0,1 % : l'écart relatif chèvre / simplexe passe sous 0,1 % dès la dimension 9
