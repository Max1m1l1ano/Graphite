# Résultats de la partie XVII (générés par scripts/recursion_argent.py)

## 1. Le petit disque (rayon 1/√2) qui glisse : les positions exactes

| position | d (exact) | d | ce qui se passe | part du pré couverte |
|---|---|---|---|---|
| au centre | 0 | 0,000000 | concentrique : couronne d'épaisseur 1 − 1/√2 | 0,500000 |
| contact intérieur (point orange) | 1 − 1/√2 = (√2 − 1)/√2 | 0,292893 | touche le pré en P de l'intérieur | 0,500000 |
| jumeau de 30°, côté intérieur | (√3 − 1)/2 | 0,366025 | coupe le pré à ±30° | 0,483412 |
| jumeau de lui-même | 1/√2 | 0,707107 | passe par O, coupe le pré à ±45° (lunule d'Hippocrate) | 0,340845 |
| jumeau de 30°, côté extérieur | (√3 + 1)/2 | 1,366025 | coupe le pré à ±30° | 0,074257 |
| au piquet | 1 | 1,000000 | centré sur P | 0,211998 |
| contact extérieur | 1 + 1/√2 = (√2 + 1)/√2 | 1,707107 | touche le pré en P de l'extérieur | 0,000000 |

Translation entre les deux contacts : (1 + 1/√2) − (1 − 1/√2) = √2 = 1,414214, le diamètre du petit disque. Produit des deux contacts : (1 − 1/√2)(1 + 1/√2) = 1/2. Rapport : (√2 + 1)² = 3 + 2√2 = 5,828427.

Aux deux contacts, le petit disque atteint l'axe en 1 − √2 = −0,414214 et en 1 + √2 = 2,414214 : les deux disques de contact sont inscrits dans le cercle de centre P et de rayon √2 (la corde de dimension infinie).

Position jumelle d'elle-même (d = 1/√2) : aire commune 1,070796326795 = π/2 − 1/2 = 1,070796326795. La part perdue, hors du pré, vaut exactement 1/2 : c'est la lunule d'Hippocrate, égale au triangle O-X₊-X₋ (base √2, hauteur 1/√2).

## 2. Les jumeaux : deux positions, les mêmes points de croisement

Le petit cercle coupe le pré aux angles ±θ avec cos θ = (d² + 1/2)/(2d). Pour un même θ < 45°, deux positions d₁, d₂ conviennent : d₁ + d₂ = 2 cos θ et d₁·d₂ = 1/2. C'est la forme de Newton de l'équation des lentilles, x·x' = f², avec f = 1/√2.

| θ | d₁ | d₂ | d₁·d₂ | part couverte en d₁ | en d₂ |
|---:|---|---|---|---|---|
| 0° | 0,292893 | 1,707107 | 0,500000 | 0,500000 | 0,000000 |
| 5° | 0,294480 | 1,697910 | 0,500000 | 0,499941 | 0,000340 |
| 15° | 0,307889 | 1,623963 | 0,500000 | 0,498327 | 0,009185 |
| 30° | 0,366025 | 1,366025 | 0,500000 | 0,483412 | 0,074257 |
| 40° | 0,471385 | 1,060704 | 0,500000 | 0,444183 | 0,186788 |
| 45° | 0,707107 | 0,707107 | 0,500000 | 0,340845 | 0,340845 |

Le petit disque ne coupe jamais le pré au-delà de ±45° : à d = 1/√2, la corde commune est son diamètre.

## 3. La récursion d'argent T(d) = 2 − 1/(2d)

T = (reflet par le piquet P : d ↦ 2 − d) ∘ (jumeau : d ↦ 1/(2d)).
- point fixe d = 1 - sqrt(2)/2 = 0,292893 ; multiplicateur T'(d) = 2*sqrt(2) + 3 = 5,828427
- point fixe d = sqrt(2)/2 + 1 = 1,707107 ; multiplicateur T'(d) = 3 - 2*sqrt(2) = 0,171573

Les deux points fixes sont exactement les deux contacts : (√2 + 1)² en 1 − 1/√2 (repousse), (√2 − 1)² en 1 + 1/√2 (attire).

**L'aller-retour depuis le centre** (reflet R, puis jumeau I, puis R, …), en fractions exactes :

| étape | position | valeur | côté | écart au contact le plus proche |
|---:|---|---|---|---|
| 0 | 0 | 0,0000000000 | dans le pré (moitié exacte) | 2,929e−01 |
| 1 | 2 | 2,0000000000 | hors du pré (rien) | 2,929e−01 |
| 2 | 1/4 | 0,2500000000 | dans le pré (moitié exacte) | 4,289e−02 |
| 3 | 7/4 | 1,7500000000 | hors du pré (rien) | 4,289e−02 |
| 4 | 2/7 | 0,2857142857 | dans le pré (moitié exacte) | 7,179e−03 |
| 5 | 12/7 | 1,7142857143 | hors du pré (rien) | 7,179e−03 |
| 6 | 7/24 | 0,2916666667 | dans le pré (moitié exacte) | 1,227e−03 |
| 7 | 41/24 | 1,7083333333 | hors du pré (rien) | 1,227e−03 |
| 8 | 12/41 | 0,2926829268 | dans le pré (moitié exacte) | 2,103e−04 |
| 9 | 70/41 | 1,7073170732 | hors du pré (rien) | 2,103e−04 |
| 10 | 41/140 | 0,2928571429 | dans le pré (moitié exacte) | 3,608e−05 |
| 11 | 239/140 | 1,7071428571 | hors du pré (rien) | 3,608e−05 |
| 12 | 70/239 | 0,2928870293 | dans le pré (moitié exacte) | 6,190e−06 |
| 13 | 408/239 | 1,7071129707 | hors du pré (rien) | 6,190e−06 |
| 14 | 239/816 | 0,2928921569 | dans le pré (moitié exacte) | 1,062e−06 |

Écarts successifs côté intérieur, rapport d'une étape à l'autre : 0,146447 ; 0,167368 ; 0,170854 ; 0,171450 ; 0,171552 ; 0,171569 ; 0,171572 ; 0,171573 ; 0,171573 ; 0,171573 → 3 − 2√2 = 0,171573. Chaque aller-retour gagne log₁₀(3 + 2√2) = 0,7656 chiffre.

Nombres de Pell : 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378 ; compagnons : 1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363. Les fractions de l'orbite intérieure sont H/(2P) et P/H : 1/4, 2/7, 7/24, 12/41, 41/140, 70/239, 239/816, 408/1393.
Vérification (8 premiers termes) : oui.

Forme close : avec w = (d − (1 − 1/√2))/(d − (1 + 1/√2)), chaque pas de T⁻¹ multiplie w par 3 − 2√2. Depuis d = 0 : w₀ = 3 - 2*sqrt(2), donc la k-ième position est connue exactement sans calculer les précédentes.

**Dans la zone de croisement**, depuis le jumeau de lui-même d = 1/√2 :

| k | Tᵏ(1/√2) | T⁻ᵏ(1/√2) | produit | angle de croisement | rapport à l'angle précédent |
|---:|---|---|---|---|---|
| 0 | 0,707107 | 0,707107 | 0,500000 | 45,0000° | — |
| 1 | 1,292893 | 0,386730 | 0,500000 | 32,8798° | 0,73066 |
| 2 | 1,613270 | 0,309929 | 0,500000 | 15,9295° | 0,48448 |
| 3 | 1,690071 | 0,295846 | 0,500000 | 6,8036° | 0,42710 |
| 4 | 1,704154 | 0,293401 | 0,500000 | 2,8334° | 0,41645 |
| 5 | 1,706599 | 0,292980 | 0,500000 | 1,1747° | 0,41460 |
| 6 | 1,707020 | 0,292908 | 0,500000 | 0,4867° | 0,41428 |
| 7 | 1,707092 | 0,292896 | 0,500000 | 0,2016° | 0,41422 |
| 8 | 1,707104 | 0,292894 | 0,500000 | 0,0835° | 0,41422 |

À chaque pas, les deux jumeaux coupent le pré aux mêmes points, qui glissent vers P ; l'angle est divisé par √2 + 1 (rapport → √2 − 1 = 0,41421).

## 4. Les anneaux de Newton aux deux contacts

Lame entre les deux surfaces près du contact (flèches exactes, s_a(x) = a − √(a² − x²)) : intérieur t = s_{1/√2} − s_1 ; extérieur t = s_{1/√2} + s_1. Au premier ordre t ≈ x²/(2R_eff) avec 1/R_eff = √2 ∓ 1.

| anneau sombre m (λ = 0,001 R) | rayon, contact intérieur | contact extérieur | rapport | approx. √(mλR_eff) int. | ext. |
|---:|---|---|---|---|---|
| 1 | 0,049069 | 0,020351 | 2,4112 | 0,049135 | 0,020352 |
| 2 | 0,069302 | 0,028778 | 2,4082 | 0,069487 | 0,028782 |
| 3 | 0,084765 | 0,035242 | 2,4052 | 0,085104 | 0,035251 |
| 5 | 0,109142 | 0,045490 | 2,3992 | 0,109868 | 0,045509 |
| 10 | 0,153340 | 0,064307 | 2,3845 | 0,155377 | 0,064359 |
| 30 | 0,258854 | 0,111199 | 2,3279 | 0,269122 | 0,111474 |

Rapport limite des rayons : √((√2 + 1)/(√2 − 1)) = √2 + 1 = 2,414214 ; rapport des aires entre deux anneaux : (√2 + 1)² = 5,828427.
Au centre (d = 0), la lame est une couronne d'épaisseur constante 1 − 1/√2 = 0,292893 : une teinte uniforme, sans anneaux.

Exemple physique : pré de rayon 100 mm, petit disque de 70,7 mm, lumière du sodium (589 nm) : premier anneau sombre à 0,377 mm au contact intérieur et à 0,156 mm au contact extérieur.

## 5. La chèvre attachée au point orange : une corde certifiée

Avec le pré de rayon 1 et le piquet sur le bord, la corde vaut r = 2 cos(α/2), où α vérifie g(α) = sin α − α cos α − π/2 = 0. g est croissante sur ]0 ; π[ (g' = α sin α > 0).
- α entre 1,90569572930888389488266643… et 1,90569572931088389488266643… : g(bas) ≤ −1,80e−12 < 0 et g(haut) ≥ 1,80e−12 > 0 (calcul par intervalles), certifié : oui.
  Donc r ∈ [1,1587284730173064490695054 ; 1,1587284730189365865869613].
- α entre 1,90569572930988389488266633… et 1,90569572930988389488266653… : g(bas) ≤ −1,80e−25 < 0 et g(haut) ≥ 1,80e−25 > 0 (calcul par intervalles), certifié : oui.
  Donc r ∈ [1,1587284730181215178282334 ; 1,1587284730181215178282336].

Valeur : r = 1,15872847301812151782823350993…
La plus grande corde de la récursion qui broute exactement la moitié est 1/√2 (contact intérieur) ; au-delà, la chèvre doit allonger sa corde (partie XVI).

## 6. Les polyèdres nobles

- Octaèdre inscrit dans le pré (sommets (±1, 0, 0)…) : arêtes √2 (diagonales 1x, 1y), rayon de la sphère médiane 0,707107 = 1/√2. Le petit disque au centre est cette sphère médiane ; il touche les 12 arêtes en leurs milieux (les sommets du cuboctaèdre). En 2D : le cercle inscrit du carré des diagonales 1x, 1y.
- Six petits disques à la position d'Hippocrate (d = 1/√2, sur ±x, ±y, ±z) : chacun coupe la sphère du pré selon une calotte de 45°. Elles se touchent deux à deux (axes à 90°), sans se chevaucher (Monte-Carlo : 0,0000). Elles couvrent 6 × (1 − 1/√2)/2 = 3 − 3/√2 = 0,878680 de la sphère (Monte-Carlo : 0,878696). Restent 8 ménisques triangulaires, centrés sur les sommets du cube, soit (3√2 − 4)/2 = 0,121320, de rayon angulaire arccos(1/√3) − 45° = 9,7356°.
- En 2D, quatre disques d'Hippocrate (±x, ±y) pavent exactement la circonférence : quatre arcs de 90° qui se touchent aux diagonales 1x, 1y. Pas de ménisque en 2D ; les ménisques naissent en 3D.

**Deux aiguilles font toujours un polyèdre noble.** Une aiguille de longueur 2 centrée sur l'axe vertical, à la hauteur h, et la même tournée de α, à la hauteur −h : leurs quatre bouts forment un tétraèdre dont les arêtes opposées sont égales deux à deux, donc aux quatre faces égales (un disphénoïde, polyèdre noble).

| α | h | côtés d'une face | quatre faces égales ? |
|---:|---|---|---|
| 90° | 0,7071 | 2,000000, 2,000000, 2,000000 | oui |
| 90° | 0,3 | 1,536229, 1,536229, 2,000000 | oui |
| 45° | 0,5 | 1,259280, 2,000000, 2,101003 | oui |
| 45° | 1e−06 | 0,765367, 1,847759, 2,000000 | oui |
| 60° | 0,8 | 1,886796, 2,000000, 2,357965 | oui |
| 30° | 1,2 | 2,000000, 2,455188, 3,080917 | oui |

Pour α = 90° et 2h = √2 (les deux aiguilles séparées d'une diagonale 1x, 1y), c'est le tétraèdre régulier d'arête 2 : le simplexe de la grille décalée en 3D (parties XV et XVI).
Pour α = 45° (la première bissection de l'arbre de Perron sur l'angle droit), les arêtes latérales aplaties valent 2 sin 22,5° et 2 cos 22,5° : leur rapport est tan 22,5° = √2 − 1 = 0,414214.
