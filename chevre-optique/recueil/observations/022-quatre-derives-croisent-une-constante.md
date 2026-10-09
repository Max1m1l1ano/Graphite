# 022 — Quatre dérives croisent une constante : π, 2√2, √2/2 et les 35,10 % de l'octaèdre

| champ | valeur |
|---|---|
| type | Coïncidence ; Hasard |
| statut | structure (le mécanisme : une grandeur qui dérive avec son paramètre passe par toutes les valeurs de son intervalle ; la probabilité d'en croiser une nommée se calcule) |
| partie | bilan de la révision 001 (fiches 002, 004, 018 et 021) |
| document | [bilan-001.md](../revisions/bilan-001.md), § 5 ; [revision-001.md](../revisions/revision-001.md), § 5 (arbre P7) et § 7 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), sections 4.2 (fiche 021) et 4.8 (fiche 018) ; [`scripts/venn_ppm.py`](../../scripts/venn_ppm.py), section 2 (fiche 004) ; [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 7, fonction `varie` (fiche 002) |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md), § 4.2 et 4.8 ; [`resultats/venn_ppm.md`](../../resultats/venn_ppm.md), § 2 ; [`resultats/centre_venn.md`](../../resultats/centre_venn.md), § 7 |
| image | [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneaux c et d |
| dimension | D7 hasard et méthode |
| test | la variation du paramètre, appliquée aux quatre : chaque grandeur traverse la constante sans s'y arrêter |
| arc | 2026-10-09, arc 002 (bilan de la révision 001) |
| révisé | non |

## Le contexte qui précède

L'auteur a demandé un bilan de la révision 001, et de regarder ce qu'elle rapporte sur les hasards et les coïncidences. En relisant les résultats, le même scénario revient quatre fois. Les résultats de la révision en avaient déjà rapproché deux (§ 4.8 : « encore une dérive qui croise une constante »).

## L'observation

- **Fiche 021.** Le rapport des dizaines de premiers vaut 3,1448 à 10⁵ (π à 0,10 %), puis 2,8321 à 10⁶ (2√2 à 0,13 %), puis 2,63 et 2,53 : il dérive vers 2.
- **Fiche 018.** Le centre du masque binaire est à 0,71 px du centre de symétrie au seuil t = 0,05 (√2/2 à 1 %), puis il continue jusqu'à 27,4 px.
- **Fiche 004.** La part des triangles vaut 35,95 %, puis 35,76 %, puis 35,12 % à 17, 19 et 23 courbes, en moyenne sur 4, 12 et 5 certificats (dossier ombres ; pour un seul certificat par n, la fiche 004 donne 35,8 et 35,7 %). Elle passe par les 35,0959 % de l'octaèdre vers 23 courbes.
- **Fiche 002.** (128/125) × la lumière du N-gone ne vaut 1 qu'en N = 16,70, tout près de 17 : un passage, sans loi.

À une seule valeur du paramètre, chacune ressemble à une découverte au niveau du ppm. Dès qu'on fait varier le paramètre, c'est une dérive qui traverse la constante.

**Pourquoi c'est important.** Une grandeur qui dérive croise beaucoup de constantes, et la chance que l'une d'elles tombe près d'une valeur échantillonnée du paramètre est grande. Le dossier lumière (N8) montre que l'écart d'un passage par une valeur, mesuré en ppm, est uniforme : les 845 ppm de la fiche 002 sont au rang 0,6, un résultat banal. Pour le sujet d'étude, c'est le cadre (le N, le t ou le n qu'on a choisis) qui fige une dérive en coïncidence.

**La règle qui en sort.** Quand un rapport mesuré tombe sur une constante, demander d'abord : « et au N suivant ? ».

## Ce que le script produit

Chaque script cité fait déjà varier le paramètre : la taille N (section 4.2), le seuil t (section 4.8), le nombre de courbes n (`venn_ppm.py`, section 2) et N continu (`centre_venn.py`, fonction `varie`). La fiche réunit les quatre courbes ; aucun calcul nouveau.

## Liens et pistes

- Les fiches liées :
  - 012 : les tests à tolérance, qui jugent une paire à une seule valeur du paramètre ;
  - 017 : le cadre qui fabrique des liens ;
  - 023 : les liens vrais par construction, l'autre famille du bilan.
- Ailleurs, c'est le même piège que l'effet de regard ailleurs (Gross et Vitells, 2010), avec un paramètre continu au lieu d'un catalogue.
- La piste : un test qui compte les passages. Pour une famille indexée par un entier, la probabilité qu'une constante tombe à moins de ε d'une valeur atteinte se calcule directement (dossier lumière, N8). À refaire sur les 31 constantes de la partie XXIX, § 5.5.

Dimensions voisines, à confirmer à la révision : D2 bases, chiffres et congruences (la fiche 021) ; D3 grain, pixels et précision (la fiche 018) ; D6 sphères, cubes, Venn et symétries (la fiche 004).
