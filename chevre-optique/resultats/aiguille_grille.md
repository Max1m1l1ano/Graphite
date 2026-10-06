# Résultats de la partie XIV (générés par scripts/aiguille_grille.py)

## 1. Les directions permises sur la grille

Une aiguille de longueur L, ses deux bouts sur des points de la grille : ses directions sont les points de la grille sur le cercle de rayon L.

| L | points sur le cercle (comptés) | formule de Jacobi | directions par quart de tour | plus grand trou |
|---:|---:|---:|---:|---|
| 1 | 4 | 4 | 1 | 90,00° |
| 2 | 4 | 4 | 1 | 90,00° |
| 3 | 4 | 4 | 1 | 90,00° |
| 5 | 12 | 12 | 3 | 36,87° |
| 10 | 12 | 12 | 3 | 36,87° |
| 13 | 12 | 12 | 3 | 44,76° |
| 25 | 20 | 20 | 5 | 20,61° |
| 65 | 36 | 36 | 9 | 16,26° |
| 125 | 28 | 28 | 7 | 16,26° |
| 325 | 60 | 60 | 15 | 12,24° |
| 625 | 36 | 36 | 9 | 16,26° |
| 1105 | 108 | 108 | 27 | 8,37° |
| 5525 | 180 | 180 | 45 | 5,45° |

L'angle du triangle 3-4-5 : arctan(4/3) = 2·arctan(1/2) = 53,130102°.
Pour L = 5^k, les directions sont les m × 53,13° (m de −k à k), à un quart de tour près :

| L | directions par quart de tour | longueurs des trous (degrés) |
|---:|---:|---|
| 5^1 = 5 | 3 | 16,260 ; 36,870 |
| 5^2 = 25 | 5 | 16,260 ; 20,610 |
| 5^3 = 125 | 7 | 4,349 ; 16,260 |
| 5^4 = 625 | 9 | 4,349 ; 11,911 ; 16,260 |
| 5^5 = 3125 | 11 | 4,349 ; 11,911 ; 16,260 |
| 5^6 = 15625 | 13 | 4,349 ; 7,561 ; 11,911 |

Jamais plus de trois longueurs de trous : c'est le théorème des trois distances (partie XI), avec 53,13° à la place de l'angle d'or. Chaque trou est la différence de deux plus grands : 90 − 53,13 = 36,87 ; 53,13 − 36,87 = 16,26 ; 36,87 − 16,26 = 20,61 ; 20,61 − 16,26 = 4,35…
Théorème de Niven : si un angle est un nombre rationnel de degrés et que son cosinus et son sinus sont rationnels, c'est un multiple de 90°. Toutes les autres rotations de la grille (53,13°, 36,87°, …) sont irrationnelles en degrés.

## 2. S'inverser : demi-cercle ou disque

Aiguille de longueur 10, un bout à l'origine : l'autre bout passe par 7 points de la grille, (10, 0) → (8, 6) → (6, 8) → (0, 10) → (−6, 8) → (−8, 6) → (−10, 0).
Pas : 36,87° ; 16,26° ; 36,87° ; 36,87° ; 16,26° ; 36,87°.
Entre deux positions, le triangle balayé a l'aire |det|/2 : 60, 28, 60, 60, 28, 60 (en demi-cases) ; total 148, contre π·L²/2 = 157,08 pour le demi-disque.
Le milieu à l'origine : les bouts sont en ±w avec |w| = 5 ; 6 positions de l'aiguille, les deux bouts font le tour complet et l'aiguille balaie le disque de rayon L/2.
Sur la grille, un pas de rotation autour d'un bout fixe balaie au moins une demi-case : le triangle (0, v, w) a l'aire |det(v, w)|/2, et un déterminant entier non nul vaut au moins 1.

Points de la grille balayés, comparés à l'aire :

| L | demi-disque (un bout fixe) | πL²/2 | disque (milieu fixe) | πL²/4 | deltoïde (Kakeya) | πL²/8 |
|---:|---:|---|---:|---|---:|---|
| 4 | 29 | 25,1 | 13 | 12,6 | 11 | 6,3 |
| 8 | 107 | 100,5 | 49 | 50,3 | 31 | 25,1 |
| 16 | 415 | 402,1 | 197 | 201,1 | 109 | 100,5 |
| 32 | 1637 | 1608,5 | 797 | 804,2 | 413 | 402,1 |
| 64 | 6491 | 6434,0 | 3209 | 3217,0 | 1625 | 1608,5 |
| 128 | 25845 | 25735,9 | 12853 | 12868,0 | 6453 | 6434,0 |
| 256 | 103187 | 102943,7 | 51433 | 51471,9 | 25761 | 25735,9 |

