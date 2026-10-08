# Dossier moities-et-crans : la moitié et le cran √2

Dossier de la révision 001, écrit par l'agent « moities » (phase 1 du workflow). Il suit le gabarit du plan (`recueil/revisions/plan-001.md`, § 7, clé `gabarit.phase_1`) et répond aux sept questions de son entrée. Les huit sections du gabarit sont les § 1 à § 8.

**Comment lire.** Chaque affirmation porte une étiquette.
- **démontré** : la preuve est donnée ici ou citée.
- **calculé** : un script du dépôt l'a sorti (je cite le fichier de résultats et sa section). **Calculé ici** : un calcul rapide fait pour ce dossier, hors du dépôt, que le script de la révision peut reprendre (§ 7).
- **classique** : théorème connu, avec référence (§ 6.3).
- **ma lecture** : mon interprétation, à tester.
- **ouvert** : on ne sait pas.

Les chemins sont relatifs à `/home/user/Graphite/chevre-optique` et ont tous été vérifiés avec `ls`. Les certificats de Dzoba (`/home/user/dzoba/venn17/certificates/`, CC BY 4.0) ont été lus comme des données : aucun code externe n'a été lancé. Aucun script du dépôt n'a été lancé non plus ; j'ai seulement relu `resultats/revision_001.md`, écrit pendant mon travail.

## En bref

- **Lien 1.** Un seul cercle, R/√2, est fixé par trois gestes différents : le miroir d'aire u ↦ 1 − u (le complément, XXX § 3), l'inversion des jumeaux d·d′ = ½ (XVII § 3) et la dilatation d'un cran u ↦ u/2 (I § 6.4). Archimède l'avait déjà posé : la tranche de l'hémisphère et celle du cône conjugué se croisent à z = R/√2 (II § 1).
- **Lien 2.** La moitié par équation devient la moitié par involution quand n tend vers l'infini. Le défaut est le plan de la lentille, x₀ = 1/(n + 4/3 − …) ; la corde tend vers √2 ; les deux parts mesurées s'écartent de ½ en miroir, de ∓ 1/√(2πn).
- **Lien 3.** Le tableau du grain (XXIII § 4) est déjà le tableau des procédés : l'équateur est l'involution, la coquille est la dilatation (ε = 1 − 2^(−1/n), la fin du plateau de XVI § 3), le plan est l'équation. La FTM50 en dimension n (calculée ici) est la ligne « équateur ».
- **Obstruction.** La moitié de Kakeya fini vient de l'inclusion–exclusion (Bonferroni, ordre 2), pas de l'involution : la piste XIV–XX se ferme. L'involution ne compte que l'excès, (q − 1)/2 pour q impair.
- **Trous.** (1) La fiche 005 reste sans cause. Aucun des 18 certificats n'est symétrique par le complément, mais « miroir + complément » arrive en tête dans les 18, à 1,5 à 2,3 fois le hasard. (2) La FTM50 en dimension n, l'aire de Perron à deux rapports et la corde du carré à coins coupés n'avaient aucun script. (3) Pour Kakeya fini avec q pair, les sources existent probablement (Blokhuis et Mazzocca ; Blokhuis, De Boeck, Mazzocca et Storme), mais je n'ai pu lire que des extraits : la preuve du § 5.4 n'est sans doute pas nouvelle (§ 6.3).
- **Recouvrement.** Ajouter les parties VI, X, XV, XVI, XIX, XXIII, XXV, XXVIII et la fiche 012 ; ne rien retirer (§ 8).

## 1. La question directrice et la projection sur D1–D8

### 1.1 La question

