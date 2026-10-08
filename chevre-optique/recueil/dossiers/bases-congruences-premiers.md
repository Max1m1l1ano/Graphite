# Dossier bases-congruences-premiers : bases, congruences et premiers

*Dossier de la révision 001, agent `bases` (phase 1). Écrit le 2026-10-07. Le plan est dans `recueil/revisions/plan-001.md` (§ 1.3 et § 5.2.3). Il suit le gabarit du plan (§ 7, clé `gabarit.phase_1`) et répond aux huit questions de son entrée. Les huit sections du gabarit sont les § 1 à § 8.*

## Pour lire ce dossier

- **Statuts.** *Démontré* : la preuve est dans le corpus, ou je l'ai écrite ici (à faire relire). *Calculé* : un script ou un calcul exact donne le nombre. *Classique* : résultat publié. *Ma lecture* : une interprétation, pas encore testée. *Ouvert* : on ne sait pas.
- **Marques.** **(R)** : un résultat du dépôt, avec son fichier de `resultats/` et sa section. **(A)** : calculé par l'agent, hors dépôt, dans un dossier temporaire ; le code est au § 7. **(P)** : rappelé d'une publication ; les références sont au § 6.3, avec « à vérifier » quand je n'en suis pas sûr.
- **Ce que je n'ai pas fait.** Je n'ai lancé aucun script du dépôt. Je n'ai écrit aucun autre fichier du dépôt que celui-ci. J'ai lu `/home/user/dzoba/venn17/README.md` (lecture seule, pour K5) et je n'ai exécuté aucun code externe.
- **Ce que j'ai fait en plus de lire.** Des calculs rapides dans un dossier temporaire (jamais dans le dépôt), et quelques recherches en ligne pour les références du § 6.3 : elles rendent des résumés, jamais une page entière, et je l'ai noté à chaque référence (« à vérifier » quand un détail manque). Les valeurs publiées que je cite (tables OEIS) ont été recoupées avec mes propres comptes.
- **Fichiers lus en plus de la liste du plan.** `zone-confusion.md` § 3 ter (le test de la base 10), `carre-neuf-points.md` § 2 (3ⁿ modulo 10), `grille-decalee.md` § 5 (la grille d'Eisenstein), `sphere-faisceaux.md` § 4, § 6 et § 7 (les gammes, l'histoire des bases), `pixels-longitudes.md` § 3 et § 8, `centre-venn.md` § 4.4 (Niven), `tiers-dimension.md` § 1 et § 3 (le tiers de dimension), `carte-connexions.md` § 9 (les pistes), `resultats/tiers_dimension.md` § 2 et `resultats/centre_venn.md` § 2 (pour T7 et la fiche 005), `figures/c1_pi_dimensions.png`, et les deux dossiers déjà écrits (`recueil/dossiers/corde-et-dimensions.md`, `recueil/dossiers/moities-et-crans.md`), seulement pour ne pas refaire ce qu'ils font.
- **Un fait arrivé pendant mon travail.** `scripts/revision_001.py` contient déjà les sections 4.3 (K3), 4.5 (T7) et 4.6 (T6), en plus des sections 1, 2.1, 4.1 et 4.2 annoncées. Je les ai relues et recalculées de mon côté : elles concordent (§ 2.3). Ce dossier ajoute ce qu'elles ne font pas (§ 2.3 et § 7).

## En bref

- **Lien 1 : le même 3 (K3, § 3.2).** Le 3 qui est l'inverse de 7 modulo 10 (fiche 013) est le i de la base 10 (XIX § 2) : 7 = 10 − 3 ≡ −3. Pour b = q² + 1 et p = q² − q + 1, on a b = p + q, q² ≡ −1 (mod b) et q³ ≡ −1 (mod p). Les chiffres qui manquent à la période de 1/p sont exactement les multiples k·q, c'est-à-dire les k·i : c'est démontré pour tout q ≥ 2 (lemme des chiffres, (A)). La période remplit le groupe seulement pour q = 2 et q = 3, d'où (5, 3) et (10, 7) ; aucun autre cas pour b ≤ 400 et p ≤ 4 000 (A). Géométrie : b et p sont les deux normes de l'aiguille (q, 1), sur la grille carrée (XIX) et sur la grille décalée (XV § 5). Le piège de la fiche 013 (1/13) s'explique : 7 et 13 sont les deux facteurs de Φ₆(10) = 91.
- **Lien 2 : le groupe (ℤ/10)* est aussi un groupe de Galois (M1, § 5.2).** L'élément 3 de l'horloge de 10 (i, XIX § 2) conjugue √5, donc envoie le nombre d'or sur −1/φ. Un premier qui finit par 3 ou 7 est inerte dans ℚ(√5) et divise F_(p+1) ; un premier qui finit par 1 ou 9 divise F_(p−1). Ce sont exactement les premiers qui devancent dans la course de Tchebychev modulo 10 (à chaque premier jusqu'à 10⁹). En base 12, où chaque unité est un reflet, la seule classe carrée (1) est la dernière à chaque premier. XII § 3 (Carmichael) construit sans le nommer le tableau des rangs d'apparition de Fibonacci.
- **Lien 3 : Midy est un demi-tour, et les périodes forment une tour (T6, § 3.3).** Si 2h est la période de 1/p, 10ʰ ≡ −1 (mod p) ; si 4 divise la période L, 10^(L/4) est un i modulo p. Un premier sur trois (33,3 % sous 10⁶) porte un i dans l'orbite de 10, et 1/17 est le cas où 10 engendre toute la tour de Gauss du 17-gone (XXVIII § 3.6). Les parts de v₂(L) valent 1/3, 1/3, 1/6, 1/12… en base 10 et 7/24, 7/24, 1/3, 1/24… en base 2 (démontré, mesuré (A)). Le Venn de Midy n'a pas des aires produit : les écarts 17/16, 5/4 et 1/2 sont ceux de la réciprocité quadratique, retrouvés à 0,006 près sur 55 couples (11 bases, 5 valeurs de ℓ ; A, T6b).
- **Lien 4 : un seul théorème des trois distances (§ 3.5).** Le diésis 128/125 et le comma pythagoricien sont des écarts η_k = ‖q_k·α‖ du même théorème, pour α = log₁₀ 2 (q = 10) et α = log₂ 3 (q = 12). La formule N = m·q_k + q_(k−1) + r donne les comptes (N − q_k, r, q_k − r) : 11, 8 et 2 pour les 21 crans (XXVI), 7 et 5 pour les 12 notes (XX), et le comma apparaît à la treizième note. Je l'ai vérifiée pour N = 2 à 150 et cinq valeurs de α (A).
- **T7 est tranché, et il a une loi (§ 3.4).** Le rapport des nombres de puissances de 2 et de 3 sous b vaut 4/3 exactement pour 10 ≤ b ≤ 16 et 244 ≤ b ≤ 256 (démontré : (27/16)ᵏ < 3 seulement pour k = 1 et 2). C'est un hasard de petits entiers. La loi qui reste : un rapport r/s se répète sur ⌊ln 3/ρ⌋ fenêtres de b (ρ = s·ln 3 − r·ln 2), donc sur 2 fenêtres pour 4/3 et sur 81 pour 19/12, la réduite du comma.
- **La fiche 015 : la dérive est la loi de Hardy et Littlewood à taille finie (§ 3.6).** Le rapport par motif exact passe de 3,90 à 2,44 de 10⁴ à 10⁹ ; la prédiction de Hardy et Littlewood, calculée sans paramètre ajusté, donne 4,20 à 2,4447 et s'accorde à 0,0005 près à 10⁹. La limite 2 reste une conjecture.
- **Trois trous.** (1) Aucune fiche ne vient des parties III à XXVIII : j'en propose dix (§ 6.1). (2) Les tables publiées de premiers (OEIS, Lemke Oliver et Soundararajan) ne donnent, à ma connaissance, ni la course à chaque premier, ni le lien avec le nombre d'or, ni la loi de la dérive des 16 motifs de dizaine (à vérifier, § 6.3). (3) Le corpus n'a pas de partie sur la réciprocité quadratique ni sur ℤ[i]/(b) : la base 3 n'a son i que dans F₉, et la fiche 005 reste sans cause (K5 est une obstruction, § 5.3).
- **Corrections au recouvrement** : ajouter les parties VI, XV, XVIII, XX, XXII et XXIV et la fiche 002 ; ne rien retirer (§ 8). Les triangles vides du nerf passent de 20 à 13.
- **Erreurs relevées** (§ 6.2) : « 222,5° est un arrondi » est resté dans `scripts/angle_or_aiguilles.py` et ses résultats après la correction des parties XI et XII ; « deux longueurs seulement aux dénominateurs des réduites » est incomplet ; XVIII § 8 n'a pas de note de correction vers XIX § 1. La fiche 014 signale déjà son point faible (« reste à préciser ») ; le § 4.4 le précise.

## 1. La question directrice et la projection sur D1–D8

### 1.1 La question

