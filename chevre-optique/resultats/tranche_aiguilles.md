# Partie XXV : les ouverts, la tranche 10⁻⁴⁹ – 10⁻⁵⁵ et les tournants d'aiguilles

Résultats calculés par `scripts/tranche_aiguilles.py`.

## 1. La divergence de la série, constante comprise

**La forme de Laplace de l'équation de la chèvre.** Avec 2α = π/2 + β (r² = 2 − 2 sin β), l'équation W_n(2α) − (2cos α)ⁿ W_n(α) = ½W_n(π) s'écrit exactement

∫₀^β (cos ψ/cos β)ⁿ dψ = ∫₀^∞ e^(−nu) tan φ(u) du,  avec sin φ = sin α·e^(−u).

Le membre de droite est une intégrale de Laplace. Son intégrande, tan φ(u) = s·e^(−u)/√(1 − s²e^(−2u)) (s = sin α), a sa singularité la plus proche en u = ln s → ln sin 45° = −ln √2 : une racine carrée.

Contrôle : la forme de Laplace redonne la corde plane, r₂² = 1,342651674182907566363 (Ullisch), et celle de la dimension 10, à 10⁻²⁵ près.

**Les grands ordres.** La singularité en racine carrée (Darboux), la dérivée de la corde par rapport à β (−2) et le déplacement de α avec la dimension (facteur e^(−1/2), signe alterné) donnent :

r²_m ≈ (−1)^m · e^(−1/2)·√(ln 2/π) · Γ(m − 1/2) · (2/ln 2)^m

| m | 10 | 20 | 30 | 40 | limite (Richardson, ordres 4, 6, 8) |
|---|---|---|---|---|---|
| coefficient / prédiction | 0,961554 | 0,985792 | 0,991235 | 0,993651 | 0,999993 ; 0,9999974 ; 1,000004 |

Le rapport tend vers 1 comme 1 + c/m, avec c ≈ −0,23.

**La meilleure précision.** On coupe au plus petit terme (j* ≈ n·ln √2). Prédiction : erreur ≈ moitié du plus petit terme ≈ e^(−1/2)·√(2/ln 2)·2^(−n/2)/n = 1,0303·2^(−n/2)/n.

| n | j* | erreur optimale | erreur × n·2^(n/2) | erreur / plus petit terme |
|---:|---:|---|---|---|
| 10 | 4 | 2,77·10⁻³ | 0,886 | 0,471 |
| 30 | 11 | 1,00·10⁻⁶ | 0,984 | 0,492 |
| 50 | 18 | 5,99·10⁻¹⁰ | 1,005 | 0,496 |
| 70 | 25 | 4,21·10⁻¹³ | 1,014 | 0,498 |
| 90 | 32 | 3,22·10⁻¹⁶ | 1,018 | 0,499 |
| 110 | 39 | 2,58·10⁻¹⁹ | 1,021 | 0,499 |

**La resommation de Borel–Padé** (39 coefficients, approximant [19/19] de la transformée de Borel, intégrale de Laplace) :

| n | 1 | 2 (Ullisch) | 3 | 5 | 10 | 24 |
|---|---|---|---|---|---|---|
| erreur de Borel–Padé | 9,13·10⁻⁷ | 6,08·10⁻¹⁰ | 1,24·10⁻¹² | 1,25·10⁻¹⁴ | 3,37·10⁻¹⁹ | 9,12·10⁻²⁷ |
| troncature optimale | 1,00·10⁰ | 3,24·10⁻¹ | 1,20·10⁻¹ | 3,33·10⁻² | 2,77·10⁻³ | 9,87·10⁻⁶ |

- En 2D, r² resommé = 1,342651673575 pour 1,342651674183 : la chèvre plane retrouvée depuis la dimension infinie.
- Les pôles réels de l'approximant s'alignent de −0,3473 vers −∞, en alternance avec ses zéros : c'est la coupure, qui commence en −ln √2 = −0,3466. (1 pôle parasite, en −0,298, est collé à un zéro : un doublet de Froissart, sans effet.)
- Les pôles complexes les plus proches de −ln √2 ± iπ (la singularité suivante prédite, −0,347 ± 3,142i) sont en −0,453 ± 3,248i.

## 2. Les bornes explicites, ordres 2 à 8

Même méthode que la partie XXIV, poussée à J termes de la série de l'équateur. Pour chaque J, on vérifie exactement (polynômes à coefficients entiers positifs en t = n − 100) que la condition de médiane change de signe entre S_J(n) ∓ C_J/n^(J+1), où S_J est la série coupée à 1/n^J. La zone centrale pèse moins que 1/n^(J+2).

