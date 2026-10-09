# Dossier ombres-cube-venn : le cube {0, 1}ⁿ et ses ombres

Dossier de la révision 001, écrit par l'agent « ombres » (phase 1). Il suit le gabarit du plan (`recueil/revisions/plan-001.md`, § 7) : ses huit sections sont les § 1 à 8, et le § 3 répond aux sept questions de mon entrée. Je renvoie aux six dossiers déjà écrits (K2, T4, fiche 010) au lieu de refaire leurs calculs.

**Étiquettes.** **démontré** ; **classique** (référence au § 6.3) ; **calculé** (`resultats/…`, section) ; **calculé ici** (calcul rapide hors dépôt, code au § 7) ; **ma lecture** ; **ouvert**. Chemins relatifs à `/home/user/Graphite/chevre-optique`, vérifiés avec `ls`. Aucun script du dépôt n'a été lancé ; j'ai lu `scripts/revision_001.py` et `resultats/revision_001.md`, et regardé les figures citées. Le dépôt `/home/user/dzoba/venn17` a été lu (README, `verify/RESULTS*.md`, certificats en JSON), sans exécuter son code.

## En bref

- **Lien 1 : un cube, des regards, et les corps de nombres les lisent (§ 3.1, 3.5).** Tous les regards sont écrits dans le corpus (Perron, Venn, ombre Σωⁱ, octaèdre, axes d'ordre 4, 3 et 2). Nouveau (calculé ici) : les périodes de Gauss du 17-gone sont des ombres Σωⁱ ; 4 ≡ i engendre le sous-groupe d'ordre 4 de (ℤ/17)*.
- **Lien 2 : la face de la fiche 015 est une restriction, pas une ombre (§ 3.3)** : la fibre de l'ombre au-dessus de 0 (roue modulo 30). 3 est le seul premier ∤ 10 qui coupe deux coordonnées (le facteur 2 de Hardy–Littlewood pour l'écart 6). 0 motif hors de sa face sous 10⁶.
- **Lien 3 : même nerf, autre garantie (§ 3.2).** Les chèvres ont le théorème du nerf (calottes convexes). Pour les dossiers (graphe de XXVII) : 75 intersections sur 81 contractiles, 6 non ; nerf (Betti 1, 0, 4) ≠ réunion (1, 4, 3). Le recouvrement v2 ne fait pas mieux : 130 sur 166, (1, 0, 1) contre (1, 0, 9, 1).
- **Gelé et liquide (§ 3.4).** Premier rang non monotone : 2 ou 3 (18 certificats). Mince en poids (0,235 % à 17) et en dessin (0,6 px), pas en rangs (20 à 33 %).
- **Trous.** (1) Un Venn dont le complément est une symétrie serait antipodal : la parité de C(n, 2) l'exclut à 17, où i existe ; à 19 et 23 il n'est ni connu ni cherché (§ 3.6). (2) Les certificats à 23 courbes ne sont pas lus ici ; la part des triangles dérive (35,95 ; 35,76 ; 35,12 % à 17, 19, 23). (3) Dzoba ne publie ni la moitié des croisements, ni la symétrie par le complément, ni le profil par rang, ni l'ordre de dessin (§ 6.3).
- **Recouvrement (§ 8)** : ajouter la partie V ; retirer la fiche 010.

## 1. La question directrice et la projection sur D1–D8

