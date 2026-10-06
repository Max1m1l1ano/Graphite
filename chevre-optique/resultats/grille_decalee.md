# Résultats de la partie XV (générés par scripts/grille_decalee.py)

## 1. La grille décalée d'une demi-maille

En 2D : des rangées espacées de 1 (la distance du piquet P au centre O), une rangée sur deux décalée d'une demi-maille. Si les triangles sont équilatéraux, la maille vaut 2/√3 = 1,154701 : c'est la grille hexagonale, et son triangle est celui de la chèvre (partie VI : sommet P, base par O).
En dimension n : le réseau A_n, la grille cubique de dimension n+1 coupée par le plan x₁ + … + x_{n+1} = 0. Le simplexe e₁, …, e_{n+1} a l'arête √2 (la diagonale d'une face du cube) et la hauteur √((n+1)/n).

| n | hauteur du simplexe e₁…e_{n+1} | √((n+1)/n) | arête ramenée à la hauteur 1 | s(n) = √(2n/(n+1)) |
|---:|---|---|---|---|
| 1 | 1,414214 | 1,414214 | 1,000000 | 1,000000 |
| 2 | 1,224745 | 1,224745 | 1,154701 | 1,154701 |
| 3 | 1,154701 | 1,154701 | 1,224745 | 1,224745 |
| 4 | 1,118034 | 1,118034 | 1,264911 | 1,264911 |
| 5 | 1,095445 | 1,095445 | 1,290994 | 1,290994 |
| 6 | 1,080123 | 1,080123 | 1,309307 | 1,309307 |

