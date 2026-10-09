# 023 — Quatre liens de la révision 001 sont vrais par construction : ils ne pouvaient pas être faux

| champ | valeur |
|---|---|
| type | Analogie ; Corrélation |
| statut | exact (chacun se démontre en une ligne, à partir des définitions) |
| partie | bilan de la révision 001 (révision 001, parties XXIV et XXX) |
| document | [bilan-001.md](../revisions/bilan-001.md), § 3 ; [revision-001.md](../revisions/revision-001.md), § 2 ; [centre-venn.md](../../centre-venn.md), § 7.2 ; [ombres-cube-venn.md](../dossiers/ombres-cube-venn.md), § 3.5 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), sections 1 (K = 1 + 1/x₀) et 2.2 (T2) ; [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 7, fonction `varie` (cas E1 à E4) |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md), § 1 et 2.2 ; [`resultats/centre_venn.md`](../../resultats/centre_venn.md), § 7 |
| image | [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneau a ; [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneau f |
| dimension | D7 hasard et méthode |
| test | une question à poser avant tout test : « ce lien aurait-il pu être faux ? » Pour les quatre, non |
| arc | 2026-10-09, arc 002 (bilan de la révision 001) |
| révisé | non |

## Le contexte qui précède

L'auteur a demandé un bilan de la révision 001 : ce qu'elle rapporte, et ce que valent ses connexions. En classant ses résultats, quatre « liens » se démontrent sans aucun calcul, à partir des seules définitions.

## L'observation

1. **La corde de la chèvre est une corde du simplexe** (fiche 016). La partie XXIV donne ρ_n² = 2 − 2x₀. La corde du simplexe à K sommets vaut c_K² = 2 − 2/(K − 1). L'égalité ρ_n = c_K revient donc à poser K − 1 = 1/x₀ : elle définit K. Ce qui se calcule vraiment, c'est le développement K − n = 7/3 − 112/(45n) + …, et il vient de la partie XXIV.
2. **Les périodes de Gauss sont des ombres Σωⁱ** (dossier ombres, § 3.5). Une période de Gauss est, par définition, la somme des ζʰ sur une classe d'un sous-groupe de (ℤ/17)*. C'est l'ombre de l'indicatrice de cette classe.
3. **Les quatre identités du banc d'essai** (partie XXX, cas E1 à E4). Tous les tests ont raison sur elles : elles ne départagent pas les tests (dossier méthode).
4. **T2 : les fiches qui partagent un dossier passent sous √2.** C'est vrai de tout recouvrement de ces tailles (p = 0,93 en v1) : un dossier commun rapproche deux fiches par construction.

**Pourquoi c'est important.** Un lien vrai par construction passe tous les tests, même la variation du paramètre. Ce n'est pas une erreur : c'est un dictionnaire. Le § 1 de CLAUDE.md s'applique tel quel :
- ce qui est partagé exactement, c'est la définition ;
- la correspondance transporte une traduction : le tiers de dimension devient un nombre de dimensions K, une période de Gauss devient un point de l'ombre ;
- ce qui reste ouvert, c'est ce que la traduction permettra de calculer.

Ce qu'il ne faut pas faire, c'est présenter un dictionnaire comme une démonstration. La synthèse de la révision 001 titrait « la diagonale √2 démontrée » : le bilan corrige en « mise en équation ».

## Ce que le script produit

Rien de nouveau : la section 1 de `scripts/revision_001.py` calcule déjà K à partir de x₀, puis compare K − n au développement. La section 2.2 donne le p = 0,93 de T2 contre des dossiers tirés au hasard. La fonction `varie` de `scripts/centre_venn.py` contient les quatre identités.

## Liens et pistes

- Les fiches liées :
  - 016 : la première des quatre, à lire comme un dictionnaire ;
  - 012 : le banc d'essai ;
  - 022 : les dérives qui croisent une constante, l'autre famille du bilan.
- La règle pour les révisions suivantes : marquer chaque lien rapporté d'une case « aurait pu être faux : oui / non ». Seuls les « oui » sont des découvertes possibles ; les « non » sont des traductions, utiles à garder.
- **Ce que le dictionnaire de la fiche 016 transporte, et qu'on ne savait pas** (calculé pour ce bilan). L'arête du simplexe s'approche de √2 comme 1/(2K) : √(2K/(K − 1)) vaut 1,5119 pour K = 8, soit 6,9 % au-dessus de √2, et il faut K ≈ 51 pour descendre à 1 %. Avec les huit dimensions D1 à D8, la diagonale ne peut donc pas s'affirmer au-delà de 6,9 %, quel que soit le nombre de fiches. « Plus les révisions s'accumulent, plus la diagonale √2 s'affirme » demande que les dimensions se divisent au fil des révisions, pas seulement que les fiches s'accumulent.

Dimensions voisines, à confirmer à la révision : D1 la chèvre et les cordes (la fiche 016) ; D6 sphères, cubes, Venn et symétries (les périodes de Gauss).
