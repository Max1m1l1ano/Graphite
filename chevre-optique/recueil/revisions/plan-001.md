# Révision 001 — plan de synthèse et rapport de lancement du workflow

*Date : 2026-10-07. Auteur du plan : agent Opus de la révision 001.*
*État : complet. Écrit section par section (le squelette d'abord, pour survivre à un redémarrage).*

## 0. Cadre et sources

**Ce que ce plan fait.** Il prépare la révision 001 du recueil (CLAUDE.md, § 10, « La révision », étape 1). Il ne révise rien lui-même : il dit quels dossiers écrire, quels liens tester, et quels agents Sonnet lancer. La synthèse viendra ensuite, dans `recueil/revisions/revision-001.md`.

**Pourquoi maintenant.** `recueil/index.md` compte 15 fiches, toutes non révisées : c'est le haut de la fourchette (11 à 15). Il n'y a encore aucun fichier `recueil/arcs/arc-NNN.md`. La révision couvre donc les fiches 001 à 015 et, à travers elles, les 30 parties.

**Ce que j'ai lu.**
- `CLAUDE.md` en entier (§ 1, § 6, § 6 bis et § 10 surtout) ;
- `recueil/README.md`, `recueil/index.md`, `recueil/arcs/README.md` et les 15 fiches ;
- `resultats/recueil_verifications.md` ;
- `README.md` (les lignes « Et : [Partie …] ») et `carte-connexions.md` (partie XXVII) ;
- `git log --stat -6` : parties XXV à XXX, puis la mise en place du recueil (commit 92814fc) ;
- les documents, scripts et résultats cités dans les sections suivantes, au besoin.

**D'où viennent les fiches.** Elles ne couvrent pas le corpus de façon égale. C'est un biais de départ, et il faut le dire :
- les fiches 001 à 012 viennent des parties XXIX et XXX (le Venn à 17 et son centre) ;
- les fiches 013 à 015 viennent du message fondateur du recueil (`scripts/recueil_verifications.py`) ;
- aucune fiche ne vient des parties I à XXVIII, sinon par leurs renvois.

Les dossiers doivent donc couvrir les 30 parties, et pas seulement les fiches. Les parties sans fiche sont le premier trou du recueil lui-même (voir § 6).

**Les étiquettes de ce plan.** Comme dans « Le tri » des parties :
- **établi** : démontré, calculé ou classique, avec la partie et le fichier `resultats/…` qui le portent ;
- **même procédé** : une analogie de structure, donc un résultat (CLAUDE.md, § 1) ;
- **ma lecture** : un rapprochement que je propose, pas encore calculé ;
- **à calculer** : un nombre que la révision doit produire. Je n'en écris aucun sans source.


## 1. Les dossiers thématiques

**Le principe.** Les dimensions D1 à D8 rangent les fiches par sujet. Les dossiers les recomposent par **procédé** : un dossier réunit les chaînes qui partagent une même construction (une équation, une ombre, un groupe, un budget de grain). Deux dossiers peuvent donc partager une partie : c'est voulu, c'est le nerf (test T1).

**Huit dossiers.** Ils couvrent les 30 parties (chaque partie tombe dans 1 à 5 dossiers, 2,9 en moyenne) et les 15 fiches (2,3 dossiers en moyenne). Le dossier `moities-et-crans` est la vraie recomposition : il prend la moitié de l'aire dans D1, D4, D5 et D6 à la fois. Le dossier `lumiere-et-physique` réunit D4 et D8, parce que D8 n'a aucune chaîne propre (§ 1.0).

**Ce que veut dire « englober ».** L'agent du dossier lit la partie, au moins les sections indiquées, avec son script, ses résultats et ses figures. Les parties en **gras** sont le noyau du dossier.

### 1.0 La table des 30 parties

Chemins vérifiés avec `ls` (les figures sont dans `figures/`). La « dimension naïve » est le classement de départ : une seule dimension par partie, chaque partie étant une chaîne (un message de l'auteur). C'est ma lecture ; elle sert au Venn multidimensionnel du § 2.

| partie | document | scripts | résultats | figures | dim. naïve | dossiers |
|---|---|---|---|---|---|---|
| I | `README.md` | `scripts/chevre.py`, `scripts/calculs.py`, `scripts/figures.py` | `resultats/resultats.md` | `fig1_geometrie.png`, `fig2_contour_ullisch.png`, `fig3_dimensions.png`, `fig4_volume_surface.png`, `fig5_diagramme_parametres.png`, `fig6_courbes50_dimensions.png`, `fig7_optique.png`, `fig8_anneaux_newton.png`, `fig9_eclipses.png` | D1 | corde, moitiés, lumière |
| II | `archimede.md` | `scripts/archimede.py`, `scripts/calculs_archimede.py`, `scripts/figures_archimede.py` | `resultats/archimede.md` | `b1_six_projections.png`, `b2_tranches_archimede.png`, `b3_cube_tournant.png`, `b4_menisque.png`, `b5_riemann_lebesgue_contour.png`, `b6_dimensions_unite.png`, `b7_cordes_2D_3D.png`, `b8_glissement_50.png`, `b9_polygones_polyedres.png` | D6 | moitiés, lumière, ombres |
| III | `pi-dimensions.md` | `scripts/pi_dimensions.py` | `resultats/pi_dimensions.md` | `c1_pi_dimensions.png` | D1 | corde, bases, méthode |
| IV | `trois-solides.md` | `scripts/trois_solides.py` | `resultats/trois_solides.md` | `d1_trois_solides.png` | D1 | corde, moitiés |
| V | `aiguille-kakeya.md` | `scripts/aiguille.py` | `resultats/aiguille.md` | `e1_aiguille_kakeya.png` | D5 | moitiés, aiguilles |
| VI | `zone-confusion.md` | `scripts/zone_confusion.py` | `resultats/zone_confusion.md` | `f1_zone_confusion.png`, `f2_dimension_reelle.png`, `f3_menisque_croisement.png` | D1 | corde, méthode |
| VII | `nombres-polynomes.md` | `scripts/polynomes.py` | `resultats/polynomes.md` | `g1_polynomes_retenues.png`, `g2_virgule_binaire.png` | D1 | corde, bases |
| VIII | `foyer-fibonacci.md` | `scripts/foyer_fibonacci.py` | `resultats/foyer_fibonacci.md` | `h1_foyer_menisques.png`, `h2_fibonacci.png` | D4 | moitiés, lumière |
| IX | `moire-fibonacci.md` | `scripts/moire_fibonacci.py` | `resultats/moire_fibonacci.md` | `i1_moire_fibonacci.png`, `i2_optique_racines.png` | D4 | bases, lumière |
| X | `carre-ptolemee.md` | `scripts/carre_ptolemee.py` | `resultats/carre_ptolemee.md` | `j1_carre_ptolemee.png` | D4 | grain, lumière, aiguilles |
| XI | `angle-or-aiguilles.md` | `scripts/angle_or_aiguilles.py` | `resultats/angle_or_aiguilles.md` | `k1_angle_or_aiguilles.png` | D2 | bases, lumière |
| XII | `lentille-144.md` | `scripts/lentille_144.py` | `resultats/lentille_144.md` | `l1_lentille_144.png` | D2 | bases, lumière |
| XIII | `perron-dephasage.md` | `scripts/perron_dephasage.py` | `resultats/perron_dephasage.md` | `m1_perron_dephasage.png` | D5 | lumière, aiguilles, méthode |
| XIV | `aiguille-grille.md` | `scripts/aiguille_grille.py` | `resultats/aiguille_grille.md` | `n1_aiguille_grille.png`, `n2_perron_grille.png` | D5 | moitiés, bases, grain, aiguilles |
| XV | `grille-decalee.md` | `scripts/grille_decalee.py` | `resultats/grille_decalee.md` | `o1_grille_decalee.png` | D6 | corde, grain, ombres |
| XVI | `menisque-projection.md` | `scripts/menisque_projection.py` | `resultats/menisque_projection.md` | `p1_contacts_disques.png`, `p2_menisque_projection.png` | D1 | corde |
| XVII | `recursion-argent.md` | `scripts/recursion_argent.py` | `resultats/recursion_argent.md` | `q1_recursion_argent.png`, `q2_newton_polyedres.png` | D1 | moitiés, lumière, aiguilles |
| XVIII | `pixels-longitudes.md` | `scripts/pixels_longitudes.py` | `resultats/pixels_longitudes.md` | `r1_pixels_contacts.png`, `r2_longitudes_lumiere.png` | D3 | grain, lumière, méthode |
| XIX | `bases-objets.md` | `scripts/bases_objets.py` | `resultats/bases_objets.md` | `t1_bases_modulaires.png`, `t2_trait_cone_thales.png` | D2 | bases, lumière, aiguilles |
| XX | `sphere-faisceaux.md` | `scripts/sphere_faisceaux.py` | `resultats/sphere_faisceaux.md` | `u1_chevres_faisceaux.png`, `u2_cartes_losange.png` | D6 | corde, moitiés, lumière, ombres |
| XXI | `vingt-quatre-miroir.md` | `scripts/vingt_quatre_miroir.py` | `resultats/vingt_quatre_miroir.md` | `v1_vingt_quatre.png`, `v2_racine_sept.png` | D2 | corde, moitiés, bases, ombres |
| XXII | `carre-neuf-points.md` | `scripts/carre_neuf_points.py` | `resultats/carre_neuf_points.md` | `w1_carre_neuf_points.png` | D1 | corde, moitiés, ombres |
| XXIII | `lentilles-boules-grain.md` | `scripts/lentilles_boules_grain.py` | `resultats/lentilles_boules_grain.md` | `x1_lentilles_boules_grain.png` | D3 | corde, grain |
| XXIV | `tiers-dimension.md` | `scripts/tiers_dimension.py` | `resultats/tiers_dimension.md` | `y1_tiers_dimension.png` | D1 | corde, moitiés, méthode |
| XXV | `tranche-aiguilles.md` | `scripts/tranche_aiguilles.py` | `resultats/tranche_aiguilles.md` | `z1_ouverts.png`, `z2_tranche_aiguilles.png` | D1 | corde, bases, aiguilles |
| XXVI | `kakeya-miroir.md` | `scripts/kakeya_miroir.py` | `resultats/kakeya_miroir.md` | `aa1_kakeya.png`, `aa2_virgule_miroir.png`, `aa3_cube_hexagone.png` | D5 | bases, aiguilles, ombres |
| XXVII | `carte-connexions.md` | `scripts/carte_connexions.py` | `resultats/carte_connexions.md` | `ab1_carte.png`, `ab2_cercles_arctiques.png`, `ab3_liens_predits.png` | D7 | moitiés, aiguilles, ombres, méthode |
| XXVIII | `octaedre-perron-venn.md` | `scripts/octaedre_perron_venn.py` | `resultats/octaedre_perron_venn.md` | `ac1_octaedre.png`, `ac2_perron.png`, `ac3_venn17.png` | D6 | bases, lumière, aiguilles, ombres |
| XXIX | `venn-ppm.md` | `scripts/venn_ppm.py` | `resultats/venn_ppm.md` | `ad1_venn_ppm.png`, `ad2_deux_ombres.png` | D6 | moitiés, grain, ombres, méthode |
| XXX | `centre-venn.md` | `scripts/centre_venn.py` | `resultats/centre_venn.md` | `ae1_centre_moitie.png`, `ae2_diaphragmes_diffraction.png`, `ae3_grains_hasard.png` | D3 | moitiés, grain, lumière, ombres, méthode |

**Le partage des aires, au départ.** Avec une aire de 1/30 par partie : D1 10, D6 5, D2 4, D5 4, D3 3, D4 3, D7 1, **D8 0**. La chèvre (D1) prend un tiers du Venn. D8 est vide : dans ce classement, aucune partie n'a la physique pour sujet principal ; elle entre partout comme analogie (le laser, les étoiles doubles, Newton, Planck). C'est un premier trou du classement naïf (§ 6.1).

### 1.1 `recueil/dossiers/corde-et-dimensions.md` — la corde de toutes les dimensions

- **Question directrice.** Quel procédé unique fait passer la corde de la chèvre plane (Ullisch, 1,1587) à la diagonale √2 de la chèvre infinie, et que transporte-t-il d'une dimension à l'autre : le simplexe, le ménisque, le plan de la lentille, la série ?
- **Projection sur D1–D8** (ma lecture) : D1 0,6 ; D6 0,2 (le simplexe, les faisceaux) ; D3 0,1 (le grain changé en dimensions) ; D2 0,1 (les décimales de la corde).
- **Parties.** **I** (§ 2–5), III (§ 4–5), IV (§ 1–3, 5), **VI** (§ 3 à 3 quater), VII (§ 1–4), XV (§ 2–3), **XVI** (§ 1–2, 6), **XX** (§ 1–2), XXI (§ 5), **XXII** (§ 1–2), **XXIII** (§ 2), **XXIV** (en entier), **XXV** (§ 1).
- **Fiches.** 010 (Ullisch broute 39,34 % de chaque anneau), 014 (√2 et √3 en fractions continues).
- **Ce qui les réunit.** Chaque partie calcule, démontre ou relit un terme de ρ_n : l'équation unique (VII, XX), le simplexe (VI), le ménisque (XVI, XXIV), le plan à 1/(n + 1) (XXIII), la série et sa divergence (XXIV, XXV).

### 1.2 `recueil/dossiers/moities-et-crans.md` — la moitié et le cran √2

- **Question directrice.** Toutes les moitiés du corpus viennent-elles de quelques procédés seulement (une involution sans point fixe, une dilatation d'un cran, une équation, une inclusion–exclusion) ? Où ces procédés se rejoignent-ils : au rayon R/√2, à la corde √2 ?
- **Projection sur D1–D8** : D1 0,4 ; D6 0,3 (le complément, les hémisphères) ; D4 0,2 (les crans, la FTM50) ; D5 0,1 (le deltoïde, Kakeya sur une grille finie).
- **Parties.** **I** (§ 4.2, 6.4), II (§ 8), IV (§ 4), V (§ 1, 3), VIII (§ 3), XIV (§ 5), **XVII** (§ 1–3), **XX** (§ 3), **XXI** (§ 3), XXII (§ 1), XXIV (§ 5), XXVII (§ 2), **XXIX** (§ 3.3, 5.2), **XXX** (§ 2–4).
- **Fiches.** 005 (la moitié exacte du Venn à 19 courbes), 010.
- **Ce qui les réunit.** La définition même de la chèvre : la moitié de l'aire. Ce dossier ne refait pas la corde ; il compare les façons d'obtenir une moitié.

### 1.3 `recueil/dossiers/bases-congruences-premiers.md` — bases, congruences et premiers

- **Question directrice.** Quelles congruences (même reste modulo b, même groupe d'unités, même réduite) relient les bases, les puissances, les périodes et les premiers ? Quelles coïncidences de chiffres survivent au changement de base ?
- **Projection sur D1–D8** : D2 0,8 ; D5 0,1 (l'aiguille dont la pente est i) ; D6 0,1 (Henderson, Fermat).
- **Parties.** III (§ 1–3), VII (§ 5, 7), IX (§ 3–4), **XI** (§ 2, 5), XII (§ 2–3), XIV (§ 1, 3–4), **XIX** (§ 2–4, 9), **XXI** (§ 1–2), XXV (§ 2–3), **XXVI** (§ 2), XXVIII (§ 3.1, 3.2, 3.6), et `scripts/recueil_verifications.py`.
- **Fiches.** 001 (2⁻¹⁷ et 5¹⁷), 005 (Fermat rend la moitié possible), 013 (1/7 et les racines digitales), 014, 015 (les dizaines de premiers).
- **Ce qui les réunit.** Le groupe des unités modulo b et ses éléments d'ordre 2 et 4 : les reflets, les quarts de tour, i.

### 1.4 `recueil/dossiers/grain-pixels-centres.md` — le grain, les pixels et les centres

- **Question directrice.** Que peut trancher un grain fini (un pixel, un ppm, un chiffre, une case de grille) ? À quel taux le grain s'échange-t-il contre des dimensions, des courbes ou des étages ?
- **Projection sur D1–D8** : D3 0,7 ; D4 0,1 (le flou) ; D5 0,1 (Perron sur une grille) ; D7 0,1 (le budget d'une mesure).
- **Parties.** X (§ 2–3), XIV (§ 6), XV (§ 3), **XVIII** (en entier), **XXIII** (§ 3–4), **XXIX** (§ 1–4), **XXX** (§ 1, 2.4, 6).
- **Fiches.** 001, 006 (le centre de la lumière selon la pesée), 007 (le premier centre faux), 008 (le centre au millième de pixel), 011 (le centre du Venn à 19 courbes à la limite).
- **Ce qui les réunit.** Le budget : combien de bits chaque pas achète (partie XXIX, § 4 ; partie XXVII, § 3).

### 1.5 `recueil/dossiers/lumiere-et-physique.md` — la lumière et les analogies physiques

- **Question directrice.** Quelles lois optiques et physiques suivent exactement le même procédé que la géométrie de la chèvre et du Venn, et que transportent-elles : une valeur, une prédiction, une méthode de mesure ?
- **Projection sur D1–D8** : D4 0,6 ; D8 0,3 ; D3 0,1.
- **Parties.** **I** (§ 6), II (§ 3, 9), **VIII** (en entier), IX (§ 1–3), X (§ 1, 6), XI (§ 3–4), XII (§ 1, 4), XIII (§ 1–4), XVII (§ 5), XVIII (§ 6–7), **XIX** (§ 6), **XX** (§ 4, 6), **XXVIII** (§ 3.3), **XXX** (§ 1.2, 4.5, 5, 6.1, 6.3).
- **Fiches.** 002 (le diésis et la lumière du 17-gone), 006, 009 (les 34 + 34 aigrettes).
- **Ce qui les réunit.** La lentille F(δ, k) de la partie I, la FTM, et le cône à sommet imaginaire de la partie XIX (CLAUDE.md, § 1).

### 1.6 `recueil/dossiers/aiguilles-kakeya-perron.md` — aiguilles, Kakeya et Perron

- **Question directrice.** Comment le grain plafonne-t-il la descente de Perron et de Kakeya ? Les aiguilles de la grille (Fibonacci, Pell, pythagoriciennes) sont-elles les mêmes réduites que celles des bases et des crans ?
- **Projection sur D1–D8** : D5 0,7 ; D2 0,1 (les réduites) ; D3 0,1 (le grain) ; D6 0,1 (l'ombre du cube).
- **Parties.** **V** (en entier), X (§ 4), **XIII** (§ 1, 3, 6), **XIV** (en entier), XVII (§ 4), XIX (§ 2, 6), XXV (§ 3), **XXVI** (§ 1, 3.6), XXVII (§ 7), **XXVIII** (§ 2, 3.3–3.5).
- **Fiches.** 003 (34·tan(π/34) ≈ π), 011.
- **Ce qui les réunit.** Retourner une aiguille dans peu de place : le recouvrement de toutes les directions.
- **Remarque.** D5 n'a aucune fiche principale (`recueil/index.md`) : ce dossier doit en proposer (§ 6.1).

### 1.7 `recueil/dossiers/ombres-cube-venn.md` — les ombres du cube, les polytopes et le Venn

- **Question directrice.** Le cube {0, 1}ⁿ et ses ombres (une direction quelconque, la grande diagonale, l'ombre symétrique Σωⁱ) sont-ils le groupe commun du Venn, de Perron, de l'octaèdre, des cercles arctiques et des premiers par position ?
- **Projection sur D1–D8** : D6 0,8 ; D5 0,1 (Perron) ; D2 0,1 (Henderson, Fermat).
- **Parties.** **II** (§ 1–2), XV (§ 1), **XX** (§ 3, 5), XXI (§ 1, 4), XXII (§ 3–4), **XXVI** (§ 3), **XXVII** (§ 2, 4, 8), **XXVIII** (§ 1, 3), **XXIX** (§ 1–2, 5), XXX (§ 3).
- **Fiches.** 003, 004 (35,8 % contre 35,10 %), 005, 006, 008, 009, 010, 015.
- **Ce qui les réunit.** Le cube et ses projections, et le procédé de Čech de la partie XX (le nerf).

### 1.8 `recueil/dossiers/hasard-et-methode.md` — le hasard et la méthode

- **Question directrice.** Pour chaque observation, quelle technique de test convient (la table du § 10 de CLAUDE.md) ? Le verdict reste-t-il dans le budget de la donnée ? Où les chaînes de production de données du corpus ont-elles accumulé, puis corrigé, des erreurs ?
- **Projection sur D1–D8** : D7 0,8 ; D3 0,2.
- **Parties.** III (§ 2), **VI** (§ 3 bis, 3 ter), XIII (§ 5), XVIII (§ 5), XXIV (§ 1), **XXVII** (§ 1), **XXIX** (§ 5.5), **XXX** (§ 7).
- **Fiches.** 002, 003, 004, 005, 007, 012 (les tests à tolérance), 015.
- **Ce qui les réunit.** La loi de l'écart : faire varier le paramètre (partie XXX, § 7). Ce dossier est écrit en second, par un agent de vérification croisée (§ 5).

### 1.9 Le recouvrement exact (bloc JSON pour le nerf)

Les clés sont les noms de fichier des dossiers. Les parties sont en chiffres romains, les fiches en numéros à trois chiffres. Le nerf se calcule sur l'union `parties ∪ fiches` de chaque dossier (test T1). Le recouvrement corrigé par les agents (v2) aura le même format (§ 5, agent `croisement`).

```json
{
  "revision": "001",
  "dossiers": {
    "corde-et-dimensions": {
      "parties": ["I", "III", "IV", "VI", "VII", "XV", "XVI", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV"],
      "fiches": ["010", "014"]
    },
    "moities-et-crans": {
      "parties": ["I", "II", "IV", "V", "VIII", "XIV", "XVII", "XX", "XXI", "XXII", "XXIV", "XXVII", "XXIX", "XXX"],
      "fiches": ["005", "010"]
    },
    "bases-congruences-premiers": {
      "parties": ["III", "VII", "IX", "XI", "XII", "XIV", "XIX", "XXI", "XXV", "XXVI", "XXVIII"],
      "fiches": ["001", "005", "013", "014", "015"]
    },
    "grain-pixels-centres": {
      "parties": ["X", "XIV", "XV", "XVIII", "XXIII", "XXIX", "XXX"],
      "fiches": ["001", "006", "007", "008", "011"]
    },
    "lumiere-et-physique": {
      "parties": ["I", "II", "VIII", "IX", "X", "XI", "XII", "XIII", "XVII", "XVIII", "XIX", "XX", "XXVIII", "XXX"],
      "fiches": ["002", "006", "009"]
    },
    "aiguilles-kakeya-perron": {
      "parties": ["V", "X", "XIII", "XIV", "XVII", "XIX", "XXV", "XXVI", "XXVII", "XXVIII"],
      "fiches": ["003", "011"]
    },
    "ombres-cube-venn": {
      "parties": ["II", "XV", "XX", "XXI", "XXII", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"],
      "fiches": ["003", "004", "005", "006", "008", "009", "010", "015"]
    },
    "hasard-et-methode": {
      "parties": ["III", "VI", "XIII", "XVIII", "XXIV", "XXVII", "XXIX", "XXX"],
      "fiches": ["002", "003", "004", "005", "007", "012", "015"]
    }
  }
}
```

### 1.10 Les projections sur D1–D8 (bloc JSON pour le Venn des dimensions)

Ma lecture, à corriger par les agents. Les poids de chaque dossier font 1. La seconde clé donne le classement naïf des 30 parties (une dimension chacune, § 1.0). Ce bloc sert au test T2 (« après » la révision) et au § 2.

```json
{
  "revision": "001",
  "projection_des_dossiers": {
    "corde-et-dimensions": {"D1": 0.6, "D6": 0.2, "D3": 0.1, "D2": 0.1},
    "moities-et-crans": {"D1": 0.4, "D6": 0.3, "D4": 0.2, "D5": 0.1},
    "bases-congruences-premiers": {"D2": 0.8, "D5": 0.1, "D6": 0.1},
    "grain-pixels-centres": {"D3": 0.7, "D4": 0.1, "D5": 0.1, "D7": 0.1},
    "lumiere-et-physique": {"D4": 0.6, "D8": 0.3, "D3": 0.1},
    "aiguilles-kakeya-perron": {"D5": 0.7, "D2": 0.1, "D3": 0.1, "D6": 0.1},
    "ombres-cube-venn": {"D6": 0.8, "D5": 0.1, "D2": 0.1},
    "hasard-et-methode": {"D7": 0.8, "D3": 0.2}
  },
  "parties_dimension_naive": {"I": "D1", "II": "D6", "III": "D1", "IV": "D1", "V": "D5", "VI": "D1", "VII": "D1", "VIII": "D4", "IX": "D4", "X": "D4", "XI": "D2", "XII": "D2", "XIII": "D5", "XIV": "D5", "XV": "D6", "XVI": "D1", "XVII": "D1", "XVIII": "D3", "XIX": "D2", "XX": "D6", "XXI": "D2", "XXII": "D1", "XXIII": "D3", "XXIV": "D1", "XXV": "D1", "XXVI": "D5", "XXVII": "D7", "XXVIII": "D6", "XXIX": "D6", "XXX": "D3"}
}
```

## 2. La structure « en Perron »

### 2.0 Comment lire ce paragraphe

- Un **arbre** a des **branches** : ce sont des chaînes de parties et de fiches, dans l'ordre où le corpus les a produites.
- Les branches se rejoignent dans le **triangle du bas** : le groupe, le procédé ou l'objet qu'elles partagent. C'est leur projection commune, comme l'arbre de Perron se lit dans sa coupe du bas (partie XXVIII, § 3.5).
- Le triangle est posé dans un **disque** du Venn : la dimension où il vit. Quand il touche plusieurs disques, l'information s'y est rejointe.
- Chaque arbre porte deux marques : **établi** (par le même procédé, avec la partie qui le montre) et **ma lecture** (à confirmer par un test ou par un dossier).

### 2.1 La diagonale √2, d'où l'on part

**Établi** (l'outil de l'agent de session, `scripts/revision_001.py`, § 1 ; CLAUDE.md, § 10) :
- la classification naïve, à parts égales et centrée, est le simplexe régulier : arête d_K = √(2K/(K − 1)), et corde vers l'antipode c_K = √(2(K − 2)/(K − 1)), avec d² + c² = 4 (Thalès) ;
- la chèvre de dimension n a exactement la corde c_K pour K = n + 2 + (N − n), où N − n est le tiers de dimension de la partie XXIV. Les deux côtés de l'angle droit tendent vers √2, l'un par en dessus, l'autre par en dessous ;
- à parts inégales, deux classes rares paraissent liées exactement quand p_a + p_b < Σp² : c'est un lien du cadre, pas un lien de contenu.

**Où l'on en est.**
- Les fiches : K = 6 dimensions occupées, arête 1,5492 (`recueil/index.md`).
- Les 30 parties, classées naïvement (§ 1.0) : K = 7 dimensions occupées (D8 est vide). À parts égales, l'arête vaudrait √(14/6) = 1,528.
- **Ma lecture du but.** Une révision « réussie » ne rapproche pas tout de √2. Elle sépare deux populations : les paires liées par un même procédé, qui passent sous √2 (comme la corde de la chèvre), et les paires indépendantes, qui restent à l'arête du simplexe. Le test T2 mesure cette séparation.

### 2.2 Les huit arbres

| arbre | triangle du bas | disque | fiches | statut |
|---|---|---|---|---|
| P1 | l'ombre du cube {0, 1}ⁿ | D6 (contre D5, D2) | 003, 004, 005, 008, 009, 015 | établi pour Venn–Perron–34 ; lecture pour les premiers |
| P2 | la moitié : involution, dilatation, équation | D1 (contre D4, D6) | 005, 010 | établi au rayon R/√2 et à la corde √2 ; ouvert pour la grille finie |
| P3 | le terme x²/6 (la courbure du second ordre) | D1 (contre D4) | 002, 003, 011 | établi au second ordre ; ouvert au-delà |
| P4 | le quart de tour i modulo b | D2 (contre D5) | 001, 013, 014 | établi (XIX, test 4.1) ; lecture pour la famille b = q² + 1 |
| P5 | le budget en bits, log₂(1/ε) | D3 (contre D5) | 006, 007, 008, 011 | établi |
| P6 | les réduites et les trois distances | D2 (contre D5, D4) | 002, 014 | établi |
| P7 | la loi de l'écart (faire varier le paramètre) | D7 (contre D3) | 002, 003, 004, 005, 007, 012 | établi, avec la réserve du § 10 |
| P8 | le cône à sommet imaginaire | D8 (contre D1, D4) | 006 | établi pour le laser ; lecture pour Wielen |

**P1 — L'ombre du cube {0, 1}ⁿ.** Disque D6.
- *Branche Venn.* XXVIII § 3.1–3.2 (Henderson ; 7 710 formes, c'est Fermat) → XXIX § 5.4 (l'ombre Σωⁱ : son centre ne reçoit que ∅ et tout si et seulement si n est premier ; contour à 34 côtés) → XXX § 3 (le complément, la sphère) → fiches 005, 008, 009.
- *Branche Perron.* V § 3 (2/(k + 2)) → XXVIII § 2.4 et § 3.5 (le plateau prouvé par l'ombre du cube ; chaque coupe est un Venn à une dimension) → XXIX § 5.1 (deux ombres : binaire contre binomiale) → fiche 003.
- *Branche du cube qui tourne.* II § 2 → XXVI § 3 (l'ombre ‖u‖₁) → XXVII § 4 (les 26 directions) → XXVIII § 1 (l'octaèdre, 35,10 %) → fiche 004, un rameau de hasard.
- *Branche des premiers.* Fiche 015 (chaque dizaine est un sommet de {0, 1}⁴) → test 4.2 de l'agent de session (Hardy–Littlewood).
- *Le triangle.* Le cube {0, 1}ⁿ projeté sur une direction. Une direction quelconque donne le binaire (Perron) ; la grande diagonale, la binomiale (Venn) ; l'ombre symétrique, un polygone à 2n côtés si n est impair (le 34) ; les axes d'ordre 3 et 4, les cercles arctiques (XXVIII § 1.3).
- *Statut.* **Établi** pour Venn et Perron (XXIX § 5.1 ; XXVIII § 3.5), Perron et l'ombre (XXVIII § 2.4), le 34 (XXIX § 5.4). **Ma lecture** pour les premiers : la face choisie par le reste modulo 3 est-elle une ombre du cube {0, 1}⁴, ou seulement une restriction à une face ? Question à l'agent `ombres`.

**P2 — La moitié.** Disque D1.
- *Branche involution.* XX § 3 (les deux hémisphères ; l'inversion de rayon √2) → XXX § 3 (le complément ; deux miroirs, un seul cercle R/√2) → XVII § 3 (les jumeaux d·d′ = ½) → fiche 005, un rameau : aucune involution connue ne force la moitié des croisements.
- *Branche dilatation.* I § 6.4 (le cran 1/√2) → XXI § 3 (doubler l'aire, c'est un pas de √2) → XXIX § 3.3 (une courbe de plus, un cran) → XXX § 2.2 (chaque cran de diaphragme garde la moitié) ; et VIII § 3 (la FTM50).
- *Branche équation.* I § 3 (Ullisch) → IV § 4 (la corde qui prend la moitié de chaque solide) → XXX § 4.3 (trois chèvres) → fiche 010.
- *Branche grille finie.* XIV § 5 (Kakeya modulo q : les carrés font la moitié) → test T5.
- *Branche Kakeya.* V § 1 et § 3 (le deltoïde, l'arbre de Perron à 4 branches).
- *Le triangle* (**ma lecture**, à tester) : un groupe ℤ/2 qui agit sans point fixe, ou une mesure homogène (l'aire en r²).
- *Statut.* **Établi** : l'involution et la dilatation se rejoignent au même cercle R/√2 (XXX § 3, le complément et Lambert). **Établi** : la moitié par équation rejoint la moitié par involution à l'infini, puisque la chèvre infinie a la corde √2 de l'hémisphère (XX § 1 ; XXII § 1). **Ouvert** : la branche de la grille finie (la piste XIV–XX de XXVII § 9). Le test T5 dit si c'est le même procédé.

**P3 — Le terme x²/6.** Disque D1.
- *Branche chèvre.* V § 2 (0,35 %) → VI § 3 (le simplexe) → XVI § 2 (r² = 1 + projection + ménisque) → XXIII § 2 (le plan à 1/(n + 1)) → XXIV § 1 (2/(3n²) = 2 × 1/6 × 2) → XXV § 1 (ordres 2 à 8, divergence).
- *Branche diaphragme inscrit.* II § 9 (l'erreur des polygones) → XXVIII § 3.3 (97,74 % ; 2π²/(3·17²)) → XXIX § 4 (« la même forme x²/6 ») → XXX § 7 (S2 : l'écart fois N⁴ tend vers 2π⁴/15) → fiche 002, un rameau de hasard (le diésis).
- *Branche polygone circonscrit.* XXVIII § 2.5 (2N·tan(π/2N)) → fiche 003 (la loi π³/(12N²)).
- *Branche du centre du Venn.* Fiche 011 (**ma lecture** : congruence K10 du § 3).
- *Le triangle.* Intégrer un profil de courbure ½ : ∫₀^x (1 − u²/2) du = x − x³/6.
- *Statut.* **Établi** pour la chèvre (XXIV § 1 : la courbure de l'équateur) et pour le polygone (classique), et l'égalité de forme au second ordre (XXIX § 4). **Ouvert** (XXIX § 6) : est-ce le même ménisque au-delà du second ordre ? Test T3.

**P4 — Le quart de tour i modulo b.** Disque D2.
- *Branche des bases.* XIX § 2 (3 ≡ i modulo 10 ; une base a un i exactement quand elle est le carré de la longueur d'une aiguille de la grille qui ne touche aucun autre point) → XXI § 2 (7² ≡ −1 modulo 50) → XXV § 3 (i modulo 50 et 53) → XXVIII § 3.6 (4 ≡ i modulo 17).
- *Branche des fractions continues.* Fiche 014 (multiplier par i alterne ±i ; √2 = ±i dans F₉).
- *Branche des racines digitales.* Fiche 013 → test 4.1 de l'agent de session (seul (10, 7) répond, hors des cas triviaux) → la famille b = q² + 1 (K3 du § 3).
- *Branche du miroir 2 ↔ 5.* XXVI § 2 (2⁻ʲ = 5ʲ·10⁻ʲ) → fiche 001.
- *Le triangle.* Le groupe des unités modulo b et son élément d'ordre 4 (i) ; pour b = 10, le découpage ℤ/10 = ℤ/2 × ℤ/5, d'où le miroir 2 ↔ 5.
- *Statut.* **Établi** : le théorème de XIX et le balayage 4.1. **Ma lecture**, contrôlée vite : la famille b = q² + 1 recolle 013 et XIX (K3).

**P5 — Le grain plafonne la profondeur.** Disque D3.
- *Branche Perron sur une grille.* XIV § 6 (1/log n ; le produit par log₂ n reste vers 2,8) → XXVI § 1 (Kakeya au grain δ, borne de Córdoba) → XXVIII § 2.5 (la fenêtre à 10⁻⁵⁰ : 0,01344 à 0,02096).
- *Branche de la série.* XXIV § 2 (la meilleure précision 2^(−n/2)/n) → XXV § 1.1 → XXVII § 3 (316 dimensions à 10⁻⁵⁰ ; 6,644 par décade ; le logarithme, « la marche 0 »).
- *Branche du Venn.* XXIX § 4 (un bit par courbe) → XXX § 6.4 (le centre, goulot) → fiches 011, 008, 006, 007.
- *Branche des pixels.* XVIII § 3–5 (un chiffre certain par niveau) → XXIII § 4 (les taux de change ε⁻², ε⁻¹, ε^(−1/2)).
- *Le triangle.* Le budget en bits, log₂(1/ε) : chaque pas (une dimension, une courbe, un étage) achète un nombre fixe de bits, ou seulement un logarithme.
- *Statut.* **Établi** (XXVII § 3 ; XXIX § 4 ; XXX § 6.4).

**P6 — Les réduites et les trois distances.** Disque D2.
- *Branche de l'angle d'or.* XI § 2 → XII § 2–3 (55/144 et 89/144 de tour) → IX § 2 (les deux familles dans le rapport φ).
- *Branche des aiguilles de la grille.* XIV § 1 et § 3 (le 3-4-5 ; la demi-case de Pick) → XV § 5 (Eisenstein, le 5-7-8) → XVII § 4 et XXVII § 7 (Pell, l'argent).
- *Branche des crans.* XIX § 4 (log₁₀ 2 ; deux longueurs seulement pour 10 et 93 points) → XX § 6 (le comma, les gammes) → XXVI § 2.5 (21 crans, trois écarts : 128/125, 625/512 et 5/4) → fiche 002 (le diésis est l'un des trois écarts).
- *Branche des fractions continues.* Fiche 014.
- *Le triangle.* Le théorème des trois distances (Sós, Surányi, Świerczkowski) et les réduites d'une fraction continue : deux voisines ont un déterminant ±1.
- *Statut.* **Établi** : les parties XI, XIV, XV, XIX, XX et XXVI se citent sur ce point.

**P7 — La loi de l'écart.** Disque D7.
- *Branche de la lignée des tests.* III § 2 (« ça marche » ne prouve rien) → VI § 3 bis (les dimensions non entières : la bosse) → XIII § 5 (la bande 2,44 – 2,56) → XXIX § 5.5 (le catalogue brouillé) → XXX § 7 (le banc d'essai) → fiche 012.
- *Branche de la précision poussée.* XVII § 6 (la corde certifiée par intervalles) → XX § 1 (50 chiffres) → XXIV § 1 (la borne 1 800/n³).
- *Branche des biais de chaîne.* Fiche 007 (le point de départ) → fiche 006 (la pesée) → test T4 (l'ordre de dessin).
- *Branche des hasards testés.* Fiches 002, 004, 005 ; tests 4.1 et 4.2 de l'agent de session.
- *Le triangle.* Faire varier le paramètre et lire la loi de l'écart (XXX § 7).
- *Statut.* **Établi**, avec la réserve écrite au § 10 de CLAUDE.md : cette épreuve n'est pas indépendante de la conclusion.

**P8 — Le cône à sommet imaginaire.** Disque D8.
- *Branche du faisceau.* XIX § 6 (le cube qui tourne, la chèvre infinie et le faisceau gaussien : r = θ·|z + i·z_R|, Deschamps 1971 ; pour la chèvre, ρ = |d + i|, et au piquet la largeur vaut √2 fois le col, la phase de Gouy 45°) → XX § 1 (la chèvre infinie au même piquet que la chèvre plane) → XXI § 3 (au point de Rayleigh, l'aire double : Self 1983).
- *Branche du photocentre.* XXX § 1.2 (Wielen 1996) → fiche 006.
- *Branche des directions au hasard.* XX § 6 (√2 entre deux directions au hasard, dans une IA).
- *Le triangle.* La source ponctuelle complexe : un cône dont le sommet est déplacé dans l'imaginaire.
- *Statut.* **Établi** pour le faisceau (CLAUDE.md, § 1 ; XIX). **Ma lecture** : la branche du photocentre relève peut-être d'un autre triangle (le barycentre pesé). Le test T4 le dira.

### 2.3 Le Venn multidimensionnel, après la révision

- **Avant.** Chaque partie est une chaîne posée dans un seul disque, avec une aire de 1/30 (§ 1.0). Chaque fiche aussi (`recueil/index.md`).
- **Après.** Chaque triangle du bas est posé à l'intersection des disques qu'il touche (tableau du § 2.2). Les dossiers ont leurs poids sur D1–D8 (§ 1.10).
- **Ce que la révision doit dessiner** (ma proposition pour `figures/rev001_perron_venn.png`, dont l'agent de session a déjà le panneau a) :
  - b. les huit arbres : leurs branches qui descendent vers les triangles, posés dans les disques ;
  - c. le nerf du recouvrement (T1), aux niveaux « fiches » et « fiches + parties » ;
  - d. les distances entre fiches avant et après (T2), avec la ligne √2.
- **Ce qui s'affirme.** D'une révision à l'autre, le nombre K de dimensions grandit et l'arête du simplexe naïf descend vers √2. Les chaînes qui se rejoignent dans un même triangle passent sous √2. C'est la lecture de l'auteur, rendue mesurable par T2.

## 3. Les congruences à tester

### 3.0 Ce qu'on appelle ici une congruence

- Chaque fiche, chaque résultat de partie, est une **section locale** : vraie dans son cadre (sa partie, son script, sa précision).
- Deux sections **se recollent** si elles coïncident sur ce qu'elles partagent, à une transformation connue près (un changement de variable, un reste modulo b, un facteur d'un cran). C'est une congruence, pas une égalité : « égal modulo x³ », « égal modulo 2 », « égal à un cran près ».
- Sur trois sections deux à deux recollées, on vérifie que les trois transformations se composent (la condition de cocycle, comme dans le procédé de Čech de la partie XX).
- Ce qui ne se recolle pas est une **obstruction**. Elle désigne un trou : la donnée ou l'observation qui manque pour recoller.
- Le cadre de référence existe : la cohomologie de Čech des faisceaux, déjà utilisée par la partie XX ; et, pour des données locales qui ne se recollent pas en une donnée globale, l'approche par faisceaux d'Abramsky et Brandenburger (§ 6.3).

### 3.1 Le tableau des congruences

| | ce qui est comparé | la transformation | se recolle jusqu'où | obstruction probable | test |
|---|---|---|---|---|---|
| K1 | le ménisque de la chèvre et la lumière du polygone (P3) | x = 2/n ↔ x = 2π/N | le terme x²/6 (établi, XXIX § 4) | l'ordre 3 : la chèvre a −98/(15n³), le polygone n'a que des puissances paires | T3 |
| K2 | les trois 34 : aigrettes, ombre Σωⁱ, éventails de Perron (P1) | N directions et leurs opposées | entièrement (2 est inversible modulo N impair) | aucune | léger, dans T3 ou à part |
| K3 | 1/7, les racines digitales de 2ⁿ, i modulo 10 (P4) | la famille b = q² + 1 | entièrement pour q = 2 et 3 | la période de 1/p reste 6 au-delà | contrôle rapide (fait) |
| K4 | les moitiés : complément, hémisphères, cran, Ullisch, Kakeya fini (P2) | involution, dilatation, équation | au cercle R/√2 et à la corde √2 (établi) | Kakeya fini, si sa moitié survit en caractéristique 2 | T5 |
| K5 | le 17 du Venn (Henderson) et le 17 de i (4² + 1) | aucune connue | non | 19 et 23 ont des Venn mais pas de i | aucun (théorie) |
| K6 | le dipôle de la pesée et le photocentre des étoiles doubles (P8, P5) | un barycentre pesé | qualitativement | les écarts ne suivent pas les premiers harmoniques des poids | T4 |
| K7 | Perron sur une grille, le centre du Venn, Kakeya au grain δ (P5) | le budget en bits | la loi logarithmique (établi) | un facteur 2 dans l'exposant : un cran (établi) | aucun |
| K8 | le 4/3 des puissances sous 10, V₃/V₂ = 4/3, 1/x₀ = n + 4/3 | « 2 l'aire, 3 le volume » (l'auteur) | à tester | trois procédés différents pour une même valeur | T7 |
| K9 | Midy pair et impair, et un Venn des périodes | la tour 2-adique de la période | à tester | les aires ne sont pas égales (2/3 et 1/3 attendus) | T6 |
| K10 | le seuil du centre du Venn et l'isopérimétrie (P3, P5) | n croisements sur un cercle contre l'aire d'un croisement | exact, par les formules de la fiche 011 | aucune ; la correction polygonale est le x²/6 de K1 | dans T3 |

### 3.2 Le détail, congruence par congruence

**K1 — Chèvre et polygone, modulo x³.**
- *Ce qui se recolle* (établi). La chèvre a μ = 2/(3n²) + … (XXIV § 1–2), le polygone inscrit 1 − (N/2π)·sin(2π/N) = x²/6 − x⁴/120 + … avec x = 2π/N. Les deux ont la même forme x²/6 (XXIX § 4). Le procédé commun, à mon sens : intégrer un profil de courbure ½ (XXIV § 1 parle de « la courbure de l'équateur »).
- *L'obstruction* (contrôle rapide du plan, à refaire dans T3). Les coefficients exacts de la chèvre sont dans `resultats/tiers_dimension.md`, § 2 : le troisième est −98/15. Le polygone n'a pas de terme impair. Un décalage n ↦ n + s ne recolle pas l'ordre 3 pour s = 0, 1/3, 1 ou 4/3 ; s = 49/10 l'annule, mais l'ordre 4 reste faux. De plus, les deux séries n'ont pas la même nature : celle de la chèvre diverge au rythme 1/ln √2 (XXIV § 2, XXV § 1.1), celle du sinus converge partout.
- *Le trou désigné* (ma lecture). Les termes impairs de la chèvre viennent de l'asymétrie de la coquille, E[τ³] ≈ −2/n³ (XXIV § 1). Un polygone n'a qu'un rayon. Le bon partenaire de la chèvre serait un diaphragme dont le rayon est distribué (une pupille apodisée, ou défocalisée comme en XXX § 6.3). C'est là qu'il faudrait chercher la suite du ménisque commun.
- *Ce que ça ferme.* L'ouvert de XXIX § 6 (« le même ménisque, au-delà du même exposant ? »).

**K2 — Les trois 34, modulo 2.**
- *Ce qui se recolle* (établi). Les aigrettes d'un diaphragme à N lames (XXVIII § 3.3), le contour de l'ombre Σωⁱ du cube {0, 1}ᴺ (XXIX § 5.4) et les N éventails de Perron posés comme des lames (XXVIII § 3.4) dépendent de la même parité. Pour N impair, les N directions et leurs opposées en font 2N, toutes distinctes (34 pour 17), parce que 2 est inversible modulo N. Pour N pair, elles se superposent deux à deux : N aigrettes, une ombre à N côtés, et des éventails qui couvrent la moitié des directions deux fois et l'autre jamais.
- *Déjà vérifié* : les aigrettes pour 5, 6, 7, 8, 16, 17 et 18 lames (XXVIII § 3.3). *À faire, léger* : l'ombre et les éventails pour N = 3 à 20, pour fermer la règle sur les trois objets à la fois.
- *Pas d'obstruction.* C'est l'exemple d'une **section globale** : le même fait vaut sur les trois dossiers (lumière, aiguilles, ombres).

**K3 — 1/7, les racines digitales et i modulo 10 : la famille b = q² + 1.**
- *Ce qui se recolle* (contrôle rapide du plan avec sympy, à refaire dans le script de la révision). Pour q premier, b = q² + 1 et p = q² − q + 1 :
  - q² ≡ −1 (mod b) : q est le i de la base b (pour b = 10, q = 3, partie XIX) ;
  - q·p ≡ 1 (mod b) : q est l'inverse de p (pour b = 10, 3 × 7 = 21 ≡ 1 ; c'est le mécanisme trouvé par le test 4.1) ;
  - p − 1 = q(q − 1) = φ(b − 1) : les unités modulo p et modulo b − 1 = q² sont aussi nombreuses ;
  - p divise q³ + 1, donc la période de 1/p en base b vaut 6 dès que q ≥ 3.
- *Conséquence.* La période remplit tout le groupe seulement si q(q − 1) ≤ 6 : q = 2 (b = 5, p = 3) et q = 3 (b = 10, p = 7). Ce sont exactement les deux cas non triviaux du balayage 4.1. Les membres suivants de la famille, (50, 43) et (170, 157), ont encore les trois premières propriétés, mais une période 6 seulement.
- *Lecture.* Le 3 de la fiche 013 et le i modulo 10 de la partie XIX sont le même 3. Les fiches 013 et 014 se recollent par la partie XIX. À noter comme nouvelle fiche (exact).

**K4 — Les moitiés.**
- *Ce qui se recolle* (établi). L'involution du complément et la dilatation d'un cran fixent le même cercle R/√2 (XXX § 3) : c'est une section globale de l'arbre P2. La moitié par équation (Ullisch) rejoint celle des hémisphères à l'infini : la chèvre infinie a la corde √2 (XX § 1 ; XXII § 1).
- *L'obstruction candidate.* Kakeya sur une grille finie (XIV § 5) : la moitié y vient des carrés modulo q, donc de l'involution x ↦ −x. En caractéristique 2, cette involution est l'identité. Si la moitié survit pour q = 2, 4, 8, elle vient d'ailleurs.
- *Ma lecture* (contrôle rapide du plan, à refaire dans T5). L'autre procédé possible est l'inclusion–exclusion à l'ordre 2 : q + 1 droites, deux à deux sécantes en un point, couvrent exactement q(q + 1)/2 + Σ_P C(m_P − 1, 2) points (m_P droites passent par P), donc au moins q(q + 1)/2, avec égalité quand aucun point n'est sur trois droites. L'involution ne compterait alors que l'excès (q − 1)/2 des q impairs (Blokhuis et Mazzocca), autant que de paires {x, −x}.
- *Fiche 005.* Aucune involution ne force la moitié des croisements (le diagramme n'est pas symétrique par le complément, XXX § 7.3) : c'est une coïncidence entre entiers, de probabilité 1,6 % par tirage. Le verdict « ouvert » reste juste.
- *Un lien de plus, si T5 le confirme* (ma lecture). L'inégalité de Bonferroni sert deux fois dans le corpus : tronquée à l'ordre 2, elle donne la moitié de Kakeya fini ; tronquée à l'ordre 1, c'est la correction de Bonferroni de la fiche 012. Même procédé : tronquer l'inclusion–exclusion.

**K5 — Le 17 de Henderson et le 17 de i.**
- *Obstruction établie par la théorie.* 17 est premier (Henderson : un Venn symétrique demande un nombre premier ; Griggs, Killian et Savage en construisent un pour chaque premier, XXVIII § 3.1) et 17 = 4² + 1 (4 ≡ i modulo 17, XXVIII § 3.6). Mais les Venn de Dzoba à 19 et 23 courbes existent, alors que 19 et 23 n'ont pas de i (ils valent 3 modulo 4 ; `resultats/recueil_verifications.md`, § 1, donne les bases jusqu'à 40 qui en ont un).
- *Le trou* (à vérifier). Une propriété mesurée des certificats dépend-elle de p modulo 4 ? Avec 11, 13, 17, 19 (et 23 par `/home/user/dzoba/venn17/verify/RESULTS-23.md`), on a trop peu de diagrammes pour trancher : je ne propose pas de test.

**K6 — Le dipôle de la pesée et le photocentre.**
- *Ce qui se recolle* (établi qualitativement, XXX § 1.2). Le centre d'une figure symétrique pesée inégalement se déplace, comme le photocentre d'une étoile double selon la bande (Wielen, 1996).
- *L'obstruction* (lue dans `resultats/centre_venn.md`, § 1). Si seule la couleur de chaque courbe comptait, l'écart serait proportionnel au premier harmonique des 17 poids, avec un facteur géométrique fixe (le fond, plus lourd en clarté L qu'en luminance Y, ne ferait qu'aggraver l'écart ci-dessous). Or :
  - clarté L : premier harmonique 1,6 %, écart 4,51 px ;
  - luminance Y : premier harmonique 4,1 %, écart 0,61 px.
  L'ordre est inversé, et les directions vont de −173° à −131°. Une seule cause ne suffit pas.
- *Le trou désigné* (ma lecture). Une seconde cause : l'ordre de dessin. `/home/user/dzoba/venn17/plotter/plotter_svg.py` (fonction `write_svg`) écrit les 17 courbes dans l'ordre i = 0 à 16 ; à chaque croisement, la courbe écrite après recouvre l'autre. Les aires visibles devraient donc croître avec i. Un essai grossier du plan sur l'image va dans ce sens ; le test T4 doit le refaire proprement. Si c'est confirmé, la fiche 006 garde son analogie (le barycentre pesé), mais sa causalité change : une part de l'écart vient de la chaîne de production de l'image.

**K7 — Le grain plafonne la profondeur, à un cran près.**
- *Ce qui se recolle* (établi). Perron sur une grille (XIV § 6), Kakeya au grain δ (XXVI § 1) et le centre du Venn (XXX § 6.4) suivent une loi logarithmique : le grain plafonne la profondeur.
- *La transformation* (établi, XXIX § 4 et XXX § 6.4). Perron compte un bit par étage en largeur ; le Venn compte un bit par courbe en aire, donc un demi-bit en largeur. Les deux lois sont congrues **modulo un cran** : un facteur 2 sur l'exposant, √2 sur la longueur.
- *Pas d'obstruction*, mais un ouvert déjà connu : la constante de Kakeya au grain δ, entre π/2 et π·ln 2 (XXVIII § 2.5).

**K8 — Les trois 4/3.**
- *La proposition de l'auteur* (CLAUDE.md, § 10, « c'est à tester »). 2 a quatre puissances sous 10, 3 en a trois ; le rapprocher de V₃/V₂ = 4/3 (partie III) et de 1/x₀ = n + 4/3 (partie XXIV).
- *L'obstruction probable.* Le compte dépend de la base. Un contrôle rapide du plan le trouve égal à 4/3 seulement pour 10 ≤ b ≤ 16 (1, 2, 4, 8 et 1, 3, 9) et pour 244 ≤ b ≤ 256 (entre 3⁵ et 2⁸) ; il tend ensuite vers log₂ 3 = 1,585, le rapport du comma de la partie XX. V_(n+1)/V_n tend vers 0. Le 4/3 de 1/x₀ est une constante de la série. Trois procédés différents pour une même valeur : c'est ce que T7 doit montrer ou démentir.
- *Ce qui reste, même si l'obstruction se confirme* : le compte des puissances sous b rejoint l'arbre P6 (les réduites de log₂ 3, dont 19/12).

**K9 — Midy, pair et impair.**
- *La proposition de l'auteur* (CLAUDE.md, § 10). Les premiers à période paire et impaire formeraient « une suite de Venn dimensionnelle, ascendante et descendante ».
- *La congruence à tester.* La valuation 2-adique de la période (impaire, paire, divisible par 4, par 8…) forme une tour. Au-delà du premier étage, chaque étage devrait diviser la part par deux (1/3, 1/3, 1/6, 1/12… attendus, T6) : un arbre de Perron sur les périodes.
- *L'obstruction probable.* Les deux régions n'ont pas la même aire. Hasse (1966) donne la densité des premiers à période paire : 2/3 pour une base comme 10 ou 3, et 17/24 pour la base 2 (à vérifier pour la base 10 exactement). `resultats/recueil_verifications.md`, § 5, donne déjà 49 périodes paires sur 75 entre 7 et 397. Le Venn de Midy est donc un Venn à aires inégales par nature : il faut le dire avant de le dessiner.

**K10 — Le seuil du centre et l'isopérimétrie.**
- *Ce qui se recolle* (exact, à partir des deux formules de la fiche 011). W_centre(n)/W_reste(n) = [(2/π)·√(n(2ⁿ − 2))]/[4·√((2ⁿ − 2)/π)] = √(n/(4π)). Le centre devient le goulot à n = 4π = 12,57, d'où « dès 13 courbes » (XXX § 6.4) ; il coûte un cran de plus (√2) à n = 8π = 25,1.
- *Ma lecture.* 4π est la constante isopérimétrique du cercle (L²/A = 4π) : on compare n croisements posés sur un cercle à l'aire d'un croisement. Si les croisements centraux sont joints par des cordes plutôt que par des arcs, le seuil est multiplié par (π/n)/sin(π/n) = 1 + π²/(6n²) + … : c'est le x²/6 de K1.
- *À noter comme nouvelle fiche* (fait amusant, exact), après vérification dans le script.

### 3.3 Le cocycle, sur deux exemples

- **Un cocycle qui se ferme (arbre P2).** Complément (XXX) → inversion des jumeaux (XVII) → hémisphères (XX) : les trois transformations fixent le même cercle R/√2. La condition de cocycle est vérifiée ; le cercle est une section globale. Dans le nerf, le triangle (moitiés, ombres, corde) doit donc être rempli : il l'est, par les parties XX à XXII et par la fiche 010.
- **Un cocycle qui se ferme au second ordre seulement (arbre P3).** Chèvre → polygone inscrit (x = 2/n ↦ 2π/N), polygone inscrit → polygone circonscrit (sin ↦ tan, aux 2N côtés de XXVIII § 2.5), chèvre → polygone circonscrit. Les trois se composent à l'ordre x², pas à l'ordre x³. L'obstruction est d'ordre 3 : c'est une classe à suivre, et le trou de K1.

## 4. Les nouveaux tests de la révision

**Où ils vont.** Dans `scripts/revision_001.py` (déjà commencé par l'agent de session), avec ses résultats `resultats/revision_001.md` et ses figures `figures/rev001_*.png` (CLAUDE.md, § 10). Chaque test tourne en moins d'une minute avec numpy, scipy, sympy ou mpmath.

**Déjà faits par l'agent de session, à ne pas refaire** (`scripts/revision_001.py`, § 4) :
- 4.1 — fiche 013 : la base varie de 3 à 60 et le premier jusqu'à 400 ; seul (10, 7) répond, hors des cas triviaux ;
- 4.2 — fiche 015 : la taille varie de 10⁴ à 10⁸ ; le rapport par motif dérive, les paires larges restent à 2 (Hardy et Littlewood).

**Ce qui n'est pas refait non plus** : le banc d'essai de XXX § 7 et le catalogue brouillé de XXIX § 5.5. Les tests ci-dessous sont nouveaux, et chacun est rattaché à une congruence du § 3.

| test | sujet | technique (table du § 10 de CLAUDE.md) | dossiers | durée visée |
|---|---|---|---|---|
| T1 | le nerf du recouvrement (outil de l'agent de session) | un signal parmi beaucoup d'essais : nul brouillé, son vrai domaine | tous | ≈ 10 s |
| T2 | la diagonale √2, après la révision (outil de l'agent de session) | variation du paramètre (les poids des aires) | tous | < 1 s |
| T3 | le ménisque x²/6, ordre par ordre (K1, K10) | lien de structure : la loi de l'écart | corde, lumière | < 5 s |
| T4 | le dipôle du centre : la palette ou l'ordre de dessin ? (K6) | mesure : le budget de grain ; puis la loi selon la pesée | grain, lumière | ≈ 10 s |
| T5 | la moitié de Kakeya fini en caractéristique 2 (K4) | lien de structure : faire varier q et sa parité | aiguilles, moitiés | ≤ 60 s |
| T6 | Midy en Perron : la tour 2-adique des périodes (K9) | lien de structure : faire varier la borne et la base | bases | ≈ 20 s |
| T7 | les trois 4/3 (K8) | coïncidence entre entiers : répliquer sur d'autres bases | bases, corde | < 1 s |
| T8 | le nerf contre la carte : deux façons de relier deux parties | un signal parmi beaucoup de paires : permutations | méthode | ≈ 30 s |

### T1 — Le nerf du recouvrement

- **But.** Voir si les dossiers se recollent, et trouver les triangles vides : trois dossiers deux à deux sécants, sans élément commun aux trois.
- **Données.** Le bloc JSON du § 1.9 ; puis le recouvrement corrigé v2 de l'agent `croisement`.
- **Calcul.** Avec `nerf`, `betti` et `triangles_vides` (`scripts/revision_001.py`), à trois niveaux :
  1. les fiches seules (`fiches`) ;
  2. les fiches sans les deux « hasard (testé) », 002 et 004 ;
  3. les fiches et les parties (`fiches ∪ parties`).
  Puis un nul : 1 000 recouvrements tirés en gardant la taille de chaque dossier et le nombre de dossiers de chaque élément (échanges de paires dans la matrice d'appartenance ; Gotelli, 2000 ; Strona et al., 2014). On compare b₁, b₂ et le nombre de triangles vides au nul.
- **Si c'est une structure.** b₀ = 1. Les triples remplis le sont plusieurs fois (par plusieurs parties ou fiches), plus souvent que dans le nul : les liens se concentrent. Les triangles vides qui restent sont les mêmes en v1 et en v2 : ils ne dépendent pas de mes choix de classement.
- **Si c'est un hasard.** La distribution des multiplicités, b₁ et le nombre de triangles vides tombent dans celle du nul, et les triangles vides changent entre v1 et v2.
- **La lecture des triangles vides.** Un triangle vide au niveau 1 qui se remplit au niveau 3 est un **trou du recueil** : la partie qui recolle existe, il manque la fiche. Un triangle qui reste vide au niveau 3 est un **trou du corpus** : aucune partie ne réunit les trois sujets.
- **Le niveau 2 en plus.** Un triangle qui se vide quand on retire les fiches « hasard » est un trou couvert par une coïncidence : la coïncidence a été notée exactement là où manquait une observation de structure. C'est une lecture possible du sujet d'étude de l'auteur (« des motifs qui paraissent un hasard mais concernent des relations dimensionnelles »).
- **Précautions.**
  - Au niveau 3, presque toutes les paires de dossiers se coupent (chaque dossier a 7 à 14 parties) : il faut lire les générateurs de H₁ et H₂ (les cycles), pas la liste des triangles vides.
  - Le nerf dépend du recouvrement, donc de mes choix : refaire le calcul sur la v2. Ce qui change entre v1 et v2 était un trou de classement, pas un trou de données.

### T2 — La diagonale √2, après la révision

- **But.** Mesurer si les fiches liées par un même procédé passent sous √2, et si les autres restent à l'arête du simplexe.
- **Données.** L'appartenance des 15 fiches aux 8 dossiers (§ 1.9), et les projections des dossiers sur D1–D8 (§ 1.10).
- **Calcul.**
  - Vecteurs d'appartenance des fiches aux dossiers, en deux versions : brute, et **à aires égales** (chaque colonne divisée par son nombre de fiches). Centrer, normaliser, puis prendre les 105 distances entre fiches.
  - Séparer les paires qui partagent un dossier des autres. Comparer les deux distributions à √2 et à l'arête √(2K/(K − 1)), K = 8, soit 1,512.
  - Appliquer la règle des liens du cadre (p_a + p_b < Σp², `scripts/revision_001.py`, § 2) aux dossiers : quelles paires de dossiers rares paraissent liées sans rien partager ?
  - En D1–D8 : les fiches projetées par les poids du § 1.10, avant et après.
- **Si c'est une structure.** Deux groupes séparés : les paires liées sous √2, les autres près de l'arête du simplexe. La version à aires égales efface les liens du cadre.
- **Si c'est un hasard.** Pas de séparation, la même qu'après une permutation des appartenances (1 000 permutations).

### T3 — Le ménisque x²/6, ordre par ordre (K1 et K10)

- **But.** Trancher l'ouvert de XXIX § 6 : le ménisque de la chèvre et celui du polygone sont-ils le même, au-delà du même exposant ?
- **Données.** Les coefficients exacts μ_j de la chèvre, j = 2 à 12 (`resultats/tiers_dimension.md`, § 2) ; les quantités du polygone, avec sympy.
- **Calcul.**
  1. Développer en 1/N : 1 − (N/2π)·sin(2π/N) (lumière du polygone inscrit), 2N·tan(π/2N)/π − 1 (polygone circonscrit, XXVIII § 2.5, fiche 003) et (π/n)/sin(π/n) − 1 (centre du Venn joint par des cordes, K10).
  2. Chercher un changement de variable N = c·(n + s), avec c et s rationnels simples, qui recolle la chèvre et le polygone aux ordres 2, 3, 4. Écrire l'écart, ordre par ordre.
  3. Comparer la croissance des coefficients : rapport μ_(j+1)/μ_j (la chèvre : ≈ −j·2/ln 2, `resultats/tiers_dimension.md`, § 2) contre celui du sinus.
  4. Pour K10 : vérifier W_centre/W_reste = √(n/4π) sur le tableau de XXX § 6.4, et calculer le seuil avec des cordes.
- **Si c'est le même ménisque.** Un c et un s simples recollent au moins les ordres 2 à 4.
- **Si c'est seulement le même exposant.** Recollement à l'ordre 2 (c = π, le même 1/6) et obstruction dès l'ordre 3. Le contrôle rapide du plan va dans ce sens (§ 3.2, K1) : le script doit l'écrire proprement.
- **Le trou.** L'asymétrie de la coquille (XXIV § 1) n'a pas de partenaire polygonal à un seul rayon (§ 3.2).

### T4 — Le dipôle du centre : la palette ou l'ordre de dessin ? (K6)

- **But.** Trouver la cause de l'écart du centre de la lumière (0,6 à 46 px, fiche 006), et tester l'analogie avec le photocentre des étoiles doubles.
- **Données.** L'image `/home/user/dzoba/venn17/images/venn17-pressure-dark-2000.png` (copie locale du dépôt de Dzoba, CC BY 4.0), la palette et l'ordre d'écriture des courbes dans `/home/user/dzoba/venn17/plotter/plotter_svg.py` (fonctions `palette` et `write_svg`), et les six barycentres de `resultats/centre_venn.md`, § 1. Lire ce code, ne pas l'exécuter.
- **Calcul.**
  1. Classer chaque pixel d'encre par sa teinte OKLab (17 teintes h = 25° + 360°·i/17), avec un seuil de distance à la couleur de la palette, et le centre de symétrie (999,497 ; 999,499) de `resultats/centre_venn.md`, § 1.
  2. Mesurer pour chaque courbe i son aire visible A_i et son centroïde c_i. Régresser A_i sur l'indice i (l'ordre de dessin).
  3. Modèle à deux causes : écart(pesée) = facteur géométrique × [H₁(palette, pesée) + H₁(ordre)], où H₁ est le premier harmonique complexe (poids des couleurs d'une part, aires visibles d'autre part). Ajuster sur les six pesées (douze nombres, quatre paramètres réels : le facteur géométrique et H₁(ordre), tous deux complexes) et lire les résidus.
  4. Comparer au modèle à une seule cause (la palette).
- **Si c'est l'ordre de dessin (avec la palette).** A_i croît avec i ; le modèle à deux causes reproduit les six écarts et leurs directions, dont la luminance (où les deux dipôles se compensent) ; le modèle à une cause échoue.
- **Si c'est un hasard de classification.** A_i plates à la précision du classement ; aucun modèle simple ne passe ; il faut chercher ailleurs (anticrénelage, seuils, fond).
- **Le budget.** La précision du centre de symétrie est 0,003 px (`resultats/centre_venn.md`, § 1) : les six écarts sont des mesures, pas du bruit. La limite est celle du classement des pixels mêlés aux croisements ; le script doit l'estimer (par exemple en changeant le seuil).
- **Le trou** (§ 6.2). L'ordre de dessin d'une image vectorielle publiée est une variable cachée de sa chaîne de production.

### T5 — La moitié de Kakeya fini, en caractéristique 2 (K4)

- **But.** Dire si la moitié de XIV § 5 (Kakeya sur une grille finie) est le même procédé que les hémisphères (une involution), ou un autre (l'inclusion–exclusion). C'est la première piste encore ouverte de la carte (XIV–XX, XXVII § 9).
- **Données.** `minimum_kakeya` de `scripts/aiguille_grille.py` (optimisation en nombres entiers, scipy `milp`), écrit pour q premier.
- **Calcul.**
  1. L'étendre aux corps F_q, q = 2, 3, 4, 5, 7, 8, 9 (et 11, 16 si le temps le permet), par des tables d'addition et de multiplication (polynômes irréductibles x² + x + 1 pour F₄, x³ + x + 1 pour F₈, x² + 1 pour F₉, x⁴ + x + 1 pour F₁₆).
  2. Imposer trois droites par symétrie, comme la partie XIV, et une limite de temps par q.
  3. Noter le minimum, et compter dans un ensemble minimal les points couverts 1, 2, 3 fois ou plus.
- **Si la moitié vient de l'involution x ↦ −x.** Elle change de forme pour q = 2, 4, 8, où cette involution est l'identité.
- **Si elle vient de l'inclusion–exclusion** (Bonferroni à l'ordre 2). Pour q + 1 droites, une par direction, deux droites se coupent toujours en un point, d'où l'identité exacte |K| = q(q + 1)/2 + Σ_P C(m_P − 1, 2), où m_P est le nombre de droites qui passent par P. Le minimum vaut alors q(q + 1)/2 pour q pair, sans aucun point triple (c'est possible avec une hyperovale, qui n'existe qu'en caractéristique 2 : à vérifier dans la littérature), et q(q + 1)/2 + (q − 1)/2 pour q impair (Blokhuis et Mazzocca), l'excès Σ_P C(m_P − 1, 2) valant (q − 1)/2 (par exemple (q − 1)/2 points triples, comme dans la construction de la parabole). La moitié est alors indépendante de la caractéristique, et l'involution ne compte que l'excès.
- **Si c'est un hasard.** Pas de loi simple selon q.
- **Contrôle rapide du plan** (sans réduction par symétrie, à refaire) : q = 2, 4, 8 donnent 3, 10 et 36 ; q = 3, 5, 7 donnent 7, 17 et 31. q = 7 prend environ 50 s et q = 9 dépasse la minute : il faut la réduction par symétrie.
- **Ce que ça change.** Si l'inclusion–exclusion est confirmée, la piste XIV–XX se ferme par une obstruction : les deux moitiés ne viennent pas du même procédé. Un autre lien s'ouvre, avec la fiche 012 (§ 3.2, K4).

### T6 — Midy en Perron : la tour 2-adique des périodes (K9)

- **But.** Tester la lecture de l'auteur : les premiers à période paire et impaire formeraient un Venn dimensionnel, « ascendant et descendant ».
- **Données.** Rien à lire : on calcule. Le point de départ est `resultats/recueil_verifications.md`, § 5 (49 périodes paires sur 75, de 7 à 397).
- **Calcul.**
  1. Pour les premiers p < 10⁶ (sauf 2 et 5), la période L(p) = ord_p(10) (sympy, `n_order`).
  2. La part des L pairs ; les parts de v₂(L) = 0, 1, 2, 3… (la tour 2-adique) ; les parts de ℓ | L pour ℓ = 3, 5, 7 (Midy étendu à ℓ blocs).
  3. Faire varier la borne (10³ à 10⁶) et la base (2, 3, 7, 10, 12).
- **Si c'est une structure.** La part paire tend vers 2/3 en base 10 et vers 17/24 en base 2 (Hasse, 1966). Les parts de v₂(L) = 0, 1, 2, 3… tendent vers 1/3, 1/3, 1/6, 1/12… : à partir du premier étage, chaque étage divise la part par deux, comme les fentes d'un arbre de Perron. La part de ℓ | L tend vers ℓ/(ℓ² − 1), soit 3/8, 5/24 et 7/48 (valeurs attendues pour une base générique, à vérifier dans la littérature).
- **Si c'est un hasard.** Des parts qui fluctuent sans converger, ou qui restent à ½ (le partage naïf).
- **Le contrôle rapide du plan** (à refaire) donne déjà 0,667 en base 10 et 0,708 en base 2 à 10⁵, puis, en base 10 sous 2·10⁵, 0,334, 0,334, 0,165 et 0,083 pour v₂ = 0 à 3, et 0,376, 0,206 et 0,145 pour ℓ = 3, 5 et 7. La structure est donc attendue. Le test sert surtout à mesurer la tour, et à dire que le Venn de Midy a des aires inégales.

### T7 — Les trois 4/3 (K8)

- **But.** Tester le rapprochement proposé par l'auteur entre les puissances sous 10 (4 pour 2, 3 pour 3), V₃/V₂ = 4/3 et 1/x₀ = n + 4/3.
- **Calcul.**
  1. Pour chaque base b de 3 à 10⁶ : c₂(b) et c₃(b), les nombres de puissances de 2 et de 3 inférieures à b ; leur rapport ; les bases où il vaut 4/3 ; sa limite.
  2. Les rapports V_(n+1)/V_n et la constante de 1/x₀ (4/3, puis −112/45…, `resultats/tiers_dimension.md`, § 2), en fonction de n.
  3. Chercher une loi qui relie c₂/c₃ à l'une des deux suites quand b et n varient.
- **Si c'est une structure.** Une même loi relie le compte des puissances et la géométrie (par exemple une famille de bases où c₂/c₃ suit V_(n+1)/V_n).
- **Si c'est une coïncidence de petits nombres.** c₂/c₃ ne vaut 4/3 que sur deux fenêtres de bases (10 à 16, puis 244 à 256, d'après le contrôle rapide du plan) et tend vers log₂ 3 = 1,585 ; aucune loi commune avec la géométrie. Le lien qui reste est celui de log₂ 3 avec le comma (arbre P6).

### T8 — Le nerf contre la carte : deux méthodes pour relier deux parties

- **But.** Comparer deux méthodes qui mettent deux parties en corrélation : les voisins communs dans le graphe des renvois (Adamic–Adar, partie XXVII) et les dossiers partagés (le recouvrement).
- **Données.** `python3 scripts/carte_connexions.py 30` (≈ 20 s ; il n'écrit rien) pour les paires reliées et l'indice des paires non reliées ; le bloc du § 1.9.
- **Calcul.** Pour chaque paire de parties non reliée : l'indice d'Adamic–Adar et le nombre de dossiers partagés. Corrélation de rang (Spearman), et la même après 1 000 permutations des étiquettes des parties. La place des cinq pistes : XIV–XX, VI–VIII, XIV–XXIV, VI–XXI, V–IX.
- **Si les deux méthodes voient la même structure.** Corrélation positive nette ; les pistes partagent au moins un dossier.
- **Si c'est un hasard.** Corrélation dans la distribution des permutations.
- **La réserve.** J'ai fait le recouvrement en lisant des résumés qui contiennent les renvois : les deux méthodes ne sont pas indépendantes. Le script doit le dire, et le mesurer en refaisant le calcul sur les paires que ni l'une ni l'autre ne relie directement.

## 5. Le rapport de lancement du workflow

### 5.0 Vue d'ensemble

- **Neuf agents Sonnet**, en deux phases.
  - **Phase 1** (sept agents en parallèle) : un agent par dossier thématique, qui écrit ce dossier.
  - **Phase 2** (deux agents en parallèle, après la phase 1) : deux agents de vérification croisée qui lisent tous les dossiers. `methode` écrit le huitième dossier (`hasard-et-methode.md`), qui est transversal ; `croisement` écrit `recueil/revisions/verification-croisee-001.md` (le recouvrement v2, les congruences, les triangles vides, les arbres corrigés, les trous).
- **Ce que les agents ne font pas.** Ils ne lancent aucun script du dépôt et n'écrivent que leur fichier. Ils préparent les tests T1 à T8 (le code minimal, dans leur section 7) ; l'agent de session les calcule ensuite dans `scripts/revision_001.py`.
- **Les chemins** des listes ci-dessous ont été vérifiés avec `ls` (par un script du plan), sauf les sept dossiers de la phase 1, que la phase 1 crée.

| label | phase | sortie | fichiers | questions |
|---|---:|---|---:|---:|
| `corde` | 1 | `recueil/dossiers/corde-et-dimensions.md` | 55 | 7 |
| `moities` | 1 | `recueil/dossiers/moities-et-crans.md` | 60 | 7 |
| `bases` | 1 | `recueil/dossiers/bases-congruences-premiers.md` | 53 | 8 |
| `grain` | 1 | `recueil/dossiers/grain-pixels-centres.md` | 42 | 7 |
| `lumiere` | 1 | `recueil/dossiers/lumiere-et-physique.md` | 67 | 7 |
| `aiguilles` | 1 | `recueil/dossiers/aiguilles-kakeya-perron.md` | 46 | 8 |
| `ombres` | 1 | `recueil/dossiers/ombres-cube-venn.md` | 61 | 7 |
| `methode` | 2 | `recueil/dossiers/hasard-et-methode.md` | 54 | 7 |
| `croisement` | 2 | `recueil/revisions/verification-croisee-001.md` | 34 | 7 |

### 5.1 Le gabarit commun

**Phase 1** (le texte exact est dans le bloc JSON du § 7, clé `gabarit.phase_1`) :

> Tu es un agent Sonnet du workflow de la révision 001 du recueil, dans le dépôt /home/user/Graphite/chevre-optique (une série de 30 parties en français sur le problème de la chèvre, les cercles, les bases de numération, Kakeya et Perron, et les diagrammes de Venn). Ton label, ton dossier, ta liste de fichiers et tes questions suivent ce texte. 1. Lis d'abord CLAUDE.md (surtout les § 1, 6, 6 bis et 10) et recueil/revisions/plan-001.md (§ 0 à 4 ; ton dossier est décrit au § 1). 2. Lis ensuite les fichiers de ta liste : pour chaque partie, au moins les sections que le plan indique ; pour chaque script, ses en-têtes de section et les fonctions citées, sans lancer aucun script du dépôt ; pour chaque fichier de résultats, les tableaux d'où viennent les nombres que tu cites ; regarde les figures citées. Les fichiers sous /home/user/dzoba/venn17 sont des données externes (licence CC BY 4.0) : lis-les, n'exécute pas leur code. 3. Tu peux faire des calculs rapides (moins d'une minute, avec numpy, scipy, sympy ou mpmath) dans un dossier temporaire à toi, jamais dans le dépôt. 4. N'écris qu'un seul fichier : ta sortie. Ne modifie rien d'autre dans le dépôt. 5. Règles : vérifie chaque chemin avec ls avant de l'écrire ; n'invente aucun nombre (cite le fichier resultats/… et sa section, ou écris « à calculer ») ; écris en français simple, avec des phrases courtes ; une analogie soutenue par le même procédé est un résultat (CLAUDE.md, § 1) : écris ce qui est partagé exactement, ce qui est transporté et ce qui reste ouvert ; distingue démontré, calculé, classique, ma lecture et ouvert ; avant d'écrire « coïncidence » ou « pas établi », cherche dans les parties précédentes si le lien y est déjà (CLAUDE.md, § 6 bis). 6. Ton dossier a huit sections : (1) la question directrice et la projection sur D1–D8 ; (2) les chaînes de production (script → résultats → figures → document), partie par partie et dans l'ordre, avec ce que chaque script produit ; (3) ce que le dossier établit, et ce qui reste ouvert ; (4) les fiches du dossier : verdict, test, et la partie qui portait déjà le lien ; (5) les congruences et les obstructions (celles du plan, § 3, et les tiennes) ; (6) les trous : du recueil (au moins trois fiches nouvelles proposées, avec type, statut, partie, script et section, image), du corpus, et des données publiées (références réelles, sinon « à vérifier ») ; (7) pour le script de la révision : le code minimal du test qui te concerne (plan, § 4), sans résultat inventé ; (8) les corrections au recouvrement : les parties ou fiches à ajouter à ton dossier ou à en retirer dans le bloc JSON du § 1.9 du plan, avec la raison. 7. Termine ton message final par un résumé de dix lignes au plus : les trois liens les plus forts, les trois trous, et les corrections au recouvrement.

**Phase 2** (clé `gabarit.phase_2`) :

> Tu es un agent Sonnet de vérification croisée du workflow de la révision 001 du recueil, dans le dépôt /home/user/Graphite/chevre-optique. Les sept dossiers de la phase 1 sont écrits dans recueil/dossiers/ : lis-les tous, ainsi que CLAUDE.md (§ 1, 6, 6 bis et 10) et recueil/revisions/plan-001.md en entier. Ton label, ta sortie, ta liste de fichiers et tes questions suivent ce texte. Règles : ne lance aucun script du dépôt (calculs rapides permis dans un dossier temporaire à toi) ; n'écris qu'un seul fichier, ta sortie ; vérifie chaque chemin avec ls ; n'invente aucun nombre (cite le fichier resultats/… et sa section, ou le dossier qui le donne, ou écris « à calculer ») ; écris en français simple, avec des phrases courtes ; une analogie soutenue par le même procédé est un résultat (CLAUDE.md, § 1). Si un dossier de la phase 1 manque, dis-le en tête de ta sortie et travaille avec les autres. Termine ton message final par un résumé de dix lignes au plus.

### 5.2 Les neuf agents

#### 5.2.1 `corde` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/corde-et-dimensions.md`.
- **Fichiers à lire** :
  - documents : `README.md`, `pi-dimensions.md`, `trois-solides.md`, `zone-confusion.md`, `nombres-polynomes.md`, `grille-decalee.md`, `menisque-projection.md`, `sphere-faisceaux.md`, `vingt-quatre-miroir.md`, `carre-neuf-points.md`, `lentilles-boules-grain.md`, `tiers-dimension.md`, `tranche-aiguilles.md` ;
  - scripts (dans `scripts/`) : `chevre.py`, `calculs.py`, `pi_dimensions.py`, `trois_solides.py`, `zone_confusion.py`, `polynomes.py`, `grille_decalee.py`, `menisque_projection.py`, `sphere_faisceaux.py`, `carre_neuf_points.py`, `lentilles_boules_grain.py`, `tiers_dimension.py`, `tranche_aiguilles.py`, `revision_001.py` ;
  - résultats (dans `resultats/`) : `resultats.md`, `pi_dimensions.md`, `trois_solides.md`, `zone_confusion.md`, `polynomes.md`, `grille_decalee.md`, `menisque_projection.md`, `sphere_faisceaux.md`, `vingt_quatre_miroir.md`, `carre_neuf_points.md`, `lentilles_boules_grain.md`, `tiers_dimension.md`, `tranche_aiguilles.md` ;
  - figures (dans `figures/`) : `fig3_dimensions.png`, `fig6_courbes50_dimensions.png`, `f2_dimension_reelle.png`, `p2_menisque_projection.png`, `u1_chevres_faisceaux.png`, `w1_carre_neuf_points.png`, `x1_lentilles_boules_grain.png`, `y1_tiers_dimension.png`, `z1_ouverts.png` ;
  - fiches (dans `recueil/observations/`) : 010, 014 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md`.
- **Questions** :
  1. Écris la chaîne de la corde, de l'équation unique (VII § 1, XX § 1) à la série (XXIV § 2, XXV § 1) : pour chaque maillon, le script, la section de résultats, la figure et le statut (démontré, calculé, mesuré).
  2. Le tiers de dimension et K = n + 2 + (N − n) (scripts/revision_001.py, § 1) : où le corpus l'avait-il déjà (XXIV § 3, XXVII § 6) ? Relie-le au simplexe de VI § 3 et au plan à 1/(n + 1) de XXIII § 2.
  3. Pour le test T3 : rassemble les coefficients exacts de resultats/tiers_dimension.md, § 2, et l'origine de chaque terme (le simplexe, la courbure de l'équateur, l'asymétrie de la coquille, XXIV § 1). D'où vient le premier terme impair, −98/15 ?
  4. La chèvre plane et la chèvre infinie (XX § 1, XXV § 1.2, XXVII § 6) : écris la chaîne exacte qui les relie (Borel–Padé, la bosse du ménisque, le tiers de dimension).
  5. Fiches 010 et 014 : à quelles parties se rattachent-elles déjà (la corde de Ptolémée de 70,81°, √2 et √3 dans la corde) ?
  6. Propose au moins trois fiches nouvelles tirées des parties I à XXV : cherche dans les textes « au passage », « curieusement », « fait amusant », « coïncidence », et donne pour chacune le type, le statut proposé, le script et la section.
  7. Littérature : le développement 2n/(n + 1) + 2/(3n²) − 98/(15n³) + … est-il publié ? (à vérifier : Fraser 1984, Meyerson 1984, Jameson et Jameson 2017). Note les chaînes corrigées de la littérature de la chèvre : Fraser puis Meyerson, et l'erratum d'Ullisch (README, § 9).

#### 5.2.2 `moities` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/moities-et-crans.md`.
- **Fichiers à lire** :
  - documents : `README.md`, `archimede.md`, `trois-solides.md`, `aiguille-kakeya.md`, `foyer-fibonacci.md`, `aiguille-grille.md`, `recursion-argent.md`, `sphere-faisceaux.md`, `vingt-quatre-miroir.md`, `carre-neuf-points.md`, `tiers-dimension.md`, `carte-connexions.md`, `venn-ppm.md`, `centre-venn.md` ;
  - scripts (dans `scripts/`) : `calculs.py`, `archimede.py`, `trois_solides.py`, `aiguille.py`, `foyer_fibonacci.py`, `aiguille_grille.py`, `recursion_argent.py`, `sphere_faisceaux.py`, `vingt_quatre_miroir.py`, `carre_neuf_points.py`, `tiers_dimension.py`, `carte_connexions.py`, `venn_ppm.py`, `centre_venn.py` ;
  - résultats (dans `resultats/`) : `resultats.md`, `archimede.md`, `trois_solides.md`, `aiguille.md`, `foyer_fibonacci.md`, `aiguille_grille.md`, `recursion_argent.md`, `sphere_faisceaux.md`, `vingt_quatre_miroir.md`, `carre_neuf_points.md`, `tiers_dimension.md`, `carte_connexions.md`, `venn_ppm.md`, `centre_venn.md` ;
  - figures (dans `figures/`) : `b8_glissement_50.png`, `d1_trois_solides.png`, `e1_aiguille_kakeya.png`, `h1_foyer_menisques.png`, `n1_aiguille_grille.png`, `q1_recursion_argent.png`, `u2_cartes_losange.png`, `v1_vingt_quatre.png`, `ab2_cercles_arctiques.png`, `ad2_deux_ombres.png`, `ae1_centre_moitie.png`, `ae2_diaphragmes_diffraction.png` ;
  - fiches (dans `recueil/observations/`) : 005, 010 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md`.
- **Questions** :
  1. Fais l'inventaire de toutes les moitiés du corpus (au moins douze) : partie, section, script, résultat, exacte ou approchée.
  2. Classe chacune par procédé : involution sans point fixe (complément, antipode, x ↦ −x), dilatation d'un cran (l'aire en r²), équation (Ullisch, cordes de partage), inclusion–exclusion, autre. Dis lesquelles se recollent, et où (XXX § 3 : le cercle R/√2 ; XX § 1 et XXII § 1 : la corde √2).
  3. La moitié par équation devient-elle la moitié par involution quand la dimension tend vers l'infini ? Écris la chaîne exacte, avec les nombres de resultats/sphere_faisceaux.md et de resultats/carre_neuf_points.md.
  4. Fiche 005 : existe-t-il une involution qui forcerait la moitié des croisements ? Sinon, pourquoi une probabilité de l'ordre de 1/(dispersion) (XXX § 7.3) est-elle la bonne ? Que faudrait-il pour que la moitié devienne exacte ?
  5. Les crans : 6,644 crans par décade (XXI § 3, XXVII § 3), 12,91 crans de f/1 à f/88 (XXX § 4.1), une courbe = un cran (XXIX § 3.3), la FTM50 (VIII § 3, XXX § 4.5) : est-ce un seul procédé ? Lequel ?
  6. Fiche 010 : les 39,34 % (arccos(1 − k²/2)/π) et la corde de Ptolémée de 70,81° (partie X) sont-ils la même moitié, vue depuis un anneau ?
  7. Pour le test T5 (fait par l'agent aiguilles), écris ce que chaque issue changerait à l'arbre P2 du plan. Puis propose au moins trois fiches nouvelles.

#### 5.2.3 `bases` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/bases-congruences-premiers.md`.
- **Fichiers à lire** :
  - documents : `pi-dimensions.md`, `nombres-polynomes.md`, `moire-fibonacci.md`, `angle-or-aiguilles.md`, `lentille-144.md`, `aiguille-grille.md`, `bases-objets.md`, `vingt-quatre-miroir.md`, `tranche-aiguilles.md`, `kakeya-miroir.md`, `octaedre-perron-venn.md` ;
  - scripts (dans `scripts/`) : `pi_dimensions.py`, `polynomes.py`, `moire_fibonacci.py`, `angle_or_aiguilles.py`, `lentille_144.py`, `aiguille_grille.py`, `bases_objets.py`, `vingt_quatre_miroir.py`, `tranche_aiguilles.py`, `kakeya_miroir.py`, `octaedre_perron_venn.py`, `recueil_verifications.py`, `revision_001.py` ;
  - résultats (dans `resultats/`) : `pi_dimensions.md`, `polynomes.md`, `moire_fibonacci.md`, `angle_or_aiguilles.md`, `lentille_144.md`, `aiguille_grille.md`, `bases_objets.md`, `vingt_quatre_miroir.md`, `tranche_aiguilles.md`, `kakeya_miroir.md`, `octaedre_perron_venn.md`, `recueil_verifications.md` ;
  - figures (dans `figures/`) : `g2_virgule_binaire.png`, `k1_angle_or_aiguilles.png`, `l1_lentille_144.png`, `t1_bases_modulaires.png`, `v1_vingt_quatre.png`, `z2_tranche_aiguilles.png`, `aa2_virgule_miroir.png`, `ac3_venn17.png` ;
  - fiches (dans `recueil/observations/`) : 001, 005, 013, 014, 015 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md`.
- **Questions** :
  1. Dresse les chaînes de production des parties VII, IX, XI, XII, XIX, XXI, XXV, XXVI et XXVIII (leurs sections sur les nombres), et de scripts/recueil_verifications.py.
  2. Le quart de tour i modulo b : rassemble toutes les occurrences (3 modulo 10, 7 modulo 50, 4 modulo 17, i modulo 53, √2 = ±i dans F₉) et le théorème de XIX § 2. Quelles bases du corpus ont un i, lesquelles non, et qu'est-ce que cela change à leur horloge (reflets contre quarts de tour) ?
  3. Congruence K3 : vérifie par un calcul rapide la famille b = q² + 1 (q premier, p = q² − q + 1 : q² ≡ −1 et q·p ≡ 1 modulo b, p − 1 = φ(b − 1), p divise q³ + 1), et écris l'argument qui explique les cas (5, 3) et (10, 7) du test 4.1 de scripts/revision_001.py.
  4. Test T6 : prépare le test de la tour 2-adique des périodes (Hasse 1966), relie-le à resultats/recueil_verifications.md, § 5, et au miroir de 1/17 (XXVIII § 3.6).
  5. Test T7 : prépare le test des trois 4/3 (les puissances sous b, V₃/V₂, 1/x₀ = n + 4/3).
  6. Les réduites et les trois distances (XI § 2, XIV § 1 et 3, XV § 5, XIX § 4, XX § 6, XXVI § 2.5) : est-ce un seul théorème ? Écris le diésis et le comma comme des écarts des trois distances.
  7. Fiches 001, 005, 013, 014 et 015 : leurs liens, et ce que le test 4.2 de l'agent de session change pour la fiche 015 (la dérive en 1/ln N, le rapport 2 de Hardy et Littlewood).
  8. Trous : le biais de Tchebychev (Rubinstein et Sarnak 1994), le biais des premiers consécutifs (Lemke Oliver et Soundararajan 2016), les densités de Hasse. Que manque-t-il dans les tables publiées des premiers par chiffre des unités et par dizaine (à vérifier) ? Propose au moins trois fiches nouvelles.

#### 5.2.4 `grain` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/grain-pixels-centres.md`.
- **Fichiers à lire** :
  - documents : `carre-ptolemee.md`, `aiguille-grille.md`, `grille-decalee.md`, `pixels-longitudes.md`, `lentilles-boules-grain.md`, `venn-ppm.md`, `centre-venn.md` ;
  - scripts (dans `scripts/`) : `carre_ptolemee.py`, `aiguille_grille.py`, `grille_decalee.py`, `pixels_longitudes.py`, `lentilles_boules_grain.py`, `venn_ppm.py`, `centre_venn.py` ;
  - résultats (dans `resultats/`) : `carre_ptolemee.md`, `aiguille_grille.md`, `grille_decalee.md`, `pixels_longitudes.md`, `lentilles_boules_grain.md`, `venn_ppm.md`, `centre_venn.md` ;
  - figures (dans `figures/`) : `j1_carre_ptolemee.png`, `n2_perron_grille.png`, `o1_grille_decalee.png`, `r1_pixels_contacts.png`, `r2_longitudes_lumiere.png`, `x1_lentilles_boules_grain.png`, `ad1_venn_ppm.png`, `ae1_centre_moitie.png`, `ae3_grains_hasard.png` ;
  - fiches (dans `recueil/observations/`) : 001, 006, 007, 008, 011 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md` ;
  - données externes (lecture seule) : `/home/user/dzoba/venn17/images/venn17-pressure-dark-2000.png`, `/home/user/dzoba/venn17/plotter/plotter_svg.py`, `/home/user/dzoba/venn17/README.md`.
- **Questions** :
  1. Dresse les chaînes de X § 2–3, XIV § 6, XV § 3, XVIII, XXIII § 3–4, XXIX § 1–4 et XXX § 1, 2.4 et 6.
  2. Le budget de décision : pour chaque mesure du dossier, la précision accessible (px, ppm, chiffres) et ce qu'elle peut trancher. Un tableau unique (par exemple : le centre à 0,003 px ; le cercle de demi-aire à ±1 830 ppm ; un croisement de 22,6 px), avec la source de chaque ligne.
  3. Les taux de change entre grain et pas (ε⁻², ε⁻¹, ε^(−1/2), le logarithme ; un bit par courbe, un demi-bit en longueur) : un tableau unique, avec la source de chaque ligne.
  4. Test T4 : lis les fonctions palette et write_svg de plotter_svg.py (ne lance rien), décris le classement des pixels par teinte et la façon d'estimer son erreur. L'ordre d'écriture des courbes dans le SVG est-il aussi celui de l'image PNG ? Cherche comment l'image a été rendue (README du dépôt) ; sinon, écris « à vérifier ».
  5. Congruence K10 : vérifie sur le tableau de XXX § 6.4 que W_centre/W_reste = √(n/4π) et que le seuil est n = 4π. Est-ce la constante isopérimétrique, ou une rencontre de constantes ? Propose la variation qui trancherait.
  6. Le biais propagé (fiche 007) : où d'autres chaînes du corpus partent-elles d'un point biaisé ou d'une fenêtre trop étroite (troncature d'une série, grille grossière, barycentre) ?
  7. Propose au moins trois fiches nouvelles, dont une pour D3 tirée des parties X, XV ou XVIII.

#### 5.2.5 `lumiere` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/lumiere-et-physique.md`.
- **Fichiers à lire** :
  - documents : `README.md`, `archimede.md`, `foyer-fibonacci.md`, `moire-fibonacci.md`, `carre-ptolemee.md`, `angle-or-aiguilles.md`, `lentille-144.md`, `perron-dephasage.md`, `recursion-argent.md`, `pixels-longitudes.md`, `bases-objets.md`, `sphere-faisceaux.md`, `octaedre-perron-venn.md`, `centre-venn.md` ;
  - scripts (dans `scripts/`) : `chevre.py`, `figures.py`, `foyer_fibonacci.py`, `moire_fibonacci.py`, `carre_ptolemee.py`, `angle_or_aiguilles.py`, `lentille_144.py`, `perron_dephasage.py`, `recursion_argent.py`, `pixels_longitudes.py`, `bases_objets.py`, `sphere_faisceaux.py`, `octaedre_perron_venn.py`, `centre_venn.py` ;
  - résultats (dans `resultats/`) : `resultats.md`, `archimede.md`, `foyer_fibonacci.md`, `moire_fibonacci.md`, `carre_ptolemee.md`, `angle_or_aiguilles.md`, `lentille_144.md`, `perron_dephasage.md`, `recursion_argent.md`, `pixels_longitudes.md`, `bases_objets.md`, `sphere_faisceaux.md`, `octaedre_perron_venn.md`, `centre_venn.md` ;
  - figures (dans `figures/`) : `fig7_optique.png`, `fig8_anneaux_newton.png`, `fig9_eclipses.png`, `b4_menisque.png`, `h1_foyer_menisques.png`, `h2_fibonacci.png`, `i1_moire_fibonacci.png`, `i2_optique_racines.png`, `k1_angle_or_aiguilles.png`, `l1_lentille_144.png`, `m1_perron_dephasage.png`, `q2_newton_polyedres.png`, `r2_longitudes_lumiere.png`, `t2_trait_cone_thales.png`, `u2_cartes_losange.png`, `ac3_venn17.png`, `ae2_diaphragmes_diffraction.png` ;
  - fiches (dans `recueil/observations/`) : 002, 006, 009 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md` ;
  - données externes (lecture seule) : `/home/user/dzoba/venn17/plotter/plotter_svg.py`.
- **Questions** :
  1. Dresse les chaînes optiques : README § 6, II § 3 et 9, VIII, IX § 1–3, X § 1 et 6, XI § 3–4, XII § 1 et 4, XIII § 1–4, XVII § 5, XVIII § 6–7, XIX § 6, XX § 4 et 6, XXVIII § 3.3, XXX § 1.2, 4.5, 5, 6.1 et 6.3.
  2. Pour chaque analogie physique du corpus (anneaux de Newton, éclipses, FTM, Fresnel, œil de poisson de Maxwell, Deschamps, Self, Wielen, HD, drizzle, Gustafsson, Hopkins, Friedel, Planck, l'IA) : ce qui est partagé exactement, ce qui est transporté, ce qui reste ouvert (CLAUDE.md, § 1). Un tableau.
  3. D8 n'a aucune chaîne propre (plan, § 1.0) : quelles analogies physiques mériteraient une fiche ? Propose-en au moins trois, avec leur test.
  4. Congruence K2 : vérifie que les aigrettes, l'ombre Σωⁱ et les éventails de Perron suivent la même parité pour N = 3 à 20 (les aigrettes sont déjà vérifiées pour 5, 6, 7, 8, 16, 17 et 18 lames, XXVIII § 3.3). Un calcul rapide suffit.
  5. Test T4 : à partir de resultats/centre_venn.md, § 1, montre si un modèle à une seule cause (la palette) peut reproduire les six écarts et leurs directions. Écris le modèle à deux causes (palette et ordre de dessin) et ce qu'il prédit pour la luminance.
  6. Fiches 002, 006 et 009 : leur place dans les arbres P3, P8 et P1 du plan.
  7. Trous dans les données publiées : le biais de couleur des parallaxes de Gaia (Lindegren et al. 2021, A&A 649, A4) et le déplacement induit par la couleur (Wielen 1996 ; Pourbaix et al. 2004). Que rangent dans le bruit les catalogues qui supposent une source unique ?

#### 5.2.6 `aiguilles` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/aiguilles-kakeya-perron.md`.
- **Fichiers à lire** :
  - documents : `aiguille-kakeya.md`, `carre-ptolemee.md`, `perron-dephasage.md`, `aiguille-grille.md`, `recursion-argent.md`, `bases-objets.md`, `tranche-aiguilles.md`, `kakeya-miroir.md`, `carte-connexions.md`, `octaedre-perron-venn.md` ;
  - scripts (dans `scripts/`) : `aiguille.py`, `carre_ptolemee.py`, `perron_dephasage.py`, `aiguille_grille.py`, `recursion_argent.py`, `bases_objets.py`, `tranche_aiguilles.py`, `kakeya_miroir.py`, `carte_connexions.py`, `octaedre_perron_venn.py` ;
  - résultats (dans `resultats/`) : `aiguille.md`, `carre_ptolemee.md`, `perron_dephasage.md`, `aiguille_grille.md`, `recursion_argent.md`, `bases_objets.md`, `tranche_aiguilles.md`, `kakeya_miroir.md`, `carte_connexions.md`, `octaedre_perron_venn.md` ;
  - figures (dans `figures/`) : `e1_aiguille_kakeya.png`, `j1_carre_ptolemee.png`, `m1_perron_dephasage.png`, `n1_aiguille_grille.png`, `n2_perron_grille.png`, `q1_recursion_argent.png`, `z2_tranche_aiguilles.png`, `aa1_kakeya.png`, `ab3_liens_predits.png`, `ac2_perron.png` ;
  - fiches (dans `recueil/observations/`) : 003, 011 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md`.
- **Questions** :
  1. Dresse les chaînes de V, X § 4, XIII § 1, 3 et 6, XIV, XVII § 4, XIX § 2 et 6, XXV § 3, XXVI § 1 et 3.6, XXVII § 7, XXVIII § 2 et 3.3–3.5.
  2. Perron : de 2/(k + 2) vérifié (V § 3) à démontré (XXVIII § 2). La fenêtre de Kakeya à 10⁻⁵⁰ et la constante entre π/2 et π·ln 2 : que manque-t-il pour la constante ?
  3. Les aiguilles de la grille et les réduites (Fibonacci, Pell, Farey, Pick, Eisenstein) : écris la demi-case comme le procédé commun, avec ses sources.
  4. Congruence K7 : le grain plafonne Perron (XIV § 6, produit par log₂ n vers 2,8) et le centre du Venn (fiche 011, XXX § 6.4). La différence est-elle exactement un cran ?
  5. Test T5 : prépare l'extension de minimum_kakeya (scripts/aiguille_grille.py) aux corps F_q (q = 2, 3, 4, 5, 7, 8, 9), avec les symétries et le compte des points couverts 1, 2, 3 fois. Dis ce que Blokhuis et Mazzocca (2008) établissent exactement, et ce qui est connu pour q pair (à vérifier).
  6. D5 n'a aucune fiche principale : propose au moins trois fiches (faits amusants, analogies) tirées des parties V, XIII, XIV, XXVI ou XXVIII, avec leur test.
  7. Fiches 003 et 011 : leur place dans les arbres P1, P3 et P5 du plan.
  8. Trous : Keich 1999 (l'ordre, pas la constante), Wang et Zahl 2025 (la constante en 3D n'est pas calculée), Dvir 2009 ; dis ce que chacun laisse ouvert.

#### 5.2.7 `ombres` (phase 1)

- **Dossier ou rôle** : `recueil/dossiers/ombres-cube-venn.md`.
- **Fichiers à lire** :
  - documents : `archimede.md`, `grille-decalee.md`, `sphere-faisceaux.md`, `vingt-quatre-miroir.md`, `carre-neuf-points.md`, `kakeya-miroir.md`, `carte-connexions.md`, `octaedre-perron-venn.md`, `venn-ppm.md`, `centre-venn.md` ;
  - scripts (dans `scripts/`) : `archimede.py`, `calculs_archimede.py`, `grille_decalee.py`, `sphere_faisceaux.py`, `vingt_quatre_miroir.py`, `carre_neuf_points.py`, `kakeya_miroir.py`, `carte_connexions.py`, `octaedre_perron_venn.py`, `venn_ppm.py`, `centre_venn.py`, `revision_001.py` ;
  - résultats (dans `resultats/`) : `archimede.md`, `grille_decalee.md`, `sphere_faisceaux.md`, `vingt_quatre_miroir.md`, `carre_neuf_points.md`, `kakeya_miroir.md`, `carte_connexions.md`, `octaedre_perron_venn.md`, `venn_ppm.md`, `centre_venn.md` ;
  - figures (dans `figures/`) : `b1_six_projections.png`, `b3_cube_tournant.png`, `o1_grille_decalee.png`, `u1_chevres_faisceaux.png`, `v2_racine_sept.png`, `w1_carre_neuf_points.png`, `aa3_cube_hexagone.png`, `ab2_cercles_arctiques.png`, `ac1_octaedre.png`, `ac3_venn17.png`, `ad1_venn_ppm.png`, `ad2_deux_ombres.png`, `ae1_centre_moitie.png` ;
  - fiches (dans `recueil/observations/`) : 003, 004, 005, 006, 008, 009, 010, 015 ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md` ;
  - données externes (lecture seule) : `/home/user/dzoba/venn17/README.md`, `/home/user/dzoba/venn17/verify/RESULTS.md`, `/home/user/dzoba/venn17/verify/RESULTS-19.md`, `/home/user/dzoba/venn17/verify/RESULTS-23.md`.
- **Questions** :
  1. Dresse les chaînes de II § 1–2, XV § 1, XX § 3 et 5, XXI § 1 et 4, XXII § 3–4, XXVI § 3, XXVII § 2, 4 et 8, XXVIII § 1 et 3, XXIX § 1–2 et 5, XXX § 3.
  2. Le cube {0, 1}ⁿ et ses ombres : fais le tableau des regards (une direction quelconque : Perron, binaire ; la grande diagonale : Venn, binomiale ; l'ombre symétrique Σωⁱ : polygone à 2n côtés ; les axes d'ordre 3 et 4 : cercles arctiques), avec ce qui est démontré et où.
  3. Le nerf : les faisceaux de chèvres (XX § 3, XXII § 3) et le nerf des dossiers (test T1) sont le même procédé de Čech. Dis ce que le nerf des dossiers peut dire et ce qu'il ne peut pas dire (le théorème du nerf demande des intersections contractiles : qu'est-ce que cela voudrait dire pour des dossiers ?).
  4. Fiche 015 : la face choisie par le reste modulo 3 est-elle une ombre du cube {0, 1}⁴, ou une restriction à une face ? Écris la correspondance exacte.
  5. Gelé et liquide (XXIX § 5.3) contre les cercles arctiques (XXVII § 2) : pourquoi la couche gelée des Venn reste-t-elle mince ? Que faudrait-il pour une forme limite ?
  6. Fiches 003, 004, 005, 006, 008, 009 et 010 : leur place dans l'arbre P1 du plan ; lesquelles sont des rameaux de hasard ?
  7. Trous : un Venn simple, symétrique et symétrique par le complément à 17 ou 19 courbes ; les certificats à 23 courbes (verify/RESULTS-23.md du dépôt de Dzoba) ; ce que le dépôt publie et ce qu'il ne publie pas (la moitié des croisements, la symétrie par le complément, l'ordre de dessin). Propose au moins trois fiches nouvelles.

#### 5.2.8 `methode` (phase 2)

- **Dossier ou rôle** : recueil/dossiers/hasard-et-methode.md (vérification croisée des tests et des chaînes ; les huit sections des dossiers de la phase 1, décrites dans gabarit.phase_1, plus le tableau des quinze fiches de la question 2).
- Sa sortie est le dossier recueil/dossiers/hasard-et-methode.md, avec les huit sections des dossiers de la phase 1 (plan, § 5.1), plus le tableau des quinze fiches (question 2).
- **Fichiers à lire** :
  - documents : `pi-dimensions.md`, `zone-confusion.md`, `perron-dephasage.md`, `pixels-longitudes.md`, `tiers-dimension.md`, `carte-connexions.md`, `venn-ppm.md`, `centre-venn.md` ;
  - scripts (dans `scripts/`) : `centre_venn.py`, `venn_ppm.py`, `carte_connexions.py`, `recueil_index.py`, `recueil_verifications.py`, `revision_001.py` ;
  - résultats (dans `resultats/`) : `pi_dimensions.md`, `zone_confusion.md`, `perron_dephasage.md`, `pixels_longitudes.md`, `tiers_dimension.md`, `carte_connexions.md`, `venn_ppm.md`, `centre_venn.md`, `recueil_verifications.md` ;
  - figures (dans `figures/`) : `f2_dimension_reelle.png`, `ab1_carte.png`, `ad2_deux_ombres.png`, `ae3_grains_hasard.png` ;
  - fiches (dans `recueil/observations/`) : 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015 ;
  - dossiers de la phase 1 (dans `recueil/dossiers/`) : `corde-et-dimensions.md`, `moities-et-crans.md`, `bases-congruences-premiers.md`, `grain-pixels-centres.md`, `lumiere-et-physique.md`, `aiguilles-kakeya-perron.md`, `ombres-cube-venn.md` ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md`, `recueil/index.csv`.
- **Questions** :
  1. La lignée des tests du corpus : III § 2, puis VI § 3 bis et 3 ter, XIII § 5, XXIX § 5.5 et XXX § 7. Qu'est-ce que chaque étape a corrigé ?
  2. Pour chaque fiche 001 à 015 : le test appliqué est-il le bon selon la table du § 10 de CLAUDE.md ? Le verdict tient-il dans le budget de la donnée ? Un tableau de quinze lignes.
  3. Les chaînes de production : relève dans les sept dossiers les erreurs et les corrections (les 2,36 px ; la « quasi-coïncidence » de V corrigée en VI ; les trois phrases de XXII corrigées en XXIII ; Fraser puis Meyerson ; l'erratum d'Ullisch) et classe-les : point de départ biaisé, fenêtre trop étroite, pesée, troncature, cadre.
  4. Le cadre fabrique des liens (scripts/revision_001.py, § 2 : p_a + p_b < Σp²) : relie-le aux doubles zéros (Legendre et Legendre), aux données de composition (Pearson 1897, Aitchison 1986), à l'effet « regarder ailleurs » (Gross et Vitells 2010) et au jardin des chemins qui bifurquent (Gelman et Loken 2014).
  5. Test T8 : prépare le test du nerf contre la carte, et dis comment mesurer la dépendance entre les deux méthodes.
  6. Corrélation et causalité : pour les fiches de type Causalité (006, 007, 012), le lien est-il établi par une intervention (refaire l'essai en ne changeant qu'une chose) ou seulement par une corrélation ? (Reichenbach 1956 ; Pearl 2009.)
  7. Les tests de la révision (T1 à T8, plan § 4) : chacun respecte-t-il la table du § 10 ? Lequel risque de déclarer « hasard » une structure, ou l'inverse ?

#### 5.2.9 `croisement` (phase 2)

- **Dossier ou rôle** : vérification croisée : recueil/revisions/verification-croisee-001.md, en sept sections : le recouvrement v2 (un bloc JSON au format du § 1.9 du plan), les congruences, les triangles vides, les arbres corrigés, les doublons et contradictions, les trous dans les données publiées, les nouvelles fiches classées par dimension.
- Sa sortie est recueil/revisions/verification-croisee-001.md, avec sept sections : le recouvrement v2 (un bloc JSON au format du § 1.9), les congruences, les triangles vides, les arbres corrigés, les doublons et contradictions, les trous dans les données publiées, les nouvelles fiches classées par dimension.
- **Fichiers à lire** :
  - documents : `README.md`, `carte-connexions.md` ;
  - scripts (dans `scripts/`) : `revision_001.py`, `carte_connexions.py`, `sphere_faisceaux.py` ;
  - résultats (dans `resultats/`) : `carte_connexions.md`, `recueil_verifications.md` ;
  - fiches (dans `recueil/observations/`) : 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015 ;
  - dossiers de la phase 1 (dans `recueil/dossiers/`) : `corde-et-dimensions.md`, `moities-et-crans.md`, `bases-congruences-premiers.md`, `grain-pixels-centres.md`, `lumiere-et-physique.md`, `aiguilles-kakeya-perron.md`, `ombres-cube-venn.md` ;
  - recueil et plan : `CLAUDE.md`, `recueil/README.md`, `recueil/index.md`, `recueil/revisions/plan-001.md`, `recueil/index.csv`.
- **Questions** :
  1. Le recouvrement : pour chaque dossier, les parties et les fiches du bloc JSON (plan, § 1.9) sont-elles celles que l'agent a réellement traitées ? Rassemble les corrections des sections 8 des dossiers et écris le recouvrement v2, au même format JSON.
  2. Les congruences K1 à K10 (plan, § 3) : pour chacune, recollement ou obstruction, avec la source ; ajoute celles que les dossiers ont trouvées.
  3. Les triangles vides : à partir du recouvrement v2, liste les triples de dossiers deux à deux sécants au niveau des fiches. Pour chacun, dis si une partie du corpus le remplit déjà (trou du recueil) ou non (trou du corpus), et propose l'observation qui le remplirait.
  4. La structure en Perron (plan, § 2) : vérifie les huit arbres contre les dossiers (branches, triangle du bas, disque) et corrige-les.
  5. Les doublons et les contradictions entre dossiers : un même nombre cité différemment, un même lien classé différemment, deux verdicts opposés.
  6. Les trous dans les données publiées : rassemble les pistes des dossiers, vérifie que chaque référence existe (sinon « à vérifier »), et classe-les par dossier.
  7. Les nouvelles fiches proposées : dédoublonne, et classe-les par dimension principale, pour que le prochain partage des aires soit plus équitable (au moins une pour D5 et une pour D8).

### 5.3 Après le workflow (l'agent de session)

1. Lire les huit dossiers et `verification-croisee-001.md`.
2. Calculer T1 à T8 dans `scripts/revision_001.py`, avec le recouvrement v1 (§ 1.9) puis v2 ; écrire `resultats/revision_001.md` et `figures/rev001_*.png`.
3. Écrire `recueil/revisions/revision-001.md`, avec les huit arbres corrigés, le Venn après la révision, l'étude des congruences et les trous. Sa première ligne `<!-- arcs: N -->` demande un choix : aucun fichier `recueil/arcs/arc-NNN.md` n'existe, mais les fiches 013 à 015 parlent d'un « arc 001 » (§ 6.1).
4. Écrire les nouvelles fiches retenues (non révisées), marquer « révisé : 001 » sur les fiches 001 à 015, relancer `python3 scripts/recueil_index.py`, puis commiter et pousser.

## 6. Les trous dans les données publiées

**Comment lire.** Chaque piste part d'une observation du corpus, dit ce qui manque dans les données publiées, où chercher, et avec quelles références. Je marque « à vérifier » toute référence dont je ne suis pas sûr (auteurs, volume ou pages). Les références déjà citées par les parties sont marquées (corpus).

### 6.1 D'abord, les trous du recueil lui-même

- **Le biais d'origine.** Douze fiches sur quinze viennent des parties XXIX et XXX ; les parties I à XXVIII n'ont aucune fiche à elles. Chaque dossier doit en proposer (section 6 de chaque dossier).
- **Deux dimensions vides.** D5 (Kakeya, Perron) et D8 (physique) n'ont aucune fiche principale (`recueil/index.md` : K = 6). Au niveau des parties, D8 n'a aucune chaîne (§ 1.0). Le partage des aires ne peut pas être équitable tant qu'elles restent vides.
- **Les triangles vides du nerf** au niveau des fiches (T1) : ce sont, par construction, des fiches qui manquent. À calculer.
- **La chaîne des arcs.** Aucun fichier `recueil/arcs/arc-NNN.md` n'existe, mais les fiches 013 à 015 indiquent « arc 001 » et les fiches 001 à 012 « avant le recueil ». La donnée brute des arcs, prévue au § 10 de CLAUDE.md, manque pour cette première révision : c'est un trou de la chaîne de production du recueil, à fermer par l'agent de fin d'arc.

### 6.2 Les pistes, une par une

**a. Les images publiées des Venn de Dzoba : l'ordre de dessin (fiche 006, K6, T4).**
- *L'observation.* Le centre de la lumière dépend de la pesée, et un modèle à une seule cause (la couleur) ne reproduit pas les écarts (§ 3.2, K6).
- *Ce qui manque.* L'ordre dans lequel les courbes sont dessinées est une variable de la chaîne de production : `write_svg` écrit les 17 courbes de 0 à 16, et la dernière couvre les autres aux croisements. Ni la palette ni cet ordre ne sont donnés comme des paramètres de mesure (à vérifier dans `/home/user/dzoba/venn17/README.md`). Toute mesure photométrique faite sur l'image publiée en hérite.
- *Où chercher.* Le code de rendu du dépôt ; refaire le rendu avec un ordre tourné (i + k modulo 17) prédirait une rotation du dipôle de 2πk/17, si l'ordre est la cause.
- *Références.* C. Dzoba, arXiv:2609.26546 (2026), et le dépôt dzoba/venn17 (corpus, parties XXIX et XXX).

**b. Les certificats de Dzoba : la moitié et le complément (fiches 004, 005).**
- *Ce qui manque.* La moitié des croisements et la symétrie par le complément ne font pas partie des critères de recherche publiés ; aucun Venn simple et symétrique à 17 ou 19 courbes n'est connu qui soit aussi symétrique par le complément (ouvert de XXX § 9).
- *Où chercher.* Les journaux de recherche (`/home/user/dzoba/venn17/search/README.md`, la méthode `ramp12h`) ; les certificats à 23 courbes : la copie locale n'a que `/home/user/dzoba/venn17/verify/RESULTS-23.md`, car ils font 889 Mo chacun et sont publiés comme fichiers de version et sur Zenodo (`/home/user/dzoba/venn17/README.md`) ; il faut les télécharger pour répliquer les fiches 004 et 005 à n = 23. Les Venn monotones à 11 et 13 courbes de Mamakani et Ruskey sont des objets indépendants pour la réplication : ceux du dépôt de Dzoba, eux, sont non monotones (même README).
- *Références.* K. Mamakani, F. Ruskey, Venn simples et symétriques à 11 et 13 courbes, 2012 et 2014 (corpus, partie XXVIII, et README de Dzoba ; titres et volumes à vérifier) ; J. Griggs, C. E. Killian, C. D. Savage (2004) et F. Ruskey, M. Weston, *A Survey of Venn Diagrams* (corpus, partie XXIX) ; la revue de Brenner, Gregor, Mütze et Verciani (2026), citée par le README de Dzoba comme donnant le problème ouvert au-delà de 13 courbes (à vérifier).

**c. L'astrométrie : le centre dépend de la couleur (fiche 006).**
- *L'observation.* Le barycentre d'une source symétrique pesée inégalement bouge selon la pesée ; c'est le principe du déplacement induit par la couleur des étoiles doubles.
- *Ce qui manque.* Un catalogue qui ajuste une seule source à une étoile double range ce déplacement dans le bruit, ou dans une correction de couleur. Le point zéro des parallaxes de Gaia dépend justement de la magnitude, de la couleur et de la position.
- *Où chercher.* Les solutions astrométriques des étoiles non résolues, et les catalogues d'étoiles multiples de Gaia.
- *Références.* L. Lindegren et al., « Gaia Early Data Release 3: Parallax bias versus magnitude, colour, and position », *A&A* 649, A4 (2021) ; R. Wielen (1996) et D. Pourbaix et al. (2004) (corpus, partie XXX) ; V. Belokurov et al., « Unresolved stellar companions with Gaia DR2 astrometry », *MNRAS* 496 (2020) (à vérifier : pages) ; Gaia Collaboration, F. Arenou et al., « Gaia Data Release 3: Stellar multiplicity », *A&A* 674, A34 (2023) (à vérifier).

**d. Les premiers par chiffre et par dizaine (fiches 013, 015 ; test 4.2).**
- *L'observation.* Le rapport par motif de la fiche 015 dérive lentement (en 1/ln N) et croise π puis 2√2 en passant (test 4.2 de l'agent de session).
- *Ce qui manque.* Une grandeur du second ordre, lue à une seule taille, passe pour une constante. C'est la même famille d'effets que le biais de Tchebychev (les premiers en 3 et 7 devancent souvent ceux en 1 et 9) et que le biais des premiers consécutifs, découvert tard parce qu'on supposait les derniers chiffres indépendants. `resultats/recueil_verifications.md`, § 6, donne 19 665 + 19 621 premiers en 3 et 7 contre 19 617 + 19 593 en 1 et 9 sous 10⁶ : le sens du biais de Tchebychev (à mesurer en faisant varier la borne).
- *Où chercher.* Les tables publiées des premiers par chiffre des unités et des quadruplets de premiers (OEIS A007530, à vérifier) ne donnent pas les 16 motifs de la dizaine : c'est la donnée que le recueil fabrique.
- *Références.* G. H. Hardy, J. E. Littlewood, « Some problems of “Partitio numerorum” III », *Acta Mathematica* 44, 1–70 (1923) ; M. Rubinstein, P. Sarnak, « Chebyshev's bias », *Experimental Mathematics* 3, 173–197 (1994) ; R. J. Lemke Oliver, K. Soundararajan, « Unexpected biases in the distribution of consecutive primes », *PNAS* 113, E4446–E4454 (2016).

**e. Les périodes de 1/p : Midy n'a pas des aires égales (fiche 013, K9, T6).**
- *Ce qui manque.* La lecture « Venn de Midy » suppose deux régions comparables. La densité des premiers à période paire est 2/3 pour une base générique, 17/24 pour la base 2 : le partage n'est pas équitable par nature.
- *Où chercher.* Les densités de la valuation 2-adique de l'ordre multiplicatif, et leurs analogues pour 3, 5, 7 (Midy étendu).
- *Références.* H. Hasse, « Über die Dichte der Primzahlen p, für die eine vorgegebene ganzrationale Zahl a ≠ 0 von gerader bzw. ungerader Ordnung mod. p ist », *Mathematische Annalen* 166, 19–23 (1966) ; P. Moree, « Artin's primitive root conjecture – a survey », *Integers* 12A (2012) (à vérifier).

**f. Kakeya sur une grille finie, en caractéristique 2 (K4, T5).**
- *Ce qui manque.* Le minimum est démontré pour q impair ; pour q pair, je ne sais pas quelle publication le donne (à vérifier). Le corpus n'a calculé que des q premiers.
- *Références.* A. Blokhuis, F. Mazzocca (2008) (corpus, partie XIV) ; Z. Dvir, « On the size of Kakeya sets in finite fields », *J. Amer. Math. Soc.* 22, 1093–1097 (2009).

**g. La constante de Kakeya au grain δ (arbre P5).**
- *Ce qui manque.* Les constructions publiées donnent l'ordre 1/ln(1/δ), pas la constante, encore entre π/2 et π·ln 2 (XXVIII § 2.5) ; en 3D, la constante de Wang et Zahl n'est pas calculée.
- *Références.* U. Keich (1999), A. Córdoba (1977), H. Wang et J. Zahl (2025) (corpus, parties XIV, XXVI, XXVIII).

**h. La chèvre en dimension n : une chaîne déjà corrigée (arbre P3).**
- *L'observation.* La littérature de la chèvre a elle-même des maillons corrigés : l'argument de Fraser (1984) corrigé par Meyerson (1984), et l'erratum d'Ullisch sur le contour 3π/4 (2023) (corpus, README § 9).
- *Ce qui manque.* Je ne sais pas si le développement 2n/(n + 1) + 2/(3n²) − 98/(15n³) + … de la partie XXIV est publié ailleurs (à vérifier). S'il ne l'est pas, c'est une donnée que le corpus apporte.

**i. Les tests de coïncidences (fiches 002, 003, 004, 012).**
- *L'observation.* Les tests à tolérance (Bonferroni, catalogue brouillé, longueur de description) déclarent « hasard » des liens de structure (XXX § 7).
- *Ce qui manque.* Dans les analyses publiées de rapprochements numériques, on corrige pour le nombre d'essais, mais on fait rarement varier le paramètre : la loi de l'écart n'est pas une donnée qu'on publie (à vérifier, par une revue de quelques analyses).
- *Références.* E. Gross, O. Vitells, « Trial factors for the look elsewhere effect in high energy physics », *Eur. Phys. J. C* 70, 525–530 (2010) ; A. Gelman, E. Loken, « The statistical crisis in science », *American Scientist* 102, 460–465 (2014) ; J. P. A. Ioannidis, « Why most published research findings are false », *PLoS Medicine* 2, e124 (2005). Pour les liens fabriqués par le cadre : K. Pearson (1897), F. Chayes (1960), J. Aitchison (1986), P. et L. Legendre, *Numerical Ecology* (déjà cités par l'agent de session dans `scripts/revision_001.py`, § 2).

### 6.3 Le cadre qui conceptualise ces liens

- **Les faisceaux et leurs obstructions.** S. Abramsky, A. Brandenburger, « The sheaf-theoretic structure of non-locality and contextuality », *New Journal of Physics* 13, 113036 (2011) ; S. Abramsky, S. Mansfield, R. Soares Barbosa, « The cohomology of non-locality and contextuality », *EPTCS* 95, 1–14 (2012). Des données locales cohérentes deux à deux qui ne se recollent pas en une donnée globale : c'est exactement l'« obstruction » du § 3.
- **Le nerf et sa persistance.** K. Borsuk, « On the imbedding of systems of compacta in simplicial complexes », *Fundamenta Mathematicae* 35, 217–234 (1948) (le théorème du nerf) ; H. Edelsbrunner, D. Letscher, A. Zomorodian, « Topological persistence and simplification », *Discrete & Computational Geometry* 28, 511–533 (2002) ; R. Ghrist, « Barcodes: the persistent topology of data », *Bull. AMS* 45, 61–75 (2008) ; G. Carlsson, « Topology and data », *Bull. AMS* 46, 255–308 (2009). Les niveaux « fiches » puis « fiches + parties » de T1 sont une filtration à deux pas.
- **Les faisceaux pour fusionner des données.** M. Robinson, « Sheaves are the canonical data structure for sensor integration », *Information Fusion* 36 (2017) (à vérifier : pages).
- **Le nul à marges fixées (T1).** N. J. Gotelli, « Null model analysis of species co-occurrence patterns », *Ecology* 81, 2606–2621 (2000) ; G. Strona et al., méthode « curveball », *Nature Communications* 5, 4114 (2014) (à vérifier).
- **Corrélation et causalité.** H. Reichenbach, *The Direction of Time*, University of California Press (1956) : deux effets corrélés renvoient à une cause commune, c'est le triangle du bas de l'arbre de Perron ; J. Pearl, *Causality*, 2e éd., Cambridge University Press (2009) : l'intervention (refaire l'essai en ne changeant qu'une chose) distingue la cause de la corrélation. C'est ce que fait la fiche 007, et ce que fera T4.

### 6.4 Où chercher les prochaines données, en bref

| piste | donnée à aller chercher | test ou dossier |
|---|---|---|
| a | un rendu du Venn avec l'ordre de dessin tourné | T4, `grain`, `lumiere` |
| b | les certificats à 23 courbes ; les journaux de `ramp12h` | `ombres`, `moities` |
| c | les écarts de couleur des solutions astrométriques à source unique | `lumiere` |
| d | les 16 motifs de dizaines à 10⁹ et plus, avec les termes du second ordre | `bases` |
| e | la tour 2-adique des périodes, base par base | T6, `bases` |
| f | le minimum de Kakeya fini pour q pair | T5, `aiguilles` |
| g | une construction de Kakeya au grain δ avec sa constante | `aiguilles` |
| h | une publication du développement de la corde | `corde` |
| i | des analyses publiées de coïncidences, relues avec la variation du paramètre | `methode` |

## 7. Le bloc JSON des agents

Pour le script du workflow, tel quel. Chaque agent reçoit le gabarit de sa phase (`gabarit.phase_1` ou `gabarit.phase_2`), puis son label, son dossier, sa liste de fichiers et ses questions. La phase 2 attend la fin de la phase 1. Les chemins relatifs partent de `/home/user/Graphite/chevre-optique` ; les chemins absolus sont la copie locale du dépôt de Dzoba. Seuls les sept dossiers de la phase 1, cités dans les listes de la phase 2, n'existent pas encore.

```json
{
  "revision": "001",
  "modele": "sonnet",
  "phases": {"1": "les sept agents de dossier, en parallèle", "2": "les deux agents de vérification croisée, en parallèle, après la phase 1"},
  "gabarit": {
    "phase_1": "Tu es un agent Sonnet du workflow de la révision 001 du recueil, dans le dépôt /home/user/Graphite/chevre-optique (une série de 30 parties en français sur le problème de la chèvre, les cercles, les bases de numération, Kakeya et Perron, et les diagrammes de Venn). Ton label, ton dossier, ta liste de fichiers et tes questions suivent ce texte. 1. Lis d'abord CLAUDE.md (surtout les § 1, 6, 6 bis et 10) et recueil/revisions/plan-001.md (§ 0 à 4 ; ton dossier est décrit au § 1). 2. Lis ensuite les fichiers de ta liste : pour chaque partie, au moins les sections que le plan indique ; pour chaque script, ses en-têtes de section et les fonctions citées, sans lancer aucun script du dépôt ; pour chaque fichier de résultats, les tableaux d'où viennent les nombres que tu cites ; regarde les figures citées. Les fichiers sous /home/user/dzoba/venn17 sont des données externes (licence CC BY 4.0) : lis-les, n'exécute pas leur code. 3. Tu peux faire des calculs rapides (moins d'une minute, avec numpy, scipy, sympy ou mpmath) dans un dossier temporaire à toi, jamais dans le dépôt. 4. N'écris qu'un seul fichier : ta sortie. Ne modifie rien d'autre dans le dépôt. 5. Règles : vérifie chaque chemin avec ls avant de l'écrire ; n'invente aucun nombre (cite le fichier resultats/… et sa section, ou écris « à calculer ») ; écris en français simple, avec des phrases courtes ; une analogie soutenue par le même procédé est un résultat (CLAUDE.md, § 1) : écris ce qui est partagé exactement, ce qui est transporté et ce qui reste ouvert ; distingue démontré, calculé, classique, ma lecture et ouvert ; avant d'écrire « coïncidence » ou « pas établi », cherche dans les parties précédentes si le lien y est déjà (CLAUDE.md, § 6 bis). 6. Ton dossier a huit sections : (1) la question directrice et la projection sur D1–D8 ; (2) les chaînes de production (script → résultats → figures → document), partie par partie et dans l'ordre, avec ce que chaque script produit ; (3) ce que le dossier établit, et ce qui reste ouvert ; (4) les fiches du dossier : verdict, test, et la partie qui portait déjà le lien ; (5) les congruences et les obstructions (celles du plan, § 3, et les tiennes) ; (6) les trous : du recueil (au moins trois fiches nouvelles proposées, avec type, statut, partie, script et section, image), du corpus, et des données publiées (références réelles, sinon « à vérifier ») ; (7) pour le script de la révision : le code minimal du test qui te concerne (plan, § 4), sans résultat inventé ; (8) les corrections au recouvrement : les parties ou fiches à ajouter à ton dossier ou à en retirer dans le bloc JSON du § 1.9 du plan, avec la raison. 7. Termine ton message final par un résumé de dix lignes au plus : les trois liens les plus forts, les trois trous, et les corrections au recouvrement.",
    "phase_2": "Tu es un agent Sonnet de vérification croisée du workflow de la révision 001 du recueil, dans le dépôt /home/user/Graphite/chevre-optique. Les sept dossiers de la phase 1 sont écrits dans recueil/dossiers/ : lis-les tous, ainsi que CLAUDE.md (§ 1, 6, 6 bis et 10) et recueil/revisions/plan-001.md en entier. Ton label, ta sortie, ta liste de fichiers et tes questions suivent ce texte. Règles : ne lance aucun script du dépôt (calculs rapides permis dans un dossier temporaire à toi) ; n'écris qu'un seul fichier, ta sortie ; vérifie chaque chemin avec ls ; n'invente aucun nombre (cite le fichier resultats/… et sa section, ou le dossier qui le donne, ou écris « à calculer ») ; écris en français simple, avec des phrases courtes ; une analogie soutenue par le même procédé est un résultat (CLAUDE.md, § 1). Si un dossier de la phase 1 manque, dis-le en tête de ta sortie et travaille avec les autres. Termine ton message final par un résumé de dix lignes au plus."
  },
  "agents": [
    {
      "label": "corde",
      "dossier": "recueil/dossiers/corde-et-dimensions.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "README.md",
        "pi-dimensions.md",
        "trois-solides.md",
        "zone-confusion.md",
        "nombres-polynomes.md",
        "grille-decalee.md",
        "menisque-projection.md",
        "sphere-faisceaux.md",
        "vingt-quatre-miroir.md",
        "carre-neuf-points.md",
        "lentilles-boules-grain.md",
        "tiers-dimension.md",
        "tranche-aiguilles.md",
        "scripts/chevre.py",
        "scripts/calculs.py",
        "scripts/pi_dimensions.py",
        "scripts/trois_solides.py",
        "scripts/zone_confusion.py",
        "scripts/polynomes.py",
        "scripts/grille_decalee.py",
        "scripts/menisque_projection.py",
        "scripts/sphere_faisceaux.py",
        "scripts/carre_neuf_points.py",
        "scripts/lentilles_boules_grain.py",
        "scripts/tiers_dimension.py",
        "scripts/tranche_aiguilles.py",
        "scripts/revision_001.py",
        "resultats/resultats.md",
        "resultats/pi_dimensions.md",
        "resultats/trois_solides.md",
        "resultats/zone_confusion.md",
        "resultats/polynomes.md",
        "resultats/grille_decalee.md",
        "resultats/menisque_projection.md",
        "resultats/sphere_faisceaux.md",
        "resultats/vingt_quatre_miroir.md",
        "resultats/carre_neuf_points.md",
        "resultats/lentilles_boules_grain.md",
        "resultats/tiers_dimension.md",
        "resultats/tranche_aiguilles.md",
        "figures/fig3_dimensions.png",
        "figures/fig6_courbes50_dimensions.png",
        "figures/f2_dimension_reelle.png",
        "figures/p2_menisque_projection.png",
        "figures/u1_chevres_faisceaux.png",
        "figures/w1_carre_neuf_points.png",
        "figures/x1_lentilles_boules_grain.png",
        "figures/y1_tiers_dimension.png",
        "figures/z1_ouverts.png",
        "recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md",
        "recueil/observations/014-fractions-continues-imaginaires.md"
      ],
      "questions": [
        "Écris la chaîne de la corde, de l'équation unique (VII § 1, XX § 1) à la série (XXIV § 2, XXV § 1) : pour chaque maillon, le script, la section de résultats, la figure et le statut (démontré, calculé, mesuré).",
        "Le tiers de dimension et K = n + 2 + (N − n) (scripts/revision_001.py, § 1) : où le corpus l'avait-il déjà (XXIV § 3, XXVII § 6) ? Relie-le au simplexe de VI § 3 et au plan à 1/(n + 1) de XXIII § 2.",
        "Pour le test T3 : rassemble les coefficients exacts de resultats/tiers_dimension.md, § 2, et l'origine de chaque terme (le simplexe, la courbure de l'équateur, l'asymétrie de la coquille, XXIV § 1). D'où vient le premier terme impair, −98/15 ?",
        "La chèvre plane et la chèvre infinie (XX § 1, XXV § 1.2, XXVII § 6) : écris la chaîne exacte qui les relie (Borel–Padé, la bosse du ménisque, le tiers de dimension).",
        "Fiches 010 et 014 : à quelles parties se rattachent-elles déjà (la corde de Ptolémée de 70,81°, √2 et √3 dans la corde) ?",
        "Propose au moins trois fiches nouvelles tirées des parties I à XXV : cherche dans les textes « au passage », « curieusement », « fait amusant », « coïncidence », et donne pour chacune le type, le statut proposé, le script et la section.",
        "Littérature : le développement 2n/(n + 1) + 2/(3n²) − 98/(15n³) + … est-il publié ? (à vérifier : Fraser 1984, Meyerson 1984, Jameson et Jameson 2017). Note les chaînes corrigées de la littérature de la chèvre : Fraser puis Meyerson, et l'erratum d'Ullisch (README, § 9)."
      ]
    },
    {
      "label": "moities",
      "dossier": "recueil/dossiers/moities-et-crans.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "README.md",
        "archimede.md",
        "trois-solides.md",
        "aiguille-kakeya.md",
        "foyer-fibonacci.md",
        "aiguille-grille.md",
        "recursion-argent.md",
        "sphere-faisceaux.md",
        "vingt-quatre-miroir.md",
        "carre-neuf-points.md",
        "tiers-dimension.md",
        "carte-connexions.md",
        "venn-ppm.md",
        "centre-venn.md",
        "scripts/calculs.py",
        "scripts/archimede.py",
        "scripts/trois_solides.py",
        "scripts/aiguille.py",
        "scripts/foyer_fibonacci.py",
        "scripts/aiguille_grille.py",
        "scripts/recursion_argent.py",
        "scripts/sphere_faisceaux.py",
        "scripts/vingt_quatre_miroir.py",
        "scripts/carre_neuf_points.py",
        "scripts/tiers_dimension.py",
        "scripts/carte_connexions.py",
        "scripts/venn_ppm.py",
        "scripts/centre_venn.py",
        "resultats/resultats.md",
        "resultats/archimede.md",
        "resultats/trois_solides.md",
        "resultats/aiguille.md",
        "resultats/foyer_fibonacci.md",
        "resultats/aiguille_grille.md",
        "resultats/recursion_argent.md",
        "resultats/sphere_faisceaux.md",
        "resultats/vingt_quatre_miroir.md",
        "resultats/carre_neuf_points.md",
        "resultats/tiers_dimension.md",
        "resultats/carte_connexions.md",
        "resultats/venn_ppm.md",
        "resultats/centre_venn.md",
        "figures/b8_glissement_50.png",
        "figures/d1_trois_solides.png",
        "figures/e1_aiguille_kakeya.png",
        "figures/h1_foyer_menisques.png",
        "figures/n1_aiguille_grille.png",
        "figures/q1_recursion_argent.png",
        "figures/u2_cartes_losange.png",
        "figures/v1_vingt_quatre.png",
        "figures/ab2_cercles_arctiques.png",
        "figures/ad2_deux_ombres.png",
        "figures/ae1_centre_moitie.png",
        "figures/ae2_diaphragmes_diffraction.png",
        "recueil/observations/005-moitie-exacte-venn-19-ramp12h.md",
        "recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md"
      ],
      "questions": [
        "Fais l'inventaire de toutes les moitiés du corpus (au moins douze) : partie, section, script, résultat, exacte ou approchée.",
        "Classe chacune par procédé : involution sans point fixe (complément, antipode, x ↦ −x), dilatation d'un cran (l'aire en r²), équation (Ullisch, cordes de partage), inclusion–exclusion, autre. Dis lesquelles se recollent, et où (XXX § 3 : le cercle R/√2 ; XX § 1 et XXII § 1 : la corde √2).",
        "La moitié par équation devient-elle la moitié par involution quand la dimension tend vers l'infini ? Écris la chaîne exacte, avec les nombres de resultats/sphere_faisceaux.md et de resultats/carre_neuf_points.md.",
        "Fiche 005 : existe-t-il une involution qui forcerait la moitié des croisements ? Sinon, pourquoi une probabilité de l'ordre de 1/(dispersion) (XXX § 7.3) est-elle la bonne ? Que faudrait-il pour que la moitié devienne exacte ?",
        "Les crans : 6,644 crans par décade (XXI § 3, XXVII § 3), 12,91 crans de f/1 à f/88 (XXX § 4.1), une courbe = un cran (XXIX § 3.3), la FTM50 (VIII § 3, XXX § 4.5) : est-ce un seul procédé ? Lequel ?",
        "Fiche 010 : les 39,34 % (arccos(1 − k²/2)/π) et la corde de Ptolémée de 70,81° (partie X) sont-ils la même moitié, vue depuis un anneau ?",
        "Pour le test T5 (fait par l'agent aiguilles), écris ce que chaque issue changerait à l'arbre P2 du plan. Puis propose au moins trois fiches nouvelles."
      ]
    },
    {
      "label": "bases",
      "dossier": "recueil/dossiers/bases-congruences-premiers.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "pi-dimensions.md",
        "nombres-polynomes.md",
        "moire-fibonacci.md",
        "angle-or-aiguilles.md",
        "lentille-144.md",
        "aiguille-grille.md",
        "bases-objets.md",
        "vingt-quatre-miroir.md",
        "tranche-aiguilles.md",
        "kakeya-miroir.md",
        "octaedre-perron-venn.md",
        "scripts/pi_dimensions.py",
        "scripts/polynomes.py",
        "scripts/moire_fibonacci.py",
        "scripts/angle_or_aiguilles.py",
        "scripts/lentille_144.py",
        "scripts/aiguille_grille.py",
        "scripts/bases_objets.py",
        "scripts/vingt_quatre_miroir.py",
        "scripts/tranche_aiguilles.py",
        "scripts/kakeya_miroir.py",
        "scripts/octaedre_perron_venn.py",
        "scripts/recueil_verifications.py",
        "scripts/revision_001.py",
        "resultats/pi_dimensions.md",
        "resultats/polynomes.md",
        "resultats/moire_fibonacci.md",
        "resultats/angle_or_aiguilles.md",
        "resultats/lentille_144.md",
        "resultats/aiguille_grille.md",
        "resultats/bases_objets.md",
        "resultats/vingt_quatre_miroir.md",
        "resultats/tranche_aiguilles.md",
        "resultats/kakeya_miroir.md",
        "resultats/octaedre_perron_venn.md",
        "resultats/recueil_verifications.md",
        "figures/g2_virgule_binaire.png",
        "figures/k1_angle_or_aiguilles.png",
        "figures/l1_lentille_144.png",
        "figures/t1_bases_modulaires.png",
        "figures/v1_vingt_quatre.png",
        "figures/z2_tranche_aiguilles.png",
        "figures/aa2_virgule_miroir.png",
        "figures/ac3_venn17.png",
        "recueil/observations/001-2-moins-17-chiffres-de-5-puissance-17.md",
        "recueil/observations/005-moitie-exacte-venn-19-ramp12h.md",
        "recueil/observations/013-racines-digitales-de-2-et-5-et-periode-de-1-sur-7.md",
        "recueil/observations/014-fractions-continues-imaginaires.md",
        "recueil/observations/015-dizaines-de-premiers-cube-et-reste-modulo-3.md"
      ],
      "questions": [
        "Dresse les chaînes de production des parties VII, IX, XI, XII, XIX, XXI, XXV, XXVI et XXVIII (leurs sections sur les nombres), et de scripts/recueil_verifications.py.",
        "Le quart de tour i modulo b : rassemble toutes les occurrences (3 modulo 10, 7 modulo 50, 4 modulo 17, i modulo 53, √2 = ±i dans F₉) et le théorème de XIX § 2. Quelles bases du corpus ont un i, lesquelles non, et qu'est-ce que cela change à leur horloge (reflets contre quarts de tour) ?",
        "Congruence K3 : vérifie par un calcul rapide la famille b = q² + 1 (q premier, p = q² − q + 1 : q² ≡ −1 et q·p ≡ 1 modulo b, p − 1 = φ(b − 1), p divise q³ + 1), et écris l'argument qui explique les cas (5, 3) et (10, 7) du test 4.1 de scripts/revision_001.py.",
        "Test T6 : prépare le test de la tour 2-adique des périodes (Hasse 1966), relie-le à resultats/recueil_verifications.md, § 5, et au miroir de 1/17 (XXVIII § 3.6).",
        "Test T7 : prépare le test des trois 4/3 (les puissances sous b, V₃/V₂, 1/x₀ = n + 4/3).",
        "Les réduites et les trois distances (XI § 2, XIV § 1 et 3, XV § 5, XIX § 4, XX § 6, XXVI § 2.5) : est-ce un seul théorème ? Écris le diésis et le comma comme des écarts des trois distances.",
        "Fiches 001, 005, 013, 014 et 015 : leurs liens, et ce que le test 4.2 de l'agent de session change pour la fiche 015 (la dérive en 1/ln N, le rapport 2 de Hardy et Littlewood).",
        "Trous : le biais de Tchebychev (Rubinstein et Sarnak 1994), le biais des premiers consécutifs (Lemke Oliver et Soundararajan 2016), les densités de Hasse. Que manque-t-il dans les tables publiées des premiers par chiffre des unités et par dizaine (à vérifier) ? Propose au moins trois fiches nouvelles."
      ]
    },
    {
      "label": "grain",
      "dossier": "recueil/dossiers/grain-pixels-centres.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "carre-ptolemee.md",
        "aiguille-grille.md",
        "grille-decalee.md",
        "pixels-longitudes.md",
        "lentilles-boules-grain.md",
        "venn-ppm.md",
        "centre-venn.md",
        "scripts/carre_ptolemee.py",
        "scripts/aiguille_grille.py",
        "scripts/grille_decalee.py",
        "scripts/pixels_longitudes.py",
        "scripts/lentilles_boules_grain.py",
        "scripts/venn_ppm.py",
        "scripts/centre_venn.py",
        "resultats/carre_ptolemee.md",
        "resultats/aiguille_grille.md",
        "resultats/grille_decalee.md",
        "resultats/pixels_longitudes.md",
        "resultats/lentilles_boules_grain.md",
        "resultats/venn_ppm.md",
        "resultats/centre_venn.md",
        "figures/j1_carre_ptolemee.png",
        "figures/n2_perron_grille.png",
        "figures/o1_grille_decalee.png",
        "figures/r1_pixels_contacts.png",
        "figures/r2_longitudes_lumiere.png",
        "figures/x1_lentilles_boules_grain.png",
        "figures/ad1_venn_ppm.png",
        "figures/ae1_centre_moitie.png",
        "figures/ae3_grains_hasard.png",
        "recueil/observations/001-2-moins-17-chiffres-de-5-puissance-17.md",
        "recueil/observations/006-centre-de-la-lumiere-selon-la-pesee.md",
        "recueil/observations/007-premier-centre-faux-point-de-depart.md",
        "recueil/observations/008-dessin-centre-au-millieme-de-pixel.md",
        "recueil/observations/011-centre-du-venn-19-a-la-limite-a-2000-px.md",
        "/home/user/dzoba/venn17/images/venn17-pressure-dark-2000.png",
        "/home/user/dzoba/venn17/plotter/plotter_svg.py",
        "/home/user/dzoba/venn17/README.md"
      ],
      "questions": [
        "Dresse les chaînes de X § 2–3, XIV § 6, XV § 3, XVIII, XXIII § 3–4, XXIX § 1–4 et XXX § 1, 2.4 et 6.",
        "Le budget de décision : pour chaque mesure du dossier, la précision accessible (px, ppm, chiffres) et ce qu'elle peut trancher. Un tableau unique (par exemple : le centre à 0,003 px ; le cercle de demi-aire à ±1 830 ppm ; un croisement de 22,6 px), avec la source de chaque ligne.",
        "Les taux de change entre grain et pas (ε⁻², ε⁻¹, ε^(−1/2), le logarithme ; un bit par courbe, un demi-bit en longueur) : un tableau unique, avec la source de chaque ligne.",
        "Test T4 : lis les fonctions palette et write_svg de plotter_svg.py (ne lance rien), décris le classement des pixels par teinte et la façon d'estimer son erreur. L'ordre d'écriture des courbes dans le SVG est-il aussi celui de l'image PNG ? Cherche comment l'image a été rendue (README du dépôt) ; sinon, écris « à vérifier ».",
        "Congruence K10 : vérifie sur le tableau de XXX § 6.4 que W_centre/W_reste = √(n/4π) et que le seuil est n = 4π. Est-ce la constante isopérimétrique, ou une rencontre de constantes ? Propose la variation qui trancherait.",
        "Le biais propagé (fiche 007) : où d'autres chaînes du corpus partent-elles d'un point biaisé ou d'une fenêtre trop étroite (troncature d'une série, grille grossière, barycentre) ?",
        "Propose au moins trois fiches nouvelles, dont une pour D3 tirée des parties X, XV ou XVIII."
      ]
    },
    {
      "label": "lumiere",
      "dossier": "recueil/dossiers/lumiere-et-physique.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "README.md",
        "archimede.md",
        "foyer-fibonacci.md",
        "moire-fibonacci.md",
        "carre-ptolemee.md",
        "angle-or-aiguilles.md",
        "lentille-144.md",
        "perron-dephasage.md",
        "recursion-argent.md",
        "pixels-longitudes.md",
        "bases-objets.md",
        "sphere-faisceaux.md",
        "octaedre-perron-venn.md",
        "centre-venn.md",
        "scripts/chevre.py",
        "scripts/figures.py",
        "scripts/foyer_fibonacci.py",
        "scripts/moire_fibonacci.py",
        "scripts/carre_ptolemee.py",
        "scripts/angle_or_aiguilles.py",
        "scripts/lentille_144.py",
        "scripts/perron_dephasage.py",
        "scripts/recursion_argent.py",
        "scripts/pixels_longitudes.py",
        "scripts/bases_objets.py",
        "scripts/sphere_faisceaux.py",
        "scripts/octaedre_perron_venn.py",
        "scripts/centre_venn.py",
        "resultats/resultats.md",
        "resultats/archimede.md",
        "resultats/foyer_fibonacci.md",
        "resultats/moire_fibonacci.md",
        "resultats/carre_ptolemee.md",
        "resultats/angle_or_aiguilles.md",
        "resultats/lentille_144.md",
        "resultats/perron_dephasage.md",
        "resultats/recursion_argent.md",
        "resultats/pixels_longitudes.md",
        "resultats/bases_objets.md",
        "resultats/sphere_faisceaux.md",
        "resultats/octaedre_perron_venn.md",
        "resultats/centre_venn.md",
        "figures/fig7_optique.png",
        "figures/fig8_anneaux_newton.png",
        "figures/fig9_eclipses.png",
        "figures/b4_menisque.png",
        "figures/h1_foyer_menisques.png",
        "figures/h2_fibonacci.png",
        "figures/i1_moire_fibonacci.png",
        "figures/i2_optique_racines.png",
        "figures/k1_angle_or_aiguilles.png",
        "figures/l1_lentille_144.png",
        "figures/m1_perron_dephasage.png",
        "figures/q2_newton_polyedres.png",
        "figures/r2_longitudes_lumiere.png",
        "figures/t2_trait_cone_thales.png",
        "figures/u2_cartes_losange.png",
        "figures/ac3_venn17.png",
        "figures/ae2_diaphragmes_diffraction.png",
        "recueil/observations/002-diesis-fois-lumiere-du-17-gone.md",
        "recueil/observations/006-centre-de-la-lumiere-selon-la-pesee.md",
        "recueil/observations/009-34-plus-34-aigrettes.md",
        "/home/user/dzoba/venn17/plotter/plotter_svg.py"
      ],
      "questions": [
        "Dresse les chaînes optiques : README § 6, II § 3 et 9, VIII, IX § 1–3, X § 1 et 6, XI § 3–4, XII § 1 et 4, XIII § 1–4, XVII § 5, XVIII § 6–7, XIX § 6, XX § 4 et 6, XXVIII § 3.3, XXX § 1.2, 4.5, 5, 6.1 et 6.3.",
        "Pour chaque analogie physique du corpus (anneaux de Newton, éclipses, FTM, Fresnel, œil de poisson de Maxwell, Deschamps, Self, Wielen, HD, drizzle, Gustafsson, Hopkins, Friedel, Planck, l'IA) : ce qui est partagé exactement, ce qui est transporté, ce qui reste ouvert (CLAUDE.md, § 1). Un tableau.",
        "D8 n'a aucune chaîne propre (plan, § 1.0) : quelles analogies physiques mériteraient une fiche ? Propose-en au moins trois, avec leur test.",
        "Congruence K2 : vérifie que les aigrettes, l'ombre Σωⁱ et les éventails de Perron suivent la même parité pour N = 3 à 20 (les aigrettes sont déjà vérifiées pour 5, 6, 7, 8, 16, 17 et 18 lames, XXVIII § 3.3). Un calcul rapide suffit.",
        "Test T4 : à partir de resultats/centre_venn.md, § 1, montre si un modèle à une seule cause (la palette) peut reproduire les six écarts et leurs directions. Écris le modèle à deux causes (palette et ordre de dessin) et ce qu'il prédit pour la luminance.",
        "Fiches 002, 006 et 009 : leur place dans les arbres P3, P8 et P1 du plan.",
        "Trous dans les données publiées : le biais de couleur des parallaxes de Gaia (Lindegren et al. 2021, A&A 649, A4) et le déplacement induit par la couleur (Wielen 1996 ; Pourbaix et al. 2004). Que rangent dans le bruit les catalogues qui supposent une source unique ?"
      ]
    },
    {
      "label": "aiguilles",
      "dossier": "recueil/dossiers/aiguilles-kakeya-perron.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "aiguille-kakeya.md",
        "carre-ptolemee.md",
        "perron-dephasage.md",
        "aiguille-grille.md",
        "recursion-argent.md",
        "bases-objets.md",
        "tranche-aiguilles.md",
        "kakeya-miroir.md",
        "carte-connexions.md",
        "octaedre-perron-venn.md",
        "scripts/aiguille.py",
        "scripts/carre_ptolemee.py",
        "scripts/perron_dephasage.py",
        "scripts/aiguille_grille.py",
        "scripts/recursion_argent.py",
        "scripts/bases_objets.py",
        "scripts/tranche_aiguilles.py",
        "scripts/kakeya_miroir.py",
        "scripts/carte_connexions.py",
        "scripts/octaedre_perron_venn.py",
        "resultats/aiguille.md",
        "resultats/carre_ptolemee.md",
        "resultats/perron_dephasage.md",
        "resultats/aiguille_grille.md",
        "resultats/recursion_argent.md",
        "resultats/bases_objets.md",
        "resultats/tranche_aiguilles.md",
        "resultats/kakeya_miroir.md",
        "resultats/carte_connexions.md",
        "resultats/octaedre_perron_venn.md",
        "figures/e1_aiguille_kakeya.png",
        "figures/j1_carre_ptolemee.png",
        "figures/m1_perron_dephasage.png",
        "figures/n1_aiguille_grille.png",
        "figures/n2_perron_grille.png",
        "figures/q1_recursion_argent.png",
        "figures/z2_tranche_aiguilles.png",
        "figures/aa1_kakeya.png",
        "figures/ab3_liens_predits.png",
        "figures/ac2_perron.png",
        "recueil/observations/003-34-tan-pi-sur-34-et-pi.md",
        "recueil/observations/011-centre-du-venn-19-a-la-limite-a-2000-px.md"
      ],
      "questions": [
        "Dresse les chaînes de V, X § 4, XIII § 1, 3 et 6, XIV, XVII § 4, XIX § 2 et 6, XXV § 3, XXVI § 1 et 3.6, XXVII § 7, XXVIII § 2 et 3.3–3.5.",
        "Perron : de 2/(k + 2) vérifié (V § 3) à démontré (XXVIII § 2). La fenêtre de Kakeya à 10⁻⁵⁰ et la constante entre π/2 et π·ln 2 : que manque-t-il pour la constante ?",
        "Les aiguilles de la grille et les réduites (Fibonacci, Pell, Farey, Pick, Eisenstein) : écris la demi-case comme le procédé commun, avec ses sources.",
        "Congruence K7 : le grain plafonne Perron (XIV § 6, produit par log₂ n vers 2,8) et le centre du Venn (fiche 011, XXX § 6.4). La différence est-elle exactement un cran ?",
        "Test T5 : prépare l'extension de minimum_kakeya (scripts/aiguille_grille.py) aux corps F_q (q = 2, 3, 4, 5, 7, 8, 9), avec les symétries et le compte des points couverts 1, 2, 3 fois. Dis ce que Blokhuis et Mazzocca (2008) établissent exactement, et ce qui est connu pour q pair (à vérifier).",
        "D5 n'a aucune fiche principale : propose au moins trois fiches (faits amusants, analogies) tirées des parties V, XIII, XIV, XXVI ou XXVIII, avec leur test.",
        "Fiches 003 et 011 : leur place dans les arbres P1, P3 et P5 du plan.",
        "Trous : Keich 1999 (l'ordre, pas la constante), Wang et Zahl 2025 (la constante en 3D n'est pas calculée), Dvir 2009 ; dis ce que chacun laisse ouvert."
      ]
    },
    {
      "label": "ombres",
      "dossier": "recueil/dossiers/ombres-cube-venn.md",
      "phase": 1,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "archimede.md",
        "grille-decalee.md",
        "sphere-faisceaux.md",
        "vingt-quatre-miroir.md",
        "carre-neuf-points.md",
        "kakeya-miroir.md",
        "carte-connexions.md",
        "octaedre-perron-venn.md",
        "venn-ppm.md",
        "centre-venn.md",
        "scripts/archimede.py",
        "scripts/calculs_archimede.py",
        "scripts/grille_decalee.py",
        "scripts/sphere_faisceaux.py",
        "scripts/vingt_quatre_miroir.py",
        "scripts/carre_neuf_points.py",
        "scripts/kakeya_miroir.py",
        "scripts/carte_connexions.py",
        "scripts/octaedre_perron_venn.py",
        "scripts/venn_ppm.py",
        "scripts/centre_venn.py",
        "scripts/revision_001.py",
        "resultats/archimede.md",
        "resultats/grille_decalee.md",
        "resultats/sphere_faisceaux.md",
        "resultats/vingt_quatre_miroir.md",
        "resultats/carre_neuf_points.md",
        "resultats/kakeya_miroir.md",
        "resultats/carte_connexions.md",
        "resultats/octaedre_perron_venn.md",
        "resultats/venn_ppm.md",
        "resultats/centre_venn.md",
        "figures/b1_six_projections.png",
        "figures/b3_cube_tournant.png",
        "figures/o1_grille_decalee.png",
        "figures/u1_chevres_faisceaux.png",
        "figures/v2_racine_sept.png",
        "figures/w1_carre_neuf_points.png",
        "figures/aa3_cube_hexagone.png",
        "figures/ab2_cercles_arctiques.png",
        "figures/ac1_octaedre.png",
        "figures/ac3_venn17.png",
        "figures/ad1_venn_ppm.png",
        "figures/ad2_deux_ombres.png",
        "figures/ae1_centre_moitie.png",
        "recueil/observations/003-34-tan-pi-sur-34-et-pi.md",
        "recueil/observations/004-triangles-et-ombres-egales-octaedre.md",
        "recueil/observations/005-moitie-exacte-venn-19-ramp12h.md",
        "recueil/observations/006-centre-de-la-lumiere-selon-la-pesee.md",
        "recueil/observations/008-dessin-centre-au-millieme-de-pixel.md",
        "recueil/observations/009-34-plus-34-aigrettes.md",
        "recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md",
        "recueil/observations/015-dizaines-de-premiers-cube-et-reste-modulo-3.md",
        "/home/user/dzoba/venn17/README.md",
        "/home/user/dzoba/venn17/verify/RESULTS.md",
        "/home/user/dzoba/venn17/verify/RESULTS-19.md",
        "/home/user/dzoba/venn17/verify/RESULTS-23.md"
      ],
      "questions": [
        "Dresse les chaînes de II § 1–2, XV § 1, XX § 3 et 5, XXI § 1 et 4, XXII § 3–4, XXVI § 3, XXVII § 2, 4 et 8, XXVIII § 1 et 3, XXIX § 1–2 et 5, XXX § 3.",
        "Le cube {0, 1}ⁿ et ses ombres : fais le tableau des regards (une direction quelconque : Perron, binaire ; la grande diagonale : Venn, binomiale ; l'ombre symétrique Σωⁱ : polygone à 2n côtés ; les axes d'ordre 3 et 4 : cercles arctiques), avec ce qui est démontré et où.",
        "Le nerf : les faisceaux de chèvres (XX § 3, XXII § 3) et le nerf des dossiers (test T1) sont le même procédé de Čech. Dis ce que le nerf des dossiers peut dire et ce qu'il ne peut pas dire (le théorème du nerf demande des intersections contractiles : qu'est-ce que cela voudrait dire pour des dossiers ?).",
        "Fiche 015 : la face choisie par le reste modulo 3 est-elle une ombre du cube {0, 1}⁴, ou une restriction à une face ? Écris la correspondance exacte.",
        "Gelé et liquide (XXIX § 5.3) contre les cercles arctiques (XXVII § 2) : pourquoi la couche gelée des Venn reste-t-elle mince ? Que faudrait-il pour une forme limite ?",
        "Fiches 003, 004, 005, 006, 008, 009 et 010 : leur place dans l'arbre P1 du plan ; lesquelles sont des rameaux de hasard ?",
        "Trous : un Venn simple, symétrique et symétrique par le complément à 17 ou 19 courbes ; les certificats à 23 courbes (verify/RESULTS-23.md du dépôt de Dzoba) ; ce que le dépôt publie et ce qu'il ne publie pas (la moitié des croisements, la symétrie par le complément, l'ordre de dessin). Propose au moins trois fiches nouvelles."
      ]
    },
    {
      "label": "methode",
      "dossier": "recueil/dossiers/hasard-et-methode.md (vérification croisée des tests et des chaînes ; les huit sections des dossiers de la phase 1, décrites dans gabarit.phase_1, plus le tableau des quinze fiches de la question 2)",
      "phase": 2,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "recueil/dossiers/corde-et-dimensions.md",
        "recueil/dossiers/moities-et-crans.md",
        "recueil/dossiers/bases-congruences-premiers.md",
        "recueil/dossiers/grain-pixels-centres.md",
        "recueil/dossiers/lumiere-et-physique.md",
        "recueil/dossiers/aiguilles-kakeya-perron.md",
        "recueil/dossiers/ombres-cube-venn.md",
        "recueil/index.csv",
        "pi-dimensions.md",
        "zone-confusion.md",
        "perron-dephasage.md",
        "pixels-longitudes.md",
        "tiers-dimension.md",
        "carte-connexions.md",
        "venn-ppm.md",
        "centre-venn.md",
        "scripts/centre_venn.py",
        "scripts/venn_ppm.py",
        "scripts/carte_connexions.py",
        "scripts/recueil_index.py",
        "scripts/recueil_verifications.py",
        "scripts/revision_001.py",
        "resultats/pi_dimensions.md",
        "resultats/zone_confusion.md",
        "resultats/perron_dephasage.md",
        "resultats/pixels_longitudes.md",
        "resultats/tiers_dimension.md",
        "resultats/carte_connexions.md",
        "resultats/venn_ppm.md",
        "resultats/centre_venn.md",
        "resultats/recueil_verifications.md",
        "figures/f2_dimension_reelle.png",
        "figures/ab1_carte.png",
        "figures/ad2_deux_ombres.png",
        "figures/ae3_grains_hasard.png",
        "recueil/observations/001-2-moins-17-chiffres-de-5-puissance-17.md",
        "recueil/observations/002-diesis-fois-lumiere-du-17-gone.md",
        "recueil/observations/003-34-tan-pi-sur-34-et-pi.md",
        "recueil/observations/004-triangles-et-ombres-egales-octaedre.md",
        "recueil/observations/005-moitie-exacte-venn-19-ramp12h.md",
        "recueil/observations/006-centre-de-la-lumiere-selon-la-pesee.md",
        "recueil/observations/007-premier-centre-faux-point-de-depart.md",
        "recueil/observations/008-dessin-centre-au-millieme-de-pixel.md",
        "recueil/observations/009-34-plus-34-aigrettes.md",
        "recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md",
        "recueil/observations/011-centre-du-venn-19-a-la-limite-a-2000-px.md",
        "recueil/observations/012-tests-a-tolerance-et-liens-de-structure.md",
        "recueil/observations/013-racines-digitales-de-2-et-5-et-periode-de-1-sur-7.md",
        "recueil/observations/014-fractions-continues-imaginaires.md",
        "recueil/observations/015-dizaines-de-premiers-cube-et-reste-modulo-3.md"
      ],
      "questions": [
        "La lignée des tests du corpus : III § 2, puis VI § 3 bis et 3 ter, XIII § 5, XXIX § 5.5 et XXX § 7. Qu'est-ce que chaque étape a corrigé ?",
        "Pour chaque fiche 001 à 015 : le test appliqué est-il le bon selon la table du § 10 de CLAUDE.md ? Le verdict tient-il dans le budget de la donnée ? Un tableau de quinze lignes.",
        "Les chaînes de production : relève dans les sept dossiers les erreurs et les corrections (les 2,36 px ; la « quasi-coïncidence » de V corrigée en VI ; les trois phrases de XXII corrigées en XXIII ; Fraser puis Meyerson ; l'erratum d'Ullisch) et classe-les : point de départ biaisé, fenêtre trop étroite, pesée, troncature, cadre.",
        "Le cadre fabrique des liens (scripts/revision_001.py, § 2 : p_a + p_b < Σp²) : relie-le aux doubles zéros (Legendre et Legendre), aux données de composition (Pearson 1897, Aitchison 1986), à l'effet « regarder ailleurs » (Gross et Vitells 2010) et au jardin des chemins qui bifurquent (Gelman et Loken 2014).",
        "Test T8 : prépare le test du nerf contre la carte, et dis comment mesurer la dépendance entre les deux méthodes.",
        "Corrélation et causalité : pour les fiches de type Causalité (006, 007, 012), le lien est-il établi par une intervention (refaire l'essai en ne changeant qu'une chose) ou seulement par une corrélation ? (Reichenbach 1956 ; Pearl 2009.)",
        "Les tests de la révision (T1 à T8, plan § 4) : chacun respecte-t-il la table du § 10 ? Lequel risque de déclarer « hasard » une structure, ou l'inverse ?"
      ]
    },
    {
      "label": "croisement",
      "dossier": "vérification croisée : recueil/revisions/verification-croisee-001.md, en sept sections : le recouvrement v2 (un bloc JSON au format du § 1.9 du plan), les congruences, les triangles vides, les arbres corrigés, les doublons et contradictions, les trous dans les données publiées, les nouvelles fiches classées par dimension",
      "phase": 2,
      "fichiers": [
        "CLAUDE.md",
        "recueil/README.md",
        "recueil/index.md",
        "recueil/revisions/plan-001.md",
        "recueil/dossiers/corde-et-dimensions.md",
        "recueil/dossiers/moities-et-crans.md",
        "recueil/dossiers/bases-congruences-premiers.md",
        "recueil/dossiers/grain-pixels-centres.md",
        "recueil/dossiers/lumiere-et-physique.md",
        "recueil/dossiers/aiguilles-kakeya-perron.md",
        "recueil/dossiers/ombres-cube-venn.md",
        "recueil/index.csv",
        "README.md",
        "carte-connexions.md",
        "scripts/revision_001.py",
        "scripts/carte_connexions.py",
        "scripts/sphere_faisceaux.py",
        "resultats/carte_connexions.md",
        "resultats/recueil_verifications.md",
        "recueil/observations/001-2-moins-17-chiffres-de-5-puissance-17.md",
        "recueil/observations/002-diesis-fois-lumiere-du-17-gone.md",
        "recueil/observations/003-34-tan-pi-sur-34-et-pi.md",
        "recueil/observations/004-triangles-et-ombres-egales-octaedre.md",
        "recueil/observations/005-moitie-exacte-venn-19-ramp12h.md",
        "recueil/observations/006-centre-de-la-lumiere-selon-la-pesee.md",
        "recueil/observations/007-premier-centre-faux-point-de-depart.md",
        "recueil/observations/008-dessin-centre-au-millieme-de-pixel.md",
        "recueil/observations/009-34-plus-34-aigrettes.md",
        "recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md",
        "recueil/observations/011-centre-du-venn-19-a-la-limite-a-2000-px.md",
        "recueil/observations/012-tests-a-tolerance-et-liens-de-structure.md",
        "recueil/observations/013-racines-digitales-de-2-et-5-et-periode-de-1-sur-7.md",
        "recueil/observations/014-fractions-continues-imaginaires.md",
        "recueil/observations/015-dizaines-de-premiers-cube-et-reste-modulo-3.md"
      ],
      "questions": [
        "Le recouvrement : pour chaque dossier, les parties et les fiches du bloc JSON (plan, § 1.9) sont-elles celles que l'agent a réellement traitées ? Rassemble les corrections des sections 8 des dossiers et écris le recouvrement v2, au même format JSON.",
        "Les congruences K1 à K10 (plan, § 3) : pour chacune, recollement ou obstruction, avec la source ; ajoute celles que les dossiers ont trouvées.",
        "Les triangles vides : à partir du recouvrement v2, liste les triples de dossiers deux à deux sécants au niveau des fiches. Pour chacun, dis si une partie du corpus le remplit déjà (trou du recueil) ou non (trou du corpus), et propose l'observation qui le remplirait.",
        "La structure en Perron (plan, § 2) : vérifie les huit arbres contre les dossiers (branches, triangle du bas, disque) et corrige-les.",
        "Les doublons et les contradictions entre dossiers : un même nombre cité différemment, un même lien classé différemment, deux verdicts opposés.",
        "Les trous dans les données publiées : rassemble les pistes des dossiers, vérifie que chaque référence existe (sinon « à vérifier »), et classe-les par dossier.",
        "Les nouvelles fiches proposées : dédoublonne, et classe-les par dimension principale, pour que le prochain partage des aires soit plus équitable (au moins une pour D5 et une pour D8)."
      ]
    }
  ]
}
```
