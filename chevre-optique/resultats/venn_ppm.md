# Partie XXIX : le Venn à 17 au ppm — l'image retrouvée, l'analyse dimensionnelle et deux ombres du même cube

Tableaux complets, recalculés par `scripts/venn_ppm.py` à partir du dépôt de Chris Dzoba (https://github.com/dzoba/venn17 ; certificats et images sous licence CC BY 4.0).

## 1. L'image retrouvée : le rendu « pressure » du dépôt

- Image de 2000 × 2000 pixels ; le contour a pour harmoniques principales [17, 34, 51, 68] : le 17-gone et ses multiples. Rayon extérieur ≈ 984 px, aire intérieure 2 956 870 px.
- Trou central : disque vide de rayon 14,4 px, soit 0,0147 du rayon et 221 ppm de l'aire.
- Encre (pixels plus clairs que le fond) : 60,8 % de l'intérieur.
  - par anneau : 0,0–0,20 : 61 % ; 0,2–0,40 : 56 % ; 0,4–0,60 : 62 % ; 0,6–0,80 : 60 % ; 0,8–0,95 : 63 % (densité uniforme, comme annoncé).

## 2. Les comptes au ppm, lus dans les certificats

| certificat | n | croisements | régions | coins (min–max, hors centre et dehors) | centre et dehors | rangs k, k+1, k+1, k+2 |
|---|---:|---:|---:|---|---|---|
| best11-s0.json | 11 | 2 046 | 2 048 | 3 – 8 | 11 et 11 coins | partout |
| v3-13-s0.json | 13 | 8 190 | 8 192 | 3 – 8 | 13 et 13 coins | partout |
| venn17-local-c3-s2.json | 17 | 131 070 | 131 072 | 3 – 11 | 17 et 17 coins | partout |
| venn17-gcp-s12.json | 17 | 131 070 | 131 072 | 3 – 13 | 17 et 17 coins | partout |
| venn17-gcp-s14.json | 17 | 131 070 | 131 072 | 3 – 12 | 17 et 17 coins | partout |
| venn17-gcp-s16.json | 17 | 131 070 | 131 072 | 3 – 12 | 17 et 17 coins | partout |
| venn19-closure-s196002.json | 19 | 524 286 | 524 288 | 3 – 16 | 19 et 19 coins | partout |

- Un croisement de l'image pèse 1/131 070 de l'aire = 7,6295 ppm, soit 22,56 pixels.
- Une région moyenne pèse 2⁻¹⁷ = 0,00000762939453125 = 7,62939453125 ppm : les chiffres de 5¹⁷ = 762939453125 (partie XXVI).
- Coins par région : en moyenne 4·(2ⁿ − 2)/2ⁿ = 3,99993896 (n = 17).

**La texture : la part des régions à 3, 4, 5, 6, 7 coins et plus.**

| certificat | 3 coins | 4 | 5 | 6 | 7 et plus |
|---|---|---|---|---|---|
| best11-s0.json | 36,0 % | 36,6 % | 21,5 % | 4,8 % | 1,1 % |
| v3-13-s0.json | 37,3 % | 37,3 % | 16,5 % | 6,8 % | 2,1 % |
| venn17-local-c3-s2.json | 35,8 % | 37,6 % | 19,5 % | 5,7 % | 1,4 % |
| venn17-gcp-s12.json | 36,0 % | 38,0 % | 18,4 % | 5,8 % | 1,8 % |
| venn17-gcp-s14.json | 35,3 % | 38,9 % | 18,5 % | 5,7 % | 1,5 % |
| venn17-gcp-s16.json | 36,7 % | 36,7 % | 18,9 % | 5,9 % | 1,7 % |
| venn19-closure-s196002.json | 35,7 % | 38,0 % | 18,8 % | 6,0 % | 1,5 % |

**Les niveaux.** Le niveau d'un croisement est le rang moyen de ses quatre régions. Le dessin donne à chaque niveau un anneau d'aire proportionnelle à son nombre de croisements.

| niveau l | croisements (c3-s2) | C(17, l) | rapport | rayon cible √(part des niveaux ≥ l) |
|---:|---:|---:|---|---|
| 1 | 17 | 17 | 1,000 | 1,0000 |
| 2 | 136 | 136 | 1,000 | 0,9999 |
| 3 | 561 | 680 | 0,825 | 0,9994 |
| 4 | 2 159 | 2 380 | 0,907 | 0,9973 |
| 5 | 5 491 | 6 188 | 0,887 | 0,9890 |
| 6 | 12 019 | 12 376 | 0,971 | 0,9676 |
| 7 | 19 822 | 19 448 | 1,019 | 0,9190 |
| 8 | 25 415 | 24 310 | 1,045 | 0,8326 |
| 9 | 24 973 | 24 310 | 1,027 | 0,7066 |
| 10 | 20 111 | 19 448 | 1,034 | 0,5557 |
| 11 | 12 138 | 12 376 | 0,981 | 0,3942 |
| 12 | 5 389 | 6 188 | 0,871 | 0,2506 |
| 13 | 2 125 | 2 380 | 0,893 | 0,1472 |
| 14 | 561 | 680 | 0,825 | 0,0738 |
| 15 | 136 | 136 | 1,000 | 0,0342 |
| 16 | 17 | 17 | 1,000 | 0,0114 |

- Σ_l C(17, l) = 2¹⁷ − 2 = 131 070 : en moyenne, un croisement par région de même rang. Les niveaux 1, 2, 15 et 16 tombent exactement sur C(17, l).
- Part des croisements de niveau ≥ 9 (donc dans le disque de rayon R/√2 si le dessin suivait exactement sa cible) : venn17-local-c3-s2 : 0,49935 (−649 ppm) ; venn17-gcp-s12 : 0,50285 (+2853 ppm) ; venn17-gcp-s14 : 0,49624 (−3761 ppm) ; venn17-gcp-s16 : 0,49818 (−1816 ppm).
- Les 17 croisements du niveau 16 entourent la région centrale, au rayon cible √(17/131 070) = 0,0114 R, soit 11,2 px ; le trou mesuré fait 14,4 px (le dessin relâche un peu sa cible).

## 3. La granularité

| grain (pixels) | grain (ppm de l'aire) | dessin rempli à |
|---:|---:|---|
| 1 | 0,34 | 60,3 % |
| 2 | 1,35 | 91,7 % |
| 3 | 3,04 | 99,2 % |
| 4 | 5,41 | 99,9 % |
| 5 | 8,45 | 100,0 % |
| 6 | 12,18 | 100,0 % |
| 8 | 21,64 | 100,0 % |
| 12 | 48,70 | 100,0 % |

- Le dessin est plein dès un grain de 4 à 5 pixels, la taille d'une région (4,75 px de côté en moyenne) : au-dessus de 7,6 ppm d'aire, il est de dimension 2 ; en dessous, ce sont des lignes.
- Les veines (les pixels les plus clairs, après un lissage de 3 px) ont pour dimension de comptage de boîtes, entre 3 et 32 px : les 10 % les plus clairs : 1,31 ; les 3 % les plus clairs : 1,14 ; les 1 % les plus clairs : 0,97. Des lignes, pas des surfaces.

**Pixels par croisement**, pour un dessin de même type (aire intérieure ∝ largeur²) :

| courbes n | croisements 2ⁿ − 2 | à 2 000 px | à 8 000 px |
|---:|---:|---|---|
| 5 | 30 | 98 562 | 1 576 997 |
| 7 | 126 | 23 467 | 375 476 |
| 11 | 2 046 | 1 445 | 23 123 |
| 13 | 8 190 | 361 | 5 777 |
| 17 | 131 070 | 22,56 | 361 |
| 19 | 524 286 | 5,64 | 90,24 |
| 23 | 8 388 606 | 0,35 | 5,64 |

- Chaque courbe de plus double le nombre de croisements : pour garder le même grain, il faut multiplier la largeur de l'image par √2. Une courbe = un cran de diaphragme (partie I).

## 4. L'analyse dimensionnelle : ce que coûte 1 ppm

| objet | rythme | pour 1 ppm |
|---|---|---|
| Venn : 2ⁿ régions, grain en aire | 1 bit par courbe | 20 courbes (19,93 en continu) |
| Venn : grain en longueur | ½ bit par courbe | 40 courbes (39,86 en continu) |
| Perron : branches de largeur 2⁻ᵏ | 1 bit par étage | 20 étages (19,93 en continu) |
| la série de la chèvre (partie XXV) : 1,03·2^(−n/2)/n | ½ bit par dimension | 31 dimensions |
| le ménisque de la chèvre : 2/(3n²) | n ∝ ε^(−1/2) | 817 dimensions (816,50 en continu) |
| le diaphragme à N lames : 2π²/(3N²) | n ∝ ε^(−1/2) | 2 566 lames (2565,10 en continu) |
| le plan de la lentille : x₀ ≈ 1/n | n ∝ ε⁻¹ | 1 000 000 dimensions |
| l'équateur (partie I) | n ∝ ε⁻² | 1·10¹² dimensions |
| Kakeya au grain δ = 1 ppm (parties XXVI et XXVIII) | 1/aire : + 0,441 par bit | aire entre 0,1008 et 0,2536 |

- 2²⁰ = 1 048 576 : le « méga » binaire. 10⁶/2²⁰ = 0,95367431640625 a les chiffres de 5²⁰ (partie XXVI) : un ppm décimal vaut 0,954 « ppm binaire ».
- Le Venn et Perron sont sur la même marche : un bit par pas. La série de la chèvre gagne un demi-bit par dimension (le facteur √2, un cran) : elle va au même rythme que le Venn mesuré en longueur, 2·log₂ 10 = 6,644 par décade.

## 5. Deux ombres du même cube

### 5.1 Henderson, vu comme une ombre

L'ombre symétrique du cube {0, 1}ⁿ dans le plan envoie l'ensemble S sur Σ_{i∈S} ω^i (ω = e^(2iπ/n)). La rotation des étiquettes devient la rotation de 2π/n. Le centre ne reçoit que ∅ et tout, sauf si n est composé :

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sous-ensembles propres de somme nulle | 0 | 0 | 2 | 0 | 8 | 0 | 14 | 6 | 32 | 0 | 98 | 0 | 128 | 36 | 254 | 0 | 998 | 0 | 1 154 |

- Zéro exactement pour les n premiers : vrai (n ≤ 20).
- L'ombre du cube de dimension 17 a pour contour un polygone régulier à 34 côtés (rayons 5,418976 à 5,418976) : le 34-gone des aigrettes et des éventails (partie XXVIII), comme l'hexagone est l'ombre du cube de dimension 3.
- Les sommets de rang k sont en moyenne à |S|² = k(n − k)/(n − 1) : k = 1 : 1,0000 (1,0000) ; k = 4 : 3,2500 (3,2500) ; k = 8 : 4,5000 (4,5000) ; k = 9 : 4,5000 (4,5000) ; k = 13 : 3,2500 (3,2500) ; k = 16 : 1,0000 (1,0000).

### 5.2 Perron et le Venn

- Perron (partie XXVIII) : à la profondeur v, la coupe est l'ombre du cube {0, 1}ᵏ sur la direction (a₀, …, a_(k−1)) ; les 2ᵏ sommets y restent séparés, rangés dans l'ordre binaire, et fusionnent par moitiés : 2^(k−j) fentes au niveau j.
- Le dessin du Venn : le rayon suit le niveau, c'est-à-dire l'ombre du cube {0, 1}¹⁷ sur sa grande diagonale (le nombre de 1) ; il y a environ C(17, l) croisements au niveau l, exactement aux deux bouts.
- Comptes par niveau : Perron, 2^(k − j) (une suite géométrique) ; Venn, C(17, l) (une binomiale). Au niveau 8, la binomiale donne 24 310 et le certificat 25 415.

## 6. Gelé et liquide : les régions non monotones

Une région de rang k est monotone si elle touche une région de rang k − 1 et une de rang k + 1 (Bultena, Grünbaum, Ruskey). Sinon, c'est un creux ou un sommet de la « hauteur » (le rang).

| certificat | non monotones | creux | sommets | rangs gelés (aucune non monotone) |
|---|---:|---:|---:|---|
| best11-s0.json | 319 (15,6 %) | 165 | 154 | 0, 1, 10, 11 |
| v3-13-s0.json | 1 222 (14,9 %) | 624 | 598 | 0, 1, 12, 13 |
| venn17-local-c3-s2.json | 15 742 (12,0 %) | 7 888 | 7 854 | 0, 1, 2, 15, 16, 17 |
| venn17-gcp-s12.json | 16 592 (12,7 %) | 8 262 | 8 330 | 0, 1, 2, 15, 16, 17 |
| venn17-gcp-s14.json | 15 249 (11,6 %) | 7 497 | 7 752 | 0, 1, 2, 15, 16, 17 |
| venn17-gcp-s16.json | 15 708 (12,0 %) | 7 905 | 7 803 | 0, 1, 2, 15, 16, 17 |
| venn19-closure-s196002.json | 68 210 (13,0 %) | 34 010 | 34 200 | 0, 1, 2, 17, 18, 19 |

- Rangs gelés : les trois du bord (0, 1, 2) et les trois du centre (15, 16, 17) pour les Venn à 17 courbes ; ils ne pèsent que 0,23 % des régions.
- La couche gelée garde la même épaisseur (2 à 3 rangs) de 11 à 19 courbes : sa part relative diminue avec n.

## 7. Le test des coïncidences au ppm

- 31 constantes de nos objets, 20 nombres du Venn à 17 ; on compare chaque paire directement (b ≈ a) et en inverse (a·b ≈ 1) : 1 240 comparaisons. Pour le hasard, on brouille les nombres du Venn (chacun multiplié par un facteur aléatoire autour de 1, à ±20 %) : ils gardent leur répartition, mais perdent toute relation exacte.

| tolérance | coïncidences observées | attendues par hasard (catalogue brouillé de ±20 %, 4 000 tirages) |
|---|---:|---|
| 10 % (100 000 ppm) | 37 | 41,057 |
| 3 % (30 000 ppm) | 12 | 12,283 |
| 1 % (10 000 ppm) | 6 | 4,083 |
| 0,3 % (3 000 ppm) | 4 | 1,206 |
| 0,1 % (1 000 ppm) | 1 | 0,407 |
| 0,01 % (100 ppm) | 0 | 0,038 |
| 0,001 % (10 ppm) | 0 | 0,004 |
| 0,0001 % (1 ppm) | 0 | moins de 0,0003 |

Les plus proches :

| écart | nos objets | le Venn à 17 | relation |
|---|---|---|---|
| 845 ppm | 128/125 (diesis) | lumière du 17-gone | a·b ≈ 1 |
| 1298 ppm | 1/2 | part des niveaux ≥ 9 | b ≈ a |
| 2852 ppm | π | 34·tan(π/34) | b ≈ a |
| 2981 ppm | 10⁶/2²⁰ | N₈/C(17, 8) | a·b ≈ 1 |
| 3191 ppm | 128/125 (diesis) | N₉/C(17, 9) | b ≈ a |
| 4852 ppm | √7 | part des quadrilatères | a·b ≈ 1 |
| 18710 ppm | 35,10 % (ombres égales) | part des triangles | b ≈ a |
| 20526 ppm | 10⁶/2²⁰ | N₉/C(17, 9) | a·b ≈ 1 |
| 20735 ppm | 128/125 (diesis) | N₈/C(17, 8) | b ≈ a |
| 22483 ppm | 10⁶/2²⁰ | cos(2π/17) | b ≈ a |

(calculs : 34 s)