> Le cube {0, 1}ⁿ et ses ombres (une direction quelconque, la grande diagonale, l'ombre symétrique Σωⁱ) sont-ils le groupe commun du Venn, de Perron, de l'octaèdre, des cercles arctiques et des premiers par position ? (plan, § 1.7)

**Ma réponse.** Le cube est commun ; « groupe » est trop fort : ce qui agit est ℤ/n, avec le complément ℤ/n × ℤ/2, cyclique d'ordre 2n si n est impair (K2). Les regards sont tous écrits dans le corpus ; les premiers par position entrent par une restriction ; le gel du Venn n'est mince qu'en poids et en dessin ; le nerf des dossiers a une hypothèse à vérifier.

**Projection sur D1–D8** (ma lecture ; le plan : D6 0,8 ; D5 0,1 ; D2 0,1) :

| dimension | poids | ce qui la porte |
|---|---:|---|
| D6 sphères, cubes, Venn | 0,65 | les regards, l'octaèdre, les cercles arctiques, Henderson, le complément, Gauss |
| D7 hasard et méthode | 0,10 | le nerf et ses hypothèses, le gel, les fiches 004 et 005 |
| D2 bases et congruences | 0,08 | la fiche 015, Fermat, i modulo 17 |
| D5 Kakeya et Perron | 0,07 | le regard « direction quelconque » |
| D4 optique | 0,05 | les 34 aigrettes |
| D1 la chèvre | 0,05 | les 2n chèvres et leur nerf |

## 2. Les chaînes de production (script → résultats → figures → document)

Dans l'ordre de production. Scripts dans `scripts/`, résultats dans `resultats/`, figures dans `figures/` ; documents à la racine. Les numéros de section du document, du script et des résultats ne coïncident pas toujours : je donne les trois.

| partie (document) | script § → résultats § | figures (panneaux) | ce que le script produit |
|---|---|---|---|
| **II § 1–2** `archimede.md` | `calculs_archimede.py` § 1–3 (avec `archimede.py`, `figures_archimede.py`) → `archimede.md` § 1–3 | `b1_six_projections.png` ; `b3_cube_tournant.png` (a, b) | croisements en ±R/√2 et ±R/φ ; les trois sphères du cube ; r²(s) du cube qui tourne, col √2/2, ménisque π/(9√3) |
| **XV § 1** `grille-decalee.md` | `grille_decalee.py` § 1 → `grille_decalee.md` § 1 | `o1_grille_decalee.png` (a, b) | A_n : le cube de dimension n + 1 coupé par x₁ + … + x_(n+1) = 0 ; maille √(2n/(n + 1)) |
| **XX § 3, 5** `sphere-faisceaux.md` | `sphere_faisceaux.py` § 3 (`simplexe`, `cech`, `champs`), § 5 → `sphere_faisceaux.md` § 3, 5 | `u1_chevres_faisceaux.png` (e, f) ; `u2_cartes_losange.png` (a, d) | n + 1 chèvres (2·10⁵ points) ; Betti de S¹ à S⁸ ; deux cartes ; √n/2 |
| **XXI § 1, 4** `vingt-quatre-miroir.md` | `vingt_quatre_miroir.py` § 1 et § 3 (le § 4 du document est le § 3 du script) → `vingt_quatre_miroir.md` § 1, 3 | `v2_racine_sept.png` (a, b, c) | § 4 : coins à √3 et √7, Legendre (colonne ≡ 7 mod 8) ; § 1 : pas de cube (§ 6.2) |
| **XXII § 3–4** `carre-neuf-points.md` | `carre_neuf_points.py` § 3–4 (`nerf_croise`, `betti`) → `carre_neuf_points.md` § 3–4 | `w1_carre_neuf_points.png` (d, e, f) | 2n chèvres, nerf = polytope croisé ; α = 90° : S² ; trou à √2 (ℤ², D₃, D₄, E₈) |
| **XXVI § 3** `kakeya-miroir.md` | `kakeya_miroir.py` § 3 → `kakeya_miroir.md` § 3.1–3.3 | `aa3_cube_hexagone.png` (a à g) | ombre ‖u‖₁ ; √2·\|cos t\| + \|sin t\| ; deux carrés ; Rupert ; 3π/4 |
| **XXVII § 2, 4, 8** `carte-connexions.md` | `carte_connexions.py` § 2, 4, 8 → `carte_connexions.md` § 2, 4, 8 | `ab2_cercles_arctiques.png` (a à f) ; `ab3_liens_predits.png` (b, c) | diamant d'ordre 48 ; boîte 40³ ; MacMahon ; ‖u‖₁‖u‖∞ ≥ 1 ; arccos(1/3) |
| **XXVIII § 1, 3** `octaedre-perron-venn.md` | `octaedre_perron_venn.py` § 1, 3 → `octaedre_perron_venn.md` § 1, 3 | `ac1_octaedre.png`, `ac3_venn17.png` (a à f) | polaire du cube ; 35,10 % ; conique inscrite ; récurrence ; Venn à 5 ellipses ; 7 710 formes ; 97,74 % ; aigrettes ; Gauss ; 4 ≡ i |
| **XXIX § 1–2, 5** `venn-ppm.md` | `venn_ppm.py` § 1, 2, 5 (et 6) → `venn_ppm.md` § 1, 2, 5 (et 6) ; document § 5.1 = résultats § 5.2, § 5.4 = § 5.1, § 5.3 = § 6 | `ad1_venn_ppm.png` (a à d) ; `ad2_deux_ombres.png` (b à f) | contour, 7 710 inconnues ; 131 070 croisements ; texture ; N_l/C(17, l) ; sommes nulles ; 34-gone ; non monotones (7 certificats) |
| **XXX § 3** `centre-venn.md` (et § 2.5, 7.3) | `centre_venn.py` § 3 (et 2, 7) → `centre_venn.md` § 3 (et 2, 7) | `ae2_diaphragmes_diffraction.png` (a, b) ; `ae1_centre_moitie.png` (f) | Euler, Lefschetz ; Lambert + Archimède ; deux miroirs ; la moitié des 18 certificats |

**Quatre chaînes.** (1) *Du cube qui tourne à l'octaèdre* : II § 2 → XXVI § 3 → XXVII § 4 → XXVIII § 1. (2) *Du simplexe au nerf* : XV § 1 → XX § 3 → XXII § 3 → XXVII § 4. (3) *Des cercles arctiques* : II § 2 → XXVII § 2 → XXVIII § 1.3–1.6. (4) *Du Venn* : XXVIII § 3 → XXIX § 2, 5 → XXX § 3.

**Points faibles.**
- Le nerf de XX (`cech`) et celui de XXII (`nerf_croise`) sont *posés* (bord du simplexe, bord du polytope croisé) ; la géométrie les justifie (calottes convexes < 90°) et le script contrôle seulement la couverture.
- `resultats/venn_ppm.md` § 6 ne tabule que 7 des 18 certificats, un seul à 19 courbes ; le texte en tire une épaisseur constante (j'en lis 18, § 3.4). La texture de XXIX § 2.2 n'a aussi qu'une ligne par taille.
- Ma liste de fichiers (plan, § 5.2.7) omet `u2_cartes_losange.png`, `ab3_liens_predits.png`, `ae2_diaphragmes_diffraction.png` et `scripts/figures_archimede.py`.

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 Le tableau des regards (question 2)

Un cube, des directions de regard : ce que chacune montre, où c'est démontré, avec quel statut.

| regard | ce qu'on voit | où | statut |
|---|---|---|---|
| **direction quelconque** (a₀, …, a_(k−1)) | 2ᵏ sommets séparés, dans l'ordre binaire, qui fusionnent par moitiés (2^(k−j) fentes au niveau j) : Perron ; aire 2/(k + 2) | V § 3 (vérifié) ; XXVIII § 2.4, 3.5 ; XXIX § 5.1 | démontré |
| **grande diagonale** (1, …, 1) | le rang ; des couches C(n, k) : la binomiale du Venn à aire égale | XXIX § 2.3, 5.1 ; R : `venn_ppm.md` § 2 (N_l/C(17, l) de 0,825 à 1,045) | démontré (ombre) ; mesuré (anneaux) |
| **ombre symétrique** Σωⁱ | zonogone de côté 1, à 2n côtés (n impair) ou n ; centre réservé à ∅ et « tout » si et seulement si n est premier ; carré moyen k(n − k)/(n − 1) ; le complément est z ↦ −z | XXIX § 5.4 ; R : `venn_ppm.md` § 5.1 ; K2 (`lumiere` § 5.1) | démontré ; Henderson (1963) classique ; complément : ma lecture, exacte |
| **ombre en 3D** | ‖u‖₁ (cube) ; max(‖u‖₁, 2‖u‖∞) (octaèdre, polaire par la sphère médiane) ; égales sur 8 triangles de 70,53°, soit 6·arccos(1/3)/π − 2 = 35,0959 % ; moyennes 3/2 et √3 | XXVI § 3.1 ; XXVIII § 1.1–1.2 ; R : `octaedre_perron_venn.md` § 1 | démontré |
| **axes d'ordre 4 et 3** | le losange est l'ombre de l'octaèdre, l'hexagone celle du cube ; le cercle inscrit est l'ombre de la sphère médiane, et le cercle arctique | II § 2 ; XXVII § 2 ; XXVIII § 1.3–1.4, 1.6 | démontré, sauf Kenyon–Okounkov (cité) |
| **axe d'ordre 2** (cube qui tourne) | ombre √2·\|cos t\| + \|sin t\| ; hexagones à 109,47° et 70,53° ; deux carrés qui se quittent à l'hexagone ; Rupert | XXVI § 3.2–3.5 ; R : `kakeya_miroir.md` § 3 | démontré ; calculé |
| **26 directions** de {−1, 0, 1}³ | ‖u‖₁·‖u‖∞ ≥ 1, égalité exactement là ; le seuil des 2n chèvres est la plus grande ombre | XXVII § 4 ; XXII § 3 | démontré |
| **une face ; un sous-groupe des unités** | la fibre de l'ombre au-dessus de 0 (fiche 015) ; les périodes de Gauss | § 3.3, 3.5 | exact, calculé ici |

**Transporté** : les comptes (2ⁿ morceaux, C(n, k) par couche), l'hexagone (√3, 35,10 %, le cercle de rayon √2/2) et les trois 34, qui sont un seul fait, la parité de n (K2). **Ouvert** : un Venn dessiné de façon que la structure de Perron y apparaisse en deux dimensions (XXVIII § 3.5 ; XXIX § 5.1 : les veines n'en sont pas) ; Kenyon–Okounkov n'est pas refait.

### 3.2 Le nerf des chèvres et le nerf des dossiers (question 3)

**Le même procédé.** XX § 3 recouvre S^(n−1) par n + 1 calottes (les chèvres) : un sommet par calotte, une arête par couple qui se coupe, et ainsi de suite ; les matrices de bord donnent les Betti (`cech`, rang modulo p). `betti` de `scripts/revision_001.py` fait la même algèbre sur les dossiers (rang en fractions).

**Pourquoi XX est un théorème et T1 n'en est pas un.** Le théorème du nerf (Borsuk 1948 ; Hatcher, cor. 4G.3) demande des intersections contractiles. Pour les chèvres c'est démontré : une calotte de moins de 90° est convexe, ses intersections aussi, et arccos(1/n) < α_n < 90° fait que toute famille propre se coupe et que la famille entière non (XX § 3 ; XXII § 3). Le corpus a même le contre-exemple : à α = 90° (XXII § 3), E ∩ W est fait de deux points, le recouvrement n'est plus bon, et le nerf devient S² au lieu du cercle.

**Ce que le nerf des dossiers dit** (sans théorème) : quels dossiers partagent un élément, quels triplets n'en partagent aucun (les triangles vides de T1 : des pistes), combien (1,1 à 1,5 en moyenne, R : `revision_001.md` § 3). **Ce qu'il ne dit pas** : les trous à l'intérieur d'un dossier, le poids (une fiche ou dix parties : la même arête), la forme du corpus sans espace.

**« Contractile », pour des dossiers.** Il faut un espace. Je prends le graphe des renvois de la partie XXVII (une partie par sommet ; une arête quand l'une cite l'autre ; même construction que `carte_connexions.py`, refaite pour 30 parties : 241 paires sur 435 ; pour 26 parties, 178 sur 325, comme XXVII) et son complexe de drapeaux (un simplexe : des parties qui se citent toutes). Un dossier est le sous-complexe sur ses parties. Une intersection est contractile quand ses parties communes se citent sans trou : connexe, sans cycle non rempli. Un *sommet-cône* (une partie qui cite toutes les autres parties communes) suffit : c'est le « triangle du bas » de l'arbre de Perron (plan, § 2.0).

**Mesure** (calculé ici ; v1, parties seules, rang réel, identique modulo 2 ; § 7). 81 intersections non vides sur 255 familles. Avec la partie I (le README, cité par toutes : tout dossier qui la contient devient un cône) : 76 acycliques, 70 avec cône. Sans elle : 75 acycliques, 67 avec cône, et six échecs :

| intersection | parties communes | défaut |
|---|---|---|
| bases | 11 (III … XXVIII) | 3 boucles |
| lumière | 13 (II … XXX) | 2 boucles |
| bases ∩ lumière | IX, XI, XII, XIX, XXVIII | 1 boucle |
| grain ∩ ombres | XV, XXIX, XXX | 2 morceaux : {XV} et {XXIX, XXX} |
| hasard ∩ lumière | XIII, XVIII, XXX | 2 morceaux : {XIII} et {XVIII, XXX} |
| lumière ∩ moitiés ∩ ombres | II, XX, XXX | 2 morceaux : {II} et {XX, XXX} |

**Lecture.** Les trois « deux morceaux » ont le défaut de XXII : l'intersection est coupée en deux, et le nerf voit une arête là où il y a un cycle. Les boucles sont dans bases et lumière. Le nerf (parties seules) a pour Betti (1, 0, 4), la réunion des dossiers (1, 4, 3) : les quatre boucles de la réunion (3 + 2 − 1) lui échappent. Les cavités de T1 (b₂ = 5 au niveau 3, p = 0,73 contre le nul, R : `revision_001.md` § 3) sont donc des propriétés du recouvrement ; les triangles vides restent des pistes.

**Le recouvrement v2** (bloc JSON de `verification-croisee-001.md`, sans les corrections de ce dossier) ne ferme rien : 166 intersections, 130 acycliques (135 avec la partie I), 112 avec cône ; sans la partie I, quatre dossiers (aiguilles, bases, lumière, moitiés) ne sont pas contractiles à eux seuls ; nerf (1, 0, 1), réunion (1, 0, 9, 1) (calculé ici ; avec la partie I : (1, 0, 10, 1)). Le b₂ = 1 de T1 en v2 est donc, lui aussi, une propriété du recouvrement. Ajouter la partie V ne change rien à ces nombres. Pour fermer les échecs de v1 : une partie-cône qui cite les deux morceaux.

### 3.3 La fiche 015 : une restriction, pas une ombre (question 4)

**Réponse.** La face choisie par a modulo 3 est la restriction du cube à une face, c'est-à-dire la fibre, au-dessus du sommet 0, de l'ombre sur les coordonnées interdites. Elle n'est pas une ombre : une ombre oublie des coordonnées, la face en fixe à 0. Les deux se confondent parce que la restriction de l'ombre sur les coordonnées libres à la face est une bijection.

**La correspondance exacte** (démontré ; contrôlé sous 10⁶, calculé ici). Coordonnées x_u ∈ {0, 1}, u ∈ {1, 3, 7, 9}, x_u = 1 si 10a + u est premier. Comme 10a + u ≡ a + u (mod 3), la coordonnée u est interdite quand 3 | a + u ; or u mod 3 vaut 1, 0, 1, 0. Donc m = a mod 3 interdit {3, 9} (m = 0), rien (m = 1), {1, 7} (m = 2), et la face est F(m) = {x : x_u = 0 pour u interdit} : F(0) = {x₃ = x₉ = 0} (4 sommets), F(1) = le cube (16), F(2) = {x₁ = x₇ = 0} (4). F(0) et F(2) se coupent au seul sommet ∅.

**Le contrôle.** 99 999 dizaines (a ≥ 1) sous 10⁶ : 0 motif hors de sa face. La paire {1, 7} : 2 700, 1 508 et 0 dizaines en a ≡ 0, 1, 2 ; {3, 9} : 0, 1 489, 2 727 ; les quatre autres paires n'existent qu'en a ≡ 1. En a ≡ 1 les six paires ont la même fréquence (bruit ±2,6 %) ; dans sa face, une paire en a 1,8 fois plus (totaux de R : `recueil_verifications.md` § 6).

**Pourquoi 3, et pas 7.** Les différences entre deux unités sont 2, 4, 6, 8 : le seul premier impair ∤ 10 qui en divise une est 3 (6 = 7 − 1 = 9 − 3). Pour q = 7, 10a + u ≡ 3a + u est divisible par 7 si u ≡ 4a : une seule coordonnée est interdite (a mod 7 = 0, 2, 4, 6 : u = 7, 1, 9, 3), aucune pour a mod 7 = 1, 3, 5. La face modulo 3 est donc la seule de codimension 2 : c'est le facteur (p − 1)/(p − 2) = 2 de la série singulière de Hardy–Littlewood (1923, classique) pour l'écart 6, pas pour 2, 4, 8. La roue modulo 30 la dessine : 1, 7 | 11, 13, 17, 19 | 23, 29 sont les trois faces (classique).

**Ce que ça relie, et ce que ça casse.** (1) Exact : n ↦ −n modulo 30 (u ↦ 10 − u) échange F(0) et F(2) ; le quart de tour u ↦ 3u (le i de XIX) ne préserve pas {1, 7} | {3, 9} : les premiers ne voient que le demi-tour. (2) (ℤ/10)* est cyclique d'ordre 4 (engendré par 3 ≡ i) ; son élément −1 fixe {1, 9} et {3, 7}, comme les diamètres du carré (n = 4 : 2 sous-ensembles propres de somme nulle, R : `venn_ppm.md` § 5.1). Pour toute base b > 6, φ(b) est pair et > 2 : aucun cube des dizaines n'est celui d'un Venn symétrique (Henderson). Une obstruction de plus pour K5 (§ 5).

### 3.4 Gelé et liquide, et les cercles arctiques (question 5)

**Les faits** (calculé ici sur les 18 certificats locaux, § 7 ; ils recoupent XXIX § 5.3 et R : `venn_ppm.md` § 6, qui n'en tabule que 7).
- Les rangs 0, 1, n − 1 et n n'ont aucune région non monotone (18 sur 18).
- Le premier rang k₁ qui en a une vaut 2 (n = 11, 13 ; 2 des 12 Venn à 19 courbes) ou 3 (les quatre à 17 ; 10 des 12 à 19) ; au pôle opposé, n − k₂ vaut 2 ou 3 aussi. À 23 courbes, `verify/RESULTS-23.md` donne pour `venn23-c19-s230019` des régions non monotones de poids 2 ({20, 22}, {19, 21}, {18, 22}) : k₁ ≤ 2 ; pour les cinq autres, {18, 19, 22} : k₁ ≤ 3.
- Profil (fraction des régions du rang ; moyenne de 12 Venn à 19 courbes) : rang 2 : 1,9 % ; 3 : 14,4 ; 4 : 19,4 ; 5 : 21,6 ; 6 : 17,8 ; 7 : 14,4 ; 8 : 12,0 ; 9 et 10 : 10,5 ; puis le miroir. À 17 courbes (4 Venn) : 3 : 10,0 ; 4 : 20,4 ; 5 : 17,2 ; 8 : 9,5. Pic ≈ 20 % vers k/n ≈ 0,25, creux ≈ 10 %.

**Pourquoi la couche gelée paraît mince** : en poids et en dessin, pas en rangs.
- *Poids.* Les rangs ≤ 2 pèsent 2(1 + n + C(n, 2))/2ⁿ : 0,235 % à 17 courbes (308 régions), 0,073 % à 19 ; à 23 avec deux rangs, 0,0006 %.
- *Dessin à aire égale.* À 17 courbes, les niveaux 1–2 forment un anneau de 0,6 px et les niveaux 15–16 un disque de 34 px de rayon (sur 984 px).
- *Rangs.* k₁/n vaut 0,18 ; 0,15 ; 0,18 ; 0,16 (0,11 pour deux Venn à 19) : 20 à 33 % des rangs sont gelés à 11–19 courbes. Comparer, comme XXIX § 5.3, 0,23 % de poids à 21,5 % d'aire gelée du losange met côte à côte un poids binomial et une aire. L'épaisseur vaut 2, 2, 3, 3 à 11, 13, 17, 19 (au plus 2 pour c19 à 23) ; proportionnelle à n elle vaudrait ≈ 3,7 à 23 : c'est l'argument pour une épaisseur constante.

**Pourquoi pas de cercle arctique.** (i) Un cercle arctique naît d'une hauteur imposée au bord d'un domaine fixe ; la sphère n'a pas de bord, seuls les pôles imposent 0 et n. (ii) La règle de Venn est globale (chaque étiquette une fois), pas locale, et aucune loi n'est connue : les diagrammes viennent d'une marche de Metropolis recuite depuis un échafaudage (deux diagrammes distincts partagent environ un dixième de leurs faces, README de Dzoba), pas d'un tirage. (iii) Les sommets du cube se concentrent sur le rang n/2 : pas de limite d'échelle.

**Pour une forme limite il faudrait** une loi (un Venn aléatoire de loi connue, ou la loi stationnaire de la marche : non publiée) ; une coordonnée (k/n, (k − n/2)/√n ou l'aire : trois figures différentes) ; une densité de défauts qui converge (les profils à 17 et 19 courbes sont proches) ; un test : k₁ à 23 courbes vaut 2 ou 3 si l'épaisseur est constante, 4 si elle croît avec n (les six certificats, en flux : **à calculer**).

### 3.5 Les périodes de Gauss sont des ombres (nouveau)

XXVIII § 3.6 construit le 17-gone par la tour de Gauss (2, 4, 8, 16 classes ; 3 est racine primitive modulo 17) ; XXIX § 5.4 définit l'ombre Σωⁱ. Les deux se rejoignent (calculé ici, 10⁻¹⁵) : une période de Gauss est l'ombre d'un sommet du cube {0, 1}¹⁷, la région indicatrice d'une classe de (ℤ/17)*. L'ombre des carrés {1, 2, 4, 8, 9, 13, 15, 16} vaut (−1 + √17)/2 ; celle de ⟨4⟩ = {1, 4, 13, 16} = {±1, ±i} (4² ≡ −1) vaut 2,0495, racine de x⁴ + x³ − 6x² − x + 1. Multiplier les étiquettes par h est la conjugaison de Galois : ombre(hS) = σ_h(ombre S). Ce n'est pas une symétrie du dessin (la rotation est i ↦ i + 1) mais du treillis booléen. `bases-congruences-premiers` (lien 2, § 3.3) a déjà (ℤ/10)* comme groupe de Galois et la tour de ⟨10⟩ ; ici c'est (ℤ/17)*, et i = 4 y engendre le sous-groupe d'ordre 4. **Ouvert** : la forme, dans les certificats, des 32 régions fixées par ⟨4⟩.

### 3.6 La symétrie par le complément (question 7, première moitié)

**Ce qu'elle est** (ma lecture, exacte). Sur le cube, S ↦ [n] \ S est la symétrie centrale ; dans l'ombre, z ↦ −z, parce que Σωⁱ = 0. Elle change le rang k en n − k et le niveau l d'un croisement en n − l. Avec la rotation, ℤ/n × ℤ/2 est cyclique d'ordre 2n si n est impair : c'est K2.

**Ce que serait un Venn qui la respecte** (démonstration esquissée, ma lecture). Je la prends au sens fort, pour un Venn simple : un homéomorphisme h de la sphère envoie la région d'étiquette A sur celle d'étiquette [n] \ A. Il garde chaque courbe et en échange les côtés. Il n'a aucun point fixe : une région, une arête ou un croisement fixé obligerait un ensemble à être son propre complément (S = [n] \ S ; S = [n] \ {i} \ S ; S = [n] \ {i, j} \ S), ce qui est impossible pour n ≥ 3. (La réflexion de l'équateur, que `moities` § 5.5 compte parmi les actions possibles, fixerait un cercle de points : elle est exclue.) Par Lefschetz, h est de degré −1 ; on le prend involutif (il ne fixe aucune cellule : on le corrige cellule par cellule), et c'est l'antipode (classique). Chaque courbe est invariante par un demi-tour, et le quotient est une famille de n courbes *unilatères* du plan projectif (pour n = 3 : les trois grands cercles).

**Une obstruction de parité** (nouveau ; démontré sous ces hypothèses). Dans le plan projectif, deux courbes unilatères se coupent un nombre impair de fois (classique). Le quotient a (2ⁿ − 2)/2 = 2^(n−1) − 1 croisements, un nombre impair, répartis sur C(n, 2) paires de courbes. Donc C(n, 2) est impair : n ≡ 2 ou 3 (mod 4). Pour n premier impair : n ≡ 3 (mod 4), c'est-à-dire que −1 n'est pas un carré modulo n, et que i n'existe pas (K5). **À 17 (4² ≡ −1) un tel Venn n'existe pas. À 19 et à 23 la parité ne l'exclut pas** ; s'il existait, ses inconnues se réduiraient de moitié (à 19 : 27 594 orbites par la rotation, 13 797 avec le complément). Cela exclut la symétrie au sens fort à 17, pas l'égalité N_l = N_(n−l), qui reste ouverte.

**Ce qu'on sait.** L'égalité N_l = N_(n−l) échoue pour les 18 certificats (écart max de 52 à 2 223, R : `centre_venn.md` § 2 ; je retrouve 132, 52, 1 275 et 703 sur quatre certificats avec le code du § 7). Le test de parité aussi (calculé ici, 18 sur 18) : le nombre c_d de croisements d'une paire de courbes à distance d ne dépend que de d, leur somme vaut (2ⁿ − 2)/n, et les c_d ne sont jamais tous ≡ 2 (mod 4). Aucun texte du dépôt de Dzoba ne cherche ni n'exclut un tel diagramme. L'autre candidat, le demi-tour équatorial « miroir + complément » (`moities` § 4.1, 5.5), a deux points fixes, au milieu d'arêtes de l'unique courbe fixée (n impair) : la parité ne l'exclut pas, et c'est lui qui laisse une trace dans les 18 certificats (f jusqu'à 14 %, 1,5 à 2,3 fois le hasard), sans être une symétrie. **Ouvert** à 19 et 23.

## 4. Les fiches du dossier : verdict, test, et la partie qui portait déjà le lien

Rameaux de hasard : **004** (testée) et **005** (compatible). **003** est le contraire : une structure que les tests à tolérance déclarent « hasard » (fiche 012).

| fiche | verdict | test, et ce que j'y ajoute | la partie qui portait déjà le lien | place dans P1 |
|---|---|---|---|---|
| **003** 34·tan(π/34) ≈ π (D6, D5, D7) | **structure**, confirmée | variation de N : l'écart × N² tend vers π³/12 (fiche). *Ajout, démontré* : 34·tan(π/34) est le périmètre sur la largeur du 34-gone de côté 1 de l'ombre Σωⁱ (périmètre 34, largeur 1/tan(π/34)) ; pour un disque ce rapport vaut π | XXVIII § 2.5 et § 3.4 (polygone circonscrit à 2N côtés) ; XXIX § 5.5 | feuille des branches Perron et K2 |
| **004** 35,8 % ≈ 35,10 % (D7, D6) | **hasard (testé)**, maintenu | variation de n : 36,0 ; 37,3 ; 35,95 (4 Venn) ; 35,76 (12 Venn) ; 35,12 % à 23 (5 certificats, README de Dzoba). Exact : 6·arccos(1/3)/π − 2 = 35,0959 %. Le test d'origine (n ≤ 19) ne voyait pas la dérive : NF4 | XXVIII § 1.2 et XXIX § 2.2 ; aucun mécanisme commun | **rameau de hasard**, branche « cube qui tourne » |
| **005** moitié exacte (D6, D7, D2) | **ouvert**, compatible avec le hasard | réplication : 12 Venn à 19 courbes, écart ±24,7 orbites, 1,6 % par tirage. *Ajout* : le complément n'étant pas une symétrie (18 sur 18 ; au sens fort, exclu à 17, § 3.6), rien ne force la moitié ; Fermat la permet (2ⁿ⁻¹ − 1 = n × entier) | XXX § 2.5, 7.3 | **rameau de hasard**, branche Venn (aussi P2) |
| **006** le centre bouge (D3, D8, D6) | **structure** | T4 (R : `revision_001.md` § 4.8–4.9) : pas d'ordre de dessin (p = 0,64 et 0,19) ; le seuil déplace le centre de 0,044 à 27,4 px, la moitié reste à 49,3–49,7 %. *Ajout (ma lecture exacte)* : le dipôle relatif est \|Σ wᵢ ωⁱ\|/Σ wᵢ, l'ombre du vecteur des poids (`lumiere` N5) | XXX § 1.2 (Wielen, 1996) | absente du plan (P8, P5) ; j'ajoute P1 par la formule |
| **008** centre au millième de pixel (D3, D6) | **calculé** | quatre rotations (≤ 0,003 px). *Ajout* : l'image se calcule sur le quotient par la rotation (7 710 inconnues), donc symétrique par construction ; les 0,004 px sont la convention du demi-pixel (999,5) : la fiche vérifie la chaîne, pas le Venn | XXIX § 1.2 ; § 5.4 (le centre est le seul point fixe) | feuille de la branche Venn (le point fixe d'Henderson) |
| **009** 34 + 34 aigrettes (D4, D6, D5) | **structure** | K2 (N = 3 à 20) : renvoi à `lumiere` § 5.1 et `aiguilles` § 5.1. Les 36 aigrettes intérieures, à 4,0°, restent ouvertes | XXVIII § 3.3–3.4 | branche de la parité (K2), pas celle du cube |
| **010** Ullisch 39,34 % (D1, D6) | **exact** ; à retirer de mon dossier | `corde` § 4.1 et `moities` § 4.2 : vrai du seul cercle du bord, cas de XXV § 1.5 ; la figure `ae2` (d) le montre (la part monte de 0,39 à 1 du niveau 6 au niveau 13) | X § 5 ; XX § 1 | hors de P1 : P2, branche équation |
| **015** dizaines et cube (D2, D6) | **exact** | § 3.3 : une restriction, la fibre de l'ombre ; 0 motif hors de sa face sous 10⁶ | XIX § 2 (3 ≡ i) ; XXVIII § 3.5 (le cube {0, 1}ⁿ) | branche des premiers, confirmée *par restriction* ; la dérive qui croise π puis 2√2 (test 4.2) est un rameau de hasard |

