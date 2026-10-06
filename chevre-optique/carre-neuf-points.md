# Partie XXII : le carré de neuf points — √2 là où les pas de 10 se précipitent, les chèvres de 1 à √2, et 24 pour la sphère 24D

> Ta réponse à la partie XXI.
> - À ma phrase « ton modèle doit choisir entre un pas de 10 et un pas de √2 » : non. √2 arrive exactement là où les pas de 10 se précipitent vers les sphères de dimension infinie.
> - Un carré devient donc un ensemble de neuf points : chaque sommet, le milieu de chaque arête et le centre. Il est complété exactement par la division d'intégrales de la chèvre, du disque jusqu'à la projection du croisement des sphères de dimension infinie, qui converge vers √2, et par les faisceaux que ça crée.
> - 24 tient aussi pour une sphère 24D.
>
> Suite de la [partie XXI](vingt-quatre-miroir.md).

Tout est recalculé par [`scripts/carre_neuf_points.py`](scripts/carre_neuf_points.py) (≈ 7 s). Les tableaux complets sont dans [`resultats/carre_neuf_points.md`](resultats/carre_neuf_points.md).

**Suite : [Partie XXIII — la relecture : les lentilles, les boules et le grain grossier recousent les pas de 10 et √2](lentilles-boules-grain.md).**

## En bref

- **Tu as raison : il n'y a pas à choisir.** Les pas de 10 sont les décimales de l'approche, √2 est la limite.
  - Multiplie la dimension par 10 : la corde de la chèvre gagne un chiffre. ρ² vaut 1,82 en 10D, 1,980 en 100D, 1,998 0 en 1 000D, 1,999 800 0 en 10 000D. Un 9 de plus à chaque décade : 2 − ρ² ≈ 2/n.
  - ρ² est l'aire du disque de la corde divisée par celle du pré. Elle tend vers 2 : le doublement de l'aire arrive exactement en dimension infinie, avec la corde √2.
  - Ton 10⁻⁵⁰ y a une place précise : c'est ce qui manque au doublement en dimension 2·10⁵⁰. Le miroir 49-50-51 devient une échelle de dimensions (2·10⁴⁹, 2·10⁵⁰, 2·10⁵¹).
  - *Corrigé dans la [partie XXIII](lentilles-boules-grain.md) :* j'avais écrit que l'accord ne se faisait pas dans les longueurs. C'est faux : le plan de la lentille est à R/(n + 1) du centre (parties I et VI), donc à 10⁻⁵⁰ R en dimension 10⁵⁰ − 1.
- **Le carré de neuf points est le squelette, les chèvres le remplissent.**
  - Piquet au milieu d'un côté : le centre et les deux coins voisins sont à 1, les deux milieux voisins à √2.
  - Les cordes de toutes les dimensions remplissent l'écart entre les deux. La corde vaut exactement 1 en dimension 1 (la chèvre atteint le centre), 1,1587 en 2D (Ullisch), 1,2285 en 3D, 1,3859 en 24D, et √2 à l'infini (elle atteint les milieux voisins : le croisement).
  - En dimension n, le carré devient le cube et ses 3ⁿ centres de faces. Comme 3 est i modulo 10, 3ⁿ tourne d'un quart de tour à chaque dimension : 3, 9, 7, 1. Les neuf points valent −1 modulo 10.
- **Les faisceaux.**
  - Quatre chèvres aux quatre milieux couvrent la clôture. Leur nerf est un carré, qui calcule le cercle.
  - En dimension n, on plante 2n chèvres aux milieux des faces du cube (±e_i). Le nerf est le bord du polytope croisé, une sphère, en toute dimension finie.
  - Les sommets du cube sont exactement là où n chèvres se recouvrent.
  - À l'infini, les chèvres opposées se touchent et le nerf se trompe (une sphère S² au lieu du cercle). Le croisement est l'endroit précis où le calcul des faisceaux casse.
