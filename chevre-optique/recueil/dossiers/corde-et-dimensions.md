# La corde de toutes les dimensions

*Dossier de la révision 001, agent `corde` (phase 1). Écrit le 2026-10-07. Le plan est dans `recueil/revisions/plan-001.md` (§ 1.1 et § 5.2.1).*

## Pour lire ce dossier

- **Statuts.** *Démontré* : la preuve est dans le corpus, ou je l'ai refaite. *Calculé* : un script donne le nombre, exact ou numérique. *Mesuré* : lu sur une donnée, avec un grain. *Classique* : résultat publié. *Ma lecture* : une interprétation de l'agent. *Ouvert* : on ne sait pas.
- **Marques.** **(R)** : résultat du dépôt, avec son fichier de `resultats/` et sa section. **(A)** : calculé par l'agent, hors dépôt, dans un dossier temporaire ; à refaire dans `scripts/revision_001.py`. **(P)** : lu dans une publication ou sur un site (références au § 6.3).
- **Ce que je n'ai pas fait.** Je n'ai lancé aucun script du dépôt, et je n'ai écrit aucun autre fichier du dépôt que celui-ci. Les données externes `/home/user/dzoba/venn17` ne servent pas à ce dossier : je ne les ai pas lues.
- **Fichiers lus en plus de la liste du plan** (la liste de l'agent `corde` omet des sources que ses propres questions citent) : `carte-connexions.md` § 6 et § 8 avec `resultats/carte_connexions.md` § 6 ; `archimede.md` § 9 avec `resultats/archimede.md` § 9 et `scripts/calculs_archimede.py` section 9 ; `carre-ptolemee.md` § 5 avec `resultats/carre_ptolemee.md` § 4 ; `centre-venn.md` § 4.3 avec `resultats/centre_venn.md` § 4 ; `bases-objets.md` § 6 avec `resultats/bases_objets.md` § 4 ; `recursion-argent.md` et `vingt-quatre-miroir.md` (les fractions de Pell) ; `kakeya-miroir.md` (l'angle magique, par recherche de mots) ; les fiches 002, 003 et 011 ; `resultats/revision_001.md` § 1, § 4.4 et § 4.5 avec `scripts/revision_001.py` § 1, § 4.4 et § 4.5.
- **Un fait arrivé pendant mon travail.** `scripts/revision_001.py` a été complété par l'agent de session (sections 4.3 à 4.8, fichier daté de 20:30 ; dernier commit : « le plan complet et les huit tests calculés »). Son § 4.4 fait déjà T3 pour le polygone inscrit, et son § 4.5 fait T7. Au § 7, je compare mes résultats aux siens : ils concordent.
- **Ce que je n'ai pas pu lire.** Les articles de Fraser, de Meyerson et de Jameson (WebFetch a échoué ; seules des recherches web ont répondu, sans texte d'article). Le § 6.3 le dit à chaque endroit où cela compte.

## En bref

- **Un seul objet.** La corde r_n est la médiane de |X − P|² quand X est tiré au hasard dans la boule unité de dimension n et P est sur la clôture (README § 5.3). Les parties I à XXV en calculent chacune un morceau.
- **Trois liens forts.**
  1. *Le simplexe est le premier ordre de la médiane* : E[τ] = 0 donne exactement r² = 2n/(n + 1) (XXIV § 1, « Ordre 1 »), l'arête du simplexe de VI § 3. Le ménisque est le deuxième ordre, 2 × 1/6 × 2. Le dernier 2 est le nombre de dérangements de 3 : E[(1 − E)^j] = (−1)^j·!j pour une loi exponentielle (§ 3.3, (A)).
  2. *La chèvre plane est dans la série de la chèvre infinie.* La série de XXIV § 2, resommée par Borel–Padé, redonne la corde d'Ullisch à 6·10⁻¹⁰ (XXV § 1.2, (R)). Les deux chèvres de XX § 1 sont aussi les deux bouts de la bosse du ménisque (XXVII § 6).
  3. *Le tiers de dimension relie quatre parties.* N − n = (n + 1)·μ/(2x₀) exactement (A). C'est la colonne « décalage » de XV § 4, le « plan à 1/(n + 1) − μ/2 » de XXIII § 2, le « tiers » de XXIV § 3, et le K = N + 2 du simplexe de classification de `revision_001.py` § 1.
