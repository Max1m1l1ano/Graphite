# 015 — Les dizaines de premiers forment un Venn à 4 ensembles, et le reste modulo 3 choisit la face du cube

| champ | valeur |
|---|---|
| type | Analogie ; Fait amusant ; Corrélation |
| statut | exact (10a + u ≡ a + u mod 3) et calculé (motifs sous 10⁶) |
| partie | recueil |
| document | [resultats/recueil_verifications.md](../../resultats/recueil_verifications.md), § 6 |
| script | [`scripts/recueil_verifications.py`](../../scripts/recueil_verifications.py), section 6 |
| données | [`resultats/recueil_verifications.md`](../../resultats/recueil_verifications.md) |
| image | — |
| dimension | D2 bases, chiffres et congruences |
| test | exact pour la face ; les comptes des 16 motifs sous 10⁶ (165 quadruplets, tous en a ≡ 1 mod 3) |
| arc | 2026-10-07, arc 001 (le recueil : message fondateur du § 10 de CLAUDE.md) |
| révisé | non |

## Le contexte qui précède

L'auteur décrit une analyse hiérarchique des premiers : les unités {1, 3, 7, 9}, puis les dizaines, centaines et milliers, « en Perron », pour suivre l'évolution des trous.

## L'observation

Chaque dizaine choisit lesquels de 10a + 1, 3, 7, 9 sont premiers : un sommet du cube {0, 1}⁴, une région d'un Venn à 4 ensembles. Le reste de a modulo 3 choisit la face accessible :
- a ≡ 0 : seulement {1, 7} ;
- a ≡ 2 : seulement {3, 9} ;
- a ≡ 1 : les quatre.

D'où des paires {1, 7} et {3, 9} près de trois fois plus fréquentes que les autres (8 424 contre 3 008 et 2 941).

## Ce que le script produit

Le script crible jusqu'à 10⁶, compte les premiers par chiffre des unités, les 16 motifs de dizaines et la face de chaque reste modulo 3.

## Liens et pistes

Le Venn multidimensionnel que l'auteur propose pour le recueil ; la série singulière de Hardy et Littlewood ; partie XXVIII (le cube {0, 1}ⁿ et ses deux ombres). Piste : étendre aux centaines (2⁴ motifs par dizaine, 10 dizaines par centaine) pour suivre les trous « en Perron ».

Dimensions voisines, à confirmer à la révision : D6 Venn et cube ; D7 hasard des premiers.