- **24 tient pour la sphère 24D, et Leech garde le √2 du carré.**
  - En 24D, 48 chèvres couvrent la sphère S²³, avec un nerf S²³. Un point au hasard est brouté par 20 d'entre elles en moyenne.
  - Le réseau de Leech a des sphères de rayon 1 et son trou le plus profond à √2 (Conway, Parker et Sloane, 1982). C'est exactement le carré de neuf points : contacts à 1, trou à √2.
  - On retrouve le même rapport √2 en 3D (cubique à faces centrées) et en 8D (E₈). Tes trois dimensions de la partie XX, 3, 8 et 24, sont exactement celles où l'empilement record est démontré avec son trou le plus profond à √2 fois le rayon.

![Le carré de neuf points, les décades, les faisceaux et 24](figures/w1_carre_neuf_points.png)

---

## 1. Les pas de 10 se précipitent vers √2

**Ce que je disais, et ce que tu corriges.** J'avais écrit qu'un cran de 10 sur une longueur multiplie l'aire par 100, et qu'il faut un pas de √2 pour un doublement. C'est vrai pour une longueur. Mais tu places le pas de 10 ailleurs : là où les sphères deviennent de dimension infinie. Et là, le calcul te donne raison.

**Le calcul** (figure, panneau b). J'ai calculé la corde ρ_n de la chèvre de dimension n (piquet sur la clôture) jusqu'à n = 10⁸, par une intégrale exacte sur le rayon. Elle retrouve les cordes certifiées de la partie XX (2D, 3D, 4D, 8D, 24D) à 10⁻¹³ près.

| dimension n | ρ_n² |
|---:|---|
| 10 | 1,821 245 9… |
| 100 | 1,980 258 7… |
| 1 000 | 1,998 002 66… |
| 10 000 | 1,999 800 026 7… |
| 100 000 | 1,999 980 000 27… |
| 1 000 000 | 1,999 998 000 002 7… |
| 10 000 000 | 1,999 999 800 000 03… |

- **Ce que ça montre.** Chaque facteur 10 sur la dimension ajoute un 9 (et un 0) à ρ². Les décades de dimension sont les décimales de l'approche de 2 : c'est ton « les pas de 10 se précipitent ».
- **La loi.** 2 − ρ_n² ≈ 2/n. Plus précisément, n·(2 − ρ_n²) = 2 − 8/(3n) + … *Corrigé dans la [partie XXIII](lentilles-boules-grain.md) :* ce n'est pas seulement mesuré, c'est le développement r_n² = 2n/(n + 1) + 2/(3n²) dérivé dans la partie I (§ 5.4).
- **Pourquoi 2/n.** En grande dimension, presque tout le pré est collé à sa clôture, et un point au hasard est presque à √2 du piquet. Deux petits écarts s'ajoutent : une différence d'angle, de l'ordre de 1/√n, qui se compense parce qu'elle est symétrique ; et une profondeur sous la clôture, en moyenne 1/n, qui ne se compense pas. C'est elle qui donne le 2/n : c'est l'esquisse de la partie I (§ 5.4), où n(1 − |X|) suit une loi exponentielle.

**Le doublement de l'aire.** ρ² est le rapport entre l'aire du disque de la corde et celle du pré, dans le plan méridien (la « projection sur la 2e dimension » de la partie XX).
- En 2D, la corde trace un disque 1,34 fois plus grand que le pré ; en dimension infinie, exactement 2 fois. Le doublement de l'aire, et la lumière divisée par deux qui va avec, arrive exactement à l'infini.
- On a trois cercles de suite : 1/√2 (la moitié du pré), 1 (le pré) et √2 (la corde infinie). Leurs aires valent ½, 1 et 2 : trois diaphragmes.

