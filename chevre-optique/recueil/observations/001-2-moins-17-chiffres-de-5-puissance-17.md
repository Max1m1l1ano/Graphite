# 001 — 2⁻¹⁷ s'écrit avec les chiffres de 5¹⁷

| champ | valeur |
|---|---|
| type | Fait amusant |
| statut | exact |
| partie | XXIX |
| document | [venn-ppm.md](../../venn-ppm.md), § 2.1 |
| script | [`scripts/venn_ppm.py`](../../scripts/venn_ppm.py), section 2 (les comptes au ppm) |
| données | [`resultats/venn_ppm.md`](../../resultats/venn_ppm.md) |
| image | — |
| dimension | D2 bases, chiffres et congruences ; puis, à la révision 001 : D3 grain, pixels et précision, D6 sphères, cubes, Venn et symétries |
| test | précision poussée : identité 2⁻ʲ = 5ʲ·10⁻ʲ, vraie pour tout j |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

L'auteur demande une analyse « par ppm » du Venn à 17 courbes. Dans un Venn simple à 17 courbes, une région moyenne pèse 2⁻¹⁷ de l'image : c'est le grain naturel du dessin.

## L'observation

2⁻¹⁷ = 0,00000762939453125, et 5¹⁷ = 762 939 453 125 : les mêmes chiffres. Une région moyenne pèse donc 7,62939453125 ppm, soit « 5¹⁷ » en millionièmes décalés.

## Ce que le script produit

Le script calcule 2⁻¹⁷ en décimal exact (module Decimal) et l'écrit à côté de 5¹⁷.

## Liens et pistes

Partie XXVI : 10⁶/2²⁰ a les chiffres de 5²⁰, et « 1 To » = 931 Go fait apparaître 5³⁰. C'est l'inversion 2 ↔ 5 de part et d'autre de la virgule (fiche 015 et `resultats/recueil_verifications.md`, § 7).

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Dossier [grain](../dossiers/grain-pixels-centres.md) : garder, partagée avec bases : lien exact, fort par l'unité, faible par le calcul.
- Dossier [bases](../dossiers/bases-congruences-premiers.md) : exact : identité 2⁻ʲ = 5ʲ·10⁻ʲ pour tout j ; statut inchangé ; rien à répliquer (17 n'a pas de rôle dans l'identité).
- Dossier [méthode](../dossiers/hasard-et-methode.md) : bon test ; le verdict tient.
