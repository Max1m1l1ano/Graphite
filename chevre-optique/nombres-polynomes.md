# Partie VII : les nombres des polynômes de la chèvre

> L'idée proposée : comparer les nombres des polynômes des dimensions impaires (3D, 5D, 7D) à ceux des dimensions paires 6, 12 et 24. Elle part d'une remarque : l'écriture des nombres (la base) rendrait visible le lien entre la transcendance de la dimension 2 et le polynôme entier de la dimension 3. Suite de la [partie VI](zone-confusion.md).

Tout est recalculé par [`scripts/polynomes.py`](scripts/polynomes.py) (≈ 5 s). Les tableaux complets sont dans [`resultats/polynomes.md`](resultats/polynomes.md).

## En bref

- **Une seule équation pour toutes les dimensions.** La parité ne change qu'une chose. En dimension impaire, tout est polynôme. En dimension paire, une racine carrée, celle du cercle, fait apparaître un arc : l'angle et π (§ 1).
- **Les dimensions impaires contiennent le rapport d'Archimède.** 3r⁴ − 8r³ + 8 = 0 s'écrit r⁴/4 = (2/3)(r³ − 1), où 2/3 est le rapport hémisphère/cylindre (§ 2).
- **Les dimensions paires 6, 12 et 24 ont une équation commune**, avec un angle et π/2. Leurs nombres clés sont κ₆ = 5/16, κ₁₂ = 231/1024 et κ₂₄ = 676039/4194304 (§ 3).
- **Paires et impaires sont réciproques** : κ₆ × h₇ = 5/16 × 16/35 = 1/7, et de même 12 ↔ 13 et 24 ↔ 25 (§ 4).
- **Ton intuition sur l'écriture a un fond exact : la base 2 compte des retenues** (théorème de Kummer, 1852).
  - Le nombre de facteurs 2 dans ces nombres est le nombre de retenues quand on additionne m + m en binaire.
  - 6, 12 et 24 donnent m = 3, 6, 12, qui s'écrivent 11, 110, 1100 : deux retenues chacun. D'où les dénominateurs 2⁴, 2¹⁰ et 2²² (§ 5).
- **Le terme constant de chaque polynôme impair est exactement le dénominateur de la dimension paire égale à son degré.**
  - 7D, de degré 12 : 1024, le dénominateur de κ₁₂ = 231/1024.
  - 13D, de degré 24 : 2²², le dénominateur de κ₂₄.
  - Vérifié de la dimension 3 à la dimension 31.
  - Le 6 est le degré du polynôme qui manque, celui de la dimension 4, qui est paire.
- **Le polynôme de degré 24 a pour groupe de Galois S₂₄**, le groupe le plus général possible. Ce n'est pas la symétrie exceptionnelle du 24 du réseau de Leech.

![Les facteurs 2 et les retenues](figures/g1_polynomes_retenues.png)

---

## 1. Une seule équation pour toutes les dimensions

Le pré a pour rayon 1, le piquet est sur le bord, et la corde vaut r = 2 cos α. Dans toutes les dimensions n, la condition « la chèvre broute la moitié » s'écrit :

```math
r^n\,\big[Q_n(1) - Q_n(r/2)\big] = Q_n\!\left(1 - \tfrac{r^2}{2}\right),
\qquad
Q_n(c) = \int_0^c (1-u^2)^{\frac{n-1}{2}}\,du .
```

$Q_n$ est l'intégrale des tranches d'une calotte. $Q_n(1)$ vaut le rapport hémisphère/cylindre $h_n$ de la partie IV, et $r^n$ est l'agrandissement du volume de la boule de rayon r.

**D'où vient la transcendance.** Tout se joue sur l'exposant (n − 1)/2.
- **Dimension impaire** : l'exposant est entier, (1 − u²)^m est un polynôme, et l'équation aussi.
- **Dimension paire** : l'exposant est un demi-entier, et la tranche contient √(1 − u²), la racine carrée du cercle. Son intégrale est un arc (arcsin). C'est ce qui fait entrer l'angle et π, avec le coefficient $\kappa_n = \binom{2m}{m}/4^m$ (la moyenne de sin²ᵐ).

Le lien entre la transcendance de la dimension 2 et le polynôme entier de la dimension 3 est donc précis : c'est la même équation, et seule la racine du cercle les distingue.

## 2. Les dimensions impaires : des polynômes entiers

| n | degré | polynôme | h_n | terme constant |
|---:|---:|---|---|---|
| 3 | 4 | 3r⁴ − 8r³ + 8 | 2/3 | 2³ |
| 5 | 8 | 5r⁸ − 80r⁶ + 128r⁵ − 128 | 8/15 | 2⁷ |
| 7 | 12 | 7r¹² − 112r¹⁰ + 840r⁸ − 1024r⁷ + 1024 | 16/35 | 2¹⁰ |
| 9 | 16 | 45r¹⁶ − 864r¹⁴ + 6720r¹² − 32256r¹⁰ + 32768r⁹ − 32768 | 128/315 | 2¹⁵ |
| 13 | 24 | 273r²⁴ − 7280r²² + … + 2²²r¹³ − 2²² | 1024/3003 | 2²² |