Les trois comptes grandissent comme L² (le problème du cercle de Gauss : l'écart à l'aire est de l'ordre du périmètre, ou moins). Les rapports demi-disque : disque : deltoïde tendent vers 4 : 2 : 1.

En dimension d, points de la grille dans la boule de rayon 12, comparés à V(d)·12^d (V(d) : le volume de la boule unité, celui de la chèvre en dimension d) :

| d | points | V(d)·12^d | rapport |
|---:|---:|---|---|
| 1 | 25 | 24,0 | 1,0417 |
| 2 | 441 | 452,4 | 0,9748 |
| 3 | 7153 | 7238,2 | 0,9882 |
| 4 | 102353 | 102328,1 | 1,0002 |
| 5 | 1322921 | 1309799,1 | 1,0100 |

## 3. Les aiguilles de Fibonacci : une case entre deux voisines

La direction d'or (1, φ) n'a aucun point de la grille. Les aiguilles (F(k), F(k+1)) l'approchent :

| k | aiguille | écart vertical à la droite y = φx | (−1/φ)^k | déterminant avec la suivante | angle × longueur² |
|---:|---|---|---|---:|---|
| 1 | (1, 1) | −0,618034 | −0,618034 | +1 | 0,46365 |
| 2 | (1, 2) | +0,381966 | +0,381966 | −1 | 0,44963 |
| 3 | (2, 3) | −0,236068 | −0,236068 | +1 | 0,44757 |
| 4 | (3, 5) | +0,145898 | +0,145898 | −1 | 0,44727 |
| 5 | (5, 8) | −0,090170 | −0,090170 | +1 | 0,44722 |
| 6 | (8, 13) | +0,055728 | +0,055728 | −1 | 0,44721 |
| 7 | (13, 21) | −0,034442 | −0,034442 | +1 | 0,44721 |
| 8 | (21, 34) | +0,021286 | +0,021286 | −1 | 0,44721 |
| 9 | (34, 55) | −0,013156 | −0,013156 | +1 | 0,44721 |
| 10 | (55, 89) | +0,008131 | +0,008131 | −1 | 0,44721 |
| 11 | (89, 144) | −0,005025 | −0,005025 | +1 | 0,44721 |
| 12 | (144, 233) | +0,003106 | +0,003106 | −1 | 0,44721 |

L'écart vaut exactement (−1/φ)^k : les aiguilles passent d'un côté à l'autre de la direction d'or, chaque fois φ fois plus près. Angle × longueur² → 1/√5 = 0,44721 : la constante de Hurwitz (partie IX).
Le déterminant de deux voisines vaut ±1 (identité de Cassini) : elles enferment exactement une case, et le triangle entre elles a l'aire 1/2 sans aucun point de la grille dedans (théorème de Pick).
La suivante est la somme des deux précédentes : (F(k+2), F(k+3)) = (F(k), F(k+1)) + (F(k+1), F(k+2)).

La même somme dans le spectre (partie XIII) : le nœud miroir de F(k−2) et F(k−1) est au centre fantôme de leur somme F(k), en x/a = R/(2F(k)), à la fréquence F(k−2)/F(k).

| nœud | x/a (R = 60) | fréquence | ce qu'est la somme |
|---|---|---|---|
| 8 × 13 | 1,4286 (hors du disque) | 8/21 = 0,38095 | 21 = la suivante |
| 13 × 21 | 0,8824 | 13/34 = 0,38235 | 34 = la suivante |
| 21 × 34 | 0,5455 | 21/55 = 0,38182 | 55 = la suivante, le nombre d’anneaux de la lentille |

La chaîne s'arrête là dans la lentille à 55 anneaux : la composante 55 est nulle (partie XI), elle ne fait pas d'aiguille.

## 4. Le pavage de Farey : les directions de la grille dans le disque de Poincaré

Chaque direction de la grille est une pente p/q, un point du bord du plan hyperbolique. Deux aiguilles voisines (déterminant ±1) sont reliées par une géodésique : ce sont les arêtes du pavage de Farey, fait de triangles idéaux.
λ-longueurs de Penner avec les cercles de Ford comme horocycles, comparées au déterminant des deux aiguilles :

| pentes | λ (cercles de Ford) | déterminant |
|---|---|---|
| 1/2 et 2/3 | 1,000000 | 1 |
| 1/3 et 2/3 | 3,000000 | 3 |
| 2/5 et 3/4 | 7,000000 | 7 |
| 3/5 et 8/13 | 1,000000 | 1 |

Relation de Ptolémée λ₁₃·λ₂₄ = λ₁₂·λ₃₄ + λ₁₄·λ₂₃ sur les aires de quatre aiguilles rangées par direction (24 directions de pentes p/q, |p| ≤ 4, q ≤ 4) : vraie pour 10626 quadruplets sur 10626.

## 5. Kakeya sur une grille finie : la moitié du plan

Le plan F_q² : q × q points, l'arithmétique modulo q (q premier), q + 1 directions, q droites de q points par direction. Un ensemble de Kakeya contient une droite entière dans chaque direction.

| q | tangentes à la parabole + une verticale | ensemble de Kakeya ? | q(q+1)/2 + (q−1)/2 | minimum exact (calculé) | part du plan |
|---:|---:|---|---:|---|---|
| 3 | 7 | oui | 7 | 7 | 0,778 |
| 5 | 17 | oui | 17 | 17 | 0,680 |
| 7 | 31 | oui | 31 | 31 | 0,633 |
| 11 | 71 | oui | 71 | — | 0,587 |
| 13 | 97 | oui | 97 | — | 0,574 |
| 17 | 161 | oui | 161 | — | 0,557 |
| 19 | 199 | oui | 199 | — | 0,551 |
| 23 | 287 | oui | 287 | — | 0,543 |
| 29 | 449 | oui | 449 | — | 0,534 |
| 31 | 511 | oui | 511 | — | 0,532 |

Pourquoi la moitié : un point (x, y) est sur une tangente de pente a si a² − 4ax + 4y = 0, c'est-à-dire si x² − y est un carré modulo q. Les carrés non nuls sont exactement la moitié des nombres non nuls : chaque colonne a (q+1)/2 points couverts, d'où q(q+1)/2, plus (q−1)/2 pour la verticale.
Blokhuis et Mazzocca (2008) ont démontré que c'est le minimum pour tout q impair ; le calcul exact le confirme pour q = 3, 5 et 7.

## 6. L'arbre de Perron sur une grille

On dessine l'arbre de Perron de la partie V (2^k branches, aire exacte 2/(k+2) du triangle) sur une grille de n × n cases, et on compte les cases touchées, rapportées à celles du triangle.

| k (branches 2^k) | aire exacte 2/(k+2) | grille 16 | grille 64 | grille 256 | grille 1024 |
|---:|---|---|---|---|---|
| 1 (2) | 0,667 | 0,721 | 0,673 | 0,669 | 0,668 |
| 2 (4) | 0,500 | 0,622 | 0,539 | 0,512 | 0,503 |
| 3 (8) | 0,400 | 0,622 | 0,484 | 0,423 | 0,406 |
| 4 (16) | 0,333 | 0,634 | 0,463 | 0,373 | 0,344 |
| 5 (32) | 0,286 | 0,657 | 0,470 | 0,353 | 0,304 |
| 6 (64) | 0,250 | 0,669 | 0,491 | 0,354 | 0,282 |
| 7 (128) | 0,222 | 0,709 | 0,516 | 0,366 | 0,275 |
| 8 (256) | 0,200 | 0,727 | 0,544 | 0,386 | 0,280 |
| 9 (512) | 0,182 | 0,715 | 0,575 | 0,412 | 0,293 |
| 10 (1024) | 0,167 | 0,738 | 0,608 | 0,441 | 0,312 |
| 11 (2048) | 0,154 | 0,738 | 0,628 | 0,468 | 0,334 |
| 12 (4096) | 0,143 | 0,814 | 0,658 | 0,496 | 0,360 |
| 13 (8192) | 0,133 | 0,820 | 0,675 | 0,522 | 0,385 |
| 14 (16384) | 0,125 | 0,826 | 0,707 | 0,549 | 0,411 |

| grille n | meilleur arbre | part minimale | × log₂ n |
|---:|---|---|---|
| 16 | k = 2 (4 branches) | 0,622 | 2,49 |
| 64 | k = 4 (16 branches) | 0,463 | 2,78 |
| 256 | k = 5 (32 branches) | 0,353 | 2,83 |
| 1024 | k = 7 (128 branches) | 0,275 | 2,75 |

Au-delà du meilleur arbre, ajouter des branches fait remonter l'aire : une branche plus fine qu'une case occupe quand même une case par rangée. Le minimum ne baisse que comme 1/log n (son produit par log₂ n reste presque constant). Córdoba (1977) a montré qu'on ne peut pas faire mieux que cet ordre, et Keich (1999) qu'il est atteint.