| J | constante du reste | borne démontrée C_J (n ≥ 100) | vrai coefficient suivant |μ_(J+1)| |
|---:|---|---|---|
| 2 | 8,793·10² | 1,803·10³ | 6,533·10⁰ |
| 3 | 2,750·10⁴ | 5,638·10⁴ | 5,682·10¹ |
| 4 | 1,203·10⁶ | 2,467·10⁶ | 5,990·10² |
| 5 | 6,769·10⁷ | 1,388·10⁸ | 7,926·10³ |
| 6 | 4,653·10⁹ | 9,539·10⁹ | 1,276·10⁵ |
| 7 | 3,781·10¹¹ | 7,751·10¹¹ | 2,422·10⁶ |
| 8 | 3,545·10¹³ | 7,266·10¹³ | 5,291·10⁷ |

Les constantes démontrées croissent comme les coefficients eux-mêmes (des factorielles) : la série est asymptotique, et chaque ordre est démontré.

## 3. Le c_n de la partie XVI en dimensions 2 et 3, exactement

- **2D, par l'aire exacte de la lentille.** On paramètre par l'angle ψ = arcsin x₀ (le plan de la lentille) : r²(θ − sin θ cos θ) = ψ + sin ψ cos ψ, avec r² = d² − 2d sin ψ + 1. Le développement exact donne k² − d² = 1/3 + 4/(405d²) − 16/(25515d⁴) + …
- **3D, par le volume exact de la lentille** (deux boules) : k² − d² = 1/2 + 1/(96d²) − 1/(768d⁴) + …
- Ce sont exactement c₂ = 2·2·1/(3·3³·5) = 4/405 et c₃ = 2·3·2/(3·4³·6) = 1/96 : la formule c_n = 2n(n − 1)/(3(n + 1)³(n + 3)) de la partie XVI est démontrée en dimensions 2 et 3, où la méthode des moments ne s'appliquait pas.
- Au passage, en 2D, le plan de la lentille est en sin ψ = x₀ avec ψ = 1/(3d) + 1/(810d³) + 71/(204120d⁵) + …

Contrôle par l'intégrale radiale : en d = 30, (k² − d² − g²)·d² = 0,00987585 (2D, prédit 0,00987585) et 0,01041522 (3D, prédit 0,01041522).

## 4. L'unité du grain : l'angle de l'aiguille

Le piquet en e₃ sur la sphère, l'aiguille tourne de e₃ vers e₂ (partie XXI). Elle passe le bord de la chèvre de dimension n à l'angle α_n tel que 2 − 2cos α_n = r_n², donc **cos α_n = x₀ exactement** : l'écart au croisement vaut 90° − α_n = arcsin x₀.

| n | 2 | 3 | 4 | 8 | 24 | 100 |
|---|---|---|---|---|---|---|
| α_n | 70,81° | 75,80° | 78,70° | 83,74° | 87,73° | 89,43° |
| x₀ = cos α_n | 0,3287 | 0,2453 | 0,1960 | 0,1091 | 0,0396 | 0,0099 |
| écart arcsin x₀ (radian) | 0,3349 | 0,2479 | 0,1973 | 0,1093 | 0,0396 | 0,0099 |

**Le miroir des lectures.** Chaque lecture lit n ≈ κ/ε. Les κ vont par paires de produit 1 autour du plan : (1/2, 2) la corde relative et l'aire, (1/√2, √2) la corde et le diamètre, (ln 2, 1/ln 2) la coquille et les crans. Le plan est leur moyenne géométrique : le miroir x·x′ = f² avec f = 1.

| lecture | corde relative (√2 − r)/√2 | corde √2 − r | coquille (partie XXIII) | plan x₀ = cos α_n | crans log₂(2/r²) | diamètre 2(√2 − r) | aire 2 − r² |
|---|---|---|---|---|---|---|---|
| κ | 1/2 | 1/√2 | ln 2 | 1 | 1/ln 2 | √2 | 2 |

## 5. La tranche 10⁻⁴⁹ – 10⁻⁵⁵

| k | facteurs | k mod 8 | carrés min. | aiguilles (sans zéro) | r₂ | r₃ | r₄ | i modulo k |
|---:|---|---:|---:|---|---:|---:|---:|---|
| 49 | 7² | 1 | 1 | (7) | 4 | 54 | 456 | — |
| 50 | 2 · 5² | 2 | 2 | (7, 1) ; (5, 5) | 12 | 84 | 744 | 7, 43 |
| 51 | 3 · 17 | 3 | 3 | (7, 1, 1) ; (5, 5, 1) | 0 | 48 | 576 | — |
| 52 | 2² · 13 | 4 | 2 | (6, 4) | 8 | 24 | 336 | — |
| 53 | 53 | 5 | 2 | (7, 2) | 8 | 72 | 432 | 23, 30 |
| 54 | 2 · 3³ | 6 | 3 | (7, 2, 1) ; (6, 3, 3) ; (5, 5, 2) | 0 | 96 | 960 | — |
| 55 | 5 · 11 | 7 | 4 | (7, 2, 1, 1) ; (6, 3, 3, 1) ; (5, 5, 2, 1) | 0 | 0 | 576 | — |

