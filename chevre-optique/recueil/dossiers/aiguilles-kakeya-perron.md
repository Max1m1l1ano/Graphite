# Dossier aiguilles-kakeya-perron : retourner une aiguille dans peu de place

Dossier de la révision 001, écrit par l'agent « aiguilles » (phase 1). Il suit le gabarit du plan (`recueil/revisions/plan-001.md`, § 7) : ses huit sections sont les § 1 à 8 et répondent aux huit questions de mon entrée. Quatre dossiers sont déjà écrits dans `recueil/dossiers/` (`corde-et-dimensions`, `moities-et-crans`, `bases-congruences-premiers`, `grain-pixels-centres`) : je renvoie à eux.

**Étiquettes.** **démontré** ; **calculé** (fichier `resultats/…` et section) ; **calculé ici** (calcul rapide hors dépôt, repris au § 6.1 et au § 7) ; **classique** (référence au § 6.3) ; **ma lecture** ; **ouvert**. Les chemins sont relatifs à `/home/user/Graphite/chevre-optique` et vérifiés avec `ls`. Aucun script du dépôt n'a été lancé ; j'ai lu `scripts/revision_001.py` (§ 4.7) et `resultats/revision_001.md` (§ 3, 4.7, 5). Les dix figures de ma liste ont été regardées.

## En bref

- **Lien 1 : la demi-case est un seul procédé.** Deux aiguilles voisines de la grille ont un déterminant ±1 : le triangle qu'elles enferment a l'aire ½ et aucun autre point (Pick). C'est le même fait pour Fibonacci, Pell, Farey et le réseau hexagonal (√3/4). Calculé ici pour [a ; a, a, …], a = 1 à 6 : déterminant ±1, écart exact ψᵏ, constante de Hurwitz 1/√(a² + 4). L'or et l'argent sont les deux premiers points du spectre de Markov (classique). En dimension 3, la demi-case ne passe pas (tétraèdres de Reeve).
- **Lien 2 : 2/(k + 2) est un théorème pour l'arbre télescopique, pas pour l'arbre optimal.** XXVIII § 2 le démontre. L'aire minimale est plus basse dès k = 3 : 43/108 contre 2/5 (calculé ici, exact). La fenêtre à 10⁻⁵⁰ est [0,01344 ; 0,02096] ; la constante reste entre π/2 et π·ln 2, un facteur 2 ln 2 = 1,386.
- **Lien 3 : le grain plafonne la profondeur ; K7 tient pour la pente, pas pour les valeurs.** Perron sur n × n : « part × log₂ n » culmine à 2,83 (n = 256), puis baisse jusqu'à 2,57 (n = 65 536) (calculé ici) : le « 2,8 » de XIV § 6 n'est pas une constante. Le Venn coûte exactement √2 par courbe hors du centre, √2·(1 + 1/2n) au centre.
- **Fermés par le calcul.** K2 (les trois 34) : éventails N = 3 à 20, ombre du cube N = 3 à 19. T5 : les plus petits ensembles de Kakeya de F_q², q ≤ 9, ont tous le même profil de multiplicités (§ 7).
- **Trous.** (1) La constante de Kakeya au grain δ. (2) D5 n'avait aucune fiche : six sont proposées (§ 6.1). (3) Données publiées : rapports optimaux des arbres de Perron, constante 3D de Wang et Zahl, minimum de Kakeya fini en dimension ≥ 3 (§ 6.3).
- **Recouvrement.** Ajouter les parties VIII, XI, XV, XXI, XXIX, XXX et la fiche 009 ; ne rien retirer (§ 8).

## 1. La question directrice et la projection sur D1–D8

> Comment le grain plafonne-t-il la descente de Perron et de Kakeya ? Les aiguilles de la grille (Fibonacci, Pell, pythagoriciennes) sont-elles les mêmes réduites que celles des bases et des crans ? (plan, § 1.6)

**Ma réponse, en cinq points.**
1. *Le grain plafonne par un logarithme.* Une branche de largeur 2⁻ᵏ occupe au moins une case : sur n × n, k ≤ log₂ n (XIV § 6). Au grain δ, 1/aire ≤ 1,127 + 1,466·k pour δ = 10⁻ᵏ (Córdoba, XXVI § 1.2).
2. *Oui pour les réduites, par un seul procédé : la demi-case* (§ 3.3). Les bases y entrent par i ≡ a/c (mod b), pour l'aiguille primitive (a, c) de norme b (XIX § 2).
3. *Perron est démontré pour la famille télescopique* ; l'optimum est plus bas (§ 3.2).
4. *Le plafond de Perron et celui du Venn sont à un cran près pour la pente* (K7), pas pour les constantes (§ 3.4).
5. *La moitié de Kakeya fini et celle des hémisphères sont deux procédés* (T5 ; `moities-et-crans` § 5.4). La demi-case de Pick en est un troisième.

**Projection sur D1–D8** (ma lecture ; le plan donnait D5 0,70 et D2, D3, D6 0,10 chacune) :

| dimension | poids | ce qui la porte |
|---|---:|---|
| D5 Kakeya, Perron | 0,55 | V, XIII, XIV, XXVI § 1, XXVIII § 2 |
| D2 bases, congruences | 0,15 | les réduites (XIV § 3–4, XV § 5, XVII § 4, XXVII § 7) ; i ≡ a/c (XIX § 2) |
| D3 grain | 0,12 | XIV § 6, XXVI § 1, fiche 011 |
| D6 cube, Venn | 0,08 | l'ombre du cube (XXVIII § 2.4 et 3.5), fiche 003 |
| D4 optique | 0,07 | Fefferman et le diaphragme (X § 4, XXVIII § 3.3), Fourier fractionnaire (XIII § 4) |
| D8 physique | 0,03 | l'hyperboloïde de l'aiguille qui tourne (XIX § 6) |

Bloc pour le § 1.10 du plan : `"aiguilles-kakeya-perron": {"D5": 0.55, "D2": 0.15, "D3": 0.12, "D6": 0.08, "D4": 0.07, "D8": 0.03}`.

**Notations qui se heurtent.** k : étages de Perron, chiffres du grain (δ = 10⁻ᵏ) ou carré d'une aiguille (XXV) ; n : côté de la grille, dimension de la chèvre ou courbes du Venn ; N : éventails, directions ou lames ; q : corps F_q, q de b = q² + 1 ou dénominateur de réduite ; P : rétrécissement P_j, nombres de Pell P_k ou piquet.

## 2. Les chaînes de production (script → résultats → figures → document)

