# 006 — Le centre de la lumière bouge selon la façon de la peser (0,6 à 46 px)

| champ | valeur |
|---|---|
| type | Analogie ; Causalité |
| statut | structure (exact : à poids égaux, le barycentre est le centre ; mesuré : le dipôle des couleurs) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 1.2 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 1 |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae1_centre_moitie.png`](../../figures/ae1_centre_moitie.png), panneaux a et b |
| dimension | D3 grain, pixels et précision |
| test | mesure contre la précision du centre de symétrie (0,003 px) : l'écart du masque RGB en vaut 4 462 fois |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | non |

## Le contexte qui précède

J'avais écrit que le barycentre de l'encre était décalé « à cause des différences de luminosité ». L'auteur a répondu : « Non, cet écart est significatif ! »

## L'observation

La luminance de l'œil met le centre de la lumière à 0,6 px du centre de symétrie, le masque RGB à 13,6 px, la moyenne RGB à 33 px et l'énergie à 46 px. C'est le même procédé que le déplacement induit par la couleur des étoiles doubles (Wielen, 1996), et le même schéma que le dipôle de HD.

## Ce que le script produit

Le script calcule les six barycentres, mesure les couleurs des 17 courbes et le premier harmonique (dipôle) de leurs poids.

## Liens et pistes

Fiche 007 (le biais propagé) ; fiche 008 (le centre exact).

Dimensions voisines, à confirmer à la révision : D8 physique ; D6 symétries.