- **Une dimension par cran** (partie XXI) : l'aiguille (7, 1, …, 1) à j uns a pour carré 49 + j. La tranche est cette aiguille vue de la dimension 1 à la dimension 7.
- **Le miroir de la tranche** : 49 + 55 = 50 + 54 = 51 + 53 = 2·52, donc 10⁻⁴⁹·10⁻⁵⁵ = 10⁻⁵⁰·10⁻⁵⁴ = 10⁻⁵¹·10⁻⁵³ = (10⁻⁵²)². Sept niveaux, centre 52, quatre en bas et quatre en haut.
- **La tranche parcourt les restes 1 à 7 modulo 8** : 49 ≡ 1 … 55 ≡ 7. Elle finit sur la colonne interdite de Legendre (partie XXI) : comme 7, 55 exige quatre carrés.

| k | plan (n = 10ᵏ − 4/3) | aire (2·10ᵏ − 4/3) | coquille ≈ ln 2·10ᵏ | équateur ≈ 0,455·10²ᵏ | ménisque ≈ 0,577·10^(k/2) |
|---:|---|---|---|---|---|
| 49 | 10⁴⁹ | 2·10⁴⁹ | 0,693·10⁴⁹ | 0,455·10⁹⁸ | 1,826·10²⁴ |
| 50 | 10⁵⁰ | 2·10⁵⁰ | 0,693·10⁵⁰ | 0,455·10¹⁰⁰ | 0,577·10²⁵ |
| 51 | 10⁵¹ | 2·10⁵¹ | 0,693·10⁵¹ | 0,455·10¹⁰² | 1,826·10²⁵ |
| 52 | 10⁵² | 2·10⁵² | 0,693·10⁵² | 0,455·10¹⁰⁴ | 0,577·10²⁶ |
| 53 | 10⁵³ | 2·10⁵³ | 0,693·10⁵³ | 0,455·10¹⁰⁶ | 1,826·10²⁶ |
| 54 | 10⁵⁴ | 2·10⁵⁴ | 0,693·10⁵⁴ | 0,455·10¹⁰⁸ | 0,577·10²⁷ |
| 55 | 10⁵⁵ | 2·10⁵⁵ | 0,693·10⁵⁵ | 0,455·10¹¹⁰ | 1,826·10²⁷ |

- Aux exposants impairs (49, 51, 53, 55), le ménisque fait apparaître √10 : 0,577·10^24,5 = 1,826·10²⁴.

**Les chiffres de la corde.** Pour chaque k de 49 à 55, en dimension 10ᵏ, les quatre premiers blocs de k chiffres sont les mêmes, à la longueur près : 99…98 | 00…02 | 66…6658 | 133…3392 (vérifié exactement). La tranche est autosimilaire : une décade de plus allonge chaque bloc d'un chiffre.

**Décades et crans.** La tranche couvre 6 décades, soit 6·log₂ 10 = 19,93 crans. 2²⁰ = 1 048 576 dépasse 10⁶ de 4,86 % : vingt crans de diaphragme couvrent la tranche, à la virgule « kibi » près (partie XIX).

## 6. Les tournants d'aiguilles

**Dans le plan** (parties XIV et XXI), seules 49, 50, 52 et 53 ont des aiguilles. Elles tournent par des angles pythagoriciens (rotation (a + bi)/c de la grille) :

| k | aiguilles du premier quadrant | rotations | demi-tour autour d'un bout : cases balayées | demi-disque πk/2 |
|---:|---|---|---|---|
| 49 | (7, 0) | 90,00° = (0 + 1i)/1 | 49 (3 positions) | 77,0 |
| 50 | (7, 1), (5, 5), (1, 7) | 36,87° = (4 + 3i)/5 ; 36,87° = (4 + 3i)/5 ; 16,26° = (24 + 7i)/25 | 74 (7 positions) | 78,5 |
| 52 | (6, 4), (4, 6) | 22,62° = (12 + 5i)/13 ; 67,38° = (5 + 12i)/13 | 68 (5 positions) | 81,7 |
| 53 | (7, 2), (2, 7) | 58,11° = (28 + 45i)/53 ; 31,89° = (45 + 28i)/53 | 73 (5 positions) | 83,3 |

**Vers 45°, la diagonale 1x, 1y** (la chèvre de dimension infinie) : chaque aiguille du plan y arrive avec une aiguille complémentaire.