> Toutes les moitiés du corpus viennent-elles de quelques procédés seulement (une involution sans point fixe, une dilatation d'un cran, une équation, une inclusion–exclusion) ? Où ces procédés se rejoignent-ils : au rayon R/√2, à la corde √2 ?
>
> (plan, § 1.2)

### 1.2 Ma réponse, en six points

1. **Un seul problème, trois façons de le résoudre.** Couper en deux par un seuil, c'est chercher une médiane : le x* tel que F(x*) = ½, où F(x) est la part de la mesure dans la région A(x) (le disque de corde x, la tranche de demi-largeur x, la boule de rayon x). C'est toujours l'équation F(x*) = ½. L'involution et la dilatation sont les deux cas où l'on connaît F d'avance, donc où l'on résout sans calcul. *(ma lecture)*
   - **Involution.** Une symétrie σ qui garde la mesure et envoie A(x*) sur le complément de A(x*). Alors F(x*) = ½ exactement, parce que μ(A) = μ(σA) = μ(complément de A). L'ensemble fixe de σ est vide (le complément S ↦ S^c des régions, l'antipode) ou de mesure nulle (un hyperplan, un cercle, un point).
   - **Dilatation.** Une mesure homogène, F(λr) = λⁿ F(r). Alors F(x) = xⁿ et x* = 2^(−1/n). Le « cran » est le cas n = 2 : 1/√2.
   - **Équation.** F quelconque (la lentille d'Ullisch, l'énergie d'Airy). On résout F(x) = ½.
2. **Les trois se rejoignent à deux endroits exacts** (§ 3.2 et § 3.3) : au cercle R/√2, où le miroir d'aire et la dilatation d'un cran ont le même point u = ½ ; et à la corde √2, où l'équation de la chèvre devient l'involution d'un hémisphère quand n tend vers l'infini.
3. **Une seule courbe les contient** : la courbe des 50 % de la partie I. Plateau de dilatation (k = 2^(−1/n)) jusqu'à d₀ = 1 − 2^(−1/n), puis équation, puis, à l'infini, l'hyperbole ρ² = d² + 1 (I § 4.2 ; XVI § 1 et § 3).
4. **Une moitié n'est pas toujours une médiane.** Le deltoïde (π/8), l'arbre de Perron à 4 branches (½), la demi-case de Pick et Kakeya sur une grille finie sont des rapports d'aires ou des bornes. Ils n'ont pas de procédé commun (XIV § 7 le disait ; § 3.2 le range). Un seul a un procédé propre : Kakeya fini, par l'inclusion–exclusion.
5. **Les crans** : un seul nombre (√2), une seule unité (le logarithme en base √2), plusieurs mécanismes (§ 3.4).
6. **Une moitié reste sans cause** : celle de la fiche 005 (§ 4.1).

### 1.3 La projection sur D1–D8

Ma lecture, calculée sur l'inventaire du § 3.1 : une ligne de l'inventaire compte pour 1/35, rangée sur sa dimension principale. Les parts sont arrondies à 0,05. Le poids D7 est ajouté à la main : c'est la part du dossier qui teste un hasard (fiche 005, § 4.1).

| dimension | plan (§ 1.10) | après lecture | lignes de l'inventaire | ce qui y vit |
|---|---:|---:|---|---|
| D1 la chèvre et les cordes | 0,40 | 0,30 | 11 sur 35 : 1, 2, 3, 10, 11, 12, 13, 19, 21, 23, 25 | Ullisch, √2, le plateau, la corde de la moitié |
| D6 sphères, cubes, Venn et symétries | 0,30 | 0,30 | 11 sur 35 : 7, 8, 9, 20, 26, 28, 30, 31, 32, 33, 34 | le complément, les hémisphères, les cercles arctiques, le Venn |
| D3 grain, pixels et précision | 0 | 0,15 | 5 sur 35 : 18, 24, 27, 29, 35 | les crans comme unité d'échelle, le grain |
| D4 optique et diffraction | 0,20 | 0,10 | 4 sur 35 : 4, 5, 6, 22 | FTM50, Airy, éclipse, le cran du diaphragme |
| D5 Kakeya, Perron et aiguilles | 0,10 | 0,10 | 4 sur 35 : 14, 15, 16, 17 | deltoïde, Perron, Pick, Kakeya fini |
| D7 hasard et méthode | 0 | 0,05 | aucune ligne principale | la fiche 005 et ses tests |
| D2, D8 | 0 | 0 | aucune | rien de principal ; le point de Rayleigh (D8) est proposé en fiche (§ 6.1) |

Au format du plan (§ 1.10) : `"moities-et-crans": {"D1": 0.30, "D6": 0.30, "D3": 0.15, "D4": 0.10, "D5": 0.10, "D7": 0.05}`.

Ce qui change par rapport au plan : le plan rangeait les crans en D4. Dans l'inventaire, trois des lignes qui comptent en crans (27, 29 et 35) mesurent un grain : décades de précision, courbes d'un Venn, crans de f/1 à f/88. Elles sont en D3. D4 garde les moitiés d'optique (FTM50, Airy, éclipse) et le diaphragme.

## 2. Les chaînes de production

### 2.1 Partie par partie, dans l'ordre

Chaîne = document → script → résultats → figures. Je note « ajout » pour les parties que je propose d'ajouter au dossier (§ 8) et « à envisager » pour celles dont le lien est plus faible. Les lettres entre parenthèses sont les panneaux de la figure. La dernière ligne est le test T5 de la révision.

| partie | document | script : ce qu'il sort pour la moitié | résultats | figures |
|---|---|---|---|---|
| I | `README.md` § 2.2, 3, 4.2, 5.1, 6.3, 6.4 | `scripts/calculs.py` § 1 (β et r d'Ullisch à 40 chiffres), § 2 (cordes de la dimension n), § 4 (courbe des 50 %, plateau), § 6 (FTM50, Airy, éclipses) ; `scripts/chevre.py` § 1–2 (le quotient d'intégrales, les calottes) | `resultats/resultats.md` § 1, 2, 4, 6 | `figures/fig5_diagramme_parametres.png` (la courbe des 50 %), `figures/fig6_courbes50_dimensions.png`, `figures/fig7_optique.png` (a : FTM ; b : éclipse) |
| II | `archimede.md` § 1, 7, 8, 9 | `scripts/calculs_archimede.py` § 1 (hauteurs des demi-volumes), § 7 (cordes dans les solides), § 8 (le glissement à 50 %), § 9 (polygones) ; bibliothèque `scripts/archimede.py` § 1 et 3 | `resultats/archimede.md` § 1, 7, 8, 9 | `figures/b2_tranches_archimede.png` (a : tranches ; b : demi-volumes), `figures/b8_glissement_50.png`, `figures/b9_polygones_polyedres.png` (a) |
| IV | `trois-solides.md` § 4 | `scripts/trois_solides.py` § 4 (corde de la moitié depuis O, formes closes) | `resultats/trois_solides.md` § 4 | `figures/d1_trois_solides.png` (c) |
| V | `aiguille-kakeya.md` § 1–3 | `scripts/aiguille.py` § 1 (le deltoïde), § 2 (chèvre et triangle), § 3 (l'arbre de Perron, aire exacte) | `resultats/aiguille.md` § 1–3 | `figures/e1_aiguille_kakeya.png` (a, b, c) |
| VI (ajout) | `zone-confusion.md` § 3 (le simplexe : l'ordre 1), § 5 (la lunule d'Hippocrate) | `scripts/zone_confusion.py` § 3 et § 5 | `resultats/zone_confusion.md` § 3 et § 5 | `figures/f1_zone_confusion.png` |
| VIII | `foyer-fibonacci.md` § 3 | `scripts/foyer_fibonacci.py` § 3 (les deux ménisques de la FTM, s = 0,807946) | `resultats/foyer_fibonacci.md` § 3 | `figures/h1_foyer_menisques.png` (c) |
| X (ajout) | `carre-ptolemee.md` § 5 | `scripts/carre_ptolemee.py` § 4 (la corde de l'arc 70,8117°, la table de Ptolémée) | `resultats/carre_ptolemee.md` § 4 | `figures/j1_carre_ptolemee.png` |
| XIV | `aiguille-grille.md` § 3, 5, 7 | `scripts/aiguille_grille.py` § 3 (la demi-case), § 5 (Kakeya dans F_q², la parabole) | `resultats/aiguille_grille.md` § 3 et § 5 | `figures/n1_aiguille_grille.png` (d, f) |
| XV (ajout) | `grille-decalee.md` § 3 (la chèvre comptée) et § 6 (la table des valeurs : le deltoïde, Kakeya fini ; la FTM50 dans l'anneau de liens) | `scripts/grille_decalee.py` § 3 (la corde comptée sur la grille) | `resultats/grille_decalee.md` § 3 | `figures/o1_grille_decalee.png` |
| XVI (ajout) | `menisque-projection.md` § 1 et § 3 | `scripts/menisque_projection.py` § 1 (ρ² = d² + 1), § 3 (le plateau 2^(−1/n), exposant (n + 1)/2) | `resultats/menisque_projection.md` § 1 et § 3 | `figures/p2_menisque_projection.png` |
| XVII | `recursion-argent.md` § 1–3 | `scripts/recursion_argent.py` § 1 (le disque de demi-aire qui glisse), § 2 (les jumeaux), § 3 (la récursion) | `resultats/recursion_argent.md` § 1–3 | `figures/q1_recursion_argent.png` (a, b, c, f) |
| XVIII (à envisager) | `pixels-longitudes.md` § 5 | `scripts/pixels_longitudes.py` § 3–4 (la chèvre en pixels, bornes certaines) | `resultats/pixels_longitudes.md` § 3–4 | `figures/r1_pixels_contacts.png` |
| XIX (ajout) | `bases-objets.md` § 6 (le cône conjugué, le faisceau) | `scripts/bases_objets.py` § 4 | `resultats/bases_objets.md` § 4 | `figures/t2_trait_cone_thales.png` |
| XX | `sphere-faisceaux.md` § 1–3 | `scripts/sphere_faisceaux.py` § 1 (cordes certifiées, angle α_n), § 2 (part de la clôture), § 3 (faisceaux, les deux cartes) | `resultats/sphere_faisceaux.md` § 1–3 | `figures/u1_chevres_faisceaux.png` (b, c, e, f), `figures/u2_cartes_losange.png` (a) |
| XXI | `vingt-quatre-miroir.md` § 3 et § 5 | `scripts/vingt_quatre_miroir.py` § 2 (le doublement de l'aire, 6,644), § 4 (le croisement, le disque inscrit) | `resultats/vingt_quatre_miroir.md` § 2 et § 4 | `figures/v1_vingt_quatre.png` (f), `figures/v2_racine_sept.png` (d) |
| XXII | `carre-neuf-points.md` § 1 | `scripts/carre_neuf_points.py` § 1 (ρ_n par l'intégrale exacte, les décades) | `resultats/carre_neuf_points.md` § 1 | `figures/w1_carre_neuf_points.png` |
| XXIII (ajout) | `lentilles-boules-grain.md` § 4 et § 5 | `scripts/lentilles_boules_grain.py` § 4 (les quatre taux de change), § 5 (la part du cran) | `resultats/lentilles_boules_grain.md` § 4 et § 5 | `figures/x1_lentilles_boules_grain.png` (e, f) |
| XXIV | `tiers-dimension.md` § 1 et § 5 | `scripts/tiers_dimension.py` § 1 (la démonstration ; l'ordre 1 est le simplexe), § 5 (le facteur 2) | `resultats/tiers_dimension.md` § 1 et § 5 | `figures/y1_tiers_dimension.png` (e, f) |
| XXV (ajout) | `tranche-aiguilles.md` § 1.2 (la série de l'infini, resommée) | `scripts/tranche_aiguilles.py` § 1 (la resommation de Borel–Padé) | `resultats/tranche_aiguilles.md` § 1 | `figures/z1_ouverts.png` |
| XXVII | `carte-connexions.md` § 2, 3, 9 | `scripts/carte_connexions.py` § 2 (cercles arctiques), § 3 (échelle du grain, 6,644) | `resultats/carte_connexions.md` § 2 et § 3 | `figures/ab2_cercles_arctiques.png` |
| XXVIII (ajout) | `octaedre-perron-venn.md` § 2.2–2.4, 3.1–3.2 | `scripts/octaedre_perron_venn.py` § 2 (théorèmes de Perron), § 3 (Fermat, 7 710) | `resultats/octaedre_perron_venn.md` | `figures/ac2_perron.png`, `figures/ac3_venn17.png` |
| XXIX | `venn-ppm.md` § 3.3, 4, 5.2 | `scripts/venn_ppm.py` § 2 (niveaux, part ≥ 9), § 3–4 (une courbe = un cran) | `resultats/venn_ppm.md` § 2–4 | `figures/ad1_venn_ppm.png` (f), `figures/ad2_deux_ombres.png` (f) |
| XXX | `centre-venn.md` § 2–4, 7.3 | `scripts/centre_venn.py` § 2 (la moitié dans les 18 certificats), § 3 (la sphère, les deux miroirs), § 4 (diaphragmes, trois chèvres) | `resultats/centre_venn.md` § 2–4 | `figures/ae1_centre_moitie.png` (c à f), `figures/ae2_diaphragmes_diffraction.png` (a à d) |
| révision (T5) | `recueil/revisions/plan-001.md` § 4 (T5) | `scripts/revision_001.py` § 4.7 (le minimum de Kakeya dans F_q, q = 2 à 9) | `resultats/revision_001.md` § 4.7 | — |

### 2.2 Cinq chaînes qui se suivent

- **Chaîne A, l'équation.** I § 2–3 (Ullisch) → `scripts/calculs.py` § 1 → `resultats/resultats.md` § 1 → `figures/fig2_contour_ullisch.png` → `README.md`. Elle continue par XX § 1 (50 chiffres certifiés, toutes les dimensions), XXII § 1 (les décades), XXIV (la série) et XXV § 1.2 (la série resommée), et finit à la corde √2.
- **Chaîne B, la dilatation.** I § 4.2 et 6.4 (le cran, le plateau) → II § 1 (demi-volumes) → IV § 4 (depuis O) → XVI § 3 (2^(−1/n), où que soit le piquet) → XVII § 1 (le disque de demi-aire) → XXI § 3 (doubler l'aire) → XXIII § 4 (la coquille) → XXVII § 3 (6,644) → XXIX § 3.3 (une courbe = un cran) → XXX § 2.2 et 4.1 (12,91).
- **Chaîne C, l'involution.** II § 1 (le cône conjugué) → XVII § 3 (les jumeaux) → XX § 3 (les deux hémisphères d'aire ½, le changement de carte y ↦ y/|y|²) → XXX § 2.5 et 3 (le complément, les deux miroirs) → fiche 005.
- **Chaîne D, la grille finie.** XIV § 5 → T5 (`scripts/revision_001.py` § 4.7).
- **Chaîne E, les rapports d'aires.** V § 1 (le deltoïde) → V § 3 (Perron) → XIV § 3 (Pick) → XXVIII § 2.2–2.4 (Perron démontré).

Un fait de chaîne à noter. La table de II § 1 contient déjà les trois procédés : trois demi-volumes en dilatation (1/2, 1/√2, 2^(−1/3)), un en équation (la cubique de l'hémisphère) et la tranche qui se croise avec celle du cône conjugué (l'involution). Les parties suivantes les ont redécouverts un par un.

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 L'inventaire des moitiés (question 1)

35 lignes, dans l'ordre des parties. Les scripts sont dans `scripts/`, les résultats dans `resultats/`. « Exacte » veut dire : une valeur ou une preuve exacte (même quand un script la calcule en nombres). « Approchée » veut dire : une mesure, un comptage ou un écart connu.

| # | partie, § | ce qui est coupé en deux | valeur | script § → résultats § | exacte ou approchée | procédé | dim. |
|---:|---|---|---|---|---|---|---|
| 1 | I § 2.2 et 3 | la chèvre plane, piquet sur la clôture | β = 1,905695729309883894882666… ; r = 1,158728473018121517828234… | `scripts/calculs.py` § 1 → `resultats/resultats.md` § 1 ; certifiée à 10⁻⁵⁰ par `scripts/sphere_faisceaux.py` § 1 → `resultats/sphere_faisceaux.md` § 1 | exacte (nombre transcendant, README § 5.5) | équation | D1 |
| 2 | I § 5.1 et 5.5 | la chèvre en dimension n | n = 3 : racine de 3r⁴ − 8r³ + 8 = 0, r₃ = 1,2285448637… ; n = 10 : 1,349535 ; n = 100 : 1,407217 | `scripts/calculs.py` § 2–3 → `resultats/resultats.md` § 2–3 ; `resultats/sphere_faisceaux.md` § 1 | exacte | équation | D1 |
| 3 | I § 4.2 ; XVI § 3 ; XVII § 1 | le plateau : le disque de corde reste dans le pré | k = 2^(−1/n) jusqu'à d₀ = 1 − 2^(−1/n) : n = 2 : 0,7071 jusqu'à 0,2929 ; n = 3 : 0,7937 jusqu'à 0,2063 ; n = 10 : 0,9330 jusqu'à 0,0670 | `scripts/calculs.py` § 4 → `resultats/resultats.md` § 4 ; `scripts/menisque_projection.py` § 3 → `resultats/menisque_projection.md` § 3 ; `scripts/recursion_argent.py` § 1 → `resultats/recursion_argent.md` § 1 | exacte | dilatation | D1 |
| 4 | I § 6.4 ; VIII § 3 | la FTM50 : lentille = ménisque = π/2 pour deux disques égaux | ν = 0,4039727533 ν_c ; décalage s = 0,807946 | `scripts/calculs.py` § 6 → `resultats/resultats.md` § 6 ; `scripts/foyer_fibonacci.py` § 3 → `resultats/foyer_fibonacci.md` § 3 | exacte | équation (les deux ménisques sont échangés par x ↦ −x) | D4 |
| 5 | I § 6.4 | la tache d'Airy : 50 % de l'énergie | J₀² + J₁² = ½ en x = 1,68022474619 ; rayon 0,534832 λN | `scripts/calculs.py` § 6 → `resultats/resultats.md` § 6 | exacte (racine numérique) | équation | D4 |
| 6 | I § 6.3 | l'éclipse : 50 % de la surface du Soleil cachée | Lune/Soleil = 1 : d = 0,8079 R, magnitude 0,596 (c'est la ligne 4) ; rapport 0,92 : 0,7037 R, 0,608 ; rapport 1,05 : 0,8701 R, 0,590 | `scripts/calculs.py` § 6 → `resultats/resultats.md` § 6 | exacte | équation | D4 |
| 7 | II § 1 | le plan qui coupe un solide en deux volumes égaux (hauteur depuis la base) | cylindre 1/2 ; bol paraboloïde 1/√2 = 0,7071 ; cône pointe en bas 2^(−1/3) = 0,7937 | `scripts/calculs_archimede.py` § 1 → `resultats/archimede.md` § 1 | exacte | dilatation (volume proportionnel à h^e, e = 1, 2, 3) | D6 |
| 8 | II § 1 | le même plan pour l'hémisphère (= cylindre − cône) | z³ − 3z + 1 = 0, z = 2 cos 80° = 0,347296 (cas irréductible) | idem | exacte | équation | D6 |
| 9 | II § 1 ; XIX § 6 | la tranche de l'hémisphère contre celle du cône conjugué | π(1 − z²) et πz² : égales à π/2 en z = 1/√2 | idem ; `scripts/bases_objets.py` § 4 → `resultats/bases_objets.md` § 4 | exacte | involution z² ↔ 1 − z² | D6 |
| 10 | II § 8 | le disque de la moitié qui glisse | δ = 0,5658 : la corde commune passe par le piquet (arc de 180°) ; δ = 0,8079 : k = 1 | `scripts/calculs_archimede.py` § 8 → `resultats/archimede.md` § 8 | exacte | équation (famille de Kepler : ψ − sin ψ = (π/2)(1 + cos ψ)) | D1 |
| 11 | II § 9 | le carré (4 côtés) et l'octogone (8 côtés) circonscrits | même corde, 1,1656443249 | `scripts/calculs_archimede.py` § 9 → `resultats/archimede.md` § 9 | exacte | symétrie du conteneur (§ 3.2) | D1 |
| 12 | IV § 4 | la corde depuis O qui prend la moitié de chaque solide | hémisphère 2^(−1/n) ; en 2D, cylindre, cône et anneau : √(2/π) = 0,7978845608 ; en 3D : hémisphère 2^(−1/3), cylindre (3/4)^(1/3), cône ((2 + √2)/4)^(1/3), anneau 2^(−1/6) | `scripts/trois_solides.py` § 4 → `resultats/trois_solides.md` § 4 | exacte | dilatation | D1 |
| 13 | V § 2 | la corde égale au côté du triangle équilatéral de hauteur R | 49,7170 % du pré au lieu de 50 % | `scripts/aiguille.py` § 2 → `resultats/aiguille.md` § 2 | approchée (0,28 point d'aire ; 0,348 % sur la corde) | involution à l'ordre 1 (le simplexe, XXIV § 1) | D1 |
| 14 | V § 1 | le deltoïde de Kakeya | π/8 = ½ du disque de diamètre 1 | `scripts/aiguille.py` § 1 → `resultats/aiguille.md` § 1 | exacte | valeur de formule (2πa² contre 4πa²) | D5 |
| 15 | V § 3 ; XXVIII § 2.3–2.4 | l'arbre de Perron à 4 branches | aire ½ du triangle (rapports 1/√2 et 1/√2, ou 3/4 puis 2/3) | `scripts/aiguille.py` § 3 → `resultats/aiguille.md` § 3 ; `scripts/octaedre_perron_venn.py` § 2 → `resultats/octaedre_perron_venn.md` | exacte | minimum d'une parabole (§ 3.2) | D5 |
| 16 | XIV § 3 | la demi-case de Pick entre deux aiguilles voisines | aire ½ (déterminant ±1) | `scripts/aiguille_grille.py` § 3 → `resultats/aiguille_grille.md` § 3 | exacte | symétrie centrale du parallélogramme | D5 |
| 17 | XIV § 5 ; T5 | Kakeya sur la grille finie F_q² | q impair : q(q + 1)/2 + (q − 1)/2 points : 7, 17, 31 pour q = 3, 5, 7 (part du plan 0,778 ; 0,680 ; 0,633, puis ½) ; q pair : q(q + 1)/2 : 3, 10, 36 pour q = 2, 4, 8 | `scripts/aiguille_grille.py` § 5 → `resultats/aiguille_grille.md` § 5 ; `scripts/revision_001.py` § 4.7 → `resultats/revision_001.md` § 4.7 | exacte (Blokhuis–Mazzocca pour q impair ; Bonferroni et construction pour q pair, § 5.4) | inclusion–exclusion | D5 |
| 18 | XV § 3 ; XVIII § 5 | la moitié des points d'une grille ou des pixels | corde comptée 1,15884 (R = 100) ; 1,158734 (R = 1 000) ; 1,158728470 (R = 2¹⁷) ; encadrement certain de largeur ≈ 4,6/R | `scripts/grille_decalee.py` § 3 → `resultats/grille_decalee.md` § 3 ; `scripts/pixels_longitudes.py` § 3–4 → `resultats/pixels_longitudes.md` § 3–4 | approchée (écart du cercle de Gauss) | comptage | D3 |
| 19 | XVII § 3 ; VI § 5 | les jumeaux d·d′ = ½ et la lunule d'Hippocrate | point fixe d = 1/√2 (le petit disque coupe le pré à ±45°) ; lunule d'aire ½ ; part broutée 1/2 − 1/(2π) = 0,340845 | `scripts/recursion_argent.py` § 2 → `resultats/recursion_argent.md` § 1–2 ; `scripts/zone_confusion.py` § 5 → `resultats/zone_confusion.md` § 5 | exacte | involution d ↦ 1/(2d) ; l'aire de la lunule est une valeur de formule | D1 |
| 20 | XX § 3 | les deux hémisphères de toute sphère | chacun ½ de l'aire ; les deux cartes sont reliées par l'inversion (y ↦ y divisé par le carré de sa norme ; la projection depuis le pôle est l'inversion de rayon √2, qui fixe l'équateur) | `scripts/sphere_faisceaux.py` § 3 → `resultats/sphere_faisceaux.md` § 3 | exacte | involution (la réflexion de l'équateur, lue dans le plan par l'inversion) | D6 |
| 21 | XX § 1–2 ; XXII § 1 | la chèvre de dimension infinie | corde √2 ; angle α_n → 90° ; part de la clôture 0,3934 (n = 2), 0,3760 (n = 4, minimum), 0,4610 (n = 100), puis ½ | `scripts/sphere_faisceaux.py` § 1–2 → `resultats/sphere_faisceaux.md` § 1–2 ; `scripts/carre_neuf_points.py` § 1 → `resultats/carre_neuf_points.md` § 1 | exacte à la limite, calculée avant | l'équation devient l'involution (§ 3.3) | D1 |
| 22 | XXI § 3 | le cran : doubler l'aire | diamètre ×√2 ; le Ménon (le carré sur la diagonale) ; faisceau gaussien à la distance de Rayleigh (aire ×2, intensité ½) ; une décade = 6,644 crans | `scripts/vingt_quatre_miroir.py` § 2 → `resultats/vingt_quatre_miroir.md` § 2 | exacte | dilatation | D4 |
| 23 | XXI § 5 | le disque inscrit a la moitié de l'aire du disque circonscrit (au croisement du plan) | rayon 1/√2 ; c'est la position jumelle d'elle-même de XVII | `scripts/vingt_quatre_miroir.py` § 4 → `resultats/vingt_quatre_miroir.md` § 4 | exacte | dilatation et jumeaux | D1 |
| 24 | XXIII § 4 | le grain qui rend la dimension invisible | équateur ≈ 0,455/ε² ; coquille ≈ 0,693/ε ; plan 1/ε − 1 ; ménisque ≈ 0,577/√ε (à 10⁻⁵⁰ : 4,55·10⁹⁹ ; 6,93·10⁴⁹ ; 10⁵⁰ ; 5,77·10²⁴ dimensions) | `scripts/lentilles_boules_grain.py` § 4 → `resultats/lentilles_boules_grain.md` § 4 | exacte (lois), calculée (valeurs) | les trois à la fois (§ 3.2) | D3 |
| 25 | XXIV § 5 | le facteur 2 entre le plan et l'aire | r² = 2R(R − x₀) (Thalès, Euclide VI.8) : un cran | `scripts/tiers_dimension.py` § 5 → `resultats/tiers_dimension.md` § 5 | exacte | dilatation | D1 |
| 26 | XXVII § 2 | les cercles arctiques | le cercle inscrit du losange (rayon 1/√2) a la moitié de l'aire du disque circonscrit ; il couvre π/4 du losange | `scripts/carte_connexions.py` § 2 → `resultats/carte_connexions.md` § 2.4 | exacte (théorèmes cités) | dilatation | D6 |
| 27 | XXVII § 3 | la série de la chèvre | un cran (√2) par dimension ; 6,6439 dimensions par décade de grain | `scripts/carte_connexions.py` § 3 → `resultats/carte_connexions.md` § 3 | exacte | dilatation (le cran) | D3 |
| 28 | XXVII § 2.3 | les parts de dominos verticaux et la hauteur moyenne des cubes | ½ attendu par symétrie ; mesuré 0,465 à 0,516 (dominos), 0,493 à 0,534 (cubes) | `scripts/carte_connexions.py` § 2 → `resultats/carte_connexions.md` § 2.2–2.3 | approchée (tirage au hasard) | involution (échange des orientations ; boîte vide contre boîte pleine) | D6 |
| 29 | XXIX § 3.3 et 4 | une courbe de plus | double les croisements (2ⁿ − 2) : un cran (√2) de largeur d'image ; 1 bit par courbe en aire, ½ bit en longueur | `scripts/venn_ppm.py` § 3–4 → `resultats/venn_ppm.md` § 3–4 | exacte | dilatation (comptage binaire d'Euler) | D3 |
| 30 | XXIX § 5.2 ; XXX § 2.1–2.2 | le cercle de demi-aire R/√2 dans le Venn à aire égale | 49,935 % des croisements dedans (−649 ppm) ; 49,43 % de l'encre ; ½ par cran jusqu'au 6ᵉ | `scripts/venn_ppm.py` § 2 → `resultats/venn_ppm.md` § 2 ; `scripts/centre_venn.py` § 2 → `resultats/centre_venn.md` § 2 | approchée (budget de grain ±1 830 ppm) | dilatation (aire égale) et involution (complément) | D6 |
| 31 | XXX § 2.5 | la moitié des régions du Venn | 2^(n−1) régions de rang ≥ (n + 1)/2 : 65 536 pour n = 17 | `scripts/centre_venn.py` § 2 → `resultats/centre_venn.md` § 2 | exacte | involution libre S ↦ S^c | D6 |
| 32 | XXX § 2.5 et 7.3 ; fiche 005 | la moitié des croisements, Venn à 19 courbes | 262 143 de chaque côté (venn19-ramp12h-s192102) | `scripts/centre_venn.py` § 2 → `resultats/centre_venn.md` § 2 | exacte (entier) | aucun procédé connu (hasard testé : 1,6 %) | D6 |
| 33 | XXX § 3 | les deux miroirs du complément | miroir d'aire r² + r′² = R² ; inversion r·r′ = R²/2 ; le même cercle R/√2 | `scripts/centre_venn.py` § 3 → `resultats/centre_venn.md` § 3 | exacte | involution (le cercle fixe) | D6 |
| 34 | XXX § 4.3 ; fiche 010 | les trois chèvres du Venn | 50,0000 % des croisements chacune ; Ullisch : 39,34 % du niveau 1 | `scripts/centre_venn.py` § 4 → `resultats/centre_venn.md` § 4 | exacte (dessin à aire égale idéal) | dilatation (mesure proportionnelle à l'aire) et équation | D6 |
| 35 | XXX § 4.1 | les crans du bord à l'orbite centrale | log₂ 7 710 = 12,913 crans : de f/1 à f/87,8 | `scripts/centre_venn.py` § 4 → `resultats/centre_venn.md` § 4 | exacte | dilatation (comptage binaire) | D3 |

Les lignes 11, 14, 15, 16, 18, 24, 32 et 34 réunissent plusieurs moitiés ou demandent une explication : elles sont traitées au § 3.2.

### 3.2 Le classement par procédé, et les recollements (question 2)

**Le classement.** Chaque ligne a un procédé principal (colonne « procédé » du § 3.1).

| procédé | lignes | nombre | ce qui le reconnaît |
|---|---|---:|---|
| dilatation | 3, 7, 12, 22, 23, 25, 26, 27, 29, 30, 34, 35 | 12 | une mesure homogène : aire en r², volume en hⁿ, comptage en 2ⁿ |
| équation | 1, 2, 4, 5, 6, 8, 10, 21 | 8 | une fonction F quelconque, résolue par une racine ou par la division d'intégrales |
| involution | 9, 13, 16, 19, 20, 28, 31, 33 | 8 | une symétrie qui échange les deux moitiés |
| inclusion–exclusion | 17 | 1 | la borne de Bonferroni à l'ordre 2 |
| autre | 11, 14, 15, 18 | 4 | pas une médiane : chacune a sa raison |
| les trois à la fois | 24 | 1 | le tableau du grain |
| aucun connu | 32 | 1 | la fiche 005 |

**Deux sortes d'involutions.** *(démontré)*
- L'involution **libre**, sans point fixe : le complément S ↦ S^c sur les régions (ligne 31 : une région n'est jamais son propre complément) et l'antipode de la sphère (mon exemple : XX § 3 ne le nomme pas).
- L'involution dont l'ensemble fixe est de **mesure nulle** : U₁ ↦ −U₁ (l'hyperplan U₁ = 0), z² ↔ 1 − z² (le cercle z = R/√2, ligne 9), les jumeaux d ↦ 1/(2d) (le point d = 1/√2, ligne 19), la symétrie centrale de la demi-case (son centre, ligne 16), l'inversion r·r′ = R²/2 (le cercle R/√2, ligne 33), x ↦ −x dans F_q (le point 0 ; l'identité si q est pair).
- Le complément a les deux visages. Sur les régions du Venn, il n'a aucun point fixe. Comme geste sur la sphère dessinée, c'est la réflexion de l'équateur : elle fixe le cercle équatorial, qui ne coïncide avec aucune région. Les « deux miroirs » de XXX § 3 sont cette seule réflexion vue dans deux dessins : dans la projection de Lambert elle s'écrit r² + r′² = R² (θ ↦ π − θ), dans la projection stéréographique r·r′ = R²/2. *(ma lecture ; la vérification est une ligne de calcul : r = 2 sin(θ/2) donne r′ = 2 cos(θ/2).)*

**Les recollements.**

*R1. Au cercle R/√2, en toute dimension* *(démontré)*. Posons u = (r/R)ⁿ, la part de mesure dans la boule de rayon r (pour n = 2, c'est l'aire). La dilatation d'un cran envoie u ↦ u/2. Le miroir de mesure (le complément dans un dessin à mesure égale) envoie u ↦ 1 − u. Le point fixe du second est u = ½, et c'est l'image de u = 1 par le premier. Le cercle est donc à la fois « la moitié de la mesure » et « le point fixe du complément ». Son rayon est 2^(−1/n) R : R/√2 pour n = 2, 0,7937 R pour n = 3. La partie XXX § 3 le montre pour n = 2 ; l'extension à toute dimension est triviale, mais elle n'est écrite nulle part.
- Les mêmes lieux étaient déjà posés ailleurs. II § 1 : à z = 1/√2, la tranche de l'hémisphère et celle du cône conjugué valent toutes deux π/2, et le bol paraboloïde est coupé en deux à la même hauteur. XVII § 2–3 : le disque de rayon 1/√2 couvre ½ du pré, et sa position jumelle d'elle-même est d = 1/√2. XIX § 6 : le cercle z = r = 1/√2 enferme la moitié du disque. XXI § 5 : le disque inscrit a la moitié de l'aire du circonscrit. XXVII § 2.4 : le cercle arctique du losange. XXX § 3 : le complément.
- *Ce qui est transporté* : les 49,935 % des croisements et les 49,43 % de l'encre (ligne 30).
- *Ce qui reste ouvert* : un Venn simple et symétrique, aussi symétrique par le complément, qui rendrait la moitié des croisements exacte (§ 4.1).

*R2. À la corde √2.* L'équation de la chèvre de dimension n devient l'involution d'un hémisphère quand n tend vers l'infini. C'est la chaîne du § 3.3.

*R3. Le long de la courbe des 50 %* *(calculé)*. Plateau de dilatation jusqu'à d₀ = 1 − 2^(−1/n), puis équation. À la jonction, ρ − ρ₀ croît comme (d − d₀)^((n+1)/2) : exposant mesuré 1,509 en 2D (attendu 1,5), 1,999 en 3D (attendu 2), 2,993 en 5D (attendu 3) (`resultats/menisque_projection.md` § 3). À l'infini, c'est l'hyperbole ρ² = d² + 1, c'est-à-dire la médiane de |X − P| quand presque tout le pré est à l'angle droit (XVI § 1).

*R4. Dans le tableau du grain* *(démontré pour les trois premières lignes, calculé pour les valeurs)*. Le tableau de XXIII § 4 est le tableau des procédés :
- **équateur** : la tranche |x₁| < ε contient la moitié du volume. La loi de x₁ est symétrique : c'est l'involution x₁ ↦ −x₁. La médiane de |x₁| vaut 0,6745/√n (le quantile à 75 % de la loi normale), et 0,6745² = 0,455 : d'où n ≈ 0,455/ε² ;
- **coquille** : (1 − ε)ⁿ = ½. C'est la dilatation : ε = 1 − 2^(−1/n), **exactement la fin du plateau d₀ de XVI § 3** ; d'où n ≈ ln 2/ε = 0,693/ε ;
- **plan de la lentille** : x₀ = ε. C'est l'équation exacte ; d'où n = 1/ε − 1 ;
- **ménisque** : μ/2 = ε. C'est le défaut de l'équation (2/(3n²)) ; d'où n ≈ 0,577/√ε.
La ligne « équateur » est aussi la FTM50 en dimension n (nouvelle fiche, § 6.1) : la lentille de deux boules unité à la distance s vaut P(|Y₁| ≥ a), avec Y uniforme dans la boule et a = s/2 = ν/ν_c, donc la FTM50 est la médiane de |Y₁|.

**Ce qui ne se recolle pas, et pourquoi.**

*Les moitiés qui ne sont pas des médianes* (lignes 14, 15, 16, 17). XIV § 7 notait : « pas établi : un sens commun à toutes les moitiés (la chèvre, le deltoïde, la demi-case de Pick, le plan fini de Kakeya) ». Voici le tri :
- la **chèvre** est une médiane (équation) ;
- la **demi-case de Pick** est la moitié d'un parallélogramme : la symétrie centrale autour de son centre échange les deux triangles *(démontré)* ;
- le **deltoïde** : aire 2πa² (a = rayon du cercle qui roule, ici ¼) contre 4πa² pour le disque de diamètre 1, dont le rayon 2a = R − a est celui que décrit le centre du cercle qui roule. Le ½ vient des deux formules, pas d'une symétrie *(démontré, formule classique)* ;
- **Perron à 4 branches** : le minimum d'une parabole, voir ci-dessous ;
- **Kakeya fini** : l'inclusion–exclusion, voir § 5.4.
Trois procédés différents (symétrie centrale, formule, minimum) plus l'inclusion–exclusion : il n'y a pas de procédé commun à ces quatre. C'est le résultat, et il confirme le « pas établi » de XIV § 7 en le rangeant.

*Perron à 4 branches : l'aire ne dépend que du rétrécissement total* *(calculé ici, en fractions exactes)*. La partie V donne l'aire ½ pour deux rapports (1/√2 et 1/√2 ; 3/4 puis 2/3) et la formule ½ + 2(α² − ½)² pour deux rapports égaux. La partie XXVIII § 2.2 donne la borne « cœur + oreilles » F (l'aire est au plus F) ; le § 2.3 montre que F ≥ 2/(k + 2), avec égalité aux seuls rapports télescopiques. J'ai calculé l'aire exacte en fractions pour des rapports (α₀, α₁) rationnels :
- sur le segment α₀α₁ = ½, avec 3/5 ≤ α₀ ≤ 3/4, l'aire vaut exactement ½ (7 points rationnels testés : (3/5, 5/6), (5/8, 4/5), (13/20, 10/13), (2/3, 3/4), (7/10, 5/7), (5/7, 7/10), (3/4, 2/3)) ;
- dans une zone à deux dimensions autour de ce segment (276 des 576 points d'une grille de pas 0,02 entre 0,50 et 0,96), l'aire vaut P² + (1 − P)² = 2P² − 2P + 1, avec P = α₀α₁ le rétrécissement total. En fractions, un seul polynôme de degré total ≤ 4 redonne l'aire exacte sur les 49 points de la grille 0,67 à 0,73 : 2α₀²α₁² − 2α₀α₁ + 1 ;
- le point télescopique (3/4, 2/3) de Perron est sur le bord de la zone, à un coin d'après la carte ; le point symétrique (1/√2, 1/√2) est à l'intérieur, et la borne F y vaut 0,50736 (plus que l'aire) ; au point (3/5, 5/6), F vaut 0,59 et l'aire reste ½ ;
- hors de la zone, l'aire est plus grande (par exemple 322/625 = 0,5152 au point (4/5, 3/5)).
*Conséquence* : le √2 de V § 3 (« une vraie moitié, avec le √2 de la diagonale du carré ») n'est pas forcé. Le minimum ½ est atteint sur tout un segment, et 1/√2 n'en est que le point symétrique. *Lecture* : P² + (1 − P)² est la somme de l'aire du tronc (largeur P) et d'un terme (1 − P)² ; elle est symétrique par P ↦ 1 − P et minimale en son point fixe, avec la valeur ½. C'est une involution sur les largeurs (P ↦ 1 − P), pas sur les aires : elle ne se recolle pas au miroir d'aire u ↦ 1 − u. *Statut : exact en fractions sur plus de 50 points rationnels, démonstration générale à écrire.*

*Le carré à coins coupés* *(démontré, et calculé ici)*. II § 9 note que les polygones circonscrits à 4 et à 8 côtés donnent la même corde, 1,1656443249, et dit pourquoi : les coins retirés sont entièrement dans le disque de corde du côté du piquet, et entièrement dehors de l'autre côté. Je précise le mécanisme et la portée. Le carré [−1, 1]², le piquet en (1, 0). Couper les quatre coins à la profondeur t retire deux triangles proches (dedans) et deux triangles lointains (dehors) ; les deux paires ont la même aire t², parce que la réflexion x ↦ −x du conteneur échange les coins proches et les coins lointains. La part dedans et la part dehors perdent la même aire : la moitié ne bouge pas. Cela tient tant que les coins proches restent dans le disque de corde, c'est-à-dire pour t ≤ √(r₀² − 1) = 0,5989379702 avec r₀ = 1,1656443249. J'ai vérifié la corde pour t de 0 à 0,59 (1,1656443249 partout) ; l'octogone régulier circonscrit est t = 2 − √2 = 0,5858, à l'intérieur du plateau ; à t = 0,60, la corde vaut 1,1656441490. Ce n'est ni une dilatation ni une équation : c'est une symétrie du conteneur combinée à la séparation par le cercle (ligne 11).

*La fiche 005* (ligne 32) : aucun procédé connu (§ 4.1).

### 3.3 De l'équation à l'involution, quand n tend vers l'infini (question 3)

**Réponse : oui, et la chaîne est exacte.** Le cadre est celui de I § 5.3–5.4 et XXIV § 1 *(démontré)*. Un point X du pré s'écrit X = ρU : ρⁿ est uniforme sur [0, 1], U est uniforme sur la sphère S^(n−1), les deux sont indépendants. Le piquet est P = e₁, sur la clôture. Alors |X − P|² = ρ² + 1 − 2ρU₁. La chèvre de corde r (on pose m = r²) broute X exactement quand U₁ ≥ τ(ρ) = (ρ² + 1 − m)/(2ρ). La corde de la moitié est la médiane de |X − P|.

1. **L'involution est cachée dans l'équation** *(démontré)*. La loi de U₁ est symétrique : la réflexion U₁ ↦ −U₁ de la sphère garde la mesure, et son ensemble fixe (l'hyperplan U₁ = 0) est de mesure nulle. Si le seuil était 0, on aurait P(U₁ ≥ 0) = ½ exactement. C'est le cas sur la coquille ρ = 1 avec m = 2 : la corde √2 broute exactement un hémisphère de la clôture.
2. **Le défaut d'involution est le plan de la lentille** *(démontré)*. Sur la coquille extérieure, τ(1) = 1 − m/2 = x₀. Donc x₀ mesure l'écart entre le seuil et le centre de symétrie de U₁ ; il est nul si et seulement si la corde vaut √2. Valeurs *(calculé, `resultats/lentilles_boules_grain.md` § 2)* : 0,328674 (n = 2), 0,245339 (n = 3), 0,089377 (n = 10), 0,009871 (n = 100), 9,998667·10⁻⁵ (n = 10⁴).
3. **À l'ordre 1, l'équation est l'involution moyennée sur la loi de ρ** *(démontré, XXIV § 1)*. Sur toute la boule le seuil τ varie avec ρ. La médiane impose E[τ] = ½(E[ρ] + (1 − m)E[ρ⁻¹]) = 0 à l'ordre 1, c'est-à-dire que le seuil moyen tombe sur le centre de symétrie. Cela donne m = 2n/(n + 1), l'arête au carré du simplexe (VI § 3). La corde égale au côté du triangle équilatéral (ligne 13) est cet ordre 1 : elle broute 49,7170 % au lieu de 50 %.
4. **Ce que l'involution ne voit pas** *(démontré, XXIV § 1)*. L'ordre suivant est 2/(3n²) = 2 × 1/6 × 2 : la courbure de la densité de U₁ à l'équateur (k/3 ≈ n/6) fois l'asymétrie de la coquille (E = −n ln ρ suit exactement une loi exponentielle, et E[(1 − E)³] = −2). C'est le tiers de dimension : la corde de la dimension n est celle du simplexe de dimension n + 1/3, et 1/x₀ = n + 4/3 − 112/(45n) + …
5. **L'angle et la corde** *(calculé, `resultats/sphere_faisceaux.md` § 1 et `resultats/carre_neuf_points.md` § 1)*. α_n = arccos x₀ : 70,812° (n = 2), 75,798° (3), 78,698° (4), 83,738° (8), 87,731° (24), 89,434° (100), puis 90°. À 90°, la calotte {U₁ ≥ 0} est un hémisphère : la moitié de la clôture, par l'involution. Le carré de la corde, ρ_n², est le rapport entre l'aire du disque de la corde et celle du pré : 1,3427 (n = 2), 1,8212 (10), 1,9208 (24), 1,98026 (100), 1,998003 (1 000), 1,9998000 (10 000), puis 2. Chaque facteur 10 sur n ajoute un 9, parce que 2 − ρ_n² ≈ 2/n (plus exactement n(2 − ρ_n²) = 2 − 8/(3n) + …). Les disques de rayons 1/√2, 1 et √2 ont des aires ½, 1 et 2 : trois diaphragmes de suite. La corde de la chèvre infinie est un cran au-dessus du pré, comme le cercle de la moitié est un cran au-dessous. C'est là que les moitiés et les crans (§ 3.4) se touchent.
6. **Les parts** *(calculé)*. La part de la clôture broutée par la vraie corde (`resultats/sphere_faisceaux.md` § 2) : 0,3934 (n = 2), 0,3773 (3), 0,3760 (4, le minimum), 0,3900 (8), 0,4255 (24), 0,4610 (100), 0,4771 (300), puis ½. La part du volume broutée par la corde √2 : 68,2 % en 2D et 66,4 % en 3D (README § 5.3 ; `resultats/resultats.md` § 2, dernière colonne), puis ½. **Les deux s'écartent de ½ en miroir**, de ∓ 1/√(2πn) au premier ordre *(calculé ici)*. Raison *(ma lecture, d'après XXIV § 1)* : la densité de U₁ en 0 vaut √(n/(2π)). La clôture voit le décalage x₀ ≈ +1/n, le volume voit le décalage moyen de la coquille, −E[1 − ρ] ≈ −1/n.
7. **Deux vitesses** *(esquissé en I § 5.3, développé en XXIII § 4)*. La corde converge en 1/n : elle ne voit que le décalage moyen de la coquille. Les parts convergent en 1/√n : les fluctuations de l'équateur sont symétriques, elles se compensent dans la médiane mais pas dans la mesure.
8. **Le retour** *(calculé, XXV § 1.2)*. La série en 1/n, développée autour de la dimension infinie, resommée par Borel–Padé, redonne r₂² = 1,342651673575 pour 1,342651674183, la corde d'Ullisch. L'involution (n = ∞) et l'équation (n = 2) sont donc reliées dans les deux sens par un calcul exact. Cette partie est dans le dossier `corde-et-dimensions` ; je propose de l'ajouter ici (§ 8).

Les nombres, ensemble :

| n | x₀ | α_n | part de la clôture | part du volume (corde √2) | ½ − 1/√(2πn) |
|---:|---:|---:|---:|---:|---:|
| 2 | 0,328674 | 70,812° | 0,3934 | 0,6817 | 0,2179 |
| 3 | 0,245339 | 75,798° | 0,3773 | 0,6642 | 0,2697 |
| 4 | 0,195987 | 78,698° | 0,3760 | 0,6512 | 0,3005 |
| 8 | 0,109071 | 83,738° | 0,3900 | 0,6197 | 0,3590 |
| 24 | 0,039597 | 87,731° | 0,4255 | 0,5763 | 0,4186 |
| 100 | 0,009871 | 89,434° | 0,4610 | 0,5392 | 0,4601 |
| 1 000 | 0,000999 | 89,943° | 0,4874 | 0,5126 | 0,4874 |
| ∞ | 0 | 90° | ½ | ½ | ½ |

Source des colonnes : x₀ et α_n, `resultats/lentilles_boules_grain.md` § 2 et `resultats/sphere_faisceaux.md` § 1 ; part de la clôture, `resultats/sphere_faisceaux.md` § 2 (n = 2, 3, 4, 8, 24, 100) ; les autres valeurs (n = 1 000, part du volume, dernière colonne) sont *calculées ici* par l'intégrale exacte sur le rayon (la méthode de `scripts/carre_neuf_points.py` § 1). La prédiction ½ − 1/√(2πn) est asymptotique : mauvaise en n = 2, juste à 3·10⁻⁵ en n = 1 000. La part du volume vaut à peu près 1 moins la dernière colonne.

### 3.4 Les crans : un seul procédé ? (question 5)

**Réponse : une seule unité et un seul nombre, plusieurs mécanismes.** Le nombre est √2 = 1/sin 45° = 1/cos 45°. L'unité est le logarithme en base √2 sur les longueurs, c'est-à-dire en base 2 sur les aires *(démontré)*.

| cran | où | valeur | d'où vient le facteur 2 en aire | procédé |
|---|---|---|---|---|
| 6,644 par décade | XXI § 3 ; XXVII § 3 | 2·log₂ 10 = 6,6439 | l'aire est la longueur au carré : une décade de longueur est 100 en aire | dilatation (exposant 2) |
| 12,91 de f/1 à f/88 | XXX § 4.1 | log₂ 7 710 = 12,913 ; √7 710 = 87,8 | chaque courbe double les croisements (2ⁿ − 2) ; le dessin à aire égale fait de l'aire le nombre de croisements ; 7 710 = (2¹⁷ − 2)/17 | comptage binaire (Euler) et dilatation |
| une courbe = un cran | XXIX § 3.3 et 4 | 1 bit par courbe en aire, ½ bit en longueur | le même comptage | idem |
| un cran par dimension | XXVII § 3 ; XXV § 1 | précision 2^(−n/2)/n | la singularité de la série en −ln √2 : l'écart entre le bord de la calotte (45°) et le sommet du sinus (90°) | singularité analytique |
| le facteur 2 plan ↔ aire | XXIV § 5 | r² = 2R(R − x₀) | Thalès et Euclide VI.8 : le diamètre compté en rayons | dilatation (exposant 2) |
| la FTM50 | VIII § 3 ; XXX § 4.5 | 0,4039727533 ν_c | la moitié de l'aire du disque, mais pour deux disques décalés de 0,8079 | équation |

- **Ce qui est partagé exactement** : le nombre √2 et l'unité logarithmique. Quand on mesure en crans, 6,644 par décade est le même nombre dans XXI, XXVII et XXIX *(démontré : c'est 2·log₂ 10)*.
- **Ce qui est transporté** : « un demi-bit par pas » (XXIX § 4) passe du Venn compté en longueur à la série de la chèvre : même rythme, 6,644 pas par décade. Pour 1 ppm, il faut 40 courbes en longueur et 31 dimensions pour la série (`resultats/venn_ppm.md` § 4) ; l'écart de 9 pas vient du facteur 1/n de la précision 1,03·2^(−n/2)/n.
- **Ce qui reste ouvert** : un mécanisme commun au √2 du comptage binaire (Euler) et au √2 de la singularité (cos 45°). XXVII § 3 les rapproche sans les relier.
- **La FTM50 n'est pas un cran.** Sur la figure de la courbe des 50 % (`figures/fig5_diagramme_parametres.png`), le diaphragme d'un cran est le point D (δ = 0, k = 1/√2), la FTM50 est le point M (δ = 0,8079, k = 1), la chèvre classique est le point G. Les trois sont sur la même courbe, au même niveau F = ½. D relève de la dilatation, M et G de l'équation. XXX § 4.5 dit vrai : « la moitié de l'aire du disque » est aussi la FTM50. Il ne faut pas en tirer que la FTM50 est un cran.
- **Le cran dépend de la dimension.** Un cran de volume en dimension n vaut 2^(1/n) en longueur : √2 en 2D, 1,26 en 3D, puis tend vers 1. Les 6,644 crans par décade valent pour l'aire. « Toutes les dimensions tiennent dans un seul cran » (XXIII § 5) parle de l'aire du disque de la corde dans le plan méridien (de 1 à 2 fois celle du pré), pas du volume.
- **Niven** (XXX § 4.4) : le cran entre le cercle inscrit et le cercle circonscrit d'un polygone régulier est un nombre entier seulement pour le triangle (2) et le carré (1) *(démontré)*. Même cette définition du cran est un privilège du carré.

### 3.5 Ce qui reste ouvert

1. La cause de la moitié exacte de la fiche 005 et de la trace « miroir + complément » (§ 4.1).
2. Un mécanisme commun au √2 du comptage binaire (Euler) et au √2 de la singularité de la série (§ 3.4).
3. La preuve que l'aire de Perron à 4 branches vaut P² + (1 − P)² sur toute la zone, et la frontière exacte de la zone (§ 3.2).
4. Le minimum de la part de la clôture en dimension 4 (0,3760) : aucune explication dans le corpus (XX § 2). Le premier ordre ½ − 1/√(2πn) donne le comportement à grand n, pas le minimum.
5. L'existence d'un Venn simple symétrique par le complément (ou par le demi-tour équatorial) à 17 ou 19 courbes (§ 6.3).
6. La FTM50 et la corde de la moitié pour des conteneurs autres que la boule en dimension n > 3 : aucun script (§ 6.2).

## 4. Les fiches du dossier

### 4.1 Fiche 005 : un Venn à 19 courbes coupe ses croisements exactement en deux (question 4)

Fiche : `recueil/observations/005-moitie-exacte-venn-19-ramp12h.md`.

- **Verdict proposé** : *hasard testé, cause ouverte*. Le statut « ouvert » de la fiche reste juste. Le dossier ajoute trois choses : aucune involution connue ne force la moitié (confirmé sur les 18 certificats) ; une trace de demi-tour existe, sans symétrie ; le « 1/(dispersion) » est un théorème local, pas une impression.
- **Dimensions** : D6 d'abord (le Venn et ses symétries), puis D7 (le hasard testé), puis D2 (Fermat : n divise 2^(n−1) − 1).
- **Test** : coïncidence entre entiers, donc réplication (CLAUDE.md § 10). Les 18 certificats servent de réplication ; l'indépendance est faible (§ ci-dessous).
- **La partie qui portait déjà le lien** : XXX § 2.5 et § 7.3 (le complément, Fermat, 1,6 %), XXX § 3 (la sphère, les deux miroirs), XXVIII § 3.1–3.2 (Fermat, les 7 710 formes), XXIX § 5.2 (le cercle de demi-aire coupe les croisements à 649 ppm).

**Existe-t-il une involution qui force la moitié des croisements ?**

*Le principe* *(démontré)*. Le niveau d'un croisement est le rang moyen de ses quatre régions (k, k + 1, k + 1, k + 2) : un entier l de 1 à n − 1. Le complément envoie le niveau l sur n − l. Pour n impair, il n'y a pas de niveau médian. Si l'ensemble K des croisements était stable par le complément, on aurait N_l = N_(n−l) pour tout l, et exactement la moitié des croisements, 2^(n−1) − 1, serait de niveau ≥ (n + 1)/2. Le demi-tour équatorial « miroir + complément » (i ↦ −i, avec complément) envoie aussi le niveau l sur n − l : s'il laissait K stable, il donnerait la même conclusion.

*Le résultat* *(calculé ici, sur les 18 certificats de Dzoba lus comme données)*. Pour chaque certificat, j'ai calculé la part f des croisements dont l'image est encore un croisement, pour toutes les applications i ↦ a·i (a premier avec n), avec ou sans complément. Je la compare au hasard qui tient compte des classes de paires {i, j} (la classe est min(|i − j|, n − |i − j|)).
- **Aucun certificat n'est stable par le complément.** Le complément seul donne f = 0,023 à 0,031 pour n = 17 et 0,022 à 0,028 pour n = 19, soit 0,75 à 1,04 fois (n = 17) et 0,90 à 1,14 fois (n = 19) le hasard. C'est le niveau du hasard. Cela confirme XXX § 2.5 (écart maximal d'un niveau à son miroir : de 52 à 2 223 croisements) par une autre mesure.
- **Une trace, pourtant.** « Miroir + complément » arrive en tête de toutes les applications, dans les 18 certificats :

| famille | certificats | « miroir + complément » : part f | rapport au hasard | rang | deuxième meilleur rapport | complément seul : rapport |
|---|---:|---|---|---|---|---|
| n = 11 | 1 | 0,140 | 1,84 | 1 sur 19 | 1,49 | 0,85 |
| n = 13 | 1 | 0,089 | 1,72 | 1 sur 23 | 1,41 | 1,41 |
| n = 17 | 4 | 0,055 à 0,070 | 1,79 à 2,30 | 1 sur 31, quatre fois | 1,28 à 1,36 | 0,75 à 1,04 |
| n = 19 | 12 | 0,037 à 0,052 | 1,48 à 2,07 | 1 sur 35, douze fois | 1,21 à 1,35 | 0,90 à 1,14 |

La trace n'est pas une symétrie : f ne dépasse pas 14 % (n = 11) et reste entre 3,7 % et 7,0 % pour n ≥ 17. Elle n'est pas non plus un effet des pôles. Pour `venn17-local-c3-s2`, par niveau : les niveaux 1 et 16 donnent f = 1 (les 17 croisements autour de chaque pôle sont forcés), les niveaux 2 et 15 donnent 0, les niveaux 3, 5 à 12 et 14 donnent 0,061 à 0,071 contre 0,029 à 0,039 attendu (×1,5 à ×2,4), et les niveaux 4 et 13 forment deux pics (0,118 et 0,120 contre 0,034 et 0,035 : ×3,4).

*Mise en garde.* Les 18 certificats viennent de la même méthode et des mêmes échafaudages de départ (le README de Dzoba : la recherche part du diagramme de Griggs, Killian et Savage, dont les croisements multiples sont résolus). Ce ne sont pas 18 réplications indépendantes. La conclusion est : la trace est une propriété de la méthode, ou de l'échafaudage, ou de ma statistique ; elle n'est pas encore une propriété des Venn symétriques.

*Lecture* *(ma lecture, avec une partie démontrée)*. L'application « i ↦ −i, avec complément » conjugue la rotation à son inverse. Avec la rotation, elle engendrerait un groupe dièdral d'ordre 2n *(démontré, trivial)*. Sur la sphère, le complément est la réflexion de l'équateur, et i ↦ −i est une réflexion d'un plan méridien ; leur produit est un **demi-tour autour d'un axe équatorial**, qui échange les deux pôles (∅ et « tout »). Dans la projection stéréographique, c'est z ↦ (R²/2)/z ; sur l'axe réel, c'est d ↦ 1/(2d) : **les jumeaux de XVII § 3**. La trace dit donc que les certificats sont en partie symétriques par le demi-tour des jumeaux.

**Pourquoi une probabilité de l'ordre de 1/(dispersion) est la bonne.** *(démontré pour le principe, calculé pour les nombres)* L'écart à la moitié est toujours un nombre entier d'orbites de n croisements (XXX § 2.5) : la rotation d'ordre n agit sans point fixe sur les croisements, et Fermat donne n | 2^(n−1) − 1, donc 0 est permis. Les écarts observés sont de signes et de parités variés : +21, −27, +24, +28, +26, +26, +19, −6, +46, 0, +11, −28 pour les 12 certificats à 19 courbes (`resultats/centre_venn.md` § 2). Pour une variable à valeurs entières, large et lisse, de dispersion σ, le théorème local donne P(0) ≈ 1/(σ√(2π)). Avec σ = 24,7 orbites (l'écart quadratique des 12), P(0) = 1,6 %, et P(au moins un zéro sur 12) = 1 − (1 − 0,0161)¹² = 17,7 %, ce que XXX § 7.3 écrit « 18 % ». C'est donc le bon ordre de grandeur, à une condition : aucune contrainte arithmétique cachée sur l'écart (une congruence, par exemple). Les parités observées ne montrent aucune contrainte.
*Réplication sur les 16 certificats à 17 et 19 courbes* *(calculé ici)* : avec σ = 19,7 pour n = 17 (quatre certificats) et σ = 24,7 pour n = 19 (douze), on attend 0,08 + 0,19 = 0,27 zéro exact ; on en observe un. La probabilité d'en voir au moins un est de 24 % : rien d'anormal.

**Que faudrait-il pour que la moitié devienne exacte ?** *(ma lecture)*
1. Qu'un des deux gestes laisse K stable : le complément, ou le demi-tour (« miroir + complément »). Chacun donne N_l = N_(n−l) pour tout l, donc la moitié exacte pour n impair. Aucun certificat ne le fait (pour n = 17 et 19, complément : f de 2 à 3 %, demi-tour : f de 4 à 7 % ; pour n = 11 et 13, complément : 6,5 % et 7,3 %, demi-tour : 14 % et 8,9 %). À une rotation près, ce sont les deux seules actions sur les étiquettes qui viennent d'une isométrie de la sphère échangeant les pôles : la réflexion de l'équateur et l'antipode agissent toutes deux par le complément seul (les étiquettes restent en place) ; un demi-tour équatorial agit par i ↦ −i avec complément (§ 5.5). Les autres applications i ↦ a·i, avec a différent de 1 et de −1, ne sont pas des isométries ; je les ai testées aussi, et aucune ne dépasse « miroir + complément ».
2. Ou une contrainte entière dans la recherche : l'écart (un entier) doit valoir 0. C'est une seule équation sur les comptes par niveau, que la recherche peut ajouter à son énergie. La moitié exacte serait alors dessinée, pas observée.
3. Pour qu'elle *existe*, rien de tout cela n'est nécessaire : elle existe dans la fiche 005, par hasard à 1,6 %. Un Venn simple symétrique à 17 ou 19 courbes, stable par le complément ou le demi-tour, n'est pas connu (XXX § 9 ; à vérifier dans la littérature, § 6.3).

**Tests proposés** : (a) répliquer la trace sur des diagrammes d'origine indépendante (les Venn à 11 et 13 courbes de Mamakani et Ruskey, qui sont monotones, alors que ceux du dépôt de Dzoba ne le sont pas, d'après son README) ; (b) la mesurer sur l'échafaudage de Griggs, Killian et Savage, avant la résolution des croisements multiples ; (c) la mesurer sur les certificats à 23 courbes (Zenodo ; la copie locale n'a que `/home/user/dzoba/venn17/verify/RESULTS-23.md`) ; (d) refaire le test avec un nul qui garde la structure par niveau. Code : § 7.3.

### 4.2 Fiche 010 : la chèvre d'Ullisch broute 39,34 % des anneaux du bord (question 6)

Fiche : `recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md`.

- **Verdict proposé** : *exact*, et *pas un hasard* : le lien était déjà posé. La formule « de chaque anneau » est à restreindre aux anneaux du bord (niveaux 1 à 4).
- **Dimensions** : D1 d'abord (la corde, l'arc de 70,81°), puis D6 (les anneaux sont les niveaux du Venn).
- **Test** : précision poussée (l'identité 2 arcsin(k/2) = arccos(1 − k²/2) à 50 chiffres, E3 de XXX § 7.1) *et* variation du paramètre n (la part de la clôture, § 3.3, calculée ici).
- **La partie qui portait déjà le lien** : XX § 1–2 (l'angle de 70,8° du piquet à la clôture ; la « part de la clôture broutée » 0,3934 de `resultats/sphere_faisceaux.md` § 2), X § 5 (la corde de Ptolémée), XXX § 4.3 (le niveau 1).

**Les 39,34 % et la corde de Ptolémée de 70,81° sont-ils la même moitié, vue depuis un anneau ?**
1. **Ils portent le même angle** *(démontré)*. φ = 180° − β = 70,8117° est l'angle au centre sous lequel on voit la corde PQ de la chèvre (X § 5 ; `resultats/carre_ptolemee.md` § 4 ; XX § 1).
2. **Deux lectures du même arc.** La *part de circonférence* est 2φ/360° = φ/π = arccos(1 − k²/2)/π = 0,39340. La *longueur de la corde* est k = 2 sin(φ/2) = 1,158728. Dans la table de Ptolémée (rayon 60), la corde de l'arc 70,8117° vaut 60·k = 69;31,25, entre 69,2574 (70°30′) et 69,6844 (71°). La corde de Ptolémée est la corde de la chèvre.
3. **Ce n'est pas la même moitié.** Le 50 % est la moyenne des parts des anneaux, pondérée par l'aire (2ρ dρ). Le 39,34 % est la part de l'anneau extérieur seul. La part d'un anneau de rayon ρ est s(ρ) = arccos((ρ² + 1 − k²)/(2ρ))/π ; elle augmente quand ρ diminue et vaut 1 pour ρ ≤ k − 1 = 0,1587.
4. **Les parts par niveau** *(calculé ici, dessin idéal à aire égale avec des niveaux binomiaux ; à refaire avec les anneaux de chaque certificat)* :

| niveau | 1 | 2 | 3 | 4 | 5 | 7 | 9 | 11 | 12 | 13 à 16 |
|---|---|---|---|---|---|---|---|---|---|---|
| part de l'anneau broutée par Ullisch | 39,341 % | 39,347 % | 39,382 % | 39,515 % | 39,894 % | 42,323 % | 48,466 % | 60,954 % | 75,626 % | 100 % |

5. **En dimension n**, la part de la clôture est 0,3934 (n = 2), 0,3760 (n = 4, minimum), puis tend vers ½ (§ 3.3). Le 39,34 % est la valeur d'un pas d'une suite qui n'est pas monotone. La chèvre plane ne voit la moitié de la clôture qu'à la limite n = ∞ : la corde √2, l'angle 90°, l'hémisphère.

Conclusion : depuis l'anneau extérieur, la chèvre plane voit 39,34 %, pas la moitié. La moitié est la moyenne sur tous les anneaux.

## 5. Les congruences et les obstructions

Rappel du cadre (plan § 3.0) : deux résultats se recollent s'ils coïncident sur ce qu'ils partagent, à une transformation connue près. Ce qui ne se recolle pas est une obstruction, et désigne un trou.

### 5.1 Les congruences du plan que ce dossier touche

- **K4, les moitiés.** *Se recolle* (établi) : au cercle R/√2 (R1, § 3.2) et à la corde √2 (§ 3.3). *Obstruction candidate* : Kakeya sur une grille finie. *Verdict après T5* : l'obstruction est réelle. La moitié vient de l'inclusion–exclusion à l'ordre 2 (§ 5.4). L'involution x ↦ −x n'explique que l'excès (q − 1)/2.
- **K7, le grain plafonne la profondeur, à un cran près.** *Se recolle* : le Venn (un bit par courbe en aire, ½ bit en longueur), Perron (un bit par étage) et la série de la chèvre (un cran par dimension) sont congrus modulo un cran (XXIX § 4 ; `resultats/venn_ppm.md` § 4). Mon ajout : les lignes 27, 29 et 35 de l'inventaire sont du même type (dilatation, comptage binaire). *Obstruction nouvelle* : l'aire ½ de Perron à 4 branches n'est pas un effet de cran. Le √2 de V § 3 est le point symétrique d'un segment (§ 3.2).
- **K2, la parité.** *Se recolle* : pour N impair, les N directions et leurs opposées en font 2N (aigrettes, ombre Σωⁱ, éventails de Perron). Même fait pour la moitié : *x ↦ −x agit sans point fixe sur les éléments non nuls si et seulement si le corps n'est pas de caractéristique 2* (Kakeya fini, § 5.4), et le complément n'a pas de niveau médian si et seulement si n est impair (XXX § 2.5). *Obstruction* : en Kakeya fini, la parité ne gouverne que l'excès.

### 5.2 Mes congruences

| id | éléments | transformation | se recolle jusqu'où | obstruction | test |
|---|---|---|---|---|---|
| C1 | lignes 3, 9, 19, 23, 26, 30, 33 : le cercle R/√2 | u = (r/R)ⁿ ; la dilatation u ↦ u/2 et le miroir u ↦ 1 − u | exact, en toute dimension : r = 2^(−1/n) R | l'échelle : dans la projection stéréographique, l'équateur n'a pas de position « R/√2 » intrinsèque ; il dépend du rayon R du disque dessiné. L'invariant est l'équateur | aucun (exact) |
| C2 | lignes 1, 2, 13, 20, 21 : équation et involution | n ↦ ∞ (x₀ ↦ 0) | à la limite ; à n fini, le défaut est x₀ = 1/(n + 4/3 − …) | aucune à la limite | variation de n : fait (§ 3.3) |
| C3 | lignes 3, 1, 4 : dilatation puis équation | d₀ = 1 − 2^(−1/n) | à l'ordre (n + 1)/2 : ρ − ρ₀ ∝ (d − d₀)^((n+1)/2) | aucune | variation de n : fait (XVI § 3) |
| C4 | ligne 24 avec 3, 4, 21 : le tableau du grain | un même ε, quatre lectures | exact : l'équateur est la FTM50 en dimension n ; la coquille est la fin du plateau | les exposants (ε⁻², ε⁻¹, ε⁻¹, ε^(−1/2)) ne se recollent pas entre eux, seulement chacun avec son procédé | variation de n : fait |
| C5 | Kakeya fini et fiche 012 : l'inclusion–exclusion | tronquer à l'ordre 1 (borne de l'union, correction de Bonferroni) ou à l'ordre 2 | même identité exacte : 1 = m − C(m, 2) + C(m − 1, 2) | la fiche 012 range Bonferroni parmi les tests à tolérance ; Kakeya fini l'utilise comme borne atteinte | à tester : écrire la correction de la fiche 012 avec le reste C(m − 1, 2) |
| C6 | lignes 14, 15, 16, 17 : les moitiés « rapports » | aucune | non | aucun procédé commun (symétrie centrale, formule, minimum, inclusion–exclusion) | aucun |
| C7 | lignes 15 et 3 : Perron et le cran | α = 1/√2 comme cran de largeur par étage | non : le minimum ½ est atteint sur tout un segment | le √2 n'est pas forcé | variation des deux rapports : fait ici (§ 3.2) |
| C8 | cran de volume 2^(1/n) et cran d'aire √2 | n ↦ 2^(1/n) | pour n = 2 seulement | un cran de volume vaut 1,26 en longueur en 3D, et tend vers 1 | aucun (définition) |
| C9 | « miroir + complément » ; les jumeaux de XVII ; z ↦ 1/z | produit de deux réflexions de la sphère | exact au niveau des groupes | les certificats ne sont pas stables : f de 4 à 7 % (§ 4.1) | réplication indépendante (§ 4.1) |
| C10 | part de la clôture (½ − 1/√(2πn)) et part du volume (½ + 1/√(2πn)) | miroir autour de ½ | calculé : écart résiduel 3·10⁻⁵ en n = 1 000 | mécanisme : ma lecture (E[τ] = 0) | variation de n : fait (§ 3.3) |

### 5.3 Les obstructions

| éléments | le trou | où chercher |
|---|---|---|
| Kakeya fini (17) et l'involution | la seule moitié du corpus qui ne vient pas d'un des trois procédés des médianes | T5 (fait) ; la littérature en caractéristique 2 (§ 6.3) |
| fiche 005 et le complément | aucun Venn simple symétrique par le complément ou le demi-tour n'est connu à 17 ou 19 courbes | Ruskey et Weston (enquête sur les Venn) ; les Venn à 11 et 13 courbes de Mamakani et Ruskey ; les certificats à 23 courbes |
| trace « miroir + complément » (18 sur 18) | cause inconnue : échafaudage, énergie de la recherche ou statistique ? | l'échafaudage de Griggs, Killian et Savage ; `/home/user/dzoba/venn17/search/README.md` (la méthode `ramp12h`) |
| cran d'aire et cran de volume | le « cran » change avec la dimension | une définition explicite du cran en dimension n dans XXIII § 5 |
| Perron à 4 branches et le cran | le √2 n'est pas forcé ; la frontière de la zone P² + (1 − P)² est inconnue | une démonstration de A = P² + (1 − P)² (§ 3.2) |
| échelle du miroir conforme | la position R/√2 dépend du disque dessiné | XXX § 3 : écrire que l'invariant est l'équateur |
| fiche 010 et « chaque anneau » | la part n'est 39,34 % que pour les anneaux du bord | `resultats/centre_venn.md` § 4 : refaire le calcul avec les anneaux de chaque certificat |
| √2 du comptage binaire et √2 de la série | deux mécanismes pour la même unité | un lien entre XXIX § 4 et XXV § 1 |

### 5.4 T5 : ce que chaque issue changerait à l'arbre P2 (question 7)

**Le test et son résultat.** T5 demande si la moitié de Kakeya fini (XIV § 5) est le même procédé que les hémisphères. À la date où j'écris, `scripts/revision_001.py` § 4.7 et `resultats/revision_001.md` § 4.7 donnent le minimum exact pour q = 2, 3, 4, 5, 7, 8, 9 : 3, 7, 10, 17, 31, 36, 49. C'est l'issue (b) du tableau ci-dessous. Mes constructions explicites (§ 7.1) donnent les mêmes tailles, et vont jusqu'à q = 25 sans optimisation.

**La preuve courte** *(démontré ici ; la borne et les deux cas semblent classiques, d'après des extraits en ligne : § 6.3)*.
1. *La borne.* Dans un ensemble de Kakeya de F_q², prenons une droite par direction : q + 1 droites, deux à deux non parallèles, donc deux à deux sécantes en exactement un point. L'inégalité de Bonferroni à l'ordre 2 donne |K| ≥ Σ|L| − Σ|L ∩ L′| = q(q + 1) − C(q + 1, 2) = q(q + 1)/2. Plus exactement, |K| = q(q + 1)/2 + Σ_P C(m_P − 1, 2), où m_P est le nombre de droites par P. C'est une identité, vraie pour toute famille de q + 1 droites de directions distinctes : elle vient de 1 = m − C(m, 2) + C(m − 1, 2) pour m ≥ 1.
2. *La construction, q pair.* Les q droites y = ax + a² (a ∈ F_q) et la verticale x = 0. Deux droites a ≠ b se coupent en (a + b, ab). Une droite c passe par ce point seulement si c² + (a + b)c + ab = (c + a)(c + b) = 0, donc c = a ou c = b. La verticale coupe la droite a en (0, a²), et les carrés sont tous distincts en caractéristique 2. Aucun point n'est sur trois droites : l'excès est 0 et |K| = q(q + 1)/2 exactement. C'est la duale d'une hyperovale : q + 2 droites du plan projectif, trois à trois non concourantes (en comptant la droite à l'infini). Une telle famille existe si et seulement si q est pair (classique : Bose ; Hirschfeld).
3. *La construction, q impair.* Les tangentes y = ax − a²/4 de la parabole y = x². Deux tangentes a ≠ b se coupent en ((a + b)/4, ab/4). Une tangente c passe par un point (x₀, y₀) exactement quand c² − 4x₀c + 4y₀ = 0 : au plus deux valeurs de c, donc aucune troisième tangente ne passe par ce point. Mais la verticale x = 0 rencontre les tangentes a et −a au même point (0, −a²/4) : un point triple pour chaque paire {a, −a}, a ≠ 0. L'excès vaut donc le nombre de paires {a, −a} : (q − 1)/2. Blokhuis et Mazzocca montrent qu'on ne peut pas faire mieux.
4. *Une formule pour les deux cas* *(calculé : treize valeurs de q de 2 à 25, § 7.1)*. L'excès est (q − |Fix|)/2, où Fix est l'ensemble des points fixes de a ↦ −a : le nombre de paires {a, −a}. Il vaut 0 si q est pair et (q − 1)/2 si q est impair.
5. *Ce que disent les carrés modulo q* *(démontré)*. XIV § 5 et XXVII § 9 expliquent la moitié par les carrés. Pour q impair, un point (x, y) est sur une tangente de la parabole exactement quand x² − y est un carré ou zéro, ce qui fait (q + 1)/2 points par colonne. C'est un décompte exact de la construction. Ce n'est pas la raison du minimum : la borne vient de l'inclusion–exclusion, pour tout q. Et pour q pair, tout élément est un carré, alors que le minimum reste q(q + 1)/2.

**Les trois issues.**

| issue | ce qu'on observerait | effet sur l'arbre P2 | effet sur le nerf |
|---|---|---|---|
| (a) l'involution x ↦ −x | le minimum change de forme pour q = 2, 4, 8, où x ↦ −x est l'identité | la branche « grille finie » rejoint le triangle des médianes ; l'obstruction de K4 disparaît | la piste XIV–XX se ferme par un recollement |
| (b) l'inclusion–exclusion | q(q + 1)/2 pour q pair ; + (q − 1)/2 pour q impair | la branche « grille finie » quitte le triangle {involution, dilatation, équation} et forme avec la fiche 012 un triangle voisin ; l'involution reste, comme explication de l'excès seulement | la piste XIV–XX se ferme par une obstruction ; une arête nouvelle XIV–fiche 012 |
| (c) le hasard | pas de loi simple en q | la branche reste un rameau ouvert, comme la fiche 005 | aucun |

**Ce que montre le calcul : (b).** Je propose donc de corriger P2 ainsi :
- **Le triangle du bas** est : *la médiane F(x*) = ½, résolue par involution, par dilatation ou par équation* (§ 1.2). Les branches involution, dilatation et équation y arrivent, et se rejoignent au cercle R/√2 et à la corde √2. La branche « équation » s'enrichit de XIX § 6 et de XXV § 1.2 (le retour de l'infini) ; la branche « dilatation » de XVI § 3 et de XXIII § 4.
- **La branche « grille finie »** devient un second triangle, voisin : *l'inclusion–exclusion tronquée*, avec la fiche 012 (ordre 1) et Kakeya fini (ordre 2). Le lien est la même inégalité, pas la même moitié.
- **La branche « Kakeya »** (V § 1 et § 3) se divise : le deltoïde (une formule) et Perron (un minimum) n'ont pas de triangle commun avec les médianes ; ils attendent le leur.
- **La fiche 005** reste un rameau : aucune des symétries possibles ne la force ; une trace de demi-tour existe (§ 4.1).
- **Ce que T5 ne change pas** : le triangle (moitiés, ombres, corde) du nerf reste rempli par XX à XXII et la fiche 010 (plan § 3.3).
- **Deux x ↦ −x, à ne pas confondre** *(ma lecture)*. Celui de T5 est a ↦ −a sur les pentes des tangentes de la parabole : la réflexion de la parabole dans son axe, qui fixe l'axe. Celui de VIII § 1 et § 3 est la rotation de 180°, qui retourne l'aiguille et échange les deux ménisques de la FTM, et ne fixe qu'un point. Dans F_q², une droite est sa propre retournée : le demi-tour de l'aiguille n'y coûte rien. Les deux ont le même nom et le même signe, pas le même rôle.

### 5.5 Le cocycle de P2

Les trois gestes de la branche involution sont dans un seul groupe, donc le cocycle se ferme sans calcul *(démontré)*. Sur la sphère, soit le groupe {±1}³ des changements de signe des trois coordonnées (x, y, z), l'axe polaire étant z. La réflexion de l'équateur E = (+, +, −) est le complément conforme (r·r′ = R²/2) ; en projection de Lambert, c'est θ ↦ π − θ, le miroir d'aire. L'antipode A = (−, −, −) échange aussi les deux hémisphères, sans point fixe ; XX § 3 ne le nomme pas, mais sur les étiquettes il agit comme E. Le changement de carte y ↦ y/|y|² de XX § 3 est E lu dans le plan ; l'inversion de rayon √2 centrée au pôle est la projection stéréographique elle-même (elle envoie la sphère sur le plan et fixe l'équateur). Le demi-tour autour d'un axe équatorial H = (+, −, −) est « miroir + complément », les jumeaux de XVII § 3. On a H = E ∘ C, avec C = (+, −, +) la réflexion d'un plan méridien, et A = E ∘ P, avec P = (−, −, +) le demi-tour autour de l'axe polaire. Le groupe est commutatif : les composées se font dans le groupe, la condition de cocycle est automatique. Tous les trois échangent les deux hémisphères et laissent l'équateur globalement fixe : c'est le cercle R/√2. Sur les étiquettes d'un Venn symétrique, E et A agissent de la même façon (le complément, les étiquettes en place) et H agit par i ↦ −i avec complément. À une rotation près, ce sont les deux seules actions possibles d'une isométrie qui échange les pôles et normalise le groupe des rotations d'ordre n (§ 4.1).

## 6. Les trous

### 6.1 Les trous du recueil : fiches nouvelles proposées

Douze fiches sur quinze viennent des parties XXIX et XXX, et les parties I à XXVIII n'ont aucune fiche à elles ; D5 et D8 n'ont aucune fiche principale (plan § 6.1). Voici dix propositions, numérotées N1 à N10. La priorité dit l'ordre d'écriture : 1 d'abord. Chaque fiche suit le format du recueil (`recueil/README.md`) ; je donne le tableau d'en-tête et l'observation. Le champ « révisé » serait « non ».

#### N1 : Kakeya sur un corps fini, la moitié vient de l'inclusion–exclusion (priorité 1)

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact (l'identité et la borne sont démontrées ; le minimum est calculé pour q = 2 à 9 dans `resultats/revision_001.md` § 4.7 ; les constructions explicites sont contrôlées jusqu'à q = 25) |
| partie | XIV (§ 5) |
| script | `scripts/aiguille_grille.py` § 5 ; `scripts/revision_001.py` § 4.7 |
| image | `figures/n1_aiguille_grille.png` (panneau f) |
| dimension | D5 (D6 pour l'involution) |
| test | variation de q et de la caractéristique (lien de structure) |

*Observation.* Pour toute famille de q + 1 droites de directions distinctes de F_q², |K| = q(q + 1)/2 + Σ C(m_P − 1, 2). Pour q pair, les droites y = ax + a² et x = 0 n'ont aucun point triple (la duale d'une hyperovale) : |K| = q(q + 1)/2, soit 3, 10, 36, 136 pour q = 2, 4, 8, 16. Pour q impair, les tangentes de la parabole donnent q(q + 1)/2 + (q − 1)/2, et l'excès est le nombre de paires {a, −a}, c'est-à-dire de 2-orbites de l'involution a ↦ −a. *Contexte.* La carte de XXVII § 9 se demandait si la moitié de Kakeya fini et celle des hémisphères viennent du même procédé. Blokhuis et Mazzocca écrivent, d'après des extraits en ligne, la même identité sous la forme q(q + 1)/2 + σ(K) (à vérifier) : cette fiche est un lien entre deux parties, pas une découverte sur Kakeya.

#### N2 : L'arbre de Perron à 4 branches, l'aire ne dépend que du rétrécissement total (priorité 1)

| champ | valeur |
|---|---|
| type | Fait amusant |
| statut | à tester (exact en fractions sur plus de 50 points rationnels ; démonstration à écrire) |
| partie | V (§ 3) ; XXVIII (§ 2.2–2.4) |
| script | `scripts/aiguille.py` § 3 (`arbre`, aire exacte) ; code du § 7.2 |
| image | `figures/e1_aiguille_kakeya.png` (panneau c) |
| dimension | D5 |
| test | précision poussée (l'identité en fractions) et variation des deux rapports |

*Observation.* Pour deux rapports α₀ et α₁ dans une zone qui contient le segment α₀α₁ = ½ (3/5 ≤ α₀ ≤ 3/4), l'aire exacte vaut P² + (1 − P)² = 2P² − 2P + 1, avec P = α₀α₁. Le minimum ½ est atteint sur tout le segment ; les deux points connus, (3/4, 2/3) et (1/√2, 1/√2), n'en sont que deux. La borne « cœur + oreilles » de XXVIII § 2.2 vaut 0,50736 en (1/√2, 1/√2) et 0,59 en (3/5, 5/6) : elle n'est pas serrée. *Contexte.* V § 3 : « une vraie moitié, avec le √2 de la diagonale du carré ».

#### N3 : La FTM50 d'une pupille en dimension n est la médiane de |Y₁| (priorité 1)

| champ | valeur |
|---|---|
| type | Analogie |
| statut | exact (l'identité) ; valeurs calculées ici |
| partie | VIII (§ 3) ; XXIII (§ 4) |
| script | `scripts/foyer_fibonacci.py` § 3 ; `scripts/lentilles_boules_grain.py` § 4 (à étendre à la FTM en dimension n) |
| image | `figures/x1_lentilles_boules_grain.png` (panneau e) |
| dimension | D4 (D3) |
| test | précision poussée (l'identité) et variation de n |

*Observation.* La lentille de deux boules unité à la distance s occupe la fraction P(|Y₁| ≥ a) de la boule, avec Y uniforme dans la boule et a = s/2 = ν/ν_c (deux calottes de hauteur 1 − a). La FTM50 est donc la médiane de |Y₁|. Valeurs : a = 0,5 (n = 1) ; 0,40397275 (n = 2, le résultat de la partie I) ; 0,34729636 (3) ; 0,30907251 (4) ; 0,20578686 (10) ; 0,06720444 (100) ; 0,02132148 (1 000) ; 0,00674465 (10⁴). Le produit a·√n tend vers 0,67449, le quantile à 75 % de la loi normale ; son carré, 0,455, est le coefficient de la ligne « équateur » de XXIII § 4. *Contexte.* VIII § 3 et XXX § 4.5 disent la FTM50 « moitié de l'aire du disque » ; XXIII § 4 compte l'équateur sans le dire.

#### N4 : « Miroir + complément » arrive en tête dans 18 certificats sur 18 (priorité 1)

| champ | valeur |
|---|---|
| type | Hasard ; Corrélation |
| statut | ouvert (à tester) |
| partie | XXX (§ 2.5, § 7.3) |
| script | `scripts/centre_venn.py` § 2 (à étendre) ; code du § 7.3 |
| image | `figures/ae1_centre_moitie.png` (panneau f) |
| dimension | D6 (D7) |
| test | réplication sur des diagrammes d'origine indépendante |

*Observation.* Aucun des 18 certificats n'est stable par le complément (part f de 2 à 3 %, au niveau du hasard). Mais « i ↦ −i avec complément » est, dans chacun, l'application qui envoie le plus de croisements sur des croisements : 1,48 à 2,30 fois le hasard, rang 1 sur 19 à 35 applications. Elle correspond à un demi-tour équatorial de la sphère, les jumeaux de XVII § 3. *Contexte.* Fiche 005 ; § 4.1 de ce dossier.

#### N5 : Les quatre lignes du tableau du grain sont les quatre procédés de la moitié (priorité 2)

| champ | valeur |
|---|---|
| type | Analogie |
| statut | exact |
| partie | XXIII (§ 4) ; XVI (§ 3) |
| script | `scripts/lentilles_boules_grain.py` § 4 ; `scripts/menisque_projection.py` § 3 |
| image | `figures/x1_lentilles_boules_grain.png` (panneau e) |
| dimension | D3 (D1) |
| test | variation de n ; précision poussée pour les identités |

*Observation.* L'équateur est l'involution x₁ ↦ −x₁ (n ≈ 0,455/ε²). La coquille est la dilatation : (1 − ε)ⁿ = ½ donne ε = 1 − 2^(−1/n), qui est exactement d₀, la fin du plateau de XVI § 3 (n ≈ 0,693/ε). Le plan est l'équation exacte (n = 1/ε − 1). Le ménisque est le défaut de l'équation (n ≈ 0,577/√ε). Les exposants 2, 1, 1, ½ sont ceux des procédés.

#### N6 : Les quatre demi-volumes d'Archimède : trois sont 2^(−1/e), le quatrième est une cubique (priorité 3)

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact |
| partie | II (§ 1) |
| script | `scripts/calculs_archimede.py` § 1 |
| image | `figures/b2_tranches_archimede.png` (panneau b) |
| dimension | D6 (D1) |
| test | variation de l'exposant e |

*Observation.* Le volume sous la hauteur h croît comme h^e : e = 1 pour le cylindre, 2 pour le bol paraboloïde, 3 pour le cône. Le plan de la moitié est à 2^(−1/e) : 1/2, 1/√2, 2^(−1/3). Le bol paraboloïde est coupé à 1/√2 comme le disque de la chèvre au centre, parce que l'exposant est le même que celui de l'aire. Le cône est coupé à 0,7937, la corde de la moitié de la boule de dimension 3 depuis O (IV § 4), parce que l'exposant est 3. L'hémisphère n'est pas une loi de puissance : z³ − 3z + 1 = 0, z = 2 cos 80°.

#### N7 : L'involution z² ↔ 1 − z² échange la tranche de l'hémisphère et celle du cône conjugué (priorité 2)

| champ | valeur |
|---|---|
| type | Analogie |
| statut | exact |
| partie | II (§ 1) ; XIX (§ 6) |
| script | `scripts/calculs_archimede.py` § 1 ; `scripts/bases_objets.py` § 4 |
| image | `figures/b2_tranches_archimede.png` (panneau a) |
| dimension | D6 |
| test | précision poussée (l'identité) |

*Observation.* À la hauteur z, la tranche de l'hémisphère est π(1 − z²) et celle du cône conjugué πz² : leur somme est la tranche du cylindre, π. Le cône est donc le complément de l'hémisphère dans le cylindre, et la substitution z² ↔ 1 − z² les échange. Son point fixe est z = 1/√2, où les deux valent π/2. C'est le miroir d'aire du complément du Venn (XXX § 3), posé par Archimède. *Contexte.* II § 1 : « les trois tranches valent π R²/2 » ; XIX § 6 : « ce cercle enferme exactement la moitié du disque ».

#### N8 : La corde de la moitié du carré ne change pas quand on coupe ses quatre coins, jusqu'à t = 0,5989 (priorité 3)

| champ | valeur |
|---|---|
| type | Fait amusant ; Coïncidence |
| statut | exact (argument de symétrie) ; valeurs calculées ici |
| partie | II (§ 9) |
| script | `scripts/calculs_archimede.py` § 9 |
| image | `figures/b9_polygones_polyedres.png` (panneau a) |
| dimension | D1 |
| test | variation de la profondeur t |

*Observation.* Le carré [−1, 1]², le piquet en (1, 0), la corde de la moitié r₀ = 1,1656443249. Si l'on coupe les quatre coins à la profondeur t, la corde ne change pas tant que les coins proches restent dans le disque de corde, soit t ≤ √(r₀² − 1) = 0,5989379702 : les deux coins proches (dedans) et les deux coins lointains (dehors) ont la même aire, par la réflexion x ↦ −x du carré. L'octogone régulier circonscrit est t = 2 − √2 = 0,5858. À t = 0,60, la corde vaut 1,1656441490. *Contexte.* II § 9 notait l'égalité entre 4 et 8 côtés comme « une coïncidence exacte ».

#### N9 : Les écarts à la moitié sont des miroirs : ½ − 1/√(2πn) sur la clôture, ½ + 1/√(2πn) sur le volume (priorité 3)

| champ | valeur |
|---|---|
| type | Analogie |
| statut | structure (le mécanisme est E[τ] = 0 ; la loi de l'écart est calculée jusqu'à n = 1 000) |
| partie | XX (§ 2) ; I (§ 5.3) |
| script | `scripts/sphere_faisceaux.py` § 2 ; `scripts/tiers_dimension.py` § 1 |
| image | — (à produire dans le script de la révision) |
| dimension | D1 |
| test | variation de n et loi de l'écart |

*Observation.* La part de la clôture broutée par la vraie corde et la part du volume broutée par la corde √2 tendent vers ½ par deux côtés, en miroir : ½ − 1/√(2πn) et ½ + 1/√(2πn) au premier ordre. L'écart résiduel de la clôture est de 8,7·10⁻⁴ (n = 100), 1,7·10⁻⁴ (n = 300) et 3·10⁻⁵ (n = 1 000) ; celui du volume, de 6,7·10⁻⁴, 1,3·10⁻⁴ et 3·10⁻⁵. La raison : la densité de U₁ en 0 vaut √(n/(2π)), et la clôture voit le décalage +1/n quand le volume voit −1/n. Cette part de la clôture a un minimum en n = 4 (0,3760), que rien n'explique encore.

#### N10 : Au point de Rayleigh, l'aire du faisceau double et l'intensité au centre est divisée par deux (priorité 2)

| champ | valeur |
|---|---|
| type | Analogie |
| statut | exact (classique : Self, 1983) |
| partie | XXI (§ 3) ; XIX (§ 6) |
| script | `scripts/vingt_quatre_miroir.py` § 2 |
| image | `figures/v1_vingt_quatre.png` (panneau f) |
| dimension | D8 (D4) |
| test | précision poussée (l'identité z² + z_R² = 2 z_R² en z = z_R) |

*Observation.* Pour un faisceau gaussien, r = θ·|z + i·z_R| ; à z = z_R, la largeur vaut √2 fois le col, l'aire est doublée, l'intensité au centre est divisée par deux et le produit de Newton aussi. C'est un cran, au sens du diaphragme. La chèvre de dimension infinie, piquet sur la clôture, est au même point : ρ = |1 + i| = √2. Cette fiche est la première de D8, vide jusqu'ici.

### 6.2 Les trous du corpus

- **Aucun script ne calculait** : la FTM50 en dimension n (N3) ; l'aire de Perron à deux rapports (N2) ; la corde du carré à coins coupés au-delà de l'octogone (N8) ; la symétrie des certificats autre que N_l = N_(n−l) (N4). `scripts/centre_venn.py` § 2 ne teste que N_l = N_(n−l).
- **Les constructions de Kakeya fini hors de portée de l'optimisation** (q ≥ 11) : le § 7.1 les couvre.
- **La corde de la moitié pour d'autres conteneurs que la boule, en dimension n > 3** : seules la boule (I) et les trois solides depuis O (IV § 4) sont calculés ; II § 7 s'arrête à la dimension 3.
- **La part de la clôture** : le minimum en n = 4 n'est pas expliqué, et la loi à grand n n'est écrite nulle part (N9).
- **Le cran en dimension n** : le cran de volume 2^(1/n) n'est défini nulle part ; XXIII § 5 parle de l'aire.
- **Les fiches** : D5 et D8 n'ont aucune fiche principale. Les parties I à XXVIII n'ont aucune fiche sur la moitié ; les deux fiches du dossier (005 et 010) viennent de la partie XXX.
- **Les anneaux de la fiche 010** : XXX § 4.3 donne les parts moyennes des trois chèvres ; la part de chaque niveau n'est pas tabulée (§ 4.2).

### 6.3 Les trous des données publiées

| piste | ce qui manque | où chercher | références |
|---|---|---|---|
| Kakeya fini en caractéristique 2 | le plan (§ 6.2 f) ne savait pas quelle publication donne le minimum pour q pair. Une recherche en ligne, limitée à des résumés (aucune page ne s'ouvre d'ici, arXiv compris), indique que Blokhuis et Mazzocca écrivent déjà la taille de K sous la forme q(q + 1)/2 + σ(K) avec σ(K) ≥ 0, obtiennent l'égalité pour q pair par une duale d'hyperovale, et que Blokhuis, De Boeck, Mazzocca et Storme classent les plus petits ensembles pour q pair. Le § 5.4 en redonne la preuve en cinq lignes : à lire avant de la présenter comme nouvelle. | Blokhuis et Mazzocca (le texte complet, cas pair) ; Blokhuis, De Boeck, Mazzocca, Storme ; Faber (2005), citée par XIV ; la borne de Wolff ; la géométrie finie : hyperovales | Blokhuis–Mazzocca 2008 ; Blokhuis–De Boeck–Mazzocca–Storme 2014 (à vérifier) ; Faber 2005 (à vérifier) ; Wolff (à vérifier) ; Bose 1947 (à vérifier) ; Hirschfeld 1998 ; Bonferroni 1936 |
| Venn simples symétriques, avec symétrie par le complément ou demi-tour équatorial | les critères de recherche publiés (README de Dzoba) ne contiennent ni la moitié des croisements, ni la symétrie par le complément, ni le demi-tour ; la statistique « miroir + complément » n'est pas un invariant publié | l'enquête de Ruskey et Weston (la notion de symétrie polaire, à vérifier) ; les Venn à 11 et 13 courbes de Mamakani et Ruskey ; `/home/user/dzoba/venn17/search/README.md` ; les certificats à 23 courbes (Zenodo) | Henderson 1963 ; Griggs–Killian–Savage 2004 ; Ruskey–Weston ; Mamakani–Ruskey (à vérifier) ; Dzoba 2026 (à vérifier) |
| la FTM d'une pupille en dimension n | rien d'optique : c'est la loi de la première coordonnée d'un point de la boule | Poincaré–Borel, mesure en grande dimension | Diaconis–Freedman 1987 ; Ball 1997 |
| Perron à 2 rapports | ce que je connais (Schoenberg, Keich) donne l'ordre et les rapports télescopiques ; la zone P² + (1 − P)² n'y est pas, à ma connaissance (à vérifier) | Schoenberg 1962 ; Keich 1999 ; la partie XXVIII | Schoenberg 1962 ; Keich 1999 |
| la part de la clôture broutée, en dimension n | le minimum en dimension 4 n'est pas dans ce que je connais de la littérature de la chèvre (à vérifier) | Fraser et Meyerson, 1984 | Fraser 1984 ; Meyerson 1984 |
| coïncidences d'entiers (fiche 005) | on ne compte pas, dans les analyses de Venn symétriques, l'écart à la moitié en orbites : c'est pourtant un entier avec une loi locale | théorème local pour les variables entières | Feller (vol. 1) |

#### Références citées dans ce dossier

Statut : « sûre » = je connais la référence (auteurs, titre, revue, année) ; « à vérifier » = je ne suis pas sûr d'un détail ou je n'ai pas pu lire la source. Aucune page web ne s'ouvre depuis cet environnement (arXiv compris) ; seule une recherche en ligne, qui rend des résumés, était possible, et je le note pour les références concernées.

- *sûre* : A. Blokhuis, F. Mazzocca, « The finite field Kakeya problem », dans *Building Bridges*, Bolyai Society Mathematical Studies 19, 205–218 (2008) ; la version arXiv:0911.4370 est celle que cite la partie XIV. Ce qu'ils démontrent pour q pair : *à vérifier* (résumé de recherche en ligne seulement : q(q + 1)/2 + σ(K) avec σ(K) ≥ 0, égalité par une duale d'hyperovale).
- *à vérifier* : A. Blokhuis, M. De Boeck, F. Mazzocca, L. Storme, « The Kakeya problem: a gap in the spectrum and classification of the smallest examples », *Designs, Codes and Cryptography* 72(1), 21–31 (2014), doi:10.1007/s10623-012-9790-3 (recherche en ligne, résumé seulement).
- *à vérifier* : T. Wolff, « Recent work connected with the Kakeya problem », dans *Prospects in Mathematics* (Princeton, 1996), American Mathematical Society (1999) : la borne q(q + 1)/2 par la méthode de Wolff, d'après un résumé en ligne.
- *sûre* : Z. Dvir, « On the size of Kakeya sets in finite fields », *J. Amer. Math. Soc.* 22, 1093–1097 (2009).
- *sûre* : Z. Dvir, S. Kopparty, S. Saraf, M. Sudan, « Extensions to the method of multiplicities, with applications to Kakeya sets and mergers », *SIAM J. Comput.* 42(6) (2013).
- *sûre* : G. Mockenhaupt, T. Tao, « Restriction and Kakeya phenomena for finite fields », *Duke Math. J.* 121(1), 35–74 (2004).
- *à vérifier* : X. W. C. Faber, « On the finite field Kakeya problem in two dimensions » (arXiv:math/0510356, octobre 2005, révisé en octobre 2006, annoncé pour le *Journal of Number Theory* ; volume et pages non confirmés) : ce qu'elle démontre pour q pair.
- *à vérifier* : R. C. Bose, « Mathematical theory of the symmetrical factorial design », *Sankhyā* 8, 107–166 (1947) : un arc du plan projectif a au plus q + 1 points si q est impair, q + 2 si q est pair.
- *sûre* : J. W. P. Hirschfeld, *Projective Geometries over Finite Fields*, 2e éd., Oxford University Press (1998).
- *sûre* : C. E. Bonferroni, « Teoria statistica delle classi e calcolo delle probabilità », *Pubblicazioni del R. Istituto Superiore di Scienze Economiche e Commerciali di Firenze* 8, 3–62 (1936).
- *sûre* : J. Galambos, I. Simonelli, *Bonferroni-type Inequalities with Applications*, Springer (1996).
- *sûre* : D. Henderson, « Venn diagrams for more than four classes », *Amer. Math. Monthly* 70, 424–426 (1963).
- *sûre* : J. Griggs, C. E. Killian, C. D. Savage, « Venn diagrams and symmetric chain decompositions in the Boolean lattice », *Electron. J. Combin.* 11(1), R2 (2004).
- *sûre* : F. Ruskey, M. Weston, « A survey of Venn diagrams », *Electron. J. Combin.*, Dynamic Survey DS5.
- *à vérifier* : la notion de diagramme de Venn à symétrie polaire ou dièdrale dans cette enquête.
- *à vérifier* : K. Mamakani, F. Ruskey, les Venn simples symétriques à 11 et 13 courbes (2012 et 2014 ; titres et volumes).
- *à vérifier* : Brenner, Gregor, Mütze, Verciani (2026), l'enquête que le README de Dzoba cite pour dire que le problème est ouvert au-delà de 13 courbes (titre et revue).
- *à vérifier* : C. Dzoba, arXiv:2609.26546 (2026), et le dépôt dzoba/venn17 (le dépôt est local et lu ; l'identifiant vient du plan).
- *sûre* : P. Diaconis, D. Freedman, « A dozen de Finetti-style results in search of a theory », *Ann. Inst. H. Poincaré Probab. Statist.* 23, 397–423 (1987).
- *sûre* : K. Ball, « An elementary introduction to modern convex geometry », dans *Flavors of Geometry*, MSRI Publications 31, Cambridge University Press, 1–58 (1997).
- *sûre* : M. Fraser, « The grazing goat in n dimensions », *College Math. J.* 15(2), 126–134 (1984) ; M. D. Meyerson, « Return of the grazing goat in n dimensions », *College Math. J.* 15(5), 430–432 (1984).
- *sûre* : I. Ullisch, « A closed-form solution to the geometric goat problem », *Math. Intelligencer* 42(3), 12–16 (2020).
- *sûre* : I. J. Schoenberg, « On the Besicovitch–Perron solution of the Kakeya problem », dans *Studies in Mathematical Analysis and Related Topics*, Stanford University Press (1962) ; U. Keich, « On L^p bounds for Kakeya maximal functions and the Minkowski dimension in ℝ² », *Bull. London Math. Soc.* 31(2), 213–221 (1999).
- *sûre* : S. A. Self, « Focusing of spherical Gaussian beams », *Applied Optics* 22(5), 658–661 (1983).
- *sûre* : W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. 1, 3e éd., Wiley (1968) : le théorème local.
- *sûre* (classiques) : J. H. Lambert (1772), la projection azimutale équivalente ; Archimède, *De la sphère et du cylindre* ; Ptolémée, *Almageste* I.10–11 (la table des cordes) ; Hippocrate de Chios, les lunules.

## 7. Le code minimal du test qui me concerne (T5, côté « moitiés »)

`scripts/revision_001.py` a déjà, au § 4.7, le minimum exact par programmation en nombres entiers (`minimum_kakeya_fq`, q = 2 à 9). Ce que ce dossier ajoute au test : (1) des ensembles de Kakeya explicites, qui vont au-delà de la portée de l'optimisation ; (2) l'identité d'inclusion–exclusion vérifiée sur chacun ; (3) la comparaison de l'excès avec l'involution a ↦ −a. Si l'un des `assert` échoue pour un q, l'issue (b) du § 5.4 est fausse pour ce q.

### 7.1 T5

Le code est autonome (bibliothèque standard). Je l'ai lancé dans un dossier temporaire : toutes les assertions passent pour q = 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 25 *(calculé ici)*. Il n'affiche que ce qu'il calcule.

```python
"""T5, côté « moitiés » : ensembles de Kakeya explicites dans F_q^2, identité d'inclusion-exclusion, rôle de l'involution x -> -x.
Autonome : bibliothèque standard seulement. Le minimum exact par programmation en nombres entiers est déjà dans scripts/revision_001.py, § 4.7
(minimum_kakeya_fq) : ce code le complète pour les q hors de sa portée (11, 13, 16, 17, 19, 25) et teste l'explication."""
import math
from collections import Counter

# polynôme irréductible : x^m = -(c_0 + c_1 x + ... + c_(m-1) x^(m-1)) ; clé q -> (p, m, [c_0, ..., c_(m-1)])
POLY = {q: (q, 1, [0]) for q in (2, 3, 5, 7, 11, 13, 17, 19)}
POLY.update({4: (2, 2, [1, 1]), 8: (2, 3, [1, 1, 0]), 16: (2, 4, [1, 1, 0, 0]), 9: (3, 2, [1, 0]), 25: (5, 2, [2, 0])})


def corps(q):
    """Tables d'addition, de multiplication et d'opposé de F_q ; un élément est un entier 0..q-1 (chiffres en base p)."""
    p, m, c = POLY[q]
    dig = lambda a: [(a // p ** i) % p for i in range(m)]
    val = lambda d: sum(x * p ** i for i, x in enumerate(d))

    def mul1(a, b):
        da, db, r = dig(a), dig(b), [0] * (2 * m - 1)
        for i, x in enumerate(da):
            for j, y in enumerate(db):
                r[i + j] = (r[i + j] + x * y) % p
        for k in range(2 * m - 2, m - 1, -1):                       # réduction par x^m = -sum c_i x^i
            t, r[k] = r[k], 0
            for i in range(m):
                r[k - m + i] = (r[k - m + i] - t * c[i]) % p
        return val(r[:m])

    add = [[val([(x + y) % p for x, y in zip(dig(a), dig(b))]) for b in range(q)] for a in range(q)]
    mul = [[mul1(a, b) for b in range(q)] for a in range(q)]
    neg = [val([(-x) % p for x in dig(a)]) for a in range(q)]
    inv = [None] + [next(b for b in range(1, q) if mul[a][b] == 1) for a in range(1, q)]
    return add, mul, neg, inv


def kakeya_explicite(q, F):
    """q + 1 droites, une par direction : q impair, tangentes y = a x - a^2/4 de la parabole y = x^2 ; q pair, y = a x + a^2 ;
    plus la verticale x = 0."""
    add, mul, neg, inv = F
    quart = inv[mul[2 % q][2 % q]] if q % 2 else None               # 1/4
    droites = []
    for a in range(q):
        b = neg[mul[mul[a][a]][quart]] if q % 2 else mul[a][a]
        droites.append([(x, add[mul[a][x]][b]) for x in range(q)])
    droites.append([(0, y) for y in range(q)])
    return droites


def une_droite_par_direction(q, droites, F):
    add, mul, neg, inv = F
    pentes = {mul[add[d[1][1]][neg[d[0][1]]]][inv[add[d[1][0]][neg[d[0][0]]]]] for d in droites[:-1]}
    return len(droites) == q + 1 and len(pentes) == q


if __name__ == "__main__":
    print("q | |K| | q(q+1)/2 | excès | identité | multiplicités | points fixes de a -> -a | paires {a, -a} | droite par direction")
    for q in (2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 25):
        F = corps(q)
        add, mul, neg, inv = F
        d = kakeya_explicite(q, F)
        mult = Counter(Counter(p for dr in d for p in dr).values())      # {m : nombre de points sur exactement m droites}
        K = sum(mult.values())
        exces = sum(math.comb(m - 1, 2) * n for m, n in mult.items())
        fixes = sum(1 for a in range(q) if neg[a] == a)                  # points fixes de a -> -a : 1 (q impair), q (q pair)
        paires = (q - fixes) // 2                                         # orbites à deux éléments : (q-1)/2 si q impair, 0 si q pair
        assert K == q * (q + 1) // 2 + exces                             # l'identité exacte, vraie pour toute famille de q+1 droites
        assert une_droite_par_direction(q, d, F)
        assert exces == paires                                           # l'excès est le nombre de paires {a, -a} : 0 si q pair, (q-1)/2 si q impair
        print(q, K, q * (q + 1) // 2, exces, K == q * (q + 1) // 2 + exces, dict(sorted(mult.items())), fixes, paires, True)
```

### 7.2 Optionnel : l'aire exacte de Perron à 4 branches

Hors du plan. À reprendre dans la partie « nouveaux tests » si N2 est retenue : l'aire en fractions pour des rapports rationnels, sur le segment α₀α₁ = ½ et dans la zone. Lancé dans un dossier temporaire : ½ exactement sur les 5 points du segment, P² + (1 − P)² sur les 3 points de la zone, et 322/625 hors zone *(calculé ici)*.

```python
"""Perron à 4 branches : aire exacte en fractions. Repère affine (les rapports d'aires sont conservés) : base [0, 2], sommet à la hauteur 1,
donc aire du grand triangle = 1. Construction de la partie V : blocs voisins recollés, puis rapprochés (rapport a à chaque étage)."""
from fractions import Fraction as Fr
from itertools import combinations


def arbre(alphas):
    n = 2 ** len(alphas)
    xs = [Fr(2 * i, n) for i in range(n + 1)]
    l, r, ax = xs[:-1], xs[1:], [Fr(1)] * n
    blocs = [(i, i + 1, l[i], r[i]) for i in range(n)]
    for a in alphas:                                        # du plus fin au plus grossier
        nouv = []
        for j in range(0, len(blocs), 2):
            (s1, _, u1, v1), (s2, e2, u2, v2) = blocs[j], blocs[j + 1]
            larg = (v1 - u1) + (v2 - u2)
            dx = (v1 - u2) - (1 - a) * larg                 # le bloc de droite glisse de dx
            for i in range(s2, e2):
                l[i] += dx
                r[i] += dx
                ax[i] += dx
            nouv.append((s1, e2, u1, u1 + a * larg))
        blocs = nouv
    return l, r, ax


def largeur(l, r, ax, y):                                   # longueur de l'union des tranches à la hauteur normalisée y
    tot, fin = Fr(0), None
    for a, b in sorted((l[i] + (ax[i] - l[i]) * y, r[i] + (ax[i] - r[i]) * y) for i in range(len(l))):
        if fin is None or a > fin:
            tot, fin = tot + b - a, b
        elif b > fin:
            tot, fin = tot + b - fin, b
    return tot


def aire(alphas):
    l, r, ax = arbre(alphas)
    bords = [(p, ax[i]) for i in range(len(l)) for p in (l[i], r[i])]
    ys = {Fr(0), Fr(1)}
    for (p, a), (q, b) in combinations(bords, 2):           # les hauteurs où deux bords se croisent
        if (a - p) != (b - q) and 0 < (q - p) / ((a - p) - (b - q)) < 1:
            ys.add((q - p) / ((a - p) - (b - q)))
    ys = sorted(ys)                                         # entre deux hauteurs consécutives la largeur est affine : trapèzes exacts
    return sum((largeur(l, r, ax, y0) + largeur(l, r, ax, y1)) * (y1 - y0) / 2 for y0, y1 in zip(ys, ys[1:]))


if __name__ == "__main__":
    assert aire([Fr(2, 3)]) == Fr(2, 3) and aire([Fr(3, 4), Fr(2, 3)]) == Fr(1, 2)            # contrôles de la partie V
    assert aire([Fr(4, 5), Fr(3, 4), Fr(2, 3)]) == Fr(2, 5)
    for a0 in (Fr(3, 5), Fr(13, 20), Fr(2, 3), Fr(7, 10), Fr(3, 4)):                         # le segment a0 * a1 = 1/2
        print("segment", a0, Fr(1, 2) / a0, aire([a0, Fr(1, 2) / a0]))
    for a0, a1 in [(Fr(7, 10), Fr(7, 10)), (Fr(7, 10), Fr(3, 4)), (Fr(13, 20), Fr(4, 5))]:  # dans la zone : aire = P^2 + (1 - P)^2
        P = a0 * a1
        print("zone", a0, a1, aire([a0, a1]), P * P + (1 - P) ** 2)
    print("hors zone", aire([Fr(4, 5), Fr(3, 5)]), "contre", Fr(12, 25) ** 2 + (1 - Fr(12, 25)) ** 2)
```

### 7.3 Optionnel : la trace « miroir + complément »

Hors du plan. À reprendre si N4 est retenue. Il lit un certificat de Dzoba comme une donnée (JSON) et n'exécute aucun code externe. Lancé sur `venn17-local-c3-s2` : « miroir + complément » 2,3, rang 1 sur 31 ; complément seul 0,87 ; plus grand rapport des autres 1,28 *(calculé ici)*. Pour un certificat à 19 courbes, compter environ vingt-cinq secondes.

```python
"""« Miroir + complément » : part des croisements dont l'image par (i -> a*i, avec ou sans complément) est un croisement,
comparée au hasard qui tient compte des classes de paires {i, j}. Données : certificats de Dzoba lus comme des données (JSON)."""
import json
import sys
from collections import Counter
from math import gcd

import numpy as np

DEPOT = "/home/user/dzoba/venn17/certificates/"


def clefs(A):                                              # un croisement = 4 étiquettes, triées
    B = np.sort(A, axis=1)
    return [(int(a) << 60) | (int(b) << 40) | (int(c) << 20) | int(d) for a, b, c, d in B.tolist()]


def trace(nom):
    dd = json.load(open(DEPOT + nom + ".json"))
    n = int(dd["n"])
    F = np.array([[int(x, 2) for x in f] for f in dd["faces"]], dtype=np.int64)
    V, plein = len(F), (1 << n) - 1
    diff = np.bitwise_or.reduce(F, axis=1) ^ np.bitwise_and.reduce(F, axis=1)   # les deux bits qui bougent
    cl = Counter()
    for x in diff.tolist():
        b = [k for k in range(n) if (x >> k) & 1]
        cl[min((b[1] - b[0]) % n, (b[0] - b[1]) % n)] += 1                      # classe de la paire {i, j}
    Phi = n * 2 ** (n - 2)                                                     # 2-faces du cube Q_n dans une classe de paires : n paires, 2^(n-2) faces chacune
    ens, res = set(clefs(F)), {}
    for a in range(1, n):
        if gcd(a, n) != 1:
            continue
        T = np.zeros(1 << n, dtype=np.int64)
        for i in range(n):
            T |= ((np.arange(1 << n) >> i) & 1).astype(np.int64) << ((a * i) % n)
        for comp in (False, True):
            if a == 1 and not comp:
                continue
            H = T[F] ^ plein if comp else T[F]
            f = sum(1 for c in clefs(H) if c in ens) / V
            nul = sum((cl[d] / V) * (cl[min((a * d) % n, n - (a * d) % n)] / Phi) for d in cl)
            res[(a, comp)] = f / nul
    tete = sorted(res, key=res.get, reverse=True)
    print(nom, "n =", n, "| miroir + complément :", round(res[(n - 1, True)], 2), "rang", 1 + tete.index((n - 1, True)),
          "sur", len(res), "| complément seul :", round(res[(1, True)], 2), "| plus grand rapport des autres :",
          round(max(v for k, v in res.items() if k != (n - 1, True)), 2))


if __name__ == "__main__":
    trace(sys.argv[1])        # ex. : venn17-local-c3-s2
```

## 8. Les corrections au recouvrement

Bloc JSON proposé pour le dossier, au format du § 1.9 du plan :

```json
{
  "moities-et-crans": {
    "parties": ["I", "II", "IV", "V", "VI", "VIII", "X", "XIV", "XV", "XVI", "XVII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVII", "XXVIII", "XXIX", "XXX"],
    "fiches": ["005", "010", "012"]
  }
}
```

**À ajouter** (8 parties et une fiche), avec la raison :

| partie ou fiche | sections | pourquoi | force |
|---|---|---|---|
| VI | § 3, § 5 | le simplexe est l'ordre 1 de l'involution (E[τ] = 0, XXIV § 1) ; la lunule d'Hippocrate a l'aire ½ sans π, et ses deux cercles sont à un cran | moyenne |
| X | § 5 | la corde de Ptolémée de l'arc 70,81° : c'est la partie qui portait déjà le lien de la fiche 010 | forte |
| XV | § 3, § 6 | la chèvre comptée sur la grille (ligne 18) ; la table des valeurs de § 6 range ensemble le deltoïde (π/8 contre π/4 : la moitié) et Kakeya fini (la moitié du plan), et l'anneau de liens juste au-dessus cite la FTM50 ; aucun des trois n'est rapproché des autres | moyenne |
| XVI | § 3 | le plateau 2^(−1/n) : la dilatation en toute dimension, nommée et mesurée ; elle n'est aujourd'hui que dans `corde-et-dimensions` | forte |
| XIX | § 6 | le cône conjugué de l'hémisphère (z = r = 1/√2, la moitié du disque) et la chèvre infinie à la distance de Rayleigh (aire ×2) | moyenne |
| XXIII | § 4, § 5 | le tableau du grain est le tableau des procédés ; « toutes les dimensions tiennent dans un cran » | forte |
| XXV | § 1.2 | la série de la dimension infinie, resommée, redonne la chèvre plane : le retour de l'involution à l'équation (§ 3.3, maillon 8) | forte |
| XXVIII | § 2.2–2.4, § 3.1–3.2 | Perron à k = 2 (théorèmes 1 à 3) ; Fermat et les 7 710 formes, qui rendent la moitié exacte possible (fiche 005) | forte |
| fiche 012 | — | Bonferroni à l'ordre 1 : la même inégalité que Kakeya fini à l'ordre 2 (K4, T5) | moyenne |

**À envisager, plus faible** : XVIII § 5 (la chèvre en pixels, avec des bornes certaines).

**À retirer : rien.** Chaque partie du dossier porte au moins une ligne de l'inventaire : I (1–6), II (7–11), IV (12), V (13–15), VIII (4), XIV (16–17), XVII (3, 19), XX (20–21), XXI (22–23), XXII (21), XXIV (25), XXVII (26–28), XXIX (29–30), XXX (31–35). Les fiches 005 et 010 restent (§ 4).

**Effet sur le nerf** *(calculé ici, avec le bloc JSON du plan, § 1.9, au niveau « fiches + parties » ; effet mécanique)*. Les tétraèdres creux passent de 6 à 3 et les triangles vides de 20 à 17 ; plus aucun triangle vide ne contient `moities-et-crans` (il y en avait 3). Qui remplit quoi : X remplit le tétraèdre aiguilles · grain · lumière · moities ; XXVIII remplit les tétraèdres aiguilles · bases · moities · ombres et aiguilles · lumière · moities · ombres ; XXV remplit le triangle aiguilles · corde · moities ; XV remplit le triangle corde · grain · moities ; XIX et XXVIII remplissent le triangle bases · lumière · moities. Les trois tétraèdres creux qui restent sont aiguilles · hasard · lumière · moities, aiguilles · hasard · lumière · ombres et bases · corde · hasard · moities. Le nerf mesure des appartenances, pas du contenu (T1 : p = 0,39 au niveau des parties) : je donne ces chiffres pour que l'agent `croisement` sache où mes ajouts agissent, pas comme une preuve. Je laisse ouvert le triangle bases · corde · moities, vide au niveau des fiches seules : la partie XXI le réunit, mais le seul contenu qui le remplirait (les 6,644 crans par décade) est déjà dans XXI § 3 et XXIV § 5, sans observation nouvelle à écrire.