### 2.1 Partie par partie, dans l'ordre (question 1)

Sections et fonctions sont celles des fichiers, qui ne suivent pas toujours le document (§ 2.3, point 4).

| partie | script | résultats | figure (panneaux) | ce que le script produit |
|---|---|---|---|---|
| V | `scripts/aiguille.py` § 1–4 : `arbre`, `aire_exacte`, `aire_tranches`, `telescope` ; optima k = 3 et 5 (Nelder–Mead) | `resultats/aiguille.md` § 1–4 | `e1_aiguille_kakeya.png` (a–d) | aires des cinq ensembles ; arbre à 2ᵏ branches, exact jusqu'à 64, par tranches jusqu'à 16 384 ; deux optima irréguliers (gains 0,46 et 0,66 %) |
| X § 4 | `scripts/carre_ptolemee.py` : la figure seulement | aucun (le § 4 des résultats est Ptolémée) | `j1_carre_ptolemee.png` (d) | un dessin ; l'argument est de la littérature (Fefferman 1971, Córdoba 1977, Bourgain 1991) |
| XIII § 1, 3, 6 | `scripts/perron_dephasage.py` § 1 (`reconstruit`), § 3 (`arbre`, `signal_perron`, `noeuds_perron`), § 4 (`stft_complet`) ; § 6 du document : aucun calcul | `resultats/perron_dephasage.md` § 1, 3, 4 | `m1_perron_dephasage.png` (a, b, d, e, f) | 12 composantes retrouvent les branchages (0,93 et 0,96) ; 264 nœuds ; loi du nœud pour l'arbre tourné ; Fourier = rotation de 90° |
| XIV | `scripts/aiguille_grille.py` § 1–6 : `points_cercle`, `deltoide`, `det2`, `lambda_ford`, `kakeya_parabole`, `minimum_kakeya`, `arbre`, `cases` | `resultats/aiguille_grille.md` § 1–6 | `n1_aiguille_grille.png` (a–f), `n2_perron_grille.png` (a–c) | directions permises (Jacobi) ; neuf aiguilles de Fibonacci ; Ptolémée de Penner (10 626 quadruplets) ; Kakeya fini (parabole jusqu'à q = 31, minimum exact q ≤ 7) ; Perron sur quatre grilles |
| XVII § 4 | `scripts/recursion_argent.py` § 3 | `resultats/recursion_argent.md` § 3 | `q1_recursion_argent.png` (c, d, e) | fractions de Pell ; facteur 5,83 par aller-retour |
| XIX § 2, 6 | `scripts/bases_objets.py` § 1 (`racines_i`, `aiguilles`), § 4 | `resultats/bases_objets.md` § 1, 4 | `t1_bases_modulaires.png`, `t2_trait_cone_thales.png` (hors liste) | i ≡ a/c pour b = a² + c² (b de 2 à 40) ; hyperboloïdes r² = w₀² + θ²z² |
| XXV § 3 | `scripts/tranche_aiguilles.py` § 5–6 (`reps`, `stations`) | `resultats/tranche_aiguilles.md` § 6 | `z2_tranche_aiguilles.png` (b–e) | tournants des aiguilles de carré 49 à 53 ; r_d(k) ; arrêts perpendiculaires (recomptés ici de 2D à 6D : accord) |
| XXVI § 1, 3.6 | `scripts/kakeya_miroir.py` § 1 (`somme_csc`, `borne_cordoba`, `tubes`, `aire_union`, `meilleur_arbre`) ; § 3.6 : texte | `resultats/kakeya_miroir.md` § 1 | `aa1_kakeya.png` (a–f) | borne π/(1 + 2γ + 2 ln(2/δ)) ; unions de tubes jusqu'à 10⁻⁵ ; tranche 10⁻⁴⁹ à 10⁻⁵⁵ extrapolée |
| XXVII § 7 | `scripts/carte_connexions.py` § 7 | `resultats/carte_connexions.md` § 7 | `ab3_liens_predits.png` (f) | aiguilles de Fibonacci et de Pell, déterminant ±1 |
| XXVIII § 2, 3.3–3.5 | `scripts/octaedre_perron_venn.py` § 2 (`decalages`, `aire_exacte`, `borne_F`, `plateau_ecarts`, `fentes`, `meilleur`, `bas`), § 3 (`aigrettes`) | `resultats/octaedre_perron_venn.md` § 2.1–2.4, 3.3 | `ac2_perron.png` (a–f), `ac3_venn17.png` (e, f) | aire exacte en fractions ; borne F ; plateau jusqu'à k = 16 ; fenêtre de 10⁻¹ à 10⁻¹⁰⁰ ; aigrettes (N = 5, 6, 7, 8, 16, 17, 18) ; éventails N = 16 et 17 |

### 2.2 Cinq chaînes qui se suivent

- **A. Perron** : V § 3 → XIV § 6 (grille) → XXVI § 1 (tubes, Córdoba) → XXVIII § 2 (théorèmes 1 à 4) → XXIX § 4. Chaque maillon reprend la même construction et change ce qu'il compte (aire, cases, tubes).
- **B. Les réduites** : XIV § 1–4 → XV § 5 (Eisenstein) → XVII § 4 → XXVII § 7 (Pell) ; pont vers les bases : XIX § 2, puis XXV § 3.
- **C. Perron et la lumière** : X § 4 (Fefferman) → XIII (Perron tourné) → XXVIII § 3.3–3.5 → XXIX § 5.1. **D. Kakeya fini** : XIV § 5 → T5 → `moities-et-crans` N1. **E. Le grain** : XIV § 6 → XXVI § 1 → XXVIII § 2.5 → fiche 011 : K7.

### 2.3 Les points faibles des chaînes

1. **Deux maillons n'ont pas de donnée** : X § 4 et XIII § 6 (Wolff, 5/2) sont de la littérature citée.
2. **Le code de `arbre` est recopié** dans cinq scripts (`octaedre_perron_venn` l'écrit autrement) : un défaut se propagerait. Mes recalculs retrouvent V (k = 3 et 5), XIV § 6 et XXVIII § 2.2–2.4 : la chaîne A est cohérente.
3. **Les optima de V sont à quatre chiffres** (0,7778 ; 0,5953 ; 0,8602) : la forme exacte, 43/108, y était invisible (fiche A3). XIV § 5 ne calcule le minimum de Kakeya fini que pour q ≤ 7 ; T5 va à 9.
4. **La numérotation diffère entre document et script.** XIX § 2 est la section 1 des résultats ; X § 5 (Ptolémée) la section 4 ; XVII § 4 la section 3 ; XXVIII § 2.4 (le plateau) la section 2.3. Le champ « script (et sa section) » d'une fiche doit citer celle du script.

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 En deux phrases

**Établi** : démontré (XXVIII § 2.2–2.5, XXVI § 1.2, fiche 003), calculé (XIV, XXV § 3, XIII § 1), classique (Fefferman, Córdoba, Pick, Hurwitz, Wolff, Wang et Zahl). **Ouvert** : la constante de Kakeya au grain δ ; l'aire minimale des arbres à 2ᵏ branches (k ≥ 3) ; la cause commune du logarithme (K7) ; la demi-case en dimension 3 ; un Venn 2D à structure de Perron ; le diaphragme de Fibonacci contre Kakeya.

### 3.2 Perron, de « vérifié » à « démontré », et la constante (question 2)

**Démontré dans XXVIII § 2** (α_j entre ½ et 1 ; P_j = α₀…α_{j−1}, le rétrécissement) : (1) l'aire de tout arbre est au plus F = P_k² + 2·Σ_j (P_j − P_{j+1})² (un cœur et des oreilles) ; (2) F ≥ 2/(k + 2), avec égalité aux seuls rapports télescopiques (k + 1)/(k + 2), …, 3/4, 2/3 ; (3) à ces rapports la coupe est un plateau de longueur 1/(k + 2), donc l'aire vaut exactement 2/(k + 2) : la preuve passe par l'ombre du cube {0, 1}ᵏ. Vérifié ici en fractions : l'aire télescopique vaut 2/(k + 2) pour k = 1 à 5, et F majore l'aire de 200 arbres au hasard (0 violation, 72 égalités).

**Ce que « démontré » ne dit pas.** 2/(k + 2) est le minimum de F, pas celui de l'aire. V § 3 et XXVIII § 2.6 l'écrivent ; le résumé de CLAUDE.md § 6 peut se lire autrement (§ 6.2). **Calculé ici** (aire exacte ; Nelder–Mead depuis des départs au hasard ; meilleur trouvé, pas un minimum prouvé) :

| k | branches | 2/(k + 2) | meilleur trouvé | gain | rapports, du plus fin au plus gros |
|---:|---:|---:|---|---:|---|
| 1 | 2 | 0,666667 | 2/3 | 0 | 2/3 |
| 2 | 4 | 0,5 | ½ | 0 | tout un segment (`moities-et-crans`, N2) |
| 3 | 8 | 0,4 | 43/108 = 0,398148 | 0,463 % | 7/9, 25/42, 43/50 |
| 4 | 16 | 0,333333 | 137/414 = 0,330918 | 0,725 % | 56/69, 55/84, 10/11, 137/200 |
| 5 | 32 | 0,285714 | 0,283825 | 0,661 % | 0,840 ; 0,721 ; 0,929 ; 0,598 ; 0,845 |
| 6 | 64 | 0,25 | 0,248324 | 0,670 % | 0,860 ; 0,761 ; 0,942 ; 0,792 ; 0,597 ; 0,853 |

- Les optima de k = 3 et 5 sont ceux de V (`resultats/aiguille.md` § 3). Pour k = 3 et 4, l'aire est un rationnel exact et un minimum local (aucun des 26 voisins à ±1/1000, ni des 80 voisins à ±1/2000, n'est plus bas).
- À chaque optimum (k = 3 à 6), l'aire égale le rétrécissement final P_k : exactement pour k = 3 et 4, à 10⁻⁸ près pour k = 5 et 6. Ce n'est pas une inégalité (140 arbres sur 300 au hasard ont une aire < P_k). Pourquoi aux optima : ouvert.

**La fenêtre et la constante** (`resultats/octaedre_perron_venn.md` § 2.4 ; retrouvée avec mpmath) :

| grain δ | bas (Córdoba) | haut (meilleur nombre N d'éventails) | haut ÷ bas |
|---|---:|---|---:|
| 10⁻¹⁰ | 0,06335 | 0,13379 (N = 5) | 2,112 |
| 10⁻²⁰ | 0,03285 | 0,05830 (N = 8) | 1,775 |
| 10⁻⁵⁰ | 0,01344 | 0,02096 (N = 13) | 1,560 |
| 10⁻¹⁰⁰ | 0,00677 | 0,01003 (N = 21) | 1,481 |

Quand δ → 0, aire × ln(1/δ) est entre π/2 = 1,5708 et π·ln 2 = 2,1776 : rapport limite 2 ln 2 = 1,386. Par décade de grain, 1/aire gagne entre ln 10/(π ln 2) = 1,057 et 2 ln 10/π = 1,466 (0,318 à 0,441 par bit ; fiche A6).

**Que manque-t-il pour la constante ?**
1. *Le bas* est la méthode du second moment : (Σ|T|)²/‖Σχ_T‖₂², avec un recouvrement δ²/sin θ pour chaque paire. Elle serait exacte si la multiplicité Σχ_T était constante sur l'union et si toutes les paires se recouvraient au maximum. Rien ne dit que la meilleure configuration s'en approche, ni qu'elle s'en éloigne.
2. *Le haut* est un arbre télescopique par éventail ; régler les rapports rapporte moins de 0,73 % jusqu'à k = 6 (calculé ici). *Ma lecture* : il faut une autre famille, ou une preuve que celle-ci est optimale.
3. *Les deux côtés se rejoignent comme 1/ln(1/δ)* : 1,56 à 10⁻⁵⁰ devient 1,48 à 10⁻¹⁰⁰. Les données à δ fini ne donnent pas la constante : aire × ln(1/δ) des unions calculées monte à 2,97 puis redescend à 2,88 (XXVI § 1.3).
4. Je ne connais pas de publication qui donne la constante, ni qui prouve que la limite existe (à vérifier).

*À calculer* : le minimum exact de l'aire de N tubes sur une grille fine, pour de petits N (programmation en nombres entiers, comme T5), pour placer le vrai minimum dans la fenêtre.

### 3.3 La demi-case, procédé commun (question 3)

**Le procédé.** Deux vecteurs v, w d'un réseau de rang 2 en forment une base si et seulement si le triangle (0, v, w) a pour aire la moitié du covolume ; il ne contient alors aucun autre point du réseau (Pick, pour tout réseau par une application affine). Pour ℤ² : det(v, w) = ±1, aire ½, la demi-case de XIV § 2 : une aiguille qui tourne de v à w balaie au moins ce triangle.

| objet (où) | réseau | paire | quantum | loi de l'écart |
|---|---|---|---|---|
| Fibonacci, [1 ; 1, 1, …] (XIV § 3) | ℤ² | (F_k, F_{k+1}) | ½ | (−1/φ)ᵏ ; angle × longueur² → 1/√5 |
| Pell, [2 ; 2, 2, …] (XXVII § 7, XVII § 4) | ℤ² | (P_k, P_{k+1}) | ½ | (1 − √2)ᵏ ; → 1/√8 |
| a = 3 à 6 (calculé ici) | ℤ² | (1, 3), (3, 10), (10, 33)… pour a = 3 | ½ | ψ_aᵏ ; → 1/√(a² + 4) |
| Farey, Ford, Pick (XIV § 3–4) | ℤ² | voisines p/q, r/s ; triangle vide | ½ | λ de Penner = det ; Ptolémée = Plücker |
| Eisenstein (XV § 5) | A₂, maille 1 | base du réseau | √3/4 | trois distances pour L = 7ᵏ (triangle 5-7-8) |
| i ≡ a/c (XIX § 2) | ℤ/b | aiguille primitive (a, c) | b = a² + c² | quart de tour = × i modulo b |

**Partagé exactement.** La base du réseau : det = ±1 ⟺ aire = covol/2 ⟺ triangle vide ⟺ voisines de Farey ⟺ réduites consécutives (v_{k+1} = a·v_k + v_{k−1}).
**Transporté.** (1) Le quantum de rotation (XIV § 2). (2) La loi de l'écart : pour [a ; a, a, …], l'écart de la k-ième aiguille à la droite limite vaut exactement ψᵏ, avec ψ = −1/λ_a et λ_a = (a + √(a² + 4))/2 (calculé ici, a = 1 à 6, 40 chiffres : |det| = 1, écart exact, constante de Hurwitz 1/√(a² + 4)). (3) Ptolémée = Plücker : λ₁₃λ₂₄ = λ₁₂λ₃₄ + λ₁₄λ₂₃ (XIV § 4). (4) Vers les bases : la rotation de 90° de la grille repliée est × i modulo b (XIX § 2).
**Pourquoi l'or et l'argent seuls** (classique ; le lien avec le corpus est ma lecture). 1/√5 et 1/√8 sont les inverses des deux premières valeurs du spectre de Lagrange (Hurwitz 1891 ; Markov 1879–1880) : ce sont les deux directions que la grille approche le plus mal (XIV § 3). Les a ≥ 3 donnent √13, √20… hors de la partie discrète du spectre.
**Ouvert.** (a) *Dimension 3* : un tétraèdre vide n'y est pas unimodulaire. Les sommets (0,0,0), (1,0,0), (0,1,0), (1,1,r) n'ont aucun autre point du réseau et le volume vaut r/6 (calculé ici, r = 1 à 7 ; Reeve 1957). Pour une aiguille de ℤ³ qui tourne dans un plan de normale primitive n, le quantum est |n|/2 (covolume du réseau du plan, classique) : il dépend du plan. (b) La demi-case et la « moitié du plan » de Kakeya fini ont chacune leur procédé (Pick ; Bonferroni) : XIV § 7 le disait déjà.

### 3.4 K7 : le grain plafonne Perron et le Venn (question 4)

**Exactement un cran ? Non.** Un cran (facteur 2 sur l'exposant, √2 sur la longueur) est la pente limite ; à taille finie les valeurs s'en écartent. Calculé ici : Perron sur n × n (arbres télescopiques, comme XIV § 6) et le Venn au centre (fiche 011 : W_centre(n) = (2/π)·√(n(2ⁿ − 2)), qui redonne 2 009 px à n = 19).

| n = W (px) | meilleur k | part du triangle | part × log₂ n | n_max du Venn (centre) | rapport Venn ÷ k |
|---:|---:|---:|---:|---:|---:|
| 16 | 2 | 0,6221 | 2,488 | 6,61 | 3,30 |
| 64 | 4 | 0,4629 | 2,777 | 9,99 | 2,50 |
| 256 | 5 | 0,3533 | 2,826 | 13,54 | 2,71 |
| 1 024 | 7 | 0,2754 | 2,754 | 17,20 | 2,46 |
| 4 096 | 9 | 0,2241 | 2,689 | 20,92 | 2,32 |
| 16 384 | 10 | 0,1878 | 2,629 | 24,68 | 2,47 |
| 65 536 | 12 | 0,1607 | 2,571 | 28,47 | 2,37 |

(Lignes 1 à 4 : `resultats/aiguille_grille.md` § 6 ; lignes 5 à 7 : nouvelles.)

1. *Le « 2,8 » n'est pas une constante.* « Part × log₂ n » culmine à 2,83 (n = 256), puis perd 0,06 chaque fois que n est multiplié par 4. *Ma lecture* : avec k ≈ log₂ n − c, la part suit 2/(k + 2) à un facteur de grille près (1,13 à 1,39 ici), et le produit tend vers 2. XXVI § 1.3 a la même bosse.
2. *Venn : un cran exact hors du centre, un peu plus au centre.* La largeur « pour le reste » (4·√((2ⁿ − 2)/π)) est multipliée par √2 par courbe à 6·10⁻⁵ près dès n = 13 ; celle du centre par √2·(1 + 1/(2n)) : +3,8 % à n = 13, +2,6 % à 19, +2,0 % à 25. C'est le √n de K10 (`grain-pixels-centres` § 3.4).
3. *Perron gagne 0,83 à 0,88 étage par bit de grille, pas 1* (k = 2, 4, 5, 7, 9, 10, 12 pour log₂ n = 4 à 16) : log₂ n − k passe de 2 à 4.

K7 se recolle pour la pente, à 20 % près à taille finie ; l'obstruction est au second ordre (√n d'un côté, le décalage de k de l'autre). La cause commune du logarithme reste ouverte (`grain-pixels-centres` § 5.1).

### 3.5 Kakeya fini, T5 (question 5)

**Blokhuis et Mazzocca (2008)**, d'après des extraits lus en ligne (à vérifier dans le texte) : pour q impair, un ensemble de Kakeya de AG(2, q) a au moins q(q + 1)/2 + (q − 1)/2 points, borne atteinte (les ensembles extrémaux viennent de coniques duales) ; Faber (2005) l'avait conjecturé. **Pour q pair** (classique ; la classification des petits ensembles est à vérifier) : le minimum est q(q + 1)/2, borne de Bonferroni et de Dvir (C(q + 1, 2) pour n = 2), atteinte par le dual d'une hyperovale. Ces ensembles n'existent que pour q pair : un ensemble de q(q + 1)/2 points n'a aucun point triple, donc ses q + 1 droites et la droite de l'infini forment un arc dual de q + 2 droites, et pour q impair un arc a au plus q + 1 points (Bose 1947).

**Calculé ici** (§ 7 : toutes les familles de q + 1 droites de directions distinctes, à symétrie près). Les minima sont ceux de `resultats/revision_001.md` § 4.7, et tous les minimiseurs ont le même profil :

| q | minimum | minimiseurs normalisés | points sur 1, 2, 3 droites |
|---:|---:|---:|---|
| 2 | 3 | 1 | 0, 3, 0 |
| 3 | 7 | 5 | 3, 3, 1 |
| 4 | 10 | 1 | 0, 10, 0 |
| 5 | 17 | 39 | 6, 9, 2 |
| 7 | 31 | 71 | 9, 19, 3 |
| 8 | 36 | 10 | 0, 36, 0 |
| 9 | 49 | 111 | 12, 33, 4 |

q pair : tous les points sont doubles. q impair : (q − 1)/2 points triples, 3(q − 1)/2 simples, aucun point sur quatre droites. L'identité n₁ = Σ_{j≥3} j(j − 2)·n_j vaut pour toute famille (elle vient de Σ n_j·j = q(q + 1) et Σ n_j·C(j, 2) = C(q + 1, 2)). **Verdict** : la piste XIV–XX se ferme par une obstruction (`moities-et-crans` § 5.4) ; l'involution a ↦ −a n'explique que l'excès, qui est le nombre de points triples.

### 3.6 Deux pistes de la carte (XXVII § 9)

- **XIV–XXIV** : XXV § 3 (figure z2, e) fait passer l'aiguille à ≈ 1/(n + 4/3) radian de la chèvre de dimension n : le n + 4/3 de XXIV. Établi par XXV ; ce n'est pas la demi-case.
- **V–IX** : fermée en partie par XXVIII § 3.3 (Fefferman, Córdoba) ; ouverte pour le diaphragme de Fibonacci.

## 4. Les fiches du dossier : verdict, test, et la partie qui portait déjà le lien

**Fiche 003 — 34·tan(π/34) ≈ π, à 2 856 ppm.**
- *Verdict* : juste, à garder (« structure »). 34·tan(π/34) est le coefficient 2N·tan(π/2N) de la fenêtre de Kakeya pour N = 17 éventails : l'aire du 34-gone circonscrit (XXVIII § 2.5).
- *Test* : « faire varier le paramètre », refait ici : 2 855,7 ppm à N = 17 ; écart × N² = 2,5927 (17), 2,5839 (170 et 1 700), π³/12 = 2,58386.
- *La partie qui portait déjà le lien* : XXVIII § 2.5 (le 34-gone, 3,1506) et le tableau « N éventails, 2N·tan(π/2N), écart à π, π²/(12N²) » de `resultats/octaedre_perron_venn.md` § 2.4 : la ligne N = 17 donne 0,2856 % contre 0,2846 %.
- *Place dans les arbres* : P1, branche Perron (le 34-gone des 17 éventails est le contour de l'ombre Σωⁱ, XXIX § 5.4). P3, branche du polygone circonscrit (la forme x³/3 de tan, contre x³/6 de sin pour le polygone inscrit de la fiche 002 ; ma lecture). **Rôle ici : le prix du nombre d'éventails.** Le coefficient de 17 éventails est à 0,29 % de π (N → ∞) ; la fenêtre est large de 56 % à 10⁻⁵⁰ : le nombre d'éventails n'est pas la cause de l'écart.

**Fiche 011 — à 2 000 px, le centre du Venn à 19 courbes est à la limite.**
- *Verdict* : calculé, juste. Je retrouve W_centre(19) = 2 009 px et W_reste(19) = 1 634 px (XXX § 6.4).
- *Test* : la loi W_centre(n) = (2/π)·√(n(2ⁿ − 2)). K7 la lit comme un écart à un cran : +2,6 % par courbe à n = 19 (§ 3.4).
- *La partie qui portait déjà le lien* : XXX § 6.4 (« Analogie de structure : Perron sur une grille ») et XIV § 6. Le plan lit le lien « à un cran près » ; K7 le précise.
- *Place dans les arbres* : P5, branche du Venn (XXIX § 4 → XXX § 6.4 → 011). P3 par K10 (le seuil √(n/4π)). Pas dans P1.

**Fiche 009 — 34 + 34 aigrettes (à ajouter à ce dossier).** Juste. C'est le troisième objet de K2 (§ 5.1) : les aigrettes d'un diaphragme à N lames et les N éventails de Perron dépendent de la même parité (XXVIII § 3.3–3.4). L'ajouter crée deux triangles vides au niveau des fiches (§ 8) : des fiches à écrire.

## 5. Les congruences et les obstructions

### 5.1 Celles du plan, côté aiguilles

- **K2, les trois 34, modulo 2 : section globale, fermée** (calculé ici). Éventails d'ouverture π/N aux angles 2πj/N : N impair, chaque direction exactement une fois ; N pair, la moitié deux fois et l'autre jamais (N = 3 à 20). Ombre Σωⁱ du cube {0, 1}ᴺ : contour à 2N côtés (N impair) ou N (N pair) (N = 3 à 19). Aigrettes : 10, 6, 14, 8, 16, 34, 18 pour N = 5, 6, 7, 8, 16, 17, 18 (XXVIII § 3.3). Les trois se lisent sur le même nombre : les droites distinctes parmi les ωⁱ, N (N impair) ou N/2 (N pair), doublé pour les côtés et les aigrettes. Pas d'obstruction. Mais la parité ne contraint pas Kakeya : avec des axes πj/N, tout N convient.
- **K4 : obstruction confirmée** par T5 (§ 3.5). **K7 : recollé pour la pente, obstruction au second ordre** (§ 3.4).

### 5.2 Mes congruences

- **M1. La demi-case : un cocycle fermé pour chaque pas, pas pour les limites.** Les sections sont les chaînes de bases de ℤ² (Fibonacci, Pell, a ≥ 3, Farey). Le pas v_{k+1} = a·v_k + v_{k−1} a pour matrice [[0, 1], [1, a]] dans GL₂(ℤ) ; composer deux pas reste dans GL₂(ℤ), donc le cocycle se ferme. L'obstruction est à la limite : φ et 1 + √2 n'ont pas la même queue de fraction continue, donc ne sont pas équivalents sous GL₂(ℤ) (classique). Deux sections locales identiques, deux orbites : 1/√5 et 1/√8.
- **M2. i ≡ a/c (mod b) et l'aiguille (a, c).** Se recolle entièrement (XIX § 2 ; `bases-congruences-premiers` § 3.1).
- **M3. Perron et le Venn : un cube, deux ombres** (XXVIII § 3.5, XXIX § 5.1). Se recolle sur {0, 1}ⁿ ; obstruction : binaire (2^(k−j) fentes) contre binomiale (C(n, l)). À suivre dans `ombres-cube-venn`.
- **M4. Les deux constantes de Kakeya.** Se recollent à l'ordre 1/ln(1/δ) ; obstruction : le facteur 2 ln 2 (§ 3.2).

### 5.3 Les obstructions et les trous qu'elles désignent

| éléments | le trou | où chercher |
|---|---|---|
| bas π/2, haut π·ln 2 (M4) | la constante de Kakeya au grain δ | minima exacts de petits N en nombres entiers ; profil de multiplicité des tubes |
| Venn au centre, Perron (K7) | √n d'un côté, décalage de k de l'autre | Perron à rapports optimisés sur n ≥ 4 096 ; Venn à 23 courbes (certificats de 889 Mo, non téléchargés) |
| demi-case en ℤ³ | le quantum ‖n‖/2 dépend du plan | énumérer les plans de rotation des aiguilles de carré 49 à 55 (XXV § 3) et calculer ‖n‖ (norme de la normale primitive) |
| Perron, Venn (M3) | pas de Venn 2D à structure de Perron | un dessin dont les veines seraient binaires (XXIX § 5.1) |

## 6. Les trous

### 6.1 Les trous du recueil : six fiches nouvelles, toutes en D5

D5 n'a aucune fiche principale (plan, § 6.1). Les numéros A1 à A6 sont ceux de ce dossier. Elles ne répètent pas les brouillons 016 à 021 de la session (A5 complète le 019).

**A1. La demi-case est le même procédé pour l'or, l'argent, Farey, Pick et l'hexagone.** *Type* : Analogie. *Statut* : structure. *Partie* : XIV § 2–4, XXVII § 7. *Script* : `scripts/aiguille_grille.py` § 3–4, `scripts/carte_connexions.py` § 7 ; a = 1 à 6 : à ajouter à `scripts/revision_001.py`. *Image* : `figures/n1_aiguille_grille.png` (d, e), `figures/ab3_liens_predits.png` (f). *Dimension* : D5 (D2). *Test* : variation de a dans [a ; a, a, …].
Pour a = 1 à 6, deux aiguilles voisines ont un déterminant ±1, l'écart exact ψᵏ et la constante de Hurwitz 1/√(a² + 4) (calculé ici). Partagé : la base du réseau. Transporté : le quantum de rotation, la loi de l'écart, Ptolémée = Plücker. Ouvert : la dimension 3 (Reeve). Contexte : XXVII § 7 l'écrit pour l'or et l'argent seulement.

**A2. Les N éventails de Perron, l'ombre Σωⁱ et les aigrettes comptent les mêmes droites.** *Type* : Analogie. *Statut* : exact (2 est inversible modulo N impair ; contrôlé numériquement). *Partie* : XXVIII § 3.3–3.4, XXIX § 5.4. *Script* : `scripts/octaedre_perron_venn.py` § 3 (aigrettes) ; éventails et ombre : à ajouter à `scripts/revision_001.py`. *Image* : `figures/ac3_venn17.png` (e, f). *Dimension* : D5 (D6, D4). *Test* : variation de N.
N impair, les éventails couvrent chaque direction une fois ; N pair, la moitié deux fois, l'autre jamais (N = 3 à 20). Le contour de l'ombre a 2N côtés (N impair) ou N (N pair) (N = 3 à 19). Contexte : K2 du plan, « à faire, léger ».

**A3. L'arbre de Perron à 8 branches fait mieux que 2/(k + 2) : 43/108.** *Type* : Fait amusant. *Statut* : calculé (exact en fractions ; minimum local). *Partie* : V § 3, XXVIII § 2.6. *Script* : `scripts/aiguille.py` § 3 (`aire_exacte`, optimisation). *Image* : `figures/e1_aiguille_kakeya.png` (c). *Dimension* : D5. *Test* : précision poussée (fractions) et voisinage.
Rapports (7/9, 25/42, 43/50), aire 43/108 = 0,398148, soit 1/216 de moins que 2/5. Pour k = 4 : (56/69, 55/84, 10/11, 137/200), 137/414, soit 1/138 de moins. À chaque optimum trouvé (k = 3 à 6), l'aire égale P_k ; ce n'est pas une inégalité générale.

**A4. Perron sur une grille : « part × log₂ n » culmine à 2,83 puis baisse.** *Type* : Fait amusant ; Corrélation. *Statut* : calculé. *Partie* : XIV § 6, XXX § 6.4. *Script* : `scripts/aiguille_grille.py` § 6 (`arbre`, `cases`) ; grilles de 4 096 à 65 536 : à ajouter. *Image* : `figures/n2_perron_grille.png` (c). *Dimension* : D3 (D5). *Test* : variation de n de 16 à 65 536.
Le tableau du § 3.4 (2,49 ; 2,78 ; 2,83 ; 2,75 ; 2,69 ; 2,63 ; 2,57). Le « 2,8 » est le sommet d'une bosse. Le rapport des profondeurs Venn ÷ Perron va de 3,3 à 2,4 : un cran à 20 % près. À fusionner avec la N6 de `grain-pixels-centres`, qui demandait ces points.

**A5. Tous les plus petits ensembles de Kakeya de F_q² (q ≤ 9) ont le même profil.** *Type* : Fait amusant. *Statut* : exact (énumération exhaustive à symétrie fixée). *Partie* : XIV § 5. *Script* : `scripts/aiguille_grille.py` § 5 (`minimum_kakeya`), `scripts/revision_001.py` § 4.7. *Image* : `figures/n1_aiguille_grille.png` (f). *Dimension* : D5 (D6). *Test* : variation de q et de la caractéristique.
q pair : tous les points sont doubles ; q impair : (q − 1)/2 points triples, 3(q − 1)/2 simples, aucun point sur quatre droites (§ 3.5). Contexte : complète le brouillon 019 (Bonferroni), qui donne le minimum, pas le profil.

**A6. Kakeya lit les chiffres du grain : 1/aire gagne entre 1,057 et 1,466 par décade.** *Type* : Analogie. *Statut* : démontré (les deux bornes). *Partie* : XXVI § 1.2, XXVIII § 2.5. *Script* : `scripts/octaedre_perron_venn.py` § 2 (`bas`, `meilleur`). *Image* : `figures/ac2_perron.png` (f). *Dimension* : D5 (D3). *Test* : loi de l'écart du rapport haut ÷ bas (2,11 ; 1,78 ; 1,56 ; 1,48 à 10⁻¹⁰, 10⁻²⁰, 10⁻⁵⁰, 10⁻¹⁰⁰, vers 1,386).
XXVI § 1.2 écrivait la pente haute, 1,466 ; la pente basse, ln 10/(π ln 2) = 1,057, vient de la constante π·ln 2 de XXVIII § 2.5. Les deux couches de la partie XIX : la chèvre lit 10⁻ᵏ, Kakeya lit k.

### 6.2 Les trous du corpus : imprécisions trouvées

1. **XIV § 6** (et `resultats/aiguille_grille.md` § 6) : « son produit par log₂ n reste presque constant, vers 2,8 ». Il culmine à 2,83 (n = 256), puis baisse jusqu'à 2,57 (n = 65 536) : § 3.4. Le dossier `grain-pixels-centres` reprend le « 2,8 ».
2. **CLAUDE.md § 6**, partie XXVIII : « minimum 2/(k + 2) aux seuls rapports télescopiques ». C'est le minimum de la borne F ; l'aire minimale est plus basse dès k = 3 (43/108 < 2/5). Même nuance pour l'« En bref » de XXVIII (« démontrée pour tout k ») : le théorème porte sur la famille télescopique, ce que XXVIII § 2.6 dit.
3. **Numérotation** : résultats et scripts de X, XVII, XIX et XXVIII n'ont pas celle du document (§ 2.3, point 4).
4. **« Córdoba (1977) »** désigne deux articles : *Amer. J. Math.* 99, 1–22 (la fonction maximale de Kakeya, la borne du bas) et *Ann. of Math.* 105, 581–588 (le multiplicateur du polygone). Les parties V, X et XIV citent le premier, les sources de XXVIII le second ; XXVI et XXVIII § 3.3 ne distinguent pas.

### 6.3 Les trous des données publiées (question 8)

- **Keich 1999.** La borne de Córdoba et la construction de Schoenberg donnent l'ordre 1/ln(1/δ) ; Keich montre que les bornes L^p de Córdoba et de Bourgain ne s'améliorent pas (à vérifier : énoncé exact). *Ouvert* : la constante (§ 3.2) ; pas de valeur publiée à ma connaissance.
- **Wang et Zahl 2025.** Dimension 3 pour tout ensemble de Kakeya de ℝ³. *Ouvert* : leur borne a la forme c_ε·δ^ε et c_ε n'est pas explicite (XXVI § 1.5), donc pas de fenêtre à 10⁻⁵⁰ en 3D ; la perte réelle (en log ou en δ^ε) ; la dimension ≥ 4 (à vérifier).
- **Dvir 2009.** |K| ≥ C(q + n − 1, n) dans F_qⁿ ; pour n = 2, c'est q(q + 1)/2, exact pour q pair. *Ouvert* : le minimum exact pour n ≥ 3 ; Dvir, Kopparty, Saraf et Sudan donnent (q/(2 − 1/q))ⁿ, et les constructions sont à un facteur 2 près (XIV § 5).
- **Les rapports optimaux des arbres de Perron** : je n'ai pas trouvé de publication ; si elle n'existe pas, les valeurs du § 3.2 sont nouvelles (à vérifier).
- **Kakeya fini, q pair** : le minimum est classique ; la classification des petits ensembles est dans Blokhuis, De Boeck, Mazzocca et Storme (à vérifier : revue, année). **Demi-case en dimension ≥ 3** : Reeve 1957 ; White 1964 pour les tétraèdres vides (à vérifier).

**Références.** Córdoba, *Amer. J. Math.* 99, 1–22 (1977) et *Ann. of Math.* 105, 581–588 (1977). Fefferman, *Ann. of Math.* 94, 330–336 (1971). Bourgain, *GAFA* 1, 147–187 (1991). Keich, *Bull. London Math. Soc.* 31, 213–221 (1999). Wolff, *Rev. Mat. Iberoam.* 11, 651–674 (1995). Wang, Zahl, arXiv:2502.17655 (2025). Dvir, *J. Amer. Math. Soc.* 22, 1093–1097 (2009). Dvir, Kopparty, Saraf, Sudan, *SIAM J. Comput.* 42(6) (2013) (pages à vérifier). Blokhuis, Mazzocca, *Building Bridges*, Bolyai Soc. Math. Stud. 19, 205–218 (2008). Faber, arXiv:math/0510356 (2005). Bose, *Sankhyā* 8, 107–166 (1947). Pick (1899). Hurwitz, *Math. Ann.* 39, 279–284 (1891). Farey, Ford, Penner : comme en XIV. Markov, *Math. Ann.* 15 (1879) et 17 (1880) (pages à vérifier). Cusick, Flahive, *The Markoff and Lagrange Spectra*, AMS (1989). Reeve, *Proc. London Math. Soc.* (3) 7, 378–395 (1957). White, *Canad. J. Math.* 16, 389–396 (1964) (à vérifier).

## 7. Le code minimal du test qui me concerne (T5)

`scripts/revision_001.py` a déjà, au § 4.7, le minimum exact par programmation en nombres entiers (`minimum_kakeya_fq`, q = 2 à 9), et `moities-et-crans` § 7.1 les constructions explicites. Ce code ajoute **tous** les minimiseurs, à symétrie près, et leur profil de multiplicités. Si une assertion échoue pour un q, le profil du § 3.5 est faux pour ce q. Il est autonome ; lancé dans un dossier temporaire, il passe pour q = 2, 3, 4, 5, 7, 8 et 9 en 3 s *(calculé ici)*. Au-delà (q = 11 : 11⁹·2 familles), il faut le MILP avec une limite de temps, sans lire un statut « limite atteinte » comme un minimum.

```python
"""T5 (agent aiguilles) : tous les plus petits ensembles de Kakeya de F_q^2, à symétrie près (q = 2 à 9).
Symétrie : translations et homothéties imposent x = 0 (direction verticale), y = 0 (pente 0) et y = x + c (pente 1, c = 0 ou 1)."""
import itertools
from collections import Counter

POLY = {4: (2, [1, 1]), 8: (2, [1, 1, 0]), 9: (3, [1, 0])}      # x^e = -(c_0 + c_1 x + ...) : x²+x+1, x³+x+1, x²+1


def corps(q):
    """Tables d'addition et de multiplication de F_q ; un élément est un entier 0..q-1 (chiffres en base p)."""
    p, c = POLY.get(q, (q, [0]))
    e = len(c)
    dig = lambda a: [(a // p ** i) % p for i in range(e)]
    val = lambda d: sum(x * p ** i for i, x in enumerate(d))

    def mul(a, b):
        r = [0] * (2 * e - 1)
        for i, x in enumerate(dig(a)):
            for j, y in enumerate(dig(b)):
                r[i + j] = (r[i + j] + x * y) % p
        for k in range(2 * e - 2, e - 1, -1):                     # réduction par x^e = -sum c_i x^i
            t, r[k] = r[k], 0
            for i in range(e):
                r[k - e + i] = (r[k - e + i] - t * c[i]) % p
        return val(r[:e])

    add = [[val([(x + y) % p for x, y in zip(dig(a), dig(b))]) for b in range(q)] for a in range(q)]
    return add, [[mul(a, b) for b in range(q)] for a in range(q)]


def optima(q):
    """((minimum, nombre de minimiseurs normalisés), {(n1, n2, n3, n4) : nombre}) ; n_j = points sur exactement j droites."""
    add, mul = corps(q)
    bit = lambda x, y: 1 << (x * q + y)
    D = {m: [sum(bit(x, add[mul[m][x]][c]) for x in range(q)) for c in range(q)] for m in range(q)}   # y = m x + c
    D["v"] = [sum(bit(c, y) for y in range(q)) for c in range(q)]                                       # x = c
    fixes = [[D["v"][0]], [D[0][0]], [D[1][0], D[1][1]]]
    libres = [D[m] for m in range(2, q)]                                                                # les q - 2 autres directions
    best, nb, profils = None, 0, Counter()
    for f in itertools.product(*fixes):
        base = f[0] | f[1] | f[2]
        for g in itertools.product(*libres):
            u = base
            for m in g:
                u |= m
            s = u.bit_count()
            if best is None or s < best:
                best, nb, profils = s, 0, Counter()
            if s == best:
                nb += 1
                lignes = list(f) + list(g)
                mult = Counter(sum((m >> i) & 1 for m in lignes) for i in range(q * q) if (u >> i) & 1)
                profils[tuple(mult.get(j, 0) for j in (1, 2, 3, 4))] += 1
    return (best, nb), profils


if __name__ == "__main__":
    for q in (2, 3, 4, 5, 7, 8, 9):
        (s, nb), profils = optima(q)
        n1, n2, n3 = (3 * (q - 1) // 2, (q * q - 2 * q + 3) // 2, (q - 1) // 2) if q % 2 else (0, q * (q + 1) // 2, 0)
        assert s == q * (q + 1) // 2 + n3, (q, s)                      # q(q+1)/2 + (q-1)/2 si q impair, q(q+1)/2 si q pair
        assert set(profils) == {(n1, n2, n3, 0)}, (q, dict(profils))   # un seul profil, jamais de point sur 4 droites
        assert n1 == 3 * n3                                            # n1 = somme_j j(j-2) n_j, ici n_j = 0 pour j >= 4
        print(q, s, nb, dict(profils))
```

## 8. Les corrections au recouvrement (bloc JSON du § 1.9 du plan)

```json
"aiguilles-kakeya-perron": {
  "parties": ["V", "VIII", "X", "XI", "XIII", "XIV", "XV", "XVII", "XIX", "XXI", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"],
  "fiches": ["003", "009", "011"]
}
```

**À ajouter** : les parties VIII, XI, XV, XXI, XXIX, XXX et la fiche 009. **À retirer** : rien (chaque partie de la liste a un maillon du § 2.1 ; les fiches 003 et 011 restent, § 4). **À envisager** : XX (§ 4 : retourner l'aiguille, i·i = −1, que XXV § 3 compte) et VI (le triangle de Pál est le simplexe de dimension 2, V § 2).

| ajout | sections | raison | force |
|---|---|---|---|
| XV | § 5 | Eisenstein et la demi-case de l'hexagone (question 3) ; branche « aiguilles de la grille » de P6 | forte |
| XXIX | § 4, 5.1 | un bit par pas ; Perron et Venn, deux ombres : le plan met XXIX § 5.1 dans P1 | forte |
| XXX | § 6.4 | la fiche 011 est dans ce dossier, pas sa partie ; K7 | forte |
| VIII | § 1 | trois façons de retourner l'aiguille, le foyer : la scène de XIV § 2 | moyenne |
| XI | § 2, 4 | théorème des trois distances, petites aiguilles du spectre : XIV § 1 et XV § 5 s'en servent | moyenne |
| XXI | § 2 | l'aiguille de 50 et 7-24-25, d'où part XXV § 3 | moyenne |
| fiche 009 | — | K2 (aigrettes) | moyenne ; deux triangles vides de plus au niveau des fiches |

**Effet sur le nerf** (recalculé ici hors dépôt ; je retrouve ceux du plan : niveau fiches, 18 paires et 9 triangles vides ; niveau fiches + parties, 28 paires et 20 vides, 11 tétraèdres dont 6 creux). Effet mécanique, pas une preuve (T1 : p = 0,395 au niveau 3).

| recouvrement des autres dossiers | niveau fiches : vides | niveau fiches + parties : vides, tétraèdres creux |
|---|---:|---|
| v1 du plan, aiguilles au plan | 9 | 20, 6 |
| v1, + XV, XXIX, XXX | 9 | 16, 3 |
| v1, + ma proposition | 11 | 15, 1 |
| les quatre propositions écrites, aiguilles au plan | 11 | 2, 15 |
| idem, + ma proposition | 13 | 2, 10 |
| idem, + XIII dans `bases-congruences-premiers` | 13 | 1, 14 |

Les deux triangles vides que crée la fiche 009 (niveau fiches) sont (aiguilles, grain, lumière) et (aiguilles, lumière, méthode) : des fiches à écrire. Le triangle vide qui reste au niveau 3 est (aiguilles, bases, méthode) : il se remplit si `bases` ajoute XIII (son § 5 teste les bases 2, 10, 12 et 60), ou si ce dossier ajoute VI, XVIII ou XXIV.
