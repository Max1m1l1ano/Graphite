# Dossier hasard-et-methode : le hasard, la méthode et les chaînes de données

Dossier de la révision 001, écrit par l'agent « methode » (phase 2), d'après le plan (`recueil/revisions/plan-001.md`, § 7). Les huit sections sont les § 1 à 8 ; le tableau des quinze fiches est le § 4. Les six dossiers de la phase 1 sont lus et cités, pas répétés ; `ombres-cube-venn`, écrit en même temps, est lu en dernier. **Étiquettes** : **démontré** ; **calculé** (fichier `resultats/…`) ; **calculé ici** (calcul rapide hors dépôt, code au § 7 ou en § 3.6) ; **classique** ; **ma lecture** ; **ouvert**. Chemins vérifiés avec `ls`. Aucun script du dépôt lancé ; les quatre figures de ma liste regardées.

## En bref

- **Lien 1 : les tests à tolérance sont des seuils sur l'écart seul.** Rangés par écart, les six cas non triviaux du banc de XXX § 7 alternent S C S S S C : aucun seuil ne les sépare. Ils jugent un ensemble (excès à 0,3 %, p = 0,03), pas une paire. Le « 10/10 » de la variation du paramètre est en partie écrit en dur (§ 3.2).
- **Lien 2 : le cadre fabrique des liens.** p_a + p_b < Σp² est le problème des doubles zéros ; selon le classement, de 0 à 21 paires sont « liées » (3 dans le recueil) ; Ochiai n'en voit aucune (§ 3.4).
- **Lien 3 : dix-huit erreurs de chaîne, cinq classes.** Le cadre est la plus fréquente (6) et aucun test ne la voit (§ 3.3).
- **Lien 4 : une intervention sur un Venn à 13 courbes** (palette connue, rendu refait ici, § 3.6). La palette déplace le centre comme G·H₁(poids) le prévoit, G lu dans le SVG (2,05 à 2,20 px observés selon le rendu, 2,08 prédits) ; décalée de 4 courbes, elle le tourne de −109,5° (prédit −110,8°). L'ordre de dessin le déplace de 0,3 px au plus : le « X » du modèle à deux causes n'est pas l'ordre.
- **Les quinze fiches** (§ 4) : dix bons tests sans réserve, cinq avec ; aucun budget ne casse, cinq énoncés dépassent leur test.
- **Trou 1 : T8 n'a pas de signal**, ni en v1 (ρ = −0,035) ni en v2 (+0,090, p = 0,23) ; les deux méthodes ne sont pas indépendantes en v1 (rapport des chances 1,69, p = 0,024), et en v2 le plafond (91 % des paires non reliées partagent un dossier) ôte la puissance (1,60, p = 0,25) (§ 3.5). **Trou 2 : δ₂ ≈ δ₃ n'est pas un « hasard » testé** : 2·10⁻⁴, contre 0,61 pour la fiche 002 (§ 3.8). **Trou 3 : la palette de l'image à 17 courbes**, et un banc à vérités indépendantes (§ 5, § 6.3).
- **Recouvrement** : ajouter les parties I, V, X, XIV, XXII, XXIII, XXV et la fiche 006 ; ne rien retirer (§ 8).

## 1. La question directrice et la projection sur D1–D8

> Pour chaque observation, quelle technique de test convient (la table du § 10 de CLAUDE.md) ? Le verdict reste-t-il dans le budget de la donnée ? Où les chaînes de production de données du corpus ont-elles accumulé, puis corrigé, des erreurs ? (plan, § 1.8)

**Ma réponse** : l'« En bref » ci-dessus ; le détail est au § 3 (une sous-section par question du plan).

**Projection sur D1–D8** (ma lecture ; le plan donnait D7 0,8 et D3 0,2) :

| dimension | poids | ce qui la porte |
|---|---:|---|
| D7 hasard et méthode | 0,55 | les tests, le banc, les chaînes d'erreurs, T8 |
| D3 grain, pixels | 0,15 | le budget de la mesure (006 à 011), T4 |
| D6 sphères, Venn | 0,10 | les cas du banc sont des Venn (002 à 005) |
| D2 bases | 0,08 | 013 à 015 ; T6, T7 |
| D1 la chèvre | 0,06 | la chaîne de la chèvre (Ullisch, Fraser et Meyerson), δ₂ ≈ δ₃ |
| D5 Kakeya, Perron | 0,03 | T5 (Bonferroni), la bande de XIII § 5 |
| D8 physique | 0,03 | 006 : le photocentre (Wielen) |

Bloc pour le § 1.10 : `"hasard-et-methode": {"D7": 0.55, "D3": 0.15, "D6": 0.10, "D2": 0.08, "D1": 0.06, "D5": 0.03, "D8": 0.03}`. **Notations qui se heurtent** : T1 à T6 du banc (`centre_venn.py`) ne sont pas T1 à T8 du plan ; K est une congruence et un nombre de dimensions ; « (A) » dans les dossiers = calculé hors dépôt.

## 2. Les chaînes de production (script → résultats → figures → document)

### 2.1 Partie par partie, dans l'ordre

| partie | script → résultats ; figures ; document | ce que le script produit pour ce dossier |
|---|---|---|
| III | `pi_dimensions.py` → `pi_dimensions.md` ; `c1` ; `pi-dimensions.md` § 2 | une suite de l'auteur et des « retenues » libres qui atteignent π, √10 et e + 0,42 |
| VI | `zone_confusion.py` → `zone_confusion.md` ; `f1` à `f3` ; `zone-confusion.md` § 3 bis, 3 ter, 4 | l'écart simplexe–chèvre en dimension réelle, δ₂ et δ₃ (retour n = 3,0000853), le décalage en 4 bases, le compte des formules p·C/q |
| XIII | `perron_dephasage.py` → `perron_dephasage.md` ; `m1` ; `perron-dephasage.md` § 5 | la bande 2,44–2,56 contre trois familles, et toutes les bandes de 0,12 |
| XVIII | `pixels_longitudes.py` → `pixels_longitudes.md` ; `r1`, `r2` ; `pixels-longitudes.md` § 5 | la corde comptée par les centres et par dedans/dehors (largeur 4,6/R) |
| XXIV | `tiers_dimension.py` → `tiers_dimension.md` ; `y1` ; `tiers-dimension.md` § 1 | la preuve de 2/(3n²), reste < 1 800/n³ pour n ≥ 100 |
| XXVII | `carte_connexions.py` → `carte_connexions.md` ; `ab1_carte.png` (d) ; `carte-connexions.md` § 1 | le graphe des renvois (178 paires sur 325), Adamic–Adar, 15 liens prédits |
| XXIX | `venn_ppm.py` → `venn_ppm.md` ; `ad2_deux_ombres.png` (e) ; `venn-ppm.md` § 5.5 | 1 240 comparaisons ; le catalogue brouillé (4 000 tirages à ±20 %) |
| XXX | `centre_venn.py` → `centre_venn.md` ; `ae3_grains_hasard.png`, `ae1` ; `centre-venn.md` § 1.3, 7 | le centre grossier (fiche 007) ; le banc : 10 relations, 6 techniques, 20 000 paires |
| recueil | `recueil_verifications.py` → `recueil_verifications.md` ; fiches 013 à 015 ; `recueil_index.py` → `index.md`, `index.csv` | congruences de i, racines digitales, Midy, 16 motifs de dizaines ; le compte des fiches et la diagonale √2 |
| révision | `revision_001.py` → `revision_001.md` ; `rev001_*.png` ; `revision-001.md` | T1 à T7, le nerf, le cadre, le balayage du seuil |

