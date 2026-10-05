# Résultats de la partie VIII (générés par scripts/foyer_fibonacci.py)

## 1. Retourner une aiguille de longueur 1

| façon de retourner | aire balayée | la longueur reste 1 ? |
|---|---|---|
| par un foyer, dans le plan de l'image (x ↦ λx, λ de 1 à −1) | 0 : l'aiguille reste sur sa droite | non : elle passe par 0 au foyer |
| par un foyer, le long de l'axe (objet et image à la distance d) | d : deux triangles opposés par le sommet | non |
| en pivotant autour du point à la distance t du milieu | π/4 + πt², minimum π/4 = 0,7854 pour t = 0 | oui |
| deltoïde de Kakeya | π/8 = 0,3927 (calculé : 0,392699) | oui : corde tangente de longueur 1,000000 à 1,000000 |
| Besicovitch–Perron (partie V) | aussi petite qu'on veut, mais ≥ c/log N avec N directions | oui |

Pivoter de 180° autour du milieu, c'est appliquer x ↦ −x : la même application que le foyer, sans passer par la longueur 0.

## 2. Le ménisque qui déphase : zones de Fresnel

Épaisseur du ménisque entre le plan du diaphragme et la sphère centrée au foyer, et retard du chemin optique :
| r (mm) | flèche f − √(f² − r²) (nm) | retard √(f² + r²) − f (nm) | r²/2f (nm) | nombre de demi-longueurs d'onde |
|---:|---:|---:|---:|---:|
| 0,1 | 100,00 | 100,00 | 100,00 | 0,36 |
| 0,5 | 2500,06 | 2499,94 | 2500,00 | 9,09 |
| 1,0 | 10001,00 | 9999,00 | 10000,00 | 36,36 |
| 2,0 | 40016,01 | 39984,01 | 40000,00 | 145,40 |

Zones de Fresnel pour f = 50 mm et λ = 550 nm : r_k = √(kλf), soit r₁ = 0,1658 mm ; chaque zone a la même aire πλf = 0,0864 mm², comme les anneaux de Newton (partie I).
Diaphragme ouvert, intensité sur l'axe (u = a²/2λz) : écart maximal à 4 sin²(πu) = 1.8e-15 ; noir pour u entier (nombre pair de zones), 4 fois l'intensité incidente pour u demi-entier.

## 3. Les deux ménisques de la FTM, et la défocalisation