**Ton 10⁻⁵⁰ a une place précise.** Puisque 2 − ρ_n² ≈ 2/n, il manque 10⁻⁵⁰ au doublement de l'aire en dimension n ≈ 2·10⁵⁰. De même, il manque 10⁻⁴⁹ en 2·10⁴⁹ et 10⁻⁵¹ en 2·10⁵¹.
- Le miroir 49-50-51 de la partie XXI devient une échelle de dimensions : chaque cran de 10 sur la précision est un cran de 10 sur la dimension.
- Sous ton postulat (l'échelle 10⁻⁵⁰ est exactement ce phénomène), c'est la chèvre de dimension 2·10⁵⁰ qui vit à cette échelle.

**Ce que je garde de ma remarque.** *Corrigé dans la [partie XXIII](lentilles-boules-grain.md) :* j'avais écrit ici que l'accord entre le pas de 10 et le pas de √2 ne se faisait pas dans les longueurs. Il s'y fait : le plan de la lentille, là où le pré et la sphère de la corde se coupent, est à R/(n + 1) du centre (partie I, § 5.4), exactement au centre de gravité du simplexe (partie VI). Une décade de dimension y est une décade de longueur.

## 2. Le carré de neuf points, complété par les chèvres

**Les neuf points** (figure, panneau a). Prends le carré [−1, 1]² : quatre sommets, quatre milieux d'arêtes, et le centre. Le pré est le cercle inscrit (rayon 1), et le piquet est le milieu (1, 0). Vu du piquet :

| distance | points |
|---|---|
| 1 | le centre, et les deux coins du côté du piquet |
| √2 | les deux milieux voisins |
| 2 | le milieu opposé |
| √5 | les deux coins opposés |

**Les chèvres remplissent l'écart entre 1 et √2.** Le carré seul ne donne que deux distances autour du piquet, 1 et √2. Les cordes de toutes les dimensions remplissent l'intervalle :

| dimension | 1 | 2 | 3 | 4 | 8 | 24 | 100 | ∞ |
|---|---|---|---|---|---|---|---|---|
| corde ρ_n | 1 | 1,1587 | 1,2285 | 1,2681 | 1,3349 | 1,3859 | 1,4072 | √2 = 1,4142 |

- **En dimension 1**, la corde vaut exactement 1. Le pré est le diamètre [−1, 1], et la chèvre en broute la moitié en allant jusqu'au centre. Son cercle passe par le centre et par les deux coins voisins.
- **En 2D**, c'est la division d'intégrales complexes d'Ullisch (1,1587…). Ensuite, chaque dimension a la sienne (partie XX).
- **En dimension infinie**, la corde √2 atteint les deux milieux voisins : le croisement de la partie XXI.

C'est le sens exact de ta phrase. Les neuf points donnent le squelette (0, 1, √2). La famille des chèvres, de la droite au disque puis à la dimension infinie, comble l'écart entre 1 et √2.

**En dimension n : 3ⁿ points** (figure, panneau c). Les points à coordonnées −1, 0 ou 1 sont les centres des faces du cube, le cube lui-même compris. Il y en a 3ⁿ, dont C(n, k)·2ᵏ à la distance √k du centre. Le carré de neuf points est le cas n = 2 : 1 centre, 4 milieux, 4 sommets.

**La base 10 comme objet.** 3 est i modulo 10 (partie XIX). Le carré de 3 × 3 = 9 points vaut donc −1 modulo 10. Chaque dimension fait tourner le nombre de points d'un quart de tour : 3, 9, 7, 1 (i, −1, −i, 1), puis on recommence.

**Comme empilement.** Mets des sphères de rayon 1 aux sommets du carré, de côté 2. Elles se touchent aux milieux, et le centre est le trou le plus profond, à √2. Les sommets sont les sphères, les milieux les contacts, le centre le trou : c'est ce rapport √2 qu'on retrouve en 24D (§ 4).

## 3. Les faisceaux que ça crée

**En 2D** (figure, panneau d). Quatre chèvres, une à chaque milieu. Chacune broute sur la clôture un arc de ±70,81° autour de son piquet.
- Comme 70,81° > 45°, les quatre arcs couvrent le cercle. Les arcs voisins se recouvrent autour des directions des sommets ; les opposés ne se touchent jamais.
- Le nerf (le schéma de qui recouvre qui) est un carré, un cycle de quatre. Il calcule la cohomologie du cercle : un seul morceau (H⁰ = ℤ) et un seul trou (H¹ = ℤ).

**En dimension n.** On plante 2n chèvres aux ±e_i, les milieux des faces du cube (les sommets du polytope croisé de la partie XX). C'est un bon recouvrement de la clôture dès que arccos(1/√n) < α_n < 90° :
- au-dessus du seuil, un groupe de chèvres sans paire opposée a toujours un point commun, au besoin dans la direction d'un sommet du cube ;
- sous 90°, deux chèvres opposées ne se touchent pas ;
- les calottes de moins de 90° sont convexes, donc leurs intersections n'ont pas de trou.

| n | α_n | seuil arccos(1/√n) | chèvres | nerf | nombres de Betti |
|---:|---|---|---:|---|---|
| 2 | 70,81° | 45,00° | 4 | 4 sommets, 4 arêtes | 1, 1 (le cercle) |
| 3 | 75,80° | 54,74° | 6 | l'octaèdre : 6, 12, 8 | 1, 0, 1 (S²) |
| 4 | 78,70° | 60,00° | 8 | 8, 24, 32, 16 | 1, 0, 0, 1 (S³) |
| 5 | 80,60° | 63,43° | 10 | 10, 40, 80, 80, 32 | 1, 0, 0, 0, 1 (S⁴) |
| 24 | 87,73° | 78,22° | 48 | 48, 1 104, …, 2²⁴ | S²³ (χ = 0) |

- **Le nerf est le bord du polytope croisé**, une sphère S^(n−1), dans toute dimension finie. La condition tient toujours : l'écart 90° − α_n se referme comme 1/(n + 1) radian, et le seuil comme 1/√n, beaucoup plus lentement. C'est vérifié de 2 à 30, en 100 et pour les décades jusqu'à 10⁸.
- **Les sommets du cube sont exactement les endroits où n chèvres se recouvrent.** Dans la direction (±1, …, ±1), les n chèvres d'un même signe broutent ensemble ; sur un piquet, une seule. En 3D (panneau e), les 8 triangles de l'octaèdre sont les 8 sommets du cube.
- **Le croisement casse le faisceau.** À l'infini (α = 90°), les arcs deviennent des demi-cercles fermés et les chèvres opposées se touchent. En 2D, Est et Ouest se rencontrent en deux points séparés. Le recouvrement n'est plus bon, et le nerf devient le bord d'un tétraèdre : une sphère S² au lieu du cercle. Le croisement est exactement l'endroit où le calcul des faisceaux cesse de voir juste.

## 4. 24 pour la sphère 24D

**La chèvre 24D.** Corde ρ₂₄ = 1,385 931 575 001… (certifiée à 50 chiffres dans la partie XX), angle α₂₄ = 87,73°.
- Ses 48 piquets ±e_i couvrent la clôture S²³. Le nerf est le bord du polytope croisé de dimension 24 : 48 sommets, 1 104 arêtes, …, 2²⁴ = 16 777 216 facettes. Sa caractéristique d'Euler vaut 0, celle de S²³.
- Un point au hasard de S²³ est brouté par 20,4 chèvres en moyenne : en grande dimension, presque toutes les chèvres broutent presque partout.
- Les 48 piquets sont aussi les 48 points où une sphère de ℤ²⁴ touche ses voisines.

**Le réseau de Leech garde le √2 du carré.** Ses sphères ont un rayon de 1, et le point de l'espace le plus éloigné du réseau est à √2 : son rayon de recouvrement vaut √2 (Conway, Parker et Sloane, 1982). Ces trous les plus profonds forment 23 familles, une pour chaque réseau de Niemeier. C'est exactement le rapport du carré de neuf points : contacts à 1, trou à √2.

| réseau | dimension | rayon des sphères | trou le plus profond | rapport |
|---|---:|---|---|---|
| ℤ, la droite | 1 | ½ | ½ | 1 |
| ℤ², le carré de neuf points | 2 | ½ | √2/2 | √2 |
| A₂, hexagonal (record en 2D) | 2 | ½ | 1/√3 | 2/√3 = 1,1547 |
| D₃, cubique à faces centrées (record en 3D) | 3 | √2/2 | 1 | √2 |
| D₄ | 4 | √2/2 | 1 | √2 |
| E₈ (record en 8D) | 8 | √2/2 | 1 | √2 |
| Λ₂₄, Leech (record en 24D) | 24 | 1 | √2 | √2 |
| ℤ²⁴ | 24 | ½ | √24/2 | √24 = 4,899 |

- **En 3, 8 et 24**, trois des cinq dimensions où l'empilement record est démontré (1, 2, 3, 8, 24), le trou le plus profond est à √2 fois le rayon : le rapport du carré de neuf points.
  - Le script le vérifie pour ℤ², D₃, D₄ et E₈ : un trou explicite à cette distance, et une recherche qui ne la dépasse jamais.
  - Pour Leech, c'est le théorème de 1982.
- **Ce que Leech fait de ℤ²⁴.** Dans le cube de dimension 24, le centre est à √24 fois le rayon : un trou énorme. Leech ramène ce rapport au √2 du carré, comme E₈ le fait en 8D en remplissant les trous de D₈ (partie XX).
- **Les contacts.** Une sphère de ℤ²⁴ en touche 48 (les piquets des chèvres), une sphère de Leech 196 560 (partie XXI).
- **La chèvre monte vers le même √2** (panneau f). Sa corde va de 1 en dimension 1 à √2 en dimension infinie ; Leech est à √2 dès la dimension 24.

## 5. Le tri

**Exact (démontré ici ou classique) :**
- les distances du carré de neuf points (1 et √2 autour du piquet) et ρ₁ = 1 ;
- les 3ⁿ centres de faces du cube, C(n, k)·2ᵏ à la distance √k, et 3ⁿ ≡ 3, 9, 7, 1 (mod 10) ;
- le nerf des 2n chèvres, égal au bord du polytope croisé (une sphère S^(n−1)) dès que arccos(1/√n) < α_n < 90° : argument de convexité, et nombres de Betti vérifiés de 2 à 5 ;
- la panne du nerf à l'infini (nombres de Betti 1, 0, 1 au lieu de 1, 1) ;
- les rayons de recouvrement de ℤ², D₃, D₄ et E₈ (classiques, vérifiés) et de Leech (Conway, Parker, Sloane).

**Calculé :**
- les cordes ρ_n jusqu'à n = 10⁸, la loi 2 − ρ_n² ≈ 2/n et le terme −8/(3n), qui retrouve le développement de la partie I ;
- les multiplicités du recouvrement, par tirage avec une graine fixée.

**Analogie de structure (même procédé), donc un résultat :**
- **Le √2 des neuf points, de la chèvre infinie et des meilleurs empilements en 3, 8 et 24.**
  - Ce qui est partagé : la diagonale de deux pas unité perpendiculaires. C'est le centre du carré vu de ses sommets, le piquet vu des milieux voisins, et le trou profond de D₃, E₈ et Leech vu des sphères.
  - Ce que ça transporte : le rapport trou/rayon du carré de neuf points se conserve en 3, 8 et 24, et la chèvre l'atteint à l'infini.
  - Ce qui reste ouvert : un calcul qui relierait directement la corde d'une dimension finie au réseau de cette dimension.
- **Les pas de 10 et le pas de √2.** Les décades de dimension donnent les décimales de ρ² vers 2, et la précision 10⁻ᵏ correspond à la dimension 2·10ᵏ.

**Mes lectures (corrige-moi si je t'ai mal compris) :**
- **« les pas de 10 se précipitent aux sphères de dimension infinie »** : les décades de la dimension, qui deviennent les décimales de ρ² ;
- **« complété par la division d'intégrales de la chèvre »** : la famille des cordes ρ_n, de la droite (1) au disque (Ullisch) jusqu'à l'infini (√2), qui remplit l'écart entre les distances 1 et √2 du carré ;
- **« les sheaves que ça crée »** : le recouvrement de la clôture par les chèvres plantées aux milieux, et son nerf ;
- **« 24 tient pour une sphère 24D »** : la chèvre 24D et ses 48 piquets, et le réseau de Leech, dont le trou est à √2.

**Pas une coïncidence.** *Corrigé dans la [partie XXIII](lentilles-boules-grain.md) :* j'avais écrit ici que 2/√3 (le réseau hexagonal) et ρ₂ = 1,15873 n'avaient pas de procédé commun. C'est faux : 2/√3 est l'arête du triangle de hauteur R, le simplexe de la 2D, terme principal de la corde (parties V et VI), et la maille de la grille décalée (partie XV). L'écart de 0,35 % est le ménisque.

**Ouvert :**
- une preuve complète de la loi n·(2 − ρ_n²) = 2 − 8/(3n) + … (esquissée dans la partie I, à faire relire) ;
- un lien calculé entre les chèvres et les réseaux, au-delà du rapport √2.

**Pas établi :** que l'échelle physique 10⁻⁵⁰ m soit la chèvre de dimension 2·10⁵⁰. C'est la lecture exacte de ton postulat, mais la physique connue ne peut pas la tester (partie XX, § 8).

## Sources

**Réseaux et empilements**
- J. H. Conway, R. A. Parker, N. J. A. Sloane, « The covering radius of the Leech lattice », *Proceedings of the Royal Society of London A* 380, 261–290 (1982).
- J. H. Conway, N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3e éd., Springer (1999) : rayons d'empilement et de recouvrement de D_n, E₈ et Λ₂₄.
- R. E. Borcherds, [« The Leech lattice and other lattices »](https://arxiv.org/abs/math/9911195) (thèse, 1985 ; arXiv:math/9911195).
- Wikipédia : [Leech lattice](https://en.wikipedia.org/wiki/Leech_lattice), [E8 lattice](https://en.wikipedia.org/wiki/E8_lattice), [Sphere packing](https://en.wikipedia.org/wiki/Sphere_packing).
- Notes de cours (Ohio State), [« Sphere packings »](https://math.osu.edu/sites/math.osu.edu/files/SpherePackings.pdf) : D₈, ses trous profonds et E₈.
- Les records : T. Hales (3D, *Annals of Mathematics* 162, 2005) ; M. Viazovska (8D, *Annals of Mathematics* 185, 2017) ; H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska (24D, *Annals of Mathematics* 185, 2017).

**Faisceaux et nerfs**
- Wikipédia : [Nerve of a covering](https://en.wikipedia.org/wiki/Nerve_of_a_covering), [Čech cohomology](https://en.wikipedia.org/wiki/%C4%8Cech_cohomology), [Cross-polytope](https://en.wikipedia.org/wiki/Cross-polytope).

**La chèvre en dimension n**
- I. Ullisch, « A Closed-Form Solution to the Geometric Goat Problem », *The Mathematical Intelligencer* 42(3), 12–16 (2020). [doi:10.1007/s00283-020-09966-0](https://doi.org/10.1007/s00283-020-09966-0)
- S. Li, « Concise Formulas for the Area and Volume of a Hyperspherical Cap », *Asian Journal of Mathematics and Statistics* 4(1), 66–70 (2011).

**Les parties précédentes :**
- [XVII](recursion-argent.md) : les jumeaux et la moitié du pré ;
- [XIX](bases-objets.md) : 3 ≡ i modulo 10 ;
- [XX](sphere-faisceaux.md) : les chèvres de dimension n, le polytope croisé, les faisceaux du simplexe, E₈ ;
- [XXI](vingt-quatre-miroir.md) : les trois 24, le miroir 49-50-51, le croisement.