### 2.2 Les chaînes, et leurs points faibles

- **Les tests** : III § 2 → VI § 3 bis, 3 ter, 4 → XIII § 5 → XVIII § 5 → XXIV § 1 → XXIX § 5.5 → XXX § 7 → CLAUDE.md § 10 → `revision_001.py`. **L'image de Dzoba** : dépôt → XXVIII § 3 → XXIX § 1–2 → XXX § 1–2 → fiches 006 à 008, 011 → T4 ; maillon absent : le programme qui a rendu l'image à 17 courbes (dossier grain § 3.5.1). **Les liens entre parties** : XXVII → plan § 1.9 → T1 et T8 → recouvrement v2. **Le recueil** : message fondateur → CLAUDE.md § 10 → `recueil_verifications.py` → fiches 013 à 015 → `recueil_index.py` → plan → `revision_001.py`. **La chèvre** : README § 3 et § 9 (Ullisch, Fraser puis Meyerson) → XVI → XXIV § 1 → XXV.
- **Le banc dépend d'un autre script** : `centre_venn.py` lit λ(d) ≈ 402·d dans `resultats/venn_ppm.md` par expression régulière, avec un repli silencieux à 410 (lu, section 7).
- **Deux « ppm »** : `venn_ppm.py` (section 7) classe par la valeur absolue du log du rapport (2 852 ppm pour 34·tan(π/34)), les fiches 003 et 012 par l'écart relatif (2 856 ; calculé ici : 2 855,66).
- **Les figures ne suivent pas les textes** : `f2_dimension_reelle.png`, panneau b, « c'est le hasard » pour δ₂ ≈ δ₃ (§ 3.8) ; `ae3_grains_hasard.png`, panneau d, portait « signes en accord sur 93 % » (71 sur 76 contre 70 pour « positif partout », `revision_001.md` § 4.11) : légende corrigée depuis (révision 001).
- **L'image de référence** n'a ni programme, ni palette, ni ordre publiés : trois chaînes ouvertes sur douze (dossier grain § 3.6). Les numéros de section des scripts de X, XVII, XIX et XXVIII ne sont pas ceux des documents (dossier aiguilles § 2.3) ; pour XXIX et XXX, les renvois des fiches 001 à 012 concordent (vérifié).

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 La lignée des tests : ce que chaque étape a corrigé (question 1)

| étape | ce qu'elle corrige ou ajoute ; ce qui reste faible |
|---|---|
| III § 2 | « Ça marche » ne prouve rien : la même recette atteint √10 et e + 0,42. **Un témoin négatif.** Faible : deux cibles choisies. |
| VI § 3 bis | La « quasi-coïncidence » de V (0,35 %) est une bosse, propriété de toute la famille. **La variation continue du paramètre.** Faible : δ₂ ≈ δ₃ (§ 3.8). |
| VI § 3 ter | Mon arrondi « 0,00009 » devient 8,5269·10⁻⁵ (85,27 contre 90). **La précision**, puis **le changement de base.** |
| VI § 4 | Une coïncidence à 0,07 %. **Le compte des formules** p·C/q : 16 à 33 à moins de 0,1 % pour chaque grandeur. Faible : un compte, pas un nul tiré. |
| XIII § 5 | Une bande riche en rapprochements. **Le nul « autres fenêtres »** : 72 contre 72,2 (bases), 1 contre 3,5 (Fibonacci). Faible : le 3-4-5 de r = 6/5 reste « sans lien » (N6). |
| XVIII § 5 | Une corde comptée sans garantie. **Le chiffre certain** (dedans/dehors). |
| XXIV § 1 | Un développement vérifié numériquement. **La borne** 1 800/n³, n ≥ 100. Faible : XXIII avait du bruit à 10⁶. |
| XXVII § 1 | Des liens cherchés à l'œil. **Un prédicteur** (Adamic–Adar). Faible : validé sur ce qu'il fait chercher (§ 3.5). |
| XXIX § 5.5 | Des « coïncidences » à 1 %. **Le catalogue brouillé** : au ppm, rien. Faible : un nul global, pas de verdict par paire. |
| XXX § 7 | Quel test choisir ? **Le banc d'essai.** Faible : six cas, verdicts en dur (§ 3.2). |

La variation du paramètre date de VI § 3 bis ; le banc l'a formalisée, il ne l'a pas inventée (CLAUDE.md § 6 bis). Les verdicts « hasard » **sans test** ont été renversés trois fois : V → VI, X → XI (222,5° dans le trou : « seule sa place est un hasard »), XXII → XXIII (2/√3) ; une quatrième est à faire (XIII, N6). Les deux verdicts testés (002 et 004) tiennent : deux cas, c'est peu.

### 3.2 Le banc d'essai relu (fiche 012 ; `scripts/centre_venn.py`, section 7)

- **Les quatre tests à tolérance sont des fonctions de l'écart d seul** (démontré par le code). Seuils implicites : p naïve 259 000 ppm, Bonferroni 186, nul brouillé 128, description 806 (= 1/1 240). Rangés par d (`resultats/centre_venn.md` § 7), les six cas non triviaux donnent S2 (159 ppm), C1 (845), S3 (1 297), S1 (2 856), S4 (11 306), C2 (18 886), soit **S C S S S C**. Au mieux 5 sur 6, avec d* entre 11 306 et 18 886 : aucun test du banc n'a ce seuil, et à 1,5 % le catalogue donne 6 rapprochements au hasard (402·d). L'échec est de principe : l'écart ne porte pas le mécanisme.
- **Ce qu'ils savent faire** (calculé ici, `venn_ppm.md` § 7) : juger l'excès d'un *ensemble*. À 0,3 %, 4 rapprochements pour 1,206 attendus (Poisson : P(X ≥ 4) = 0,034, avant correction des huit tolérances) ; l'excès (2,8) est de l'ordre des deux liens expliqués (S1, S3). Par paire, ils répondent à « est-ce surprenant parmi 1 240 ? » : S1 ne l'est pas (1,15 paire attendue), et c'est un théorème (N·tan(π/N) = π + π³/(3N²) + …).
- **Le « 10/10 » n'est pas mesuré.** Dans `varie()`, C1 et C2 renvoient `False` et E4 `True` sans calcul ; S4 compare à 0,1 ; S1 et S2 testent la limite de la loi qu'on leur donne. E1 à E4 sont des identités, justes pour les six tests. Sur les six cas non triviaux : p naïve 4/6, Bonferroni 3/6, nul brouillé 2/6, description 3/6, variation 6/6 (deux en dur). La précision poussée ne rend jamais « hasard » : son 4/4 vient de six abstentions.
- **Pour CLAUDE.md § 10** : « seules deux méthodes ne se trompent jamais ici » est trop fort ; la phrase d'après (« l'épreuve n'est pas indépendante de la conclusion ») est la bonne. La table reste juste comme *pratique*. La révision l'a reprise dans CLAUDE.md § 10, sous la phrase qui est restée. Un vrai banc demande des vérités indépendantes et plus de négatifs (N2, § 6.3).

