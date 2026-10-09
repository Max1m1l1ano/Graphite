# 017 — Le cadre fabrique des liens : deux dimensions rares paraissent liées quand les aires ne sont pas partagées également

| champ | valeur |
|---|---|
| type | Corrélation ; Hasard ; Causalité |
| statut | exact (l'arête passe sous √2 exactement quand p_a + p_b < Σp²) |
| partie | révision 001 |
| document | [revision-001.md](../revisions/revision-001.md), § 3 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), section 2.1 |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md) |
| image | [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneau b |
| dimension | D7 hasard et méthode |
| test | la règle p_a + p_b < Σp² prédit le côté de √2 pour les 15 paires de dimensions des fiches 001 à 015 (15 sur 15) ; avec des parts égales, aucune paire ne passe sous √2 |
| arc | 2026-10-07, arc 001 (révision 001) |
| révisé | non |

## Le contexte qui précède

Pour mesurer la « diagonale √2 » du Venn des dimensions, la révision 001 centre les vecteurs d'appartenance des 15 premières fiches, classées chacune sur une seule dimension (fiche 016). Les parts sont inégales : D2 et D7 ont 4 fiches, D3 en a 3, D6 en a 2, D1 et D4 en ont 1, D5 et D8 aucune.

## L'observation

Les fiches de D1 et de D4, qui ne partagent rien, sont à 1,3636 l'une de l'autre, sous √2 : elles paraissent liées. Celles de D2 et de D7, les deux grosses classes, sont repoussées à 1,7206. La règle est exacte : la corrélation entre deux classes est positive quand p_a + p_b < Σp². Deux classes rares ont en commun de ne pas être les grosses. Avec des parts égales, p_a + p_b = 2/K > Σp² = 1/K, et le lien apparent disparaît. Le partage équitable des aires que demande l'auteur est donc la condition qui empêche le cadre de fabriquer des corrélations.

## Ce que le script produit

La section 2.1 de `scripts/revision_001.py` calcule les 15 arêtes du simplexe déformé, les compare à la règle et au simplexe régulier (1,5492 pour K = 6).

## Liens et pistes

C'est le « problème des doubles zéros » de l'écologie numérique (Legendre et Legendre, *Numerical Ecology*), de la même famille que les corrélations parasites des données à somme constante (Pearson, 1897 ; Chayes, 1960 ; Aitchison, 1986), un piège connu des données de microbiome en abondances relatives (Gloor et al., 2017). C'est un exemple direct du sujet d'étude : la restriction du cadre produit des motifs qui ne sont pas dans les données. Piste : chercher, dans les articles qui classent des observations par catégories de tailles inégales, des liens entre catégories rares qui ne survivent pas à un rééquilibrage.

Dimensions voisines, à confirmer à la révision : D6 sphères, cubes, Venn et symétries (le simplexe déformé).
