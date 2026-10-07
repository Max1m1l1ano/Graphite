# Partie XXVIII : l'hexagone rejoint l'octaèdre, le théorème de Perron développé, le Venn à 17

Tableaux complets, recalculés par `scripts/octaedre_perron_venn.py`.

## 1. L'hexagone rejoint l'octaèdre

### 1.1 Le cube [−½, ½]³ et l'octaèdre |x| + |y| + |z| ≤ 1

- Polaire du cube par la sphère de rayon √2/2 : {y : x·y ≤ ½ pour tout x du cube} = {½‖y‖₁ ≤ ½} = l'octaèdre. L'ombre du cube ‖u‖₁ (partie XXVI) est la jauge de l'octaèdre.
- Les 12 milieux d'arêtes coïncident : oui ; à distance 0,707107 = √2/2 (la sphère médiane des deux solides).
- Le long de (1, 1, 1), chaque sommet de l'octaèdre se projette sur un sommet du cube (écart 3,2·10⁻¹⁶) : les deux ombres sont le même hexagone.
- Le plan x + y + z = 0 coupe le cube et l'octaèdre selon le même hexagone (6 sommets, identiques) : ses sommets sont 6 des 12 milieux communs, à 0,707107 du centre (le cercle inscrit dans l'ombre passe par eux).

| axe | arêtes du contour (cube) | leurs milieux · axe | arêtes du contour (octaèdre) | leurs milieux · axe |
|---|---:|---|---:|---|
| ordre 3 : (1, 1, 1) | 6 | max 0,000 | 6 | max 0,000 |
| ordre 4 : (0, 0, 1) | 4 | max 0,500 | 4 | max 0,000 |

Quand les milieux des arêtes du contour sont dans le plan équatorial (produit scalaire nul), la sphère médiane touche le contour en ces points : son ombre est le cercle inscrit dans l'ombre du solide.

### 1.2 L'ombre de l'octaèdre

- Par ses faces : ¼ Σ_σ |σ·u| ; c'est max(‖u‖₁, 2‖u‖∞) à 2·10⁻¹⁶ près sur 200 000 directions ; projection directe des sommets : écart 1·10⁻¹⁵ (cube et octaèdre).
- Égale à l'ombre du cube sur une part 0,350956 des directions (grille de Fibonacci, 2·10⁶ points) ; théorie 6·arccos(1/3)/π − 2 = 0,350959.
- Moyennes sur la sphère : octaèdre 1,732050808 (√3 = 1,732050808, Cauchy : surface 4√3 / 4) ; cube 1,500000000 (3/2).

| direction | ombre du cube | ombre de l'octaèdre | forme (cube / octaèdre) |
|---|---|---|---|
| axe d'ordre 4 | 1,000000 | 2,000000 | carré d'aire 1 / losange (diamant) d'aire 2 |
| axe d'ordre 3 | 1,732051 | 1,732051 | le même hexagone |
| axe d'ordre 2 | 1,414214 | 1,414214 | rectangle 1 × √2 / losange de diagonales 2 et √2 |

- Le zonoèdre engendré par les 4 grandes diagonales [−σ/2, σ/2] a 14 sommets et 12 faces : le dodécaèdre rhombique (les losanges de la partie II). Sa fonction d'appui est l'ombre de l'octaèdre (écart 0).
- arccos(1/3) = 70,53° : l'angle des 8 triangles sphériques (côtés 60°, sommets aux axes d'ordre 2) où les deux ombres sont égales.

### 1.3 La conique inscrite (l'argument du cercle arctique)

Kenyon et Okounkov : la frontière gelée d'un pavage en losanges d'un polygone à 3d côtés est une courbe de classe d inscrite (tangente à tous les côtés) ; pour l'hexagone, une conique. Cinq tangentes fixent une conique :

