# Partie XXX : le centre du Venn — la moitié du disque, les diaphragmes, les grains repositionnés et les tests du hasard

Tableaux complets, recalculés par `scripts/centre_venn.py` à partir du dépôt de Chris Dzoba (https://github.com/dzoba/venn17 ; certificats et images sous licence CC BY 4.0).

## 1. Les centres

- Centre de symétrie d'ordre 17 (rotations de 2πk/17, clarté perçue OKLab) : (999,497 ; 999,499), corrélation 0,9939. Le centre de l'image est (999,5 ; 999,5) : écart 0,004 px.
- Estimations séparées, rotation par rotation : k = 1 : (999,494 ; 999,500) ; k = 2 : (999,496 ; 999,499) ; k = 4 : (999,497 ; 999,500) ; k = 8 : (999,497 ; 999,499) (dispersion ≤ 0,003 px).

| pondération de la lumière | barycentre (x ; y) | écart au centre de symétrie | direction (° , y vers le haut) |
|---|---|---:|---:|
| luminance Y (l'œil, photométrie) | (998,89 ; 999,58) | 0,61 px | −173 |
| masque de clarté OKLab (L > fond + 0,1) | (998,67 ; 1000,45) | 1,26 px | −131 |
| clarté OKLab L | (996,35 ; 1002,73) | 4,51 px | −134 |
| masque en moyenne RGB (> fond + 25), celui de la partie XXIX | (987,13 ; 1005,11) | 13,58 px | −156 |
| moyenne des canaux RGB | (967,83 ; 1009,04) | 33,07 px | −163 |
| énergie R + G + B linéaire (radiométrie) | (954,20 ; 1007,88) | 46,07 px | −170 |

- Mon premier essai (recherche grossière partie du barycentre du masque RGB) : (997,13 ; 999,61), à 2,36 px du vrai centre ; il s’est arrêté au bord de ses deux fenêtres de recherche. Avec la recherche fine, le même masque RGB donne (999,499 ; 999,502), à 0,004 px : ce n'est pas le masque qui trompait, c'est le point de départ.

- Les couleurs des 17 courbes (mesurées : les 5 % de pixels les plus clairs de chaque teinte) ont une clarté perçue de 0,60 à 0,71, une moyenne RGB de 101 à 177.
- Premier harmonique (le dipôle) des 17 poids, selon la pesée : clarté L 1,6 % ; luminance Y 4,1 % ; moyenne RGB 9,8 % ; énergie linéaire 17,7 %.
- Si les 17 courbes pesaient pareil, le barycentre serait exactement le centre de symétrie : la rotation d'ordre 17 annule tout premier harmonique. Tout écart vient donc des poids, pas de la géométrie.
- Précision du centre de symétrie : 0,003 px. L'écart du masque de la partie XXIX (13,6 px) en vaut 4 462 fois.
- Trou central, vu du centre de symétrie : rayon 14,57 px. Le plus grand disque vide centré sur un pixel est en (999 ; 999), à 0,70 px : la grille des pixels ne peut pas mieux faire.

## 2. La moitié du disque fait la moitié du Venn

- Centre de symétrie du rendu « rose » : (999,51 ; 999,50), corrélation 0,997.

| rendu | encre de l'intérieur | dans le contour réduit de 1/√2 | dans le cercle R/√2 | rayon médian ρ | ⟨ρ²⟩ |
|---|---:|---:|---:|---:|---:|
| pression, centre de symétrie, clarté | 66,8 % | 49,43 % | 50,61 % | 0,7112 | 0,5037 |
| pression, barycentre et masque de la partie XXIX | 60,8 % | 49,40 % | 51,93 % | 0,7114 | 0,5036 |
| rose, centre de symétrie, clarté | 24,5 % | 26,73 % | 29,06 % | 0,7575 | 0,5622 |

- Pour une densité uniforme, ρ² est uniforme sur [0, 1] : le contour réduit de 1/√2 contient la moitié, le rayon médian vaut 1/√2 = 0,7071 et ⟨ρ²⟩ = 1/2. Le cercle de demi-aire est aussi le cercle quadratique moyen (l'« étalement » de la partie X).
- Le centre change la moitié mesurée : 51,93 % depuis le barycentre de la partie XXIX, 50,61 % depuis le centre de symétrie (cercle R/√2).

**Les crans du diaphragme dans l'image** (part de l'encre dans le contour réduit de 2^(−j/2)) :

| cran j | rayon | f/… | part attendue 2⁻ʲ | pression | rose |
|---:|---:|---:|---:|---:|---:|
| 0 | 1,0000 | f/1 | 1,000000 | 1,000000 | 1,000000 |
| 1 | 0,7071 | f/1,4 | 0,500000 | 0,494347 | 0,267328 |
| 2 | 0,5000 | f/2 | 0,250000 | 0,243846 | 0,020460 |
| 3 | 0,3536 | f/2,8 | 0,125000 | 0,118963 | 0,000000 |
| 4 | 0,2500 | f/4 | 0,062500 | 0,061422 | 0,000000 |
| 5 | 0,1768 | f/5,6 | 0,031250 | 0,031124 | 0,000000 |
| 6 | 0,1250 | f/8 | 0,015625 | 0,014782 | 0,000000 |
| 7 | 0,0884 | f/11 | 0,007812 | 0,006830 | 0,000000 |
| 8 | 0,0625 | f/16 | 0,003906 | 0,003409 | 0,000000 |
| 9 | 0,0442 | f/22 | 0,001953 | 0,001643 | 0,000000 |
| 10 | 0,0312 | f/32 | 0,000977 | 0,000768 | 0,000000 |
| 11 | 0,0221 | f/45 | 0,000488 | 0,000295 | 0,000000 |
| 12 | 0,0156 | f/64 | 0,000244 | 0,000023 | 0,000000 |
| 13 | 0,0110 | f/90 | 0,000122 | 0,000000 | 0,000000 |
| 14 | 0,0078 | f/128 | 0,000061 | 0,000000 | 0,000000 |

**Traits par pixel d'arc**, le long de cercles (densité de lignes) :

| rayon / R | 0,02 | 0,14 | 0,26 | 0,38 | 0,50 | 0,62 | 0,74 | 0,86 | 0,98 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pression | 0,146 | 0,198 | 0,253 | 0,203 | 0,171 | 0,202 | 0,171 | 0,210 | 0,176 |
| rose | 0,000 | 0,000 | 0,000 | 0,020 | 0,044 | 0,079 | 0,113 | 0,076 | 0,006 |

- Le cercle de demi-aire en pixels (rayon 695,6 px, aire 1 519 956) : comptés par leur centre, 1 519 987 pixels (+21 ppm) ; entièrement dedans 1 517 135, qui le touchent 1 522 699 : écart 5 564 = 8r à 0,6 près (partie XVIII), soit ±1830 ppm de façon certaine.
- Au grain d'un croisement (22,56 pixels), le cercle en frôle environ 920 : ±3510 ppm. L'image ne peut pas trancher la moitié mieux que cela ; le certificat, si.

**La moitié dans les 18 certificats** (croisements de niveau ≥ (n + 1)/2) :

| certificat | n | croisements | moitié haute | écart | en orbites de n | symétrie polaire (N_l = N_(n−l)) |
|---|---:|---:|---:|---:|---:|---|
| best11-s0 | 11 | 2 046 | 968 | −26882 ppm | −5 | non (écart max 132) |
| v3-13-s0 | 13 | 8 190 | 4 069 | −3175 ppm | −2 | non (écart max 52) |
| venn17-gcp-s12 | 17 | 131 070 | 65 909 | +2853 ppm | +22 | non (écart max 1 275) |
| venn17-gcp-s14 | 17 | 131 070 | 65 042 | −3761 ppm | −29 | non (écart max 1 581) |
| venn17-gcp-s16 | 17 | 131 070 | 65 297 | −1816 ppm | −14 | non (écart max 357) |
| venn17-local-c3-s2 | 17 | 131 070 | 65 450 | −649 ppm | −5 | non (écart max 442) |
| venn19-closure-s195001 | 19 | 524 286 | 262 542 | +761 ppm | +21 | non (écart max 1 482) |
| venn19-closure-s195002 | 19 | 524 286 | 261 630 | −978 ppm | −27 | non (écart max 1 159) |
| venn19-closure-s196001 | 19 | 524 286 | 262 599 | +870 ppm | +24 | non (écart max 1 729) |
| venn19-closure-s196002 | 19 | 524 286 | 262 675 | +1015 ppm | +28 | non (écart max 1 425) |
| venn19-closure-s196004 | 19 | 524 286 | 262 637 | +942 ppm | +26 | non (écart max 1 311) |
| venn19-closure-s196007 | 19 | 524 286 | 262 637 | +942 ppm | +26 | non (écart max 1 368) |
| venn19-fresh-s190002 | 19 | 524 286 | 262 504 | +689 ppm | +19 | non (écart max 1 615) |
| venn19-fresh-s192007 | 19 | 524 286 | 262 029 | −217 ppm | −6 | non (écart max 551) |
| venn19-fresh-s192015 | 19 | 524 286 | 263 017 | +1667 ppm | +46 | non (écart max 2 223) |
| venn19-ramp12h-s192102 | 19 | 524 286 | 262 143 | +0 ppm | +0 | non (écart max 703) |
| venn19-ramp12h-s192104 | 19 | 524 286 | 262 352 | +399 ppm | +11 | non (écart max 1 197) |
| venn19-ramp12h-s192106 | 19 | 524 286 | 261 611 | −1015 ppm | −28 | non (écart max 1 406) |

- Moitié exacte : venn19-ramp12h-s192102 met 262 143 croisements de chaque côté (2¹⁸ − 1 = 19 × 13 797 : Fermat rend l'égalité possible en orbites entières).
- Les 12 Venn à 19 courbes s'écartent de la moitié de ±24,7 orbites (écart quadratique). Pour un tirage normal de cette largeur, la probabilité de tomber pile sur 0 est 1,6 %, et celle qu'au moins un des 12 y tombe, 18 %.
- Chaque certificat a exactement n croisements autour de chacun des deux pôles (∅ et tout) : vrai pour les 18. L'écart à la moitié est toujours un nombre entier d'orbites : 2^(n−1) − 1 est divisible par n (Fermat).

## 3. La sphère et les deux miroirs

- Euler sur la sphère : croisements = régions − 2 = 2ⁿ − 2 (χ = 2). La rotation fixe exactement deux régions, les pôles ∅ et tout : le nombre de Lefschetz d'une rotation de la sphère vaut χ = 2.
- Lambert (aire conservée) : un point à l'angle θ du pôle va au rayon 2 sin(θ/2), sa corde depuis le pôle. L'équateur va à la corde √2 = 1,414214, dans un disque de rayon 2 : rapport 1/√2. Archimède : la zone entre deux plans a l'aire 2πR·h.
- Miroir d'aire (le complément, en dessin à aire égale) : ρ_l² + ρ_(18−l)² = 1 pour la binomiale : exact (fractions exactes, l = 2 … 16). Pour le certificat de l'image, l'écart maximal est 2075 ppm.
- Miroir conforme (le même complément, en projection stéréographique, équateur à R/√2) : r·r′ = R²/2, de 0,500000000000 à 0,500000000000 pour la binomiale. Les deux foyers de la partie XVII sont jumeaux : (1 − 1/√2)(1 + 1/√2) = 0,500000000000.

## 4. Les diaphragmes

| cran j | rayon 2^(−j/2) | f/… | part 2⁻ʲ | niveau (certificat) | niveau (binomiale) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1,0000 | f/1 | 1,000000 | 1,000 | 1,000 |
| 1 | 0,7071 | f/1,4 | 0,500000 | 8,996 | 9,000 |
| 2 | 0,5000 | f/2 | 0,250000 | 10,308 | 10,360 |
| 3 | 0,3536 | f/2,8 | 0,125000 | 11,240 | 11,339 |
| 4 | 0,2500 | f/4 | 0,062500 | 12,004 | 12,128 |
| 5 | 0,1768 | f/5,6 | 0,031250 | 12,656 | 12,774 |
| 6 | 0,1250 | f/8 | 0,015625 | 13,237 | 13,334 |
| 7 | 0,0884 | f/11 | 0,007812 | 13,739 | 13,847 |
| 8 | 0,0625 | f/16 | 0,003906 | 14,216 | 14,287 |
| 9 | 0,0442 | f/22 | 0,001953 | 14,666 | 14,696 |
| 10 | 0,0312 | f/32 | 0,000977 | 15,081 | 15,081 |
| 11 | 0,0221 | f/45 | 0,000488 | 15,397 | 15,397 |
| 12 | 0,0156 | f/64 | 0,000244 | 15,712 | 15,712 |
| 13 | 0,0110 | f/90 | 0,000122 | 16,000 | 16,000 |

- Du bord à l'orbite centrale (17 croisements, 1/7 710 de l'aire) : log₂ 7 710 = 12,913 crans, soit un diaphragme fermé de f/1 à f/87,8.
- Une courbe de plus double les croisements : il faut ouvrir d'un cran (f/N → f/(N/√2)) pour les résoudre.

| chèvre | part des croisements broutés | niveau moyen brouté | part des niveaux ≥ 9 dans ce qu'elle broute |
|---|---:|---:|---:|
| au centre, corde R/√2 | 0,500000 | 10,109 | 0,9987 |
| point orange (partie XVII) | 0,500000 | 9,599 | 0,7376 |
| Ullisch, piquet sur le bord | 0,500000 | 8,899 | 0,5735 |

- La chèvre d'Ullisch broute 39,34 % du niveau 1 : la limite exacte est 2 × 70,81° / 360° = 0,39340 (l'arc de la partie XX, la corde de Ptolémée de la partie X : cos φ = 1 − k²/2).

**Niven : les cercles inscrit et circonscrit d'un polygone régulier, en crans** (−2·log₂ cos(π/N)) :

| N | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| crans | 2,000 | 1,000 | 0,612 | 0,415 | 0,301 | 0,228 | 0,179 | 0,145 | 0,119 | 0,100 | 0,085 | 0,073 | 0,064 | 0,056 | 0,050 | 0,044 | 0,040 | 0,036 | 0,032 | 0,030 | 0,027 | 0,025 |

- Nombre entier de crans : N = 3, 4 seulement (2 crans pour le triangle, 1 pour le carré). Niven : si cos(2π/N) est rationnel, il vaut 0, ±1/2 ou ±1.

## 5. La figure de diffraction de l'image

- 70 aigrettes entre 0,08 et 0,2 cycle par pixel : 34 dans la famille du contour (résidu 9,17° modulo 180°/17, prévu par les 17 coins), 36 dans une seconde famille (résidu 2,57°), tournée de 3,99°.
- Le contour seul (le masque du 17-gone) donne 34 aigrettes, dont 100 % dans la famille du contour. Le cœur seul (ρ < 0,6) en donne 40, dont 85 % dans la seconde famille : elle vient de l'intérieur.

| anneau de fréquences (cycle/px) | harmoniques angulaires dominantes du spectre |
|---|---|
| 0,01 – 0,03 | 34 (0,132), 68 (0,089), 60 (0,024), 4 (0,022), 48 (0,015) |
| 0,03 – 0,08 | 68 (0,240), 34 (0,132), 4 (0,015), 16 (0,005), 64 (0,004) |
| 0,08 – 0,20 | 68 (0,145), 34 (0,067), 4 (0,009), 18 (0,004), 2 (0,003) |
| 0,20 – 0,25 | 68 (0,044), 34 (0,039), 4 (0,021), 2 (0,006), 6 (0,003) |
| 0,25 – 0,45 | 4 (0,056), 68 (0,021), 34 (0,010), 2 (0,005), 6 (0,003) |

- Harmoniques angulaires de l'encre, vue du centre de symétrie : 17 (0,0264), 34 (0,0154), 51 (0,0179), 68 (0,0152) ; le plus grand des autres : 0,0022. Le spectre, lui, ne garde que les multiples de 34 (Friedel : |F(k)| = |F(−k)|).

## 6. Au plus près du centre

**Empiler les 17 copies tournées** (r de 6 à 80 px) : part de la variance que les copies ne partagent pas.

| décalage du centre d'empilement | 0 px | 0,125 px | 0,25 px | 0,5 px | 1 px | 1,5 px | 2 px | 3 px | 4 px | 8 px | 13,5758 px |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| incohérence | 2,1 % | 4,0 % | 9,0 % | 24,9 % | 50,2 % | 64,1 % | 71,5 % | 81,6 % | 88,0 % | 99,5 % | 98,9 % |

- Dans la direction perpendiculaire : 0,5 px : 24,8 % ; 1 px : 51,0 % ; 2 px : 71,3 %.
- Autour de mon premier centre (2,36 px du bon) : incohérence 76,2 %.
- Grille 4 fois plus fine (0,25 px) : 4,3 échantillons par case en moyenne (17 copies, gouttes de 0,5 px).

**Défocalisation** (disque de rayon 4 px, harmonique 17) : inversion prévue entre 9,7 et 17,7 px (zéros de J₁) ; mesurée de 16 à 21 px. Signes en accord avec 2 J₁(x)/x sur 93 % des rayons fiables au-delà du trou (76 rayons de 15 à 90 px ; on écarte ceux où l'harmonique 17 est presque nulle). Ce score est surtout le taux de base : « positif partout » fait 92 %. C'est la couronne inversée qui confirme le modèle, pas ce pourcentage (révision 001).

**Largeur d'image nécessaire** (pixels) : le reste à 2 px par côté de croisement, le centre à 2 px d'arc entre les n croisements de l'orbite centrale ; repositionner les grains divise ces largeurs par 2 au mieux.

| n | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| reste | 102 | 144 | 204 | 289 | 409 | 578 | 817 | 1 155 | 1 634 | 2 311 | 3 268 | 4 622 | 6 536 | 9 244 | 13 073 |
| centre | 96 | 141 | 208 | 305 | 446 | 652 | 950 | 1 383 | 2 009 | 2 915 | 4 225 | 6 115 | 8 843 | 12 775 | 18 438 |

- À 2 000 px : le centre résout jusqu'à n = 18,99 courbes, le reste jusqu'à 19,58 ; en repositionnant les grains, 20,85 et 21,58. À 8 000 px : 22,73 et 23,58.
- L'orbite centrale de l'image : cible 11,2 px, trou mesuré 14,6 px, soit 5,39 px d'arc entre deux croisements (le dessin élargit le centre).

## 7. Le banc d'essai des tests du hasard

- Nul brouillé de la partie XXIX : λ(d) ≈ 402·d paires attendues à la tolérance d (lu dans resultats/venn_ppm.md).

| cas | vérité | écart | p naïve (une comparaison) | Bonferroni (× 1 240) | nul brouillé (partie XXIX) | précision poussée (50 chiffres) | variation du paramètre | longueur de description |
|---|---|---:|---|---|---|---|---|---|
| E1 moitié des régions : Σ_(k ≥ 9) C(17, k) = 2¹⁶ | exact | 0 | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ |
| E2 2⁻¹⁷·10¹⁷ = 5¹⁷ | exact | 0 | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ |
| E3 la corde d'Ullisch est la corde de son arc : 2 arcsin(k/2) = arccos(1 − k²/2) | exact | 0 | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ |
| E4 disque uniforme : ⟨r²⟩ = R²/2 | exact | 0 | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ | pas le hasard ✓ |
| S1 34·tan(π/34) ≈ π (polygone → cercle) | structure | 2856 ppm | pas le hasard ✓ | hasard ✗ | hasard ✗ | — | pas le hasard ✓ | hasard ✗ |
| S2 lumière du 17-gone ≈ 1 − 2π²/(3·17²) | structure | 159 ppm | pas le hasard ✓ | pas le hasard ✓ | hasard ✗ | — | pas le hasard ✓ | pas le hasard ✓ |
| S3 croisements des niveaux ≥ 9 ≈ ½ (certificat de l'image) | structure | 1297 ppm | pas le hasard ✓ | hasard ✗ | hasard ✗ | — | pas le hasard ✓ | hasard ✗ |
| S4 encre dans le contour réduit de 1/√2 ≈ ½ (image) | structure | 11306 ppm | pas le hasard ✓ | hasard ✗ | hasard ✗ | — | pas le hasard ✓ | hasard ✗ |
| C1 (128/125) × lumière du 17-gone ≈ 1 | hasard | 845 ppm | pas le hasard ✗ | hasard ✓ | hasard ✓ | — | hasard ✓ | hasard ✓ |
| C2 part des triangles ≈ ombres égales de l'octaèdre (35,10 %) | hasard | 18886 ppm | pas le hasard ✗ | hasard ✓ | hasard ✓ | — | hasard ✓ | hasard ✓ |

| technique | justes / jugés |
|---|---:|
| p naïve (une comparaison) | 8 / 10 |
| Bonferroni (× 1 240) | 7 / 10 |
| nul brouillé (partie XXIX) | 6 / 10 |
| précision poussée (50 chiffres) | 4 / 4 |
| variation du paramètre | 10 / 10 |
| longueur de description | 7 / 10 |

**Variation du paramètre, le détail :**

- E1 : vrai pour tout n impair (3 à 39).
- E2 : vrai pour tout j (1 à 59).
- E3 : vrai pour toute corde k (19 valeurs).
- E4 : vrai pour tout R (intégrale exacte).
- S1 : écart × N² → π³/12 = 2,5839 (2,5927, 2,5839, 2,5839).
- S2 : écart × N⁴ → 2π⁴/15 = 12,988.
- S3 : 17 certificats : moyenne −87 ppm, dispersion 1637 ppm.
- S4 : tient pour le dessin à aire égale, pas pour la rose (26,7 %).
- C1 : ne vaut 1 qu'en N = 16,70, un passage par zéro sans loi.
- C2 : 11, 13, 17, 19 courbes : 36,0, 37,3, 35,8, 35,7 % ; rien ne suit 35,10 %.

- Sur 20 000 paires tirées au hasard (log-uniformes sur 4 décades), part déclarée « pas le hasard » : p naïve (une comparaison) : 5,81 % ; Bonferroni (× 1 240) : 0,00 % ; nul brouillé (partie XXIX) : 0,00 % ; longueur de description : 0,00 %.
- Un réel tombe pile sur une constante donnée, à 50 chiffres, avec une probabilité de l'ordre de 10⁻⁵⁰ ; un compte entier dispersé de ±25 orbites tombe pile sur sa moitié avec 1,6 %.

(calculs : 80 s)
