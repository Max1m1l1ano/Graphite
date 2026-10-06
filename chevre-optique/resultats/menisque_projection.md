# Résultats de la partie XVI (générés par scripts/menisque_projection.py)

## 1. En dimension infinie : ρ² = d² + 1, et la diagonale 1x, 1y

Valeurs de ρ_n(d)² − d² (la corde de la moitié, piquet à la distance d) : elles montent vers 1 quand n grandit.

| n | d = 0 | d = 0,5 | d = 1 | d = 2 | d = 5 |
|---:|---|---|---|---|---|
| 2 | 0,500000 | 0,366047 | 0,342652 | 0,335764 | 0,333727 |
| 3 | 0,629961 | 0,529451 | 0,509322 | 0,502527 | 0,500415 |
| 5 | 0,757858 | 0,687045 | 0,673396 | 0,668524 | 0,666973 |
| 10 | 0,870551 | 0,827664 | 0,821246 | 0,819020 | 0,818320 |
| 30 | 0,954842 | 0,937366 | 0,936035 | 0,935629 | 0,935507 |
| 100 | 0,986233 | 0,980425 | 0,980259 | 0,980213 | 0,980201 |
| 300 | 0,995390 | 0,993383 | 0,993363 | 0,993357 | 0,993356 |
| ∞ | 1 | 1 | 1 | 1 | 1 |

Pourquoi : pour un point X tiré au hasard dans le pré, E|OX|² = n/(n+2) → 1 et E(OX·u)² = 1/(n+2) → 0 dans toute direction u. En grande dimension, presque tout le pré est à la distance 1 de O et perpendiculaire à OP. La distance PX est alors l'hypoténuse d'un triangle rectangle de côtés d (le piquet) et 1 (le point) : ρ² = d² + 1, et pour d = 1, la diagonale 1x, 1y.

| n | E|OX|² = n/(n+2) | E(OX·u)² = 1/(n+2) | E|PX|² (d = 1) | médiane r_n² |
|---:|---|---|---|---|
| 2 | 0,5000 | 0,2500 | 1,5000 | 1,3427 |
| 3 | 0,6000 | 0,2000 | 1,6000 | 1,5093 |
| 10 | 0,8333 | 0,0833 | 1,8333 | 1,8212 |
| 100 | 0,9804 | 0,0098 | 1,9804 | 1,9803 |
| ∞ | 1 | 0 | 2 | 2 |

La grille décalée A_n (grille cubique de dimension n+1 coupée par x₀ + … + x_n = 0) : ses arêtes e_i − e_j sont toutes des diagonales 1x, 1y, de longueur √2, dans toutes les dimensions. Seule la hauteur du simplexe dépend de n.

| n | arête e_i − e_j | hauteur du simplexe √((n+1)/n) | arête ÷ hauteur = s_n | s_n² = 1 + g_n² |
|---:|---|---|---|---|
| 2 | 1,414214 | 1,224745 | 1,154701 | 1 + 0,333333 |
| 3 | 1,414214 | 1,154701 | 1,224745 | 1 + 0,500000 |
| 4 | 1,414214 | 1,118034 | 1,264911 | 1 + 0,600000 |
| 10 | 1,414214 | 1,048809 | 1,348400 | 1 + 0,818182 |
| 100 | 1,414214 | 1,004988 | 1,407195 | 1 + 0,980198 |
| ∞ | √2 | 1 | √2 | 1 + 1 |

## 2. Entre 2 et l'infini : r² = 1 + g² + μ