### 3.3 Les erreurs des chaînes, classées (question 3)

**A** point de départ biaisé ; **B** fenêtre trop étroite ; **C** pesée ; **D** troncature ; **E** cadre (définition, provenance, mémoire du corpus). Erreurs des six dossiers et du corpus ; [v] : vérifiée par moi.

| # | où | l'erreur | cl. | état |
|---:|---|---|:-:|---|
| 1 | XXX § 1.3, fiche 007 [v] | centre faux de 2,36 px : départ = barycentre biaisé (13,6 px), fenêtres ±8 puis ±2 px | A | refaite : 0,004 px |
| 2 | X § 1 [v] | le « trou » de ±24,18° suit le point P tiré au hasard, avec un seuil à moi | A | « ce qui vient de moi » |
| 3 | XXIX § 2.3, XXX § 2.5 | « le certificat de l'image » = c3-s2 (−649 ppm) ; XXIX § 6 : « je ne sais pas lequel des quatre » (−3 761 à +2 853 ppm) | A | ouverte |
| 4–6 | V § 2 ; XV § 3, XXIII § 4 ; XIV § 5, XXVII § 9 | une seule dimension regardée (« quasi-coïncidence » du 0,35 %) ; grille grossière qui confond la chèvre et son simplexe ; moitié de Kakeya fini vue sur q = 3, 5, 7 et expliquée par les carrés | B | VI ; corrigée ; T5 (q = 2 à 9) |
| 7 | XIV § 6 | « ≈ 2,8 » : 2,83 à n = 256, 2,57 à 65 536 | B | dossier aiguilles |
| 8 | Ullisch 2020 | contour centré en 3π/8, corrigé en 3π/4 (erratum 2023) : même zéro, même β | B | corrigée |
| 9 | XXX § 1.2 | poids mesurés sur les 5 % de pixels les plus clairs de chaque teinte : l'ordre des pesées s'inverse (K6) | C | ouverte (dossier grain § 3.5.4) |
| 10–12 | VI § 3 ter [v] ; XXIII § 1 ; XXIV § 2, XXV § 1.2 [v] | « 0,00009 » arrondi sur une figure, lu comme donnée ; n²·μ_n = 0,6668 à 10⁶ (bruit de double précision) ; série divergente coupée au plus petit terme (0,32 à n = 2 contre 6,08·10⁻¹⁰ pour Borel–Padé) | D | corrigées |
| 13 | XXII → XXIII | trois phrases fausses ; la deuxième (« 2/√3 : une coïncidence ») répète V | E | notes « Corrigé dans XXIII » |
| 14 | XXIX § 1.2, XXX § 1.1 | palette et programme du traceur attribués à une image qu'il n'a pas rendue | E | ouverte |
| 15 | XXX § 6.3, CLAUDE.md § 6 | « 93 % des signes » : 71 sur 76 contre 70 pour « positif partout » | E | corrigée (texte, résultats, figure ae3) |
| 16 | XXIX § 5.5 [v] | « ppm » : valeur absolue du log du rapport ici, écart relatif ailleurs | E | à écrire |
| 17 | XI, XVIII § 8, XIX § 4 | phrases restées après leur correction (222,5° « arrondi » ; « deux longueurs » ; « la base ne fait que choisir le pas ») | E | dossier bases § 6.2 |
| 18 | Fraser 1984 | faille de l'argument, corrigée par Meyerson (1984) ; non relu | E | à vérifier |

**A 3, B 5, C 1, D 3, E 6.** (1) *Le cadre est la classe la plus fréquente, et aucun test ne la voit* (une palette attribuée à tort, un certificat choisi puis oublié) : seule la relecture les attrape, et la règle de CLAUDE.md § 6 bis n'est pas outillée. (2) *A et B se corrigent par une intervention* : un autre départ (1), une fenêtre ×3 (5, 6), une autre méthode (12) ; le dossier grain en tire : garder un témoin positif. (3) *C n'a qu'un cas, le plus coûteux* : l'ordre inversé des pesées a fabriqué K6. (4) *La même erreur revient* (4 et 13).

### 3.4 Le cadre fabrique des liens : quatre cadres connus (question 4)

La règle est exacte (`revision_001.py` § 2.1, fiche 017) : deux classes paraissent liées exactement quand p_a + p_b < Σp².
- **Les doubles zéros** (Legendre et Legendre). Sur des vecteurs 0/1 centrés, la distance euclidienne compte comme ressemblance l'absence commune des grosses classes ; la cure est un coefficient qui les ignore (Jaccard, Ochiai). *Calculé ici* : 5 paires de fiches de dimensions différentes passent sous √2 (D1–D4 : 1 ; D1–D6 : 2 ; D4–D6 : 2) ; leur coefficient d'Ochiai vaut 0.
- **La somme constante** (Pearson 1897 ; Chayes 1960 ; Aitchison 1986). Une fiche est une composition (0/1, somme 1) ; la centrer par la fiche moyenne dans l'espace euclidien est le geste qu'Aitchison déconseille, et ses log-rapports ne sont pas définis pour les parts nulles (D5, D8). Ici, la cure est le partage égal.
- **Regarder ailleurs** (Gross et Vitells 2010). Le facteur d'essais corrige une valeur-p ; ici la règle est exacte et prédit les 3 liens (15 paires sur 15). Il ne joue que si l'on lit les 3 liens sans elle.
- **Le jardin des chemins qui bifurquent** (Gelman et Loken 2014). Le classement est un chemin. *Calculé ici* : si chaque fiche peut aussi tomber sur l'une des dimensions voisines qu'elle déclare (27 648 classements), le nombre de paires liées par le seul cadre va de 0 à 21 (moyenne 3,2) ; 17,7 % des classements n'en ont aucune, 63,7 % en ont 3 ou plus. Le « 3 » est une réalisation, pas une mesure.

Le partage égal supprime le faux lien, pas le chemin : publier le classement avant de calculer, ou calculer sur toutes les variantes. Le même mécanisme joue dans T2 (fiches centrées par dossier), pas dans T1 (arêtes = présences communes, asymétrique par construction).

### 3.5 T8 : le nerf contre la carte (question 5)

