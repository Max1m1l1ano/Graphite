# La forme de la révision, conjointe à Lean : les étapes, le but de chaque agent, ses prédictions et les confusions possibles

> « Peux tu trouver la meilleure manière de formuler le workflow et établir les étapes conjoint à LEAN. Fais ton plan en établissant un but précis pour lancer chaque agent et en prédisant ce que chacun rapporteraient avec un registre de scénarios de requête et de ramifications des possibles cinfusions. »
>
> (ton message du 10 octobre 2026, arc 004)

**Quand et pourquoi ce fichier existe.**
- Il a été écrit le 10 octobre 2026 (arc 004), en réponse au message ci-dessus. C'est un plan à valider pour la révision 002 : rien n'est encore lancé.
- Il part de quatre sources :
  - la forme proposée par le [bilan 001](bilan-001.md), § 8 ;
  - la règle des drapeaux ([CLAUDE.md](../../CLAUDE.md), § 10) ;
  - les deux projets Lean du dépôt de Dzoba, lus et jamais exécutés : `verify/lean`, de Justin Grimes, et son portage à 19 courbes, `verify/lean19`, tous deux sous licence Apache 2.0 ;
  - les confusions réellement observées à la révision 001.
- Le registre des scénarios est dans [`scenarios-revision.csv`](scenarios-revision.csv) (49 lignes).
- **Ce fichier n'entre dans aucune liste de lecture d'agent** : ses prédictions doivent rester cachées aux agents (scénario S06).