| hexagone (côtés a, b, c, a, b, c) | conique tangente aux 5 premiers côtés : résidu sur le 6ᵉ | la conique |
|---|---|---|
| (1, 1, 1) | 8·10⁻¹⁷ | x² + y² = 0,750000 = r² du cercle inscrit (0,750000) |
| (2, 3, 4) | 9·10⁻¹⁶ | ellipse 0,2269x² + 0,0588xy + 0,1127y² = 1 |
| (1, 2, 5) | 4·10⁻¹⁷ | ellipse 0,6125x² + 0,3897xy + 0,1708y² = 1 |

Pour l'hexagone régulier, la conique est le cercle inscrit, c'est-à-dire l'ombre de la sphère médiane (§ 1.1) ; pour a × b × c, l'ellipse inscrite de Cohn, Larsen et Propp. Le 6ᵉ côté est tangent parce que les grandes diagonales d'un hexagone centré se coupent au centre (Brianchon).

### 1.4 La récurrence de l'octaèdre compte les deux pavages

- Diamant aztèque : AD(n) = 2^(n(n+1)/2) vérifie AD(n)·AD(n − 2) = 2·AD(n − 1)² (Dodgson) : vrai pour n ≤ 60.
- Hexagone : T(a, b, c)·T(a, b − 1, c − 1) = T(a + 1, b − 1, c − 1)·T(a − 1, b, c) + T(a, b − 1, c)·T(a, b, c − 1) (Kuo, 2004), avec la formule de MacMahon : vrai pour les 1 728 triplets a, b, c ≤ 12.
- Les six hexagones de l'identité de Kuo forment trois paires de même milieu (un seul milieu : (a, b − ½, c − ½)) : les sommets opposés d'un octaèdre, comme les six voisins de f(x, y, t) dans f(t + 1)f(t − 1) = f(x ± 1)… + f(y ± 1)….

### 1.5 Le cône de lumière de la récurrence linéarisée

- Ondes planes de h(t + 1) + h(t − 1) = ½[h(x ± 1) + h(y ± 1)] : cos ω = (cos k₁ + cos k₂)/2.
- Vitesse de groupe : |∇ω|² = ½ − (cos k₁ − cos k₂)² / (2[4 − (cos k₁ + cos k₂)²]) (écart numérique 2·10⁻¹²) ; maximum sur la grille 0,500000000000 = ½, donc |v| ≤ 1/√2.
- Source ponctuelle, t = 240 : le support exact est le losange |x| + |y| ≤ 240 (un pas par tour).

| rayon ÷ t | part de l'énergie Σh² en dedans | plus grand |h| au-delà |
|---|---|---|
| 0,60 | 0,229088 | 5,1·10⁻² |
| 0,70 | 0,708794 | 5,1·10⁻² |
| 1/√2 = 0,7071 | 0,897726 | 5,1·10⁻² |
| 0,72 | 0,999342 | 2,9·10⁻³ |
| 0,75 | 1,000000 | 7,6·10⁻⁶ |
| 0,80 | 1,000000 | 1,1·10⁻¹² |
| 0,90 | 1,000000 | 1,3·10⁻³⁴ |

- Au coin (t, 0) du losange : |h| = 5,660·10⁻⁷³ = 2^(−240) = 5,660·10⁻⁷³.
- Le losange est le cône exact, le cercle inscrit de rayon t/√2 le cône des vitesses de groupe : celui du cercle arctique des dominos (Jockusch, Propp, Shor). Le polynôme 1 − (x + 1/x + y + 1/y)z/2 + z² est un facteur du dénominateur de la fonction génératrice des probabilités de placement des dominos (Cohn, Elkies, Propp).

## 2. Le théorème de Perron, développé

### 2.1 Une fusion

| α | aire exacte (rapport au triangle) | 3α² − 4α + 2 |
|---|---|---|
| 1/2 | 3/4 | 3/4 |
| 3/5 | 17/25 | 17/25 |
| 2/3 | 2/3 | 2/3 |
| 3/4 | 11/16 | 11/16 |
| 4/5 | 18/25 | 18/25 |
| 19/20 | 363/400 | 363/400 |