**Méthodes.** A : voisins communs du graphe des renvois (Adamic–Adar, XXVII § 1.3). B : dossiers partagés (v1 : plan § 1.9 ; v2 : `verification-croisee-001.md`). **Statistique** : ρ de Spearman entre A et B sur les paires non reliées. **Nul** : test de Mantel (QAP), qui permute les *parties* et non les valeurs des paires, 1 000 fois ; plus un nul par degrés voisins, car A est presque le compte des voisins communs (corrélation 0,98).

**Mesurer la dépendance.** (a) Le rapport des chances du tableau 2×2 « se citent / partagent un dossier ». (b) T8 lui-même, qui retire les paires reliées. (c) La corrélation partielle, degrés retirés. (d) Un classement des parties sans les renvois (mots du texte hors renvois, imports communs des scripts), comparé aux dossiers. (e) Un test prospectif : geler le classement d'Adamic–Adar et compter, aux révisions suivantes, les liens établis dans ses 15 premiers rangs. Le code de (a) et (b) est au § 7.

**Calculé ici** (parties 2 à 30 ; mon graphe redonne 178 paires à N = 26 et 207 à N = 27, comme XXVII) : 241 paires reliées sur 435 ; sur 406 paires, 212 reliées et 194 non.
- *Dépendance* : en v1, 78 % des paires reliées partagent un dossier, 68 % des non reliées (rapport des chances 1,69 ; Fisher p = 0,024). En v2, 94 % contre 91 % (1,60 ; p = 0,25) : le plafond ôte sa puissance au test « partage au moins un dossier ».
- *Signal* sur les non reliées. **v1** : ρ = −0,035 (nul QAP : p = 0,65 ; nul par degrés : p ≈ 0,6) ; partielle −0,078 ; Jaccard des ensembles de dossiers −0,053 (p = 0,77). **v2** : ρ = +0,090 (QAP : p = 0,23 ; par degrés : p = 0,40, le nul valant en moyenne +0,07) ; partielle −0,055 ; Jaccard +0,076 (p = 0,21) ; avec les corrections du § 8 : +0,082 (p = 0,25). Les cinq pistes (XIV–XX, VI–VIII, XIV–XXIV, VI–XXI, V–IX) partagent 1, 0, 1, 1 et 0 dossiers en v1 (moyenne 0,6 contre 0,88 pour une paire non reliée), 2, 1, 3, 3 et 0 en v2 (1,8 contre 1,86) : pas d'excès. Les comptes de B vont de 0 à 3 en v1, de 0 à 5 en v2.
- **Lecture** : ni v1 ni v2 ne montrent de signal, et ρ passe de −0,035 à +0,090 d'un recouvrement à l'autre : c'est la taille du bruit du classement, et les degrés expliquent déjà le +0,09. A et B ne voient pas la même structure ; ce n'est pas la dépendance qui fait un signal, c'est l'absence de signal qui reste après l'avoir retirée.

**Le prédicteur lui-même** (calculé ici, rangs de `carte_connexions.md` § 1.1). Graphe I–XXVI : 147 paires non reliées, 6,2 voisins communs en moyenne (écart-type 1,7). Les 11 liens que XXVII a établis ont pour rangs 1, 4, 5, 12, 17, 41, 54, 56, 60, 102, 123 : somme 475 contre 814 attendue (p = 0,006). Mais 4 sont dans les 15 premiers, que l'auteur a cherchés d'abord (hypergéométrique : p = 0,015). Sans eux, les 7 autres font 453 contre 518 (p = 0,28). **Le prédicteur n'est validé que par les liens qu'il a fait chercher** ; le test propre est prospectif (e).

### 3.6 Corrélation et causalité : intervention ou corrélation ? (question 6)

Une intervention refait l'essai en ne changeant qu'une chose ; une corrélation observe deux grandeurs qui varient ensemble (Reichenbach 1956 ; Pearl 2009).

| fiche | le lien causal affirmé | intervention faite | corrélation seulement |
|---|---|---|---|
| 007 | le biais du barycentre s'est propagé à la recherche du centre | **oui** : même essai depuis le centre de symétrie (0,004 px) ; un centre faussé de 0,5 à 2,36 px ne change pas le verdict de T4 (dossier grain § 3.5.3) | — |
| 006 | le centre bouge selon la pesée, à cause des couleurs | **oui sur l'analyse** : six pesées d'une même image (0,61 à 46 px), le seuil de 0,001 à 0,40 ; **oui sur un système modèle** (ci-dessous) | la palette de l'image à 17 courbes : un G ajusté sur quatre pesées (résidu 1,4 à 2,0 px), palette inconnue |
| 012 | les tests à tolérance échouent parce qu'ils ne voient que l'écart | **oui, par construction** : un banc à vérités connues (§ 3.2) | les vérités sont posées par l'auteur ; deux « hasard » écrits en dur |

**L'intervention sur l'image, faite sur un système modèle** (calculé ici ; code en § 7). Le Venn à 13 courbes du traceur (`/home/user/dzoba/venn17/plotter/venn-13-color.svg`) donne sa palette et son ordre. J'en lis la géométrie, je repeins les 13 courbes avec mon propre rendu (aucun code de Dzoba exécuté) et je change une seule chose à la fois.
- **Le bras de levier est lu, pas ajusté** : le centroïde de chaque courbe est à 4,756 mm = 18,58 px du centre, à 3,1° + 27,7°·i.
- **La palette.** Le centre se déplace de G·H₁(poids) sans paramètre libre : moyenne RGB 2,05 à 2,20 px observés (trois rendus, trait de 1,3 à 1,5 px), 2,08 prédits ; énergie 1,46 à 1,59 contre 1,50 ; phases à 11° près. Décalée de 4 courbes, la palette tourne le déplacement de −109,5° (RGB) et −108,5° (énergie), pour −110,8° prédits (le module est 24 % sous la prédiction). À même luminance Y, le déplacement en Y tombe de 0,38 à 0,13 px (prédit 0) et ceux de RGB et d'énergie restent à 2,3 et 1,6 px : le motif de K6.
- **L'ordre.** Quatre autres ordres (12 → 0, départ en 6, deux permutations) changent le centre de 0,3 px au plus en moyenne RGB (la palette, elle : 2,1 px), de 0,2 en énergie, 0,06 en Y, 0,02 en L ; à couleurs égales, de rien. L'effet suit les contrastes de poids.
- **Ce que ça corrige.** Le modèle à deux causes (plan, T4 étape 3 ; dossier lumière § 3.3) met l'ordre dans X = G·H₁(aires visibles), commun aux pesées : 1,22 px ici, et 2,40 px de changement si l'on inverse l'ordre. L'intervention donne 0,02 à 0,32 px, inégaux. Le X de 8 à 19 px ajusté sur l'image à 17 courbes (dossier lumière § 3.3) n'est donc pas l'ordre ; le dossier l'attribuait déjà à l'erreur sur les couleurs.
- **Un témoin sur le PNG de Dzoba** : un seuil sur la clarté OKLab, constante pour ses 13 courbes, déplace le centre de 0,07 à 0,30 px jusqu'à t = 0,3 ; un seuil sur la moyenne RGB, variable, de 1,1 à 11,7 px pour t = 0,3 à 0,6. Un effet de seuil prouve que la grandeur seuillée varie d'une courbe à l'autre (dossier grain § 3.5.5).
- **Limite** : un système modèle (13 courbes, trait de 1,25 px, mon anticrénelage). Il valide la méthode et la taille des effets ; la palette de l'image à 17 courbes reste inconnue.