En 3D, A₃ (dans Z⁴, somme nulle) et la grille cubique à faces centrées (dans Z³, somme paire) ont les mêmes nombres de points aux distances² 2, 4, 6, 8 : [12, 6, 24, 12] et [12, 6, 24, 12]. C'est l'empilement des couches hexagonales décalées, le plus dense de l'espace (Kepler).
Variante « brique » (grille carrée, une rangée sur deux décalée d'une demi-maille, rangées espacées de 1) : la diagonale vaut √5/2 = 1,118034 = φ − 1/2, et l'angle au sommet du triangle vaut 2·arctan(1/2) = 53,1301°, l'angle du 3-4-5 (partie XIV).

## 2. La corde de la chèvre et la maille décalée : le ménisque

| n | corde r(n) | maille s(n) | écart r − s | écart relatif |
|---:|---|---|---|---|
| 1,5 | 1,098684 | 1,095445 | 0,003239 | 0,2957 % |
| 2 | 1,158728 | 1,154701 | 0,004028 | 0,3488 % |
| 2,5 | 1,199270 | 1,195229 | 0,004042 | 0,3382 % |
| 3 | 1,228545 | 1,224745 | 0,003800 | 0,3103 % |
| 4 | 1,268079 | 1,264911 | 0,003168 | 0,2505 % |
| 6 | 1,311462 | 1,309307 | 0,002154 | 0,1646 % |
| 10 | 1,349535 | 1,348400 | 0,001136 | 0,0842 % |
| 20 | 1,380526 | 1,380131 | 0,000394 | 0,0286 % |
| 50 | 1,400359 | 1,400280 | 0,000079 | 0,0057 % |
| 100 | 1,407217 | 1,407195 | 0,000022 | 0,0015 % |
| 400 | 1,412451 | 1,412449 | 0,000001 | 0,0001 % |

Le ménisque relatif est maximal en n = 2,0832 (0,3495 %), l'écart absolu en n = 2,2438 (0,004087, partie VI) : entre 2D et 3D. Ensuite les deux décroissent vers 0, et r comme s tendent vers √2, la diagonale du carré de la grille.

Meilleures distances offertes par chaque grille (rangées ou couches espacées de 1), comparées à la corde :

| grille | distance | écart à la corde |
|---|---|---|
| 2D : grille carrée, côté 1 | 1,000000 | −13,699 % |
| 2D : grille carrée, diagonale √2 | 1,414214 | +22,049 % |
| 2D : brique, diagonale √5/2 | 1,118034 | −3,512 % |
| 2D : grille décalée, maille 2/√3 | 1,154701 | −0,348 % |
| 3D : grille cubique, côté 1 | 1,000000 | −18,603 % |
| 3D : couches décalées, maille √(3/2) | 1,224745 | −0,309 % |

## 3. La chèvre comptée sur la grille : quand la grille voit le ménisque

Pré de rayon N (en mailles), piquet sur un point de la grille à la distance N : la corde comptée est la distance au piquet du point de rang médian. La grille « voit » le ménisque quand cette corde est plus près de la chèvre r(n) que du simplexe s(n).

| grille | voit le ménisque | toujours à partir de N | points du pré à ce N | corde comptée = arête du simplexe exactement |
|---|---|---|---|---|
| 2D, grille carrée | 95 % des tailles | 41 | 5261 | jamais |
| 2D, grille décalée | 98 % des tailles | 38 | 5239 | jamais |
| 3D, grille cubique | 83 % des tailles | 18 | 24405 | N = 2, N = 4, N = 6, N = 12, N = 14 |
| 3D, couches décalées | 97 % des tailles | 14 | 16295 | jamais |

La grille cubique contient la grille à couches décalées (les points de somme paire) : tant qu'elle est grossière, elle retombe pile sur l'arête du tétraèdre √(3/2), sans voir le ménisque.

## 4. Les dimensions d'or de la grille décalée

s(n)² = 2n/(n+1) : la maille atteint la valeur v en n = v²/(2 − v²), une dimension algébrique. La chèvre atteint la même valeur un peu plus tôt : le ménisque la décale.

| valeur de la maille | dimension exacte de la grille décalée | dimension où la chèvre l'atteint | décalage |
|---|---|---|---|
| 2/√3 (grille hexagonale) = 1,154701 | 2 = 2,000000 | 1,959030 | 0,0410 |
| 2 sin 36° (côté du pentagone, √(3 − φ)) = 1,175571 | √5 = 2,236068 | 2,186645 | 0,0494 |
| 6/5 (triangle 3-4-5) = 1,200000 | 18/7 = 2,571429 | 2,510772 | 0,0607 |
| √(3/2) (couches décalées) = 1,224745 | 3 = 3,000000 | 2,926202 | 0,0738 |
| 2/φ = 1,236068 | 2φ = 3,236068 | 3,155561 | 0,0805 |
| √φ = 1,272020 | φ³ = 4,236068 | 4,130669 | 0,1054 |

### La carte des dimensions particulières (parties III à XV)

| dimension n | ce qui s'y passe | partie |
|---:|---|---|
| 2,0000 | chèvre 2D sur la grille hexagonale (ménisque 0,35 %) | VI, XV |
| 2,0832 | ménisque relatif maximal | XV |
| 2,1866 | corde = côté du pentagone (φ) | XII |
| 2,2361 | maille décalée = côté du pentagone (n = √5) | XV |
| 2,2438 | ménisque absolu maximal | VI |
| 2,4222 | déplacement δ maximal | VI |
| 2,5000 | borne 5/2 de Wolff (Kakeya en 3D) | XIII |
| 2,5108 | corde = 6/5 (triangle 3-4-5) | XIII |
| 2,5831 | rⁿ = φ (limite de la ligne de Fibonacci) | XIII |
| 3,0000 | chèvre 3D sur les couches décalées (0,31 %) | VI, XV |
| 3,0001 | δ repasse au niveau de la 2D | VI |
| 3,1556 | corde = 2/φ | XIII |
| 3,1995 | part manquante maximale | VI |
| 3,2361 | maille décalée = 2/φ (n = 2φ) | XV |
| 4,1307 | corde = √φ (r² = φ) | XIII |
| 4,2361 | maille décalée = √φ (n = φ³) | XV |
| 7,0000 | corde ≈ nombre plastique (à 4·10⁻⁵ près) | III |

## 5. L'aiguille sur la grille décalée

| L | points de la grille décalée sur le cercle (comptés) | formule d'Eisenstein | points de la grille carrée (partie XIV) |
|---:|---:|---:|---:|
| 1 | 6 | 6 | 4 |
| 2 | 6 | 6 | 4 |
| 3 | 6 | 6 | 4 |
| 5 | 6 | 6 | 12 |
| 7 | 18 | 18 | 4 |
| 13 | 18 | 18 | 12 |
| 19 | 18 | 18 | 4 |
| 49 | 30 | 30 | 4 |
| 91 | 54 | 54 | 12 |

Sur la grille décalée, ce sont les nombres premiers de la forme 3k + 1 (7, 13, 19…) qui ouvrent des directions ; 5 n'en ouvre plus. L'angle du triangle 5-7-8 (ou 3-5-7) vaut arccos(11/14) = 38,2132° :

| L | directions par sixième de tour | longueurs des trous |
|---:|---:|---|
| 7^1 = 7 | 3 | 16,426 ; 21,787 |
| 7^2 = 49 | 5 | 5,360 ; 16,426 |
| 7^3 = 343 | 7 | 5,360 ; 11,066 ; 16,426 |

S'inverser avec la grille décalée (maille 1) :
- un bout fixe : 4 positions (0°, 60°, 120°, 180°), trois triangles équilatéraux d'aire totale 3√3/4 = 1,2990, contre π/2 = 1,5708 pour le demi-disque (grille carrée : 3 positions seulement) ;
- le milieu fixe (aiguille de longueur 2) : 3 positions, l'hexagone d'aire 3√3/2 = 2,5981, contre π = 3,1416 pour le disque ;
- chaque pas de rotation coûte au moins un triangle de la grille, √3/4 = 0,4330 : la demi-maille.

Échantillonnage (Petersen et Middleton, 1962) : à nombre de points égal, la grille décalée laisse passer des fréquences 7,5 % plus fines dans toutes les directions ; pour la même finesse, il lui faut 13,4 % de points en moins.
