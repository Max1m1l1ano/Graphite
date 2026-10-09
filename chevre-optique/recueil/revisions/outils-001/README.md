# Les outils de la révision 001

Ce sont les outils qui ont produit la révision 001, archivés tels qu'ils ont tourné. Le bilan ([`bilan-001.md`](../bilan-001.md), § 7 et 10.1) propose de les réunir dans un script du dépôt, `scripts/revision_outils.py`.

**Ils ne se relancent pas tels quels.**
- Ils gardent les chemins absolus de la session : le dépôt `/home/user/Graphite/chevre-optique`, et un dossier de travail `/tmp/claude-0/…/scratchpad/revision-001/`, effacé avec le conteneur.
- Leurs entrées (`resultats_*.json`, `journal.jsonl`, `v2.json`) étaient dans ce dossier de travail. Leur contenu utile est conservé dans [`sorties-agents-001.json`](../sorties-agents-001.json) et dans le bloc JSON du § 1 de [`verification-croisee-001.md`](../verification-croisee-001.md).
- `stats_agents.py` lit les transcriptions des agents de la session (`/root/.claude/projects/…/subagents/`), qui ne sont pas dans le dépôt.

## Les workflows (étape 2 : les dossiers)

| fichier | ce qu'il a fait |
|---|---|
| `workflow-1-revision_001.js` | Le premier workflow : un agent Sonnet par dossier, deux à la fois, puis les agents de vérification croisée. Il a écrit corde, moitiés, bases et grain (95 à 146 Ko chacun). Un redémarrage du conteneur a arrêté lumière et aiguilles après 20 et 26 min, et la vérification croisée n'a jamais tourné. |
| `workflow-1b-recueil-reprise.js` | La reprise ratée du premier. Le texte de tous les prompts avait changé, donc le cache ne servait plus et les dossiers déjà écrits repartaient de zéro. Elle a été arrêtée au bout de 3 min, avant d'écraser quoi que ce soit. |
| `workflow-2-dossiers-reprise.js` | Le deuxième workflow, avec la consigne d'être concis. Il a écrit lumière et aiguilles. La limite d'usage hebdomadaire a coupé lumière juste avant sa sortie structurée, et empêché ombres et méthode de démarrer. |
| `workflow-3-ombres-methode.js` | Le troisième workflow, lancé après la levée de la limite. Il a écrit ombres et méthode. |
| `schemas.json` | Les deux schémas de sortie structurée, `dossier` et `verif`. |

## Les scripts (étapes 3 et 6, puis le bilan)

| fichier | ce qu'il fait | entrées | sorties |
|---|---|---|---|
| `extraire.py` | Extrait la sortie structurée de chaque agent depuis le journal d'un workflow, c'est-à-dire ses entrées `result`. | `journal.jsonl` | `resultats_*.json` |
| `v2.py` | Construit le recouvrement v2 : celui du plan (v1), plus les corrections de chaque agent. | `plan-001.md`, § 1.9 ; `resultats_*.json` | `v2.json` |
| `croisee.py` | Écrit la vérification croisée : le recouvrement v2 en JSON, les congruences, les doublons, les désaccords, les erreurs du plan, les trous et les fiches proposées. | `resultats_*.json`, `v2.json`, `resultats/revision_001.md` | `verification-croisee-001.md` |
| `fiches_par_dimension.py` | Classe les 64 fiches proposées par leur première dimension. | `resultats_*.json` | le tableau du § 7 de la vérification croisée |
| `sorties.py` | Réunit les sorties structurées des huit agents. | `resultats_*.json` | `sorties-agents-001.json` |
| `maj_fiches.py` | Marque les fiches 001 à 015 « révisé : 001 », avec les dimensions confirmées et les verdicts. Il est idempotent. | `resultats_*.json` | `recueil/observations/001` à `015` |
| `stats_agents.py` | Mesure, pour chaque agent, la durée, les appels d'outils et le contexte cumulé (bilan, § 1). | les transcriptions des agents | un tableau sur la sortie standard |

L'ordre d'emploi, après les workflows : `extraire.py`, `v2.py`, puis `scripts/revision_001.py`, qui lit le v2 pour refaire le nerf. Viennent ensuite `croisee.py`, `fiches_par_dimension.py`, `sorties.py` et `maj_fiches.py`.