1 = le piquet (d² avec d = 1) ; g² = (n−1)/(n+1) = la projection (rayon² de la base du simplexe, rayon quadratique de l'ombre du pré) ; μ = r² − s² = le ménisque.

| n | r_n² | 1 + g_n² = s_n² | μ_n = r² − s² | μ / (1 − g²) | (r − s)/s |
|---:|---|---|---|---|---|
| 1 | 1,000000 | 1,000000 | 0,0000000 | 0,00000 | 0,000 % |
| 1,5 | 1,207107 | 1,200000 | 0,0071069 | 0,00888 | 0,296 % |
| 2 | 1,342652 | 1,333333 | 0,0093183 | 0,01398 | 0,349 % |
| 2,4236 | 1,425506 | 1,415820 | 0,0096864 | 0,01658 | 0,341 % |
| 3 | 1,509322 | 1,500000 | 0,0093225 | 0,01864 | 0,310 % |
| 4 | 1,608025 | 1,600000 | 0,0080250 | 0,02006 | 0,250 % |
| 5 | 1,673396 | 1,666667 | 0,0067291 | 0,02019 | 0,202 % |
| 10 | 1,821246 | 1,818182 | 0,0030641 | 0,01685 | 0,084 % |
| 20 | 1,905851 | 1,904762 | 0,0010889 | 0,01143 | 0,029 % |
| 50 | 1,961006 | 1,960784 | 0,0002220 | 0,00566 | 0,006 % |
| 100 | 1,980259 | 1,980198 | 0,0000606 | 0,00306 | 0,002 % |
| 300 | 1,993363 | 1,993355 | 0,0000072 | 0,00108 | 0,000 % |
| ∞ | 2 | 2 | 0 | 0 | 0 % |

Le ménisque culmine entre 2 et 3, de quelque façon qu'on le mesure :

| mesure | maximum en n = | valeur |
|---|---|---|
| (r − s)/s | 2,0832 | 0,0034950 |
| r − s | 2,2438 | 0,0040868 |
| μ = r² − s² | 2,4236 | 0,0096864 |
| c_n (§ 6) | 2,5917 | 0,0106148 |

c_n est maximal à la racine de 2n³ − n² − 12n + 3 = 0 : n = 2,591738.

**Pourquoi la base du simplexe et l'ombre du pré ont le même rayon quadratique.** Deux égalités, toutes deux dans R^{n+1} (l'espace de la grille A_n) :
- Archimède : un point uniforme sur la sphère S^n de R^{n+1}, projeté sur n − 1 axes, est uniforme dans la boule B^{n−1} (la section du pré). Donc E|y|² = (n−1)/(n+1).
- Parseval : les n + 1 sommets e_i du simplexe forment un repère orthonormé ; leurs carrés projetés sur un sous-espace W de dimension n − 1 font en moyenne dim W/(n+1). Le sommet e₀ se projette en O, les n autres sur la sphère de rayon R_b : (n/(n+1)) R_b² = (n−1)/(n+1), soit R_b²/h² = (n−1)/(n+1) avec h² = (n+1)/n.

| n | Monte-Carlo : E|y|² (S^n projetée) | E|y|⁴ | P(|y| < 1/2) | attendu (n−1)/(n+1) ; (n−1)/(n+3) ; 2^(1−n) | (1/(n+1)) Σ |P_W e_i|² | R_b²/h² |
|---:|---|---|---|---|---|---|
| 2 | 0,3330 | 0,2002 | 0,5012 | 0,3333 ; 0,2000 ; 0,5000 | 0,333333 | 0,333333 |
| 3 | 0,5003 | 0,3335 | 0,2491 | 0,5000 ; 0,3333 ; 0,2500 | 0,500000 | 0,500000 |
| 5 | 0,6667 | 0,5001 | 0,0622 | 0,6667 ; 0,5000 ; 0,0625 | 0,666667 | 0,666667 |

**Ménisque et translation : μ ≈ 2δ.** δ_n est la translation (partie VI) qui amène le cercle du simplexe à la moitié exacte. Comme ρ² − d² est la bonne coordonnée, reculer le piquet de δ ajoute 2δ à ρ² − d² au premier ordre.

| n | δ_n | 2δ_n | μ_n | 2δ/μ |
|---:|---|---|---|---|
| 2 | 0,0047121 | 0,0094242 | 0,0093183 | 1,0114 |
| 2,4236 | 0,0048992 | 0,0097984 | 0,0096864 | 1,0116 |
| 3 | 0,0047122 | 0,0094243 | 0,0093225 | 1,0109 |
| 5 | 0,0033905 | 0,0067809 | 0,0067291 | 1,0077 |
| 10 | 0,0015374 | 0,0030749 | 0,0030641 | 1,0035 |
| 30 | 0,0002759 | 0,0005518 | 0,0005515 | 1,0007 |

## 3. La chèvre s'annule loin du bord : le plateau