Lentille = ménisque = π/2 (la condition de la chèvre pour deux disques égaux) : s = 0,807946, soit ν/ν_c = 0,4040 (FTM50 de la partie I).
Les deux ménisques (disque 1 privé du disque 2, et l'inverse) s'échangent par x ↦ −x autour du centre de la lentille : rotation de 180°.
Contrôle : FTM sans défocalisation contre formule fermée, écart maximal 4.4e-16
La FTO (la FTM avec son signe) devient négative (contraste inversé) au-delà de W₂₀ = 0,6416 λ, d'abord vers ν/ν_c = 0,489.

| défocalisation W₂₀ | premier zéro de la FTO (ν/ν_c) | minimum (contraste inversé) | approximation géométrique 2J₁(v)/v, premier zéro |
|---|---|---|---|
| 0,50 λ | aucun | 0,0012 en 0,990 | 0,3049 |
| 0,75 λ | 0,3000 | −0,0380 en 0,422 | 0,2033 |
| 1,00 λ | 0,1931 | −0,0728 en 0,275 | 0,1525 |
| 2,00 λ | 0,0840 | −0,1056 en 0,115 | 0,0762 |

## 4. Une facette géodésique est un ménisque de phase

Sur une onde qui converge vers le centre O de la sphère (le foyer), une facette plane retarde la lumière de l'épaisseur du ménisque qui la sépare de la sphère. Épaisseur maximale par facette, pour une sphère de rayon R :
| fréquence ν | facettes | ménisque le plus épais (R) | × ν² | zones de Fresnel par facette (R = 1 m, λ = 550 nm) |
|---:|---:|---|---|---:|
| 1 | 20 | 2,0535e−01 | 0,2053 | 746 711 |
| 2 | 80 | 6,5828e−02 | 0,2633 | 239 373 |
| 3 | 180 | 2,8353e−02 | 0,2552 | 103 102 |
| 5 | 500 | 1,1471e−02 | 0,2868 | 41 714 |
| 8 | 1280 | 4,5284e−03 | 0,2898 | 16 467 |
| 13 | 3380 | 1,7221e−03 | 0,2910 | 6 262 |
| 21 | 8820 | 6,5971e−04 | 0,2909 | 2 399 |
| 34 | 23120 | 2,5232e−04 | 0,2917 | 918 |

Le ménisque d'une facette suit 1/ν², comme les zones de Fresnel suivent r² : passer d'une fréquence de Fibonacci à la suivante le divise par (F_(k+1)/F_k)², qui tend vers φ².

## 5. Les géodésiques sont des rayons : l'œil de poisson de Maxwell

Point source P = (0,45 ; 0,25), image attendue P' = −P/|P|² = (−1,6981 ; −0,9434).
18 rayons tracés numériquement : tous repassent par P' à 7.1e-08 près. |OP|·|OP'| = 1,000000 = R².
Sur le cercle |x| = R, l'image de x est −x : la rotation de 180°, l'aiguille retournée.

## 6. La réciprocité κ₂ₘ·h₂ₘ₊₁ = 1/(2m + 1) et la boîte à chapeau d'Archimède

m = 1 à 12 : κ₂ₘ·h₂ₘ₊₁ = 1/(2m + 1) vérifié ; aire(S^2m) = 2π·volume(B^(2m−1)) vérifié (calcul exact).
Pour m = 1 : κ₂·h₃ = ½ · ⅔ = ⅓, et aire(S²) = 4π = 2π × 2 : la sphère a l'aire du cylindre qui l'entoure (Archimède).

## 7. La lentille de Fibonacci : deux foyers dans le rapport φ

| anneaux N = F_j | foyer 1 (u) | foyer 2 (u) | u₁ + u₂ | F_(j−2), F_(j−1) | rapport des distances focales z₁/z₂ = u₂/u₁ | écart des intensités |
|---:|---|---|---|---|---|---|
| 21 | 8,2012 | 12,7988 | 21,000000 | 8, 13 | 1,560599 | 1e-15 |
| 34 | 12,9789 | 21,0211 | 34,000000 | 13, 21 | 1,619635 | 4e-16 |
| 55 | 21,0840 | 33,9160 | 55,000000 | 21, 34 | 1,608612 | 5e-13 |
| 89 | 33,9927 | 55,0073 | 89,000000 | 34, 55 | 1,618211 | 5e-13 |
| 144 | 55,0323 | 88,9677 | 143,999999 | 55, 89 | 1,616647 | 7e-13 |
| 233 | 88,9973 | 144,0027 | 233,000000 | 89, 144 | 1,618057 | 1e-14 |
| 377 | 144,0123 | 232,9877 | 377,000000 | 144, 233 | 1,617832 | 6e-15 |
| 610 | 232,9990 | 377,0010 | 610,000000 | 233, 377 | 1,618037 | 3e-14 |

φ = 1,618034. La somme u₁ + u₂ vaut N : pour tout diaphragme à N zones égales, I(N − u) = I(u) exactement. Les deux foyers sont donc symétriques (en 1/z) autour du foyer unique u = N/2 de la lame de Fresnel périodique.
Lame de Fresnel périodique (144 zones) : un seul foyer principal, en u = 72,01 = 144/2.

## 8. Sphères géodésiques aux fréquences de Fibonacci

| fréquence ν | points | volume manquant 4π/3 − V | rapport au précédent | grille de Fibonacci, même N | grille / géodésique |
|---:|---:|---|---|---|---|
| 1 | 12 | 1,6526e+00 |  | 1,8184e+00 | 1,100 |
| 2 | 42 | 5,3008e−01 | 3,1177 | 5,6372e−01 | 1,063 |
| 3 | 92 | 2,4740e−01 | 2,1426 | 2,6562e−01 | 1,074 |
| 5 | 252 | 9,1544e−02 | 2,7025 | 9,7363e−02 | 1,064 |
| 8 | 642 | 3,6106e−02 | 2,5354 | 3,8394e−02 | 1,063 |
| 13 | 1692 | 1,3726e−02 | 2,6304 | 1,4571e−02 | 1,062 |
| 21 | 4412 | 5,2678e−03 | 2,6057 | 5,5909e−03 | 1,061 |
| 34 | 11562 | 2,0108e−03 | 2,6198 | 2,1334e−03 | 1,061 |
| 55 | 30252 | 7,6857e−04 | 2,6162 | 8,1542e−04 | 1,061 |

φ² = 2,6180. Avec les fréquences doublées de la partie II (2, 4, 8…), le même rapport tend vers 4 = 2² :
- ν = 1 → 2 : rapport 3,1177
- ν = 2 → 4 : rapport 3,7386
- ν = 4 → 8 : rapport 3,9269
- ν = 8 → 16 : rapport 3,9813
- ν = 16 → 32 : rapport 3,9953
