# Partie XXIV : un tiers de dimension

Résultats calculés par `scripts/tiers_dimension.py`.

## 1. La démonstration du terme 2/(3n²)

**L'écriture exacte.** X = ρU, U uniforme sur la sphère, ρⁿ uniforme sur [0, 1]. Donc E = −n ln ρ suit *exactement* la loi exponentielle : P(E > t) = P(ρⁿ < e^(−t)) = e^(−t). (La partie I utilisait n(1 − ρ), seulement asymptotiquement exponentielle.)
La condition |X − P|² ≤ m s'écrit U₁ ≥ τ(ρ) = (ρ² + 1 − m)/(2ρ), et sur la coquille extérieure (ρ = 1), τ = 1 − m/2 = x₀ : τ est le plan de la lentille vu depuis chaque coquille.

**Ordre 1 : le simplexe.** E[τ] = ½(E[ρ] + (1 − m)E[ρ⁻¹]) = 0 donne exactement m = 2n/(n + 1), l'arête² du simplexe (partie VI).
Autrement dit, k² − d² = E[ρ]/E[ρ⁻¹] = (n − 1)/(n + 1) : la projection g² de la partie XVI, par un troisième calcul (après Archimède et Parseval).

**Ordre 2.** E[τ] = (k/3)·E[τ³], avec k = (n − 3)/2 ≈ n/2 (courbure de l'équateur) et E[τ³] ≈ E[(1 − E)³]/n³ = −2/n³ (asymétrie de la coquille). Comme E[τ] = −(μ/2)·n/(n − 1) :
μ/2 ≈ (n/6)·(2/n³), donc μ ≈ 2/(3n²). Le calcul exact (§ 2) donne bien μ = 2/(3n²) − 98/(15n³) + ….

**Le reste et l'inversion (borne explicite).**
- Série de l'équateur : ∫₀^τ (1 − u²)^k du = τ − kτ³/3 + R, |R| ≤ C(k, 2)|τ|⁵/5 (Lagrange, k ≥ 2).
- Pour ρ ≥ ρ₀ = √m − 1 ≥ 0,4 : |τ| ≤ (E + a)/(nρ₀), avec m = 2 − 2a/n, a ≤ 1,1. Donc |R| ≤ (n²/8)(1/5)(2,5/n)⁵·E[(E + 1,1)⁵] = 879,3/n³ (E[(E + 1,1)⁵] = 360,15).
- Zone centrale ρ < ρ₀ (toujours broutée) : poids ρ₀ⁿ ≈ (√2 − 1)ⁿ, borné ici par 1/n⁴.
- Inversion : la fraction broutée croît avec m. On vérifie exactement (polynômes en t = n − 100 à coefficients positifs) que la condition change de signe entre m± = 2n/(n + 1) + 2/(3n²) ± 1800/n³. **Résultat : |r_n² − 2n/(n + 1) − 2/(3n²)| < 1800/n³ pour tout n ≥ 100.** Vérification : faite.
- La constante est grossière : la vraie limite de n³·|μ − 2/(3n²)| est 98/15 = 6,53. Pour n < 100, la borne reste vraie sur les cordes calculées, avec une marge d'au moins 299.

| n | zone centrale (√m − 1)ⁿ | (1/√2)ⁿ |
|---:|---|---|
| 10 | 2,83·10⁻⁵ | 3,12·10⁻² |
| 24 | 1,20·10⁻¹⁰ | 2,44·10⁻⁴ |
| 100 | 9,61·10⁻⁴⁰ | 8,88·10⁻¹⁶ |
| 1000 | 3,04·10⁻³⁸⁴ | 3,05·10⁻¹⁵¹ |

## 2. Tous les termes

Coefficients exacts (fractions, 14 termes) et 30 termes à 170 chiffres, calculés en 12,7 s.

| j | μ_j dans μ = Σ μ_j/n^j | valeur | μ_(j+1)/μ_j |
|---:|---|---|---|
| 2 | 2/3 | 0,666667 | −9,800 |
| 3 | −98/15 | −6,53333 | −8,697 |
| 4 | 5966/105 | 56,819 | −10,542 |
| 5 | −1698106/2835 | −598,979 | −13,233 |
| 6 | 247172734/31185 | 7926,01 | −16,103 |
| 7 | −258717260798/2027025 | −1,27634·10⁵ | −18,979 |
| 8 | 220958094270374/91216125 | 2,42236·10⁶ | −21,844 |
| 9 | −114870855285496738/2170943775 | −5,29129·10⁷ | −24,704 |
| 10 | 269584442064157889822/206239658625 | 1,30714·10⁹ | −27,564 |
| 11 | −1404443800817031224162086/38979295480125 | −3,60305·10¹⁰ | −30,428 |
| 12 | 4914437055598353937139770898/4482618980214375 | 1,09633·10¹² | −33,295 |

En puissances de 1/n :

- r² = 2 − 2/n + 8/(3n²) − 128/(15n³) + 6176/(105n⁴) − 1703776/(2835n⁵) + 247235104/(31185n⁶) + …
- x₀ = 1 − r²/2 = 1/n − 4/(3n²) + 64/(15n³) − 3088/(105n⁴) + 851888/(2835n⁵) − 123617552/(31185n⁶) + …
- n(2 − r²) = 2 − 8/(3n) + 128/(15n²) − 6176/(105n³) + 1703776/(2835n⁴) − 247235104/(31185n⁵) + … (partie XXII : 2 − 8/(3n))

- 1/x₀ = n + 4/3 − 112/(45n) + 3856/(189n²) − 150832/(675n³) + … : **le ménisque vaut un tiers de dimension** (§ 3).

**Contrôles.** Cordes certifiées de la partie XX retrouvées à 48 chiffres (n = 4, 8, 24). Cordes à 60 chiffres par l'équation de la chèvre (partie I § 5.1, Newton), écart à la série tronquée à l'ordre J :

| n | r_n² (40 chiffres) | J = 2 | J = 4 | J = 8 | J = 12 |
|---:|---|---|---|---|---|
| 24 | 1,920806330585009698788278620635702986165 | 4,90·10⁻⁴ | 5,00·10⁻⁵ | 1,02·10⁻⁵ | 1,71·10⁻⁵ |
| 100 | 1,980258668277162760343219319608913062907 | 8,00·10⁻⁶ | 5,32·10⁻⁸ | 4,26·10⁻¹¹ | 2,70·10⁻¹³ |
| 1000 | 1,998002658191559204512007547520640953466 | 8,48·10⁻⁹ | 5,93·10⁻¹³ | 5,16·10⁻²⁰ | 3,52·10⁻²⁶ |
| 10000 | 1,999800026658139209236218625139484217211 | 8,53·10⁻¹² | 6,00·10⁻¹⁸ | 5,28·10⁻²⁹ | 3,64·10⁻³⁹ |

Chaque ordre gagne un facteur ≈ n : les coefficients sont justes (à 10⁻⁵⁰ près en dimension 10 000 avec 20 termes).

**La série diverge.** μ_(j+1)/μ_j ≈ −A·j, et l'écart entre deux rapports successifs tend vers A = 1/ln √2 = 2/ln 2 = 2,88539 :

| j | 5 | 10 | 15 | 20 | 25 | 28 |
|---|---|---|---|---|---|---|
| écart des rapports | 2,6907 | 2,8607 | 2,8756 | 2,8816 | 2,8834 | 2,8839 |

Lecture (argument de col, pas une preuve) : le bord de la calotte de la corde est à α → 45°, et le développement de W_n(α) = ∫₀^α sinⁿ « sent » le sommet du sinus à 90°, à la distance ln(sin 90°/sin 45°) = ln √2.

**Troncature optimale.** On s'arrête au plus petit terme, vers j* ≈ n·ln √2. L'erreur vaut alors ≈ 2^(−n/2)/n :

| n | j* | n·ln √2 | erreur optimale | 2^(−n/2)/n | rapport |
|---:|---:|---:|---|---|---|
| 10 | 4 | 3,5 | 2,77·10⁻³ | 3,12·10⁻³ | 0,89 |
| 16 | 6 | 5,5 | 2,27·10⁻⁴ | 2,44·10⁻⁴ | 0,93 |
| 24 | 9 | 8,3 | 9,87·10⁻⁶ | 1,02·10⁻⁵ | 0,97 |
| 32 | 12 | 11,1 | 4,75·10⁻⁷ | 4,77·10⁻⁷ | 1,00 |
| 50 | 18 | 17,3 | 5,99·10⁻¹⁰ | 5,96·10⁻¹⁰ | 1,01 |
| 70 | 25 | 24,3 | 4,21·10⁻¹³ | 4,16·10⁻¹³ | 1,01 |

Soit −log₁₀(2^(−n/2)/n) = 0,1505·n + log₁₀ n chiffres au mieux : 5,0 en 24D, 17,1 en 100D, 1,5·10⁴⁹ en dimension 10⁵⁰.

**Les décimales en blocs.** En dimension 10ᵏ, chaque terme de la série occupe un bloc de k chiffres.

En dimension 10⁴ (60 chiffres exacts, blocs de 4) :

```
r² = 1,9998 0002 6658 1392 0923 6218 6251 3948 4217 2108 2519
```

En dimension 10⁵⁰ (série à 14 termes, reste < 10⁻⁷⁰⁰ ; blocs de 50 chiffres) :

```
r² = 1,
     99999999999999999999999999999999999999999999999998
     00000000000000000000000000000000000000000000000002
     66666666666666666666666666666666666666666666666658
     13333333333333333333333333333333333333333333333392
     15238095238095238095238095238095238095238095237494
     25890652557319223985890652557319223985890652565247
```

Bloc 1 : 2 − 2/n. Bloc 2 : le 2 de 8/3 = 2 + 2/3 (le 2/n² du simplexe 2n/(n + 1)). Bloc 3 : le 2/3 du ménisque (0,666…), moins le 8 de 128/15 = 8,53… (66 − 8 = 58). Bloc 4 : 0,1333… = 2/15, plus le 58 de 6176/105 = 58,8… Chaque bloc porte la partie décimale d'un coefficient ; les retenues les recousent (parties XIX et XXIII).

## 3. Un tiers de dimension

On cherche le simplexe qui a la même corde : 2N/(N + 1) = r_n², soit N = r²/(2 − r²) = 1/x₀ − 1.

| n | 1 | 2 | 3 | 4 | 5 | 8 | 10 | 24 | 100 | 10³ | 10⁴ | 10⁵ | 10⁶ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N − n | 0,0000 | 0,0425 | 0,0760 | 0,1024 | 0,1236 | 0,1683 | 0,1886 | 0,2545 | 0,3103 | 0,3309 | 0,3331 | 0,3333 | 0,3333 |

- N − n croît de 0 (dimension 1) vers 1/3 (vérifié pour n = 2 … 60 et aux décades), avec N − n = 1/3 − 112/(45n) + ….
- Donc r_n² = 2N/(N + 1) avec N = n + 1/3 − …, et le plan de la lentille est en x₀ = 1/(N + 1) = 1/(n + 4/3 − …).

## 4. Le piquet n'importe où

Même démonstration avec τ = (ρ² − c)/(2dρ), c = k² − d², D = 1/d² :

k² = d² + (n − 1)/(n + 1) + μ(n, d), avec

- ordre 1/n² : 2D/3
- ordre 1/n³ : −14D(2D + 5)/15
- ordre 1/n⁴ : 2D(491D² + 1442D + 1050)/105

- C'est la loi k² ≈ δ² + (n − 1)/(n + 1) de la partie I (§ 5.4), désormais démontrée, avec sa correction 2/(3n²d²). Le paramètre est 1/(nd²) : valable tant que d ≫ 1/√n, comme annoncé.
- La partie en D (piquet lointain) redonne exactement le c_n/ρ² de la partie XVI (§ 6) : c_n = 2n(n − 1)/(3(n + 1)³(n + 3)), retrouvé ici par les moments, et n²c_n → 2/3.
- Les deux « à faire relire » (partie I § 5.4, partie XVI § 6) sont le même terme : le τ³ de l'équateur.

| n | d | μ calculé | μ prédit (ordres 2 à 4) |
|---:|---:|---|---|
| 100 | 0,5 | 2,2674·10⁻⁴ | 2,2931·10⁻⁴ |
| 100 | 1,0 | 6,0648·10⁻⁵ | 6,0702·10⁻⁵ |
| 100 | 3,0 | 6,8905·10⁻⁶ | 6,8916·10⁻⁶ |
| 1000 | 0,2 | 1,5523·10⁻⁵ | 1,5547·10⁻⁵ |
| 1000 | 1,0 | 6,6019·10⁻⁷ | 6,6019·10⁻⁷ |

**μ ≈ 2δ (parties VI et XVI).** On garde la corde du simplexe et on rapproche le piquet du centre de δ :

| n | δ | μ | 2δ/μ | 1 + 5μ/4 |
|---:|---|---|---|---|
| 2 | 0,0047121107 | 9,3183·10⁻³ | 1,011363 | 1,011648 |
| 3 | 0,0047121571 | 9,3225·10⁻³ | 1,010923 | 1,011653 |
| 5 | 0,0033904650 | 6,7291·10⁻³ | 1,007701 | 1,008411 |
| 10 | 0,0015374287 | 3,0641·10⁻³ | 1,003515 | 1,003830 |
| 20 | 0,0005451246 | 1,0889·10⁻³ | 1,001276 | 1,001361 |
| 50 | 0,0001110107 | 2,2196·10⁻⁴ | 1,000268 | 1,000277 |
| 100 | 0,0000303265 | 6,0648·10⁻⁵ | 1,000074 | 1,000076 |

2δ − δ² = μ(n, 1 − δ) ≈ μ(1 + 2δ) donne 2δ/μ ≈ 1 + 5μ/4, juste quand n grandit.

## 5. Le facteur 2 entre le plan et l'aire

**Euclide (Éléments VI.8) et Thalès (III.31).** Le triangle P Q P′ (P′ l'antipode du piquet, Q sur le bord de la lentille) est rectangle en Q. Le côté PQ = r est moyen proportionnel entre le diamètre PP′ = 2R et sa projection PH = R − x₀ : **r² = 2R·(R − x₀)**, exactement, en toute dimension.
- Donc 2R² − r² = 2R·x₀ : le défaut d'aire est l'aire de la bande de largeur x₀ et de hauteur 2R (le diamètre).
- Le facteur 2 est le diamètre mesuré en rayons. En dimension infinie, x₀ = 0 et Q est le coin du demi-carré (partie I, § 5.3).
- En unités : x₀ = (2R² − r²)/(2R²) (défaut relatif au disque limite, rayon √2, le cercle des coins) et 2 − r² = (2R² − r²)/R² (relatif au pré, le cercle des côtés). Les deux unités sont à un cran (partie I, § 6.4).

**Les lectures du grain.** (n + 4/3)·défaut tend vers une constante pour chaque lecture :

| lecture | n = 100 | n = 10³ | n = 10⁴ | limite | n au grain 10⁻⁵⁰ |
|---|---|---|---|---|---|
| corde relative (√2 − r)/√2 | 0,50135 | 0,50013 | 0,50001 | 0,50000 | ≈ 0,5·10⁵⁰ |
| corde √2 − r | 0,70902 | 0,70729 | 0,70712 | 0,70711 | ≈ 0,707·10⁵⁰ |
| plan x₀ | 1,00023 | 1,00000 | 1,00000 | 1,00000 | ≈ 1·10⁵⁰ |
| cran log₂(2/r²) | 1,45019 | 1,44342 | 1,44277 | 1,44270 | ≈ 1,44·10⁵⁰ |
| aire 2 − r² (unité : le pré) | 2,00045 | 2,00000 | 2,00000 | 2,00000 | ≈ 2·10⁵⁰ |
| aire en unité du disque central (½) | 4,00091 | 4,00001 | 4,00000 | 4,00000 | ≈ 4·10⁵⁰ |

- Le plan et l'aire : n = 10⁵⁰ − 4/3 et n = 2·10⁵⁰ − 4/3 (à 10⁻⁵⁰ près). Le facteur 2 multiplie, le 4/3 décale : 1 pour le simplexe (centre de gravité), 1/3 pour le ménisque, le même dans les deux lectures.
- Un facteur 2, c'est exactement 1 cran (base 2), 0,30103 décade (base 10) et 3,0103 dB.

## 6. Les liens avec les autres parties

| partie | ce qu'on avait | ce que la partie XXIV ajoute |
|---|---|---|
| I § 5.4 | esquisse de 2/(3n²) | démonstration complète, borne 1 800/n³, tous les ordres |
| I § 4.3 et § 5.4 | k² ≈ δ² + (n − 1)/(n + 1) | démontrée, + 2/(3n²δ²), validité δ ≫ 1/√n |
| I § 5.2–5.3 | coquille et équateur | 2/3 = 2 (double produit 2ρU₁) × 1/6 (équateur) × 2 (coquille) |
| I § 5.5 | paires transcendantes, impaires algébriques | même série rationnelle ; écart sous (1/√2)ⁿ |
| I § 6.4, XXI | un cran, le doublement de l'aire | le facteur 2 entre plan et aire |
| IV, VII, XX | Wallis, W_n, cordes certifiées | c_n se simplifie ; contrôles à 48 chiffres |
| VI | simplexe, n²(r² − a²) = 0,037 … 0,65 | E[τ] = 0 : la chèvre linéarisée ; 2/3 démontré |
| VI § 3 bis | dimensions non entières | la chèvre de dimension n = le simplexe de dimension n + 1/3 |
| XVI | g² deux fois ; c_n/ρ² ; μ ≈ 2δ | g² = E[ρ]/E[ρ⁻¹] ; c_n retrouvé ; 2δ/μ ≈ 1 + 5μ/4 |
| XVII, XVIII | √2 − 1, tan 22,5° | zone centrale (√2 − 1)ⁿ |
| XVIII, XXII, XXIII | un chiffre par décade, 2 − 8/(3n), deux couches | les blocs de k chiffres en 10ᵏ |