Toutes égales : oui. Le minimum est 2/3, en α = 2/3 : un cœur α² = 4/9 et deux oreilles (1 − α)² = 1/9.

### 2.2 La borne cœur + oreilles, pour tous les rapports

- 80 arbres au hasard (k = 1 à 5, rapports α = m/64 entre ½ et 1), aires exactes en fractions : max(aire − F) = 0 ; égalité dans 30 cas, dont les 22 arbres à une seule fusion.
- Rapports télescopiques (k + 1)/(k + 2), …, 3/4, 2/3 : aire exacte = F = 2/(k + 2) : k = 1 : 2/3, k = 2 : 1/2, k = 3 : 2/5, k = 4 : 1/3, k = 5 : 2/7.

### 2.3 Le plateau, en entiers

Aux rapports télescopiques, en unités v = u(k + 2) et largeur × N(k + 2), la coupe est l'union des 2^k intervalles [c_i, c_i + v], c_i = Σ_j b_j(i)·2^j·(v − j − 2). Le lemme : sa longueur vaut 2^k·v, puis 2^k (plateau), puis 2^k·(v − k). Vérification exacte (en entiers) sur la grille v = p/48 :

| k | branches | points de la grille | écarts au lemme |
|---:|---:|---:|---:|
| 1 | 2 | 145 | 0 |
| 2 | 4 | 193 | 0 |
| 3 | 8 | 241 | 0 |
| 4 | 16 | 289 | 0 |
| 6 | 64 | 385 | 0 |
| 8 | 256 | 481 | 0 |
| 10 | 1 024 | 577 | 0 |
| 12 | 4 096 | 673 | 0 |
| 14 | 16 384 | 769 | 0 |
| 16 | 65 536 | 865 | 0 |

Les fentes (k = 4) : à la profondeur v entre j et j + 1, combien de morceaux, de quelle largeur, et quels bits hauts (b_j … b_(k−1)) chacun porte :

| v | morceaux | largeurs | bits hauts, de gauche à droite |
|---|---:|---|---|
| 0,5 | 16 | 0,5 | 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 |
| 1,5 | 8 | 2 | 7, 6, 5, 4, 3, 2, 1, 0 |
| 2,5 | 4 | 4 | 3, 2, 1, 0 |
| 3,5 | 2 | 8 | 1, 0 |
| 4,5 | 1 | 16 | 0 |
| 5,5 | 1 | 24 | 0 |

Chaque combinaison des bits hauts apparaît une fois et une seule, dans l'ordre binaire décroissant : chaque coupe est un diagramme de Venn à une dimension.

### 2.4 Kakeya au grain δ : la fenêtre démontrée

Avec N éventails d'ouverture π/N (hauteur 1, aire tan(π/2N) chacun), des arbres télescopiques à 2^k branches et un tube 1 × δ par direction (Partie XXVI) : aire ≤ N·[tan(π/2N)·2/(k + 2) + 2^k·δ/cos(π/2N)]. En bas, la borne de Córdoba π/(1 + 2γ + 2 ln(2/δ)).