Leurs racines redonnent les cordes de la partie I à 15 chiffres près. Le degré vaut toujours 2(n − 1).

**La forme d'Archimède.** Chaque polynôme s'écrit h_n·(rⁿ − 1) = (polynôme en r²) :
- dimension 3 : (2/3)(r³ − 1) = r⁴/4 ;
- dimension 5 : (8/15)(r⁵ − 1) = r⁶/3 − r⁸/48 ;
- dimension 7 : (16/35)(r⁷ − 1) = 3r⁸/8 − r¹⁰/20 + r¹²/320.

Le 2/3 de la dimension 3 est le rapport hémisphère/cylindre d'Archimède. En multipliant (2/3)(r³ − 1) = r⁴/4 par 12, on obtient 8(r³ − 1) = 3r⁴ : le 8 vaut 12 × 2/3.

**Les groupes de Galois.** La partie I avait trouvé S₄, S₈, S₁₂ et S₁₆ pour les dimensions 3, 5, 7 et 9. Pour la dimension 13 (degré 24), le polynôme est irréductible.
- Modulo 19, il se factorise en degrés 1, 3, 3 et 17. Le groupe contient donc un cycle de longueur 17, et par le théorème de Jordan il contient A₂₄.
- Modulo 5, il reste irréductible, ce qui donne une permutation impaire.
- Le groupe de Galois est donc **S₂₄**.

## 3. Les dimensions paires 2, 6, 12 et 24

Avec α = arccos(r/2), l'équation de la § 1 devient, en dimension paire n = 2m :

```math
\kappa_n\left[\frac{\pi}{2} - (2 - r^n)\,\alpha\right] = \sqrt{4 - r^2}\;\Pi_n(r).
```

| n | κ_n | Π_n |
|---:|---|---|
| 2 | 1/2 | r/4 |
| 6 | 5/16 | 5r/32 + 5r³/192 + r⁵/192 + 13r⁷/128 − r⁹/128 |
| 12 | 231/1024 | polynôme de degré 21 |
| 24 | 676039/4194304 | polynôme de degré 45 |

- En dimension 2, on retrouve exactement l'équation d'Ullisch : (2 − r²)α + (r/2)√(4 − r²) = π/2.
- Pour 6, 12 et 24, le script vérifie que la corde de la partie I satisfait l'équation à 10⁻²⁸ près.
- Le premier terme de Π_n vaut toujours κ_n·r/2.

## 4. Les paires et les impaires sont réciproques

| paire ↔ impaire | κ de la paire | h de l'impaire | produit |
|---|---|---|---|
| 2 ↔ 3 | 1/2 | 2/3 | 1/3 |
| 4 ↔ 5 | 3/8 | 8/15 | 1/5 |
| **6 ↔ 7** | 5/16 | 16/35 | **1/7** |
| **12 ↔ 13** | 231/1024 | 1024/3003 | **1/13** |
| **24 ↔ 25** | 676039/4194304 | 4194304/16900975 | **1/25** |

La puissance de 2 qui est au dénominateur du côté pair (16, 1024, 4194304) passe au numérateur du côté impair. Le produit vaut toujours 1 divisé par la dimension impaire. C'est l'équation $h_{n-1}h_n = \frac{\pi}{2}c_n$ de la partie IV vue d'un autre côté, puisque $h_{2m} = \frac{\pi}{2}\kappa_{2m}$.

## 5. Les facteurs 2 comptent les retenues de la base 2

**Le théorème de Kummer (1852).** Le nombre de facteurs 2 dans $\binom{2m}{m}$ est égal au nombre de **retenues** quand on pose l'addition m + m en binaire, c'est-à-dire au nombre de chiffres 1 dans l'écriture binaire de m. Donc :

```math
\kappa_{2m} = \frac{\binom{2m}{m}}{4^m} \quad\text{a pour dénominateur}\quad 2^{\,2m - (\text{nombre de 1 de } m)} .
```

| n | m en binaire | retenues | dénominateur de κ_n |
|---:|---|---:|---|
| 6 | 11 | 2 | 2⁴ = 2^(6 − 2) |
| 12 | 110 | 2 | 2¹⁰ = 2^(12 − 2) |
| 24 | 1100 | 2 | 2²² = 2^(24 − 2) |
| 8 | 100 | 1 | 2⁷ |
| 14 | 111 | 3 | 2¹¹ |
| 30 | 1111 | 4 | 2²⁶ |