- **Trois trous.** (1) T3 : la corde et le polygone ont le même 1/6, pas le même ménisque (obstruction à l'ordre 4). (2) Le développement de la corde n'est confirmé dans aucune source que j'ai pu atteindre ; la preuve couvre n ≥ 100 ; la loi des grands ordres est dérivée, pas démontrée. (3) δ₂ ≈ δ₃ à 10⁻⁵ reste sans raison ; et les réseaux records atteignent √2 en dimension 3, 8 et 24 alors que la chèvre n'y arrive qu'à l'infini.
- **Corrections au recouvrement** : ajouter les parties II, X, XVII, XIX, XXVII ; ajouter les fiches 003 et 011 (002 en option, au choix de `croisement`) ; ne rien retirer (§ 8).

---

## 1. La question directrice et la projection sur D1–D8

### 1.1 La question

> Quel procédé unique fait passer la corde de la chèvre plane (Ullisch, 1,1587) à la diagonale √2 de la chèvre infinie, et que transporte-t-il d'une dimension à l'autre : le simplexe, le ménisque, le plan de la lentille, la série ? (plan, § 1.1)

### 1.2 La réponse en bref (ma lecture, appuyée sur XXIV § 1)

Le procédé est **la médiane**. On écrit X = ρU, avec ρ la distance au centre et U une direction uniforme. Alors |X − P|² = ρ² + 1 − 2ρU₁, et r² est la médiane de cette variable. La dimension n n'entre que par deux lois :

- **la coquille** : ρⁿ est uniforme sur [0, 1], donc E = −n ln ρ est *exactement* exponentielle, et E[ρ^a] = n/(n + a) ;
- **l'équateur** : U₁ a la densité ∝ (1 − u²)^k, avec k = (n − 3)/2.

Chaque partie de la liste lit l'une de ces deux lois :

| ce que la partie calcule | ce que c'est dans la médiane |
|---|---|
| l'équation unique (VII § 1, XX § 1) | la condition de médiane, écrite avec les intégrales de Wallis |
| le simplexe, arête² = 2n/(n + 1) (VI § 3) | le premier ordre : E[τ] = 0 |
| le plan de la lentille x₀ (XXIII § 2) | τ sur la coquille extérieure (ρ = 1) |
| la projection g² = (n − 1)/(n + 1) (XVI § 2) | le même premier ordre : E[ρ]/E[ρ⁻¹] |
| le ménisque μ ≈ 2/(3n²) (XVI, XXIV) | le deuxième ordre : 2 (double produit) × 1/6 (équateur) × 2 (coquille) |
| la série (XXIV § 2, XXV § 1) | tous les ordres ; elle diverge parce que le bord de la calotte (45°) est à ln √2 du sommet du sinus (90°) |

**Ce que le procédé transporte** d'une dimension à l'autre :
- le simplexe, à un tiers de dimension près (N = n + 1/3 − 112/(45n) + …) ;
- le plan de la lentille, x₀ = 1/(n + 1) − μ/2 (exact) ;
- une série en 1/n à coefficients rationnels, sans la constante de Wallis, qui ramène de la dimension infinie à la dimension 2 une fois resommée.

**Ce qu'il ne transporte pas** :
- la nature du nombre (transcendant en dimension paire, algébrique en dimension impaire : la série est rationnelle, sa somme ne l'est pas) ;
- l'égalité avec le simplexe, qui n'est vraie qu'au premier ordre ;
- le ménisque du polygone (T3, § 5 et § 7).

### 1.3 La projection sur D1–D8 (ma lecture)

Les poids du dossier font 1 (plan, § 1.10).

| dimension | poids du plan | poids de l'agent | ce qui le porte |
|---|---:|---:|---|
| D1 la chèvre et les cordes | 0,60 | 0,55 | I, VII, XVI, XX § 1, XXIV, XXV § 1 : la corde, son équation, sa série |
| D6 sphères, cubes, Venn et symétries | 0,20 | 0,15 | le simplexe (VI § 3), les faisceaux (XX § 3), le sommet e₃ (XXI § 5), le carré de neuf points et Leech (XXII), la grille décalée (XV) |
| D3 grain, pixels et précision | 0,10 | 0,10 | un grain, une dimension (XXIII § 3–4), les blocs de décimales (XXIV § 2), l'unité du grain (XXV § 1.5) |
| D2 bases, chiffres et congruences | 0,10 | 0,10 | les facteurs 2 et les retenues (VII § 5–7), les périodes des blocs (XXIV § 2), un 9 par décade de dimension (XXII § 1) |
| D8 physique | 0 | 0,05 | le cône à sommet imaginaire et la distance de Rayleigh (XIX § 6, XX § 1) ; le col g_n (§ 6.1, fiche F5) |
| D7 hasard et méthode | 0 | 0,05 | δ₂ ≈ δ₃, l'artefact flottant de XXIII, les seuils entiers de IV § 4 (§ 6.1, fiches F3, F6, F7) |
| D4, D5 | 0 | 0 (effleurés) | D5 : l'aiguille qui passe le bord de la chèvre à α_n (XXV § 1.5, fiche F4) ; D4 : le cran de XXIV § 5 |

Pourquoi je retire 0,05 à D1 et 0,05 à D6 : les maillons « grain » et « physique » sont plus nombreux que le plan ne le voyait, et D8 n'a aucune fiche principale dans le recueil (plan, § 6.1). Les fiches F5 et F4 du § 6.1 visent D8 et D5, deux dimensions vides.

### 1.4 Les notations qui se heurtent

Le dossier suit le corpus, où quatre angles se partagent trois symboles : α_n désigne deux angles différents, et β en désigne deux autres. Une confusion ici change une valeur de 54,59° à 70,81° ou à 109,19°.

| symbole | sens | valeur à n = 2 | où |
|---|---|---:|---|
| α_P | angle au piquet, r = 2R cos α_P ; tend vers 45° | 54,594° | README § 2.2 ; XXV § 1.1 (noté α) ; **`resultats/resultats.md` § 2 le nomme « α_n »** |
| α_n | angle au centre O, cos α_n = x₀ ; tend vers 90° | 70,812° | XX § 1–2, XXII, XXV § 1.5 ; `resultats/carre_neuf_points.md` § 1 ; CLAUDE.md § 6 |
| β | angle d'Ullisch : β = 2α_P = π − α_n | 109,188° | README § 2.2–3.1 ; `resultats/sphere_faisceaux.md` § 1 (β_n) ; `resultats/carre_ptolemee.md` § 4 |
| β (XXV) | 2α_P = π/2 + β, donc β = π/2 − α_n ; r² = 2 − 2 sin β | 19,188° | XXV § 1.1 |

Les valeurs viennent de (R) : `resultats/resultats.md` § 2 (54,59416°), `resultats/carre_neuf_points.md` § 1 (70,8117°), `resultats/carre_ptolemee.md` § 4 (β = 109,1883°). Le dernier angle (19,188°) est une différence que j'ai faite (A). Les autres symboles :

| symbole | sens | valeur à n = 2 |
|---|---|---:|
| x₀ | plan de la lentille = cos α_n = 1 − r²/2 | 0,328674 (R : `resultats/resultats.md` § 2) |
| μ | r² − 2n/(n + 1) | 0,0093183 (R : `resultats/menisque_projection.md` § 2) |
| g² | (n − 1)/(n + 1), la projection (XVI) | 1/3 |
| N | N = r²/(2 − r²) = 1/x₀ − 1 : la dimension du simplexe de même corde | 2,0425 (R : `resultats/tiers_dimension.md` § 3, N − n = 0,0425) |
| K | K = N + 2 = 1 + 1/x₀ : nombre de fiches du simplexe de classification | 4,0425 (R : `resultats/revision_001.md` § 1) |

---

## 2. Les chaînes de production (script → résultats → figures → document)

### 2.1 La chaîne de la corde, maillon par maillon (question 1)

Les scripts sont dans `scripts/`, les résultats dans `resultats/`, les figures dans `figures/`. « § » est la section du document de la partie ; « section » est celle du script (elle porte le même numéro que dans le fichier de résultats, sauf indication). Le statut dit ce qui est démontré, calculé ou mesuré.

**A. L'objet et son équation**

| n° | maillon | document | script (section ; fonctions) | résultats | figure (panneau) | statut |
|---|---|---|---|---|---|---|
| M1 | La corde est la distance médiane : P(\|X − P\| ≤ r) = ½, avec X = ρU | I § 5.3 | `chevre.py` (`fraction_broutee_mp`, `corde_moitie_mp`) | `resultats.md` § 2 | `fig1_geometrie.png` (c) | démontré (définition et concentration de la mesure) |
| M2 | Le plan : r = 2R cos α_P, sin β − β cos β = π/2 ; β = 1,905 695 729 309 88 rad (109,19°), r₂ = 1,158 728 473 018 12… | I § 2.2 | `calculs.py` section 1 | `resultats.md` § 1 | `fig1_geometrie.png` | calculé ; r₂ confirmé par l'OEIS A133731 (P) |
| M3 | La division d'Ullisch : β = ∮ z/f ÷ ∮ 1/f, sur \|z − 3π/4\| = π/4 | I § 3 | `chevre.py` (`racine_par_quotient`, `nombre_de_zeros`) ; `calculs.py` section 1 | `resultats.md` § 1 | `fig2_contour_ullisch.png` (a, b) | classique (Ullisch 2020, erratum 2023) ; calculé (un zéro dans le cercle ; erreur en 0,453^N) |
| M4 | L'équation unique : W_n(2α) − (2 cos α)ⁿ W_n(α) = ½ W_n(π) | I § 5.1 | `chevre.py` (`equation_chevre`, `W`) ; `calculs.py` section 2 | `resultats.md` § 2 | `fig3_dimensions.png` | démontré (calottes) ; calculé (accord à 30 chiffres, n = 2 à 8) |
| M5 | La même équation avec Q_n : rⁿ[Q_n(1) − Q_n(r/2)] = Q_n(1 − r²/2) ; polynômes entiers (n impair), κ_n et Π_n (n pair) | VII § 1–3 | `polynomes.py` sections 1–2 | `polynomes.md` § 1–2 | `g1_polynomes_retenues.png` | démontré (même équation) ; calculé (racines à 10⁻²⁸) |
| M6 | La même équation dans le plan méridien : G_n(β) = 0, G₂ = f/2 ; division d'intégrales dimension par dimension ; cordes certifiées à 10⁻⁵⁰ (n = 2, 3, 4, 8, 24) | XX § 1 | `sphere_faisceaux.py` section 1 (`I_n`, `G`, `division_sure`) | `sphere_faisceaux.md` § 1 | `u1_chevres_faisceaux.png` (b, c) | calculé (arithmétique d'intervalles) |
| M7 | La nature du nombre : transcendant (n pair, Baker), algébrique (n impair, Galois S_d) ; réciprocité κ_(2m)·h_(2m+1) = 1/(2m+1) | I § 5.5 ; VII § 2–4 ; XX § 2 | `calculs.py` section 3 ; `polynomes.py` sections 1–3 | `resultats.md` § 3 ; `polynomes.md` § 1–3 ; `sphere_faisceaux.md` § 2 | `g1_polynomes_retenues.png` | démontré (Baker 1966, Jordan) ; calculé (Galois par réduction modulo p, n = 5, 7, 9, 13) |
| M8 | Les pas de dimension : W_n·W_(n−1) = 2π/n ; Wallis ; les partages de IV (cône → √2, κ = ½ pour la chèvre) | III § 4–5 ; IV § 1–5 | `pi_dimensions.py` sections 3–4 ; `trois_solides.py` sections 1, 3–5 | `pi_dimensions.md` § 3–4 ; `trois_solides.md` § 1, 3–5 | `c1_pi_dimensions.png` ; `d1_trois_solides.png` (c) | démontré (récurrence de Wallis) ; calculé (Richardson : limites à 0,1 %) |

**B. Le premier ordre : le simplexe et le plan**

| n° | maillon | document | script (section ; fonctions) | résultats | figure (panneau) | statut |
|---|---|---|---|---|---|---|
| M9 | Le simplexe de sommet P et de hauteur R : arête² = 2n/(n + 1) ; plan en 1/(n + 1) = centre de gravité | VI § 3 | `zone_confusion.py` section 3 | `zone_confusion.md` § 3 | `f1_zone_confusion.png` (c, d) | démontré (géométrie) ; calculé (n²(r² − a²) : 0,037 à 0,65) |
| M10 | Les dimensions réelles (bêta incomplète) : la bosse de l'écart chèvre–simplexe ; ménisque, tangence, croisement | VI § 3 bis, § 3 quater | `zone_confusion.py` sections 3 bis et 3 ter (le passage ménisque → croisement) | `zone_confusion.md` § 3 bis, § 3 quater | `f2_dimension_reelle.png` (a, b) ; `f3_menisque_croisement.png` | calculé |
| M11 | La grille décalée : maille² = 2n/(n + 1) ; la chèvre atteint chaque valeur « d'or » plus tôt, de 0,041 à 0,105 : c'est N − n | XV § 2–4 | `grille_decalee.py` sections 2–4 | `grille_decalee.md` § 2–4 | `o1_grille_decalee.png` (b, d) | calculé (je retrouve les six décalages, (A)) |

**C. Le deuxième ordre : projection et ménisque**

| n° | maillon | document | script (section ; fonctions) | résultats | figure (panneau) | statut |
|---|---|---|---|---|---|---|
| M12 | La dimension infinie : ρ² = d² + 1 (la diagonale 1x, 1y) | XVI § 1 | `menisque_projection.py` section 1 | `menisque_projection.md` § 1 | `p1_contacts_disques.png` ; `p2_menisque_projection.png` (a) | démontré |
| M13 | Entre 2 et l'infini : r² = 1 + g² + μ, g² = (n − 1)/(n + 1) | XVI § 2 | `menisque_projection.py` section 2 | `menisque_projection.md` § 2 | `p2_menisque_projection.png` (a, b) | calculé ; démontré ensuite en XXIV § 1 |
| M14 | Le piquet à distance d : le plateau 2^(−1/n), l'hyperbole, le terme c_n/ρ² | XVI § 3, 5, 6 | `menisque_projection.py` sections 3, 5, 6 | `menisque_projection.md` § 3, 5, 6 | `p2_menisque_projection.png` (c, d) | calculé ; démontré en XXIV § 4 (n ≥ 4) et XXV § 1.4 (n = 2, 3) |

**D. Les faisceaux, le croisement, le grain**

| n° | maillon | document | script (section ; fonctions) | résultats | figure (panneau) | statut |
|---|---|---|---|---|---|---|
| M15 | n + 1 chèvres sur un simplexe, 2n sur le polytope croisé ; nerf de Čech ; arccos(1/n) < α_n < 90° | XX § 3 | `sphere_faisceaux.py` section 3 | `sphere_faisceaux.md` § 3 | `u1_chevres_faisceaux.png` (e) | calculé (rang exact modulo p) |
| M16 | Le croisement du plan : l'aiguille tourne de e₃ vers e₂ et passe le bord de la chèvre ; √2 au croisement | XXI § 5 | `vingt_quatre_miroir.py` section 4 | `vingt_quatre_miroir.md` § 4 | `v2_racine_sept.png` (d) | calculé ; exact en XXV § 1.5 (cos α_n = x₀) |
| M17 | Les pas de 10 se précipitent vers √2 : ρ_n jusqu'à n = 10⁸ ; n(2 − ρ²) = 2 − 8/(3n) ; Leech à √2 en 24D | XXII § 1, § 4 | `carre_neuf_points.py` sections 1, 4 | `carre_neuf_points.md` § 1, § 4 | `w1_carre_neuf_points.png` (b, f) | mesuré et calculé ; **artefact flottant au-delà de 10⁵ (§ 6.2, erreur 1)** |
| M18 | Le plan de la lentille : x₀ = 1/(n + 1) − μ/2, exact | XXIII § 2 | `lentilles_boules_grain.py` section 2 | `lentilles_boules_grain.md` § 2 | `x1_lentilles_boules_grain.png` (b) | exact (identité) ; calculé (13 valeurs de n) |

**E. La série et ses prolongements**

| n° | maillon | document | script (section ; fonctions) | résultats | figure (panneau) | statut |
|---|---|---|---|---|---|---|
| M19 | La démonstration en quatre pas : coquille exponentielle, équateur, moments exacts, inversion ; borne 1 800/n³ pour n ≥ 100 | XXIV § 1 | `tiers_dimension.py` section 1 (`Mp_sym`, `Mp_n`) | `tiers_dimension.md` § 1 | `y1_tiers_dimension.png` (a) | démontré (vérification exacte sur des polynômes à coefficients positifs) |
| M20 | Tous les termes μ_j (14 exacts, 30 à 170 chiffres) ; divergence ≈ j!(1/ln √2)^j ; troncature optimale ≈ 2^(−n/2)/n | XXIV § 2 | `tiers_dimension.py` section 2 (`developpement`, `serie`) | `tiers_dimension.md` § 2 | `y1_tiers_dimension.png` (b) | calculé (coefficients exacts, reproduits par moi) ; le taux A est mesuré |
| M21 | L'équation de la chèvre comme intégrale de Laplace ; singularité en racine carrée (Darboux) ; loi des grands ordres ; meilleure précision 1,0303·2^(−n/2)/n | XXV § 1.1 | `tranche_aiguilles.py` section 1 (`forme_laplace`, `richardson`) | `tranche_aiguilles.md` § 1 | `z1_ouverts.png` (a, b) | calculé ; la dérivation analytique n'est pas une preuve |
| M22 | Borel–Padé [19/19] : la corde plane sort de la série de la chèvre infinie | XXV § 1.2 | `tranche_aiguilles.py` section 1 (`borel_pade`) | `tranche_aiguilles.md` § 1 | `z1_ouverts.png` (c, d) | calculé (6·10⁻¹⁰ en n = 2) |
| M23 | Les ordres 2 à 8 démontrés, avec une borne pour n ≥ 100 | XXV § 1.3 | `tranche_aiguilles.py` section 2 (`borne_prouvee`, `zone_centrale`) | `tranche_aiguilles.md` § 2 | `z1_ouverts.png` (e) | démontré |
| M24 | c₂ = 4/405 et c₃ = 1/96 exacts par la lentille ; c_n = 2n(n − 1)/(3(n + 1)³(n + 3)) | XXIV § 4 ; XXV § 1.4 | `tiers_dimension.py` section 4 ; `tranche_aiguilles.py` section 3 | `tiers_dimension.md` § 4 ; `tranche_aiguilles.md` § 3 | `y1_tiers_dimension.png` (d) ; `z1_ouverts.png` (f) | démontré (n ≥ 4 par les moments ; n = 2, 3 par la lentille) |
| M25 | Le tiers de dimension : N = r²/(2 − r²), N − n de 0 à 1/3 ; 1/x₀ = n + 4/3 − 112/(45n) + … ; K = N + 2 | XXIV § 3 ; XXVII § 6 ; XXVII § 8 ; `revision_001.py` § 1 | `tiers_dimension.py` section 3 ; `carte_connexions.py` ; `revision_001.py` section 1 | `tiers_dimension.md` § 3 ; `carte_connexions.md` § 6 ; `revision_001.md` § 1 | `y1_tiers_dimension.png` (c) ; `ab3_liens_predits.png` (e) | calculé (n = 2 à 60 et décades) ; la limite 1/3 vient de la série |
| M26 | Le facteur 2 : Thalès et Euclide, r² = 2R(R − x₀) ; les lectures du grain (κ) | XXIV § 5 ; XXV § 1.5 | `tiers_dimension.py` section 5 ; `tranche_aiguilles.py` section 4 | `tiers_dimension.md` § 5 ; `tranche_aiguilles.md` § 4 | `y1_tiers_dimension.png` (e, f) | démontré (Euclide VI.8, classique) ; les lectures sont calculées |

### 2.2 Ce que chaque script produit

- **`chevre.py`** : bibliothèque, sans sortie. Les fractions de calotte, la fraction broutée, la corde de la moitié (`corde_moitie_mp`), la division d'intégrales (`racine_par_quotient`, `nombre_de_zeros`).
- **`calculs.py`** → `resultats/resultats.md` : § 1 le quotient d'Ullisch (β, r, convergence) ; § 2 la corde en dimension n par le quotient et par recherche directe (accord à 10⁻³⁰) avec α_P, x₀, 1/(n + 1) ; § 3 les polynômes et les groupes de Galois ; § 4 le piquet à distance δ et la courbe des 50 % ; § 5 volume et surface ; § 6 l'optique.
- **`figures.py`** → `fig1` à `fig9` (la corde : `fig1_geometrie.png`, `fig2_contour_ullisch.png`, `fig3_dimensions.png`, `fig6_courbes50_dimensions.png`).
- **`pi_dimensions.py`** → `pi_dimensions.md` § 1–5 et `c1_pi_dimensions.png` : la suite 3 + √2/10 + …, les formules de π, Wallis, les sommes sur toutes les dimensions, φ et le nombre plastique contre r₇.
- **`trois_solides.py`** → `trois_solides.md` § 1–6 et `d1_trois_solides.png` : les trois solides, la suite de π, les partages (corde de la moitié depuis O), les erreurs comparées.
- **`zone_confusion.py`** → `zone_confusion.md` § 1–5 et `f1`, `f2`, `f3` : la zone de 0,283 %, les croissants, le simplexe en dimension n, la bosse en dimension réelle, le test de la base 10, π − 3, la lunule.
- **`polynomes.py`** → `polynomes.md` § 1–5 et `g1`, `g2` : les polynômes impairs, les équations paires, la réciprocité, les retenues de Kummer, la preuve par la virgule binaire.
- **`grille_decalee.py`** → `grille_decalee.md` § 1–5 et `o1` : la grille décalée, la corde et la maille, la chèvre comptée, les dimensions d'or, l'aiguille.
- **`menisque_projection.py`** → `menisque_projection.md` § 1–6 et `p1`, `p2` : ρ² = d² + 1, r² = 1 + g² + μ, le plateau, les contacts, les trois déplacements, c_n.
- **`sphere_faisceaux.py`** → `sphere_faisceaux.md` § 1–7 et `u1`, `u2` : la division dimension par dimension, les cordes certifiées, la récurrence h_n et la part de la clôture, les faisceaux et le nerf de Čech, le losange, 3-8-24, la musique et l'IA, 10⁻⁵⁰.
- **`vingt_quatre_miroir.py`** → `vingt_quatre_miroir.md` § 1–4 et `v1`, `v2` : les trois 24, le miroir 49-50-51, √7, le croisement du plan.
- **`carre_neuf_points.py`** → `carre_neuf_points.md` § 1–4 et `w1` : ρ_n de 1 à 10⁸, le carré de neuf points, les faisceaux, Leech.
- **`lentilles_boules_grain.py`** → `lentilles_boules_grain.md` § 1–6 et `x1` : le contrôle de 2/(3n²), le plan x₀, les deux couches de décimales, les quatre taux de change du grain, le carré relu, 24D relu.
- **`tiers_dimension.py`** → `tiers_dimension.md` § 1–6 et `y1` : la démonstration et sa borne, les 14 coefficients exacts, N − n, le piquet à distance d, les lectures du grain.
- **`tranche_aiguilles.py`** → `tranche_aiguilles.md` § 1–7 et `z1`, `z2` : Laplace, Borel–Padé, les bornes des ordres 2 à 8, c₂ et c₃, α_n, la tranche 49–55, les tournants d'aiguilles.
- **`revision_001.py`** (de l'agent de session, pas de moi) → `revision_001.md` : § 1 K = N + 2 et Thalès ; § 4.4 T3 ; § 4.5 T7.

### 2.3 Les points faibles de la chaîne

1. **M17 n'est pas un maillon sûr au-delà de 10⁵.** Les tableaux de XXII § 1 et de XXIII § 1 et § 3 contiennent du bruit de double précision (§ 6.2, erreur 1). Ce qui reste solide : les valeurs jusqu'à 10⁵ et les identités.
2. **M20 à M22 ne se démontrent pas de la même façon.** Les coefficients sont exacts et démontrés (M19, M23). Le taux de divergence A est *mesuré* (30 termes). La loi des grands ordres (M21) est *dérivée* par Laplace et Darboux, puis vérifiée sur 40 coefficients : le rapport tend vers 1 comme 1 − 0,23/m (XXV § 1.1). Ce n'est pas une preuve.
3. **M22 dépend du nombre de coefficients.** Avec les 39 coefficients de `tranche_aiguilles.py`, l'erreur est 6·10⁻¹⁰ en n = 2 (R). Avec les coefficients jusqu'à 1/n¹² (ceux du tableau de `tiers_dimension.md` § 2), un Padé [5/6] donne 5,6·10⁻⁵ en n = 2 et 1,2·10⁻³ en n = 1 (A). Le résultat tient, mais il demande une quarantaine de coefficients.
4. **M24 et M19 ne couvrent pas les mêmes n.** Les moments de ρ⁻³ sont infinis pour n ≤ 3 : la méthode de XXIV s'applique à n ≥ 4 pour c_n, et la borne 1 800/n³ à n ≥ 100. Entre 4 et 99, la borne est *vérifiée sur les cordes calculées* (marge d'au moins 299 en dessous de 100, R : `tiers_dimension.md` § 1), pas démontrée.
5. **M25 : la monotonie de N − n est un contrôle, pas une preuve** (n = 2 à 60 et les décades, R : `tiers_dimension.md` § 3).
6. **Le maillon K = N + 2 n'a pas de script propre dans le corpus** avant `revision_001.py` § 1 : XXIV § 3 et XXVII § 6 donnent N − n, pas K.

---

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 Ce qui est établi

| n° | énoncé | statut | où, et comment je l'ai contrôlé |
|---|---|---|---|
| E1 | L'équation unique W_n(2α) − (2 cos α)ⁿ W_n(α) = ½ W_n(π) donne la corde de toute dimension ; ses trois écritures (I § 5.1, VII § 1, XX § 1) sont la même | démontré (calottes), calculé | R : `sphere_faisceaux.md` § 1 (cordes encadrées à 10⁻⁵⁰ pour n = 2, 3, 4, 8, 24). A : les trois écritures s'annulent à 10⁻³⁰ aux cordes certifiées (n = 2, 3, 8, 24) |
| E2 | Au premier ordre, la médiane est le simplexe : E[τ] = 0 donne exactement r² = 2n/(n + 1) | démontré | R : XXIV § 1 ; `tiers_dimension.md` § 1 |
| E3 | r_n² = 2n/(n + 1) + 2/(3n²) + O(n⁻³), avec \|reste\| < 1 800/n³ pour n ≥ 100 | démontré (vérification exacte) | R : XXIV § 1 ; `tiers_dimension.md` § 1. Hors de n ≥ 100, la borne est vérifiée sur les cordes calculées (marge ≥ 299) |
| E4 | Les coefficients μ_j sont rationnels, la constante de Wallis disparaît ; les ordres 2 à 8 sont démontrés, avec une borne pour n ≥ 100 | démontré | R : XXIV § 1 (pas 2) ; XXV § 1.3 ; `tranche_aiguilles.md` § 2. A : un solveur indépendant (séries de Laurent en fractions exactes) redonne μ₂ à μ₈ et 1/x₀ jusqu'à 1/n⁴ |
| E5 | La série diverge au taux A = 1/ln √2 = 2/ln 2 = 2,8854 ; la meilleure précision de la série tronquée est ≈ 1,03·2^(−n/2)/n | mesuré (le taux, 30 termes) ; calculé (la loi des grands ordres) | R : `tiers_dimension.md` § 2 (2,8839 à j = 28) ; XXV § 1.1. A : j* = 4, 6, 9 et erreurs 2,769·10⁻³, 2,269·10⁻⁴, 9,874·10⁻⁶ en n = 10, 16, 24, la série de r² coupée à 1/n^J (identiques à R ; en gardant 2n/(n + 1) exact, on trouve 2,751·10⁻³ en n = 10) ; rapport coefficient/loi à m = 10 : 0,96155 (identique à R) |
| E6 | La série, resommée par Borel–Padé, redonne la corde plane : r₂² = 1,342 651 673 575 pour 1,342 651 674 183 | calculé | R : XXV § 1.2 ; `tranche_aiguilles.md` § 1 (39 coefficients, [19/19]) |
| E7 | La chèvre de dimension n a la corde du simplexe de dimension N = n + 1/3 − 112/(45n) + … ; N − n monte de 0 à 1/3 | calculé (la monotonie) ; démontré (la limite, par la série) | R : XXIV § 3 ; `tiers_dimension.md` § 3. A : identité exacte N − n = (n + 1)·μ/(2x₀) (§ 3.2) |
| E8 | Piquet à distance d : k² = d² + (n − 1)/(n + 1) + 2D/(3n²) − 14D(2D + 5)/(15n³) + …, D = 1/d², valable pour d ≫ 1/√n ; c_n = 2n(n − 1)/(3(n + 1)³(n + 3)) | démontré (n ≥ 4) ; démontré en 2D et 3D par la lentille | R : XXIV § 4 ; XXV § 1.4 (c₂ = 4/405, c₃ = 1/96) |
| E9 | r² = 2R(R − x₀) : le facteur 2 entre le plan et l'aire est le diamètre en rayons | démontré (Thalès III.31, Euclide VI.8) | R : XXIV § 5 |
| E10 | cos α_n = x₀ exactement : l'aiguille qui tourne de e₃ vers e₂ passe le bord de la chèvre à α_n | démontré | R : XXV § 1.5 ; `tranche_aiguilles.md` § 4 |

### 3.2 Le tiers de dimension et K = n + 2 + (N − n) (question 2)

**Où le corpus l'avait déjà.**
- **XV § 4** : la colonne « décalage » (0,041 ; 0,049 ; 0,061 ; 0,074 ; 0,081 ; 0,105) *est* N − n, pris à la dimension où la chèvre atteint chaque maille. Pour la maille 2/√3, le simplexe a N = 2 et la chèvre l'atteint en n = 1,959 030 : 2 − 1,959 03 = 0,041. Je retrouve les six valeurs (A) ; elles sont dans `grille_decalee.md` § 4 (R). XV disait « le ménisque la décale d'une quantité qui grandit avec la dimension, de 0,04 à 0,1 », sans la limite.
- **XXIV § 3** : le nom, la table jusqu'à 10⁶ (0,0425 en 2D, 0,3333 en 10⁶) et la limite 1/3, qui sort de la série.
- **XXVII § 6** : le même N − n (0,0425 ; 0,1886 ; 0,3103 ; 0,3309), opposé à la bosse du ménisque en longueur (R : `carte_connexions.md` § 6).
- **XXVII § 8** : l'angle. −1/(n + 1) est le cosinus de l'angle au centre du simplexe de dimension n + 1 ; la chèvre a cos α_n = x₀, un peu moins. L'écart d'angle (0,283° en 2D) *est* le ménisque.
- **`revision_001.py` § 1** : le simplexe de classification à K fiches, avec c_K = ρ_n pour K − 1 = 1/x₀. Donc K = N + 2 = n + 2 + (N − n) (R : `revision_001.md` § 1 : K = 4,042527 en 2D).

**Comment ça se relie** (tout est exact ; les formules sont de moi, (A)) :
- *Le simplexe de VI § 3* (dimension n, n + 1 sommets, arête² = 2n/(n + 1)) est le simplexe de classification à K = n + 2 sommets vu par sa corde : c_K² = 2 − 2/(K − 1) = 2(K − 2)/(K − 1), qui vaut 2n/(n + 1) pour K = n + 2. La chèvre est le même simplexe à N + 2 sommets.
- *Le plan à 1/(n + 1)* (XXIII § 2) est le cosinus de l'angle entre deux sommets, avec K − 1 = n + 1. Pour la chèvre, K − 1 = 1/x₀. Le « décalage » K − 1 − (n + 1) est N − n.
- *L'identité* : N − n = 1/x₀ − (n + 1) = (n + 1)·μ/(2x₀). Je l'ai contrôlée en 40 chiffres pour n = 2, 3, 4, 10, 24, 100 : elle redonne 0,042527 ; 0,075997 ; 0,102366 ; 0,188555 ; 0,254544 ; 0,310288 (A), c'est-à-dire la table de XXIV § 3. Elle explique la montée : μ s'éteint comme 2/(3n²), mais le facteur (n + 1)/(2x₀) croît comme n². Ce que le ménisque perd en longueur, la dimension le regagne.
- *Pourquoi 4/3* : 1/x₀ = (n + 1)/(1 − (n + 1)μ/2) = n + 1 + (n + 1)²μ/2 + … → n + 1 + ½·(2/3) = n + 4/3. Le 1 est le simplexe (le centre de gravité), le 1/3 est la moitié de lim n²μ.
- *Thalès* : dans le triangle P Q P′ de XXIV § 5, PQ = r = c_K et QP′ = √(4 − r²) = d_K. C'est le même triangle que celui de `revision_001.py` § 1 (d_K² + c_K² = 4). L'angle entre deux sommets est π − α_n, soit l'angle β d'Ullisch en 2D : 109,188° contre 109,471° pour le tétraèdre (K = 4). Ce dernier lien est déjà dans XXVII § 8.

### 3.3 Les coefficients exacts et l'origine de chaque terme (question 3)

**Les coefficients** (R : `tiers_dimension.md` § 2, qui en donne 11 ; j = 2 à 8 ici) :

| j | μ_j dans μ = r² − 2n/(n + 1) = Σ μ_j/nʲ | valeur | μ_(j+1)/μ_j |
|---:|---|---:|---:|
| 2 | 2/3 | 0,666667 | −9,800 |
| 3 | −98/15 | −6,53333 | −8,697 |
| 4 | 5966/105 | 56,819 | −10,542 |
| 5 | −1698106/2835 | −598,979 | −13,233 |
| 6 | 247172734/31185 | 7926,01 | −16,103 |
| 7 | −258717260798/2027025 | −1,27634·10⁵ | −18,979 |
| 8 | 220958094270374/91216125 | 2,42236·10⁶ | −21,844 |

Les autres écritures (R : `tiers_dimension.md` § 2) :
- r² = 2 − 2/n + 8/(3n²) − 128/(15n³) + 6176/(105n⁴) − 1703776/(2835n⁵) + 247235104/(31185n⁶) − … ;
- x₀ = 1/n − 4/(3n²) + 64/(15n³) − 3088/(105n⁴) + 851888/(2835n⁵) − … ;
- 1/x₀ = n + 4/3 − 112/(45n) + 3856/(189n²) − 150832/(675n³) + … ; le terme suivant, 207502864/(66825n⁴), est de moi (A).

Les dénominateurs 3, 15, 105, 2835, 31185 sont des produits de nombres impairs : ce sont les 1/(2i + 1) de l'intégrale de l'équateur (XXIV § 2).

**D'où vient chaque terme (XXIV § 1).** La condition de médiane est Σᵢ (−1)ⁱ C(k, i)/(2i + 1)·E[τ^(2i+1)] = 0, avec k = (n − 3)/2 et τ = (ρ² + 1 − m)/(2ρ). Le terme i = 0 est le double produit ; les termes i ≥ 1 sont l'équateur, pondéré par la coquille.

| terme | ce qui l'amène | statut |
|---|---|---|
| 2n/(n + 1) = 2/(1 + 1/n) | **le simplexe** : E[τ] = ½(E[ρ] + (1 − m)E[ρ⁻¹]) = 0, exact | démontré (XXIV § 1) |
| μ₂ = 2/3 | 2 × 1/6 × 2 : **le double produit** (E[τ] = −(μ/2)·n/(n − 1)), **l'équateur** (k/3 ≈ n/6, courbure de la densité de U₁), **la coquille** (E[τ³] ≈ −2/n³, asymétrie de la loi exponentielle) | démontré (XXIV § 1) |
| μ₃ = −98/15 | cinq contributions, ci-dessous | (A), à refaire |
| μ_j (j ≥ 4) | à chaque ordre entre un terme de plus de l'équateur (i = j − 1), et les corrections en 1/n de tous les précédents | structure lue sur le solveur (A) |

**D'où vient −98/15 (calculé par l'agent, hors dépôt, à refaire dans `revision_001.py`).** Au troisième ordre (le coefficient de 1/n³ de l'équation de médiane), trois morceaux se compensent. Les chiffres sont les coefficients de e³ avec e = 1/n :

- le double produit : −(μ₃ + μ₂)/2, parce que E[τ] = −(μ/2)·n/(n − 1) et n/(n − 1) = 1 + e + … ;
- l'équateur, premier terme (τ³) : −11/6 ;
- l'équateur, deuxième terme (τ⁵) : −11/10.

La somme est nulle : −(μ₃ + 2/3)/2 = 11/6 + 11/10 = 44/15, donc μ₃ = −88/15 − 2/3 = −98/15. En détail :

| contribution à μ₃ | valeur | ce que c'est |
|---|---:|---|
| −μ₂ (le facteur n/(n − 1)) | −2/3 | le double produit, avec son moment exact E[ρ⁻¹] = n/(n − 1) |
| correction de la coquille dans E[τ³] | −2 | τ ≈ (1 − E)(1 − 1/n)/n, donc E[τ³] = −2/n³ + 6/n⁴ − … |
| rétroaction de μ₂ sur le seuil | +1/3 | m contient μ ; E[τ³] devient −2/n³ + 5/n⁴ − … |
| courbure de l'équateur : k = (n − 3)/2 et non n/2 | −2 | le « −3 » de k |
| deuxième terme de l'équateur (τ⁵) | −11/5 | C(k, 2)/5 × E[τ⁵], avec E[τ⁵] ≈ −44/n⁵ |
| **total** | **−98/15** | −10/15 − 30/15 + 5/15 − 30/15 − 33/15 |

Pour le contrôle : E[τ³] = −2e³ + 5e⁴ − (106/5)e⁵ + … avec la rétroaction, et −2e³ + 6e⁴ − 30e⁵ + … sans elle ; E[τ⁵] = −44e⁵ + 205e⁶ − … ; E[τ⁷] = −1854e⁷ + … (A).

**Le −2, le −44 et le −1854 sont des nombres de dérangements** (A). Pour E exponentielle de moyenne 1, E[(1 − E)^j] = Σᵢ C(j, i)(−1)ⁱ i! = (−1)^j·!j, où !j est le nombre de dérangements de j objets : 1, 0, 1, 2, 9, 44, 265, 1854… (j = 0 à 7, vérifié exactement jusqu'à j = 12). Le coefficient de tête de E[τ^(2i+1)] est −!(2i+1) : −2, −44, −1854 pour i = 1, 2, 3. Chaque terme de l'équateur entre donc à l'ordre e^(i+1) avec le poids (−1)^(i+1)·!(2i+1)/(2ⁱ·i!·(2i + 1)) = 1/3, −11/10, 309/56 (i = 1, 2, 3). Le « −2 de l'asymétrie de la coquille » de XXIV § 1 est !3 au signe près. C'est la fiche F1 du § 6.1.

**Pourquoi des termes impairs, et pourquoi le polygone n'en a pas.** Les séries du polygone (sinus, tangente) sont paires en y = π/N. La corde ne l'est pas, et un décalage n ↦ n + s fabrique du 1/n³ à partir du 1/n² : μ₂/(n + s)² = μ₂/n² − 2sμ₂/n³ + … Pour que ce décalage explique −98/15, il faut s = 49/10. C'est le s* de T3 (§ 7). Les cinq contributions ci-dessus ne ressemblent pas à un décalage unique : elles mêlent trois lois (double produit, coquille, équateur).

### 3.4 La chèvre plane et la chèvre infinie : la chaîne exacte (question 4)

1. **Le même procédé partout** (XX § 1, M6). La division de deux intégrales de contour donne la corde de chaque dimension, avec G₂ = f/2 en 2D. XX § 1 corrige une phrase : c'est la chèvre de dimension *infinie* qui est à la distance de Rayleigh de son faisceau (ρ = |d + i|), pas la chèvre plane.
2. **Une série en 1/n, de la dimension infinie vers le bas** (XXIV § 2, M20). Coefficients rationnels exacts, divergente : μ_(j+1)/μ_j ≈ −A·j (XXIV § 2), plus précisément −A·(j − ½) dès j = 4 (A).
3. **La forme de Laplace exacte** (XXV § 1.1, M21) : ∫₀^β (cos ψ/cos β)ⁿ dψ = ∫₀^∞ e^(−nu) tan φ(u) du, avec sin φ = sin α·e^(−u) et r² = 2 − 2 sin β. La singularité de tan φ est une racine carrée en u = −ln √2 : Darboux donne Γ(m − ½)/(ln √2)^m.
4. **Borel–Padé** (XXV § 1.2, M22). On divise μ_m par (m − 1)!, on prolonge la transformée de Borel par un Padé [19/19], on refait l'intégrale de Laplace. En n = 2 : 6·10⁻¹⁰. En n = 1 (corde 1) : 9·10⁻⁷ (R : `tranche_aiguilles.md` § 1).
5. **La bosse du ménisque** (VI § 3 bis, XXVII § 6, M10). En *longueur*, l'écart chèvre–simplexe est nul en n = 1, culmine en n = 2,08 (relatif, 0,3495 %) ou 2,24 (absolu), et s'éteint à l'infini. La chèvre plane (0,3488 %) est presque au sommet ; la chèvre infinie est à l'autre bout. Les maxima des autres mesures : δ en 2,42, μ en 2,42, c_n en 2,59, la part manquante en 3,20 (R : VI § 3 bis ; XVI § 2).
6. **Le tiers de dimension** (XXIV § 3, M25). Le *même* ménisque, compté en dimensions, monte sans bosse de 0 à 1/3 : N − n = (n + 1)μ/(2x₀).
7. **Là où la série simple échoue** : la meilleure troncature donne 0,32 en n = 2, 0,12 en n = 3, 0,03 en n = 5 (R : XXV § 1.2). L'erreur optimale est ≈ 1,03·2^(−n/2)/n. La série seule n'est fiable qu'à partir de n ≈ 10 (3·10⁻³), et la bosse du ménisque (n = 2 à 3) tombe dans la zone où elle ne l'est pas.

En une phrase : *la chèvre plane est la dimension 2 de la série de la chèvre infinie, une fois la série resommée ; la bosse du ménisque marque l'endroit où la troncature simple ne suffit plus.* Statut : calculé (6·10⁻¹⁰), pas démontré. Le lien analytique (une somme de Borel égale à la corde, avec un terme exponentiellement petit de l'ordre de 2^(−n/2)) est ouvert (§ 3.5, O2).

### 3.5 Ce qui reste ouvert

| n° | question | pourquoi elle est ouverte | où chercher |
|---|---|---|---|
| O1 | Le ménisque de la chèvre est-il celui d'un polygone, au-delà du 1/6 ? | T3 : recollement aux ordres 2 et 3, obstruction à l'ordre 4 (§ 5, § 7) ; le partenaire manque : un diaphragme au rayon distribué | XXX § 6.3 (défocalisation) ; XXVIII § 2.5 (le polygone circonscrit) |
| O2 | Quel est le terme exponentiellement petit qui complète la série ? | la meilleure précision est ≈ 2^(−n/2)/n, comme le reste (1/√2)ⁿ de XXIV § 2 : même taille ? Une transsérie reste à écrire | Boyd 1999 ; Bender–Orszag ; Flajolet–Sedgewick (§ 6.3) |
| O3 | La borne 1 800/n³ pour 4 ≤ n < 100 ; la monotonie de N − n en dimension réelle | vérifiées sur des cordes, pas démontrées ; E[ρ⁻³] est infini pour n ≤ 3 | XXIV § 4 (la limite de la méthode) ; XXV § 1.4 (2D et 3D par la lentille) |
| O4 | Pourquoi δ₂ ≈ δ₃ à 10⁻⁵ ? | la bosse explique l'essentiel (VI § 3 bis), pas la précision ; n* = 3,0000853 | § 5, obstruction B ; fiche F7 |
| O5 | Pourquoi les réseaux records atteignent-ils √2 en dimension 3, 8 et 24 ? | la chèvre n'y arrive qu'à l'infini : √2 − ρ_n = 0,1857 ; 0,0794 ; 0,0283 (A, à partir de `carre_neuf_points.md` § 1) | XX § 5 et XXII § 4 : « je ne sais pas » ; Conway–Parker–Sloane 1982 |
| O6 | Le choix de l'unité du grain (plan, aire, angle, cran) | le modèle physique le décide, pas le calcul (XXIV § 5, XXV § 1.5) | compter les dimensions autrement, au même grain |
| O7 | La loi des grands ordres, constante comprise, est-elle démontrable ? | dérivée par Laplace et Darboux, vérifiée sur 40 coefficients (1 − 0,23/m) | résurgence ; Darboux (Flajolet–Sedgewick, ch. VI) |

---

## 4. Les fiches du dossier : verdict, test, et la partie qui portait déjà le lien

Le plan donne deux fiches au dossier : 010 et 014. Je les juge d'abord (question 5). J'ajoute ensuite trois fiches que T3 et K10 citent (002, 003, 011) : leur place est discutée au § 8.

### 4.1 Fiche 010 — la chèvre d'Ullisch broute 39,34 % de chaque anneau du bord

`recueil/observations/010-ullisch-39-34-pourcent-de-chaque-anneau.md` · type Fait amusant · statut exact · partie XXX · dimension D1.

- **Verdict : lien fort, exact. Elle reste dans le dossier.** Les 39,34 % sont 2α₂/360°, avec α₂ = 70,8117° et cos α₂ = x₀ = 1 − k²/2 (k = 1,1587…). C'est la part de la clôture broutée par la chèvre plane. Le dossier la voit comme le cas n = 2 d'une famille : 0,3934 (n = 2), 0,3773 (n = 3), 0,3760 (n = 4, le minimum entier), 0,3786 (n = 5), puis la montée vers ½ (R : `sphere_faisceaux.md` § 2). Le minimum réel est vers n ≈ 3,67 (0,3758) (A).
- **La partie qui portait déjà le lien** (la fiche cite XX et X ; il y en a deux de plus) :
  - **X § 5** : « la corde de la chèvre est la corde de l'arc 180° − β = 70,81° » ; dans la table de Ptolémée (rayon 60), elle vaut 69;31,25, entre les cordes de 70°30′ (69,2574) et de 71° (69,6844) (R : `carre_ptolemee.md` § 4 ; je retrouve 120·sin(35,4058°) = 69,5237 (A)).
  - **XX § 1 et § 2** : l'angle α_n = π − β_n (70,812° en 2D) et la part de la clôture.
  - **XXII § 3** : les quatre chèvres du carré de neuf points broutent chacune un arc de ±70,81° sur la clôture (R : `carre_neuf_points.md` § 3).
  - **XXV § 1.5** : cos α_n = x₀ *exactement* (Euclide). La fiche 010 est donc un cas particulier d'un résultat démontré.
- **Test.** Fait par la fiche : précision, l'identité 2 arcsin(k/2) = arccos(1 − k²/2) à 50 chiffres. Le test « faire varier n » est déjà fait par XX § 2 (la table ci-dessus). Il reste à le citer dans la fiche.
- **Une réserve (A).** Le titre dit « de chaque anneau du bord ». C'est vrai du seul cercle de bord (ρ = 1) : `centre_venn.md` § 4 écrit d'ailleurs « du niveau 1 ». Pour un anneau de rayon ρ, la part est arccos((ρ² + 1 − k²)/(2ρ))/π : 39,34 % (ρ = 1), 39,57 % (0,99), 40,48 % (0,95), 41,64 % (0,9), 44,05 % (0,8), 46,64 % (0,7), 50 % (ρ = √(k² − 1) = 0,5854), 100 % (ρ ≤ k − 1 = 0,1587). La moyenne pondérée par l'aire redonne 50 % (intégrale numérique : 0,500000). Je propose d'écrire « du cercle de bord ».

### 4.2 Fiche 014 — les fractions continues imaginaires

`recueil/observations/014-fractions-continues-imaginaires.md` · type Fait amusant ; Analogie · statut exact · partie recueil · dimension D2.

- **Verdict : lien faible, par les nombres. Je la garde dans le dossier, avec cette étiquette.** √2 est la limite de la corde (I § 5.3). 2/√3 est l'arête du triangle de hauteur R (n = 2) et √(3/2) celle du tétraèdre (n = 3) (R : VI § 3 ; XV § 4). Aucun procédé de la corde ne produit une fraction continue imaginaire : le lien est celui des constantes, pas celui d'un calcul.
- **La partie qui portait déjà le lien.**
  - **XVII § 4** : la récursion d'argent T(d) = 2 − 1/(2d) est une fraction continue « avec des moins » ; ses positions exactes 0, 1/4, 2/7, 7/24, 12/41, 41/140… sont faites de nombres de Pell, ceux des fractions 3/2, 7/5, 17/12, 41/29, 99/70… qui approchent √2 ; ses points fixes sont 1 ∓ 1/√2. C'est la même famille que « √3 = 2 − 1/(4 − 1/(4 − …)) » de la fiche (même forme, coefficients constants). Le point orange de XVII § 1 est le bout du plateau de XVI § 3 : la chèvre plane y commence, avec la corde 1/√2.
  - **XXI § 2 et § 3** : Pell, 7² − 2·5² = −1 ; 7/5 et 10/7.
  - **XIX § 2** : i modulo 10, le i de la base (3 ≡ i).
- **Test** (fait par la fiche) : 61 étages, écart inférieur à 10⁻³⁰. *Test rapide de ma part (A)* : les arêtes √(2n/(n + 1)) des simplexes n'ont pas toutes la forme de √2. En dimension 2, 2/√3 = [1 ; 6, 2, 6, 2, …]. En dimension 3, √(3/2) = [1 ; 4, 2, 4, 2, …]. En dimension 5, √(5/3) = [1 ; 3, 2, 3, 2, …]. Pour √2, c'est [1 ; 2, 2, 2, …]. Mais en dimension 4, √(8/5) = [1 ; 3, 1, 3, 2, …], en 6 [1 ; 3, 4, 3, 2, …]. Le motif ne tient pas : pas de loi. Je ne propose pas de fiche.
- **Une idée (ma lecture, à ne pas croire sans test).** Les fractions « avec des moins » de XVII et de la fiche sont peut-être le bon outil pour écrire d₀ = 1 − 1/√2 et le plateau comme limites de convergentes : la récursion fait déjà 0,77 chiffre par pas (R : XVII § 4).

### 4.3 Trois fiches que T3 et K10 citent : 002, 003, 011

| fiche | ce qu'elle dit | ce qu'elle est pour T3 | verdict pour ce dossier | partie qui portait déjà le lien |
|---|---|---|---|---|
| **002** · D7 · hasard | (128/125) × la lumière du 17-gone ≈ 1, à 845 ppm | la lumière du polygone inscrit, 1 − sin x/x = x²/6 − x⁴/120 + …, avec x = 2π/17 (97,74 %) : le comparant de K1 | lien de comparaison, non de structure ; « hasard » reste juste (le produit ne vaut 1 qu'en N = 16,70) | XXIX § 5.5 ; XXX § 7 |
| **003** · D6 · structure | 34·tan(π/34) ≈ π, à 2 856 ppm ; loi de l'écart π³/(12N²) | le polygone circonscrit : 34·tan(π/34)/π − 1 = x²/3 + … avec x = π/34 (deuxième série de T3) | exactement une des trois séries de T3 : recollement à l'ordre 2, obstruction à l'ordre 4 (écart 2893/350 = 8,27, A) | XXVIII § 2.5 ; XXIX § 5.5 ; XXX § 7 |
| **011** · D3 · calculé | le centre du Venn devient le goulot dès 13 courbes ; W_centre = (2/π)√(n(2ⁿ − 2)) contre W_reste = 4√((2ⁿ − 2)/π) | K10 : le rapport vaut exactement √(n/(4π)), le seuil 4π = 12,566 (cercle) ou π/arctan(1/4) = 12,824 (segments) ; la correction par cordes est x²/6 avec x = π/n | exact (R : `revision_001.md` § 4.4) ; la troisième série de T3 : écart 26737/3150 = 8,49 (A) | XXX § 6.4 ; XIV (Perron sur une grille) |

Ces trois fiches sont dans le dossier par T3, pas par la chèvre. L'effet de leur ajout sur le nerf est au § 8.

---

## 5. Les congruences et les obstructions

Une congruence est un recollement à une transformation connue près ; une obstruction est ce qui ne se recolle pas, et elle désigne un trou (plan, § 3.0).

### 5.1 Celles du plan, côté corde

**K1 — la chèvre et le polygone, modulo x³ (test T3).** Je compare μ(n) = r_n² − 2n/(n + 1) = Σ μ_j/nʲ aux trois séries de lumière du plan, avec le changement de variable y = a·e/(1 + s·e), e = 1/n, y = π/N (calculé par l'agent, hors dépôt, à refaire ; le code est au § 7). Le facteur a est fixé par l'ordre 2 ; s par l'ordre 3. Les séries du polygone sont paires en y, donc s* = −μ₃/(2μ₂) = 49/10 est le même pour les trois.

| série comparée | a | écart à l'ordre 2 | écart à l'ordre 3 (s = 49/10) | écart à l'ordre 4 (s = 49/10) | ordre 5 | ordre 6 |
|---|---:|---:|---:|---:|---:|---:|
| inscrit : 1 − (N/2π) sin(2π/N) | 1 | 0 | 0 | 9379/1050 ≈ 8,93 | −287,9 | 6036 |
| circonscrit : N tan(π/N)/π − 1 | √2 | 0 | 0 | 2893/350 ≈ 8,27 | −274,8 | 5876 |
| cordes (K10) : (π/n)/sin(π/n) − 1 | 2 | 0 | 0 | 26737/3150 ≈ 8,49 | −279,2 | 5930 |

- **Sans décalage** (s = 0), l'ordre 3 vaut −98/15 pour les trois séries. Avec s = 1/3, 1 et 4/3, il vaut −274/45, −26/5 et −214/45 (les trois séries, A) : aucun de ces décalages « naturels » ne recolle l'ordre 3.
- **Mon résultat est celui de l'agent de session** : `resultats/revision_001.md` § 4.4 donne, pour l'inscrit avec N = π(n + s), 47,89 contre 56,82 à l'ordre 4 (écart 8,93). Je ne trouve aucune différence. Mon apport : les deux autres séries (circonscrit, cordes) et le décalage libre pour les trois.
- **La croissance** (point 3 du plan). μ_(j+1)/μ_j = −9,80 ; −8,70 ; −10,54 ; −13,23 ; −16,10 ; −18,98 pour j = 2 à 7 (R : `tiers_dimension.md` § 2), soit ≈ −A·(j − ½) avec A = 2/ln 2 dès j = 4 environ. Les rapports successifs des coefficients du polygone inscrit sont −0,200 ; −0,095 ; −0,056 ; −0,036 (A) : ils tendent vers 0, car la série est entière. La série du polygone converge partout ; celle de la chèvre diverge.
- **Verdict (calculé, avec la nuance ci-dessous)** : même exposant, même 1/6, pas le même ménisque. Le plan écrivait « obstruction dès l'ordre 3 » ; c'est vrai sans décalage. Avec un décalage libre, c'est **l'ordre 4** (déjà noté par l'agent de session). L'obstruction globale est plus profonde : une série divergente ne peut pas être f∘φ avec f et φ convergentes, et le polygone n'a pas d'asymétrie de coquille (§ 3.3).

**K8 — les trois 4/3, côté corde.** Les deux 4/3 de la corde n'ont pas la même origine (A) :
- V₃/V₂ = W₃ = 4/3 = 2·h₃ = 2·(2/3) : le rapport hémisphère/cylindre d'Archimède, doublé (III § 4 ; VII § 2) ;
- 1/x₀ = n + 4/3 + … : 4/3 = 1 + 1/3, le simplexe plus la moitié de lim n²μ = 2/3 (§ 3.2).

Le « 1/3 » est ∫₀¹ u² du dans les deux cas (dans W₃ = 2∫₀¹(1 − u²)du = 2(1 − 1/3), et dans le τ − kτ³/3 de l'équateur), mais il est combiné différemment : 2 − 2/3 d'un côté, 1 + 1/3 de l'autre. C'est ma lecture, et elle ne dit pas qu'un lien existe. Le verdict de T7 (R : `revision_001.md` § 4.5) : coïncidence de petits entiers, 4/3 seulement pour 10 ≤ b ≤ 16 et 244 ≤ b ≤ 256.

**K10 — le seuil du centre et l'isopérimétrie, côté corde.** Les formules de la fiche 011 se recollent exactement (R : `revision_001.md` § 4.4 : 4π = 12,566 et π/arctan(1/4) = 12,824). La correction polygonale (π/n)/sin(π/n) − 1 = π²/(6n²) + 7π⁴/(360n⁴) + … est la troisième série du tableau : même verdict que K1.

### 5.2 Les miennes

| n° | ce qui est comparé | transformation | jusqu'où ça se recolle | écart ou obstruction |
|---|---|---|---|---|
| **C-A** | la chèvre de dimension n et le simplexe de dimension N | n ↦ N = n + 1/3 − 112/(45n) + … (définie par c_K = ρ_n) | exactement, par définition ; modulo 1/n, N = n + 1/3 | la monotonie et la limite 1/3 (O3) |
| **C-B** | le plan x₀ et le centre de gravité 1/(n + 1) | x₀ = 1/(n + 1) − μ/2, et N − n = (n + 1)μ/(2x₀) | exactement (identité) | aucune |
| **C-C** | la chèvre infinie (série en 1/n) et la chèvre plane | resommation de Borel–Padé | à 6·10⁻¹⁰ en n = 2, 9·10⁻⁷ en n = 1 (R) | la série seule : 0,32 en n = 2 ; le terme exponentiellement petit (O2) |
| **C-D** | la loi du piquet : c_n/ρ² (XVI § 6) et c_n/d² (XXIV § 4, XXV § 1.4) | D = 1/d² contre 1/ρ², ρ² = d² + g² + … | même terme au premier ordre en D | le « … » de XVI § 6 cache l'ordre d⁻⁴ ; XXV § 1.4 le donne en 2D (−16/25515) et en 3D (−1/768) |
| **C-E** | le triangle de Thalès P Q P′ de XXIV § 5 et celui de `revision_001.py` § 1 | (PQ, QP′) = (c_K, d_K), d_K² + c_K² = 4, K − 1 = 1/x₀ | exactement | aucune |
| **C-F** | le cône à sommet imaginaire de XIX § 6 (r = θ·\|z + i z_R\|) et la chèvre infinie (ρ = \|d + i\|) | z_R = 1, w₀ = θ = 1 | exactement (R : `bases_objets.md` § 4) | en dimension finie, ρ² = d² + g_n² a un col g_n < 1 : fiche F5 (ma lecture) |
| **C-G** | la part de la clôture (XX § 2) et la fiche 010 | 2α_n/360° avec cos α_n = x₀ | exactement | la fiche généralise à tout anneau (§ 4.1) |
| **C-H** | l'angle entre deux fiches du simplexe de classification et l'angle de la chèvre | cos = −1/(K − 1) = −x₀, donc π − α_n = β | exactement ; déjà dans XXVII § 8 | aucune |

### 5.3 Les obstructions et les trous qu'elles désignent

| n° | ce qui ne se recolle pas | le trou | où chercher |
|---|---|---|---|
| **A** | la corde et le polygone, à l'ordre 4 (K1/T3) ; la série divergente et la série entière | un partenaire pour l'asymétrie de la coquille : un diaphragme à rayon distribué (pupille apodisée ou défocalisée) | `scripts/centre_venn.py` section 6 (défocalisation) ; XXVIII § 2.5. Test à écrire : moyenner la lumière du polygone sur un rayon ρ = e^(−E/n), E exponentielle (ma lecture, non fait) |
| **B** | δ₂ ≈ δ₃ à 10⁻⁵ (VI § 3 bis, XVI § 2, XXIV § 4) : les courbes μ(2 ; d) et μ(3 ; d) se coupent en d* = 0,995183, à 1,05·10⁻⁴ de 1 − δ = 0,995288 (A) | pourquoi le croisement est si près du piquet déplacé ; la bosse n'explique pas cette précision | variation du paramètre d (A, fait) ; fiche F7 |
| **C** | la chèvre et les réseaux records : le trou le plus profond est à √2 fois le rayon en dimension 3, 8 et 24 (D₃, E₈, Leech), mais ρ_n < √2 pour tout n fini : √2 − ρ_n = 0,1857 ; 0,0794 ; 0,0283 (A) | un lien démontré entre empilements et chèvre (XX § 5 : « je ne sais pas ») | Conway–Parker–Sloane 1982 ; Viazovska 2017 ; Cohn–Kumar–Miller–Radchenko–Viazovska 2017 (§ 6.3) |
| **D** | la loi des grands ordres : dérivée, pas démontrée | la résurgence : la série et sa somme de Borel diffèrent d'un terme en 2^(−n/2) | Boyd 1999 ; Bender–Orszag ; Flajolet–Sedgewick (§ 6.3) |
| **E** | la preuve par les moments : n ≥ 100 pour la borne, n ≥ 4 pour c_n | 4 ≤ n < 100 vérifié, non démontré ; E[ρ⁻³] infini pour n ≤ 3 | XXV § 1.4 (2D et 3D par la lentille) |
| **F** | l'unité du grain : plan (n ≈ 1/ε), aire (2/ε), angle (1/ε), cran (1,44/ε) | le calcul ne choisit pas ; le modèle physique le fait | XXIV § 5 : « compter les dimensions autrement, au même grain » |

---

## 6. Les trous

### 6.1 Les trous du recueil : neuf fiches nouvelles proposées

Les parties I à XXV n'ont aucune fiche à elles (plan, § 6.1). J'ai cherché « au passage », « curieusement », « fait amusant » et « coïncidence » dans les documents des parties I à XXV : « au passage » donne trois endroits (II § 9, IV « En bref », XXV § 1.4), « curieusement » et « fait amusant » aucun, « coïncidence » dix fichiers (README, lignes d'index seulement, puis II, III, IV, V, VI, XIII, XV, XXII, XXIII). Les fiches ci-dessous viennent de ces passages et de la lecture des maillons. Avant d'écrire « nouveau », j'ai cherché dans les parties précédentes (CLAUDE.md § 6 bis) : deux idées que j'avais ont été abandonnées parce qu'elles y étaient déjà (l'angle d'Ullisch proche de l'angle du tétraèdre est dans XXVII § 8 ; les maxima de μ et de c_n, 2,4236 et 2,5917, sont dans XVI § 2).

Les trois que je jugerais les plus utiles : **F1** (une structure nouvelle, démontrée), **F2** (le résultat central de XXV, sans fiche) et **F3** (une erreur de donnée qui se propage). **F4** et **F5** visent les dimensions vides D5 et D8 (plan, § 6.1).

#### F1 — Le « −2 » de la coquille est le nombre de dérangements de 3 : E[(1 − E)^j] = (−1)^j·!j

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact (démontré en deux lignes ; vérifié exactement pour j = 0 à 12, A) |
| partie | XXIV (et I) |
| document | `tiers-dimension.md` § 1 (« Ordre 2 ») ; `README.md` § 5.4 (l'esquisse) |
| script | `scripts/tiers_dimension.py`, section 1 (`skew`, l'intégrale de (1 − E)³e^(−E)) |
| données | `resultats/tiers_dimension.md` § 1 et § 2 |
| image | `figures/y1_tiers_dimension.png`, panneau a |
| dimension | D1 ; D7 |
| test | variation du paramètre : j = 0 à 12, exact ; preuve : E[(1 − E)^j] = Σᵢ C(j, i)(−1)ⁱ i! = (−1)^j Σₖ (−1)ᵏ j!/k! = (−1)^j·!j |

- **Contexte.** XXIV § 1 écrit E[(1 − E)³] = −2 pour « l'asymétrie de la loi exponentielle », sans nommer le nombre.
- **Observation.** Pour E exponentielle de moyenne 1, les moments de 1 − E valent 1, 0, 1, −2, 9, −44, 265, −1854 : ce sont (−1)^j fois les nombres de dérangements !j (OEIS A000166). C'est la représentation intégrale classique !j = ∫₀^∞ (x − 1)^j e^(−x) dx. Les coefficients de tête de E[τ³], E[τ⁵] et E[τ⁷] sont −2, −44 et −1854, soit −!3, −!5 et −!7 (A). Le 2/3 de la corde devient « 2 (double produit) × 1/6 (équateur) × !3 (coquille) ».
- **Pistes.** (1) !j se calcule par inclusion–exclusion, le procédé de la moitié de Kakeya fini (K4) et de la correction de Bonferroni (fiche 012) : à noter, sans plus. (2) !j ≈ j!/e a la croissance factorielle des μ_j ; mais le taux géométrique A = 2/ln 2 n'est pas lié à e : à tester, pas à croire.

#### F2 — La chèvre plane est contenue dans la série de la chèvre infinie

| champ | valeur |
|---|---|
| type | Analogie |
| statut | structure (le mécanisme est connu, la sommation de Borel ; la loi de l'écart reste à écrire) |
| partie | XXV (et XX) |
| document | `tranche-aiguilles.md` § 1.2 ; `sphere-faisceaux.md` § 1 |
| script | `scripts/tranche_aiguilles.py`, section 1 (`forme_laplace`, `borel_pade`) |
| données | `resultats/tranche_aiguilles.md` § 1 |
| image | `figures/z1_ouverts.png`, panneau c |
| dimension | D1 |
| test | variation du paramètre : le nombre de coefficients. 39 coefficients : 6·10⁻¹⁰ en n = 2 (R). coefficients jusqu'à 1/n¹² (Padé [5/6]) : 5,6·10⁻⁵ en n = 2 et 1,2·10⁻³ en n = 1 (A) |

- **Contexte.** XX § 1 : « deux chèvres au même endroit, séparées par une infinité de dimensions ».
- **Observation.** La série en 1/n de la dimension infinie (√2), resommée, redonne la corde d'Ullisch : 1,342 651 673 575 pour 1,342 651 674 183 (r₂²). Même la dimension 1 (r = 1) revient à 9·10⁻⁷. Le même procédé (une intégrale de Laplace ou de contour) décrit les deux bouts.
- **Pistes.** La loi de l'écart en fonction du nombre de coefficients ; le terme en 2^(−n/2) que la sommation ne voit pas (O2).

#### F3 — Le « 0,6668 » est du bruit de double précision, pas une valeur

| champ | valeur |
|---|---|
| type | Causalité |
| statut | exact (refait en 70 chiffres) |
| partie | XXIII (et XXII) |
| document | `lentilles-boules-grain.md` § 1 ; `carre-neuf-points.md` § 1 |
| script | `scripts/lentilles_boules_grain.py`, section 1 (l'assertion a une tolérance de 0,01) ; `scripts/carre_neuf_points.py`, section 1 |
| données | `resultats/lentilles_boules_grain.md` § 1 et § 3 ; `resultats/carre_neuf_points.md` § 1 |
| image | — |
| dimension | D7 ; D3 |
| test | intervention : refaire le calcul en 70 chiffres, sans rien changer d'autre. n²μ_n = 0,66660134 (10⁵), 0,66666013 (10⁶), 0,66666601 (10⁷) ; la série à quatre termes donne les mêmes valeurs à 11 chiffres (A) |

- **Contexte.** XXIII § 1 recontrôle le terme 2/(3n²) et écrit : « 0,6666 et 0,6668 en 10⁵ et 10⁶ ».
- **Observation.** μ_n = r_n² − 2n/(n + 1) est la différence de deux nombres proches de 2. En double précision, l'erreur absolue est ≈ 2·10⁻¹⁶ ; multipliée par n² = 10¹², elle fait 2·10⁻⁴ : c'est l'écart entre 0,6668 et 0,66666. Le tableau écrit aussi 0,6661 en 10⁷, et le § 3 donne μ = 6,668·10⁻¹³ et 6,661·10⁻¹⁵ (vraies valeurs 6,667·10⁻¹³ et 6,667·10⁻¹⁵). Le texte conclut que « la limite 2/3 est atteinte à 10⁻⁴ près » ; la vraie distance est 6,5·10⁻⁶ en 10⁶.
- **Pistes.** Même famille que la fiche 007 (une valeur de départ fausse qui se propage). Le test du script ne voit pas l'artefact : sa tolérance (0,01, ligne 102) est 50 fois plus large que lui (2·10⁻⁴).

#### F4 — L'aiguille qui se retourne passe le bord de chaque chèvre : cos α_n = x₀, et 39,34 % = 2α₂/360°

| champ | valeur |
|---|---|
| type | Analogie |
| statut | exact (XXV § 1.5, par Euclide) |
| partie | XXV (et XXI) |
| document | `tranche-aiguilles.md` § 1.5 ; `vingt-quatre-miroir.md` § 5 |
| script | `scripts/tranche_aiguilles.py`, section 4 ; `scripts/vingt_quatre_miroir.py`, section 4 |
| données | `resultats/tranche_aiguilles.md` § 4 ; `resultats/vingt_quatre_miroir.md` § 4 |
| image | `figures/v2_racine_sept.png`, panneau d |
| dimension | D5 ; D1 |
| test | précision (cordes certifiées) ; variation de n : α_n = 70,81° (n = 2) à 89,43° (n = 100) (R : `tranche_aiguilles.md` § 4) |

- **Contexte.** XXI § 5 fait tourner l'aiguille de e₃ vers e₂ avec le piquet en e₃ ; XXV § 1.5 relit le croisement.
- **Observation.** Un seul nombre, x₀, a quatre lectures : le plan de la lentille (XXIII § 2) ; le cosinus de l'angle au centre de l'arc brouté (la fiche 010 : 2α₂/360° = 39,34 %) ; le défaut d'aire divisé par 2R (Euclide : 2R² − r² = 2R·x₀, XXIV § 5) ; et l'angle qui reste avant le croisement de l'aiguille, arcsin x₀ ≈ 1/(n + 4/3) radian. La fiche 010 et le croisement de XXI sont deux lectures du même cosinus. D5 n'a aucune fiche principale.
- **Pistes.** Un grain en angle (1/ε) donne n = 1/ε − 4/3, comme le plan ; le facteur 2 n'apparaît que si l'on mesure une aire (XXV § 1.5).

#### F5 — Le col de la chèvre de dimension n est g_n = √((n − 1)/(n + 1)) : un faisceau dont la distance de Rayleigh est g_n

| champ | valeur |
|---|---|
| type | Analogie |
| statut | à tester (ma lecture) |
| partie | XIX (et XVI, XXIV) |
| document | `bases-objets.md` § 6 ; `menisque-projection.md` § 2 et § 5 ; `tiers-dimension.md` § 4 |
| script | `scripts/bases_objets.py`, section 4 ; `scripts/menisque_projection.py`, sections 2 et 5 |
| données | `resultats/bases_objets.md` § 4 ; `resultats/menisque_projection.md` § 2 et § 5 |
| image | `figures/t2_trait_cone_thales.png`, panneau c ; `figures/p2_menisque_projection.png`, panneau a |
| dimension | D8 ; D1 |
| test | variation du paramètre n ; comparer ρ² − d² − g_n² à la correction c_n/d² de XXIV § 4 (R) |

- **Contexte.** XIX § 6 : la chèvre de dimension infinie est un faisceau gaussien de col w₀ = 1 et de pente θ = 1, ρ = |d + i| ; au piquet (d = 1) elle est à la distance de Rayleigh z_R = 1. XX § 1 corrige : la chèvre *plane* n'y est pas.
- **Observation (A).** En dimension n, XVI § 2 et XXIV § 4 donnent ρ² = d² + g_n² + c_n/d² + …, avec g_n² = (n − 1)/(n + 1) = E[ρ]/E[ρ⁻¹] (le rayon quadratique de l'ombre du pré). C'est une hyperbole de col g_n et de pente 1 : z_R = g_n. Au piquet, d/z_R = 1/g_n = 1,732 (n = 2), 1,414 (n = 3), puis 1 à l'infini. La phase de Gouy arctan(1/g_n) vaut 60° (n = 2), 54,74° (n = 3, l'« angle magique » du cube, XXVI § 3.2) et 45° (n = ∞). La chèvre plane est donc à 1,73 distance de Rayleigh, ce qui s'accorde avec la correction de XX § 1. Valable pour d ≫ 1/√n seulement (XXIV § 4).
- **Pistes.** Le terme c_n/d² serait la correction non paraxiale ; à comparer au faisceau exact de Deschamps (source ponctuelle complexe). D8 n'a aucune fiche principale.

#### F6 — Les seuils entiers de IV § 4 ne tiennent pas en dimension réelle

| champ | valeur |
|---|---|
| type | Coïncidence |
| statut | hasard (testé en dimension réelle, A) |
| partie | IV |
| document | `trois-solides.md` § 2 et § 4 |
| script | `scripts/trois_solides.py`, section 4 |
| données | `resultats/trois_solides.md` § 4 |
| image | `figures/d1_trois_solides.png`, panneau c |
| dimension | D1 ; D7 |
| test | variation du paramètre : n réel (A) |

- **Contexte.** IV § 4 : « la corde du cylindre dépasse R entre 5 et 6 : c'est le seuil du pic du volume, la même inégalité » ; « la corde de l'anneau dépasse R entre 7 et 8, au même seuil que le pic de l'aire : une coïncidence de seuils entiers ».
- **Observation (A).** J'ai refait l'anneau (cylindre moins cône, piquet en O) : mon modèle redonne les cordes du tableau de IV à quatre chiffres (0,9859 en n = 6 ; 0,9981 en 7 ; 1,0079 en 8 ; 1,0514 en 15). Pour n réel, la corde du cylindre vaut R en n = 5,7635 (W_n = 1), alors que le volume de la boule est maximal en n = 5,2569. La corde de l'anneau vaut R en n = 7,1976 (∫ de π/4 à π/2 de sin^(n−2) = ½), alors que l'aire de la sphère est maximale en n = 7,2569. Pour le cylindre, l'égalité est celle d'un *pas* (V_n < V_(n−1) dès n = 6) : le seuil de pas est le pic décalé d'un demi-pas (5,2569 + ½ = 5,7569 contre 5,7635). Pour l'anneau, ce n'est pas le même décalage (7,7569 attendu) : les deux seuils sont à 0,06 l'un de l'autre, soit 0,8 %, sans être égaux.
- **Pistes.** C'est le test « coïncidence d'entiers → répliquer en faisant varier le paramètre » de CLAUDE.md § 10. Le verdict est « hasard » pour l'anneau, « pas d'égalité exacte » pour le cylindre.

#### F7 — δ₂ ≈ δ₃ à 10⁻⁵ : une proximité, nommée trois fois, jamais expliquée

| champ | valeur |
|---|---|
| type | Coïncidence ; Corrélation |
| statut | ouvert |
| partie | VI (et XVI, XXIV) |
| document | `zone-confusion.md` § 3 et § 3 bis ; `menisque-projection.md` § 2 ; `tiers-dimension.md` § 4 |
| script | `scripts/zone_confusion.py`, section 3 bis ; `scripts/menisque_projection.py`, section 2 ; `scripts/tiers_dimension.py`, section 4 |
| données | `resultats/zone_confusion.md` § 3 bis ; `resultats/menisque_projection.md` § 2 ; `resultats/tiers_dimension.md` § 4 |
| image | `figures/f2_dimension_reelle.png`, panneau b |
| dimension | D1 ; D7 |
| test | variation du paramètre d (A) : les deux courbes μ(2 ; d) et μ(3 ; d) se coupent en d* = 0,995183 |

- **Contexte.** VI § 3 : le déplacement qui rattrape l'écart vaut δ₂ = 0,0047121107 et δ₃ = 0,0047121571 (R : `tiers_dimension.md` § 4), soit un écart relatif de 9,8·10⁻⁶. VI § 3 bis : la bosse du déplacement (maximum en n = 2,42) explique que les valeurs en 2 et en 3 soient proches « à quelques pour cent », pas à 10⁻⁵ ; la courbe repasse au niveau de δ₂ en n* = 3,0000853, « un hasard tant qu'on ne trouve pas de raison ».
- **Observation.** (1) XVI § 2 écrit que le ménisque en carrés (0,009318 en 2D et 0,009322 en 3D) est « la même proximité » que δ. Elle ne l'est pas : 4,5·10⁻⁴ contre 9,8·10⁻⁶, et 2δ/μ vaut 1,011363 et 1,010923 (R : `tiers_dimension.md` § 4). La proximité de δ est donc environ 46 fois plus étroite que celle de μ. (2) (A) δ_n est défini par μ(n ; 1 − δ) = 2δ − δ² = 1 − d². Les deux courbes μ(2 ; d) et μ(3 ; d), avec μ = ρ_n(d)² − d² − g_n², se coupent en d* = 0,995183, à 1,05·10⁻⁴ de 1 − δ = 0,995288 (1 − δ₂ = 0,9952878893, 1 − δ₃ = 0,9952878429). La proximité de δ est donc celle d'un croisement tombé tout près de la droite 1 − d². Pourquoi il y tombe : ouvert.
- **Pistes.** Faire varier la paire (n, n + 1) : les croisements de μ(n ; d) et μ(n + 1 ; d) tombent-ils près de 1 − d² pour d'autres n ? (non fait).

#### F8 — Les polygones circonscrits à 4 et à 8 côtés ont la même corde (1,165644)

| champ | valeur |
|---|---|
| type | Fait amusant |
| statut | exact |
| partie | II |
| document | `archimede.md` § 9 |
| script | `scripts/calculs_archimede.py`, section 9 (qui appelle `corde_moitie_polygone` de `scripts/archimede.py`) |
| données | `resultats/archimede.md` § 9 |
| image | `figures/b9_polygones_polyedres.png`, panneau a |
| dimension | D1 ; D6 |
| test | variation du paramètre : N = 12 et 24 ne coïncident pas (1,16327773 et 1,15946948, R) ; N = 8 et 16 non plus (1,16564432 et 1,1610165, A) |

- **Contexte.** II § 9 : « une coïncidence exacte au passage : les polygones circonscrits à 4 et à 8 côtés donnent la même corde ». L'explication est dans le texte, mais pas dans le recueil.
- **Observation (A).** Le piquet est au milieu d'un côté. Les coins que l'on retire au carré pour faire l'octogone sont des petits triangles. Les deux triangles du côté du piquet sont entièrement dans le disque de corde r (leur point le plus éloigné du piquet est à 1,1589, moins que r = 1,1656 : marge 0,0067). Les deux autres sont entièrement dehors (leur point le plus proche est à 1,7321). Le carré et l'octogone perdent donc la même moitié de ces coins, et gardent la même corde. La coïncidence est exacte, mais fragile : elle tient de 4 à 8 côtés, non de 8 à 16.
- **Pistes.** Chercher d'autres paires (N, 2N) : aucune dans le tableau de II § 9 (N = 3, 4, 6, 8, 12, 24, 48, 96, 192).

#### F9 — Les facteurs 2 des polynômes de la chèvre comptent les retenues de la base 2 (Kummer)

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact (démontré en VII § 7) |
| partie | VII |
| document | `nombres-polynomes.md` § 5 à § 7 |
| script | `scripts/polynomes.py`, sections 3 et 5 |
| données | `resultats/polynomes.md` § 4 et § 5 |
| image | `figures/g1_polynomes_retenues.png` |
| dimension | D2 ; D1 |
| test | variation du paramètre : toutes les dimensions impaires de 3 à 31, l'exposant jusqu'à 801 (R : VII § 5) |

- **Observation.** Le nombre de facteurs 2 du dénominateur de κ_n (n = 6, 12, 24 : 2⁴, 2¹⁰, 2²²) est le nombre de retenues de m + m en binaire (Kummer, 1852). Le terme constant du polynôme impair de degré 2(n − 1) est ±2^e avec le même exposant (7D : 1024 ; 13D : 2²²).
- **Réserve.** Le dossier `bases` proposera sans doute la même fiche : à fusionner à la synthèse.

### 6.2 Les trous du corpus : erreurs et imprécisions trouvées

Je n'ai trouvé aucune erreur dans les chiffres de la chaîne principale : les coefficients μ₂ à μ₈, les cordes, N − n, c_n, les bosses, les troncatures optimales et le rapport de la loi des grands ordres sont reproduits (§ 3.1). Ce qui suit est périphérique.

| n° | où | ce qui est écrit | ce qui est vrai (A) | correction proposée |
|---:|---|---|---|---|
| 1 | `resultats/lentilles_boules_grain.md` § 1 (tableau) et § 3 (colonne μ) ; `lentilles-boules-grain.md` § 1 ; `resultats/carre_neuf_points.md` § 1 | n²·μ_n = 0,6666 puis 0,6668 en 10⁵ et 10⁶ (0,6661 en 10⁷) ; μ = 6,668·10⁻¹³ et 6,661·10⁻¹⁵ ; « jusqu'à 10⁶, la limite 2/3 est atteinte à 10⁻⁴ près » ; n(t_n − 1) = −1,33329 en 10⁶ | artefact de la double précision : 0,66660134 (10⁵), 0,66666013 (10⁶), 0,66666601 (10⁷) en 70 chiffres, égaux à la série à quatre termes à 11 chiffres ; μ = 6,667·10⁻¹³ et 6,667·10⁻¹⁵ ; n(t_n − 1) = −1,333329 (−4/3 + 64/(15n)) | recalculer en précision étendue (mpmath, 50 chiffres) ; resserrer l'assertion de la ligne 102 de `lentilles_boules_grain.py` ; fiche F3 |
| 2 | `resultats/lentilles_boules_grain.md` § 4 (en-tête) ; `figures/x1_lentilles_boules_grain.png`, panneau e (légende) | « la sphère de son équateur » | les nombres (44,76 ; 4 549 ; 4,55·10⁵) sont ceux de la **boule** (la tranche \|x₁\| < ε de la boule). Pour la sphère S^(n−1) ils seraient 46,76 et 4 551 (l'équateur a l'exposant (n − 3)/2, deux de moins) | écrire « la boule de son équateur », comme le fait le document |
| 3 | `resultats/resultats.md` § 2 contre `resultats/carre_neuf_points.md` § 1 | une colonne « angle α_n » vaut 54,594° en 2D ; l'autre, 70,812° | deux angles sous le même nom (§ 1.4) : l'angle au piquet et l'angle au centre | noter α_P l'angle au piquet |
| 4 | fiche 010 ; `centre-venn.md` § 4.3 | « 39,34 % de chaque anneau du bord » | vrai du seul cercle de bord (§ 4.1) ; `centre_venn.md` § 4 dit « du niveau 1 » | « … du cercle de bord » |
| 5 | `menisque-projection.md` § 2 | « le ménisque en carrés vaut presque la même chose en 2D et 3D (0,009318 ; 0,009322) : c'est la même proximité que δ » | 4,5·10⁻⁴ contre 9,8·10⁻⁶ ; 2δ/μ = 1,0114 et 1,0109 (R : `tiers_dimension.md` § 4) | « une proximité plus lâche : 4,5·10⁻⁴ contre 9,8·10⁻⁶ » (F7) |
| 6 | `README.md` § 9 ; `tiers-dimension.md`, `lentilles-boules-grain.md` et `menisque-projection.md` (leurs « Sources ») | « The College Mathematics Journal 15(2), 126–134 (1984) » | volume et pages justes ; le titre de la revue en 1984 était, d'après les notices vues par recherche web, *The Two-Year College Mathematics Journal* (renommée en 1985) : à vérifier | écrire « (Two-Year) College Mathematics Journal » |
| 7 | `recueil/revisions/plan-001.md` § 5.2.1 et § 7 ; JSON § 1.9 | la liste de l'agent `corde` | omet `carte-connexions.md` et `resultats/carte_connexions.md` (XXVII § 6, cité par les questions 2 et 4), `scripts/vingt_quatre_miroir.py` (XXI § 5, cité au § 1.1), `archimede.md` avec `calculs_archimede.py` (les polygones de T3), `carre-ptolemee.md` et `centre-venn.md` (la fiche 010), `bases-objets.md` (XIX § 6). Le JSON omet les parties II, X, XVII, XIX et XXVII | § 8 |

Deux précisions de lecture, qui ne sont pas des erreurs :
- **T3 (plan § 3.2 et § 4)** : « obstruction dès l'ordre 3 » est vrai sans décalage ; avec un décalage libre, c'est l'ordre 4 (§ 5.1). `resultats/revision_001.md` § 4.4 le dit déjà.
- **XVI § 6 et XXIV § 4** : « c_n/ρ² » et « c_n/d² » sont le même terme au premier ordre en 1/d², et diffèrent à l'ordre d⁻⁴ (C-D).

**Ce qui manque, sans être faux.**
- Aucun script ne prouve la monotonie de N − n en dimension réelle (O3).
- Le tableau des coefficients de `tiers_dimension.md` § 2 s'arrête à j = 12 ; XXIV § 2 dit en avoir calculé 14 exacts et 30 à 170 chiffres.
- Le script `lentilles_boules_grain.py` calcule la corde en double précision jusqu'à n = 10⁷ ; `tiers_dimension.py` sait faire mieux (`corde2_hp`, 60 chiffres) : la correction de la fiche F3 est à portée de main.

### 6.3 Les trous des données publiées (question 7)

**Ce que j'ai pu atteindre.** WebFetch a échoué (hôte introuvable). Seules des recherches web ont répondu, avec des titres, des extraits et des liens ; je n'ai lu aucun des trois articles demandés.

**Le développement 2n/(n + 1) + 2/(3n²) − 98/(15n³) + … est-il publié ?**
- *Non confirmé.* Aucune notice vue ne mentionne un terme en 1/n² : Fraser (1984) donne l'extension à n dimensions et la limite √2 ; Meyerson (1984) corrige une faille de son argument, et la limite reste √2 (README § 9 ; Wikipédia, « Goat grazing problem », dans les extraits de recherche) ; Jameson et Jameson (2017, « Goats and birds ») donnent la quartique en dimension 3, 3r⁴ − 8r³ + 8 = 0 (README § 9). Je ne sais pas si le terme en 2/(3n²) est dans Fraser : la partie I l'appelle « établi ici » (§ 5.4).
- *Ce que j'ai vérifié par ailleurs (P, A).* Le r₂ du corpus, 1,158 728 473 018 12…, est celui de l'OEIS A133731, de MathWorld (« Goat Problem ») et de MathPages (kmath074). Le polynôme de la dimension 3 et la racine 1,22854486… se retrouvent par la formule d'intersection de deux boules (lentille de volume π(8r³ − 3r⁴)/12 pour R = 1, d = 1) : 8r³ − 3r⁴ = 8 donne 3r⁴ − 8r³ + 8 = 0 (A).
- *À faire.* Lire Fraser (1984) et Meyerson (1984), puis chercher « 2/(3n²) » dans les articles de Math. Gazette sur la chèvre. Si le terme n'y est pas, le développement est une donnée que le corpus apporte (plan § 6.2 h).

**Les chaînes corrigées de la littérature.**
- Fraser, « A Tale of Two Goats » (1982) → Fraser, « The Grazing Goat in n Dimensions » (1984), limite √2 → Meyerson (1984), faille corrigée → Jameson et Jameson (2017), la quartique 3D.
- Ullisch (2020), forme close avec le contour |z − 3π/8| = π/4 → erratum (2023), contour |z − 3π/4| = π/4 (README § 3.1 et § 9 ; l'erratum, doi:10.1007/s00283-023-10299-x, n'a pas été lu). *Mon contrôle (A)* : les deux cercles contiennent exactement un zéro de f(z) = sin z − z cos z − π/2 (principe de l'argument : 1,0000), β = 1,905 695 729 309 883 894 9 ; les autres zéros (4,0903 ; 7,9264 ; −0,7057 ± 1,4268i) sont dehors. Le contour de 2020 converge même plus vite (erreur 1,4·10⁻¹⁵ contre 1,2·10⁻¹¹ avec 32 points). Le motif de l'erratum n'est donc pas la vitesse ; je ne sais pas ce qu'il corrige.
- Dans le corpus : V → VI (« quasi-coïncidence » → ce n'est pas un hasard), « 0,00009 » → 0,0000853 (VI § 3 ter), « la chèvre classique est à la distance de Rayleigh » → c'est la chèvre infinie (XX § 1), XXII → XXIII (trois phrases), VII → VIII (trois mécanismes).

**Les pistes de données** (au format du plan § 6.2) :

| piste | ce que le corpus observe | ce qui manque dans les données publiées | où chercher | références |
|---|---|---|---|---|
| h1 | la série de la corde, ses coefficients rationnels, sa divergence en A = 2/ln 2 | un développement en 1/n de la corde publié, et une sommation de Borel pour l'équation de médiane | Fraser 1984, Meyerson 1984 ; articles de la Math. Gazette sur la chèvre | voir ci-dessous (à vérifier) |
| h2 | la loi des grands ordres (XXV § 1.1) | la transsérie : le terme en 2^(−n/2) qui complète la série | théorie de la résurgence ; sommation de Borel pour les intégrales de Laplace à singularité en racine carrée | Boyd 1999 ; Bender–Orszag 1978 ; Flajolet–Sedgewick 2009 |
| h3 | la chèvre n'atteint √2 qu'à l'infini ; les réseaux de Leech, E₈ et D₃ y sont en 24, 8 et 3 | un lien démontré entre empilements record et chèvre | rayon de recouvrement : Conway–Parker–Sloane 1982 ; empilements : Viazovska 2017, Cohn–Kumar–Miller–Radchenko–Viazovska 2017, Hales 2005 | voir ci-dessous |
| h4 | N − n monte de 0 à 1/3 | la dimension du simplexe de même corde : aucune publication connue (à chercher) | — | — |

**Références.** Celles du corpus sont dans README § 9. Mon classement (« sûre » : je l'ai vue ou je la connais ; « à vérifier » : un détail n'est pas confirmé) :

*Sûres.*
- I. Ullisch, « A Closed-Form Solution to the Geometric Goat Problem », *The Mathematical Intelligencer* 42(3), 12–16 (2020), doi:10.1007/s00283-020-09966-0.
- M. Fraser, « A Tale of Two Goats », *Mathematics Magazine* 55(4), 221–227 (1982).
- M. Fraser, « The Grazing Goat in n Dimensions », *(Two-Year) College Mathematics Journal* 15(2), 126–134 (1984). Le doi:10.2307/2686517 du README n'est pas confirmé.
- M. D. Meyerson, « Return of the Grazing Goat in n Dimensions », *College Mathematics Journal* 15(5), 430–432 (1984), JSTOR 2686558.
- G. Jameson, N. Jameson, « Goats and birds », *The Mathematical Gazette* 101(551), 2017 (existence, auteurs, titre, revue, année confirmés ; pages 296–300 et doi du README non relus).
- M. E. Hoffman, « The Bull and the Silo: An Application of Curvature », *American Mathematical Monthly* 105(1), 55–58 (1998).
- OEIS A133731 (développement décimal de la corde 2D, 1,1587284730181215178…) ; MathWorld, « Goat Problem » ; MathPages (page kmath074) ; Wikipédia, « Goat grazing problem ».
- OEIS A000166 (nombres de dérangements) ; la représentation !n = ∫₀^∞ (x − 1)ⁿ e^(−x) dx est classique.
- E. E. Kummer, « Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen », *J. reine angew. Math.* 44 (1852) : le théorème sur les puissances d'un premier dans un coefficient binomial.
- J. H. Conway, R. A. Parker, N. J. A. Sloane, « The covering radius of the Leech lattice », *Proc. Roy. Soc. London A* 380 (1982) 261–290.
- M. Viazovska, « The sphere packing problem in dimension 8 », *Annals of Math.* 185 (2017) ; H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, « The sphere packing problem in dimension 24 », *Annals of Math.* 185 (2017) ; T. Hales, « A proof of the Kepler conjecture », *Annals of Math.* 162 (2005).
- J. P. Boyd, « The Devil's Invention: Asymptotic, Superasymptotic and Hyperasymptotic Series », *Acta Applicandae Mathematicae* 56 (1999) 1–98 ; C. M. Bender, S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers*, McGraw-Hill (1978) ; P. Flajolet, R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009) ; G. A. Baker, P. Graves-Morris, *Padé Approximants*, 2e éd., Cambridge University Press (1996).

*À vérifier.*
- L'erratum d'Ullisch, doi:10.1007/s00283-023-10299-x (Math. Intelligencer, 2023 ou 2024 : contenu et pages non lus).
- Les articles de Math. Gazette ou Math. Magazine sur la chèvre vus seulement par leurs titres : « Tethering in pastures new » (D. Mahony, 2018), « The Grazing Goat and Spherical Curiosities » (*Math. Magazine* 94(5), 2021), « Venn diagrams and grazing goats » (auteur et volume inconnus). Je ne sais pas s'ils parlent du développement en 1/n.
- Brennan (prénom non vérifié), « The tethered goat — a calculus », *Irish Math. Soc. Bulletin* 40 : trouvé par son adresse (`maths.tcd.ie/pub/ims/bull40/brennan.pdf`), année et contenu non vérifiés.
- arXiv:2304.00981, « On the Closed-Form Solution to the Interior Goat Problem in One Dimension » : titre seul ; je ne sais pas à quel problème en dimension 1 il répond (en dimension 1 la corde vaut R dans notre modèle).

---

## 7. Le code minimal du test T3 (et la partie corde de T7)

### 7.1 Ce qui existe déjà, et ce que j'ajoute

L'agent de session a écrit, après mon lancement, le § 4.4 de `scripts/revision_001.py` (T3 et K10) et le § 4.5 (T7). Son T3 compare la lumière du polygone inscrit, avec N = π(n + s) et cinq coefficients μ_j tapés à la main, et trouve s = 49/10 et l'ordre 4 faux (47,89 contre 56,82). Mon code donne le même résultat et ajoute :
- les coefficients μ_j (j ≤ 8) *calculés* par la méthode de XXIV § 1, en fractions exactes, sans aucun nombre recopié ; les quatre premiers sont vérifiés contre `resultats/tiers_dimension.md` § 2 par des `assert` ;
- les trois séries du plan (inscrit, circonscrit, cordes de K10), chacune avec son facteur a fixé par l'ordre 2 ;
- cinq décalages s (0, 1/3, 1, 4/3 et le s* qui recolle l'ordre 3), avec l'écart exact ordre par ordre ;
- la comparaison des rapports μ_(j+1)/μ_j avec ceux du sinus (point 3 du plan) ;
- le contrôle de K10 : W_centre/W_reste = √(n/(4π)) (point 4 du plan), et les deux seuils.

À insérer dans `scripts/revision_001.py` après le § 4.4 : il remplace le dictionnaire `MU` tapé à la main par `mu_exacts(8)`. Durée : environ 6 s avec sympy (déjà utilisé par le § 4.4).

### 7.2 Ce que j'ai obtenu en l'exécutant (A, hors dépôt)

- s* = −μ₃/(2μ₂) = 49/10, le même pour les trois séries (les séries du polygone sont paires).
- Écarts à s* = 49/10, aux ordres 2 à 6 : inscrit [0, 0, 9379/1050, −20402209/70875, 5378444783/891000] ; circonscrit [0, 0, 2893/350, −19476109/70875, 36648164081/6237000] ; cordes [0, 0, 26737/3150, −19784809/70875, 5283259583/891000].
- Pour s = 0, 1/3, 1 et 4/3, l'écart de l'ordre 3 vaut −98/15, −274/45, −26/5 et −214/45, pour les trois séries.
- Rapports μ_(j+1)/μ_j, j = 2 à 7 : −9,80 ; −8,70 ; −10,54 ; −13,23 ; −16,10 ; −18,98. Rapports du polygone inscrit : −0,200 ; −0,095 ; −0,056 ; −0,036.
- Seuils du centre du Venn : 12,566 (cercle) et 12,824 (segments).

**Verdict (calculé)** : le même exposant et le même 1/6, pas le même ménisque ; recollement aux ordres 2 et 3, obstruction à l'ordre 4 (§ 5.1).

### 7.3 Le code de T3

```python
"""
T3 : le ménisque x²/6, ordre par ordre (K1, K10).  Code minimal pour scripts/revision_001.py (≈ 6 s).

Ce que le test compare : la série de la chèvre, μ(n) = r_n² − 2n/(n + 1) = Σ_j μ_j / n^j  (partie XXIV),
avec les séries de lumière du polygone (inscrit, circonscrit) et du centre du Venn joint par des cordes (K10).
Il cherche le changement de variable x = a·e/(1 + s·e), e = 1/n, qui recolle les deux séries ordre par ordre :
le facteur a est fixé par l'ordre 2, le décalage s par l'ordre 3 ; l'ordre 4 est alors le premier vrai test.
"""
from fractions import Fraction as Fr
from math import comb, factorial
import sympy as sp

# ---------------------------------------------------------------------------
# (a) Les coefficients exacts de la chèvre (méthode de la partie XXIV, § 1 ; aucun script du dépôt n'est lancé).
#     Condition de médiane :  Σ_i (−1)^i C(k, i)/(2i + 1) · E[τ^(2i+1)] = 0,   k = (n − 3)/2,
#     τ = (ρ² + 1 − m)/(2ρ),  E[ρ^a] = n/(n + a)  (exact : E = −n ln ρ est exponentielle),  m = r².
#     Séries de Laurent en e = 1/n à coefficients rationnels exacts.
# ---------------------------------------------------------------------------
TOP = 40


class S:
    def __init__(self, d=None):
        self.d = {p: Fr(c) for p, c in (d or {}).items() if c != 0 and p <= TOP}

    def __add__(self, o):
        o = o if isinstance(o, S) else S({0: o})
        d = dict(self.d)
        for p, c in o.d.items():
            d[p] = d.get(p, 0) + c
        return S(d)
    __radd__ = __add__

    def __neg__(self):
        return S({p: -c for p, c in self.d.items()})

    def __sub__(self, o):
        return self + (-(o if isinstance(o, S) else S({0: o})))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, S):
            return S({p: c * Fr(o) for p, c in self.d.items()})
        d = {}
        for p, c in self.d.items():
            for q, c2 in o.d.items():
                if p + q <= TOP:
                    d[p + q] = d.get(p + q, 0) + c * c2
        return S(d)
    __rmul__ = __mul__

    def coeff(self, p):
        return self.d.get(p, Fr(0))


def geom(a):                                   # n/(n + a) = 1/(1 + a·e)
    return S({k: Fr((-a) ** k) for k in range(TOP + 1)})


K = S({-1: Fr(1, 2), 0: Fr(-3, 2)})            # k = (1 − 3e)/(2e)


def residu(mu, J):
    m = S({k: Fr(2 * (-1) ** k) for k in range(TOP + 1)}) + mu        # m = 2n/(n + 1) + μ
    omm, tot = 1 - m, S()
    for i in range(J + 1):
        p = 2 * i + 1
        ff = S({0: 1})
        for t in range(i):
            ff = ff * (K - t)
        ff = ff * Fr(1, factorial(i))
        Et, pw = S(), S({0: 1})
        for s_ in range(p + 1):
            Et = Et + comb(p, s_) * pw * geom(p - 2 * s_)
            pw = pw * omm
        tot = tot + ff * Et * Fr((-1) ** i, p * 2 ** p)
    return tot


def mu_exacts(jmax):
    mus = {}
    for j in range(2, jmax + 1):
        def mk(x):
            d = {i: mus[i] for i in range(2, j)}
            d[j] = Fr(x)
            return S(d)
        r0, r1 = residu(mk(0), jmax).coeff(j), residu(mk(1), jmax).coeff(j)
        mus[j] = -r0 / (r1 - r0)
    return mus


MU = mu_exacts(8)
# contrôle contre resultats/tiers_dimension.md, § 2 : 2/3, −98/15, 5966/105, −1698106/2835, …
assert MU[2] == Fr(2, 3) and MU[3] == Fr(-98, 15) and MU[4] == Fr(5966, 105) and MU[5] == Fr(-1698106, 2835)

# ---------------------------------------------------------------------------
# (b) Les séries de lumière du polygone et du centre du Venn (sympy), chacune dans sa variable y = π/N ou π/n.
# ---------------------------------------------------------------------------
y, e, s = sp.symbols('y e s')
SERIES = {
    "polygone inscrit : 1 − (N/2π)·sin(2π/N)": sp.series(1 - sp.sin(2 * y) / (2 * y), y, 0, 12).removeO(),
    "polygone circonscrit : N·tan(π/N)/π − 1": sp.series(sp.tan(y) / y - 1, y, 0, 12).removeO(),
    "K10, cordes : (π/n)/sin(π/n) − 1": sp.series(y / sp.sin(y) - 1, y, 0, 12).removeO(),
}
# (la fiche 003 est le circonscrit à 2N côtés : y = π/(2N), même série.)

# ---------------------------------------------------------------------------
# (c) Le recollement : y = a·e/(1 + s·e).  a² = μ_2/p_2 (ordre 2) ; s* = −μ_3/(2μ_2) (ordre 3, le même pour tout
#     polygone, car les séries du polygone sont paires) ; les ordres 4, 5, 6 sont les vrais tests.
# ---------------------------------------------------------------------------
mu_serie = sum(sp.Rational(MU[j].numerator, MU[j].denominator) * e ** j for j in MU)


def residus(p_serie, shift, ordres=(2, 3, 4, 5, 6)):
    p2 = p_serie.coeff(y, 2)
    a = sp.sqrt(sp.Rational(MU[2].numerator, MU[2].denominator) / p2)
    sub = p_serie.subs(y, a * e / (1 + shift * e))
    ecart = sp.series(mu_serie - sub, e, 0, 8).removeO()
    return a, [sp.simplify(sp.expand(ecart).coeff(e, j)) for j in ordres]


if __name__ == "__main__":
    s_etoile = -sp.Rational(MU[3].numerator, MU[3].denominator) / (2 * sp.Rational(MU[2].numerator, MU[2].denominator))
    print("s* =", s_etoile, "(= −μ_3/(2μ_2))")
    for nom, ser in SERIES.items():
        for sh in (0, sp.Rational(1, 3), 1, sp.Rational(4, 3), s_etoile):
            a, res = residus(ser, sh)
            print(f"{nom} | a = {a} | s = {sh} | écarts aux ordres 2..6 : {res}")
    # (d) la croissance des coefficients : le rapport μ_(j+1)/μ_j contre celui des séries du polygone
    print("μ_(j+1)/μ_j =", [float(MU[j + 1] / MU[j]) for j in range(2, 8)], "; attendu ≈ −(2/ln 2)·(j − 1/2) pour j ≥ 4 (parties XXIV et XXV)")
    # le sinus : coefficients de y^(2j) de 1 − sin(2y)/(2y), rapport de deux coefficients successifs
    ins = SERIES["polygone inscrit : 1 − (N/2π)·sin(2π/N)"]
    c_ins = [ins.coeff(y, 2 * j) for j in range(1, 6)]
    # (e) K10 (fiche 011) : W_centre/W_reste = sqrt(n/(4π)) ; seuil avec un cercle (4π) et avec des segments (π/arctan(1/4))
    nn = sp.symbols('n', positive=True)
    Wc, Wr = 2 / sp.pi * sp.sqrt(nn * (2 ** nn - 2)), 4 * sp.sqrt((2 ** nn - 2) / sp.pi)
    assert sp.simplify(Wc / Wr - sp.sqrt(nn / (4 * sp.pi))) == 0
    print("seuil du centre :", float(4 * sp.pi), "(cercle),", float(sp.pi / sp.atan(sp.Rational(1, 4))), "(segments)")
    print("polygone inscrit, rapports successifs :", [float(c_ins[i + 1] / c_ins[i]) for i in range(len(c_ins) - 1)],
          "; ils tendent vers 0 (série entière), contre une croissance en j pour la chèvre")
```

### 7.4 La partie corde de T7 (les deux 4/3)

À placer après le code de T3 (il en utilise `e`, `sp` et `mu_serie`). Durée : moins d'une seconde.

```python
"""
T7 (partie corde) : les deux 4/3.  À placer après le code de T3 (il utilise e, sp et mu_serie).
Ce que le test regarde : (a) 1/x0 = n + 4/3 − 112/(45n) + … (la série de la partie XXIV) ;
(b) V_(n+1)/V_n = W_(n+1) (partie III, § 4) : V_3/V_2 = 4/3, et la suite tend vers 0 ;
(c) l'identité N − n = (n + 1)·μ/(2·x0), qui donne 4/3 = 1 + lim n²μ/2.
"""
from math import gamma, pi

# (a) la série de 1/x0, à partir des coefficients exacts de la corde (e = 1/n)
r2 = 2 / (1 + e) + mu_serie                       # r² = 2n/(n + 1) + μ
x0 = 1 - r2 / 2
inv_x0 = sp.expand(sp.series(1 / x0, e, 0, 4).removeO())
coefs = [inv_x0.coeff(e, k) for k in (-1, 0, 1, 2, 3)]       # n, 1, 1/n, 1/n², 1/n³
print("1/x0 =", " + ".join(f"({c})·n^{-(k)}" for k, c in zip((-1, 0, 1, 2, 3), coefs)))
assert coefs[:3] == [1, sp.Rational(4, 3), sp.Rational(-112, 45)]        # partie XXIV, § 2

# (b) les rapports de volumes V_(n+1)/V_n
V = lambda n: pi ** (n / 2) / gamma(n / 2 + 1)
rapports = {n: V(n + 1) / V(n) for n in range(1, 13)}
assert abs(rapports[2] - 4 / 3) < 1e-12                                   # V_3/V_2 = 4/3
print("V_(n+1)/V_n :", {n: round(v, 4) for n, v in rapports.items()})

# (c) N − n = (n + 1)·μ/(2·x0), et 4/3 = 1 + (1/2)·lim n²μ
N_moins_n = sp.expand(sp.series(1 / x0 - 1 - 1 / e, e, 0, 3).removeO())
ident = sp.expand(sp.series((1 / e + 1) * mu_serie / (2 * x0), e, 0, 3).removeO())
assert sp.expand(N_moins_n - ident) == 0
print("N − n =", N_moins_n, " (1/3 − 112/(45n) + …)")
```

Sortie (A) : `1/x0 = (1)·n^1 + (4/3)·n^0 + (−112/45)·n^−1 + (3856/189)·n^−2 + (−150832/675)·n^−3` ; V₂/V₁ = 1,5708, V₃/V₂ = 1,3333, V₅/V₄ = 1,0667, V₁₃/V₁₂ = 0,682 (la suite tend vers 0) ; `N − n = 3856e²/189 − 112e/45 + 1/3`.

---

## 8. Les corrections au recouvrement (bloc JSON du § 1.9 du plan)

### 8.1 La proposition

```json
"corde-et-dimensions": {
  "parties": ["I", "II", "III", "IV", "VI", "VII", "X", "XV", "XVI", "XVII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVII"],
  "fiches": ["003", "010", "011", "014"]
}
```

- **À ajouter, parties** : II, X, XVII, XIX, XXVII.
- **À ajouter, fiches** : 003 et 011 (002 en option).
- **À retirer** : rien.

### 8.2 Les raisons

| ajout | sections lues | raison |
|---|---|---|
| **II** | § 9 (et § 1–4) | la corde de la chèvre dans un polygone à N côtés (`calculs_archimede.py` section 9) : un autre paramètre de forme, N au lieu de n, avec le même exposant 1/N² que les séries de T3 ; et la fiche F8 (r₄ = r₈) |
| **X** | § 5 | la corde de Ptolémée de l'arc 70,81° : la fiche 010, dont le dossier a besoin (question 5) |
| **XVII** | § 1, § 4, § 6 | le point orange est le bout du plateau de XVI § 3 ; la récursion d'argent est une fraction continue « avec des moins » (le lien de la fiche 014) ; première corde certifiée par intervalles |
| **XIX** | § 6 (et § 2) | le cône à sommet imaginaire : la chèvre infinie est à la distance de Rayleigh (fiche F5) ; i modulo 10 (fiche 014) |
| **XXVII** | § 6 et § 8 | le plan lui-même cite XXVII § 6 dans ses questions 2 et 4 ; § 8 donne l'angle arccos(1/(n + 1)) contre α_n |
| **fiches 003, 011** | — | ce sont les deux objets de T3 et K10 : le polygone circonscrit (003) et le seuil du centre (011) ; le plan rattache T3 au dossier `corde` |
| *(002, en option)* | — | la lumière du 17-gone est le polygone inscrit de K1 ; son lien est le plus faible des trois |

**Rien à retirer.** La fiche 014 reste, avec l'étiquette « lien faible, par les nombres » (§ 4.2). Je ne retire aucune partie : toutes celles de la liste du plan portent un maillon de la chaîne du § 2.1 (I : M1–M4, M7 ; III et IV : M8 ; VI : M9–M10 ; VII : M5 ; XV : M11 ; XVI : M12–M14 ; XX : M6, M15 ; XXI : M16 ; XXII : M17 ; XXIII : M18 ; XXIV et XXV : M19–M26).

### 8.3 Ce que ça change dans le nerf (calculé par l'agent, hors dépôt, à refaire par T1)

J'ai recalculé le nerf du JSON v1 (clés `corde`, `moities`, `bases`, `grain`, `lumiere`, `aiguilles`, `ombres`, `methode`) avec les définitions du plan : une paire est sécante si elle partage une partie ou une fiche ; un triangle est vide si les trois paires sont sécantes mais qu'aucun élément n'est commun aux trois.

| recouvrement de `corde` | niveau « fiches » : paires sécantes sur 28, triangles vides | niveau « fiches + parties » : paires sécantes, triangles vides |
|---|---|---|
| v1 du plan | 18, 9 | 28, 20 |
| + II, X, XVII, XIX, XXVII | 18, 9 | 28, 12 |
| + II, X, XVII, XIX, XXVII + 003, 011 | 21, 14 | 28, 12 |
| + II, X, XVII, XIX, XXVII + 002, 003, 011 | 22, 16 | 28, 11 |
| + II, X, XVII, XIX, XXVII, sans 014 | 17, 7 | 28, 12 |

- **Les cinq parties sont un gain net** : 20 triangles vides tombent à 12 au niveau « fiches + parties », sans rien changer au niveau « fiches ».
- **Les fiches 003 et 011 ont un coût** : elles ajoutent trois paires sécantes et cinq triangles vides au niveau des fiches (9 → 14), et n'en remplissent aucun. Un triangle vide au niveau des fiches est, par construction, une fiche qui manque (plan § 6.1). C'est donc une information, pas un défaut : elle dit que `corde`, `grain`, `aiguilles` ou `ombres` partagent des paires de fiches sans en avoir une commune aux trois. Je laisse le choix à l'agent `croisement` ; ma préférence est de les ajouter.
- **La fiche 014** : la retirer ferait tomber de 9 à 7 les triangles vides au niveau des fiches. Je ne le propose pas, parce que le lien par XVII § 4 est réel, même s'il est mince.
- **Réserve (le plan la fait déjà pour T8)** : le recouvrement a été fait en lisant des résumés qui contiennent les renvois, donc ces nombres ne sont pas indépendants des parties.

---

## Annexe : les chemins cités

J'ai vérifié par `ls` l'existence de chaque document, script, fichier de résultats, figure et fiche cité dans ce dossier (script de contrôle hors dépôt). Aucun fichier n'a été écrit dans le dépôt, hormis celui-ci.