Tant que le disque de la corde est entièrement dans le pré, la moitié s'obtient avec ρ₀ = 2^(−1/n), où que soit le piquet. Le plateau s'arrête au contact intérieur, en d₀ = 1 − 2^(−1/n). Ensuite, la chèvre se réveille doucement : ρ − ρ₀ croît comme (d − d₀)^((n+1)/2).

Le ménisque généralisé G_n(d) = ρ_n(d) − max(ρ₀, √(d² + g²)) mesure ce que ni le disque inscrit (le plateau), ni la projection (l'hyperbole) n'expliquent. Il est nul sur le plateau, vaut r − s en d = 1, culmine exactement là où les deux lois donnent la même corde (d_b = √(ρ₀² − g²)) et s'éteint au loin comme c_n/(2ρ³).

| n | ρ₀ = 2^(−1/n) | d₀ (contact) | exposant mesuré | (n+1)/2 | d_b | G max | G(1) = r − s |
|---:|---|---|---|---|---|---|---|
| 2 | 0,707107 | 0,292893 | 1,509 | 1,5 | 0,4082 | 0,03185 | 0,004028 |
| 3 | 0,793701 | 0,206299 | 1,999 | 2 | 0,3605 | 0,02875 | 0,003800 |
| 5 | 0,870551 | 0,129449 | 2,993 | 3 | 0,3020 | 0,02167 | 0,002604 |
| 10 | 0,933033 | 0,066967 | — | 5,5 | 0,2288 | 0,01289 | 0,001136 |
| 30 | 0,977160 | 0,022840 | — | 15,5 | 0,1391 | 0,00485 | 0,000198 |
| ∞ | 1 | 0 | — | — | 0 | 0 | 0 |

Vérifications sur 400 positions de d ∈ ]0 ; 100] : la courbe de la chèvre reste au-dessus de son hyperbole (ρ² − d² > g²) et ρ² − d² décroît : n = 2 : oui, n = 3 : oui, n = 5 : oui, n = 10 : oui. Pour chaque d, ρ_n(d) croît avec n.

## 4. Les contacts à 45°

Pas de calcul ici : dans le plan (d, ρ), deux cercles centrés sur la même droite se touchent de l'intérieur quand |Δd| = |Δρ|, de l'extérieur quand |Δd| = ρ₁ + ρ₂. Avec le pré (0 ; 1) : ρ = 1 − d (corde dans le pré), ρ = 1 + d (pré dans la corde), ρ = d − 1 (contact extérieur).

## 5. Les trois déplacements par le point du simplexe (d = 1, ρ = s_n)

- Translation : la corde reste s_n, le piquet glisse (ligne horizontale du plan (d, ρ)).
- Hyperbole : ρ² − d² reste g_n² (la projection est fixe ; tous les cercles passent par la base du simplexe).
- Triangle : ρ/d reste s_n (le triangle rectangle O-P-B garde sa forme et grandit depuis O).

Contacts avec le pré : « intérieur » quand la corde est dans le pré ou le pré dans la corde, « extérieur » quand les deux disques se touchent de l'extérieur. Contacts avec le cercle de la chèvre (centre P, rayon r_n) : le ménisque de la partie VI qui devient tangence puis croisement.

| n | translation : pré dans la corde jusqu'à | tangence avec la chèvre (VI) | moitié | contact extérieur | hyperbole : corde dans le pré jusqu'à | rayon (cercle circonscrit) | triangle : corde dans le pré jusqu'à | moitié | pré dans la corde dès |
|---:|---|---|---|---|---|---|---|---|---|
| 2 | 0,1547 | 0,99597 | 0,99529 | 2,1547 | 0,3333 | 0,6667 | 0,4641 | 1,01353 | 6,4641 |
| 3 | 0,2247 | 0,99620 | 0,99529 | 2,2247 | 0,2500 | 0,7500 | 0,4495 | 1,00913 | 4,4495 |
| 5 | 0,2910 | 0,99740 | 0,99661 | 2,2910 | 0,1667 | 0,8333 | 0,4365 | 1,00499 | 3,4365 |
| 10 | 0,3484 | 0,99886 | 0,99846 | 2,3484 | 0,0909 | 0,9091 | 0,4258 | 1,00186 | 2,8703 |
| ∞ | √2 − 1 = 0,4142 | 1 | 1 | √2 + 1 = 2,4142 | 0 | 1 | √2 − 1 | 1 | √2 + 1 |