### 3.7 Les tests T1 à T8 contre la table du § 10 (question 7)

| test | technique annoncée | risque de « hasard » pour une structure | risque de « structure » pour un hasard |
|---|---|---|---|
| T1 nerf | nul brouillé | **net** : le nul garde les marges ; un recouvrement fait à la main met la structure dans les marges, et ce nul passe pour conservateur (Gotelli 2000 : à vérifier) ; p = 0,16 ; 0,24 ; 0,39 en v1, 0,53 ; 0,71 ; 0,37 en v2 (`resultats/revision_001.md` § 3) | le nerf n'est pas la réunion : 6 intersections sur 81 ne sont pas contractiles (Betti 1, 0, 4 contre 1, 4, 3 ; dossier ombres § 3.2) |
| T2 diagonale | variation du paramètre | — (p = 0,93 en v1, 0,68 en v2 : il ne dit rien) | **net** : « les liées passent sous √2 » est vrai de tout recouvrement de ces tailles |
| T3 ménisque | loi de l'écart | non | l'ordre 3 se recolle avec s libre (49/10) ; seul l'ordre 4 est un test, et il échoue |
| T4 centre | mesure contre le budget | l'« absence d'ordre » est une absence de signature (p = 0,64 ; 0,19) ; la puissance vient des témoins | la palette isoluminante est ajustée (Y₀ libre) ; le terme d'ordre est proportionnel aux contrastes (§ 3.6) |
| T5 Kakeya fini | variation de q | non | retrouve un théorème (Dvir 2009, n = 2 ; Blokhuis et Mazzocca) : une correction du corpus |
| T6 Midy | variation de la borne et de la base | non | **net** : « moitié à chaque étage » est la loi géométrique de v₂, celle de tout entier au hasard ; pas un invariant de Perron (aire 2/(k + 2)) |
| T7 4/3 | répliquer sur d'autres bases | non : le compte suit log₂ 3 (19/12) | non |
| T8 nerf/carte | permutations | oui, en v1 et v2 (ρ = −0,04 ; +0,09 ; comptes de 0 à 3, puis de 0 à 5) | **net** si la dépendance (1,69 ; 1,60) n'est pas retirée |

La synthèse dit maintenant « presque chaque test fait varier un paramètre » (`revision-001.md` § 7) : T1 et T8 sont des nuls, dernière ligne de la table du § 10.

### 3.8 Ce qui reste ouvert

- **δ₂ ≈ δ₃** (VI § 3 bis ; `f2_dimension_reelle.png`, b). Le tri de VI § 6 dit « à moitié expliqué », § 3 bis « reste un hasard », la figure « c'est le hasard ». *Calculé ici* : le niveau de δ₂ revient en n = 3,0000853, à 8,53·10⁻⁵ d'un entier : probabilité 1,7·10⁻⁴ pour une racine répartie au hasard (2·10⁻⁴ par l'écart relatif 9,8·10⁻⁶ sur ±5 %), de l'ordre de 10⁻³ avec une marge d'essais (trois courbes, deux ancres). Le même calcul donne 0,61 pour la fiche 002 (dossier lumière § 4.1). « Hasard » est testé pour 002, pas pour δ₂ ≈ δ₃ : statut **ouvert** (dossier corde, F7).
- La palette de l'image à 17 courbes ; un banc d'essai à vérités indépendantes ; le test prospectif de T8 ; les erreurs de cadre, que rien n'outille.

## 4. Les fiches du dossier : verdict, test, et la partie qui portait déjà le lien

Les quinze fiches (question 2). « Bon test » : conforme à la table du § 10. « Tient » : le verdict reste dans le budget de la donnée. Dimensions : la principale d'abord, puis les voisines que ce dossier confirme.

| n° | test appliqué : le bon ? | budget de la donnée : le verdict tient-il ? | partie qui portait le lien | dim. |
|---|---|---|---|---|
| 001 | précision, identité 2⁻ʲ = 5ʲ·10⁻ʲ : **oui** | exact : **tient** | XXVI § 2 | D2, D3, D6 |
| 002 | variation (zéro en N = 16,70) et nul brouillé, concordants : **oui** | exact ; la proximité n'est pas rare (0,304 d'un entier : probabilité 0,61) : **tient** | XXVIII § 3.3, XXVI § 2.5 | D7, D4, D2 |
| 003 | variation, loi π³/(12N²) : **oui** | exact, classique : **tient** | XXVIII § 2.5 | D6, D5, D7 |
| 004 | variation sur n : **oui**, mais sans le point n = 23 | 35,3 à 36,7 % pour les 4 certificats à 17 courbes (la fiche cite c3-s2, 35,8) ; à 23 courbes 35,01 à 35,18 % (`/home/user/dzoba/venn17/paper/venn17-19.tex`, l. 391 : 2 937 192 à 2 951 107 triangles sur 2²³ ; dossier ombres NF4) : la part dérive et passe par 35,10 %, comme C1 par 1 en N = 16,70 ; les droites au hasard donnent 35,51 % (Miles 1964, à vérifier) : **tient**, à suivre | XXVIII § 1, XXIX § 2.2 | D7, D6 |
| 005 | réplication sur 12 Venn (entiers) : **oui** | ±24,7 orbites ; 1,6 % par tirage, 18 % sur 12 ; mais 3 familles de recherche et deux certificats au même compte (262 637) : 12 % pour 8 tirages indépendants (calculé ici) : **tient** | XXVIII § 3.1 | D6, D7, D2 |
| 006 | mesure contre le budget (0,003 px) : **oui** | 0,61 px = 200 budgets : la pesée **tient** ; « dipôle de la palette » **établi sur le système modèle** (§ 3.6), à établir pour l'image | XXX § 1.2 seule | D3, D8, D7 |
| 007 | refaire l'essai, une intervention : **oui** | 2,36 px contre 0,003 px : **tient** | X § 1, XV § 3 | D7, D3 |
| 008 | quatre rotations : **oui, mais** même interpolation, même grille | 0,004 px d'écart, 0,003 px de dispersion : **tient** ; un témoin à centre connu manque (§ 6.2) | IV, XVIII | D3, D6 |
| 009 | séparer les sources : **oui** | 34 sur 34 (contour), 85 % (cœur) ; pas de résolution angulaire : **tient** | XXVIII § 3.3 | D4, D6 |
| 010 | précision, 50 chiffres : **oui** | exact pour le cercle du bord : **tient** ; « chaque anneau » **non** (dossier corde § 6.2, n° 4 ; titre corrigé depuis) | X, XX § 3 | D1, D6, D4 |
| 011 | loi W_c(n), W_r(n) : **oui** | la loi **tient** ; « 18,99 à 2 000 px » dépend du critère de 2 px (de 1,5 à 3 px : 19,8 à 17,8 courbes, calculé ici) : « pile à la limite » **non** (titre précisé depuis) | XVIII § 6 | D3, D5, D6 |
| 012 | le banc : **oui comme pratique** | six cas, verdicts en dur (§ 3.2) : « un seuil sur l'écart ne sépare pas » **tient** ; « ne se trompent jamais » **non** (CLAUDE.md § 10 le précise depuis) | VI § 3 bis, 3 ter, XIII § 5 | D7, D6 |
| 013 | variation (1/13 seulement) : **oui, mince** | T4.1 : b ≤ 60, p ≤ 400, seul (10, 7) non trivial : « propre à la base 10 » **tient** ; b = q² + 1 | XIX § 2 | D2, D7 |
| 014 | précision, 61 étages, 10⁻³⁰ : **oui** ; le modulo 3 est un calcul fini dans F₉ | exact : **tient** ; « (−2)^(3/2) ≡ −i mod 3 » **non** (±1 dans F₉), la fiche le dit | XIX § 2 | D2, D1 |
| 015 | exact (restes mod 3) ; comptes sous 10⁶ : **oui pour la face, non pour « 3 fois »** | la face **tient** ; le rapport dérive de 3,90 à 2,53 (fiche 021) : « près de trois fois » **non** au-delà de 10⁶ | XXVIII, Hardy–Littlewood | D2, D6, D7 |

