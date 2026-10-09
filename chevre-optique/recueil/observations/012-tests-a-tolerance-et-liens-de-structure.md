# 012 — Les tests à tolérance déclarent « hasard » des liens de structure

| champ | valeur |
|---|---|
| type | Hasard ; Corrélation ; Causalité |
| statut | calculé (banc d'essai : 10 relations, 6 techniques, 20 000 paires au hasard) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 7 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 7 |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneau f |
| dimension | D7 hasard et méthode ; puis, à la révision 001 : D6 sphères, cubes, Venn et symétries |
| test | le banc lui-même : précision poussée 4/4 et variation du paramètre 10/10 ; Bonferroni 7/10, catalogue brouillé 6/10, longueur de description 7/10 |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

L'auteur : « faire une analyse de hasard là-dessus ne devrait pas donner des résultats exacts au hasard, mais je sais que plusieurs techniques concluraient un hasard, et les tester nous permettrait de définir lesquelles sont les mieux faites pour notre situation ».

## L'observation

Seules deux méthodes ne se trompent jamais : pousser la précision, pour les identités ; faire varier le paramètre et vérifier la loi de l'écart, pour tout le reste. L'auteur a demandé de l'inscrire dans CLAUDE.md (§ 10).

## Ce que le script produit

Le script définit les dix relations, applique les six techniques et mesure les faux positifs sur 20 000 paires au hasard.

## Liens et pistes

Fiches 002, 003, 004 et 005. Limite : la variation du paramètre n'est pas indépendante de la vérité du banc.

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Test 4.7 (T5) : la même inégalité de Bonferroni, tronquée à l'ordre 2, donne la moitié de Kakeya fini (fiche 019). Le banc relu (dossier méthode, vérifié dans le code) : quatre cas sont des identités, trois verdicts de la variation sont écrits à la main, et la précision ne dit jamais « hasard ». « Ne se trompent jamais » est trop fort ; CLAUDE.md, § 10, le précise.
- Dossier [méthode](../dossiers/hasard-et-methode.md) : bon test comme pratique, avec réserve ; « ne se trompent jamais » dépasse le test.