Les contacts du triangle sont ceux de la translation divisés par la projection : 1/(1 + s) = (s − 1)/g² et 1/(s − 1) = (s + 1)/g². En dimension infinie, g² = 1 et les deux déplacements touchent le pré aux mêmes distances, √2 − 1 et √2 + 1 (le nombre d'argent).

**Le déplacement hyperbolique.** Tous ses cercles passent par la base du simplexe (en 2D, les points A et B à ±1/√3 sur la perpendiculaire à OP). Son membre tangent au pré, en d = 1/(n+1), de rayon n/(n+1), est la sphère circonscrite au simplexe : elle touche le pré au piquet. Il ne touche jamais le pré de l'extérieur, et n'atteint la moitié qu'à l'infini (le plan de la base) : il suit exactement l'asymptote de la chèvre.

| n | part en d = 0 : g^n | part au contact : (n/(n+1))^n | part en d = 1 (simplexe) | déficit 1/2 − part, d = 1 | d = 2 | d = 5 | d = 20 | prédit en d = 20 : c_n V_{n−1}/(2 V_n ρ³) |
|---:|---|---|---|---|---|---|---|---|
| 2 | 0,333333 | 0,444444 | 0,497170 | 2,830e−03 | 3,818e−04 | 2,503e−05 | 3,929e−07 | 3,925e−07 |
| 3 | 0,353553 | 0,421875 | 0,496684 | 3,316e−03 | 4,667e−04 | 3,102e−05 | 4,881e−07 | 4,874e−07 |
| 5 | 0,362887 | 0,401878 | 0,496993 | 3,007e−03 | 4,295e−04 | 2,869e−05 | 4,519e−07 | 4,510e−07 |
| 10 | 0,366648 | 0,385543 | 0,498083 | 1,917e−03 | 2,685e−04 | 1,781e−05 | 2,802e−07 | 2,795e−07 |
| ∞ | 1/e | 1/e | 1/2 | 0 | 0 | 0 | 0 | 0 |

En 2D, le déficit en d = 1 (0,0028299, soit 0,566 % de la moitié) est la zone de confusion de la partie VI divisée par π ; en 3D (0,0033163), c'est la part manquante exacte (59 − 24√6)/64 de la partie VI.
Sur 500 positions de d ∈ ]0 ; 200], la part couverte le long de l'hyperbole reste sous 1/2 (plus petit déficit, en d = 200 : 3,93e−10 pour n = 2, 4,88e−10 pour n = 3, 4,52e−10 pour n = 5, 2,80e−10 pour n = 10).

## 6. Le terme suivant : ρ² − d² = g² + c_n/ρ² + …

Développement au second ordre (fait ici, à la main, puis vérifié) : la coupe par la sphère de la corde est presque plate, x₁ ≈ (|y|² − H)/(2ρ) + (|y|⁴ − H²)/(8ρ³), et près du bord elle sort du pré. On obtient
c_n = (Var|y|² − ménisque du bord)/4, avec Var|y|² = 4(n−1)/((n+1)²(n+3)) (la dispersion de l'ombre) et le terme du bord (n−1)(1 − g²)³/6 = 4(n−1)/(3(n+1)³). Donc c_n = 2n(n−1)/(3(n+1)³(n+3)).

| n | c_n (formule) | (ρ² − d² − g²)·ρ², d = 30 | d = 100 | Var|y|² | bord | bord/Var = (n+3)/(3(n+1)) |
|---:|---|---|---|---|---|---|
| 2 | 0,0098765 | 0,0098795 | 0,0098769 | 0,088889 | 0,049383 | 0,5556 |
| 3 | 0,0104167 | 0,0104210 | 0,0104171 | 0,083333 | 0,041667 | 0,5000 |
| 5 | 0,0077160 | 0,0077204 | 0,0077165 | 0,055556 | 0,024691 | 0,4444 |
| 10 | 0,0034676 | 0,0034702 | 0,0034678 | 0,022886 | 0,009016 | 0,3939 |

En 3D, le ménisque du bord vaut exactement la moitié de la dispersion de l'ombre ; à l'infini, le tiers.