| grain δ | borne du bas (Córdoba) | haut, 3 éventails (hexagone) | haut, 17 éventails | meilleur N | haut ÷ bas | partie XXVI (calculé) |
|---|---|---|---|---|---|---|
| 10⁻¹ | 0,38567 | 1,84752 (k = 1) | 3,28256 (k = 0) | 1,84752 (N = 3, k = 1) | 4,790 | 1,179 |
| 10⁻² | 0,24638 | 0,96995 (k = 3) | 1,39164 (k = 1) | 0,96995 (N = 3, k = 3) | 3,937 | 0,643 |
| 10⁻³ | 0,18101 | 0,60572 (k = 5) | 0,76670 (k = 3) | 0,60572 (N = 3, k = 5) | 3,346 | 0,430 |
| 10⁻⁴ | 0,14305 | 0,42924 (k = 7) | 0,50309 (k = 6) | 0,42361 (N = 4, k = 7) | 2,961 | 0,318 |
| 10⁻⁵ | 0,11825 | 0,32415 (k = 10) | 0,35876 (k = 8) | 0,32048 (N = 4, k = 10) | 2,710 | 0,250 |
| 10⁻¹⁰ | 0,06335 | 0,13905 (k = 24) | 0,13843 (k = 22) | 0,13379 (N = 5, k = 24) | 2,112 | — |
| 10⁻²⁰ | 0,03285 | 0,06202 (k = 55) | 0,05882 (k = 53) | 0,05830 (N = 8, k = 54) | 1,775 | — |
| 10⁻⁴⁹ | 0,01371 | 0,02319 (k = 149) | 0,02144 (k = 146) | 0,02142 (N = 13, k = 147) | 1,563 | — |
| 10⁻⁵⁰ | 0,01344 | 0,02269 (k = 152) | 0,02097 (k = 150) | 0,02096 (N = 13, k = 150) | 1,560 | — |
| 10⁻⁵¹ | 0,01318 | 0,02222 (k = 155) | 0,02052 (k = 153) | 0,02051 (N = 14, k = 153) | 1,557 | — |
| 10⁻⁵² | 0,01293 | 0,02177 (k = 159) | 0,02010 (k = 156) | 0,02009 (N = 12, k = 157) | 1,554 | — |
| 10⁻⁵³ | 0,01269 | 0,02133 (k = 162) | 0,01969 (k = 159) | 0,01968 (N = 13, k = 160) | 1,551 | — |
| 10⁻⁵⁴ | 0,01246 | 0,02091 (k = 165) | 0,01929 (k = 163) | 0,01928 (N = 14, k = 163) | 1,548 | — |
| 10⁻⁵⁵ | 0,01223 | 0,02051 (k = 168) | 0,01891 (k = 166) | 0,01891 (N = 15, k = 166) | 1,546 | — |
| 10⁻¹⁰⁰ | 0,00677 | 0,01094 (k = 316) | 0,01003 (k = 314) | 0,01003 (N = 21, k = 313) | 1,481 | — |

- Constantes (aire × ln(1/δ) quand δ → 0) : en bas π/2 = 1,5708 ; en haut π·ln 2 = 2,1776 avec assez d'éventails, 2√3·ln 2 = 2,4011 avec 3. Rapport limite 2 ln 2 = 1,3863.
- Le coefficient 2N·tan(π/2N) est l'aire du polygone régulier à 2N côtés circonscrit au cercle unité :

| N éventails | polygone circonscrit | 2N·tan(π/2N) | écart à π | π²/(12N²) |
|---:|---|---|---|---|
| 2 | carré | 4,000000 | 27,3240 % | 20,5617 % |
| 3 | hexagone | 3,464102 | 10,2658 % | 9,1385 % |
| 4 | octogone | 3,313708 | 5,4786 % | 5,1404 % |
| 6 | dodécagone | 3,215390 | 2,3491 % | 2,2846 % |
| 12 | 24 côtés | 3,159660 | 0,5751 % | 0,5712 % |
| 17 | 34 côtés | 3,150564 | 0,2856 % | 0,2846 % |
| 100 | 200 côtés | 3,141851 | 0,0082 % | 0,0082 % |

## 3. Le Venn à 17

### 3.1 Henderson : n doit être premier

- n divise C(n, k) pour tout 0 < k < n ⟺ n premier : vrai pour n ≤ 200.
- 2¹⁷ − 2 = 131 070 = 17 × 7 710 (Fermat) ; régions dans exactement k ensembles, par orbites de 17 :

| k | C(17, k) | orbites |
|---:|---:|---:|
| 1 | 17 | 1 |
| 2 | 136 | 8 |
| 3 | 680 | 40 |
| 4 | 2 380 | 140 |
| 5 | 6 188 | 364 |
| 6 | 12 376 | 728 |
| 7 | 19 448 | 1 144 |
| 8 | 24 310 | 1 430 |
| 9 | 24 310 | 1 430 |
| 10 | 19 448 | 1 144 |
| 11 | 12 376 | 728 |
| 12 | 6 188 | 364 |
| 13 | 2 380 | 140 |
| 14 | 680 | 40 |
| 15 | 136 | 8 |
| 16 | 17 | 1 |

