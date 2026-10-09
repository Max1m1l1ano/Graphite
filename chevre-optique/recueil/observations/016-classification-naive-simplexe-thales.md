# 016 — La classification naïve est un simplexe : sa diagonale et la corde de la chèvre font un angle droit (Thalès)

| champ | valeur |
|---|---|
| type | Analogie ; Corrélation |
| statut | exact (d² + c² = 4 pour deux vecteurs unités ; la corde de la chèvre est la corde c du simplexe à K = 1 + 1/x₀ dimensions) |
| partie | révision 001 (parties XX et XXIV) |
| document | [revision-001.md](../revisions/revision-001.md), § 2 ; [tiers-dimension.md](../../tiers-dimension.md) ; [sphere-faisceaux.md](../../sphere-faisceaux.md) |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), section 1 |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md) |
| image | [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneau a |
| dimension | D1 la chèvre et les cordes |
| test | variation du paramètre : K − n tend vers 7/3 selon 7/3 − 112/(45n) + 3856/(189n²) (2,33086 à n = 1 000, accord à 6 chiffres) ; contrôle numérique du simplexe centré : d² + c² = 4 à 10⁻¹² près |
| arc | 2026-10-07, arc 001 (révision 001) |
| révisé | non |

## Le contexte qui précède

L'auteur demande que la révision range les fiches dans un « Venn multidimensionnel qu'on sait va finir par donner la diagonale √2 », classé naïvement au début, avec un partage équitable des aires entre les prompts. En cherchant comment mesurer ce √2 sur le recueil, on a centré les vecteurs d'appartenance des fiches.

## L'observation

Une classification naïve à parts égales dans K dimensions, une fois centrée, est le simplexe régulier inscrit dans la sphère. Deux fiches de dimensions différentes sont à d = √(2K/(K − 1)) ; la corde vers l'antipode vaut c = √(2(K − 2)/(K − 1)). Thalès donne d² + c² = 4, et les deux côtés tendent vers √2 quand K grandit. La corde de la chèvre de dimension n est exactement une corde c de ce simplexe, pour K = 1 + 1/x₀(n) = n + 2 + (N − n), où N − n est le tiers de dimension de la partie XXIV. Le √2 qui « s'affirme » quand les dimensions se multiplient est donc le même que celui de la chèvre infinie, vu des deux côtés de l'angle droit.

## Ce que le script produit

La section 1 de `scripts/revision_001.py` recalcule les cordes ρ_n par les calottes (elles redonnent le tableau de la partie XX), en déduit K, compare K − n au développement 7/3 − 112/(45n) + 3856/(189n²) issu de la partie XXIV, et contrôle le simplexe centré sans formule.

## Liens et pistes

Partie XX (deux directions au hasard en grande dimension sont à √2 ; les arêtes √2 du polytope croisé) ; partie XXIV (la chèvre de dimension n a la corde du simplexe de dimension n + 1/3, plan en 1/x₀ = n + 4/3 − …) ; partie III (la concentration de la mesure). Piste : le décalage 7/3 = 2 + 1/3 et le 4/3 de la partie XXIV dans la mesure de la diagonale des révisions suivantes.

Dimensions voisines, à confirmer à la révision : D7 hasard et méthode (la classification) ; D6 sphères, cubes, Venn et symétries (le simplexe).
