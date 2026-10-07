# 005 — Un Venn à 19 courbes coupe ses croisements exactement en deux

| champ | valeur |
|---|---|
| type | Fait amusant ; Hasard |
| statut | ouvert (compatible avec le hasard : 1,6 % par tirage, 18 % pour un sur douze) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 2.5 et § 7.3 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 2 (les 18 certificats) |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae1_centre_moitie.png`](../../figures/ae1_centre_moitie.png), panneau f |
| dimension | D6 sphères, cubes, Venn et symétries |
| test | réplication sur les 12 Venn à 19 courbes (écart quadratique ±24,7 orbites ; les deux autres ramp12h : +11 et −28) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | non |

## Le contexte qui précède

L'auteur demande une analyse où « la moitié de l'aire du disque fait la moitié de l'aire du Venn ». On compte, dans chaque certificat de Dzoba, les croisements de niveau ≥ (n + 1)/2.

## L'observation

`venn19-ramp12h-s192102` en met 262 143 de chaque côté. C'est possible parce que 2¹⁸ − 1 = 19 × 13 797 (Fermat). Pourtant, il n'est pas symétrique par le complément : un niveau et son miroir diffèrent de 703 croisements au plus.

## Ce que le script produit

Le script lit les 18 certificats, compte les croisements par niveau, l'écart à la moitié en ppm et en orbites, et teste la symétrie N_l = N_(n−l).

## Liens et pistes

L'auteur pense qu'un résultat exact ne vient pas du hasard (message du 7 octobre). Pour un réel à 50 chiffres, c'est vrai ; pour un entier, l'exactitude arrive avec une probabilité de l'ordre de 1/(dispersion). Piste : chercher une cause dans la méthode `ramp12h` (une rampe de 12 h sur le paramètre λ).

Dimensions voisines, à confirmer à la révision : D2 congruences (Fermat) ; D7 hasard.