**Pourquoi 6, 12 et 24 se ressemblent.** Doubler n revient à ajouter un 0 à droite de m en binaire (11 → 110 → 1100). Le nombre de 1 ne change pas, donc les retenues restent 2, et le dénominateur reste 2^(n − 2). Ta suite 6, 12, 24 est exactement une suite de même signature binaire.

**Les polynômes impairs portent la signature de leur degré.** Le polynôme de la dimension impaire n a pour degré 2(n − 1). Son terme constant est ±2^e, sans aucun facteur impair, avec e = 2(n − 1) − (nombre de 1 de (n − 1)/2). C'est exactement le dénominateur de κ dans la dimension paire 2(n − 1) :

| dimension impaire | degré | terme constant | dénominateur de κ au degré |
|---:|---:|---|---|
| 3 | 4 | 8 | κ₄ = 3/8 |
| 5 | 8 | 128 | κ₈ = 35/128 |
| **7** | **12** | **1024** | **κ₁₂ = 231/1024** |
| 9 | 16 | 32768 | κ₁₆ = 6435/32768 |
| **13** | **24** | **2²²** | **κ₂₄ = 676039/2²²** |

Le script le vérifie pour toutes les dimensions impaires de 3 à 31. L'exposant s'explique par Kummer, à travers $h_n$. En revanche, je n'ai pas de preuve écrite que le terme constant ne garde aucun facteur impair : c'est vérifié sur ces 15 cas, pas démontré.

**Et 6 ?** Ce serait le degré du polynôme de la dimension 4, qui n'existe pas, puisque la dimension 4 est paire et donc transcendante. Dans ta suite, 12 et 24 sont les degrés des polynômes des dimensions 7 et 13, et 6 est la place vide entre les deux familles.

## 6. Ce que ça dit de « l'apparence »

**Tu avais raison sur un point précis.** Écrire en base 2 ne change pas la racine, mais rend visible une structure vraie. En binaire, le polynôme de la dimension 7 s'écrit :

> 111·r¹¹⁰⁰ − 1110000·r¹⁰¹⁰ + 1101001000·r¹⁰⁰⁰ − 10000000000·r¹¹¹ + 10000000000

Les puissances de 2 y apparaissent comme des zéros à droite, et leur nombre compte des retenues. C'est une propriété arithmétique réelle, avec un mécanisme démontré (Kummer).

**La limite est tout aussi précise.**
- **Ce qui ne bouge pas** : la valeur de la corde, 1,3247 R en dimension 7, est la même dans toutes les bases.
- **Ce que voit une base** : chaque base première compte ses propres retenues. La base 3 compte les facteurs 3 (par exemple deux retenues pour m + m quand m = 5, et deux facteurs 3 dans C(10, 5)), et ainsi de suite pour 5 et 7.
- **Et la base 10** : 10 = 2 × 5 n'est pas premier, donc ses retenues ne comptent rien de plus que celles des bases 2 et 5.

Les bases qui parlent à la chèvre sont les bases premières jusqu'à la dimension : 2, 3, 5, 7, puis 11 et 13 en dimension 13. Ce sont exactement les nombres premiers qui apparaissent dans ses coefficients (partie VI).

**Sur le 24.** Le 24 de la chèvre est le degré d'un polynôme sans symétrie particulière (groupe S₂₄). Le 24 exceptionnel des empilements de sphères, celui du réseau de Leech (partie III), a une symétrie très spéciale, liée au groupe de Mathieu M₂₄. Les deux 24 ne se rejoignent pas ici.

## 7. Le tri

- **Démontré** :
  - l'équation unique et le rôle de la racine du cercle ;
  - la réciprocité κ₂ₘ·h₂ₘ₊₁ = 1/(2m + 1) ;
  - les dénominateurs des κ par le théorème de Kummer ;
  - le groupe S₂₄ de la dimension 13 (factorisations calculées et théorème de Jordan).
- **Vérifié par le calcul, pas démontré en général** : le terme constant du polynôme impair égal au dénominateur de κ au degré (dimensions 3 à 31).
- **À nuancer** : le 24 de la chèvre n'est pas celui de Leech. Et la base 2 révèle une structure arithmétique des coefficients, pas la valeur de la corde.

## Sources

- E. E. Kummer, « Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen », *Journal für die reine und angewandte Mathematik* 44, 93–146 (1852) : le théorème des retenues.
- C. Jordan, « Sur la limite de transitivité des groupes non alternés », *Bulletin de la SMF* 1, 40–71 (1873) : un groupe primitif contenant un cycle de longueur première (assez petite) contient le groupe alterné.
- J. H. Conway et N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, Springer (1988) : le réseau de Leech et le groupe de Mathieu M₂₄.
- Parties I (polynômes et groupes de Galois des dimensions 3 à 9) et IV (rapports h_n et c_n).
