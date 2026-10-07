# Le recueil : hasards, coïncidences, faits amusants, analogies, corrélations et causalités

Le recueil garde les moments où une remarque surgit pendant le travail. Ce peut être un hasard, une coïncidence, un fait amusant, une analogie, une corrélation ou un lien de causalité. Chaque moment est rattaché à ce qui l'a produit : le script, la partie, l'image et le contexte.

**Ces mots ne sont pas à éviter.** Ils sont précieux : c'est par eux que les moments s'enchaînent d'une partie à l'autre, et le recueil permet de les comparer, de les réviser et de les regrouper. Le protocole complet est dans [CLAUDE.md, § 10](../CLAUDE.md).

## Ce qu'il contient

| chemin | contenu |
|---|---|
| [`index.md`](index.md) et `index.csv` | le tableau de toutes les fiches, régénéré par `python3 scripts/recueil_index.py` |
| `observations/NNN-titre.md` | une fiche par observation (numérotation continue) |
| [`arcs/`](arcs/README.md) | les données brutes de chaque arc réponse : `arc-NNN.md` (le récit) et `arc-NNN.csv` (une ligne par production) |
| `revisions/` | les synthèses de révision, `revision-NNN.md` |
| `dossiers/` | les dossiers thématiques nés des révisions |

## Une fiche

Chaque fiche commence par un tableau `champ | valeur` (le script d'index le lit), puis quatre parties :
- le contexte qui précède ;
- l'observation ;
- ce que le script produit ;
- les liens et les pistes.

| champ | ce qu'on y met |
|---|---|
| type | un ou plusieurs des six mots : Hasard, Coïncidence, Fait amusant, Analogie, Corrélation, Causalité |
| statut | exact, structure (un mécanisme connu et la loi de l'écart), hasard (testé), ouvert, à tester |
| partie | le numéro de la partie (ou « recueil » si la remarque est née hors d'une partie) |
| document | le document et la section |
| script | le script qui traite les données, et sa section |
| données | le fichier de résultats |
| image | l'image `.png` et le panneau, s'il y en a une ; sinon « — » |
| dimension | d'abord une seule (D1 à D8 ci-dessous), puis d'autres au fil des révisions |
| test | le test appliqué et son verdict (voir CLAUDE.md, § 10 : le choix du test) |
| arc | la date et l'arc réponse |
| révisé | non, ou le numéro de la révision |

## Les dimensions de départ

On les classe naïvement au début. À chaque révision, les observations rangées sur une seule dimension se recoupent, et les dimensions se recomposent.

| | dimension | ce qu'elle couvre |
|---|---|---|
| D1 | la chèvre et les cordes | la moitié de l'aire, les dimensions, Ullisch, √2 |
| D2 | bases, chiffres et congruences | base 10, 2, 3, 12 ; i modulo b ; racines digitales ; Midy ; les premiers |
| D3 | grain, pixels et précision | ppm, Gauss, échantillonnage, granularité, centres |
| D4 | optique et diffraction | diaphragmes, FTM, Fresnel, Newton, défocalisation |
| D5 | Kakeya, Perron et aiguilles | recouvrements, branches, éventails |
| D6 | sphères, cubes, Venn et symétries | polytopes, ombres, faisceaux, cohomologie |
| D7 | hasard et méthode | tests, coïncidences, statistiques, chaînes de données |
| D8 | physique | les analogies physiques : astrométrie, molécules, lasers, Planck |

## Quand réviser

- Quand les fiches non révisées sont entre 11 et 15 : il ne faut jamais laisser la pile dépasser 15.
- Ou après 10 à 16 arcs réponses depuis la dernière révision.
- Ou quand l'auteur le demande.

C'est le premier de ces trois signaux qui compte. `python3 scripts/recueil_index.py` compte les fiches et dit si une révision est due.

## La diagonale √2

L'index suit aussi, à chaque passage, la forme du Venn des dimensions. On range chaque fiche sur sa dimension principale, puis on retire la fiche moyenne : on obtient un simplexe. À parts égales, son arête vaut √(2K/(K − 1)) pour K dimensions, et elle rejoint √2 quand K grandit, comme la corde de la chèvre de dimension infinie (révision 001, § 2). À parts inégales, deux dimensions rares paraissent liées sans rien partager : l'index les signale. C'est le « partage équitable des aires » qui l'empêche.