## 5. Les congruences et les obstructions

| | ce qui est comparé | se recolle jusqu'où | obstruction | où |
|---|---|---|---|---|
| K2 | les trois 34 | entièrement (N impair) : μ_N ∪ (−μ_N) = μ_2N ; le complément est z ↦ −z | aucune | renvoi `lumiere` § 5.1, `aiguilles` § 5.1 |
| K5 | le 17 de Henderson et le 17 de i | une implication : i existe modulo n (n ≡ 1 mod 4) ⟹ pas de Venn symétrique dont le complément est une symétrie (parité de C(n, 2)) | pas de transformation entre les deux 17 ; la réciproque est ouverte (19, 23 : non exclu, non construit) ; la part de régions non monotones ne suit pas n mod 4 : 15,6 (11) ; 14,9 (13) ; 12,1 (17) ; 13,1 (19) ; 14,4 % (23) (calculé ici ; trop peu de diagrammes) | § 3.6, 3.4 |
| M1 | la face de 015 et l'ombre | exactement : fibre au-dessus de 0 ; deux faces se coupent en ∅ | le quart de tour 3 ≡ i ne préserve pas les faces ; (ℤ/b)* d'ordre pair n'est pas un groupe de Henderson | § 3.3 |
| M2 | les périodes de Gauss et les ombres | exactement : σ_h(ombre S) = ombre(hS), à 10⁻¹⁵ | pas une symétrie du dessin (la rotation est i ↦ i + 1) | § 3.5 |
| M3 | le nerf des chèvres et celui des dossiers | chèvres : convexité ; dossiers : 75 intersections sur 81 (v1), 130 sur 166 (v2) | 6 (v1) et 36 (v2) intersections non contractiles | § 3.2 |
| M4 | le gel du Venn et le cercle arctique | le rang est une hauteur (comme le pavage) | pas de bord, pas de loi, profil à pic (k/n ≈ 0,25) ; épaisseur 2 ou 3 | § 3.4 |
| M5 | le complément et la symétrie du diagramme | l'ombre : z ↦ −z | le diagramme : N_l ≠ N_(n−l), 18 sur 18 ; au sens fort, C(n, 2) doit être impair : exclu à 17 | § 3.6 |
| M6 | la texture, l'octaèdre, les droites au hasard | non | la part de triangles dérive : 35,95 ; 35,76 ; 35,12 % | § 6.1, NF4 |

