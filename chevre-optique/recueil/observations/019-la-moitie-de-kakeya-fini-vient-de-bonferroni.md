# 019 — La moitié de Kakeya fini vient de l'inclusion–exclusion (Bonferroni), pas de l'involution

| champ | valeur |
|---|---|
| type | Analogie ; Causalité |
| statut | structure (identité exacte : taille de K = q(q + 1)/2 + Σ C(m_P − 1, 2) ; minimum calculé pour q = 2, 3, 4, 5, 7, 8, 9) |
| partie | révision 001 (parties XIV et XXVII) |
| document | [revision-001.md](../revisions/revision-001.md), § 6 et 7 ; [aiguille-grille.md](../../aiguille-grille.md), § 5 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), section 4.7 |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md) |
| image | — |
| dimension | D5 Kakeya, Perron et aiguilles |
| test | variation du paramètre : le corps F_q et la parité de q (minimum exact par programmation linéaire en nombres entiers) |
| arc | 2026-10-07, arc 001 (révision 001) |
| révisé | non |

## Le contexte qui précède

La partie XIV a trouvé qu'un ensemble de Kakeya du plan fini F_q² couvre environ la moitié du plan, et l'a expliqué par les carrés modulo q (l'involution x ↦ −x). La carte des connexions (partie XXVII, § 9) en a fait une piste : est-ce la même moitié que celle des hémisphères (partie XX) ? En caractéristique 2, l'involution est l'identité : le plan de la révision a proposé de calculer q = 2, 4, 8.

## L'observation

Le minimum vaut exactement q(q + 1)/2 pour q = 2, 4, 8 (3, 10, 36), sans aucun point triple, et q(q + 1)/2 + (q − 1)/2 pour q = 3, 5, 7, 9 (7, 17, 31, 49), avec exactement (q − 1)/2 points triples. La moitié vient de l'inclusion–exclusion tronquée à l'ordre 2 (l'inégalité de Bonferroni), vraie dans toutes les caractéristiques ; l'involution ne compte que l'excès des q impairs. La piste XIV–XX se ferme par une obstruction, et un autre lien s'ouvre : tronquée à l'ordre 1, la même inégalité est la correction de Bonferroni de la fiche 012.

## Ce que le script produit

La section 4.7 de `scripts/revision_001.py` construit les corps F_q (tables d'addition et de multiplication par des polynômes irréductibles), calcule le minimum avec les symétries de la partie XIV, et compte les multiplicités des points.

## Liens et pistes

Partie XIV, § 5 ; partie XXVII, § 9 ; fiche 012 (Bonferroni). Pour q pair, la construction qui atteint la borne passe par une hyperovale (à vérifier dans la littérature) ; pour q impair, le minimum est celui de Blokhuis et Mazzocca (2008). Piste : q = 16 et q = 25, et l'analogue en dimension 3.

Dimensions voisines, à confirmer à la révision : D7 hasard et méthode (Bonferroni) ; D2 bases, chiffres et congruences (les corps finis).