- *Dix tests sur quinze sont les bons, sans réserve.* Réserves : 008 (biais de grille partagé), 012 (un banc, pas une preuve), 013 (un seul autre premier ; T4.1 l'a étendu), 014 (calcul fini, pas précision), 015 (« trois fois » exige la variation de N).
- *Cinq énoncés dépassent leur test* : 006 (la cause), 010, 011, 012, 015 : une erreur de cadre (classe E). *Aucun budget ne casse.*
- *Le lien, ou ses objets, était déjà dans une partie antérieure pour quatorze fiches sur quinze* ; seule 006 est née en XXX. Pour les trois « hasard » (002, 004, 005), ce sont les objets, pas un lien.

## 5. Les congruences et les obstructions

| id | ce qui est comparé | verdict | détail |
|---|---|---|---|
| K4 | Bonferroni d'ordre 1 (fiche 012) et d'ordre 2 (Kakeya fini, fiche 019) | **se recolle** | tronquer l'inclusion–exclusion ; bornes de sens opposés (l'ordre 1 majore, l'ordre 2 minore) ; égalité à l'ordre 2 sans point sur trois droites |
| K6 | le dipôle de la pesée et le photocentre | **se recolle** | l'ordre inversé des écarts vient du choix des poids (5 % les plus clairs) ; sur le système modèle, G·H₁ prédit palette et rotation (§ 3.6) ; reste la palette de l'image |
| K8 | les trois 4/3 | **par log₂ 3 seulement** | coïncidence de petits entiers (T7) ; réduites de log₂ 3 (19/12) |
| K9 | Midy et un arbre de Perron | **trivialement** | « moitié à chaque étage » est la loi géométrique de v₂ ; aucun invariant de Perron n'y passe |
| M1 | les quatre tests à tolérance | **exactement** | quatre seuils sur d (128 < 186 < 806 < 259 000 ppm), totalement ordonnés (cocycle trivial) ; l'étiquette S/C n'est pas une fonction de d |
| M2 | p_a + p_b < Σp², doubles zéros, somme constante | **se recolle** | Ochiai voit 0 lien là où le cadre en voit 3 ; obstruction : le chemin (0 à 21) |
| M3 | 007 (départ), T4 (seuil), 006 (pesée) | **sur l'analyse** | trois interventions sur le calcul ; sur l'image : le système modèle seulement |
| M4 | le nerf et la carte (T8) | **non**, en v1 comme en v2 | ρ = −0,035 (v1), +0,090 (v2) sur les non reliées ; rapport des chances 1,69 et 1,60 |
| M5 | fiche 002 et δ₂ ≈ δ₃ | **même méthode, deux verdicts** | 0,61 (hasard) contre 2·10⁻⁴ (ouvert) |
| M6 | fiche 005 et sa réplication | **avec le hasard** | 1,6 % par tirage ; obstruction : trois familles de recherche, pas douze objets indépendants |
| M7 | XIII (r = 6/5 : 3-4-5, 7-24-25) et XIV, XXI, XXV (rotations de la grille) | **ma lecture** | l'arc de 73,74° est le carré de (4 + 3i)/5, entier de Gauss de norme 25 ; réserve : 3/5 est le plus simple cosinus pythagoricien de la bande (8 de dénominateur ≤ 25 : 0,033 attendu, grossier) |

**Obstructions et trous qu'elles désignent**
- **K6, fiches 006 et 007** : la palette et l'ordre de rendu de l'image à 17 courbes. *Où* : une demande à Dzoba ; l'archive Zenodo v1.3 (doi 10.5281/zenodo.23189412, README) ; un rendu avec les palettes candidates (Y₀ de 0,30 à 0,36), G lu dans la géométrie, comparé aux six centres.
- **T8 (M4)** : aucun classement des parties indépendant des renvois. *Où* : les mots du texte hors renvois, les imports communs des scripts, un lecteur extérieur ; le test prospectif.
- **Fiche 012 (M1)** : un banc à vérités indépendantes. *Où* : Heegner, convergents, e^π − π ≈ 20 et π⁴ + π⁵ ≈ e⁶ (§ 6.3).
- **δ₂ ≈ δ₃ (M5)** : une raison, ou un témoin. *Où* : la forme exacte de δ(n) en 2D et 3D ; le même passage pour les deux autres courbes de la bosse.
- **Fiche 005 (M6)** : des objets indépendants. *Où* : les certificats à 23 courbes (Zenodo), les Venn à 11 et 13 courbes de Mamakani et Ruskey, les journaux de `ramp12h`.
- **K9 (T6)** : un invariant commun à Midy et Perron. *Où* : l'aire exacte d'un arbre appliquée à des périodes ; les densités de Hasse, Wiertelak, Moree.

## 6. Les trous

### 6.1 Les trous du recueil : sept fiches nouvelles proposées

Aucune ne double les fiches 016 à 021 ni celles des autres dossiers (D5 : N6 ; D8 : N5). Format : type · statut · partie · script, section · image · dimensions.

- **N1 — Les tests à tolérance sont des seuils sur l'écart seul.** Hasard ; Corrélation · exact · XXX § 7 · `scripts/centre_venn.py`, section 7 (`verdict`) · `figures/ae3_grains_hasard.png`, f · D7. Seuils ordonnés (128, 186, 806, 259 000 ppm) ; six cas rangés par écart : S C S S S C ; au mieux 5 sur 6.
- **N2 — Le banc : six cas non triviaux, un « 10/10 » en partie écrit en dur.** Hasard ; Causalité · calculé (lecture du code) · XXX § 7 · `centre_venn.py`, section 7 (`varie`) · `ae3`, f · D7. Bons verdicts sur six cas : p naïve 4, Bonferroni 3, nul brouillé 2, description 3, variation 6 (C1 et C2 en dur) ; banc à élargir (§ 6.3). Déjà reprise en note dans la fiche 012 et dans CLAUDE.md § 10 : une fiche à part est facultative.
- **N3 — δ₂ ≈ δ₃ : 2·10⁻⁴, donc « ouvert », pas « hasard ».** Coïncidence · ouvert · VI § 3 bis · `scripts/zone_confusion.py`, section 3 bis · `figures/f2_dimension_reelle.png`, b · D1, D7. Retour en n = 3,0000853 : 1,7·10⁻⁴ pour une racine au hasard, contre 0,61 pour la fiche 002.
- **N4 — Le prédicteur d'Adamic–Adar n'est validé que par les liens qu'il a fait chercher.** Corrélation · calculé · XXVII § 1.3 · `scripts/carte_connexions.py`, section 1 (`ETABLIS`, `PRED`) · `figures/ab1_carte.png`, d · D7. 4 des 11 liens établis sont dans les 15 premiers rangs (p = 0,015) ; les 7 autres : rang moyen 64,7 pour 74 (p = 0,28).
- **N5 — Intervention sur un Venn à 13 courbes : la palette déplace le centre comme G·H₁ le prévoit, l'ordre presque pas.** Causalité ; Analogie · calculé ici · XXX § 1.2 · `centre_venn.py`, section 1 (`POIDS`, `dipole`), appliqué au SVG `plotter/venn-13-color.svg` repeint hors dépôt · image à produire · D8, D3, D7. 2,05 à 2,20 px observés contre 2,08 prédits ; palette décalée de 4 : −109,5° pour −110,8° ; ordre : 0,3 px au plus.
- **N6 — Le 3-4-5 de la bande de XIII est une rotation de la grille.** Coïncidence ; Analogie · à tester · XIII § 5 · `scripts/perron_dephasage.py`, section 5 · `figures/m1_perron_dephasage.png` · D5, D2. r = 6/5 (n = 2,5108) coupe le triangle en deux 3-4-5 ; le contact (7/25, 24/25) est ((4 + 3i)/5)², comme les rotations de XIV § 1, XXI, XXV. Probabilité grossière 0,03 par bande.
- **N7 — Le nombre de « liens apparents » dépend du classement.** Corrélation ; Hasard · calculé ici · révision 001 · `scripts/revision_001.py`, section 2.1 (`vecteurs`) · `figures/rev001_diagonale_cadre.png`, b · D7. 3 liens dans le recueil ; de 0 à 21 sur 27 648 reclassements (17,7 % sans lien).

### 6.2 Les trous du corpus

- **Aucun script ne cherche les liens déjà posés** avant d'écrire « coïncidence » (CLAUDE.md § 6 bis) ; la carte de XXVII pourrait servir de garde-fou.
- **Aucun estimateur de centre n'est validé sur un rendu à centre connu** (fiche 008) : le SVG à 13 courbes en donne un (centre à la page, 256 mm).
- **Le facteur d'essais** de Bonferroni (1 240) compte les comparaisons faites, pas les formules possibles (VI § 4 : 10 × 1 000 × 12).
- **Cinq triangles vides du nerf v1 touchent ce dossier, trois en v2.** v1, corpus : aiguilles · grain · méthode, bases · grain · méthode ; recueil : grain · méthode · lumière, grain · méthode · ombres, méthode · lumière · ombres (la fiche 006 les remplissait). Pour les deux premiers : la dérive du « 2,8 » de Perron (dossier aiguilles) et celle des dizaines (fiche 021), testées par la variation de n ou de N. v2 : bases · corde · méthode, bases · grain · méthode, corde · méthode · moities, tous « trous du recueil » ; chacun se remplirait par une fiche déjà commune aux deux autres dossiers (014, 001, 010), que je range ici comme cas d'audit (§ 8). Avec les parties, l'unique triangle vide qui touche ce dossier (aiguilles · bases · méthode) est rempli par XIV ou XXV.

### 6.3 Les trous des données publiées

Aucune recherche en ligne. « sûre » : auteur, revue et année connus ; « à vérifier » : le reste.
- **Un banc à vérités indépendantes.** *Calculé ici* : les presque-entiers de Heegner suivent la loi de l'écart −196 884·e^(−π√d) (rapport 0,9999 à 1,0000 pour d = 19, 43, 67, 163 ; écart relatif de 2,5·10⁻⁷ à 2,9·10⁻³⁰) ; les convergents de log₂ 10 et log₂ 3 ont un écart inférieur à 1/q² ; sans mécanisme connu : e^π − π ≈ 20 (4,5·10⁻⁵), π⁴ + π⁵ ≈ e⁶ (4,4·10⁻⁸), si proches que les tests à tolérance les diraient « structure » : le facteur d'essais décide. Cox, *Primes of the Form x² + ny²*, Wiley 1989 (sûre) ; Diaconis et Mosteller, *JASA* 84, 853–861 (1989) (sûre) ; Gross et Vitells, *EPJ C* 70, 525–530 (2010) (sûre) ; Gelman et Loken, *American Scientist* 102, 460–465 (2014) (sûre).
- **Classes rares et faux liens.** Legendre et Legendre, *Numerical Ecology*, 3e éd., Elsevier 2012 (sûre) ; Pearson, *Proc. R. Soc. Lond.* 60, 489–498 (1897) (sûre) ; Chayes, *J. Geophys. Res.* 65, 4185–4193 (1960) (sûre) ; Aitchison, *The Statistical Analysis of Compositional Data*, 1986 (sûre) ; Ahlgren, Jarneving, Rousseau, *JASIST* 54, 550–560 (2003) (à vérifier).
- **Liens, matrices, nuls.** Adamic et Adar, *Social Networks* 25, 211–230 (2003) (sûre) ; Liben-Nowell et Kleinberg, *JASIST* 58, 1019–1031 (2007) (sûre) ; Mantel, *Cancer Research* 27, 209–220 (1967) (sûre) ; Krackhardt, *Social Networks* 10, 359–381 (1988) (sûre) ; Gotelli, *Ecology* 81, 2606–2621 (2000) (sûre) ; Strona et al., *Nature Commun.* 5, 4114 (2014) (à vérifier).
- **Causalité, Bonferroni.** Reichenbach, *The Direction of Time*, 1956 (sûre) ; Pearl, *Causality*, 2e éd., Cambridge 2009 (sûre) ; Lipsitch, Tchetgen Tchetgen, Cohen, *Epidemiology* 21, 383–388 (2010) (à vérifier) ; Bonferroni (1936) (sûre) ; Dvir, *J. Amer. Math. Soc.* 22, 1093–1097 (2009) (sûre).

## 7. Le code minimal du test qui me concerne (T8 : le nerf contre la carte)

`revision_001.py` a `nerf`, `betti`, `triangles_vides`, `curveball` et `COUV` ; il n'a pas le graphe des renvois. `carte_connexions.py` le construit aux lignes 84 à 140 mais écrit des fichiers à l'import : le code reprend sa règle, sans écriture. Essayé hors dépôt sur v1, v2 et N = 30 (≈ 2 s chacun) : résultats au § 3.5. Non inclus (dix lignes chacun) : le nul par degrés voisins, la corrélation partielle, la somme des rangs des liens établis, le compte des liens apparents sur `itertools.product` des classements. Les interventions du § 3.6 (rendu du SVG à 13 courbes avec PIL, palettes et ordres échangés, centroïdes des pesées, témoin du seuil) sont refaites par [`scripts/revision_001.py`](../../scripts/revision_001.py), § 4.12 *(note de la synthèse : le code de l'agent était dans un répertoire temporaire de la session)*.

```python
# T8 (à coller dans revision_001.py, qui a déjà os, re, itertools, np, REC et COUV). Lit les .md, n'écrit rien.
import math
from scipy.stats import fisher_exact, spearmanr
ROM = "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XXIV XXV XXVI XXVII XXVIII XXIX XXX".split()
rom = lambda s: ROM.index(s) + 1 if s in ROM else 99                      # 99 : partie plus tardive, ligne ignorée
MOTIF = re.compile(r"[Pp]arties? ((?:[IVXL]+(?:,\s*|\s+et\s+|\s+à\s+|\s*–\s*)?)+)")


def graphe_renvois(dossier, nmax):
    """Même règle que scripts/carte_connexions.py (lignes 84 à 140) : « partie XIV », « parties V et XIV », lien vers un fichier."""
    tous = {}
    for f in sorted(os.listdir(dossier)):
        if f.endswith(".md") and f != "CLAUDE.md":
            m = re.match(r"# Partie ([IVXL]+)", open(os.path.join(dossier, f), encoding="utf-8").readline())
            if m or f == "README.md":
                tous[f] = rom(m.group(1)) if m else 1

    def cibles(txt):
        out = []
        for m in MOTIF.finditer(txt):
            nums = re.findall(r"[IVXL]+", m.group(1))
            plage = re.search(r"\sà\s|–", m.group(1)) and len(nums) == 2
            out += range(rom(nums[0]), rom(nums[1]) + 1) if plage else [rom(x) for x in nums]
        return out + [tous.get(g, 0) for g in re.findall(r"\]\(([a-z0-9-]+\.md)", txt)]
    vois = {i: set() for i in range(1, nmax + 1)}
    for f, n in tous.items():
        if n <= nmax:
            lignes = open(os.path.join(dossier, f), encoding="utf-8").read().split("\n")
            for c in cibles("\n".join(l for l in lignes if not any(r > nmax for r in cibles(l)))):
                if 1 <= c <= nmax and c != n:
                    vois[n].add(c)
                    vois[c].add(n)
    return vois


def t8(couv, vois, nmax=30, tirages=1000, graine=1):
    """ρ de Spearman entre Adamic–Adar et les dossiers partagés, sur les paires non reliées ; nul QAP (on permute les parties)."""
    P = list(range(2, nmax + 1))                  # la partie I cite tout : exclue, comme dans XXVII
    deg = {i: len(v) for i, v in vois.items()}
    app = {p: {d for d in couv if ROM[p - 1] in couv[d]["parties"]} for p in P}
    n = len(P)
    AA, SH, LIE = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n), bool)
    for (i, a), (j, b) in itertools.combinations(enumerate(P), 2):
        AA[i, j] = AA[j, i] = sum(1 / math.log(deg[z]) for z in vois[a] & vois[b] if deg[z] > 1)
        SH[i, j] = SH[j, i] = len(app[a] & app[b])
        LIE[i, j] = LIE[j, i] = b in vois[a]
    iu = np.triu_indices(n, 1)
    libre = ~LIE[iu]
    rho = lambda M: spearmanr(AA[iu][libre], M[iu][libre])[0]
    r0, rng = rho(SH), np.random.default_rng(graine)
    nul = np.array([rho(SH[np.ix_(p, p)]) for p in (rng.permutation(n) for _ in range(tirages))])
    s, l = SH[iu] > 0, LIE[iu]                    # dépendance : « se citent » contre « partagent un dossier »
    rc, pf = fisher_exact([[(s & l).sum(), (~s & l).sum()], [(s & ~l).sum(), (~s & ~l).sum()]])
    return dict(rho=r0, p_qap=(nul >= r0).mean(), rapport_des_chances=rc, p_fisher=pf)
# usage : t8(COUV["v1"], graphe_renvois(os.path.join(REC, ".."), 30)) ; puis COUV["v2"]. ≈ 2 s.
```

**Lecture.** *Structure* : ρ nettement positif (p_qap < 0,05) et cinq pistes (XIV–XX, VI–VIII, XIV–XXIV, VI–XXI, V–IX) qui partagent plus de dossiers que la paire non reliée moyenne (0,88 en v1, 1,86 en v2). *Hasard* : ρ dans le nul (v1 : −0,035, p = 0,65 ; v2 : +0,090, p = 0,23). Écrire toujours le rapport des chances : loin de 1, les méthodes ne sont pas indépendantes.

## 8. Les corrections au recouvrement

Le plan (§ 1.9) donne les parties III, VI, XIII, XVIII, XXIV, XXVII, XXIX, XXX et les fiches 002, 003, 004, 005, 007, 012, 015 ; l'entrée v2 de `verification-croisee-001.md` est la même.
- **À ajouter, parties** : I (erratum d'Ullisch, Fraser puis Meyerson : README § 3.1 et § 9), V (la « quasi-coïncidence »), X (le trou qui suit le point P), XIV (T5, le « 2,8 »), XXII et XXIII (les trois phrases), XXV (Borel–Padé). Chacune porte un cas du § 3.3.
- **À ajouter, fiche** : 006 (causalité, K6, T4 : § 3.6), dont l'analyse est ici. En v1 elle remplissait trois des cinq triangles vides du nerf qui touchent ce dossier ; en v2 elle n'en remplit aucun (la fiche 003 est déjà dans six dossiers sur huit) : la raison est son contenu, pas le nerf. Les parties XIV et XXV remplissent le seul triangle vide du niveau 3 qui touche ce dossier (aiguilles · bases · méthode) : un effet du classement, pas une découverte, à écrire dans T1.
- **À retirer** : rien. **Pas ajoutées** : les sept fiches du § 4 hors liste (001, 008, 009, 010, 011, 013, 014) sont des cas d'audit ; les ranger ici ferait de ce dossier un sommet relié à tous (001, 010 et 014 rempliraient les trois triangles vides de v2 : option non retenue).

```json
{"hasard-et-methode": {
  "parties": ["I", "III", "V", "VI", "X", "XIII", "XIV", "XVIII", "XXII", "XXIII", "XXIV", "XXV", "XXVII", "XXIX", "XXX"],
  "fiches": ["002", "003", "004", "005", "006", "007", "012", "015"]}}
```