**Le cocycle** (plan, § 3.3). Rotation et complément commutent : ℤ/n × ℤ/2 agit sur le cube et sur l'ombre (K2). La multiplication par h ∈ (ℤ/n)* ne commute pas avec la rotation : le groupe qui agit sur les étiquettes est affine, ℤ/n ⋊ (ℤ/n)*, et seul ℤ/n × ℤ/2 est géométrique. C'est ce qui sépare M2 (Galois) de K2.

## 6. Les trous

### 6.1 Les trous du recueil : sept fiches nouvelles (non révisées)

| n° | titre | type ; statut | partie ; script ; image | dim. | observation |
|---|---|---|---|---|---|
| NF1 | Les périodes de Gauss du 17-gone sont les ombres Σωⁱ des régions fixées par un sous-groupe de (ℤ/17)* | Analogie ; exact | XXVIII § 3.6 (résultats § 3.4), XXIX § 5.4 ; `octaedre_perron_venn.py` § 3, `venn_ppm.py` § 5 ; `ad2_deux_ombres.png` (c) | D6 (D2) | § 3.5 |
| NF2 | La face choisie par a mod 3 est la fibre de l'ombre au-dessus de 0 ; 3 est le seul premier qui coupe deux coordonnées | Analogie ; exact | recueil (fiche 015) ; `recueil_verifications.py` § 6 ; — | D2 (D6) | § 3.3 : 0 motif hors de sa face ; la roue modulo 30 |
| NF3 | Le premier rang non monotone d'un Venn de Dzoba vaut 2 ou 3 de 11 à 19 courbes (au plus 2 ou 3 à 23) | Corrélation ; calculé | XXIX § 5.3 ; `venn_ppm.py` § 6 ; `ad1_venn_ppm.png` (c) | D6 (D7) | § 3.4 ; les six à 23 : 2 ou 3 (constante) ou 4 (proportionnelle) : à calculer |
| NF4 | La part des triangles dérive avec n : 35,95 ; 35,76 ; 35,12 % à 17, 19 et 23 courbes | Coïncidence ; Corrélation ; à tester | XXIX § 2.2 ; `venn_ppm.py` § 2 ; `ad1_venn_ppm.png` (d) | D6 (D7) | calculé ici : de 35,28 à 36,74 % (4 Venn à 17), de 35,56 à 36,09 % (12 à 19) ; à 23, cinq comptes du README : 35,01 à 35,18 %, moyenne 35,118 ± 0,030, à 0,7 σ de 35,0959 % ; f4 : 35,0958 % (4,8 ppm de la cible, 14 régions sur 2,9 millions : environ 1 % pour cinq diagrammes, donc du hasard). Étalon possible (de mémoire, à vérifier) : les cellules de droites au hasard (Miles 1964), 35,51 % de triangles (2 − π²/6), variance des côtés 0,935 ; les Venn : 0,985 (17), 0,958 (19) (calculé ici) ; ma simulation est biaisée. Test : l'histogramme complet des six certificats à 23 (à calculer) |
| NF5 | Un Venn simple dont le complément est une symétrie est antipodal ; il exige C(n, 2) impair, donc n ≡ 2 ou 3 (mod 4) : impossible à 17, non exclu à 19 et 23 | Analogie ; exact (l'obstruction) ; ouvert (19, 23) | XXX § 3, 9 ; `centre_venn.py` § 2–3 ; `ae1_centre_moitie.png` (f), `ae2_diaphragmes_diffraction.png` (b) | D6 (D2) | § 3.6 : quotient en n courbes unilatères du plan projectif, parité des croisements ; pour n premier, −1 n'est pas un carré modulo n ; le demi-tour « miroir + complément » reste possible |
| NF6 | ‖u‖₁·‖u‖∞ ≥ 1 : le seuil des 2n chèvres est la plus grande ombre du cube | Analogie ; exact | XXVII § 4, XXII § 3 ; `carte_connexions.py` § 4 ; `ab3_liens_predits.png` (b, c) | D6 (D1) | égalité sur les 26 directions ; marge ≈ √n (1/x₀ = n + 4/3 − … contre √n). En v1, sans la fiche 010, `corde` et `ombres` n'ont aucune fiche commune |
| NF7 | Le nerf d'un recouvrement ne lit l'espace que si les intersections sont contractiles : 75 sur 81 (v1), 130 sur 166 (v2) pour les dossiers | Analogie ; Corrélation ; calculé | XX § 3 (le procédé) ; `revision_001.py` § 3 (code au § 7) ; `rev001_perron_venn.png` (a) | D7 (D6) | § 3.2 : six échecs (trois à deux morceaux, trois boucles) ; le nerf (1, 0, 4) contre la réunion (1, 4, 3) ; v2 : (1, 0, 1) contre (1, 0, 9, 1) |

### 6.2 Les trous du corpus

- **Les phrases à nuancer.** XXIX § 5.3 : « épaisseur constante » repose sur une ligne par taille, et « pas de cercle arctique macroscopique » compare un poids binomial à une aire (§ 3.4). XXIX § 2.2 : « la texture ne dépend presque pas de n » vaut de 11 à 19 (35,3 à 37,3 % de triangles), mais les cinq comptes à 23 courbes (35,01 à 35,18 %) sont sous toutes les valeurs à 17 et 19 (NF4).
- **XXI § 1** (70², η(24τ), Δ) n'a aucun lien avec le cube ; le dossier garde XXI pour son § 4.
- **Le plan** : la branche Perron de P1 part de V § 3, mais V n'est pas dans les parties de `ombres-cube-venn` (§ 8).
- **XXVIII § 3.5** demande si un Venn lu le long d'un rayon a la structure de Perron : XXIX § 5.1 répond « en couches, non » pour l'image ; le cas général reste ouvert.
- **XXX § 3 (« ce qui reste ouvert ») et § 9** : un Venn simple, symétrique et symétrique par le complément, à 17 courbes, n'existe pas au sens fort (parité, § 3.6) ; à 19 courbes la question reste entière.

### 6.3 Les trous des données publiées (dépôt `dzoba/venn17`, CC BY 4.0)

- **Publié** : 24 certificats (11, 13, quatre à 17, douze à 19 dans l'arbre ; six à 23, 889 Mo chacun, sur Zenodo) ; la transcription du vérificateur ; le nombre de régions non monotones ; des formes canoniques sur 4n étiquetages (rotation, miroir, échange des pôles) ; une preuve Lean par taille ; le code de recherche et son journal.
- **Non publié** (README, `verify/RESULTS*.md`) : la moitié des croisements, les croisements par niveau N_l ; la symétrie par le complément (l'échange des pôles ne sert qu'à comparer deux diagrammes) ; le profil des défauts par rang ; l'histogramme complet des degrés (cinq comptes de triangles à 23) ; l'ordre de dessin, la palette et le code de rendu des images à 17 courbes (le traceur n'a que les modes `tutte` et `level`, sans « pression » ni « rose ») ; la loi de la marche.

*Où chercher.* L'archive Zenodo (10.5281/zenodo.23189412) pour les six certificats à 23 courbes (lecture en flux : k₁, N_l, degrés) ; `search/README.md` pour le journal ; `paper/venn17-19.tex`. *Un test à faire à 23* : la symétrie par le complément (N_l = N_(n−l)) et la forme canonique avec et sans échange des pôles.

*Références.* **Sûres** : D. W. Henderson, *Amer. Math. Monthly* 70 (1963), 424–426 ; J. Griggs, C. E. Killian, C. D. Savage, *Electron. J. Combin.* 11 (2004), R2 ; F. Ruskey, M. Weston, « A survey of Venn diagrams », *Electron. J. Combin.*, DS5 ; B. Grünbaum, *Math. Magazine* 48 (1975), 12–23 ; R. Kenyon, A. Okounkov, *Acta Math.* 199 (2007), 263–302 ; K. Borsuk, *Fund. Math.* 35 (1948), 217–234 ; A. Hatcher, *Algebraic Topology* (2002), cor. 4G.3 ; G. H. Hardy, J. E. Littlewood, *Acta Math.* 44 (1923), 1–70 ; Gauss, *Disquisitiones arithmeticae* (1801). **À vérifier** : C. Dzoba, arXiv:2609.26546 et DOI Zenodo 10.5281/zenodo.23189412 (identifiants lus dans `README.md` et `CITATION.cff`, non vérifiés en ligne) ; Bultena, Grünbaum, Ruskey (monotonie, 1999) ; Mamakani et Ruskey (11 et 13 courbes) ; Brenner, Gregor, Mütze, Verciani (2026, cité par le README) ; R. E. Miles, *PNAS* 52 (1964), 901–907 et 1157–1160 ; P. Pritchard, *Acta Inform.* 17 (1982), 477–485 ; « polar symmetric » chez Ruskey et Weston (à lire avant NF5).

## 7. Le code minimal du test qui me concerne (T1 prolongé)

T1 existe déjà dans `scripts/revision_001.py`. Ce qui s'y ajoute : (a) le test « les intersections sont-elles contractiles ? » (§ 3.2) ; puis trois contrôles qui donnent les nombres du § 3 : (b) un certificat de Dzoba (§ 3.4, 3.6, 4), (c) la fiche 015 (§ 3.3), (d) Gauss (§ 3.5). Testé hors dépôt (2,8 s pour `__main__` ; 3 s par certificat à 19 courbes ; les 18 : `resume` sur chaque `.json` de `DZ`, 35 s). Chemins en tête, lecture seule.

```python
import itertools, json, os, re, collections
import numpy as np
# `nerf` et `betti_rapide` : à reprendre tels quels de scripts/revision_001.py (script plat, sans __main__ : l'importer le relancerait en entier)
REP, DZ = "/home/user/Graphite/chevre-optique", "/home/user/dzoba/venn17/certificates"   # lecture seule

def romain(s):
    v = {"I": 1, "V": 5, "X": 10, "L": 50}
    return sum(-v[c] if i + 1 < len(s) and v[s[i + 1]] > v[c] else v[c] for i, c in enumerate(s))

def renvois(nmax=30):   # les paires de parties qui se citent : la construction de carte_connexions.py (178 paires pour nmax = 26)
    num = {}
    for f in sorted(os.listdir(REP)):
        if f.endswith(".md") and f != "CLAUDE.md":
            m = re.match(r"# Partie ([IVXL]+)", open(f"{REP}/{f}").readline())
            if m or f == "README.md":
                num[f] = romain(m.group(1)) if m else 1
    motif = re.compile(r"[Pp]arties? ((?:[IVXL]+(?:,\s*|\s+et\s+|\s+à\s+|\s*–\s*)?)+)")
    paires = set()
    for f, n in num.items():
        txt = open(f"{REP}/{f}").read()
        for m in motif.finditer(txt):
            r = re.findall(r"[IVXL]+", m.group(1))
            cibles = range(romain(r[0]), romain(r[1]) + 1) if len(r) == 2 and re.search(r"\sà\s|–", m.group(1)) else map(romain, r)
            paires |= {tuple(sorted((n, c))) for c in cibles if 1 <= c <= nmax and c != n}
        paires |= {tuple(sorted((n, num[g]))) for g in re.findall(r"\]\(([a-z0-9-]+\.md)", txt) if g in num and num[g] != n}
    return paires

def drapeaux(S, adj):   # complexe de drapeaux induit sur S (clés 0, 1, … ; la dernière est vide)
    F, k = {0: [(s,) for s in sorted(S)]}, 0
    while F[k]:
        F[k + 1] = [c + (s,) for c in F[k] for s in sorted(S) if s > c[-1] and all(s in adj[x] for x in c)]
        k += 1
    return F

def test_nerf(sans=(), fichier="plan-001.md", apres="### 1.9"):  # (a) les intersections de dossiers sont-elles contractiles ?
    t = open(f"{REP}/recueil/revisions/{fichier}").read(); t = t[t.index(apres):]       # le premier bloc JSON après `apres`
    P = {d: {romain(x) for x in v["parties"]} - set(sans)
         for d, v in json.loads(re.search(r"```json\n(.*?)\n```", t, re.S).group(1))["dossiers"].items()}
    pr = renvois()
    adj = {i: ({b for a, b in pr if a == i} | {a for a, b in pr if b == i}) - set(sans) for i in range(1, 31) if i not in sans}
    inter, U = {}, collections.defaultdict(set)
    for r in range(1, len(P) + 1):
        for I in itertools.combinations(sorted(P), r):
            S = set.intersection(*(P[d] for d in I))
            if S:   # (Betti de l'intersection, a-t-elle un sommet-cône ?)
                inter[I] = (betti_rapide(drapeaux(S, adj)), any(all(y in adj[x] for y in S if y != x) for x in S))
    for S in P.values():
        for k, v in drapeaux(S, adj).items():
            U[k] |= set(v)
    mauvais = {I: b for I, (b, c) in inter.items() if not (b[0] == 1 and not any(b[1:]))}
    print(fichier, sans, len(inter), "intersections,", len(inter) - len(mauvais), "acycliques,", sum(c for _, c in inter.values()), "avec cône ; nerf",
          betti_rapide(nerf(P, 7)), "; réunion", betti_rapide({k: sorted(U[k]) for k in sorted(U)}))
    for I, b in mauvais.items():
        print("  échec :", I, b)

def resume(chemin):     # (b) un certificat de Dzoba (JSON seulement)
    d = json.load(open(chemin)); n = d["n"]; N = 2 ** n
    F = np.array([[int(s[::-1], 2) for s in f] for f in d["faces"]], dtype=np.int64)   # étiquettes LSB d'abord
    w = sum((np.arange(N) >> i) & 1 for i in range(n))                                 # rang d'une étiquette
    haut, bas = np.zeros(N, bool), np.zeros(N, bool)
    for a, b in itertools.combinations(range(4), 2):
        x, y = F[:, a], F[:, b]; z = x ^ y; ok = (z != 0) & ((z & (z - 1)) == 0)       # un seul bit change : un arc
        x, y = x[ok], y[ok]; bas_x = w[x] < w[y]
        haut[np.where(bas_x, x, y)] = True; bas[np.where(bas_x, y, x)] = True
    nm = ~(haut & bas) & (w > 0) & (w < n)                                             # non monotone (Bultena, Grünbaum, Ruskey)
    rang = np.bincount(w[nm], minlength=n + 1)
    Nl = np.bincount(np.minimum.reduce([w[F[:, i]] for i in range(4)]) + 1, minlength=n + 1)   # croisements par niveau
    var, cd = np.bitwise_or.reduce(F, 1) & ~np.bitwise_and.reduce(F, 1), {}                  # var : les deux bits des courbes qui se croisent
    for v, c in zip(*np.unique(var, return_counts=True)):                                      # c_d : croisements d'une paire à distance d
        i, j = [b for b in range(n) if int(v) >> b & 1]; cd.setdefault(min((j - i) % n, (i - j) % n), set()).add(int(c))
    return dict(n=n, k1=int(np.argmax(rang > 0)), k2=int(n - np.argmax(rang[::-1] > 0)), non_monotones=int(nm.sum()),
                triangles=round(100 * float((np.bincount(F.ravel(), minlength=N) == 3).mean()), 3), ecart_polaire=int(np.abs(Nl - Nl[::-1]).max()),
                c_d=[sorted(c) for _, c in sorted(cd.items())])

def dizaines(N=10 ** 6):  # (c) fiche 015 : motifs hors de leur face ; {1,7} et {3,9} selon a mod 3
    c = np.ones(N + 1, bool); c[:2] = False
    for p in range(2, int(N ** .5) + 1):
        if c[p]:
            c[p * p::p] = False
    U, a = (1, 3, 7, 9), np.arange(1, N // 10)
    m = sum(c[10 * a + u].astype(int) << i for i, u in enumerate(U))                   # bit i : 10a + U[i] est premier
    hors = sum(int(((m[a % 3 == r] >> i) & 1).sum()) for r in range(3) for i, u in enumerate(U) if (r + u) % 3 == 0)
    return hors, np.bincount((a % 3)[m == 5], minlength=3).tolist(), np.bincount((a % 3)[m == 10], minlength=3).tolist()

def gauss(n=17):        # (d) les périodes de Gauss sont des ombres Σ ω^i
    ombre = lambda S: sum(np.exp(2j * np.pi * i / n) for i in S)
    H4, QR = sorted({pow(4, k, n) for k in range(4)}), sorted({k * k % n for k in range(1, n)})
    return H4, abs(ombre(QR) - (-1 + n ** .5) / 2), abs(np.polyval([1, 1, -6, -1, 1], ombre(H4).real))

if __name__ == "__main__":
    for f, a in (("plan-001.md", "### 1.9"), ("verification-croisee-001.md", "")):   # recouvrement v1, puis v2
        test_nerf(fichier=f, apres=a); test_nerf(sans=(1,), fichier=f, apres=a)      # avec la partie I, puis sans
    print([resume(f"{DZ}/{c}.json") for c in ("best11-s0", "venn17-gcp-s12")], dizaines(), gauss())
```

**Sorties** (calculé ici). (a) v1 avec la partie I : 81 intersections, 76 acycliques, 70 avec cône, nerf (1, 0, 4), réunion (1, 3, 4) ; sans elle : 75, 67, (1, 0, 4), (1, 4, 3), et les six échecs du § 3.2. v2 : 166, 135, 117, (1, 0, 1), (1, 0, 10, 1) ; sans la partie I : 130, 112, (1, 0, 1), (1, 0, 9, 1). (b) `best11-s0` : k₁ = 2, 319 non monotones, 35,986 % de triangles, écart polaire 132, c_d = 44, 38, 34, 46, 24 ; `venn17-gcp-s12` : 3, 16 592, 36,005 %, 1 275, c_d = 1 228, 1 122, 1 070, 968, 844, 884, 834, 760 (sommes 186 et 7 710). Sur les 18 : un seul c_d par distance, somme (2ⁿ − 2)/n, jamais tous ≡ 2 (mod 4). (c) 0 motif hors de sa face ; {1, 7} : [2 700, 1 508, 0] ; {3, 9} : [0, 1 489, 2 727]. (d) ⟨4⟩ = [1, 4, 13, 16], résidus de l'ordre de 10⁻¹⁵.

## 8. Les corrections au recouvrement (bloc JSON du § 1.9 du plan)

```json
{
  "revision": "001",
  "dossiers": {
    "ombres-cube-venn": {
      "parties": ["II", "V", "XV", "XX", "XXI", "XXII", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"],
      "fiches": ["003", "004", "005", "006", "008", "009", "015"]
    }
  }
}
```

- **Ajouter la partie V.** La branche Perron de P1 (plan, § 2.2) part de V § 3 (2/(k + 2)), que XXVIII § 2.4 démontre par l'ombre du cube ; le § 1.7 et le JSON du § 1.9 l'omettent. Le nerf au niveau 3 ne change pas (1, 0, 5), calculé ici.
- **Retirer la fiche 010.** Exacte, mais de P2 : sa part de 39,34 % n'est vraie que du cercle du bord (`corde` § 4.1, `moities` § 4.2), un cas de XXV § 1.5, et le Venn n'y sert que de dessin. Effet sur le nerf des fiches (calculé ici ; niveau 3 inchangé). En v1 : 18 → 17 arêtes (corde et ombres n'ont plus de fiche commune), 7 → 6 triangles, 9 → 8 triangles vides ; le triangle bases · corde · ombres disparaît parce que l'arête manque, le trou s'agrandit sans se fermer, et la fiche NF6 rétablirait l'arête. En v2 : les arêtes restent (fiche 003), mais le triangle corde · moitiés · ombres, que 010 était seule à remplir, s'ouvre : 26 → 25 triangles, 10 → 11 triangles vides, b₁ 2 → 3. Le plan (§ 3.3) veut ce triangle rempli (le cercle R/√2, cocycle de P2) : la fiche 010 cachait ce trou du recueil ; il demande une fiche du cercle R/√2, pas la 010.
- **Garder** 003 et 009 (K2), 004 et 005 (rameaux de hasard, que le nerf doit voir), 006 et 008 (le dipôle, le point fixe) ; XXI, pour son § 4.