- (7 + 0i)(1 + 1i) = 7(1 + i) : arctan(0/7) + arctan(1/1) = 45°
- (7 + 1i)(4 + 3i) = 25(1 + i) : arctan(1/7) + arctan(3/4) = 45°
- (6 + 4i)(5 + 1i) = 26(1 + i) : arctan(4/6) + arctan(1/5) = 45°
- (7 + 2i)(9 + 5i) = 53(1 + i) : arctan(2/7) + arctan(5/9) = 45°
- Pour 50, le complément est 4 + 3i, l'aiguille 3-4-5 : c'est la formule de Hermann de la partie XXI.

**Combien de dimensions pour que l'aiguille existe et tourne.** Nombre r_d(k) de points du réseau ℤᵈ à distance √k de l'origine :

| d | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
|---:|---|---|---|---|---|---|---|
| 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 4 | 12 | 0 | 8 | 8 | 0 | 0 |
| 3 | 54 | 84 | 48 | 24 | 72 | 96 | 0 |
| 4 | 456 | 744 | 576 | 336 | 432 | 960 | 576 |
| 5 | 3370 | 5240 | 6240 | 3760 | 3920 | 6720 | 7360 |
| 8 | 1887888 | 1764112 | 2201472 | 2496928 | 2382048 | 2289280 | 2685312 |

- **En 24D**, r₂₄(k) = (16/691)·σ*₁₁(k) + (128/691)·((−1)^(k−1)·259·τ(k) − 512·τ(k/2)) (Ramanujan), vérifié pour k = 49 … 55. Le τ de la partie XXI (Δ = η²⁴) compte les aiguilles de la tranche en dimension 24 : τ(49) = −1696965207, τ(50) = 611981400, r₂₄(49) = 9,053·10¹⁶.

**Le retournement i·i = −1 sur le réseau** (partie XX : une sphère S^(d−2) de chemins en dimension d). Les arrêts possibles du quart de tour sont les aiguilles du réseau de même longueur, perpendiculaires :

| aiguille | 2D | 3D | 4D | 5D | 6D | 8D |
|---|---|---|---|---|---|---|
| (7) (carré 49) | 2 | 4 | 54 | 456 | 3370 | 235998 |
| (7, 1) (carré 50) | 2 | 2 | 14 | 86 | 746 | 39062 |
| (7, 1, 1) (carré 51) | — | 0 | 24 | 112 | 792 | 40600 |
| (7, 1, 1, 1) (carré 52) | — | — | 12 | 36 | 812 | 54060 |

- (7, 1, 1) n'a **aucun** arrêt perpendiculaire en 3D : sur le réseau, elle ne peut pas s'y retourner par deux quarts de tour. Il faut une quatrième dimension (24 arrêts).

**Le croisement, dans la tranche.** En tournant de e₃ vers e₂, l'aiguille passe la chèvre de dimension n à arcsin x₀ ≈ 1/(n + 4/3) radian du croisement. Les chèvres de dimension 10⁴⁹ à 10⁵⁵ sont donc passées dans les derniers 10⁻⁴⁹ radian (5,7·10⁻⁴⁸ degré) du quart de tour, une décade d'angle par décade de dimension.

## 7. Les liens avec les autres parties

| partie | ce qu'on avait | ce que la partie XXV ajoute |
|---|---|---|
| XXIV | la divergence au rythme 1/ln √2, mesurée | dérivée, constante e^(−1/2)√(ln 2/π) ; Borel–Padé |
| XXIV | bornes explicites : ordre 2 seulement | ordres 2 à 8 démontrés pour n ≥ 100 |
| XVI, XXIV | c_n vérifié en 2D et 3D | démontré par l'aire et le volume exacts de la lentille |
| XX | deux chèvres au même endroit | la série de l'infini, resommée, redonne la chèvre plane |
| XXI | 49-50-51, une dimension par cran | la tranche 49 – 55 : l'aiguille (7, 1, …, 1) en 1 à 7 dimensions |
| XXI | √7 et Legendre | 55 ≡ 7 (mod 8) exige quatre carrés |
| XXI | le croisement, α_n | cos α_n = x₀ : le grain comme angle |
| XIV | aiguilles de la grille, 3-4-5, demi-case | rotations 3-4-5, 7-24-25, 5-12-13, 28-45-53 ; demi-tours |
| XIX | i modulo une base, aiguille primitive | i n'existe que modulo 50 et 53 dans la tranche |
| XX | retournement : S^(d−2) chemins | arrêts du réseau ; aucun pour (7, 1, 1) en 3D |
| XXI | τ de Ramanujan, Δ = η²⁴ | r₂₄(k) de la tranche par τ(k) |
| XIX | kilo contre kibi | 20 crans ≈ 6 décades |