> Quelles congruences (même reste modulo b, même groupe d'unités, même réduite) relient les bases, les puissances, les périodes et les premiers ? Quelles coïncidences de chiffres survivent au changement de base ?
>
> (plan, § 1.3)

### 1.2 Ma réponse, en huit points

1. **Un seul objet : le groupe des unités modulo b.** C'est « l'horloge » de la base. On y distingue trois niveaux. Un *reflet* est un x avec x² ≡ 1. Un *quart de tour* est un x d'ordre 4. Un *i* est un x avec x² ≡ −1 : un quart de tour dont le carré est le demi-tour −1. Les bases 12 et 24 n'ont que des reflets ; la base 60 a des quarts de tour sans i ; la base 10 a un i (§ 3.1).
2. **Quand une base a un i.** Exactement quand b est une somme de deux carrés premiers entre eux, b = a² + c² (XIX § 2, classique). Alors i ≡ a/c : c'est la pente de l'aiguille (a, c) de la grille. Les occurrences du corpus sont toutes des cas de ce théorème (§ 3.1).
3. **La base 10 réunit deux couches.** Son i vient de son facteur 5 (3 ≡ i modulo 5, aussi modulo 10). Ses racines digitales viennent de 10 ≡ 1 (mod 9) et son demi-tour de 10 ≡ −1 (mod 11) : c'était déjà écrit dans la partie VI, § 3 ter (« 10 − 1 = 3², 10 + 1 = 11 »). Les deux couches se rejoignent dans la famille b = q² + 1 : b − 1 = q², et q est le i (§ 3.2).
4. **Un premier p ne voit la base b que par l'ordre L de b modulo p**, c'est-à-dire par la période de 1/p. Midy dit que la moitié de la période est un demi-tour (b^(L/2) ≡ −1). Si 4 divise L, le quart de la période est un i. La valuation 2-adique de L est une tour de racines de l'unité, et ses étages se partagent par moitiés ; l'entrelacement avec les autres premiers est fixé par la réciprocité quadratique (§ 3.3).
5. **Les réduites et les trois distances sont un seul théorème.** Il explique les crans (diésis, comma), l'angle d'or, les aiguilles 3-4-5 et 5-7-8 et les trous de la grille (§ 3.5). Le comma est aussi derrière T7 : le compte des puissances sous b suit les réduites de log₂ 3 (§ 3.4).
6. **Peu de coïncidences de chiffres survivent au changement de base, mais celles qui survivent ont une raison.** Survivent : les identités (2⁻ʲ = 5ʲ·10⁻ʲ, fiche 001) et deux familles (b = q² + 1, § 3.2 ; b = 2q² avec q de Pell, § 5.2). Ne survivent pas à la variation du paramètre : le 4/3 des puissances (§ 3.4), 3 + √2/10 ≈ π (III § 1) et les rapports de Lemke Oliver et Soundararajan qui valent 2/3 et 17/24 à 10⁸ (§ 3.6).
7. **Les premiers par position.** La face du cube est exacte (10a + u ≡ a + u modulo 3). Les comptes par motif dérivent lentement avec N, et la dérive est exactement la prédiction de Hardy et Littlewood à taille finie (à 0,0005 près à 10⁹) ; la limite 2 est une conjecture, pas un théorème (§ 3.6).
8. **Le groupe (ℤ/10)* est un groupe de Galois.** L'élément 3 (i) envoie le nombre d'or sur son conjugué −1/φ ; le dernier chiffre d'un premier dit si φ existe modulo p, et la course de Tchebychev est la course entre les premiers où φ n'existe pas (3 et 7) et ceux où il existe (1 et 9) (§ 3.6 et M1, § 5.2).

### 1.3 La projection sur D1–D8

| dimension | poids du plan (§ 1.10) | poids proposé | pourquoi |
|---|---:|---:|---|
| D2 bases, chiffres et congruences | 0,8 | 0,7 | le noyau : i modulo b, les périodes, Midy, les premiers, les réduites des logarithmes |
| D5 Kakeya, Perron et aiguilles | 0,1 | 0,1 | l'aiguille (a, c) dont la pente est i (XIX § 2), l'aiguille (q, 1) sur deux grilles (§ 3.2), les directions de la grille et leurs trois distances (XIV) |
| D6 sphères, cubes, Venn et symétries | 0,1 | 0,1 | Henderson et Fermat (XXVIII § 3.1–3.2), la tour de Gauss du 17-gone, le cube {0, 1}⁴ des dizaines (fiche 015) |
| D7 hasard et méthode | 0 | 0,1 | ce dossier teste des coïncidences d'entiers par la variation du paramètre : T7, le 4/3, 3 + √2/10, la dérive de la fiche 015, les rapports 2/3 et 17/24 ; il applique la table du § 10 de CLAUDE.md |
| D1, D3, D4, D8 | 0 | 0 (effleurés) | D1 : √2 et √3 de la fiche 014 sont des cordes ; D3 : le grain du ppm de la fiche 001 (2⁻¹⁷ est l'aire moyenne d'une région du Venn à 17 courbes) ; D4 : rien ; D8 : le diésis et le comma sont des rapports de fréquences (XX § 6, XXVI § 2) |

Je garde D2 comme dimension principale. Je prends 0,1 sur D2 pour D7, parce qu'une fiche proposée sur trois (N5, N8, N9, au § 6.1) est un test de coïncidence ou de dérive. Les poids font 1,0 dans les deux colonnes.

## 2. Les chaînes de production

### 2.1 Partie par partie, dans l'ordre

Chaque bloc donne : le document et ses sections sur les nombres, le script (en-têtes de section et fonctions citées), les résultats, les figures, et ce que le script produit. Les numéros de section des résultats ne suivent pas toujours ceux du document ; je donne les deux.

**III — π, √2 et les dimensions.**
- Document : `pi-dimensions.md` § 1 à 3 (la suite 3 + √2/10 + √3/100 + …, les retenues, les vraies formules), § 6 (φ, ρ, 3² et 2³).
- Script : `scripts/pi_dimensions.py`, sections 1 (la suite et sa limite), 2 (`gloutonne` : les retenues), 3 (Archimède, Viète, Nilakantha, Wallis), 4 (sommes sur toutes les dimensions), 5 (φ, ρ et la chèvre). Résultats : `resultats/pi_dimensions.md` § 1 à 5. Figure : `figures/c1_pi_dimensions.png` (a : qui converge vers π ; b : r₇ contre ρ ; c : Σ Vₙ).
- Il produit : les sommes partielles de 3 + Σ √k/10^(k−1), dont l'écart à π tombe à −1,7·10⁻⁴ à l'étape 2 puis remonte à +0,017, et la limite 3,160992928… (R, § 1) ; les retenues gloutonnes de π, de √10 et de e + 0,42, aussi désordonnées l'une que l'autre (R, § 2) ; Σ Vₙ = e^π(1 + erf √π) = 45,99932… (R, § 4) ; r₇ = 1,324680 contre ρ = 1,324718 (R, § 5).

**VII — Les nombres des polynômes de la chèvre.**
- Document : `nombres-polynomes.md` § 5 (Kummer : les facteurs 2 comptent les retenues de la base 2), § 7 (la virgule binaire, le coefficient B(m, k)).
- Script : `scripts/polynomes.py`, fonctions `v2`, `polynome_impair`, `h`, `kappa_p`, `B`, `F_sur_h`, `h_frac`, `periode2`, `chiffres` ; en-têtes 1 (impairs), 2 (pairs 2, 6, 12, 24), 3 (réciprocité et retenues), 5 (la preuve). Les en-têtes sont numérotés 1, 2, 3, 5 ; les résultats ont cinq sections, le § 4 étant les retenues. Résultats : `resultats/polynomes.md` § 1 à 5. Figures : `figures/g1_polynomes_retenues.png`, `figures/g2_virgule_binaire.png` (a : les périodes binaires des coefficients ; b : divisés par h₇, tout s'arrête avant 10 chiffres).
- Il produit : les polynômes impairs de la dimension 3 à 31, leurs termes constants ±2^e avec e = 2(n − 1) − s₂((n − 1)/2) (s₂ = nombre de 1 en binaire), les périodes binaires de hₙ (2, 4, 12, 12, 60 pour n = 3, 5, 7, 9, 13) et la preuve que F/hₙ n'a que des fractions binaires finies (R, § 5).

**IX — Le moiré de Fibonacci, l'équation d'optique et les racines de l'unité.**
- Document : `moire-fibonacci.md` § 3 (1/a + 1/b = 1/c et Fermat), § 4 (les racines de l'unité : e^(iπ/5), les huit racines dixièmes, le pentagone), § 5 (Hurwitz).
- Script : `scripts/moire_fibonacci.py`, sections 3 (l'équation d'optique), 4 (les racines de l'unité, la corde du pentagone), 5 (Hurwitz). Résultats : `resultats/moire_fibonacci.md` § 3 à 5. Figures : `figures/i1_moire_fibonacci.png` et `figures/i2_optique_racines.png`, que le plan ne demandait pas et que je n'ai pas regardées.
- Il produit : le tableau des deux foyers (z₁/z_N → φ², z₂/z_N → φ, 1/z₁ + 1/z₂ = 1/z_N exact) et les solutions entières de 1/aⁿ + 1/bⁿ = 1/cⁿ pour a ≤ b ≤ 300 (397 pour n = 1, dont 63 primitives ; 17 pour n = 2, dont 3 primitives ; aucune pour n = 3) (R, § 3) ; les racines dixièmes de l'unité autres que ±1, aux parties réelles ±φ/2 et ±1/(2φ) (R, § 4) ; q²·|x − p/q| → 1/√5 pour φ (R, § 5).

**XI — L'angle d'or, les trous du cercle et les petites aiguilles.**
- Document : `angle-or-aiguilles.md` § 2 (les trous : théorème des trois distances), § 5 (220 = 4×55, 121 = 11 + 2×55).
- Script : `scripts/angle_or_aiguilles.py`, sections 1 (le partage 1/φ² + 1/φ), 2 (la boucle N = 2 à 60 : les longueurs des trous), 3 (le spectre : `mot_fibonacci`, `coef`), 4 (les petites aiguilles : `spectre_local`, `reconstruit`). Résultats : `resultats/angle_or_aiguilles.md` § 1 à 4. Figure : `figures/k1_angle_or_aiguilles.png` (a : le partage ; b : N = 13 a deux trous, N = 10 en a trois ; c : l'escalier des trous ; d : les petites aiguilles ; e : le spectre).
- Il produit : deux longueurs seulement pour N = 2, 3, 5, 8, 13, 21, 34, 55, trois sinon, toutes de la forme 360°/φᵏ, la plus grande égale à la somme des deux autres (R, § 2) ; les composantes de Fibonacci et de Lucas du spectre, les zéros aux multiples de 55 (R, § 3).

**XII — 144, la douzième lentille.**
- Document : `lentille-144.md` § 2 (137,5° et 222,5° exacts : 55/144 et 89/144 de tour), § 3 (pourquoi 144 est la dernière : Carmichael).
- Script : `scripts/lentille_144.py`, fonction `decimal_fini` ; sections 1 (les approximations F(k − 2)/F(k) de tour), 2 (les facteurs premiers de F(k) jusqu'à k = 60), 3 (la lentille à 144 anneaux : `mot_fibonacci`, `intensite_axe`), 4 (la corde en dimension réelle : `part`, `corde`). Résultats : `resultats/lentille_144.md` § 1 à 4. Figure : `figures/l1_lentille_144.png` (a : les fractions de Fibonacci ; b : le tour en 144 pas ; c : la lentille ; d : la chèvre entre 2D et 3D).
- Il produit : les angles qui tombent juste en degrés pour k = 3, 4, 5, 6 et 12 seulement (180°, 120°, 144°, 135°, 137,5°) ; les indices sans nouveau facteur premier jusqu'à k = 60 : 6 et 12 (R, § 2).

**XIV — L'aiguille sur une grille.**
- Document : `aiguille-grille.md` § 1 (les directions permises : Jacobi, Fermat, Niven), § 3 (les convergentes, Hurwitz, Cassini), § 4 (le pavage de Farey, Penner).
- Script : `scripts/aiguille_grille.py`, § 1 (`points_cercle`, `r2_formule`, `angles_quart`, `ecarts`), § 3 (les aiguilles de Fibonacci), § 4 (`det2`, `lambda_ford`) ; les § 2, 5 et 6 (demi-disque, Kakeya fini, Perron sur grille) sont hors de ce dossier. Résultats : `resultats/aiguille_grille.md` § 1, 3 et 4. Figures : `figures/n1_aiguille_grille.png`, `figures/n2_perron_grille.png` (hors liste).
- Il produit : le nombre de directions par quart de tour (1, 3, 3, 5, 9, 27, 45 pour L = 1, 5, 13, 25, 65, 1 105, 5 525) et leur plus grand trou (90°, 36,87°, 44,76°, 20,61°, 16,26°, 8,37°, 5,45°), que j'ai recalculés (A) ; le déterminant ±1 entre aiguilles voisines de Fibonacci (R, § 3).

**XIX — Les bases 2 et 10 sont deux objets.**
- Document : `bases-objets.md` § 2 (i modulo 10 et le théorème), § 3 (les subdivisions 1/n), § 4 (deux échelles qui ne se recalent jamais), § 9 (les deux couches).
- Script : `scripts/bases_objets.py`, § 1 (`racines_i`, `aiguilles` : le script s'arrête avec `SystemExit` si le théorème échoue pour un b de 2 à 40), § 2 (`periode`, `developpement`), § 3 (la fraction continue de log₁₀ 2, les quasi-retours, Benford sur 10⁴ puissances, `GAPS` pour M = 10, 30, 93, 100), § 6 (`ordre_mod`, `facteurs`, `cycle_txt`, et l'assertion `ASSERT_24`). Résultats : `resultats/bases_objets.md` § 1, 2, 3 et 6. Figure : `figures/t1_bases_modulaires.png` (a : la droite enroulée ; b : les horloges mod 10, 5, 13, 2 ; c : les aiguilles des bases à i ; d : les périodes de 1/n ; e : le cercle des décades ; f : les flottants).
- Il produit : la liste des bases de 2 à 40 avec leurs racines de −1 (2, 5, 10, 13, 17, 25, 26, 29, 34, 37), les périodes de 1/n en bases 2 et 10, log₁₀ 2 = [0 ; 3, 3, 9, 2, 2, 4, 6, 2, 1, 1, …] et ses réduites, les cycles du dernier chiffre de bⁿ, et la liste des bases où toute unité est un reflet : 2, 3, 4, 6, 8, 12, 24 (R, § 6, vérifié jusqu'à 200).

**XXI — Les trois 24 et le miroir 49-50-51.**
- Document : `vingt-quatre-miroir.md` § 1 (η(24τ) : les exposants sont des carrés premiers avec 6), § 2 (7² ≡ −1 modulo 50, Pell, l'aiguille de 50).
- Script : `scripts/vingt_quatre_miroir.py`, § 1 (`sup`, `qp`, `serie` : η(24τ) en q = 1/10), § 2 (`RAC50`, `deux_carres`, `trois_carres`, `gmul`, `cents`) avec les assertions `RAC50 == [7, 43]` et `DEUX_FACONS == 50`. Résultats : `resultats/vingt_quatre_miroir.md` § 1 et 2. Figure : `figures/v1_vingt_quatre.png` (a : les trois 24 ; b : η(24τ) ; c : ses chiffres en base 10, rangés par 24 ; d : l'aiguille de 50 ; e : le miroir 10⁻⁴⁹, 10⁻⁵¹ ; f : le faisceau gaussien).
- Il produit : les 168 premiers chiffres de η(24τ) en q = 1/10 (0,0, vingt-trois 9, un 8, vingt-quatre 9, soixante et onze 0, un 1, quarante-sept 0), 7² + 1² = 5² + 5² = 50 comme premier nombre à deux écritures, (7 + i)² = 2·(24 + 7i), et les trois paires de tritons (R, § 2).

**XXV — Les ouverts refermés, la tranche 10⁻⁴⁹ – 10⁻⁵⁵ et les tournants d'aiguilles.**
- Document : `tranche-aiguilles.md` § 2 (la tranche : i modulo 50 et 53), § 3 (les tournants d'aiguilles).
- Script : `scripts/tranche_aiguilles.py`, § 5 (`THETA`, `RD`, `reps`, `MINC`, `IMOD` avec l'assertion `[k pour lesquels IMOD[k]] == [50, 53]`), § 6 (`sig11s`, `stations`, r₂₄ par le τ de Ramanujan). Résultats : `resultats/tranche_aiguilles.md` § 5 (= doc. § 2) et § 6 (= doc. § 3). Figure : `figures/z2_tranche_aiguilles.png` (a : sept niveaux ; b : les aiguilles du plan ; c : combien de dimensions ; d : le retournement i·i = −1 ; e : cos αₙ = x₀ ; f : six décades, vingt crans).
- Il produit : le tableau k = 49 à 55 (carrés minimaux 1, 2, 3, 2, 2, 3, 4 ; r₂, r₃, r₄ ; i modulo k : 7 et 43 pour 50, 23 et 30 pour 53, aucun pour 49, 51, 52, 54, 55) ; les arrêts du retournement sur le réseau (aucun pour (7, 1, 1) en dimension 3).

**XXVI — Kakeya à 10⁻⁵⁰, la virgule du kibi et son miroir, le cube qui tourne.**
- Document : `kakeya-miroir.md` § 2 (la virgule : diésis, miroir 5ʲ, 9,49 – 9,72 – 9,95 %, la retenue, les gaps, la tranche en crans).
- Script : `scripts/kakeya_miroir.py`, § 2 : `dec`, `trois_ecarts`, `rapport`, `fc`. Résultats : `resultats/kakeya_miroir.md` § 2.1 à 2.6 (doc. 2.1 = rés. 2.1 ; doc. 2.2 = rés. 2.3 ; doc. 2.3 = rés. 2.1 ; doc. 2.4 = rés. 2.2 ; doc. 2.5 = rés. 2.4 et 2.5 ; doc. 2.6 = rés. 2.6). Figure : `figures/aa2_virgule_miroir.png` (a : le cercle des décades, 21 crans, trois écarts ; b : kilo à téra et leurs miroirs ; c : 9,49 – 9,72 – 9,95 ; d : la retenue qui court jusqu'au 9 ; e : les crans les plus proches des décades ; f : vingt crans dans la tranche).
- Il produit : 128/125, (128/125)², le miroir 10⁶/2²⁰ = 0,95367431640625 (les chiffres de 5²⁰), les écarts 9,4902 – 9,7152 – 9,9512 %, et le tableau des écarts du cercle des décades : 4 crans (5/4 ×1, 2 ×3), 11 crans (128/125 ×1, 5/4 ×8, 32/25 ×2), 21 crans (128/125 ×11, 625/512 ×8, 5/4 ×2), 94 crans (R, § 2.1 à 2.4).

**XXVIII — L'hexagone rejoint l'octaèdre, Perron développé, le Venn à 17.**
- Document : `octaedre-perron-venn.md` § 3.1 (Henderson), § 3.2 (Fermat dessiné : 7 710 formes), § 3.6 (Gauss, i et 1/17).
- Script : `scripts/octaedre_perron_venn.py`, § 3 : `premier`, `codes_venn`, `croisements_ellipses` (le Venn à 5 ellipses), `polygone`, `tf_polygone`, `aigrettes` ; le calcul de Gauss, de 4 ≡ i et de 1/17 est écrit en ligne (lignes 683 à 705). Résultats : `resultats/octaedre_perron_venn.md` § 3.1, 3.2 et 3.4 (= doc. § 3.6). Figure : `figures/ac3_venn17.png` (a : cinq ellipses ; b : les 7 710 formes ; c : le diaphragme à 17 lames ; d : les 34 aigrettes ; e : N ou 2N aigrettes ; f : Perron à 17 lames).
- Il produit : cos(2π/17) = 0,932472229404356, les ordres modulo 17 (2 → 8, 3 → 16, 4 → 4, 10 → 16), 10⁴ ≡ 4 ≡ i et 10⁸ ≡ −1, 05882352 + 94117647 = 99999999, et les périodes de Gauss en 2, 4 et 8 classes (R, § 3.4).

**Recueil — `scripts/recueil_verifications.py`.**
- Sections : 1 (les congruences de i : bases 10, 2, 3 et F₉), 2 (les puissances sous 10), 3 (les exposants 1/2 et 3/2 et leurs fractions continues), 4 (les racines digitales), 5 (Midy et Midy étendu), 6 (les premiers par position), 7 (l'inversion 2 ↔ 5 et le croisement en 7/2). Résultats : `resultats/recueil_verifications.md` § 1 à 7. Pas de figure.
- Chaîne : § 3 → fiche 014 ; § 4 → fiche 013 ; § 6 → fiche 015 ; § 7 → le lien de la fiche 001. Les § 1 (i modulo b, F₉), § 2 (le 4/3) et § 5 (Midy) n'ont aucune fiche : ce sont des trous du recueil (§ 6.1).
- Il produit : les bases b ≤ 40 où −1 est un carré, le tableau des puissances sous 10 (2 en a quatre, 3 en a trois), les quatre fractions continues imaginaires vérifiées à moins de 10⁻³⁰, DR(a·b) = DR(DR(a)·DR(b)) sur 100 000 paires, 49 périodes paires et 26 impaires parmi les 75 premiers de 7 à 397 avec Midy 49 sur 49 et Midy étendu 375 sur 375 (je les ai recomptés, (A)), et les 16 motifs de dizaines sous 10⁶ dont 165 quadruplets (R, § 6).

### 2.2 Cinq chaînes qui se suivent

- **A. Le quart de tour i modulo b.** XIX § 2 (le théorème, vérifié pour b de 2 à 40) → XXI § 2 (7² ≡ −1 modulo 50) → XXV § 2 (`IMOD` : de 49 à 55, seuls 50 et 53 ont un i) → XXVIII § 3.6 (4 ≡ i modulo 17) → recueil § 1 (les bases ≤ 40, F₉) → `scripts/revision_001.py` § 4.1 et § 4.3. Chaque maillon reprend le théorème de XIX sans le redémontrer.
- **B. Les périodes et les retenues.** VII § 5 et § 7 (Kummer, périodes binaires) → XIX § 3 (périodes de 1/n en bases 2 et 10) → recueil § 4 et § 5 (racines digitales, Midy) → XXVIII § 3.6 (le miroir de 1/17) → `scripts/revision_001.py` § 4.1 et § 4.6.
- **C. Les réduites et les trois distances.** XI § 2 (l'angle d'or) → XIV § 1, 3 et 4 (les directions du cercle de rayon 5ᵏ, les convergentes) → XV § 5 (la grille d'Eisenstein, le triangle 5-7-8) → XIX § 4 (log₁₀ 2) → XX § 6 (log₂ 3, 19/12) → XXVI § 2.4 et § 2.5 (21 crans).
- **D. Les décades, les crans et la virgule.** XIX § 4 (2¹⁰ ≈ 10³, kibi contre kilo) → XXV § 2 (six décades, vingt crans) → XXVI § 2 (le diésis, le miroir aux chiffres de 5ʲ) → XXIX § 2.1 (fiche 001 : 2⁻¹⁷ et 5¹⁷).
- **E. Les premiers.** recueil § 6 (les 16 motifs) → fiche 015 → `scripts/revision_001.py` § 4.2 (la variation de N). Cette chaîne n'a aucune partie : elle est née du message fondateur du recueil.

### 2.3 Où en est `scripts/revision_001.py`, et ce que ce dossier ajoute

Les sections qui me concernent existent déjà dans le script et dans `resultats/revision_001.md` : § 4.1 (fiche 013), § 4.2 (fiche 015), § 4.3 (K3), § 4.5 (T7), § 4.6 (T6). Je les ai relues, puis recalculées avec un code écrit de mon côté (§ 7). Tout concorde :

- **K3** (R, § 4.3) : q = 2, 3, 7, 13 donnent p premier, avec les périodes 2, 6, 6, 6 ; q = 5, 11, 17, 19 donnent p = 21, 111, 273, 343, non premiers. Je retrouve la même table (A).
- **T7** (R, § 4.5) : 4/3 pour b de 10 à 16 et de 244 à 256 seulement. Même résultat (A), jusqu'à b = 3·10⁶ (§ 7.1).
- **T6** (R, § 4.6) : base 10, sous 10⁶ : v₂(L) = 0, 1, 2, 3 pour 0,3334 ; 0,3340 ; 0,1660 ; 0,0832, parts paire 0,6666, et 3 | L, 5 | L, 7 | L pour 0,3758 ; 0,2076 ; 0,1457. Base 2 : 0,2923 ; 0,2916 ; 0,3329 ; 0,0417 et 0,7077. Je retrouve ces nombres au dernier chiffre (A).

Ce que j'ajoute, et que le script n'a pas :

1. **Le lemme des chiffres** de K3 (§ 3.2) : vrai pour tout q ≥ 2, pas seulement pour q premier avec p premier. Il explique pourquoi les chiffres de la période sont les unités modulo b − 1. Avec lui, l'**extension du balayage 4.1** : b de 3 à 400 et p jusqu'à 4 000 donnent les mêmes trois cas (3, 2), (5, 3), (10, 7) (A). Et la factorisation Φ₆(q² + 1) = Φ₆(q)·Φ₃(q), qui explique le piège de 1/13.
2. **T6 en valeurs exactes** : 1/3, 1/3, 1/6, 1/12… pour une base générique et 7/24, 7/24, 1/3, 1/24, 1/48… pour la base 2, par un calcul de quatre lignes ; les quatre densités de L pair selon le caractère quadratique de la base (1/3, 5/6, 17/24, 2/3) ; ℓ/(ℓ² − 1) démontré (§ 3.3). Et **T6b**, un test que le plan n'avait pas prévu : la loi jointe des événements « 2 divise L » et « ℓ divise L ». Elle n'est pas le produit des marges quand la partie sans carré de la base vaut ℓ ou 2ℓ ; les écarts sont ceux de la réciprocité quadratique.
3. **T7 : la preuve et la loi.** Le rapport vaut 4/3 exactement quand (27/16)ᵏ < 3, soit k = 1 et 2. Pour un rapport r/s quelconque, le nombre de fenêtres de b est ⌊ln 3/ρ⌋ ou ⌊ln 2/|ρ|⌋ avec ρ = s·ln 3 − r·ln 2 : les rapports qui se répètent sont les réduites de log₂ 3 (§ 3.4).
4. **La formule des trois distances** (comptes et longueurs), vérifiée pour N = 2 à 150 et cinq valeurs de α, avec le diésis et le comma comme écarts, la liste des N à deux longueurs, et la lecture de XXVI § 2.5 comme un cas (§ 3.5).
5. **Les premiers par position** (§ 3.6) : la course de Tchebychev modulo 10 jusqu'à 10⁹ et en base 12, le tableau de Lemke Oliver et Soundararajan jusqu'à 10⁹, le lien entre le dernier chiffre et le nombre d'or (F_(p∓1)), les paires de dizaine et les 16 motifs jusqu'à 10⁹, la prédiction de Hardy et Littlewood à taille finie pour la dérive de la fiche 015, et le recoupement avec les tables publiées (OEIS).
6. **Deux compléments** (§ 7.2 et § 7.3) : l'effet de mes corrections sur le nerf du recouvrement, et la famille de Pell des bases à deux écritures avec le décompte des termes 10 et 12 dans les fractions continues de √(aᵉ).

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 Le quart de tour i modulo b (question 2)

**Le théorème** (XIX § 2 ; classique (P)). Pour b ≥ 2, ces trois énoncés sont équivalents : (1) x² ≡ −1 (mod b) a une solution ; (2) 4 ne divise pas b, et aucun nombre premier ≡ 3 (mod 4) ne divise b ; (3) b = a² + c² avec a et c premiers entre eux. Alors i ≡ a/c (mod b) : c'est la pente de l'aiguille (a, c) de la grille. Il y a 2ˢ solutions, où s est le nombre de facteurs premiers impairs distincts de b. Le script de XIX le vérifie pour b de 2 à 40 (R : `resultats/bases_objets.md` § 1). Je l'ai étendu à b ≤ 120 et j'ai compté les racines : 2 pour 41, 53 et 101, 4 pour 65 et 85 (A). Les bases ≤ 120 qui ont un i sont 2, 5, 10, 13, 17, 25, 26, 29, 34, 37, 41, 50, 53, 58, 61, 65, 73, 74, 82, 85, 89, 97, 101, 106, 109 et 113 (A).

**Toutes les occurrences du corpus.**

| ce qu'on lit | où | statut |
|---|---|---|
| 3 ≡ i, 7 ≡ −i modulo 10 ; l'horloge 1 → 3 → 9 → 7 → 1 | XIX § 2 (R : `resultats/bases_objets.md` § 1) | démontré, vérifié |
| 3ⁿ ≡ 3, 9, 7, 1 (mod 10) : le nombre 3ⁿ des centres de faces du cube tourne d'un quart de tour par dimension | XXII § 2 (`carre-neuf-points.md`) | démontré (c'est l'ordre de 3 modulo 10) |
| 2 ≡ i (mod 5) : 1/5 a la période 4 en binaire | XIX § 3 | démontré |
| 10 ≡ i (mod 101) : 1/101 a la période 4 en décimal ; 101 = 10² + 1 | XIX § 3 | démontré |
| 7 ≡ i et 43 ≡ −i (mod 50) ; 50 = 7² + 1² = 5² + 5² | XXI § 2 (R : `resultats/vingt_quatre_miroir.md` § 2) | démontré, assertion `RAC50 == [7, 43]` |
| 23 ≡ i et 30 ≡ −i (mod 53) ; 53 = 7² + 2² ; aucun i pour 49, 51, 52, 54, 55 | XXV § 2 (R : `resultats/tranche_aiguilles.md` § 5) | démontré, assertion `IMOD` |
| 4 ≡ i et 13 ≡ −i (mod 17) ; 17 = 4² + 1 = 2⁴ + 1 ; 10⁴ ≡ 4 et 10⁸ ≡ −1 | XXVIII § 3.6 (R : `resultats/octaedre_perron_venn.md` § 3.4) | démontré |
| 2 ≡ −1 (mod 3) ; √2 = ±i et 2√2 = −i dans F₉ = F₃[i] | recueil § 1 (R), fiche 014 | démontré dans F₉, faux dans ℤ/3 |
| i ≡ −i ≡ 1 (mod 2) | XIX § 2 | cas dégénéré : l'aiguille (1, 1) ne tourne pas |
| retourner l'aiguille = i·i = −1 ; en 2D deux chemins, par i ou par −i, « comme 3 et 7 modulo 10 » | XX § 4 | lecture du corpus, cohérente avec le théorème |
| e^(iπ/5) et les racines dixièmes de l'unité | IX § 4 | complexe, pas modulaire ; voir M1 (§ 5.2) |
| 10^(L/4) est un i modulo p quand 4 divise la période L : 4 mod 17, 27 mod 73, 10 mod 101, 100 mod 137 | XXVIII § 3.6 pour 17 ; le cas général n'est pas dans le corpus (§ 3.3) | démontré, calculé (A) |

**Les bases du corpus, avec ou sans i.** λ(b) est l'ordre maximal d'une unité modulo b. Tous les nombres de ce tableau sont calculés (A) ; les racines de −1 sont celles de `resultats/bases_objets.md` § 1 quand b ≤ 40.

| base b | où dans le corpus | i modulo b | λ(b) | horloge |
|---|---|---|---:|---|
| 2 | XIX | « i ≡ 1 » : dégénéré | 1 | aucune unité à tourner |
| 3 | recueil § 1, fiche 014 | non (dans F₉) | 2 | reflets seulement |
| 4 | diviseur de 24 | non | 2 | reflets seulement |
| 5 | XIX § 3 | 2 et 3 | 4 | quart de tour |
| 7 | VII (1/7), XXI (√7) | non | 6 | ordres 1, 2, 3, 6 : aucun quart de tour |
| 10 | XIX | 3 et 7 | 4 | 1 → 3 → 9 → 7 |
| 11 | XIX § 3 (1/11, 10 ≡ −1) | non | 10 | ordres 1, 2, 5, 10 : un demi-tour, pas de quart |
| 12, 24 | XIX § 9, XXI § 1 | non | 2 | reflets seulement (5² ≡ 7² ≡ 11² ≡ 1 modulo 12, R : `resultats/bases_objets.md` § 6) |
| 13 | XIX § 3, VII (dimension 13) | 5 et 8 | 12 | quart de tour |
| 17 | XXVIII § 3.6 | 4 et 13 | 16 | quart de tour |
| 19, 23 | XXVIII (Venn à 19 et 23 courbes) | non | 18, 22 | aucun quart de tour |
| 25, 26 | XIX § 2 (tableau) | 7 et 18 ; 5 et 21 | 20, 12 | quart de tour |
| 41, 53 | XX § 6 (gammes à 41 et 53 notes) | 9 et 32 ; 23 et 30 | 40, 52 | quart de tour |
| 49, 54 | XXV | non | 42, 18 | aucun quart de tour |
| 50 | XXI § 2, XXV | 7 et 43 | 20 | quart de tour |
| 51, 52, 55 | XXV | non | 16, 12, 20 | quarts de tour sans i |
| 60, 270, 360, 720 | XIX § 9, XII (« 12, 24, 60, 720, 270 ») | non | 4, 36, 12, 12 | quarts de tour sans i |
| 101 | XIX § 3 | 10 et 91 | 100 | quart de tour |

**Ce que cela change à l'horloge.** Il y a trois sortes d'horloges (R : XIX § 9 pour la distinction ; A pour le tableau).

- **Reflets seulement** : toute unité x vérifie x² ≡ 1. Ce sont exactement les diviseurs de 24 : 2, 3, 4, 6, 8, 12, 24 (R : `resultats/bases_objets.md` § 6, vérifié jusqu'à 200 ; je le retrouve (A)). Le dernier chiffre de aⁿ, pour a premier avec la base, n'y fait jamais mieux qu'un demi-tour (CLAUDE.md § 3).
- **Quarts de tour sans i** : il y a des unités d'ordre 4, mais leur carré n'est pas −1. Dans ℤ/60 = ℤ/4 × ℤ/3 × ℤ/5, le quart de tour n'agit que sur le facteur ℤ/5 : si x ≡ 2 (mod 5) et x ≡ 1 (mod 12), alors x² ≡ −1 (mod 5) mais x² ≡ 1 (mod 12), donc x² ≠ −1. C'est le cas de 60, 360, 720, 270, 51, 52 et 55.
- **Un i** : −1 est un carré. Il faut que 4 ne divise pas b et qu'aucun premier ≡ 3 (mod 4) le divise : les bases du cercle et de l'heure (12, 24, 60, 360) n'en auront jamais. La base 10 le doit à son facteur 5 (3² ≡ −1 modulo 5, et 3 ≡ 1 modulo 2).
- **Une base sans i garde un quart de tour dans le plan.** ℤ[i]/(b) a b² éléments et contient toujours i. Pour b = 3, c'est le corps F₉ : ses éléments d'ordre 4 sont ±i, et « √2 = ±i » y dit seulement que 2 ≡ −1. Pour b = 12, c'est ℤ[i]/(4) × F₉. Ma lecture : la « grille pliée » de XIX § 2 se replie sur une droite de restes seulement quand b = a² + c² avec a et c premiers entre eux ; sinon, le quart de tour de la grille agit sur le plan (x, y), pas sur la droite.

**Ce que la partie VI disait déjà.** `zone-confusion.md` § 3 ter écrit : 10 − 1 = 3² (règles de 3 et de 9), 10 + 1 = 11 (règle de 11), 10 = 2 × 5 (règles de 2 et de 5). Ce sont les trois congruences les plus simples de la base 10 : 10 ≡ 1 (mod 9) donne les racines digitales (fiche 013), 10 ≡ −1 (mod 11) donne le demi-tour de 1/11 (XIX § 3), et 10 = 3² + 1 donne le i de la base 10. On remarque que 10 − 1 = 3² : le module des racines digitales est le carré de i. C'est la famille K3 (§ 3.2) : b − 1 = q².

### 3.2 La famille b = q² + 1 et la congruence K3 (question 3)

**Énoncé** (démontré ici, à faire relire ; vérifié (A)). Soit q ≥ 2, b = q² + 1 et p = q² − q + 1.

1. q² ≡ −1 (mod b) ; b − p = q ; q·p ≡ 1 (mod b) ; p divise q³ + 1 = (q + 1)·p. Donc b ≡ q (mod p) et q³ ≡ −1 (mod p).
2. Si q est premier, p − 1 = q(q − 1) = φ(q²) = φ(b − 1).
3. Si p est premier et q ≥ 3, l'ordre de b modulo p est exactement 6 : la période de 1/p en base b est 6. Pour q = 2, b = 5 et p = 3, la période est 2.
4. **Lemme des chiffres.** Pour tout q ≥ 2, les chiffres ⌊b·r/p⌋ pour r = 1, …, p − 1 sont exactement les entiers de [1, b − 2] qui ne sont pas multiples de q. Les chiffres de [0, b − 1] qui manquent sont donc 0, q, 2q, …, q·q = b − 1 : ce sont les k·q, les k·i, avec i = q.
5. Si q est premier, les entiers de [1, q² − 1] non multiples de q sont les unités modulo q² = b − 1. Si de plus la période visite tous les restes r (p premier et p − 1 = L), les chiffres de la période de 1/p sont exactement les unités modulo b − 1.

**Preuve.** (1) se calcule : q·p = q·b − q² ≡ −q² ≡ 1. (2) vient de φ(q²) = q² − q. (3) b = p + q ≡ q (mod p) et q³ ≡ −1, donc b⁶ ≡ 1. Pour q ≥ 3, p > q + 1, donc le premier p ne divise ni q + 1 ni q − 1 : b³ ≡ −1 ≢ 1 et b² ≢ 1, l'ordre est 6. (4) Comme b = p + q, le chiffre est d(r) = r + ⌊q·r/p⌋. Il croît avec r, de d(1) = 1 à d(p − 1) = p − 1 + q − 1 = b − 2, par pas de 1 ou de 2. Le nombre de pas de 2 est (b − 3) − (p − 2) = q − 1. Ils ont lieu quand ⌊q·r/p⌋ augmente, c'est-à-dire en r = j(q − 1) + 1 pour j = 1, …, q − 1 (car j·p/q = j(q − 1) + j/q avec 0 < j/q < 1). Le chiffre sauté vaut alors d(r − 1) + 1 = j·q. (5) est immédiat. ∎

**Pourquoi (5, 3) et (10, 7)** (la question du plan). Le balayage 4.1 cherche les (b, p) dont la période a pour chiffres les unités modulo b − 1.

- Le lemme dit que les chiffres de tous les restes r forment déjà cet ensemble, pour b = q² + 1 et p = q² − q + 1, quand q est premier.
- Il reste à savoir si la période visite tous les restes. Elle en visite 6 (point 3), et il y en a p − 1 = q(q − 1). Les deux sont égaux exactement pour q = 3 (6 = 6, donc (10, 7)). Pour q = 2, la période 2 est p − 1 = 2 (donc (5, 3)).
- Les cas suivants de la famille, (50, 43) et (170, 157), ont encore les points 1, 2 et 4 mais une période 6 pour 42 et 156 restes : ils ne sont pas pleins.
- **Balayage élargi (A).** Pour b de 3 à 400 et p premier jusqu'à 4 000, les seuls cas pleins sont (3, 2), (5, 3) et (10, 7), comme dans le balayage 4.1 (b ≤ 60, p ≤ 400). Le cas (3, 2) est hors famille et trivial : 1/2 = 0,111… en base 3.
- **Le 3 de 1/7 est le i.** Dans la base 10, 7 = 10 − 3 ≡ −3 = −i. Les chiffres qui manquent à 1/7 sont 0, 3, 6, 9 : les k·i pour k = 0, 1, 2, 3. La raison que donne le § 4.1 du script (7 × 3 ≡ 1, donc 7d mod 10 ≤ 3) est ce lemme écrit pour q = 3.
- **La coïncidence de la fiche 013 est trois faits indépendants** : (a) les chiffres de 1/7 sont les unités modulo 9 (le lemme) ; (b) la période est pleine (10 est racine primitive modulo 7, q = 3) ; (c) 2 engendre les unités modulo 9 (2 est racine primitive modulo 9 : c'est une propriété de q = 3 seul). Les deux ensembles égaux (les chiffres de 1/7 et les racines digitales de 2ⁿ) sont donc deux routes vers « les unités modulo 9 ».
- **Pourquoi 1/13 échoue, et pourquoi 1/7 et 1/13 ont la même période** *(démontré)*. b² − b + 1 = (q² + 1)² − (q² + 1) + 1 = q⁴ + q² + 1 = (q² − q + 1)(q² + q + 1). Pour q = 3 et b = 10 : Φ₆(10) = 91 = 7 × 13. Les deux premiers de période 6 en base 10 sont donc les deux facteurs, p = q² − q + 1 = 7 et p′ = q² + q + 1 = 13. Tous deux divisent 10³ + 1 = 1 001 = 7 × 11 × 13, d'où le même demi-tour 10³ ≡ −1 : 142 + 857 = 999 et 076 + 923 = 999. Seul le facteur q² − q + 1 a ses chiffres dans les unités modulo b − 1 (le lemme). Ceux de 13 sont {0, 2, 3, 6, 7, 9} (A) : on y lit 10 ≡ −3 (mod 13), l'autre racine sixième.

**La raison géométrique** (ma lecture, vérifiée (A)). Dans l'anneau de Gauss, b = N(q + i) = q² + 1 : c'est le carré de la longueur de l'aiguille (q, 1) sur la grille carrée (XIX § 2). Dans l'anneau d'Eisenstein, avec N(a + bω) = a² − ab + b², p = N(q + ω) = q² − q + 1 : c'est le carré de la longueur de la même aiguille sur la grille décalée (XV § 5). Pour q = 3 : 10 = N(3 + i) et 7 = N(3 + ω). De plus (3 + ω)² = 8 + 5ω est le triangle 5-7-8 de XV § 5 (5² + 8² − 5·8 = 7²), comme (2 + i)² = 3 + 4i est le triangle 3-4-5. L'autre premier de période 6 en base 10, 13 = N(3 − ω) = q² + q + 1, est la même aiguille vue de l'autre côté. Modulo b, q est un quart de tour ; modulo p, q est un sixième de tour (q³ ≡ −1 : une racine primitive sixième de l'unité). **K3 est donc la même aiguille (q, 1) lue sur deux grilles.** Ce qui reste ouvert : le corpus ne dit nulle part « ω modulo p », l'analogue hexagonal de « i modulo b » (§ 6.2).

**L'obstruction de K3.** La famille ne se recolle à la fiche 013 que pour q = 2 et q = 3. Pour q ≥ 5, elle donne encore l'ensemble des chiffres (lemme), mais plus la période pleine.

### 3.3 Midy est un demi-tour, et les périodes forment une tour (T6 et T6b, question 4)

**Le demi-tour** *(démontré ; classique)*. Soit p un premier qui ne divise pas la base b, et L = ord_p(b) la période de 1/p. Si L = 2h, alors b^h est une racine carrée de 1 différente de 1 dans le corps ℤ/p, donc b^h ≡ −1. Les deux moitiés de la période s'ajoutent alors en b^h − 1, c'est-à-dire en chiffres tous égaux à b − 1 : c'est le théorème de Midy. Le demi-tour −1 est le miroir d ↦ (b − 1) − d. `resultats/recueil_verifications.md` § 5 le vérifie pour les 49 premiers de période paire entre 7 et 397, et pour 375 découpages en blocs (R). Ces deux vérifications contrôlent un théorème, elles ne découvrent rien : pour L = k·h avec k ≥ 2, la période A = (b^L − 1)/p est un multiple de b^h − 1, parce que (b^L − 1)/(b^h − 1) = 1 + b^h + … + b^((k−1)h) est divisible par p (p ne divise pas b^h − 1, puisque h < L). La somme des k blocs est congrue à A modulo b^h − 1, donc multiple de b^h − 1 *(démontré ici)*. Pour k = 2, elle vaut exactement b^h − 1 ; pour k ≥ 3 le multiple peut être plus grand, comme dans 0588 + 2352 + 9411 + 7647 = 19 998 = 2 × 9 999 pour 1/17 (R : `resultats/octaedre_perron_venn.md` § 3.4). C'est le cas général que traitent Ginsberg (2004, trois blocs), Gupta et Sury (2005, à vérifier) et Lewittes (2007) *(P, § 6.3)*.

**Le quart de tour** *(démontré)*. Si 4 | L, alors b^(L/4) est un i modulo p : son carré est b^(L/2) ≡ −1, et il faut p ≡ 1 (mod 4). Exemples *(A)* : 10⁴ ≡ 4 (mod 17), 10² ≡ 27 (mod 73), 10 ≡ 10 (mod 101), 10² ≡ 100 (mod 137). Sous 10⁶, 26 109 des 78 496 premiers (hors 2 et 5) ont 4 | L : une part de 0,3326 *(A)*. C'est un tiers des premiers, ou les deux tiers de ceux qui valent 1 modulo 4 : modulo les autres premiers ≡ 1 (mod 4), un i existe, mais ce n'est pas une puissance de 10. Le corpus a ce lien pour p = 17 seulement (XXVIII § 3.6 : 10⁴ ≡ 4 ≡ i et 10⁸ ≡ −1) ; la règle générale « 4 | L donne un i dans l'orbite de la base » n'y est pas, et `resultats/recueil_verifications.md` § 5 ne parle que du demi-tour.

**La tour des étages** *(démontré ; mesuré (R) § 4.6 de `resultats/revision_001.md`, recalculé (A))*. Écrivons p − 1 = 2^e·m et b = g^k pour une racine primitive g. Alors v₂(L) = e − min(v₂(k), e). Les premiers ont e = j avec la part 2^(−j) (j ≥ 1), et v₂(k) = j′ avec la part 2^(−(j′+1)), indépendamment l'un de l'autre pour une base « générique » (ni un carré, ni −1 fois un carré, ni ±2 fois un carré). D'où P(v₂(L) = 0) = Σ 2^(−e)·2^(−e) = 1/3 et P(v₂(L) = s) = (2/3)·2^(−s) pour s ≥ 1.

| étage v₂(L) | 0 | 1 | 2 | 3 | 4 | L pair |
|---|---:|---:|---:|---:|---:|---:|
| base générique, attendu | 1/3 | 1/3 | 1/6 | 1/12 | 1/24 | 2/3 |
| base 10, p < 10⁶ | 0,3334 | 0,3340 | 0,1660 | 0,0832 | 0,0417 | 0,6666 |
| base 3, p < 10⁶ | 0,3338 | 0,3338 | 0,1657 | 0,0832 | 0,0415 | 0,6662 |
| base 12, p < 10⁶ | 0,3330 | 0,3341 | 0,1660 | 0,0833 | 0,0415 | 0,6670 |
| base 2, attendu | 7/24 | 7/24 | 1/3 | 1/24 | 1/48 | 17/24 |
| base 2, p < 10⁶ | 0,2923 | 0,2916 | 0,3329 | 0,0417 | 0,0206 | 0,7077 |

À partir du premier étage, chaque étage garde la moitié du précédent : c'est la loi d'un arbre de Perron dont les fentes se referment de moitié *(ma lecture ; l'arbre est celui de XXVIII § 2)*. Les parts de ℓ | L valent ℓ/(ℓ² − 1) : 3/8, 5/24 et 7/48, mesurées 0,376, 0,208 et 0,146 pour ℓ = 3, 5, 7 (R, § 4.6). La preuve est la même, avec P(v_ℓ(p − 1) = e) = ℓ^(−e) et P(ℓ ∤ L | e) = ℓ^(−e) : P(ℓ | L) = Σ ℓ^(−e)(1 − ℓ^(−e)) = ℓ/(ℓ² − 1) *(démontré ici ; Hasse l'avait donné pour ℓ impair)*. Le plan écrivait « à vérifier dans la littérature » : c'est le résultat de Hasse (1965/66) pour ℓ impair et de Hasse (1966) pour ℓ = 2.

**Pourquoi la base 2 est à part** *(classique ; démontré ici)*. Le caractère quadratique (2/p) est fixé par p modulo 8 : 2 est un carré exactement si p ≡ ±1 (mod 8). Cela impose v₂(k) ≥ 1 pour ces p, et change la tour. Le calcul (quatre lignes) donne 7/24, 7/24, 1/3, puis 2^(−s)/3 pour s ≥ 3, et L pair avec la densité 17/24 : c'est le résultat de Hasse (1966). Le même calcul fournit trois autres densités, selon ce que le caractère quadratique (b/p) est en fonction de p :

| le caractère quadratique de b est | toujours +1 (b est un carré) | celui de −1, (−1/p) | celui de ±2, (±2/p) | libre (sans lien avec p modulo 8) |
|---|---:|---:|---:|---:|
| densité de L pair | 1/3 | 5/6 | 17/24 | 2/3 |
| rapport à 2/3 | 1/2 | 5/4 | 17/16 | 1 |

*(démontré ici. On conditionne la tour sur (b/p) ; les puissances quatrièmes et suivantes de b restent génériques. Si b est un non-carré, L est pair d'office. Si b est un carré, v₂(k) ≥ 1 et P(L pair | e) = 1 − 2^(−(e−1)). Pour (b/p) = (−1/p) : p ≡ 3 (mod 4) donne un non-carré, p ≡ 1 (mod 4) un carré, d'où 1/2 + Σ_{e≥2} 2^(−e)·(1 − 2^(−(e−1))) = 5/6. Pour (±2/p), p modulo 8 décide, d'où 17/24. Le « −1 » du tableau ne veut pas dire b = −1, car alors L vaudrait 2 : seul le caractère quadratique de b est celui de −1.)*

**T6b : l'enchevêtrement du Venn de Midy** *(démontré pour la règle, calculé (A) pour les nombres)*. Le plan prévoyait de mesurer les parts. Je mesure en plus la loi jointe de « 2 | L » et « ℓ | L », par R(2, ℓ) = P(2 | L et ℓ | L)/(P(2 | L)·P(ℓ | L)). Si les deux événements étaient indépendants, on aurait R = 1. La règle de la réciprocité quadratique dit quand ce n'est pas le cas : ℓ | L force p ≡ 1 (mod ℓ). Si ℓ divise la partie sans carré s de la base, s = ℓ·c, alors (s/p) = (ℓ/p)·(c/p), avec (ℓ/p) = 1 si ℓ ≡ 1 (mod 4) et (ℓ/p) = (−1/p) si ℓ ≡ 3 (mod 4). Le caractère (b/p) est donc celui de c (si ℓ ≡ 1 mod 4) ou de −c (si ℓ ≡ 3 mod 4), et le tableau des densités ci-dessus donne R.

| (b/p) sachant que ℓ divise L | exemples (base, ℓ) | R attendu | R mesuré, p < 3·10⁶ |
|---|---|---:|---|
| toujours +1 | (5, 5), (13, 13) | 1/2 | 0,499 ; 0,503 |
| celui de −1 | (3, 3), (12, 3), (7, 7), (11, 11) | 5/4 | 1,251 ; 1,252 ; 1,250 ; 1,247 |
| celui de ±2 | (10, 5), (6, 3), (14, 7) | 17/16 | 1,063 ; 1,062 ; 1,061 |
| libre | les 46 autres couples (11 bases, ℓ = 3, 5, 7, 11, 13) | 1 | de 0,995 à 1,006 |

L'écart maximal entre les 55 rapports mesurés et la règle est de 0,006 (A, § 7.1). Le « Venn de Midy » de l'auteur (CLAUDE.md § 10 : « une suite de Venn dimensionnelle, ascendante et descendante ») devient donc : une tour d'étages dont les parts se divisent par deux, des tours indépendantes pour chaque ℓ impair, et un seul recollement entre elles, que la réciprocité quadratique fixe. Les aires sont inégales par nature (2/3 contre 1/3), et pas seulement pour la base 2.

**Le miroir de 1/17** (XXVIII § 3.6 ; R : `resultats/octaedre_perron_venn.md` § 3.4). Ici p − 1 = 16 = 2⁴ et 10 est une racine primitive, donc v₂(L) = 4 : c'est l'étage le plus haut possible. La tour est entière : 10⁸ ≡ −1 (le demi-tour), 10⁴ ≡ 4 ≡ i (le quart de tour), 10² ≡ 15 ≡ −2 (le huitième), 10 (le seizième). Les périodes de Gauss « en 2, 4 et 8 classes » du 17-gone (R) sont les orbites des sous-groupes ⟨10⟩ ⊃ ⟨10²⟩ ⊃ ⟨10⁴⟩ ⊃ ⟨10⁸⟩, d'indices 1, 2, 4 et 8 *(démontré : (ℤ/17)* est cyclique d'ordre 16)*. Le miroir 05882352 + 94117647 = 99999999 est le demi-tour, comme pour 1/7 (142 + 857 = 999). 17 est un premier de Fermat, 2^(2²) + 1 : c'est pour cela que la tour de 17 est une chaîne pure de ℤ/16. Pour un premier p = 2^e·m + 1, la tour est pleine (v₂(L) = e) exactement quand b n'est pas un carré modulo p, donc pour la moitié des cas ; 17 en fait partie *(démontré)*.

### 3.4 T7 : les trois 4/3 sont une coïncidence de petits entiers, mais le compte des puissances a une loi (question 5)

**Le compte** *(R : `resultats/recueil_verifications.md` § 2)*. c_a(b) est le nombre de puissances a⁰, a¹, … strictement inférieures à b : c_a(b) = ⌈log_a b⌉ pour b ≥ 2. En base 10 : c₂ = 4 (1, 2, 4, 8) et c₃ = 3 (1, 3, 9). Le rapprochement avec V₃/V₂ = 4/3 et avec 1/x₀ = n + 4/3 est dit « à tester » (CLAUDE.md § 10).

**Théorème** *(démontré ; vérifié (A) pour b ≤ 3·10⁶)*. c₂(b)/c₃(b) = 4/3 si et seulement si b ∈ [10, 16] ou b ∈ [244, 256].

*Preuve.* c₂/c₃ = 4/3 exige (c₂, c₃) = (4k, 3k). Alors 2^(4k−1) < b ≤ 2^(4k) et 3^(3k−1) < b ≤ 3^(3k). Ces deux intervalles se coupent si et seulement si 2^(4k−1) < 3^(3k) (toujours vrai) et 3^(3k−1) < 2^(4k), c'est-à-dire (27/16)^k < 3. Or (27/16)^k vaut 1,69 ; 2,85 ; 4,80 pour k = 1, 2, 3. Donc k = 1 (b de 10 à 16) et k = 2 (b de 244 à 256). ∎

**La loi générale** *(démontré ici ; vérifié (A))*. Le même argument vaut pour tout rapport r/s en termes minimaux : (c₂, c₃) = (r·k, s·k) est possible si et seulement si (2^r/3^s)^k < 2 et (3^s/2^r)^k < 3. Avec ρ = s·ln 3 − r·ln 2, le nombre de fenêtres de b est ⌊ln 3/ρ⌋ si ρ > 0, et ⌊ln 2/|ρ|⌋ si ρ < 0.

| r/s | s·ln 3 − r·ln 2 | nombre de fenêtres | première fenêtre de b |
|---|---:|---:|---|
| 4/3 | +0,52325 | 2 | [10, 16] puis [244, 256] |
| 3/2 | +0,11778 | 9 | [5, 8] |
| 8/5 | −0,05212 | 13 | [129, 243] |
| 19/12 | +0,01355 | 81 | [262 145, 524 288] |
| 65/41 | −0,01146 | 60 | [2⁶⁴ + 1, 3⁴¹] |
| 84/53 | +0,00209 | 526 | [2⁸³ + 1, 2⁸⁴] |

Les rapports qui se répètent sur de très nombreuses fenêtres sont exactement les réduites de log₂ 3 : 3/2, 8/5, 19/12, 65/41, 84/53 *(A : listes exactes en entiers, § 7.1)*. Pour 19/12, ρ = ln(3¹²/2¹⁹) est le logarithme du comma pythagoricien. Le rapport 4/3 n'est pas une réduite de log₂ 3 : il tient sur deux fenêtres, parce que 27/16 est un mauvais rapport. **La coïncidence est donc petite, et la loi qui reste est celle du comma** *(démontré ; le plan, K8, disait seulement que « le compte des puissances sous b rejoint l'arbre P6 »)*.

**La limite log₂ 3 a déjà un nom dans le corpus.** VI § 3 ter écrit : « la dimension, c'est le nombre de fois qu'une base entre dans une autre », et la rattache à la dimension d'autosimilarité d = log N / log s (Cantor : log 2/log 3 ; dix copies réduites de moitié : log₂ 10 = 3,32). Or c_a(b) est exactement le nombre de fois que a entre dans b. Le rapport c₂/c₃ tend donc vers log₂ 3 : c'est d pour N = 3 copies réduites de moitié (s = 2), la dimension du triangle de Sierpiński *(démontré ; classique pour le triangle)*. C'est le même log₂ 3 que celui du comma (XX § 6) et que celui des réduites ci-dessus.

**Les deux autres 4/3.** V₃/V₂ = (4π/3)/π = 4/3 est un pas de Wallis : V_(n+1)/V_n = ∫_(−1)^1 (1 − t²)^(n/2) dt tend vers 0 (partie III ; R : `resultats/revision_001.md` § 4.5). Pour n = 2 : ∫(1 − t²) dt = 2 − 2/3 = 2(1 − 1/3). Le 4/3 de 1/x₀ = n + 4/3 − 112/(45n) + … est une constante de la série de la corde : 1 pour le simplexe, 1/3 pour le ménisque (XXIV ; `resultats/tiers_dimension.md` § 2). Il ne dépend pas de n. Aucune loi ne relie donc c₂/c₃ (qui tend vers log₂ 3 = 1,585) à V_(n+1)/V_n (qui tend vers 0) ni à la constante 4/3 (qui reste 4/3 pour tout n). Il y a pourtant un point commun, que je note sans le tester : le 1/3 de Wallis est ∫₀¹ u² du, et le 1/3 de la corde vient du terme −k·τ³/3 de ∫₀^τ (1 − u²)^k du (XXIV § 1, pas 2), donc de ∫₀^τ u² du aussi. Le signe est renversé dans la corde par la coquille, E[τ³] = −2/n³ (XXIV § 1, ordre 2) : 2(1 − 1/3) d'un côté, n + 1 + 1/3 de l'autre *(ma lecture, non testée)*. **Verdict : coïncidence de petits entiers, répliquée sur les bases de 3 à 3 000 000 : deux fenêtres seulement** (statut « hasard », testé). **Ce qui reste, et qui est exact** : le lien de log₂ 3 avec le comma, par les réduites de l'arbre P6 (§ 3.5).

### 3.5 Les réduites et les trois distances : un seul théorème (question 6)

**Ce que dit déjà le corpus.** Chaque partie dit que ce qu'elle voit est « le théorème des trois distances de la partie XI » : XIV § 1 (« l'angle du 3-4-5 joue le rôle de l'angle d'or », « exactement l'escalier des trous de l'angle d'or »), XV § 5 (« c'est encore le théorème des trois distances »), XIX § 4, XX § 6 et XXVI § 2.5. La réponse à la question 6 est donc oui : c'est un seul théorème, et le corpus le sait déjà, partie par partie. Ce qu'il ne fait pas, c'est écrire la forme quantitative, qui donne les comptes et les longueurs, et dire que le diésis et le comma en sont des écarts.

**Le théorème** *(classique (P) : Steinhaus (conjecture), Sós, Surányi et Świerczkowski (1958) ; la forme avec les réduites : Alessandri et Berthé (1998) ; vérifié (A) pour N = 2 à 150 et cinq valeurs de α)*. Soit α irrationnel, de réduites p_k/q_k et de quotients partiels a_k. Posons η_k = |q_k·α − p_k|, avec q₋₁ = 0 et η₋₁ = 1. Si N = m·q_k + q_(k−1) + r, avec 1 ≤ m ≤ a_(k+1) et 0 ≤ r < q_k, les N points {j·α}, 0 ≤ j < N, découpent le cercle en N intervalles :
- N − q_k de longueur η_k ;
- r de longueur η_(k−1) − m·η_k ;
- q_k − r de longueur η_(k−1) − (m − 1)·η_k.

La plus grande longueur est la somme des deux autres. Il n'y a que deux longueurs exactement quand r = 0. (Alessandri et Berthé comptent N + 1 points, ce qui change r en r + 1.) La théorie musicale des gammes « bien formées » (Carey et Clampitt 1989) emploie le même théorème : une gamme engendrée par un seul intervalle a deux tailles de pas si et seulement si son nombre de notes est un dénominateur de réduite ou de semi-réduite du générateur *(P ; la caractérisation par les semi-réduites m'est connue par un extrait : à vérifier)*. Mes comptes concordent : pour la quinte (α = log₂ 3 − 1), deux longueurs pour N = 2, 3, 5, 7, 12, 17, 29, 41, 53 et 94 jusqu'à 120, trois pour N = 6, 8 et 13 ; pour log₁₀ 2, deux longueurs pour N = 2, 3, 4, 7, 10, 13, 23, … *(A)*.

**Le corpus, cas par cas** *(R pour ce que chaque partie lit ; A pour la lecture avec la formule)*.

| partie | le tour α | les N points | ce que la partie lit | ce que la formule ajoute |
|---|---|---|---|---|
| XI § 2 | 1/φ² = 0,382 | N = 2 à 60 | deux longueurs exactement pour N = 2, 3, 5, 8, 13, 21, 34, 55 ; toutes en 360°/φᵏ | a_k = 1 pour tout k, donc m = 1 et r = 0 si et seulement si N est un nombre de Fibonacci |
| XIV § 1 | arctan(4/3)/90° = 0,5903 | 2k + 1 directions du cercle de rayon 5ᵏ | 90 − 53,13 = 36,87 ; 53,13 − 36,87 = 16,26 ; 36,87 − 16,26 = 20,61 ; … | 2k + 1 multiples consécutifs de 53,13° modulo 90° : N = 3, 5, 7 |
| XIV § 3 | 1/φ | les aiguilles de Fibonacci | déterminant ±1 (Cassini), angle × longueur² → 1/√5 (Hurwitz) | ce sont les couples (q_k, η_k) : p_(k+1)·q_k − p_k·q_(k+1) = ±1 est ce qui rend la formule exacte |
| XV § 5 | arg(8 + 5ω) = 38,21° = arccos(11/14) | les directions de longueur 7ᵏ sur la grille décalée | « les trous n'ont jamais plus de trois longueurs » | même théorème ; (3 + ω)² = 8 + 5ω |
| XIX § 4 | log₁₀ 2 = 0,30103 | N = 10 et 93 | « 2 aux dénominateurs des réduites (10 et 93 points) » | incomplet : voir ci-dessous |
| XX § 6 | log₂ 3 − 1 = 0,58496 | 5, 7 et 12 notes ; 6 et 8 notes | « deux tailles de pas : 90,22 et 113,69 cents pour 12 » ; « trois » pour 6 ou 8 | N = 12 : (7, 0, 5) ; N = 13 : (8, 1, 4) |
| XXVI § 2.5 | log₁₀ 2 | N = 21 crans | 11 × 128/125, 8 × 625/512, 2 × 5/4 | N = 21 = 1·10 + 3 + 8 : (N − q, r, q − r) = (11, 8, 2) |

**Le diésis et le comma sont des écarts η** *(démontré ; calculé (A))*. Pour α = log₁₀ 2, les réduites donnent q₁ = 3 et q₂ = 10, et η₁ = log₁₀(5/4), η₂ = |10·log₁₀ 2 − 3| = log₁₀(1024/1000) = log₁₀(128/125). Le diésis est donc le plus petit écart, η₂, au dénominateur 10. Pour N = 21 = 1·10 + 3 + 8, les longueurs sont η₂ (11 fois), η₁ − η₂ = log₁₀(625/512) (8 fois) et η₁ = log₁₀(5/4) (2 fois) : exactement la table de XXVI § 2.5, qui devient une conséquence de la formule. Les autres lignes du tableau de `resultats/kakeya_miroir.md` § 2.4 (4, 11 et 94 crans) en sont aussi des cas : N = 94 = 9·10 + 3 + 1 donne (84, 1, 9), c'est-à-dire 84 fois 128/125, une fois 5²⁸/2⁶⁵ et 9 fois 5²⁵/2⁵⁸ *(R pour le tableau ; A pour la formule)*. La règle « la plus grande est la somme des deux autres » est, en logarithmes, la ligne que XXVI § 2.5 écrit en rapports : 5/4 = (128/125)·(625/512). Pour N = 10 (r = 0), il n'y a que deux longueurs, log₁₀(5/4) (7 fois) et log₁₀(32/25) (3 fois), et leur rapport est le diésis : (32/25)/(5/4) = 128/125.

Pour α = log₂ 3 − 1, les réduites sont 1/1, 1/2, 3/5, 7/12, 24/41, 31/53, … (les q valent 1, 2, 5, 12, 41, 53). Les deux écarts de la gamme à 12 notes sont η₃ = |5α − 3| = log₂(256/243) (le limma, 90,22 cents) et η₂ − η₃ = log₂(2187/2048) (l'apotome, 113,69 cents). **Le comma pythagoricien est η₄ = |12α − 7| = log₂(3¹²/2¹⁹) : c'est le troisième écart, qui apparaît à la treizième note** (N = 13 : une fois 23,46 cents, huit fois le limma, quatre fois l'apotome ; c'est la sortie de ma formule, 8, 1, 4 pour N = 13). Il vaut aussi le rapport apotome/limma = 531441/524288.

**Deux écarts, un procédé.** Le comma est au dénominateur 12 (7/12 de tour), le diésis au dénominateur 10 (3/10 de tour). Les deux se lisent de la même façon ; seule la paire de nombres change : 2 et 3 pour le comma (la couche 1 de CLAUDE.md § 3), 2 et 5 pour le diésis, parce que 10 = 2·5 (XXVI § 2.1). C'est le résultat que la règle de CLAUDE.md § 1 demande : le procédé est partagé exactement (le théorème), ce que la correspondance transporte est la formule (comptes et longueurs), et ce qui reste ouvert est la version pour plusieurs rotations à la fois.

**Ce que le corpus avait d'incomplet** *(fait établi, voir § 6.2)*. XIX § 4 (`bases-objets.md`, ligne 195) écrit « 2 aux dénominateurs des réduites (10 et 93 points) » ; `resultats/bases_objets.md` § 3 (ligne 92) écrit « Deux longueurs seulement aux dénominateurs des réduites (10, 93) ». C'est vrai, mais il y a deux longueurs pour toutes les valeurs N = m·q_k + q_(k−1) : pour log₁₀ 2 et N < 120, ce sont N = 2, 3, 4, 7, 10, 13, 23, 33, 43, 53, 63, 73, 83, 93 et 103 *(A)*. Les réduites ne sont que les extrémités des séries (3, 10, 93, …).

**Ce qui reste ouvert.** Le théorème vaut pour une rotation d'un cercle, un seul α. Pour L composé, par exemple 65 = 5 × 13, les directions de XIV § 1 sont des multiples de deux angles indépendants (arctan(1/2) et arctan(2/3)) : ce n'est plus une orbite d'une seule rotation, et la table de XIV § 1 (1, 3, 3, 5, 9, 27, 45 directions par quart de tour) n'est pas un cas du théorème *(ma lecture)*. Je n'ai pas cherché de version à plusieurs rotations ou en dimension supérieure *(ouvert)*.

### 3.6 Les premiers par position (question 7 et 8)

**Le dernier chiffre** *(R : `resultats/recueil_verifications.md` § 6 ; recoupé (A) avec les tables publiées)*. Hors 2 et 5, tout premier finit par 1, 3, 7 ou 9 : les quatre éléments du groupe (ℤ/10)* = ⟨3⟩, l'horloge 1 → 3 → 9 → 7 de XIX § 2. Dirichlet (classique) dit que chaque classe reçoit un quart des premiers. Mes comptes coïncident, à chaque puissance de 10 de 10³ à 10⁹, avec ceux de la table publiée OEIS A073505 à A073508 *(A ; P, § 6.3)* : à 10⁹, 12 711 386 ; 12 712 499 ; 12 712 314 ; 12 711 333 pour 1, 3, 7, 9.

**La face du cube est exacte** *(R : fiche 015)* : 10a + u ≡ a + u (mod 3), donc a ≡ 0 laisse {1, 7}, a ≡ 2 laisse {3, 9}, a ≡ 1 laisse les quatre. C'est la roue de 30 lue par dizaines : (ℤ/30)* ≅ ℤ/2 × ℤ/4 a huit éléments, deux (a ≡ 0), quatre (a ≡ 1) et deux (a ≡ 2), et ×7 est un quart de tour d'ordre 4 modulo 30 (1 → 7 → 19 → 13 → 1 ; 11 → 17 → 29 → 23 → 11) *(démontré)*. **Les quadruplets** de la fiche 015 (165 sous 10⁶, tous avec a ≡ 1) sont les quadruplets premiers (p, p + 2, p + 6, p + 8), que compte une table publiée (MathWorld, d'après Nicely ; OEIS A050258, numéro à vérifier) : 1, 2, 5, 12, 38, 166, 899 et 4 768 sous 10 à 10⁸. Mes décomptes de dizaines, plus un pour {5, 7, 11, 13}, redonnent les six derniers nombres : 5, 12, 38, 166, 899, 4 768 *(A ; P pour la table)*.

**La symétrie de la table des 16 motifs** *(R : `resultats/recueil_verifications.md` § 6 ; lecture (A))*. La table est symétrique par 1 ↔ 9 et 3 ↔ 7, c'est-à-dire par x ↦ −x, le demi-tour de l'horloge de 10 : {3} 10 709 contre {7} 10 681 ; {1} 10 660 contre {9} 10 644 ; {1, 7} 4 208 contre {3, 9} 4 216 ; {1, 3} 1 515 contre {7, 9} 1 493 ; {1, 7, 9} 556 contre {1, 3, 9} 542 ; {3, 7, 9} 520 contre {1, 3, 7} 514. Le quart de tour ×3 n'est pas une symétrie : il enverrait {1, 3} sur {3, 9}, qui valent 1 515 et 4 216. Le 3 de « modulo 3 » le casse. Ce que le demi-tour conserve, c'est la symétrie n ↦ −n de la série singulière de Hardy et Littlewood *(ma lecture)*.

**Ce que le test 4.2 de la session change pour la fiche 015** *(question 7 ; R : `resultats/revision_001.md` § 4.2 ; A pour la suite)*.
1. **« Près de trois fois » est une valeur à taille finie.** Le rapport par motif vaut 3,90 à 10⁴, 3,14 à 10⁵, 2,83 à 10⁶, 2,63 à 10⁷, 2,53 à 10⁸ (R), et 2,44 à 10⁹ (A). La fiche doit dire « 2,8 à 10⁶, 2,4 à 10⁹, 2 à la limite (conjecture de Hardy et Littlewood) ».
2. **Les paires larges sont stables.** À 10⁸, les paires {1, 3}, {7, 9}, {3, 7} et {1, 9} (distances 2, 2, 4, 8) comptent 146 841 ; 146 953 ; 146 720 ; 146 459, égales à 0,35 % près ; les paires {1, 7} et {3, 9} (distance 6) comptent 293 573 et 293 080, soit le double (A). C'est S(6)/S(2) = (3 − 1)/(3 − 2) = 2 : la distance 6 est divisible par 3, les distances 2, 4 et 8 par aucun premier impair. À 10⁹ : 1 141 217 ; 1 142 128 ; 1 141 545 ; 1 140 858 contre 2 283 666 et 2 282 637 (A).
3. **La dérive n'est pas une loi en 1/ln N à constante fixe.** (R − 2)·ln N vaut 17,5 ; 13,2 ; 11,5 ; 10,2 ; 9,7 et 9,2 de 10⁴ à 10⁹ (A, arithmétique sur (R) et le nouveau point) : le produit baisse de moitié. La session écrit « en 1/ln N » ; c'est juste à l'ordre dominant seulement.
4. **La dérive est exactement la prédiction de Hardy et Littlewood à taille finie** *(calculé (A), conjecture H–L)*. Dans une dizaine, la densité de k premiers est T_k/ln(n)^k, avec T_k = (2·(5/4)·(3/2))^k·∏_(p≥7) (1 − k/p)/(1 − 1/p)^k (2, 5 et 3 sont fixés par n = 10a et la classe de a modulo 3). Un motif exact s'obtient par inclusion–exclusion. On trouve T₂ = 13,2032 (soit 10·2C₂), T₃ = 42,87, T₄ = 124,5. Le rapport par motif vaut alors 1 + ΣB/ΣF, avec B = T₂/L² (une paire sur sa face) et F = B − 2T₃/L³ + T₄/L⁴ (une paire sur la face a ≡ 1, les deux autres composés), L = ln n. Le résultat, sans aucun paramètre ajusté :

| N | observé | Hardy–Littlewood à N fini |
|---|---:|---:|
| 10⁴ | 3,8969 | 4,1979 |
| 10⁵ | 3,1448 | 3,2370 |
| 10⁶ | 2,8321 | 2,8535 |
| 10⁷ | 2,6306 | 2,6523 |
| 10⁸ | 2,5255 | 2,5286 |
| 10⁹ | 2,4442 | 2,4447 |

L'écart entre le modèle et l'observé passe de 0,30 (à 10⁴) à 0,0005 (à 10⁹). La limite est bien 2, approchée comme 2·T₃/T₂/ln N = 6,494/ln N au premier ordre, mais le second ordre est grand : à 10¹², le modèle donne 2,30 ; à 10²⁰, 2,16 ; à 10¹⁰⁰, 2,03 (A). **La dérive de la fiche 015 est donc la correction de taille finie de la conjecture, pas un défaut du modèle. Ce que la conjecture a de testé : un rapport qui combine les six motifs de paires et trois ordres de corrélation (k = 2, 3, 4), à 0,02 % près à 10⁹ ; ce qu'elle a de non démontré : tout** *(Hardy et Littlewood 1923 ; elle implique la conjecture des jumeaux)*.

**La course de Tchebychev modulo 10** *(calculé (A) ; la fiche 015 ne la contient pas)*. Les classes 3 et 7 (les non-carrés de (ℤ/10)*, c'est-à-dire i et −i) devancent les classes 1 et 9 (les carrés, 1 et −1) *à chaque premier* jusqu'à 10⁹ : l'avance vaut 10, 9, 36, 76, 305, 485 et 2 094 aux puissances de 10 de 10³ à 10⁹ (A). Les valeurs publiées pour 10¹⁰, 10¹¹, 10¹² donnent +6 819, +759 et +41 792 *(P : arithmétique sur OEIS A073505 à A073508, à vérifier)*. C'est le biais de Tchebychev pour le module 5 (Rubinstein et Sarnak 1994) : (ℤ/10)* ≅ (ℤ/5)*. **Dans la base 12, où chaque unité est un reflet, la seule classe carrée est 1, et c'est la dernière à chaque premier jusqu'à 10⁹** (12 710 866 premiers ≡ 1 contre 12 712 625, 12 711 847 et 12 712 194 pour 5, 7 et 11 à 10⁹ ; A). En base 10 le biais favorise ±i ; en base 12 il pénalise 1. C'est la différence entre une horloge qui a un quart de tour et une qui n'en a pas.

**Le dernier chiffre dit où vit le nombre d'or modulo p** *(démontré ; calculé (A) pour p < 10⁶ ; lien nouveau avec IX, XI, XII)*. Pour p premier ≠ 2, 5 : (5/p) = 1 si p ≡ ±1 (mod 5), c'est-à-dire si p finit par 1 ou 9 ; (5/p) = −1 si p finit par 3 ou 7. Dans le premier cas, φ existe dans ℤ/p et p divise F_(p−1) ; dans le second, φ est dans F_(p²) et son conjugué −1/φ est son image par Frobenius, et p divise F_(p+1) (exemples : 11 | F₁₀ = 55 ; 19 | F₁₈ ; 7 | F₈ = 21 ; 13 | F₁₄ = 377). Pour les 78 496 premiers sous 10⁶, il n'y a aucun contre-exemple (A). Les premiers des classes 3 et 7, qui devancent dans la course de Tchebychev, sont donc exactement ceux modulo lesquels le nombre d'or n'existe pas. Le corpus n'a ni « résidu quadratique » ni « rang d'apparition » (recherche dans les fichiers .md du dépôt), mais XII § 3 construit, sans le nommer, le tableau des rangs d'apparition : le « nouveau facteur premier » de F_k est un premier p dont le rang k divise p − 1 (chiffres 1, 9) ou p + 1 (chiffres 3, 7). On y lit 11 au rang 10 (p − 1), 29 au rang 14 (14 divise 28), 89 au rang 11 (11 divise 88), 61 au rang 15 (15 divise 60), et 7 au rang 8 (p + 1), 13 au rang 7 (7 divise 14), 17 au rang 9 (9 divise 18) *(R pour le tableau de XII ; démontré pour la règle)*. C'est un lien nouveau entre la fiche 015 et les parties IX, XI et XII, par le même groupe (ℤ/10)* : l'élément 3 qui est i modulo 10 est l'élément de Galois de ℚ(ζ₁₀) qui envoie φ sur −1/φ (M1, § 5.2).

**Lemke Oliver et Soundararajan** *(P ; calculé (A))*. Les rapports « même chiffre après même chiffre » valent à 10⁸ : 0,7080 ; 0,6666 ; 0,6669 ; 0,7075 pour 1 → 1, 3 → 3, 7 → 7, 9 → 9, donc 17/24 = 0,7083 et 2/3 = 0,6667 à 0,0008 près. Ce sont les densités de Hasse (base 2 et base générique), à 0,001 près. **Ce n'est pas une loi**, parce que les rapports continuent de monter : 0,7327 ; 0,7015 ; 0,7010 ; 0,7329 à 10⁹ (A). Même leçon que 2√2 et π dans la dérive de la fiche 015 (R § 4.2) : une grandeur qui dérive lentement croise des constantes célèbres. Lemke Oliver et Soundararajan expliquent ces rapports par les k-uplets de Hardy et Littlewood et conjecturent qu'ils tendent vers 1 très lentement *(P)*. Une prépublication de Holt (2024, à vérifier : je n'ai lu que le résumé) y voit un effet de crible « transitoire ». La table complète 4 × 4 à 10⁸ est symétrique par (a → b) ~ (−b → −a) : 1 → 3 contre 7 → 9 : 1,2156 et 1,2169 ; 1 → 7 contre 3 → 9 : 1,2412 et 1,2405 ; 3 → 1 contre 9 → 7 : 0,9456 et 0,9446 ; 7 → 1 contre 9 → 3 : 1,0233 et 1,0249 *(A)*. C'est la même symétrie que celle des motifs de dizaine : « renverser l'ordre et prendre le demi-tour ».

**Les densités de Hasse** *(P ; démontré ici)*. 2/3 (base générique), 17/24 (base 2) et ℓ/(ℓ² − 1) sont retrouvées à 0,001 près (§ 3.3). Les tables que je connais ne donnent pas les rapports d'enchevêtrement R(2, ℓ) de T6b (17/16, 5/4, 1/2), qui sont pourtant des cas de la théorie de Kummer avec enchevêtrement (Wiertelak ; Moree 2005 ; Lenstra, Moree et Stevenhagen) *(P, à vérifier)*.

### 3.7 Ce qui reste ouvert

1. **La conjecture de Hardy et Littlewood** pour k = 2, 3, 4 : c'est elle qui explique la dérive de la fiche 015 et la limite 2, et elle n'est démontrée pour aucun k ≥ 2. Seul le côté « prédit à 0,02 % » est établi.
2. **Le nombre d'or comme élément de Galois et la course de Tchebychev** : l'explication que les non-résidus mènent (le terme des carrés de premiers dans la formule explicite) est classique pour le module 5 ; je n'ai pas relié ce terme au rang d'apparition de Fibonacci *(ouvert)*.
3. **Le « Venn de Midy » au-delà de la tour** : la tour et l'enchevêtrement de T6b sont démontrés. La lecture de l'auteur en « suite de Venn dimensionnelle ascendante et descendante par ellipses » est un cadre à définir : que serait une dimension, un étage, une ellipse ? *(ouvert)*.
4. **ω modulo p** : le corpus a « i modulo b » (XIX § 2) et pas son analogue hexagonal. Pour p = q² − q + 1 premier, q est une racine sixième primitive de l'unité, comme q est un i modulo q² + 1 *(démontré)*. La grille d'Eisenstein (XV) l'utilise sans le dire *(ma lecture)*.
5. **K5** : 17 est un premier de Fermat et le i de 17 est 4 ; mais le Venn de Henderson existe à 19 et 23, qui n'ont pas de i. Aucune transformation connue ne relie les deux 17 *(§ 5.3)*.
6. **La fiche 005** : la moitié exacte à 19 courbes reste sans cause. Fermat (2^(n−1) ≡ 1 mod n) rend la moitié *permise* pour tout premier n, avec ou sans i ; il ne la rend pas probable *(§ 4.2)*.
7. **La base 3 dans le plan** : ℤ[i]/(3) = F₉, dont le groupe multiplicatif est cyclique d'ordre 8 (1 + i est d'ordre 8). La fiche 014 n'a testé que √2 = ±i ; je ne connais aucune occurrence, dans le corpus, des huitièmes de tour de F₉ *(ouvert)*.
8. **Plusieurs rotations à la fois** dans le théorème des trois distances (§ 3.5), qui contrôleraient les directions de XIV § 1 pour L composé *(ouvert, non cherché)*.

## 4. Les fiches du dossier

Les cinq fiches sont des lectures du même groupe, (ℤ/b)* pour b = 10 ou ses voisins : 001 regarde les deux premiers de 10 (2 et 5), 013 les unités modulo 9 = 10 − 1, 014 le i et le corps F₉, 015 les unités modulo 10 et la face modulo 3, 005 les unités modulo n pour n premier (Fermat). Chaque entrée donne : le verdict proposé, les dimensions (la principale d'abord), le test, la partie qui portait déjà le lien, puis ce que le dossier ajoute. La dernière sous-section (§ 4.6) répond à la question 7 sur les liens entre les cinq fiches.

### 4.1 Fiche 001 : 2⁻¹⁷ s'écrit avec les chiffres de 5¹⁷

Fiche : `recueil/observations/001-2-moins-17-chiffres-de-5-puissance-17.md`.

- **Verdict proposé** : *exact*, et c'est une identité : 2⁻ʲ = 5ʲ·10⁻ʲ pour tout j. Le statut « exact » reste. Rien à répliquer : 17 n'a pas de rôle dans l'identité.
- **Dimensions** : D2 d'abord (bases et chiffres), puis D3 (le grain du ppm : 2⁻¹⁷ est l'aire moyenne d'une région du Venn à 17 courbes), puis D6 (ce 17 est celui du Venn).
- **Test** : précision poussée (CLAUDE.md § 10, tableau du choix du test : « une identité entre nombres réels »). C'est le bon test pour une identité ; ici elle est algébrique, et la preuve suffit.
- **La partie qui portait déjà le lien** : XXVI § 2.2 (« le miroir est un nombre exact : les chiffres de 5ʲ », avec 10⁶/2²⁰ = 0,95367431640625), et la remarque de CLAUDE.md § 10 sur « 2 et 5, de part et d'autre de la virgule ». La fiche cite elle-même XXVI et `resultats/recueil_verifications.md` § 7.

**Ce que le dossier ajoute.**
1. **Où tombe le premier chiffre.** Le nombre de zéros après la virgule dans 2⁻ʲ est j − (nombre de chiffres de 5ʲ) = j − ⌊j·log₁₀ 5⌋ − 1 = ⌈j·log₁₀ 2⌉ − 1. C'est la marche en 3, 3, 4 de CLAUDE.md § 3, gouvernée par la rotation d'angle log₁₀ 2 : le même cercle des décades que les trois distances (§ 3.5) et que la loi de Benford (XIX § 4). Pour j = 17 : 17 − 12 = 5 zéros, et 5¹⁷ = 762 939 453 125 a 12 chiffres *(démontré)*.
2. **Le lien avec la fiche 013.** 2·5 = 10 se lit de deux façons : à la virgule (2⁻ʲ = 5ʲ/10ʲ, fiche 001) et modulo 9, où 10 ≡ 1 : 5 ≡ 2⁻¹. Donc DR(5ⁿ) = DR(2⁻ⁿ) : les racines digitales de 5ⁿ (1, 5, 7, 8, 4, 2) sont celles de 2ⁿ (1, 2, 4, 8, 7, 5) parcourues à l'envers (R : `resultats/recueil_verifications.md` § 4) *(démontré, trivial)*. Ce que la fiche 013 appelle « les mêmes chiffres dans un autre ordre » est l'inversion x ↦ x⁻¹ dans (ℤ/9)*.
3. **Le lien avec la fiche 015.** Les chiffres des premiers évitent 2 et 5 (hors les deux premiers eux-mêmes) parce que 2 et 5 sont les facteurs de 10 : les quatre chiffres 1, 3, 7, 9 sont le groupe (ℤ/10)*.
4. **Le lien avec le diésis.** 128/125 = 2⁷·5⁻³ (XXVI § 2.1) est écrit avec les mêmes deux nombres ; il est le troisième écart du théorème des trois distances (§ 3.5). La fiche 002 (« (128/125) × la lumière du 17-gone ≈ 1 à 845 ppm », statut « hasard ») porte le même 128/125 : c'est pour cela que je la propose à ce dossier (§ 8).

### 4.2 Fiche 005 : un Venn à 19 courbes coupe ses croisements exactement en deux

Fiche : `recueil/observations/005-moitie-exacte-venn-19-ramp12h.md`. Le dossier `recueil/dossiers/moities-et-crans.md` (§ 4.1) l'analyse en détail : l'involution du complément, les 18 certificats, la probabilité 1/(dispersion). Je n'y reviens pas. Je ne donne que l'angle des congruences.

- **Verdict proposé** : *ouvert, compatible avec le hasard* (statut de la fiche inchangé). Du côté des bases, Fermat est une condition *nécessaire*, pas *sélective*.
- **Dimensions** : D6 d'abord (le Venn et ses symétries), puis D2 (Fermat, les congruences), puis D7 (le hasard testé).
- **Test** : coïncidence entre entiers, donc réplication (CLAUDE.md § 10). Les 12 certificats à 19 courbes servent de réplication, avec l'indépendance faible que note `recueil/dossiers/moities-et-crans.md`.
- **La partie qui portait déjà le lien** : XXVIII § 3.1 (Henderson : un Venn simple symétrique à n courbes demande n premier) et § 3.2 (Fermat dessiné : les 7 710 formes à 17 courbes), XXX § 2.5 et § 7.3 (la moitié, le 1,6 %).

**Ce que le dossier ajoute (D2).**
1. **Fermat rend la moitié permise, pour tout premier n.** La rotation d'ordre n agit sans point fixe sur les 2ⁿ − 2 croisements ; toute partie stable a donc un nombre de croisements divisible par n. La moitié 2^(n−1) − 1 est divisible par n si n est premier (Fermat). Pour n = 19 : 2¹⁸ − 1 = 262 143 = 19 × 13 797 *(démontré ; R : fiche)*. Cela vaut pour 11, 13, 17, 19, 23, avec ou sans i : c'est une condition nécessaire, que tous les premiers satisfont.
2. **Pas de i nécessaire (K5).** Les Venn simples symétriques sont connus ou construits pour n = 3, 5, 7 (≡ 3, 1, 3 modulo 4), 11, 13 (≡ 3, 1), 17, 19, 23 (≡ 1, 3, 3) (README de Dzoba, lu comme données ; R : `/home/user/dzoba/venn17/README.md`). Les deux familles, avec i (5, 13, 17) et sans i (3, 7, 11, 19, 23), existent. Rien ne distingue 19 de 17 par p modulo 4 *(R pour la liste ; ma lecture pour la conclusion)*. Il n'y a que huit valeurs, donc aucun test.
3. **Ce qui reste d'ouvert.** La cause de l'exactitude à 19 (une rampe de 12 h sur le paramètre λ, `ramp12h`, d'après la fiche) n'est pas arithmétique, ou je ne la vois pas.

### 4.3 Fiche 013 : les racines digitales de 2ⁿ et 5ⁿ parcourent les chiffres de la période de 1/7

Fiche : `recueil/observations/013-racines-digitales-de-2-et-5-et-periode-de-1-sur-7.md`.

- **Verdict proposé** : *exact, propre à la base 10, et expliqué*. La fiche dit « exact pour 7 ; la variation échoue pour 13 : propre à 7, mécanisme à trouver ». Le test 4.1 de la session l'a déjà ramenée à « exact, et propre à la base 10 ». Le mécanisme est maintenant trouvé (K3, § 3.2), et il se démontre pour toute base q² + 1.
- **Dimensions** : D2 d'abord ; puis D5 (le même 3 est la pente de l'aiguille (3, 1) de XIX § 2, et l'aiguille (3, 1) de XV § 5 sur la grille décalée) ; puis D7 (la variation du paramètre est la méthode).
- **Test** : variation du paramètre (CLAUDE.md § 10) : fait par la session (b de 3 à 60, p jusqu'à 400 : 3 cas, dont un non trivial, (10, 7)) et étendu ici à b ≤ 400, p ≤ 4 000 (mêmes trois cas) *(R § 4.1 ; A)*.
- **La partie qui portait déjà le lien** : XIX § 2 (3 ≡ i modulo 10, l'aiguille de pente i) et VI § 3 ter (10 − 1 = 3², « un motif propre à la base 10 dit quelque chose de vrai sur le nombre 10 »). XXII § 2 (3ⁿ ≡ 3, 9, 7, 1 mod 10) lit le même 3.

**Ce que le dossier ajoute.** La coïncidence de la fiche est trois faits indépendants (§ 3.2) : (a) les chiffres de 1/7 sont les unités modulo 9 (le lemme des chiffres) ; (b) la période de 1/7 est pleine, car 10 est une racine primitive modulo 7 ; (c) 2 engendre les unités modulo 9, car 2 est une racine primitive modulo 9 (ordre 6 = φ(9)). Les deux ensembles égaux de la fiche viennent de (a) + (b) d'un côté et de (c) de l'autre. Le seul (b, p) où les trois valent est (10, 7). Le piège de la variation (1/13) s'explique exactement : 13 est l'autre facteur de Φ₆(10) = 91 = 7 × 13 (§ 3.2) ; il a la même période et le même demi-tour (076 + 923 = 999), mais pas les mêmes chiffres. Le 3 de la piste de la fiche (« saute justement 3 et 6 ») est le q de la famille : les chiffres absents de 1/7 sont 0, 3, 6, 9 = k·q.

### 4.4 Fiche 014 : les fractions continues imaginaires

Fiche : `recueil/observations/014-fractions-continues-imaginaires.md`.

- **Verdict proposé** : *exact* (les quatre fractions sont justes à moins de 10⁻³⁰ sur 61 étages, R : `resultats/recueil_verifications.md` § 3). Ce que la fiche appelle « reste à préciser » se précise en deux points.
- **Dimensions** : D2 d'abord (les bases 2, 3, 10, 12 ; i), puis D1 (√2 et √3 sont des cordes), puis D5 (les réduites de √2 sont les aiguilles de Pell (1, 2), (2, 5), (5, 12) de la récursion d'argent, XVII).
- **Test** : précision poussée (c'est le bon test pour un nombre réel exact). La variation du paramètre n'a pas été faite : elle est ci-dessous.
- **La partie qui portait déjà le lien** : XIX § 2 (« 1 ≡ −1 ≡ i ≡ −i » en base 2 ; 3 ≡ i en base 10) et CLAUDE.md § 10 (« Les congruences de i », « les exposants 1/2 et 3/2 »).

**Premier point : le lien avec F₉ est exact, mais il porte sur 2^(3/2), pas sur (−2)^(3/2).** CLAUDE.md § 10 et `resultats/recueil_verifications.md` § 1 disent : en base 3, 2 ≡ −1, √2 = ±i, et 2√2 = −i dans F₉. C'est exact *(R)*. La fiche cite le lien de l'auteur sous la forme « (−2)^(3/2) ≡ −i modulo 3 » et signale elle-même qu'il « reste à préciser » : dans F₉, (−2)^(3/2) donne ±1. Voici la précision. −2 ≡ 1 modulo 3, et (−2)^(3/2) = −2√2·i = −(−i)·i = −1 dans F₉, une des deux valeurs ±1 *(démontré)*. Le −i appartient à 2^(3/2) = 2√2, pas à (−2)^(3/2). CLAUDE.md § 10 sépare d'ailleurs les deux liens : « 2√2 ≡ −i » pour la base 3, et « (−2)^(3/2) vers la base 12 » pour la base 12 ; la phrase de la fiche les réunit *(ma lecture)*. Je propose d'écrire « 2^(3/2) ≡ −i dans F₉ » dans la fiche : son statut ne change pas.

**Second point : le « 10 » et le « 12 » dans les fractions continues sont des termes de clôture.** 3√3 = √27 = [5 ; 5, 10] (R § 3) et 10 = 2·⌊√27⌋ : la période d'une racine carrée finit toujours par 2·⌊√N⌋. Je compte (a ≤ 30, e ≤ 5, √(aᵉ) non entier) : sur 75 nombres, 35 ont un 10 dans leur période (ou en partie entière) et 17 en ont un 12 *(A, § 7.3)*. Pour e = 3, le 10 apparaît pour a = 3, 11, 13, 15, 17, 19, 24, 26, 27, 29 : 3 est le plus petit, parce que ⌊3√3⌋ = 5, ce qui n'a rien à voir avec la base 10. Pour 12, rien dans [2 ; 1, 4] (2^(3/2)) ni dans sa forme « par défaut » (3 − 1/(6 − …)) ne le contient : 12 = 2·6 est le double du terme 6 de la forme par défaut, et c'est tout *(ma lecture)*. Le lien « (−3)^(3/2) vers la base 10 » reste donc, du côté des fractions continues, une lecture de l'auteur : l'arithmétique qui le soutient est celle de 3 ≡ i (mod 10) et de 27 ≡ −i (mod 10) (R : `resultats/recueil_verifications.md` § 1), pas celle des termes de la fraction.

**Ce qui est solide.** 1/(i·y) = −i/y : multiplier par i alterne ±i (R § 3). C'est un fait de F_p-algèbre aussi bien que de ℂ. La base 3 a, dans le plan, un groupe F₉* cyclique d'ordre 8 (1 + i est d'ordre 8) *(démontré)* : la fiche n'a vu que les quarts de tour de F₉.

### 4.5 Fiche 015 : les dizaines de premiers forment un Venn à 4 ensembles, et le reste modulo 3 choisit la face du cube

Fiche : `recueil/observations/015-dizaines-de-premiers-cube-et-reste-modulo-3.md`.

- **Verdict proposé** : *exact pour la face (10a + u ≡ a + u modulo 3), calculé pour les comptes, et structure pour la dérive* : la loi de l'écart est la prédiction à taille finie de Hardy et Littlewood (§ 3.6), calculée sans paramètre ajusté. La limite 2 reste une conjecture.
- **Dimensions** : D2 d'abord (les premiers par position, la roue de 30), puis D6 (le cube {0, 1}⁴ est un Venn à quatre ensembles ; l'ombre du cube de XXVIII), puis D7 (le hasard des premiers, la dérive qui croise des constantes).
- **Test** : exact pour la face ; pour les comptes, la variation du paramètre N (fait par la session, § 4.2) puis la loi de l'écart (ici).
- **La partie qui portait déjà le lien** : XXVIII § 3 (le cube {0, 1}ⁿ et ses deux ombres) pour le Venn à 4 ensembles ; XIX § 2 (l'horloge 1 → 3 → 9 → 7) pour les quatre chiffres. Pour la face modulo 3, c'est la règle de 3 par la somme des chiffres (VI § 3 ter : 10 − 1 = 3²).

**Ce que le test 4.2 de la session change** (question 7 ; § 3.6 pour le détail et les nombres) :
1. « Près de trois fois » devient « 2,8 fois à 10⁶, 2,4 fois à 10⁹, 2 à la limite (conjecturée) » : le rapport par motif dérive de 3,90 à 2,44 entre 10⁴ et 10⁹ *(R pour 10⁴ à 10⁸ ; A pour 10⁹)*.
2. Ce qui est stable est le rapport des paires larges : les distances 2, 4 et 8 comptent la même chose à 0,35 % près, la distance 6 le double (S(6)/S(2) = 2, parce que 3 divise 6 et aucun premier impair ne divise 2, 4 ni 8) *(A)*.
3. La dérive en 1/ln N est juste à l'ordre dominant seulement : (R − 2)·ln N baisse de 17,5 à 9,2. Le modèle de Hardy et Littlewood à taille finie la reproduit à 0,0005 près à 10⁹ *(A)*.
4. La table des 16 motifs est symétrique par le demi-tour x ↦ −x de l'horloge de 10 (1 ↔ 9, 3 ↔ 7), pas par le quart de tour ×3 : le 3 de « modulo 3 » le casse *(R pour les comptes ; ma lecture)*.
5. Les 165 quadruplets sous 10⁶ sont, avec {5, 7, 11, 13}, les 166 quadruplets premiers que compte la table publiée *(A ; P)*.

### 4.6 Les liens entre les cinq fiches (question 7)

| paire | lien | statut |
|---|---|---|
| 001–013 | 2·5 = 10 se lit à la virgule (2⁻ʲ = 5ʲ·10⁻ʲ) et modulo 9 (5 = 2⁻¹, DR(5ⁿ) = DR(2⁻ⁿ)) | démontré |
| 013–015 | la même congruence 10 ≡ 1 (mod 9) : modulo 9, elle donne les racines digitales (013) ; modulo 3, la face du cube (015 : 10a + u ≡ a + u). Les deux fiches sont la règle de 3 et de 9 par la somme des chiffres | démontré |
| 013–014 | le 3 : 3 ≡ i et 27 ≡ −i modulo 10 (K3, XIX), et 2√2 = −i dans F₉. Trois écritures de i, dans ℤ/10 et dans F₉ | exact dans ℤ/10 et dans F₉ ; faux dans ℤ/3 |
| 001–015 | les chiffres des premiers évitent 2 et 5, les facteurs de 10 | démontré |
| 005–015 | le Venn à 19 courbes et le Venn à 4 ensembles des dizaines : le quart de tour d'ordre 4 (×3) existe sur le cube {0, 1}⁴, alors que Henderson interdit un Venn simple à 4 courbes symétrique (4 n'est pas premier) | ma lecture |
| 005–013, 005–014, 001–014 | aucun lien trouvé | — |

Ce qui manque : une fiche qui mette 001, 013 et 015 sous la seule identité « 10 ≡ 1 (mod 9) et 2·5 = 10 », et des fiches pour les parties III à XXVIII de ce dossier, qui n'en ont aucune (§ 6.1).

## 5. Les congruences et les obstructions

Rappel du cadre (plan § 3.0) : deux résultats se recollent s'ils coïncident sur ce qu'ils partagent, à une transformation connue près. Ce qui ne se recolle pas est une obstruction, et désigne un trou.

### 5.1 Les congruences du plan que ce dossier touche

- **K3, 1/7, les racines digitales et i modulo 10 : la famille b = q² + 1.** *Se recolle* (démontré, § 3.2) : les quatre propriétés du plan, plus le lemme des chiffres, pour tout q ≥ 2. Les chiffres de la période de 1/p sont toujours les entiers non multiples de q de [1, b − 2] ; ils sont exactement les unités modulo b − 1 quand q est premier *et* que la période visite tous les restes. *Obstruction* (confirmée) : la période vaut 6, pas p − 1, dès que q ≥ 3 et p est premier ; elle remplit le groupe si et seulement si p − 1 ≤ 6, donc pour q = 2 et q = 3 seulement. *Verdict* : K3 se recolle entièrement sur q = 2, 3 et au niveau des chiffres pour tout q. Le piège de la fiche 013 (1/13) est l'autre facteur de Φ₆(10) = 91 = 7 × 13. Le plan notait « à noter comme nouvelle fiche (exact) » : c'est N1 et N2 (§ 6.1).
- **K5, le 17 de Henderson et le 17 de i.** *Obstruction établie par la théorie, confirmée.* Les Venn simples symétriques sont connus pour n = 3, 5, 7, 11, 13 et construits pour 17, 19, 23 (Dzoba) ; ceux qui ont un i (5, 13, 17) et ceux qui n'en ont pas (3, 7, 11, 19, 23) existent tous. Aucune transformation connue ne relie les deux 17. Je ne propose pas de test (huit valeurs de n).
- **K8, les trois 4/3.** *Obstruction confirmée et précisée* (§ 3.4) : le compte des puissances sous b vaut 4/3 sur deux fenêtres seulement, et tend vers log₂ 3 ; V_(n+1)/V_n tend vers 0 ; la constante 4/3 de 1/x₀ reste. *Ce qui se recolle* : le compte des puissances et les réduites de log₂ 3 (le nombre de fenêtres d'un rapport r/s est ⌊ln 3/ρ⌋ ou ⌊ln 2/|ρ|⌋, avec ρ = s·ln 3 − r·ln 2), et la limite log₂ 3 avec la dimension d'autosimilarité de VI § 3 ter.
- **K9, Midy pair et impair.** *Se recolle* (démontré, § 3.3) : la tour 2-adique des périodes, avec les parts 1/3, 1/3, 1/6, 1/12 pour une base générique (7/24, 7/24, 1/3, 1/24 pour la base 2), et ℓ/(ℓ² − 1) pour ℓ | L. *Obstruction* (confirmée, et précisée) : les aires sont inégales (2/3 et 1/3), et les deux événements « 2 divise L » et « ℓ divise L » sont indépendants, sauf quand la partie sans carré s de la base vaut ℓ ou 2ℓ. Alors R(2, ℓ) vaut 1/2, 5/4 ou 17/16, par la réciprocité quadratique.

### 5.2 Mes congruences

| id | éléments | transformation | se recolle jusqu'où | obstruction | test |
|---|---|---|---|---|---|
| M1 | IX § 4 (racines dixièmes de l'unité, φ), XIX § 2 (3 ≡ i mod 10), XI (angle d'or), course de Tchebychev mod 10 (§ 3.6), Fibonacci F_(p∓1) | l'élément σ₃ de Gal(ℚ(ζ₁₀)/ℚ) ≅ (ℤ/10)* = ⟨3⟩ | exact : σ₃(√5) = −√5, donc σ₃(φ) = −1/φ ; un premier p ≡ 3 ou 7 (mod 10) est inerte dans ℚ(√5) et divise F_(p+1) ; 1 ou 9, il divise F_(p−1) | pourquoi les inertes devancent dans la course : classique pour le module 5 (carrés de premiers), non relié ici à Fibonacci | exact (démontré) ; Fibonacci vérifié pour p < 10⁶ (§ 7.1) |
| M2 | XXVIII § 3.6 (1/17, 4 ≡ i, Gauss), `resultats/recueil_verifications.md` § 5 (Midy), T6 | b^(L/2) ≡ −1 et b^(L/4) ≡ i dans (ℤ/p)* | exact ; pour p = 17 la tour est entière (ℤ/16 ⊃ 2ℤ/16 ⊃ 4ℤ/16 ⊃ 8ℤ/16) | aucune | démontré |
| M3 | XI § 2, XIV § 1 et 3, XV § 5, XIX § 4, XX § 6, XXVI § 2.5 | le théorème des trois distances : α ↦ (N − q_k, r, q_k − r) | exact pour une rotation ; diésis = η₂ de log₁₀ 2, comma = η₄ de log₂ 3 | plusieurs rotations à la fois (L composé en XIV § 1) | démontré ; formule vérifiée N = 2 à 150, cinq α (§ 7.1) |
| M4 | XXI § 2 (7² ≡ −1 mod 50, Machin 239, Ljunggren), XVII (compagnons de Pell 1, 3, 7, 17, 41, 99, 239…), XIX § 2 | p² + 1 = 2q² : i ≡ p modulo b = 2q² | exact : b = 2, 50, 1 682, 57 122, 1 940 450, 65 918 162 ; deux écritures p² + 1² = q² + q² | aucune ; remarque : 239 est le seul p > 1 dont le q est lui-même un carré (Ljunggren : x² + 1 = 2y⁴) | exact (§ 7.3) |
| M5 | XIX § 2 (l'aiguille (3, 1), N = 10), XV § 5 (la même sur la grille décalée, N = 7), fiche 013 | l'aiguille (q, 1) lue dans ℤ[i] (norme q² + 1) et dans ℤ[ω] (norme q² − q + 1) | exact : (3 + ω)² = 8 + 5ω est le triangle 5-7-8 de XV § 5 | « ω modulo p », l'analogue hexagonal de « i modulo b », n'est dit nulle part | démontré (A) |
| M6 | VI § 3 ter (10 − 1 = 3², 10 + 1 = 11, 10 = 2·5), fiches 013 et 015 | 10 ≡ 1 (mod 9), 10 ≡ −1 (mod 11), 10 = 2·5 | exact : modulo 9, les racines digitales ; modulo 3, la face du cube ; modulo 11, le demi-tour de 1/11 | aucune | démontré |
| M7 | fiche 001 (2⁻ʲ = 5ʲ·10⁻ʲ), fiche 013 (5 ≡ 2⁻¹ mod 9) | x ↦ x⁻¹ | exact | aucune | démontré |
| M8 | VI § 3 ter (d = log N / log s), T7 (c₂/c₃ → log₂ 3), XX § 6 (le comma) | log₂ 3 | exact | le 4/3 n'est pas une réduite de log₂ 3 | démontré (§ 3.4) |
| M9 | course de Tchebychev : (ℤ/10)* (±i devant) et (ℤ/12)* (1 derrière) | les classes carrées de (ℤ/b)* | calculé jusqu'à 10⁹ ; classique (Rubinstein et Sarnak) | pourquoi les carrés perdent à tous les x : conjectural (GRH, indépendance linéaire) | calculé (§ 7.1) |

### 5.3 Les obstructions

| éléments | le trou | où chercher |
|---|---|---|
| K5 : le 17 de Henderson et le 17 de i | aucune transformation connue ; i existe pour 5, 13, 17, pas pour 3, 7, 11, 19, 23, et les Venn existent partout | Henderson 1963 ; Griggs, Killian, Savage 2004 ; `/home/user/dzoba/venn17/README.md` ; plus de diagrammes d'origine indépendante |
| K9 : le Venn de Midy a des aires inégales et enchevêtrées | l'enchevêtrement de « 2 divise L » et « ℓ divise L » par la réciprocité quadratique ; la lecture « ellipses ascendantes et descendantes » n'a pas de cadre | théorie de Kummer avec enchevêtrement (Wiertelak ; Moree 2005 ; Lenstra, Moree, Stevenhagen) |
| K8 : les trois 4/3 | trois procédés pour un même nombre ; aucune loi commune | le seul lien survivant passe par log₂ 3 et le comma (arbre P6) |
| K3 : la période de 1/p vaut 6 au-delà de q = 3 | la famille ne remplit le groupe que pour q = 2, 3 ; le lemme des chiffres, lui, vaut pour tout q | l'analogue hexagonal : « ω modulo p » ; Φ₆(q²+1) = Φ₆(q)·Φ₃(q) |
| fiche 014 : « (−2)^(3/2) ≡ −i modulo 3 » | la phrase réunit 2^(3/2) (≡ −i dans F₉) et (−2)^(3/2) (= ±1 dans F₉) ; la fiche le signale déjà (« reste à préciser ») ; le 10 et le 12 de 3√3 et de 2√2 sont des termes de clôture | demander à l'auteur la phrase voulue ; écrire « 2^(3/2) ≡ −i dans F₉ » dans la fiche (§ 4.4) |
| la base 3 dans le plan | ℤ/3 n'a que des reflets ; son i n'existe que dans F₉, dont le groupe est cyclique d'ordre 8 | le corpus n'utilise de F₉ que √2 = ±i |
| fiche 015 : la face est exacte, les comptes dérivent, la limite 2 est conjecturée | la conjecture de Hardy et Littlewood pour k = 2, 3, 4 n'est démontrée pour aucun k ≥ 2 | rien de plus à calculer ici : à 10⁹ le modèle est à 0,0005 près |
| Lemke Oliver et Soundararajan : les rapports « même chiffre » | ils passent par 17/24 et 2/3 à 10⁸ puis s'en éloignent (0,7327 et 0,7015 à 10⁹) ; la loi de l'écart est conjecturale | Lemke Oliver, Soundararajan 2016 ; Holt (2024, à vérifier) |
| fiche 005 | Fermat est nécessaire, pas sélectif ; la cause de l'exactitude à 19 courbes est inconnue | `recueil/dossiers/moities-et-crans.md` § 4.1 ; les Venn à 11 et 13 courbes d'origine indépendante |
| XIX § 4 : « 2 aux dénominateurs des réduites (10 et 93 points) » | incomplet : il y a deux longueurs pour toutes les valeurs N = m·q_k + q_(k−1) (r = 0) | corriger la phrase (§ 6.2) |
| XIV § 1 pour L composé | les directions sont des multiples de plusieurs angles à la fois : pas un cas du théorème des trois distances | une version du théorème pour un sous-groupe de rang ≥ 2 de ℝ/ℤ |

### 5.4 Le cocycle de M1, sur un exemple

La condition de cocycle (plan § 3.0) se vérifie ici sur le triplet de quarts de tour 3, 9, 7 de l'horloge de 10, avec le caractère χ(a) = (a/5), le symbole de Legendre modulo 5, qui dit si σ_a laisse √5 fixe. On a χ(3) = −1, χ(9) = +1, χ(7) = −1, χ(1) = +1. Les transformations se composent comme 3·3 = 9, 3·9 = 7, 3·7 = 1 (modulo 10), et leurs images aussi : (−1)(−1) = +1, (−1)(+1) = −1, (−1)(−1) = +1. **Le cocycle se ferme** : χ est trivial sur le demi-tour 9 = 3², donc il se factorise par ℤ/4 → ℤ/2. C'est pour cela que 1 et 9 jouent le même rôle pour φ, et 3 et 7 le rôle opposé. Les trois sections locales (XIX § 2 : l'horloge ; IX § 4 : le nombre d'or et son conjugué ; la course de Tchebychev) se recollent donc sur le seul caractère quadratique de 5 *(démontré, élémentaire)*.

## 6. Les trous

### 6.1 Les trous du recueil : fiches nouvelles proposées

Douze des quinze fiches viennent des parties XXIX et XXX, et les parties III à XXVIII n'ont aucune fiche à elles (plan § 6.1). Dans ce dossier, les sections 1, 2 et 5 de `scripts/recueil_verifications.py` (le i modulo b et F₉, les puissances sous 10, Midy) n'ont aucune fiche (§ 2.1). Voici dix propositions, N1 à N10. La priorité dit l'ordre d'écriture : 1 d'abord. Chaque fiche suivrait le format de `recueil/README.md` ; je donne le tableau d'en-tête, l'observation et le contexte. Le champ « révisé » serait « non ». Les nombres cités sont ceux du § 3 ; ils viennent du code du § 7.1 sauf mention contraire.

#### N1 : Le 3 de 1/7 est le i de la base 10 : la famille b = q² + 1 (priorité 1)

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact (lemme démontré pour tout q ≥ 2 ; vérifié pour q = 2 à 120 ; balayage b ≤ 400, p ≤ 4 000) |
| partie | XIX (§ 2) et la fiche 013 |
| script | `scripts/revision_001.py` § 4.3 (K3) ; `scripts/bases_objets.py` § 1 (i modulo b) ; code du § 7.1 de ce dossier |
| image | `figures/t1_bases_modulaires.png` (panneaux c et d) |
| dimension | D2 (D5 pour l'aiguille) |
| test | variation du paramètre (q) ; démonstration |

*Observation.* Pour q ≥ 2, b = q² + 1 et p = q² − q + 1, les chiffres ⌊b·r/p⌋ (r = 1, …, p − 1) sont exactement les entiers de [1, b − 2] qui ne sont pas multiples de q ; les chiffres absents sont 0, q, 2q, …, q² = b − 1, c'est-à-dire les k·i, puisque q² ≡ −1 (mod b). Pour q = 3, 1/7 = 0,142857… saute 0, 3, 6, 9 et ses chiffres sont les unités modulo 9. La période de 1/p vaut 6 dès que q ≥ 3 et p est premier : elle remplit le groupe seulement pour q = 2 et q = 3. *Contexte.* La fiche 013 et le test 4.1 de la session ; K3 du plan (« à noter comme nouvelle fiche »).

#### N2 : La même aiguille (q, 1) a pour norme q² + 1 sur la grille carrée et q² − q + 1 sur la grille décalée (priorité 2)

| champ | valeur |
|---|---|
| type | Analogie ; Fait amusant |
| statut | exact |
| partie | XV (§ 5) et XIX (§ 2) |
| script | `scripts/grille_decalee.py` § 5 (`points_hex`, `r_hex`) ; `scripts/bases_objets.py` § 1 |
| image | — |
| dimension | D5 (D2) |
| test | variation du paramètre (q) ; identité exacte |

*Observation.* b = N(q + i) = q² + 1 dans ℤ[i] et p = N(q + ω) = q² − q + 1 dans ℤ[ω] (ω = e^(2πi/3)) : la même aiguille, lue sur les deux grilles. Pour q = 3 : 10 et 7. (3 + ω)² = 8 + 5ω est le triangle 5-7-8 de XV § 5, comme (2 + i)² = 3 + 4i est le 3-4-5 de XIV. Modulo b, q est un quart de tour (q² ≡ −1) ; modulo p, q est un sixième de tour (q³ ≡ −1) ; et b = p + q est lui-même d'ordre 6 modulo p. L'autre premier de période 6 en base 10, 13, est N(3 − ω) = q² + q + 1. *Contexte.* K3 (§ 3.2) ; le corpus a « i modulo b » (XIX) et pas « ω modulo p ».

#### N3 : Midy est un demi-tour, et 10^(L/4) est un i : la tour du 17-gone (priorité 2)

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact |
| partie | recueil (§ 5) et XXVIII (§ 3.6) |
| script | `scripts/recueil_verifications.py` § 5 ; `scripts/octaedre_perron_venn.py` § 3 (calcul de Gauss, lignes 683 à 705) |
| image | — |
| dimension | D2 (D6) |
| test | identité exacte ; comptage sur les premiers < 10⁶ |

*Observation.* Si la période L de 1/p en base b est 2h, b^h ≡ −1 (mod p) : c'est Midy, un demi-tour. Si 4 divise L, b^(L/4) est un i : 10⁴ ≡ 4 (mod 17), 10² ≡ 27 (mod 73), 10 ≡ 10 (mod 101), 10² ≡ 100 (mod 137). 26 109 des 78 496 premiers sous 10⁶ (0,3326) ont un i dans l'orbite de 10. Pour p = 17, 10 est une racine primitive : la tour est entière (10⁸ ≡ −1, 10⁴ ≡ i, 10² ≡ −2 comme huitième de tour), et les périodes de Gauss en 2, 4 et 8 classes sont les orbites de ⟨10⟩ ⊃ ⟨10²⟩ ⊃ ⟨10⁴⟩ ⊃ ⟨10⁸⟩. *Contexte.* `resultats/recueil_verifications.md` § 5 vérifie Midy sans fiche ; XXVIII § 3.6 a le cas de 17 ; la règle générale « 4 divise L donne un i » n'est nulle part.

#### N4 : La tour 2-adique des périodes et son enchevêtrement par la réciprocité quadratique (T6, T6b) (priorité 1)

| champ | valeur |
|---|---|
| type | Corrélation ; Fait amusant |
| statut | structure (un mécanisme connu, la théorie de Kummer et la réciprocité, et la loi de l'écart) |
| partie | recueil (§ 5) |
| script | `scripts/revision_001.py` § 4.6 (T6) ; code du § 7.1 (T6b) |
| image | — |
| dimension | D2 (D7) |
| test | variation de la borne et de la base (T6) ; prédiction par la réciprocité (T6b) |

*Observation.* Pour une base générique, v₂(ord_p(b)) = 0, 1, 2, 3 pour 1/3, 1/3, 1/6, 1/12 des premiers (mesuré 0,333 ; 0,334 ; 0,166 ; 0,083 en base 10 sous 10⁶) ; pour la base 2, 7/24, 7/24, 1/3, 1/24. La part de ℓ divise L vaut ℓ/(ℓ² − 1). Les événements « 2 divise L » et « ℓ divise L » ne sont pas indépendants quand la partie sans carré de la base vaut ℓ ou 2ℓ : R(2, ℓ) = 1/2 (le caractère quadratique de la base est toujours +1), 5/4 (c'est celui de −1) ou 17/16 (c'est celui de ±2). Écart maximal à la prédiction sur 55 couples : 0,006. *Contexte.* K9 du plan (Midy pair et impair) et la lecture de l'auteur en « Venn dimensionnel ».

#### N5 : Les trois 4/3 sont une coïncidence de petits entiers ; la loi du comma est derrière (T7) (priorité 1)

| champ | valeur |
|---|---|
| type | Coïncidence ; Hasard |
| statut | hasard (testé : réplication sur les bases de 3 à 3 000 000) |
| partie | recueil (§ 2), III, XXIV |
| script | `scripts/recueil_verifications.py` § 2 ; `scripts/revision_001.py` § 4.5 (T7) ; code du § 7.1 |
| image | — |
| dimension | D2 (D7, D1) |
| test | coïncidence entre entiers : réplication sur d'autres bases |

*Observation.* c₂(b)/c₃(b) vaut 4/3 seulement pour b de 10 à 16 et de 244 à 256 (démontré : (27/16)^k < 3 exige k ≤ 2) ; il tend vers log₂ 3. Pour un rapport r/s quelconque, le nombre de fenêtres de b est ⌊ln 3/ρ⌋ ou ⌊ln 2/|ρ|⌋, avec ρ = s·ln 3 − r·ln 2 : 2 pour 4/3, 9 pour 3/2, 13 pour 8/5, 81 pour 19/12 (le comma), 60 pour 65/41, 526 pour 84/53. V₃/V₂ = 4/3 est un pas de Wallis (qui tend vers 0 avec n) ; le 4/3 de 1/x₀ = n + 4/3 est une constante de la série. *Contexte.* K8 ; CLAUDE.md § 10 (« c'est à tester »), VI § 3 ter (la dimension, c'est le nombre de fois qu'une base entre dans une autre).

#### N6 : Le diésis et le comma sont le troisième écart du théorème des trois distances (priorité 1)

| champ | valeur |
|---|---|
| type | Analogie |
| statut | exact |
| partie | XXVI (§ 2.5), XX (§ 6), XI (§ 2), XIX (§ 4) |
| script | `scripts/kakeya_miroir.py` § 2 (`trois_ecarts`) ; `scripts/angle_or_aiguilles.py` § 2 ; `scripts/bases_objets.py` § 3 ; code du § 7.1 |
| image | `figures/aa2_virgule_miroir.png` (panneaux a et e) |
| dimension | D2 (D5) |
| test | identité exacte, vérifiée pour N = 2 à 150 et cinq valeurs de α |

*Observation.* Pour N = m·q_k + q_(k−1) + r points {j·α}, les écarts sont η_k (N − q_k fois), η_(k−1) − m·η_k (r fois) et η_(k−1) − (m − 1)·η_k (q_k − r fois). Pour α = log₁₀ 2 et N = 21 : 11 × 128/125 (le diésis, η₂ = log₁₀(128/125)), 8 × 625/512, 2 × 5/4. Pour α = log₂ 3 − 1 et N = 12 : le limma (7 fois) et l'apotome (5 fois) ; à N = 13 apparaît le troisième écart, le comma pythagoricien, une fois. Les N à deux longueurs sont les N = m·q_k + q_(k−1) (r = 0), pas seulement les dénominateurs des réduites : 2, 3, 4, 7, 10, 13, 23, … pour log₁₀ 2. *Contexte.* XI, XIV, XV, XIX, XX et XXVI disent chacune « c'est le théorème des trois distances » ; aucune n'écrit la formule ni ne dit que le diésis et le comma en sont des écarts.

#### N7 : Le dernier chiffre d'un premier dit si le nombre d'or existe modulo p ; la course de Tchebychev (priorité 1)

| champ | valeur |
|---|---|
| type | Corrélation ; Fait amusant |
| statut | exact pour le lien (démontré, vérifié pour p < 10⁶) ; calculé pour la course (jusqu'à 10⁹) |
| partie | recueil (fiche 015), IX, XI, XII |
| script | `scripts/recueil_verifications.py` § 6 ; code du § 7.1 |
| image | — |
| dimension | D2 (D7) |
| test | exact ; variation de la borne (10³ à 10⁹) et de la base (10, 12) |

*Observation.* Pour p premier, hors 2 et 5 : si p finit par 1 ou 9, 5 est un carré modulo p, le nombre d'or existe dans ℤ/p et p divise F_(p−1) ; si p finit par 3 ou 7, il n'existe que dans F_(p²) et p divise F_(p+1) (aucun contre-exemple parmi les 78 496 premiers sous 10⁶). Les classes 3 et 7 (i et −i modulo 10) devancent ensemble les classes 1 et 9 à chaque premier jusqu'à 10⁹ (avance 2 094 à 10⁹ ; +6 819, +759 et +41 792 à 10¹⁰, 10¹¹ et 10¹² d'après les tables publiées) ; en base 12, la classe 1, seul carré de (ℤ/12)*, est la dernière à chaque premier. *Contexte.* La fiche 015 et l'horloge de XIX ; le corpus n'a ni « résidu quadratique » ni « rang d'apparition de Fibonacci ».

#### N8 : La dérive des dizaines de premiers est la prédiction de Hardy et Littlewood à taille finie (priorité 1)

| champ | valeur |
|---|---|
| type | Corrélation |
| statut | structure (la loi de l'écart est calculée sans paramètre ajusté ; la conjecture reste ouverte) |
| partie | recueil (fiche 015) |
| script | `scripts/recueil_verifications.py` § 6 ; `scripts/revision_001.py` § 4.2 ; code du § 7.1 |
| image | — |
| dimension | D2 (D7, D6) |
| test | variation du paramètre N (10⁴ à 10⁹) et loi de l'écart |

*Observation.* Le rapport par motif exact, 2·({1,7}+{3,9})/({1,3}+{7,9}+{3,7}+{1,9}), vaut 3,8969 ; 3,1448 ; 2,8321 ; 2,6306 ; 2,5255 ; 2,4442 de 10⁴ à 10⁹. La prédiction de Hardy et Littlewood à taille finie (densités T_k/ln(n)^k de k premiers dans une dizaine, inclusion–exclusion) donne 4,1979 ; 3,2370 ; 2,8535 ; 2,6523 ; 2,5286 ; 2,4447. Les paires larges sont à 2 (S(6)/S(2) = 2) : 146 841 ; 146 953 ; 146 720 ; 146 459 pour les distances 2, 2, 4, 8 et 293 573 ; 293 080 pour la distance 6, à 10⁸. La limite 2 est approchée comme 6,49/ln N au premier ordre. *Contexte.* La fiche 015 et le test 4.2 de la session.

#### N9 : Les rapports de Lemke Oliver et Soundararajan croisent 17/24 et 2/3 à 10⁸ puis s'en vont (priorité 3)

| champ | valeur |
|---|---|
| type | Coïncidence ; Hasard |
| statut | hasard (testé : variation de la borne) |
| partie | recueil (fiche 015) |
| script | code du § 7.1 (§ 6 du code) |
| image | — |
| dimension | D7 (D2) |
| test | coïncidence entre entiers : variation de la borne |

*Observation.* Les rapports « même chiffre après même chiffre » valent 0,7080 ; 0,6666 ; 0,6669 ; 0,7075 pour 1 → 1, 3 → 3, 7 → 7, 9 → 9 à 10⁸, soit 17/24 et 2/3 à 0,0008 près, qui sont les densités de Hasse de la base 2 et d'une base générique. À 10⁹ ils valent 0,7327 ; 0,7015 ; 0,7010 ; 0,7329 : ils continuent de monter. La table 4 × 4 est symétrique par (a → b) ~ (−b → −a) à 0,002 près à 10⁸. *Contexte.* Même leçon que le 2√2 et le π de la fiche 015 (R : `resultats/revision_001.md` § 4.2) ; Lemke Oliver et Soundararajan (2016).

#### N10 : La famille de Pell des bases à deux écritures : le 7 de Hutton et le 239 de Machin sont des i (priorité 2)

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact |
| partie | XXI (§ 2) |
| script | `scripts/vingt_quatre_miroir.py` § 2 (`RAC50`, `deux_carres`) ; code du § 7.3 |
| image | `figures/v1_vingt_quatre.png` (panneau d) |
| dimension | D2 (D5) |
| test | identité exacte ; vérifiée pour les six premiers membres |

*Observation.* Les couples (p, q) avec p² + 1 = 2q² (1, 1), (7, 5), (41, 29), (239, 169), (1 393, 985), (8 119, 5 741) donnent les bases b = p² + 1 = 2q² = 2, 50, 1 682, 57 122, 1 940 450, 65 918 162. Dans chacune, i ≡ p, et b s'écrit p² + 1² et q² + q² (deux écritures distinctes dès b = 50) : l'aiguille (p, 1) et la diagonale du carré q × q ont la même longueur. Le 7 de 7² ≡ −1 (mod 50) est le deuxième membre (XXI § 2) ; le 239 de Machin, tel que 239² + 1 = 2·13⁴, est le quatrième, et Ljunggren montre qu'il est le seul p > 1 dont le q est un carré. *Contexte.* XXI § 2 cite Pell, Hutton, Machin et Ljunggren sans dire que 239 est un i modulo 57 122 ; XVII a les compagnons de Pell 1, 3, 7, 17, 41, 99, 239…

### 6.2 Les trous du corpus

- **Aucune partie sur la réciprocité quadratique.** Le mot « résidu quadratique » n'apparaît dans aucun fichier .md du dépôt (recherche faite) ; Legendre n'y est que le théorème des trois carrés. La règle qui fixe quand φ existe modulo p, l'enchevêtrement de T6b et la course de Tchebychev en dépendent.
- **Aucune partie sur ℤ[i]/(b) ni sur ℤ[ω]/(p).** Le corpus a « i modulo b » (XIX), pas « i dans le plan modulo b » (F₉ pour b = 3, ℤ[i]/(4) × F₉ pour b = 12), ni l'analogue hexagonal « ω modulo p ».
- **Aucun script ne calcule** la formule des trois distances (comptes et longueurs), la règle « 4 divise L donne un i », le nombre de fenêtres de T7, les motifs de dizaine au-delà de 10⁸, ni la prédiction de Hardy et Littlewood à taille finie. Le code du § 7 les donne.
- **Le lien entre IX § 4 et XIX § 2** (les racines dixièmes de l'unité et l'horloge de 10) n'est écrit nulle part : c'est le groupe de Galois de ℚ(ζ₁₀).
- **Les erreurs ou incomplétudes relevées** (j'ai relu les passages cités) :
  1. `scripts/angle_or_aiguilles.py` l. 50 et `resultats/angle_or_aiguilles.md` § 1 (l. 8) disent « 222,5° est un arrondi : la valeur exacte 222,4922…° est irrationnelle ». C'est vrai de l'angle d'or, mais XI § 5 barre la phrase et XII § 2 montre que 222,5° vaut exactement 89/144 de tour (rang 12 de Fibonacci). Le script et ses résultats n'ont que la première moitié.
  2. XIX § 4 (`bases-objets.md`, ligne 195) écrit « 2 aux dénominateurs des réduites (10 et 93 points) » ; `resultats/bases_objets.md` § 3 (ligne 92) et la ligne 213 de `scripts/bases_objets.py` écrivent « Deux longueurs seulement aux dénominateurs des réduites (10, 93) ». C'est incomplet : il y a deux longueurs pour toutes les valeurs N = m·q_k + q_(k−1), dont 4, 7, 13, 23, … 103 pour log₁₀ 2 (§ 3.5).
  3. XVIII § 8 (« Pas établi », ligne 222 de `pixels-longitudes.md`) écrit « La base ne fait que choisir le pas du grain grossier ». XIX le corrige : l'auteur écrit que la phrase « ne tient pas » (ligne 4 de `bases-objets.md`) et le § 1 reprend la correction (« Ma phrase mélangeait deux choses ») ; XVIII ne renvoie à XIX que par le lien « Suite » de sa ligne 17 et n'a pas de note de correction à cet endroit.
  4. *(pas une erreur : un point que la fiche signale déjà)* La fiche 014 écrit que le lien « (−2)^(3/2) ≡ −i modulo 3 » de l'auteur « reste à préciser ». Le § 4.4 le précise : dans F₉, −i est la valeur de 2^(3/2), alors que (−2)^(3/2) vaut ±1.
- **Un décalage de numérotation sans conséquence** : les en-têtes de `scripts/polynomes.py` sont numérotés 1, 2, 3, 5 et ses résultats ont cinq sections (§ 2.1).
- **D5 et D8 n'ont aucune fiche principale** (plan § 6.1). Mes fiches N2 et N10 auraient D5 en deuxième dimension.

### 6.3 Les trous des données publiées

| piste | ce qui manque | où chercher | références |
|---|---|---|---|
| premiers par dernier chiffre | les comptes π(10ⁿ ; 10, a) sont publiés jusqu'à 10¹³ (OEIS A073505 à A073508), ainsi que le chiffre le plus fréquent (A244191). Ce que je n'ai pas vu (à vérifier) : la course à chaque premier (non seulement aux puissances de 10), la même en base 12, le lien avec le nombre d'or, la face modulo 3, les 16 motifs de dizaine sauf les quadruplets, et la loi de la dérive | Prime Pages ; OEIS ; Granville et Martin sur les courses de nombres premiers | OEIS A073505–A073508 ; Granville–Martin 2006 ; Rubinstein–Sarnak 1994 |
| premiers consécutifs | Lemke Oliver et Soundararajan donnent le déficit des paires de même chiffre ; ce qui manque (à vérifier) : l'évolution avec x qui traverse 17/24 et 2/3 à 10⁸, la symétrie (a → b) ~ (−b → −a), et le lien avec les motifs de dizaine | Lemke Oliver–Soundararajan ; Holt (prépublication de 2024, résumé seulement) | Lemke Oliver–Soundararajan 2016 ; Holt 2024 (à vérifier) |
| densités de Hasse | Hasse donne 17/24 (ℓ = 2, base 2) et ℓ/(ℓ² − 1) (ℓ impair). Je n'ai pas vu de table des rapports d'enchevêtrement R(2, ℓ) = 17/16, 5/4, 1/2 pour des bases courantes, ni de tour v₂ pour la base 10 (à vérifier) ; ils découlent de la théorie de Kummer avec enchevêtrement | Wiertelak ; Moree ; Lenstra, Moree, Stevenhagen | Hasse 1965/66 et 1966 ; Moree 2005 ; Lenstra–Moree–Stevenhagen (2014) |
| trois distances en musique et en décimal | la théorie des gammes bien formées connaît le théorème pour les gammes (Carey et Clampitt) ; je n'ai pas vu la lecture du diésis comme écart η de log₁₀ 2 (à vérifier) | théorie musicale mathématique ; Alessandri–Berthé | Carey–Clampitt 1989 ; Alessandri–Berthé 1998 ; Sós, Surányi, Świerczkowski 1958 |
| quadruplets et motifs de dizaine | les quadruplets premiers sont comptés ; les autres motifs ne le sont pas, à ma connaissance | OEIS (quadruplets A050258, numéro à vérifier) ; MathWorld | Hardy–Littlewood 1923 ; OEIS ; MathWorld |
| Midy étendu | le résultat général (k blocs) est publié ; je ne l'ai pas vu relié au i (4 divise L) | Ginsberg, Gupta et Sury, Lewittes, Martin | Ginsberg 2004 ; Gupta–Sury 2005 ; Lewittes 2007 |

#### Références citées dans ce dossier

Statut : « sûre » = je connais la référence (auteurs, titre, revue, année) et une recherche en ligne l'a confirmée ; « à vérifier » = je ne suis pas sûr d'un détail (volume, pages, numéro) ou je n'ai pu lire qu'un résumé. Aucune page n'a été lue en entier ; les recherches en ligne rendent des résumés.

- *sûre* : H. Hasse, « Über die Dichte der Primzahlen p, für die eine vorgegebene ganzrationale Zahl a ≠ 0 von gerader bzw. ungerader Ordnung mod. p ist », *Math. Annalen* 166 (1966), 19–23 : 17/24 pour la base 2. (La note de Hasse de *Math. Annalen* 162 (1965/66), 74–76 donne le cas d'un nombre premier impair ℓ ; son titre exact : à vérifier.)
- *sûre* : M. Rubinstein, P. Sarnak, « Chebyshev's bias », *Experimental Mathematics* 3(3) (1994), 173–197.
- *sûre* : A. Granville, G. Martin, « Prime number races », *Amer. Math. Monthly* 113(1) (2006), 1–33.
- *sûre* : R. J. Lemke Oliver, K. Soundararajan, « Unexpected biases in the distribution of consecutive primes », *Proc. Natl. Acad. Sci. USA* 113(31) (2016), E4446–E4454 ; arXiv:1603.03720.
- *à vérifier* : F. B. Holt, prépublication arXiv:2405.03540 (2024) sur le biais de Lemke Oliver et Soundararajan comme effet de crible « transitoire » (résumé seulement).
- *sûre* : G. H. Hardy, J. E. Littlewood, « Some problems of “Partitio numerorum”; III: On the expression of a number as a sum of primes », *Acta Mathematica* 44 (1923), 1–70.
- *sûre* : P. Moree, « On primes p for which d divides ord_p(g) », *Funct. Approx. Comment. Math.* 33 (2005), 85–95 ; P. Moree, « Artin's primitive root conjecture – a survey », *Integers* 12A (2012), A13 (arXiv:math/0412262).
- *à vérifier* : H. W. Lenstra Jr., P. Moree, P. Stevenhagen, « Character sums for primitive root densities », *Math. Proc. Cambridge Philos. Soc.* (2014), arXiv:1112.4816 (volume et pages à vérifier).
- *à vérifier* : J. Wiertelak, sur l'existence de la densité des premiers p tels que d divise ord_p(a) (références non lues).
- *sûre* : S. Świerczkowski, « On successive settings of an arc on the circumference of a circle », *Fund. Math.* 46 (1958), 187–189.
- *à vérifier* (pages) : V. T. Sós, « On the distribution mod 1 of the sequence nα », *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.* 1 (1958), 127–134 ; P. Surányi, « Über die Anordnung der Vielfachen einer reellen Zahl mod 1 », même revue, 1 (1958), 107–111.
- *sûre* : P. Alessandri, V. Berthé, « Three distance theorems and combinatorics on words », *L'Enseignement Math.* 44 (1998), 103–132.
- *à vérifier* (numéro et pages) : N. Carey, D. Clampitt, « Aspects of well-formed scales », *Music Theory Spectrum* 11(2) (1989), 187–206.
- *à vérifier* : E. Midy, *De quelques propriétés des nombres et des fractions décimales périodiques* (Nantes, 1836) ; B. D. Ginsberg, « Midy's (nearly) secret theorem — an extension after 165 years », *College Math. J.* 35(1) (2004) ; A. Gupta, B. Sury, « Decimal expansion of 1/p and subgroup sums », *Integers* 5 (2005), A19 ; J. Lewittes, « Midy's theorem for periodic decimals », *Integers* 7 (2007), A02. Les titres et revues sont confirmés par une recherche en ligne ; les pages de Ginsberg ne le sont pas.
- *sûre* : OEIS A073505 à A073508 (π(10ⁿ ; 10, a) pour a = 1, 3, 7, 9) : mes comptes à 10³ à 10⁹ coïncident avec les valeurs lues. *À vérifier* : les valeurs lues pour 10¹⁰ à 10¹² et le numéro A050258 des quadruplets (valeurs de MathWorld, d'après Nicely).
- *sûre* : D. W. Henderson, « Venn diagrams for more than four classes », *Amer. Math. Monthly* 70 (1963), 424–426 ; J. Griggs, C. E. Killian, C. D. Savage, « Venn diagrams and symmetric chain decompositions in the Boolean lattice », *Electron. J. Combin.* 11(1) (2004), R2.
- *sûre* (classique) : K. F. Gauss, *Disquisitiones arithmeticae* (1801) : le 17-gone, les périodes de Gauss ; A. Hurwitz, « Über die angenäherte Darstellung der Irrationalzahlen durch rationale Brüche », *Math. Annalen* 39 (1891), 279–284 ; K. Ireland, M. Rosen, *A Classical Introduction to Modern Number Theory*, 2e éd., Springer GTM 84 (1990) : normes de ℤ[i] et de ℤ[ω], réciprocité quadratique.
- *à vérifier* : C. E. Ljunggren, sur x² + 1 = 2y⁴ (1942) ; la partie XXI cite ProofWiki et arXiv:1705.03011.
- *à vérifier* : C. Dzoba, le dépôt dzoba/venn17 (lu en local : `/home/user/dzoba/venn17/README.md`, CC BY 4.0) ; Brenner, Gregor, Mütze, Verciani (2026), l'enquête que ce README cite.

## 7. Le code minimal du test qui me concerne (T6 et T7, côté « bases »)

### 7.0 Ce qui existe déjà, ce qui s'ajoute

`scripts/revision_001.py` a déjà, au § 4.3 (K3), au § 4.5 (T7) et au § 4.6 (T6), les calculs que le plan demande (R : `resultats/revision_001.md`). Je les ai relus, puis recalculés avec un code à moi : tout concorde au dernier chiffre (§ 2.3). Le code ci-dessous ajoute ce que ces sections n'ont pas. Il se découpe en six blocs, chacun une section possible de `resultats/revision_001.md` :

1. **K3** : le lemme des chiffres, pour q de 2 à 120, et le balayage b ≤ 400, p ≤ 4 000 (la session s'arrête à b ≤ 60 et p ≤ 400).
2. **T6** : la tour 2-adique, avec ses valeurs attendues (1/3, 1/3, 1/6, 1/12, 1/24 ; pour la base 2 : 7/24, 7/24, 1/3, 1/24, 1/48), contrôlées à 0,01 près.
3. **T6b** : la loi jointe de « 2 divise L » et « ℓ divise L » pour 11 bases et ℓ = 3, 5, 7, 11, 13, contre la règle de la réciprocité quadratique.
4. **T7** : les fenêtres de b où c₂/c₃ = r/s, par un balayage vectoriel jusqu'à 3·10⁶, contre la preuve par intervalles ; le nombre de fenêtres pour les réduites de log₂ 3.
5. **Les trois distances** : la fonction `trois_distances`, qui compare la mesure à la formule (assertion pour N = 2 à 150 et cinq valeurs de α), les écarts du diésis et du comma, les N à deux longueurs.
6. **Les premiers par position** : la course de Tchebychev en base 10 et en base 12, le tableau de Lemke Oliver et Soundararajan, le lien avec Fibonacci (assertion), les motifs de dizaine avec la prédiction de Hardy et Littlewood à taille finie.

Dépendances : numpy et mpmath. Durée mesurée sur 4 cœurs : 19 s et 0,7 Go de mémoire pour `NM = 10**8` (la valeur écrite) ; 53 s et 5,3 Go pour `NM = 10**9`, qui redonne les valeurs à 10⁹ citées au § 3.6. Le code n'écrit aucun fichier. Les assertions portent sur des théorèmes (lemme des chiffres, fenêtres de T7, formule des trois distances, Fibonacci) ou sur des prédictions déduites d'un théorème avec une tolérance (tour à 0,01, T6b à 0,03). Les comptes de premiers (Tchebychev, Lemke Oliver et Soundararajan, motifs de dizaine) sont imprimés sans assertion. Si une assertion échoue, le point correspondant du § 3 est faux.

### 7.1 Le code

```python
"""Agent bases : code minimal des tests T6 (et T6b), T7 et K3 pour scripts/revision_001.py, avec les trois distances et les premiers
par position. Dépendances : numpy, mpmath. Durée : 19 s et 0,7 Go avec NM = 10**8 ; 53 s et 5,3 Go avec NM = 10**9 (valeurs citées au § 3.6).
Aucun résultat n'est écrit en dur. Les assertions portent sur des théorèmes (identités exactes) ou sur des prédictions déduites
d'un théorème (tolérance indiquée) ; le reste est imprimé."""
import time
from math import gcd, log

import mpmath as mp
import numpy as np

T0 = time.time()
NM = 10 ** 8            # borne du crible des premiers (§ 6) ; 10 ** 9 pour retrouver les valeurs à 10⁹ du dossier
E = len(str(NM)) - 1    # NM = 10^E


def premiers(n):
    c = bytearray([1]) * (n + 1)
    c[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if c[i]:
            c[i * i::i] = bytearray(len(c[i * i::i]))
    return [i for i in range(n + 1) if c[i]]


def est_premier(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def v_ell(a, p, ell):
    """valuation ell-adique de l'ordre de a modulo p (p premier, p ne divise pas a), sans calculer l'ordre"""
    e, m = 0, p - 1
    while m % ell == 0:
        m //= ell
        e += 1
    x, k = pow(a, m, p), 0
    while x != 1:
        x, k = pow(x, ell, p), k + 1
    return k


def phi(n):
    return sum(1 for d in range(1, n + 1) if gcd(d, n) == 1)


# ---- 1. K3 : la famille b = q² + 1, p = q² − q + 1 ---------------------------------------------------------------------------
print("1. K3 : lemme des chiffres, q = 2 … 120")
for q in range(2, 121):
    b, p = q * q + 1, q * q - q + 1
    chiffres = {(b * r) // p for r in range(1, p)}                      # les chiffres ⌊b·r/p⌋, r = 1 … p − 1
    assert chiffres == {d for d in range(1, b - 1) if d % q}            # tous les entiers de [1, b − 2] non multiples de q
    assert sorted(set(range(b)) - chiffres) == [k * q for k in range(q + 1)]   # absents : 0, q, 2q, …, q·q = b − 1
    assert (q * q) % b == b - 1 and (q * p) % b == 1 and (q ** 3 + 1) % p == 0 and b - p == q
for q in (2, 3, 5, 7, 11, 13):
    b, p = q * q + 1, q * q - q + 1
    ordre = None
    if est_premier(p) and p > 2:
        ordre, x = 1, b % p
        while x != 1:
            x, ordre = (x * b) % p, ordre + 1
    print(f"  q = {q:2d} : b = {b:4d}, p = {p:4d}, p premier : {est_premier(p)!s:5}, période de 1/p en base b : {ordre}")


def periode_pleine(b, p):
    """les chiffres de la période de 1/p en base b sont-ils exactement les unités modulo b − 1 ? (arrêt dès qu'un chiffre n'en est pas une)"""
    r, vus, chiffres = 1, set(), set()
    while r not in vus:
        vus.add(r)
        d = (r * b) // p
        if gcd(d, b - 1) != 1:
            return False
        chiffres.add(d)
        r = (r * b) % p
    return len(chiffres) == phi(b - 1)


P4000 = premiers(4000)
cas = [(b, p) for b in range(3, 401) for p in P4000 if b % p and periode_pleine(b, p)]
print("  balayage b = 3 … 400, p ≤ 4000 : chiffres de la période = unités modulo b − 1 pour", cas)

# ---- 2. T6 : la tour 2-adique des périodes ; 3. T6b : l'enchevêtrement du Venn de Midy -----------------------------------------
N6 = 10 ** 6
PR = premiers(N6)
print("\n2. T6 : parts de v2(L), L = ordre de la base modulo p, p < 10^6")
attendu_generique = [1 / 3, 1 / 3, 1 / 6, 1 / 12, 1 / 24]
attendu_base2 = [7 / 24, 7 / 24, 1 / 3, 1 / 24, 1 / 48]
for base in (10, 2, 3, 12):
    ps = [q for q in PR if base % q]
    v2 = np.array([v_ell(base, q, 2) for q in ps])
    parts = [float(np.mean(v2 == k)) for k in range(5)]
    print(f"  base {base:2d} : v2 = 0 … 4 :", " ".join(f"{x:.4f}" for x in parts), "| L pair :", f"{np.mean(v2 > 0):.4f}",
          "| i dans <base> (4 | L) :", f"{np.mean(v2 > 1):.4f}")
    assert max(abs(x - y) for x, y in zip(parts, attendu_base2 if base == 2 else attendu_generique)) < 0.01


def sans_carre(n):
    s, d = 1, 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
        if n % d == 0:
            s, n = s * d, n // d
        d += 1
    return s * n


def r_attendu(base, ell):
    """R(2, ell) attendu par la réciprocité quadratique. ell | L force p ≡ 1 (mod ell). Si ell divise la partie sans carré s de la base,
    s = ell·c : (s/p) = (ell/p)·(c/p), avec (ell/p) = 1 si ell ≡ 1 (mod 4) et (−1/p) si ell ≡ 3 (mod 4). La base se comporte donc comme c' = ±c.
    Densité de L pair selon c' : carré 1/3, −1 : 5/6, ±2 : 17/24, sinon 2/3 ; R = densité / (2/3)."""
    s = sans_carre(base)
    if s % ell:
        return 1.0
    c = (s // ell) * (1 if ell % 4 == 1 else -1)
    return {1: 0.5, -1: 1.25, 2: 17 / 16, -2: 17 / 16}.get(c, 1.0)


N6B = 3 * 10 ** 6
PRB = premiers(N6B)
print("\n3. T6b : R(2, l) = P(2|L et l|L) / (P(2|L)·P(l|L)), p < 3·10^6, observé (attendu)")
ecart_max = 0.0
for base in (2, 3, 5, 6, 7, 10, 11, 12, 13, 14, 15):
    ps = [q for q in PRB if base % q]
    pair = np.array([v_ell(base, q, 2) > 0 for q in ps])
    lignes = []
    for ell in (3, 5, 7, 11, 13):
        ind = np.array([v_ell(base, q, ell) > 0 for q in ps])
        R = float(np.mean(pair & ind) / (np.mean(pair) * np.mean(ind)))
        ecart_max = max(ecart_max, abs(R - r_attendu(base, ell)))
        lignes.append(f"l={ell}: {R:.3f} ({r_attendu(base, ell):.3f})")
    print(f"  base {base:2d} :", " | ".join(lignes))
print(f"  écart maximal à la prédiction : {ecart_max:.3f}")
assert ecart_max < 0.03

# ---- 4. T7 : les puissances de 2 et de 3 sous b ------------------------------------------------------------------------------
print("\n4. T7 : c2(b) / c3(b)")
LIM = 3 * 10 ** 6
b_ = np.arange(3, LIM + 1)
c2 = np.searchsorted(2 ** np.arange(0, 23, dtype=np.int64), b_, side="left")      # nombre de 2^k < b
c3 = np.searchsorted(3 ** np.arange(0, 15, dtype=np.int64), b_, side="left")      # nombre de 3^k < b


def fenetres_observees(r, s):
    ok = np.flatnonzero(c2 * s == c3 * r)
    if not len(ok):
        return []
    coupures = np.flatnonzero(np.diff(ok) > 1)
    debuts, fins = np.r_[ok[0], ok[coupures + 1]], np.r_[ok[coupures], ok[-1]]
    return [[int(b_[d]), int(b_[f])] for d, f in zip(debuts, fins)]


def fenetres_theoriques(r, s, kmax):
    """(c2, c3) = (r k, s k) exige que (2^(rk−1), 2^(rk)] et (3^(sk−1), 3^(sk)] se coupent"""
    out = []
    for k in range(1, kmax + 1):
        lo, hi = max(2 ** (r * k - 1), 3 ** (s * k - 1)) + 1, min(2 ** (r * k), 3 ** (s * k))
        if lo <= hi:
            out.append([lo, hi])
    return out


def nombre_de_fenetres(r, s):
    """k admissible ssi (2^r/3^s)^k < 2 et (3^s/2^r)^k < 3 ; avec rho = s ln 3 − r ln 2 : k < ln 3 / rho si rho > 0, k < ln 2 / |rho| sinon"""
    rho = s * log(3) - r * log(2)
    x = log(3) / rho if rho > 0 else log(2) / -rho
    return int(x)


for r, s in ((4, 3), (3, 2), (8, 5), (19, 12)):
    obs = fenetres_observees(r, s)
    th = [f for f in fenetres_theoriques(r, s, 40) if f[0] <= LIM]
    th = [[lo, min(hi, LIM)] for lo, hi in th]
    assert obs == th
    print(f"  r/s = {r}/{s} : fenêtres de b ≤ {LIM} : {obs[:6]}{' …' if len(obs) > 6 else ''}")
assert fenetres_observees(4, 3) == [[10, 16], [244, 256]]
print("  nombre de fenêtres (b quelconque) pour les réduites de log2 3 et pour 4/3 :")
for r, s in ((2, 1), (3, 2), (4, 3), (8, 5), (19, 12), (65, 41), (84, 53)):
    n = nombre_de_fenetres(r, s)
    assert n == len(fenetres_theoriques(r, s, n + 5))
    print(f"    {r:3d}/{s:2d} : s·ln 3 − r·ln 2 = {s * log(3) - r * log(2):+.5f} → {n} fenêtres")

# ---- 5. les trois distances : (N − q_k, r, q_k − r) ---------------------------------------------------------------------------
mp.mp.dps = 30


def trois_distances(alpha, N):
    """écarts mesurés entre les N points j·alpha mod 1, et prédiction N = m·q_k + q_(k−1) + r (conventions q_(−1) = 0, η_(−1) = 1)"""
    p = sorted(mp.frac(j * alpha) for j in range(N))
    g = [p[i + 1] - p[i] for i in range(N - 1)] + [1 + p[0] - p[-1]]
    mesure = {}
    for x in g:
        cle = mp.nstr(x, 10)
        mesure[cle] = mesure.get(cle, 0) + 1
    x, a, conv = alpha, [], []
    h0, h1, k0, k1 = 0, 1, 1, 0
    for _ in range(14):
        c = int(mp.floor(x))
        a.append(c)
        h0, h1, k0, k1 = h1, c * h1 + h0, k1, c * k1 + k0
        conv.append((h1, k1))
        x = 1 / (x - c)
    q = [k for _, k in conv]
    qq = lambda j: 0 if j < 0 else q[j]
    eta = lambda j: mp.mpf(1) if j < 0 else abs(q[j] * alpha - conv[j][0])
    for k in range(0, len(q) - 1):
        for m in range(1, a[k + 1] + 1):
            r = N - m * qq(k) - qq(k - 1)
            if 0 <= r < qq(k):
                predit = {}
                for longueur, nombre in zip((eta(k), eta(k - 1) - m * eta(k), eta(k - 1) - (m - 1) * eta(k)), (N - qq(k), r, qq(k) - r)):
                    if nombre:
                        cle = mp.nstr(longueur, 10)
                        predit[cle] = predit.get(cle, 0) + nombre
                return mesure, predit, (N - qq(k), r, qq(k) - r)
    return mesure, None, None


phi_or = (1 + mp.sqrt(5)) / 2
ALPHAS = (("log10 2", mp.log10(2)), ("log2 3", mp.log(3, 2) - 1), ("log2 5", mp.log(5, 2) - 2), ("1/φ²", 1 / phi_or ** 2),
          ("arctan(4/3)/90°", mp.atan(mp.mpf(4) / 3) / (mp.pi / 2)))
print("\n5. trois distances : la formule vaut pour N = 2 … 150 et cinq valeurs de α")
for nom, alpha in ALPHAS:
    for N in range(2, 151):
        mesure, predit, _ = trois_distances(alpha, N)
        assert mesure == predit, (nom, N)
for nom, alpha, Ns in (("log10 2", mp.log10(2), (10, 21, 93)), ("log2 3", mp.log(3, 2) - 1, (12, 13, 53))):
    for N in Ns:
        mesure, _, comptes = trois_distances(alpha, N)
        print(f"  {nom}, N = {N:3d} : écarts {sorted(mesure.items())} ; comptes (N − q_k, r, q_k − r) = {comptes}")
for nom, alpha in ALPHAS[:2]:
    print(f"  {nom} : N < 120 avec exactement deux longueurs (r = 0) :", [N for N in range(2, 120) if len(trois_distances(alpha, N)[0]) == 2])

# ---- 6. les premiers par position : Tchebychev mod 10, Lemke Oliver–Soundararajan, motifs de dizaine et Hardy–Littlewood -------
print(f"\n6. premiers jusqu'à {NM:.0e}")
crible = np.ones(NM // 2, dtype=bool)               # indice i <-> 2i + 1
crible[0] = False
for i in range(1, int(NM ** 0.5) // 2 + 1):
    if crible[i]:
        p = 2 * i + 1
        crible[(p * p) // 2::p] = False
P = 2 * np.flatnonzero(crible) + 1                  # tous les premiers impairs
P4 = P[P % 5 != 0]                                  # hors 2 et 5 : ils finissent par 1, 3, 7 ou 9
D = P4 % 10
d = np.cumsum((D == 3) | (D == 7)) - np.cumsum((D == 1) | (D == 9))
print("  Tchebychev mod 10, non-résidus {3,7} moins résidus {1,9}, aux puissances de 10 :",
      [int(d[np.searchsorted(P4, 10 ** k, side='right') - 1]) for k in range(3, E + 1)],
      "| positif à chaque premier :", bool(np.all(d > 0)))
code = np.zeros(10, dtype=np.int64)
for i, a in enumerate((1, 3, 7, 9)):
    code[a] = i
C = code[D]
print("  Lemke Oliver–Soundararajan : (observé / indépendance) pour 1→1, 3→3, 7→7, 9→9")
for e in range(5, E + 1):
    m = int(np.searchsorted(P4, 10 ** e, side="right"))
    M = np.bincount(C[:m - 1] * 4 + C[1:m], minlength=16).reshape(4, 4).astype(float)
    R = M / (np.outer(M.sum(1), M.sum(0)) / M.sum())
    print(f"    10^{e} :", "  ".join(f"{R[i, i]:.4f}" for i in range(4)), "  (2/3 = 0.6667, 17/24 = 0.7083)")
print("  tableau complet à la borne (ligne = chiffre de p, colonne = chiffre du premier suivant, ordre 1 3 7 9) :")
for i in range(4):
    print("    ", " ".join(f"{R[i, j]:.4f}" for j in range(4)))

# course de Tchebychev en base 12 : toute unité y est un reflet, la seule classe carrée est 1
P12 = P[P % 3 != 0]                                 # hors 2 et 3 : classes 1, 5, 7, 11 modulo 12
R12 = P12 % 12
cum12 = {a: np.cumsum(R12 == a) for a in (1, 5, 7, 11)}
print("  base 12 : premiers ≡ 1, 5, 7, 11 (mod 12) à la borne :", [int(cum12[a][-1]) for a in (1, 5, 7, 11)],
      "| la classe 1 est la dernière à chaque premier :", bool(np.all((cum12[1] <= cum12[5]) & (cum12[1] <= cum12[7]) & (cum12[1] <= cum12[11]))))

# le dernier chiffre d'un premier et le nombre d'or : p divise F_(p−1) si p finit par 1 ou 9, F_(p+1) si p finit par 3 ou 7
def fib_mod(n, m):
    def rec(k):
        if k == 0:
            return 0, 1
        a, b = rec(k >> 1)
        c, d = (a * ((2 * b - a) % m)) % m, (a * a + b * b) % m
        return (d, (c + d) % m) if k & 1 else (c, d)
    return rec(n)[0]


faux = [p for p in PR if p not in (2, 5) and fib_mod(p - 1 if p % 10 in (1, 9) else p + 1, p) != 0]
print(f"  Fibonacci : premiers < 10^6 (hors 2, 5) qui ne divisent pas F_(p−1) (1, 9) ou F_(p+1) (3, 7) : {len(faux)}")
assert not faux

# motifs de dizaine : la dizaine a contient 10a + 1, 3, 7, 9 aux indices 5a, 5a+1, 5a+3, 5a+4 du crible des impairs
dz = crible.reshape(-1, 5)
u = {1: dz[:, 0], 3: dz[:, 1], 7: dz[:, 3], 9: dz[:, 4]}
primes_G = np.array(PRB, dtype=float)
P7 = primes_G[primes_G >= 7]


def T(k):
    """densité de Hardy–Littlewood de k premiers dans une dizaine, à 1/ln(n)^k près : 2, 5 et 3 sont fixés par n = 10a et la classe de a mod 3"""
    s = np.sum(np.log1p(-k / P7) - k * np.log1p(-1 / P7)) - k * (k - 1) / (2 * P7[-1] * np.log(P7[-1]))
    return 3.75 ** k * float(np.exp(s))


def rapport_hl(N):
    a = np.arange(1, N // 10, max(1, N // 10 ** 7), dtype=float)       # un échantillon régulier de dizaines suffit pour un rapport
    L = np.log(10 * a + 5)
    B = T(2) / L ** 2                                          # paire sur sa face (a ≡ 0 ou 2 mod 3) : les deux autres sont composés d'office
    F = B - 2 * T(3) / L ** 3 + T(4) / L ** 4                  # paire sur la face a ≡ 1 : les deux autres doivent être composés (inclusion–exclusion)
    return 1 + float(B.sum() / F.sum())


def rapport_hl_grand(e):
    """même rapport pour N = 10^e très grand : la somme sur les dizaines devient une intégrale en u = ln n, de poids e^u"""
    u = np.linspace(np.log(15), e * np.log(10), 400_000)
    w = np.exp(u - u.max())
    B = T(2) / u ** 2
    F = B - 2 * T(3) / u ** 3 + T(4) / u ** 4
    return 1 + float((w * B).sum() / (w * F).sum())


def ex(a_, b_, c_, d_, m):
    return int(np.sum(u[a_][:m] & u[b_][:m] & ~u[c_][:m] & ~u[d_][:m]))


print("  motifs exacts de dizaine : rapport par motif = 2·({1,7}+{3,9}) / ({1,3}+{7,9}+{3,7}+{1,9}), observé et Hardy–Littlewood à N fini")
for e in range(4, E + 1):
    m = 10 ** (e - 1)
    haut = ex(1, 7, 3, 9, m) + ex(3, 9, 1, 7, m)
    bas = ex(1, 3, 7, 9, m) + ex(7, 9, 1, 3, m) + ex(3, 7, 1, 9, m) + ex(1, 9, 3, 7, m)
    print(f"    10^{e} : {2 * haut / bas:.4f}   HL : {rapport_hl(10 ** e):.4f}")
print(f"  limite : R − 2 ≈ 2·T3/T2 / ln N, avec 2·T3/T2 = {2 * T(3) / T(2):.3f} ; Hardy–Littlewood plus loin :",
      {f"10^{e}": round(rapport_hl_grand(e), 4) for e in (12, 20, 100)})
m = len(dz)
print("  paires larges (les deux premiers, quoi qu'il en soit des deux autres), dizaines sous", NM, ":",
      {f"{a_}{b_}": int(np.sum(u[a_][:m] & u[b_][:m])) for a_, b_ in ((1, 3), (7, 9), (3, 7), (1, 7), (3, 9), (1, 9))})
print(f"\n(durée {time.time() - T0:.0f} s)")
```

### 7.2 Optionnel : l'effet de mes corrections sur le nerf

À lancer depuis la racine du dépôt. Il ne lit que le bloc JSON du plan (§ 1.9) et n'écrit rien. Résultat attendu : les 20 triangles vides et les 6 tétraèdres creux du plan, puis 13 et 14 avec mes ajouts (§ 8).

```python
"""Agent bases : effet de mes corrections de recouvrement sur le nerf (union parties + fiches), d'après le bloc JSON du plan, § 1.9.
Lancer depuis la racine du dépôt. Dépendances : bibliothèque standard seulement. Durée : moins d'une seconde."""
import itertools
import json
import re

texte = open("recueil/revisions/plan-001.md", encoding="utf-8").read()
CLOTURE = "`" * 3                                            # trois accents graves, qui ouvrent et ferment le bloc JSON du plan
J = json.loads(re.search(r"### 1\.9.*?" + CLOTURE + r"json\n(.*?)" + CLOTURE, texte, re.S).group(1))["dossiers"]


def nerf(J):
    elements = {d: {("partie", x) for x in J[d]["parties"]} | {("fiche", x) for x in J[d]["fiches"]} for d in J}
    commun = lambda S: bool(set.intersection(*[elements[d] for d in S]))
    noms = sorted(J)
    n = {k: sum(1 for S in itertools.combinations(noms, k) if commun(S)) for k in (2, 3, 4)}
    vides = [S for S in itertools.combinations(noms, 3) if not commun(S) and all(commun(p) for p in itertools.combinations(S, 2))]
    creux = [S for S in itertools.combinations(noms, 4) if not commun(S) and all(commun(p) for p in itertools.combinations(S, 3))]
    return n, vides, creux


n0, vides0, creux0 = nerf(J)
print(f"plan : arêtes {n0[2]}, triangles {n0[3]}, tétraèdres {n0[4]}, triangles vides {len(vides0)}, tétraèdres creux {len(creux0)}")
AJOUTS = [("partie", "VI"), ("partie", "XV"), ("partie", "XVIII"), ("partie", "XX"), ("partie", "XXII"), ("partie", "XXIV"), ("fiche", "002")]
for genre, x in AJOUTS:                                       # un ajout à la fois : qui remplit quoi
    J1 = json.loads(json.dumps(J))
    J1["bases-congruences-premiers"]["parties" if genre == "partie" else "fiches"].append(x)
    n1, vides1, creux1 = nerf(J1)
    print(f"  + {genre} {x:5s} : triangles vides {len(vides0)} → {len(vides1)}, tétraèdres creux {len(creux0)} → {len(creux1)}")
    for S in vides0:
        if S not in vides1:
            print("      remplit le triangle", " · ".join(S))
    for S in creux0:
        if S not in creux1:
            print("      remplit le tétraèdre", " · ".join(S))
J2 = json.loads(json.dumps(J))
for genre, x in AJOUTS:
    J2["bases-congruences-premiers"]["parties" if genre == "partie" else "fiches"].append(x)
n2, vides2, creux2 = nerf(J2)
print(f"tous les ajouts : arêtes {n2[2]}, triangles {n2[3]}, tétraèdres {n2[4]}, triangles vides {len(vides2)}, tétraèdres creux {len(creux2)}")
```

### 7.3 Optionnel : la famille de Pell et les fractions continues de √(aᵉ)

Ce code donne les nombres de N10 et du § 4.4 (35 fractions sur 75 avec un 10, 17 avec un 12).

```python
"""Agent bases : deux compléments. (1) La famille de Pell p² + 1 = 2q² : i ≡ p modulo b = 2q². (2) Les termes 10 et 12 dans les fractions
continues de √(aᵉ). Bibliothèque standard seulement ; moins d'une seconde."""
from math import isqrt

# (1) les couples (p, q) avec p² − 2q² = −1 : (x + y√2)(3 + 2√2) garde x² − 2y² = −1
x, y, famille = 1, 1, []
while len(famille) < 6:
    famille.append((x, y))
    x, y = 3 * x + 4 * y, 2 * x + 3 * y
for p, q in famille:
    b = p * p + 1
    assert b == 2 * q * q and (p * p) % b == b - 1            # b = 2q² et p est un i modulo b
print("p² + 1 = 2q² : (p, q, b) =", [(p, q, p * p + 1) for p, q in famille])


# (2) fraction continue régulière de √N : (a0, période), la période finit par 2·a0
def fraction_continue(N):
    a0 = isqrt(N)
    if a0 * a0 == N:
        return a0, []
    m, d, a, periode = 0, 1, a0, []
    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        periode.append(a)
        if a == 2 * a0:
            return a0, periode


couples = [(a, e) for a in range(2, 31) for e in range(1, 6) if isqrt(a ** e) ** 2 != a ** e]
avec = {t: [(a, e) for a, e in couples if t in fraction_continue(a ** e)[1] or fraction_continue(a ** e)[0] == t] for t in (10, 12)}
print(f"√(aᵉ), a ≤ 30, e ≤ 5, non entiers : {len(couples)} ; avec un 10 : {len(avec[10])} ; avec un 12 : {len(avec[12])}")
print("  e = 3 : a avec un 10 :", [a for a, e in avec[10] if e == 3], "; a avec un 12 :", [a for a, e in avec[12] if e == 3])
print("  3√3 = √27 :", fraction_continue(27), "; 2√2 = √8 :", fraction_continue(8))
```

### 7.4 Ce que le code ne fait pas

- **Pas de figure.** Trois panneaux iraient dans une nouvelle figure de `figures/` (dont le nom commencerait par `rev001_`) : (a) le rapport par motif de la fiche 015 en fonction de ln N, observé et prédit par Hardy et Littlewood ; (b) les fenêtres de c₂/c₃ en échelle logarithmique de b, avec les réduites de log₂ 3 ; (c) le cercle des décades et le cercle des quintes avec leurs trois écarts, pour N = 12 et 13 (log₂ 3) et N = 10 et 21 (log₁₀ 2).
- **Pas de test de l'hypothèse de Hardy et Littlewood** : le modèle est calculé, il n'est pas démontré.
- **Pas de comparaison à une loi de Lemke Oliver et Soundararajan** : je n'ai pas la forme exacte de leur terme secondaire (à vérifier).

## 8. Les corrections au recouvrement

Bloc JSON proposé pour le dossier, au format du § 1.9 du plan :

```json
{
  "bases-congruences-premiers": {
    "parties": ["III", "VI", "VII", "IX", "XI", "XII", "XIV", "XV", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIV", "XXV", "XXVI", "XXVIII"],
    "fiches": ["001", "002", "005", "013", "014", "015"]
  }
}
```

**À ajouter** (6 parties et une fiche), avec la raison :

| partie ou fiche | sections | pourquoi | force |
|---|---|---|---|
| VI | § 3 ter | le trio 10 − 1 = 3², 10 + 1 = 11, 10 = 2·5 (M6) ; la dimension d'autosimilarité, qui donne la limite log₂ 3 de T7 ; « un motif propre à la base 10 dit quelque chose de vrai sur le nombre 10 », le verdict de la fiche 013 ; la carte de XXVII donne VI–XIX comme piste | forte |
| XV | § 5 | l'aiguille (3, 1) sur la grille décalée, 7 = N(3 + ω) et (3 + ω)² = 8 + 5ω (M5) ; le théorème des trois distances pour L = 7ᵏ (question 6 du plan) | forte |
| XX | § 6 | le comma, la réduite 19/12 et la gamme à 12 notes (90,22 et 113,69 cents) : le cas log₂ 3 du théorème des trois distances (M3, question 6 du plan) | forte |
| XXIV | § 1 et § 3 | le 4/3 de 1/x₀ = n + 4/3, troisième terme de T7 (question 5 du plan) ; referme un tétraèdre creux | forte |
| XVIII | § 3 et § 8 | le cercle de Gauss (comptage de r₂, le même Fermat que XIX § 2 et XIV § 1) et la phrase « la base ne fait que choisir le pas du grain grossier », à laquelle XIX répond | moyenne |
| fiche 002 | — | le diésis 128/125 est le troisième écart de log₁₀ 2 (N6) ; la fiche l'emploie dans un rapprochement testé « hasard » | moyenne |
| XXII | § 2 | 3ⁿ ≡ 3, 9, 7, 1 (mod 10) : l'horloge de i comptée par les centres de faces du cube ; aucun effet sur le nerf | faible |

**À envisager, plus faible** : XVII (les compagnons de Pell 1, 3, 7, 17, 41, 99, 239 de la famille de N10) ; XXIX § 2.1 et XXX § 2.5, parties d'origine des fiches 001 et 005, que le bloc du plan ne met pas dans ce dossier alors qu'il y met les fiches.

**À retirer : rien.** Chaque partie du bloc porte une section de ce dossier : III (V₃/V₂ et 3 + √2/10, § 2.1 et § 3.4), VII (Kummer et les périodes binaires, chaîne B), IX (les racines dixièmes de l'unité, M1), XI (les trous de l'angle d'or, M3), XII (Carmichael et les rangs d'apparition, § 3.6), XIV (les directions et les convergentes, M3), XIX, XXI (la famille de Pell, N10), XXV (i modulo 50 et 53), XXVI (le diésis, N6), XXVIII (Henderson, Fermat et le 17). Les cinq fiches du bloc restent (§ 4).

**Effet sur le nerf** *(calculé (A), avec le bloc JSON du plan, § 1.9, au niveau « fiches ∪ parties » ; code du § 7.2 ; effet mécanique)*. Les triangles vides passent de 20 à 13, mais les tétraèdres creux passent de 6 à 14 : remplir un triangle crée des cavités d'un étage plus haut (ce que la session lit comme b₂ = 5, `resultats/revision_001.md` § 3). Qui remplit quoi, un ajout à la fois :
- XV remplit bases · corde · grain et bases · grain · ombres ;
- XVIII remplit bases · grain · hasard, bases · grain · lumière et bases · hasard · lumière ;
- XX remplit bases · corde · lumière et bases · lumière · moities ;
- la fiche 002 remplit bases · hasard · lumière ;
- XXIV referme le tétraèdre bases · corde · hasard · moities ;
- VI et XXII ne changent pas le nerf : leur raison est le contenu.

Il reste un triangle vide avec mon dossier, aiguilles · bases · hasard, que mes ajouts ne remplissent pas. Le nerf mesure des appartenances, pas du contenu (T1 : p = 0,395 au niveau 3) : je donne ces nombres pour que l'agent `croisement` sache où mes ajouts agissent, pas comme une preuve.

**Deux pistes de la carte de XXVII que ce dossier relie** (`carte-connexions.md` § 9 et le classement du § 8) : XIV–XX, par le théorème des trois distances que les deux parties citent de XI (M3), et VI–XIX, par le trio 10 − 1 = 3², 10 + 1 = 11, 10 = 2·5 de VI § 3 ter et le i = 3 de XIX § 2 (M6, K3). Les voisins communs que la carte donne pour la première (entre autres XI, XV, XIX et XXVI) disent bien où le lien se trouve.
