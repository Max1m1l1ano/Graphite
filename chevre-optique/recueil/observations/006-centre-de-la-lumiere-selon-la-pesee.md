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
| dimension | D3 grain, pixels et précision ; puis, à la révision 001 : D8 physique, D7 hasard et méthode, D6 sphères, cubes, Venn et symétries |
| test | mesure contre la précision du centre de symétrie (0,003 px) : l'écart du masque RGB en vaut 4 462 fois |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

J'avais écrit que le barycentre de l'encre était décalé « à cause des différences de luminosité ». L'auteur a répondu : « Non, cet écart est significatif ! »

## L'observation

La luminance de l'œil met le centre de la lumière à 0,6 px du centre de symétrie, le masque RGB à 13,6 px, la moyenne RGB à 33 px et l'énergie à 46 px. C'est le même procédé que le déplacement induit par la couleur des étoiles doubles (Wielen, 1996), et le même schéma que le dipôle de HD.

## Ce que le script produit

Le script calcule les six barycentres, mesure les couleurs des 17 courbes et le premier harmonique (dipôle) de leurs poids.

## Liens et pistes

Fiche 007 (le biais propagé) ; fiche 008 (le centre exact).

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Tests 4.8 et 4.9 (T4) : la seconde cause est le seuil, pas l'ordre de dessin ; la moitié ne bouge pas avec le seuil (fiche 018). La cause « dipôle des couleurs » est établie par une intervention sur un système modèle : sur un Venn à 13 courbes de palette connue, G·H₁ prédit l'écart sans paramètre libre (2,08 px prédits, 2,05 à 2,20 observés), et l'ordre de dessin ne compte pas (dossier méthode ; refait par revision_001.py, § 4.12). Sur l'image à 17 courbes, la palette reste ajustée : le code de rendu n'est pas publié (dossiers grain et lumière).
- Dossier [grain](../dossiers/grain-pixels-centres.md) : lien fort ; la causalité se précise grâce à T4.
- Dossier [lumière](../dossiers/lumiere-et-physique.md) : structure, causalité précisée : une palette de conception presque isoluminante et le seuil ; la branche « photocentre » est à détacher de P8 en un triangle « barycentre pesé » (D8 contre D3).
- Dossier [méthode](../dossiers/hasard-et-methode.md) : bon test (mesure contre le budget) ; la pesée tient, l'énoncé causal dépasse le test.
- Dossier [ombres](../dossiers/ombres-cube-venn.md) : structure.