- Total : 7 710 orbites ; colliers binaires de 17 perles : 7 712.
- Venn simple à n courbes (Euler, V − E + F = 2 avec E = 2V et F = 2ⁿ) : V = 2ⁿ − 2 croisements. Pour 17 : 131 070 croisements = 17 × 7 710, 262 140 arcs, 15 420 croisements sur chaque courbe.

### 3.2 Un Venn symétrique à 5 ellipses, vérifié

- Ellipses de demi-axes 1,06 et 0,5, centres à 0,36 du centre, inclinées de 2,95 rad, tournées de 72° : 32 régions sur 32, chacune d'un seul morceau : oui (grille 900 × 900).
- Croisements : 30 = 2⁵ − 2, en 6 orbites de 5 (4 par paire de voisines, 2 par paire éloignée). Le contour est connexe, donc Euler donne 2·30 − 30 + 2 = 32 faces : avec les 32 codes présents, chaque combinaison est une seule région (le Venn est simple).
- Régions hors centre et dehors : 30 = 5 × 6 (C(5, k)/5 = 1, 2, 2, 1).

### 3.3 Le diaphragme à 17 lames

- Lumière : (N/2π)·sin(2π/N) = 0,977388 du cercle (partie II) ; il manque 2,261 % (2π²/(3N²) = 2,277 %, les ménisques de la partie V), soit 0,0330 cran.
- Contrôle de la transformée exacte : F(0) = 3,070554, aire du 17-gone 3,070554.

| lames N | aigrettes comptées | attendu (N pair : N ; impair : 2N) |
|---:|---:|---:|
| 5 | 10 | 10 |
| 6 | 6 | 6 |
| 7 | 14 | 14 |
| 8 | 8 | 8 |
| 16 | 16 | 16 |
| 17 | 34 | 34 |
| 18 | 18 | 18 |

- Les 34 aigrettes du 17-gone sont espacées de 10,580° à 10,590° (180/17 = 10,588°).
- Même parité pour le diaphragme de Perron : N éventails posés comme N lames (angles 2πj/N) couvrent chaque direction modulo π une fois si N est impair ; pour N pair, la moitié des directions deux fois et l'autre jamais.
  - N = 16 : 8 directions distinctes sur 16.
  - N = 17 : 17 directions distinctes sur 17.

### 3.4 Gauss, i et la période de 1/17

- cos(2π/17) = 0,932472229404356 ; formule de Gauss : 0,932472229404356.
- Ordres modulo 17 : 2 → 8, 3 → 16 (racine primitive), 4 → 4, 10 → 16.
- 4² = 16 ≡ −1 : 4 ≡ i (mod 17), car 17 = 4² + 1 (comme 101 = 10² + 1 à la partie XIX) ; 2⁴ ≡ −1 ; 10⁴ ≡ 4 ≡ i ; 10⁸ ≡ −1 (mod 17).
- 1/17 = 0,(0588235294117647) : période 16 ; 05882352 + 94117647 = 99999999 (Midy, car 10⁸ ≡ −1) ; par quarts : 0588 + 2352 + 9411 + 7647 = 19 998 = 2 × 9 999.
- Périodes de Gauss (racine primitive 3) : on coupe les 16 racines en 2, 4, 8 classes ; chaque étape est une racine carrée.
  - 2 classes de 8 : 1,561553, −2,561553
  - 4 classes de 4 : 2,049481, 0,344151, −0,487928, −2,905704
  - 8 classes de 2 : 1,864944, 0,891477, −1,965946, −1,700434, 0,184537, −0,547326, 1,478018, −1,205269
  - niveau 2 : (−1 ± √17)/2 = 1,561553, −2,561553.

(calculs : 20 s)