**Ma lecture de « LEAN » (scénario S47).** Je l'ai lu comme le prouveur Lean 4, celui qui vérifie les certificats de Dzoba : « vérifié en Lean », partie XXIX, § 6. Si tu pensais à la méthode Lean de gestion, dis-le-moi. Deux de ses idées sont déjà dans ce plan : s'arrêter au premier défaut (le gel et l'audit, § 5), et ne pas accumuler d'en-cours (un commit par étape, § 2).

## En bref

- **Lean devient le juge des énoncés exacts.** Le procédé est en quatre temps :
  - un énoncé Lean est écrit avant toute preuve ;
  - il est traduit en retour, à l'aveugle, puis validé par toi, puis gelé ;
  - ensuite seulement, on le prouve ;
  - le verdict, c'est la compilation, lue dans le journal, jamais dans le rapport d'un agent.
- **Chaque énoncé du recueil prend une voie** (§ 5) :
  - L1, un calcul ou une identité ;
  - L2, un théorème avec Mathlib ;
  - L3, un énoncé profond, pas maintenant ;
  - N, un énoncé numérique, qui reste en Python ;
  - P, un fait sur un procédé, qui se teste en relançant le script.

  L'inventaire en compte 31 : 10 en L1, 7 en L2, 4 en L3, 5 en N, 5 en P.
- **Neuf étapes, chacune avec un contrat** que des scripts vérifient, et un commit après chacune (§ 2).
- **Sept rôles d'agents**, chacun avec un but en une phrase, un livrable, un critère d'arrêt et une prédiction écrite avant le lancement (§ 3). L'écart entre la prédiction et le rapport est lui-même un drapeau.
- **Le registre des scénarios** compte 49 scénarios de requête, dont 27 déjà observés. Ils se répartissent en 5 voulus, 30 confusions, 7 pannes, 5 dérives et 2 fuites. Les quatre confusions les plus coûteuses ont leurs ramifications au § 6.
- **Lean ne tourne pas dans cette session.** Les téléchargements de GitHub sont refusés (403), et l'hôte du cache de Mathlib ne répond pas. Je propose un CI GitHub Actions sur ton dépôt, qui compile et rend son journal (§ 5.4) ; c'est à valider par toi.
- **Le principe de formulation** (§ 1 et 4) : écrire la révision comme un projet Lean. Les énoncés viennent d'abord, les trous sont comptés, la compilation juge, et les consignes sont gelées par une somme de contrôle.

## 1. Le principe : formuler la révision comme un projet Lean

Un projet Lean et une révision se ressemblent par le procédé. C'est un dictionnaire (fiche 023), mais il transporte une pratique précise.

| dans un projet Lean | dans la révision |
|---|---|
| le `lakefile` : les cibles et leurs dépendances | le plan : les dossiers, leurs entrées, leurs sorties |
| un énoncé `theorem … : …`, écrit avant sa preuve | un énoncé du registre des résultats, avec son id |
| `sorry`, un trou dans une preuve | un drapeau à juger, un énoncé (A) |
| `#print axioms` : ce sur quoi repose un théorème | « Le tri » : ce sur quoi repose chaque énoncé |
| `lake build` passe | la vérification croisée et les contrôles par script passent |
| `native_decide` : une frontière de confiance (le compilateur, pas le noyau) | un calcul en flottants : à pousser en précision avant de dire « exact » |
| `SHA256SUMS` (le dépôt de Dzoba) | le gel des consignes et des énoncés |

**Ce qui est partagé exactement.** Les deux séparent ce qui est énoncé, ce qui est établi et ce qui reste un trou, et un outil les compte.

**Ce qui se transporte.** Une règle de Lean : un build qui passe avec des `sorry` n'est pas une preuve. Pour la révision, une synthèse qui « passe » avec des drapeaux à juger n'établit rien de ces drapeaux. La révision doit donc afficher son nombre de trous, comme `#print axioms` affiche `sorryAx`.

**Ce qui reste ouvert.** Lean ne juge que ce qui se formalise. L'association et l'assemblage, quand ils ne se calculent pas, restent à toi et à moi.

## 2. Les étapes

Chaque contrat est vérifié par un script avant le commit de l'étape. Si un contrat échoue, l'étape s'arrête : on ne passe pas à la suivante avec un défaut.

| étape | qui | but | livrable | contrat vérifié par script |
|---|---|---|---|---|
| 0. préparer | script | réunir ce que l'agent Opus doit lire | `revisions/NNN/paquet.md` (60 Ko au plus) : index, registres, fiches nouvelles, arcs, graphe des fichiers, ouverts ; et l'inventaire des énoncés exacts | taille ; tous les fichiers du graphe existent |
| 1. planifier | A1 (Opus) | découper la révision et choisir les voies Lean | `plan-NNN.md` (30 Ko au plus) et `plan-NNN.json` ; les prédictions dans un fichier à part | schéma ; budgets présents ; listes de lecture = le graphe ; division des dimensions proposée |
| 2. lire | A2 (Sonnet, 8 au plus, deux à la fois) | lever des drapeaux et tester les congruences, dossier par dossier | le dossier (30 Ko au plus) ; son JSON écrit section par section ; son code dans `revisions/NNN/code/` | taille ; schéma ; chaque (A) a un chemin de code ; seul le dossier a changé (git status) |
| 2L. énoncer | A4 (Opus), en même temps que l'étape 2 | écrire les énoncés Lean des voies L1 et L2, sans preuve | `lean/Recueil/*.lean`, chaque énoncé avec `sorry` et l'id de son énoncé français | le CI compile les énoncés (avec `sorry`) ; un énoncé par id |
| 3. traduire en retour | A5 (Sonnet), à l'aveugle | dire en français ce que dit chaque énoncé Lean | `retro-NNN.json` | commentaires retirés avant l'envoi ; une paraphrase par énoncé |
| 4. croiser et juger | script, puis moi, puis toi | réunir, comparer et juger | `verification-croisee-NNN.md` ; `drapeaux-NNN.csv` ; les énoncés Lean gelés (`lean/SHA256SUMS`) | chaque drapeau a un verdict ou « à juger » ; chaque écart de rétro-traduction est un drapeau ; tu as validé les énoncés |
| 5. prouver | A6 (Opus), en boucle avec le CI | prouver les énoncés gelés | les preuves ; `lean/audit-NNN.json` (un statut par énoncé) | les sommes n'ont pas changé ; aucun `sorry` ni `admit` ; `#print axioms` sans `sorryAx` ; les `native_decide` listés |
| 6. tester et contredire | moi, et A3 (Opus) | refaire ce qui entre dans la synthèse | `scripts/revision_NNN.py` et ses résultats ; `contradicteur-NNN.json` | reproductible (deux passages, `PYTHONHASHSEED` varié) ; trois énoncés par dossier refaits |
| 7. synthétiser | moi | écrire la synthèse, avec un statut par énoncé | `revision-NNN.md` (25 Ko au plus) | aucun (A) ni drapeau à juger dans l'En bref ; chaque nombre a son id |
| 8. mettre à jour et clore | script, puis A7 (Sonnet) | mettre à jour, vérifier, archiver | fiches, registres, index ; `arc-NNN.csv` ; les drapeaux de A7 | index régénéré ; les drapeaux de A7 jugés avant le message final |

**Les statuts d'un énoncé, après la révision :**
- *exact (Lean)* ;
- *exact (Lean, native_decide)* ;
- *exact (script)* ;
- *calculé* ;
- *(A)*, un calcul d'agent non refait ;
- *drapeau à juger*.

Un énoncé ne monte à « exact (Lean) » que si son énoncé Lean a été validé par toi (étape 4).

## 3. Les agents : but, livrable, arrêt, prédiction

Les prédictions sont écrites avant le lancement et cachées aux agents. Elles valent pour une révision comme la 001 (8 dossiers, une trentaine de parties, une vingtaine de fiches) et viennent de ses chiffres (bilan, § 1). Après la révision, un script compare prédictions et rapports. Un écart veut dire qu'il faut juger : soit l'agent a trouvé quelque chose, soit la requête était mal comprise.

**A1, le planificateur (Opus).**
- *But* : découper la révision en dossiers et dire, pour chaque énoncé exact, sa voie Lean. Le livrable est un `plan-NNN.json` valide, avec un plan de 30 Ko au plus.
- *Lancé quand* le paquet de l'étape 0 existe et passe son contrat.
- *Arrêt* : le JSON est valide et complet, ou 45 min sont écoulées.
- *Prédiction* :
  - 25 à 35 Ko ; il dépasse les 30 Ko une fois sur trois (Opus détaille volontiers) ;
  - 2 à 5 erreurs du plan trouvées ensuite (7 à la révision 001, mais les listes de lecture seront tirées du graphe) ;
  - pour la voie Lean, il range environ 10 énoncés en L1, 7 en L2, 4 en L3, et une dizaine en N ou en P (§ 5.1) ;
  - il propose de diviser D7 (30 % des fiches).
- *Ce qui surprendrait* : aucune division proposée (S07), ou un énoncé numérique rangé en L1 (S05).

**A2, les lecteurs de dossier (Sonnet, 8 au plus).**
- *But* : pour le dossier k, lever des drapeaux et tester les congruences en faisant varier leur paramètre. Chaque drapeau donne sa nature et, s'il en existe un, le procédé court qui le juge.
- *Livrable* : un dossier de 30 Ko au plus, et son JSON écrit après chaque section.
- *Lancé quand* le plan est validé.
- *Arrêt* : le dossier est fini, ou l'agent atteint 60 min ou 150 appels.
- *Prédiction, par dossier* :
  - 4 à 8 drapeaux (la révision 001 : de 3 à 9, 6,4 en moyenne) ;
  - leur nature : un tiers de procédé court, un tiers d'association, un sixième d'assemblage, le reste en références et en plan ;
  - 5 à 10 fiches proposées et 6 à 12 congruences ;
  - 30 % de références « à vérifier ».
- *Prédiction, après jugement* : ⅓ à ½ des drapeaux confirmés, et peu d'infirmés. La révision 001 n'en a infirmé aucun, mais 28 restent à juger : cette prédiction est la plus incertaine.
- *Ce qui surprendrait* :
  - 0 drapeau, ou plus de 15 ;
  - plus de 90 % de « confirmé » dans ses propres verdicts : la question était orientée (S09) ;
  - le mot « erreur trouvée » (S11).

**A3, le contradicteur (Opus, un autre modèle que les lecteurs).**
- *But* : refaire, par un calcul indépendant, les trois énoncés les plus forts de chaque dossier, choisis par moi.
- *Livrable* : pour chacun, « retrouvé », « non retrouvé » ou « autre valeur », avec le code.
- *Lancé quand* les dossiers sont jugés (étape 4) ; il ne reçoit que les énoncés et leurs définitions, pas les dossiers.
- *Arrêt* : les 24 énoncés sont traités, ou 60 min sont écoulées.
- *Prédiction* :
  - 70 à 90 % retrouvés ;
  - les écarts portent surtout sur l'association, et sur les valeurs qui dépendent d'un choix de cadre (un seuil, un classement).
- *Ce qui surprendrait* : 100 % retrouvés, avec les mêmes méthodes que les dossiers : il a recopié (S23).

**A4, le formalisateur Lean (Opus).**
- *But* : écrire l'énoncé Lean de chaque énoncé des voies L1 et L2, sans preuve. Chaque énoncé porte en commentaire l'énoncé français et son id ; les définitions du corpus sont reprises et citées.
- *Livrable* : des fichiers qui compilent avec `sorry`.
- *Lancé quand* le plan est validé, en même temps que les lecteurs.
- *Arrêt* : tous les énoncés sont écrits, ou 45 min sont écoulées.
- *Prédiction* :
  - 17 énoncés écrits ;
  - 1 à 3 écarts de formalisation vus ensuite par la rétro-traduction, surtout en L2. Exemples : « pour tout q » contre « q ≤ 30 », ℝ contre ℚ, une définition de ω.
- *Ce qui surprendrait* : aucun écart du tout, à vérifier par toi avant d'y croire.

**A5, le rétro-traducteur (Sonnet, à l'aveugle).**
- *But* : dire en une phrase française ce que dit chaque énoncé Lean, avec ses quantificateurs, ses domaines et ses hypothèses.
- *Livrable* : `retro-NNN.json`.
- *Lancé quand* les énoncés compilent. Il ne reçoit que les fichiers Lean, sans commentaires.
- *Arrêt* : tous les énoncés sont traduits, ou 20 min sont écoulées.
- *Prédiction* :
  - 80 % au moins des paraphrases concordent avec l'énoncé d'origine ;
  - les écarts portent sur les quantificateurs et les domaines.
- *Ce qui surprendrait* : 100 % de concordance mot pour mot, signe d'une fuite des commentaires (S31).

**A6, le prouveur Lean (Opus, avec le CI).**
- *But* : prouver les énoncés gelés sans les modifier, sans `sorry`, sans axiome nouveau.
- *Livrable* : pour chaque énoncé, un statut tiré du journal du CI : « prouvé », « échec » avec le message, ou « lemme manquant ».
- *Lancé quand* les énoncés sont gelés (étape 4).
- *Arrêt* : tout est prouvé, ou 2 h sont écoulées, ou 10 passages du CI sont faits.
- *Prédiction* :
  - L1 : 10 sur 10, en moins d'une heure ;
  - L2 : 3 à 5 sur 7 ; les échecs viennent de noms de lemmes ou de définitions manquantes ;
  - 0 énoncé modifié (le gel rendrait toute modification visible) ;
  - 0 à 2 `native_decide`.
- *Ce qui surprendrait* :
  - un énoncé de L2 prouvé en quelques minutes par `simp` : l'énoncé est peut-être devenu trivial (S27) ;
  - une somme de contrôle changée (S34).

**A7, le vérificateur de fin d'arc (Sonnet).**
- *But* : lever des drapeaux sur les comptes, les liens, les dates et les statuts de l'arc, sans rien corriger. Il écrit aussi `arc-NNN.md` (10 Ko au plus).
- *Livrable* : la liste de ses drapeaux, avec leur nature.
- *Lancé quand* l'arc est commité. Sa consigne est tirée de git par script (S39).
- *Arrêt* : la liste est rendue, ou 30 min sont écoulées.
- *Prédiction* :
  - 3 à 11 drapeaux par arc, surtout de procédé court (l'arc 002 en a donné 6, l'arc 003 en a donné 11, tous justes) ;
  - 25 à 30 min, autant que d'écrire un récit.
- *Ce qui surprendrait* : aucun drapeau sur un arc qui a changé des comptes.

**La session (moi) et toi.**
- Je juge les drapeaux de procédé court, je fais tourner les scripts, et j'écris la synthèse.
- Tu juges l'association et l'assemblage, et tu valides chaque énoncé Lean avant son gel.
- *Ma prédiction* : 2 à 4 excès dans mon premier En bref, trouvés par la relecture verbe par verbe (S43). J'en ai fait 5 à la révision 001.

## 4. Le gabarit d'une consigne

Une consigne a toujours les mêmes huit parties. Elle est gelée au lancement : sa somme sha256 est notée dans le plan. Si on la change, c'est un nouveau lancement, pas une reprise (S44).

1. **Rôle** : une phrase.
2. **But** : une question, un livrable et un critère d'arrêt. Une seule question par agent.
3. **Entrées** : une liste tirée du graphe des fichiers par script, avec leurs sommes.
4. **Définitions** : le glossaire (drapeau, procédé court, association, assemblage, (A), exact, structure), plus les notations du corpus qui ont deux sens, avec leur partie. Exemples : complément, sphère et boule, α_n, ppm (S16).
5. **Ce qui n'est pas ton travail** : juger, corriger le corpus, écrire ailleurs que dans ton fichier.
6. **Sortie** : le schéma JSON, écrit sur disque au fil des sections ; le code dans le dépôt.
7. **Budget** : la taille, la durée, le nombre d'appels.
8. **Voix** : le français simple, sans première personne.

**Deux règles de formulation**, tirées de la révision 001.
- Les questions sont ouvertes (« est-ce que… ? »), et chacune dit ce qui la rendrait fausse (S09).
- Aucune consigne ne contient de prédiction (S06).

## 5. La voie Lean en détail

### 5.1 Le tri des énoncés du recueil

Le tableau donne l'inventaire, avec, pour chaque énoncé, sa voie, l'outil qui le prouverait et le risque de confusion principal. La prédiction est celle de A6.

| énoncé | où | voie | en Lean | risque |
|---|---|---|---|---|
| 2⁻¹⁷ = 5¹⁷·10⁻¹⁷ | fiche 001 | L1 | `norm_num` | — |
| DR(a·b) = DR(DR(a)·DR(b)) ; 10⁶ − 1 = 7 × 142 857 ; l'orbite de ×2 modulo 9 | fiche 013 | L1 | `Nat.mul_mod`, `decide` | S29 : DR vaut 9, pas 0, pour les multiples de 9 |
| 1/(i·y) = −i/y | fiche 014 | L1 | `field_simp` sur ℂ | — |
| 10a + u ≡ a + u (mod 3) | fiche 015 | L1 | `omega` | — |
| Φ₆(10) = 7 × 13 ; l'ordre de 10 vaut 6 modulo 7 et modulo 13 | révision 001, § 4.10 | L1 | `norm_num` ; `orderOf` dans `ZMod`, `decide` | — |
| N(3 + i) = 10, N(3 + ω) = 7, N(3 − ω) = 13 | bilan, § 4 | L1 | `Zsqrtd.norm` pour les entiers de Gauss ; ceux d'Eisenstein à définir | S29 : la définition de ω |
| C(n, 2) impair ⇔ n ≡ 2 ou 3 (mod 4) | dossier ombres | L1 | `Nat.choose_two_right`, `omega` | — |
| d² + c² = 4 pour deux vecteurs unitaires | fiche 016 | L1 | `norm_add_sq_real`, `norm_sub_sq_real` | — |
| le Venn antipodal à 3 courbes, en combinatoire : 8 vecteurs de signes, l'antipode est le complément | bilan, § 3 | L1 | `decide` sur `Fin 3 → Bool` | S28 : la combinatoire n'est pas la topologie |
| l'arithmétique du facteur 2 de Hardy–Littlewood | fiche 021 | L1 | `norm_num` | S28 : le facteur vient d'une conjecture, et Lean ne prouverait que l'arithmétique |
| −1 est un carré modulo p ⇔ p ≡ 1 (mod 4) | lien K5 | L2 (déjà dans Mathlib) | `ZMod.exists_sq_eq_neg_one_iff` | — |
| le dipôle de poids rationnels est nul seulement à poids égaux (17 premier) | bilan, § 4 | L2 | `Polynomial.cyclotomic.irreducible_rat`, `minpoly` | S27 : des poids réels au lieu de rationnels |
| E[(1 − E)^j] = (−1)^j·!j | révision 001, § 4.10 | L2 | `numDerangements` | — |
| la règle des faux liens p_a + p_b < Σp² | fiche 017 | L2 | algèbre réelle, après avoir défini le simplexe pesé | S29 |
| l'arête √(2K/(K − 1)) et la corde √(2(K − 2)/(K − 1)) du simplexe centré | fiche 016 | L2 | `EuclideanSpace`, sommes finies | — |
| le lemme des chiffres de la famille b = q² + 1 | dossier bases, § 3.2 | L2 | arithmétique modulaire | S27 : pour tout q, alors que le script vérifie jusqu'à q = 30 |
| W_c/W_r = √(n/(4π)) | fiche 020 | L2 | dépend du modèle d'aire | S29 |
| l'obstruction de parité du Venn antipodal | dossier ombres | L3 | la topologie du plan projectif ; peut-être les bibliothèques de Grimes (Jordan, Schoenflies) | pas maintenant |
| le minimum de Kakeya dans F_q, pour q de 4 à 9 | fiche 019 | L3 | un certificat et `native_decide` | pas maintenant |
| l'aire 43/108, comme aire d'une réunion de triangles | révision 001, § 4.10 | L3 | la géométrie du plan | S28 : ne prouver que la formule et dire « l'aire » |
| la cavité du nerf v2 | révision 001, § 4 | L3 | homologie simpliciale | pas maintenant |

En N, ce qui reste en Python avec mpmath : 34·tan(π/34) ≈ π, (128/125) fois la lumière ≈ 1, 35,8 % ≈ 35,10 %, les presque-entiers de Heegner, la dérive des dizaines. En P, ce qui se teste en relançant un script : les fiches 005, 007, 008, 012 et 018.

### 5.2 Le gel et l'audit

- **Le gel.** Après ta validation (étape 4), un script écrit `lean/SHA256SUMS`, avec une somme par fichier d'énoncés. Le prouveur ne peut pas changer un énoncé sans que la somme change (S34).
- **L'audit**, écrit par un script dans `lean/audit-NNN.json`, comme le `audit.json` de Grimes :
  - le statut de chaque énoncé, lu dans le journal du CI ;
  - les `sorry` et les `admit` restants ;
  - la sortie de `#print axioms` (sans `sorryAx`) ;
  - la liste des `native_decide`.
- **La frontière de confiance.** Un énoncé prouvé par `native_decide` s'écrit « exact (Lean, native_decide) ». Le calcul est fait par le compilateur, pas vérifié par le noyau. Le README de Grimes le dit pour ses propres certificats.

### 5.3 Les versions

On épingle la chaîne d'outils et Mathlib (`lean-toolchain`, `lake-manifest.json`). Je propose les versions des projets de Grimes, Lean v4.32.1 et Mathlib au commit `520045ab`, qui compilent ensemble d'après leur README. On ne dépend pas de leur code : seules les versions sont reprises.

### 5.4 Où Lean tourne

**Dans cette session, Lean ne s'installe pas.** Les téléchargements des versions de GitHub sont refusés (403), et l'hôte du cache de Mathlib (`lakecache.blob.core.windows.net`) ne répond pas. Sans ce cache, Mathlib se compilerait pendant des heures sur 4 processeurs.

Trois possibilités, à choisir par toi :
1. **Un CI GitHub Actions sur ton dépôt** (ma proposition). Un fichier `.github/workflows/lean.yml` utilise l'action officielle `leanprover/lean-action`, qui installe Lean, récupère le cache de Mathlib et compile. Je pousse les fichiers, puis je lis le résultat par les outils GitHub de la session, sans réseau direct.
   - Le coût : quelques minutes d'Actions par passage.
   - C'est un ajout au dépôt, réversible.
2. **Ouvrir le réseau de l'environnement** : les hôtes de GitHub pour les versions, et l'hôte du cache. Il faut aussi environ 5 Go de disque.
3. **Ta machine.**

**Le dépôt de Dzoba reste en lecture seule.** On ne compile pas son projet Lean : son code se lit, il ne s'exécute pas. Réutiliser les bibliothèques de Grimes (Jordan, Schoenflies) pour la voie L3 demanderait ton accord. Il faudrait alors les compiler dans le CI, hors de cette session, et respecter leur licence Apache 2.0 (avis de licence et attribution).

## 6. Le registre des scénarios et les ramifications

Le registre [`scenarios-revision.csv`](scenarios-revision.csv) donne, pour chaque requête :
- comment elle peut être comprise ;
- ce qui y mène ;
- ce qu'on verrait dans la sortie ;
- où cela mène si on ne le voit pas ;
- si c'est déjà arrivé ;
- la formulation qui le prévient, et le procédé court qui le détecte.

| qui reçoit la requête | scénarios | dont observés |
|---|---:|---:|
| A1, le planificateur | 9 | 5 |
| A2, les lecteurs | 12 | 10 |
| A3, le contradicteur | 4 | 0 |
| A4, le formalisateur | 5 | 0 |
| A5, le rétro-traducteur | 2 | 0 |
| A6, le prouveur | 6 | 1 |
| A7, le vérificateur | 3 | 3 |
| la session | 5 | 5 |
| toi et moi | 3 | 3 |

Les rôles nouveaux, liés à Lean, n'ont encore rien d'observé : leurs scénarios sont des prédictions. Les ramifications des quatre confusions les plus coûteuses suivent.

**C1. « Drapeau » lu comme « erreur » (S11).**
- L'agent écrit « erreur trouvée ».
  - La session reprend le mot (S46), et le bilan compte un rendement.
    - Une règle de budget est fondée sur un faux rendement : c'est arrivé au bilan 001, puis a été corrigé.
  - La session corrige le corpus sans te montrer la correction (S42).
    - Une lecture devient un fait : c'est la classe d'erreur que la révision chasse.
- *Prévention* : le mot « drapeau » dans le schéma, et la règle du § 10.

**C2. L'écart de formalisation (S27, S28, S29).**
- L'énoncé Lean est plus faible que l'énoncé français.
  - « Exact (Lean) » se pose sur un autre énoncé.
    - L'autorité de la machine couvre un faux lien : l'erreur la plus difficile à voir, parce que tout le monde fait confiance au noyau.
- L'énoncé Lean est plus fort que le français.
  - La preuve échoue, et le prouveur veut modifier l'énoncé (S34).
    - Le gel le rend visible : la somme change, et le contrôle de l'étape 5 l'arrête.
- *Prévention* : la rétro-traduction à l'aveugle (A5), ta validation, puis le gel.

**C3. La liste de lecture incomplète (S03).**
- Un agent ne voit pas une partie de son sujet.
  - De faux trous apparaissent dans le nerf.
    - On écrit des fiches pour boucher des trous de lecture : la loi de Goodhart.
  - C'est arrivé à la révision 001 : 6 fichiers manquaient pour corde et 4 pour ombres. Les 4 « trous du corpus » de v1 étaient, d'après ma lecture, des trous de lecture.
- *Prévention* : des listes tirées du graphe des fichiers.

**C4. Un mot à deux sens (S16).**
- Si deux dossiers prennent deux sens différents, ils se contredisent.
  - Le désaccord se voit et se juge : du temps de jugement, mais pas d'erreur.
- S'ils prennent le même sens faux, ils se confirment.
  - L'erreur est corrélée et invisible (S25) : la pire des deux branches.
- *Exemples* : complément (antipodal ou polaire), sphère et boule, α_n, ppm.
- *Prévention* : le glossaire des notations du corpus, et un contradicteur d'un autre modèle.

**Une ramification de la session elle-même (S49).** Ton message est arrivé pendant que l'agent de fin d'arc 003 travaillait. J'ai clos l'arc 003 (ses onze drapeaux jugés, commit `69ac25e`) avant d'ouvrir celui-ci. La règle est donc de clore l'arc ouvert d'abord.

## 7. Le coût estimé

C'est une estimation, pas une mesure.

| rôle | durée |
|---|---:|
| A1 | 45 min |
| A2 | 8 × 60 min |
| A3 | 60 min |
| A4 | 45 min |
| A5 | 20 min |
| A6 | 120 min |
| A7 | 30 min |
| **total** | **≈ 13 h** |

La révision 001 a pris 15 h, sans Lean. Le texte écrit tomberait vers 0,5 Mo au lieu de 1,4, plus les fichiers Lean (une soixantaine de Ko). Ce qui change surtout, c'est ce qu'on obtient : une partie des énoncés exacts passe de « exact (script) » à « exact (Lean) », et chaque drapeau a un verdict.

## 8. Ce qu'il faut décider

1. **« LEAN ».** Est-ce bien le prouveur ? Si c'est la méthode de gestion, je reprends le plan dans ce sens.
2. **Le CI GitHub Actions** (§ 5.4) : je l'ajoute au dépôt, avec un premier projet `lean/` qui contient les énoncés de la voie L1 ? C'est le plus petit pas qui teste toute la chaîne : énoncés, rétro-traduction, gel, preuve et audit.
3. **La validation des énoncés Lean** : c'est toi qui valides la fidélité de chaque énoncé avant son gel. Veux-tu le faire énoncé par énoncé, ou sur un tableau des rétro-traductions ?
4. **Les bibliothèques de Grimes** pour la voie L3 (Jordan, Schoenflies, Apache 2.0) : on les laisse de côté pour l'instant ?
5. **Les prédictions** : je les garde ainsi, cachées aux agents, et comparées après la révision ?

## Sources

- L. de Moura, S. Ullrich, « The Lean 4 Theorem Prover and Programming Language », *CADE 28*, LNCS 12699, 625–635 (2021).
- The mathlib Community, « The Lean Mathematical Library », *CPP 2020*, 367–381 (2020).
- J. Grimes, *Lean formalization of a simple rotationally symmetric 17-Venn diagram* (2026), dans le dépôt [dzoba/venn17](https://github.com/dzoba/venn17), `verify/lean` (Apache 2.0) : la frontière de confiance de `native_decide` et l'audit des axiomes.
- R. W. Brislin, « Back-translation for cross-cultural research », *Journal of Cross-Cultural Psychology* 1, 185–216 (1970) : la rétro-traduction à l'aveugle.
- B. A. Nosek et al., « The preregistration revolution », *PNAS* 115, 2600–2606 (2018) : écrire les prédictions avant de voir les résultats.
- IEC 60812:2018, *Failure modes and effects analysis (FMEA and FMECA)* : le registre des scénarios en est une forme simple, avec les modes de défaillance, leurs effets, leur détection et leur prévention.
