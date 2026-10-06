# Résultats de la partie XII (générés par scripts/lentille_144.py)

## 1. L'angle d'or approché par les nombres de Fibonacci

Angle d'or exact : 360°/φ² = 137,507764° ; complément 360°/φ = 222,492236°.

| k | F(k) | fraction de tour | angle (degrés) | complément | écart à l'angle d'or | écriture décimale finie ? |
|---:|---:|---|---|---|---|---|
| 3 | 2 | 1/2 | 180,000000 | 180,000000 | +42,492236 | oui |
| 4 | 3 | 1/3 | 120,000000 | 240,000000 | −17,507764 | oui |
| 5 | 5 | 2/5 | 144,000000 | 216,000000 | +6,492236 | oui |
| 6 | 8 | 3/8 | 135,000000 | 225,000000 | −2,507764 | oui |
| 7 | 13 | 5/13 | 138,461538 | 221,538462 | +0,953774 | non |
| 8 | 21 | 8/21 | 137,142857 | 222,857143 | −0,364907 | non |
| 9 | 34 | 13/34 | 137,647059 | 222,352941 | +0,139295 | non |
| 10 | 55 | 21/55 | 137,454545 | 222,545455 | −0,053219 | non |
| 11 | 89 | 34/89 | 137,528090 | 222,471910 | +0,020326 | non |
| 12 | 144 | 55/144 | 137,500000 | 222,500000 | −0,007764 | oui |
| 13 | 233 | 89/233 | 137,510730 | 222,489270 | +0,002966 | non |
| 14 | 377 | 144/377 | 137,506631 | 222,493369 | −0,001133 | non |
| 15 | 610 | 233/610 | 137,508197 | 222,491803 | +0,000433 | non |
| 16 | 987 | 377/987 | 137,507599 | 222,492401 | −0,000165 | non |
| 17 | 1597 | 610/1597 | 137,507827 | 222,492173 | +0,000063 | non |
| 18 | 2584 | 987/2584 | 137,507740 | 222,492260 | −0,000024 | non |
| 19 | 4181 | 1597/4181 | 137,507773 | 222,492227 | +0,000009 | non |
| 20 | 6765 | 2584/6765 | 137,507761 | 222,492239 | −0,000004 | non |
| 21 | 10946 | 4181/10946 | 137,507765 | 222,492235 | +0,000001 | non |

Pour k = 12 : 55/144 de tour = 137,5° et 89/144 = 222,5° exactement ; le pas 360°/144 vaut 2,5° = 5²×10⁻¹, et 222,5 = 89 × 2,5 = 88 × 2,5 + 2,5 = 220 + 2,5.
Écart de 137,5° à l'angle d'or : −0,007764° ; prévision de Hurwitz 360°/(√5·144²) = 0,007764°.

## 2. Pourquoi 144 est la dernière

360 = 2³·3²·5. Une fraction F(k−2)/F(k) de tour s'écrit en degrés avec un nombre fini de décimales seulement si F(k) n'a pas d'autre facteur premier que 2, 3 et 5.

| k | F(k) | facteurs premiers | nouveau facteur premier (primitif) |
|---:|---:|---|---|
| 3 | 2 | 2 | 2 |
| 4 | 3 | 3 | 3 |
| 5 | 5 | 5 | 5 |
| 6 | 8 | 2^3 | aucun |
| 7 | 13 | 13 | 13 |
| 8 | 21 | 3 · 7 | 7 |
| 9 | 34 | 2 · 17 | 17 |
| 10 | 55 | 5 · 11 | 11 |
| 11 | 89 | 89 | 89 |
| 12 | 144 | 2^4 · 3^2 | aucun |
| 13 | 233 | 233 | 233 |
| 14 | 377 | 13 · 29 | 29 |
| 15 | 610 | 2 · 5 · 61 | 61 |
| 16 | 987 | 3 · 7 · 47 | 47 |
| 25 | 75025 | 5^2 · 3001 | 3001 |

Indices k ≥ 3 sans nouveau facteur premier, jusqu'à k = 60 : [6, 12] (F(6) = 8 et F(12) = 144). Théorème de Carmichael (1913) : au-delà de k = 12, chaque F(k) apporte un nouveau premier, forcément ≥ 7. Les fractions de Fibonacci de l'angle d'or tombent donc juste en degrés pour k = 3, 4, 5, 6 et 12, puis plus jamais.
144 = 12² est aussi le plus grand carré de la suite de Fibonacci (Cohn, 1964) ; avec 8, c'est la seule puissance parfaite au-delà de 1 (Bugeaud, Mignotte et Siksek, 2006).

## 3. La lentille de Fibonacci à 144 anneaux

Ses deux foyers sont en u = 55,0323 et 88,9677 (partie VIII), soit 0,38217 et 0,61783 du nombre d'anneaux, contre 55/144 = 0,38194, 89/144 = 0,61806 et 1/φ² = 0,38197, 1/φ = 0,61803.
En degrés (× 2,5°) : 137,581° et 222,419°.

| anneaux F(k) | foyers (u₁ ; u₂) | rapport u₂/u₁ | approximation de l'angle d'or 360·F(k−2)/F(k) |
|---:|---|---|---|
| 8 | 3,364 ; 4,636 | 1,37829 | 135,0000° |
| 13 | 4,935 ; 8,065 | 1,63408 | 138,4615° |
| 21 | 8,201 ; 12,799 | 1,56060 | 137,1429° |
| 34 | 12,979 ; 21,021 | 1,61963 | 137,6471° |
| 55 | 21,084 ; 33,916 | 1,60861 | 137,4545° |
| 89 | 33,993 ; 55,007 | 1,61821 | 137,5281° |
| 144 | 55,032 ; 88,968 | 1,61665 | 137,5000° |
| 233 | 88,997 ; 144,003 | 1,61806 | 137,5107° |
| 377 | 144,012 ; 232,988 | 1,61783 | 137,5066° |

## 4. La corde de la chèvre en dimension réelle, autour de 2,5

| dimension n | corde de la chèvre |
|---:|---|
| 2,000 | 1,158728 |
| 2,187 | 1,175600 |
| 2,240 | 1,179976 |
| 2,420 | 1,193688 |
| 2,450 | 1,195816 |
| 2,500 | 1,199270 |
| 2,550 | 1,202615 |
| 3,000 | 1,228545 |

La corde vaut celle du pentagone, 2 sin 36° (avec r² = 3 − φ), en n = 2,1866.
Bosse des écarts entre la chèvre et le simplexe (partie VI) : sommets en n = 2,24 (cordes), 2,42 (déplacement) et 3,20 (part manquante).
