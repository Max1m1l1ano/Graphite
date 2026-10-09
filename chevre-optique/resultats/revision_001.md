# Révision 001 du recueil : les tests attachés à la révision

Écrit par `python3 scripts/revision_001.py`. La synthèse est dans [`recueil/revisions/revision-001.md`](../recueil/revisions/revision-001.md).

## 1. La diagonale √2 : la classification naïve, la corde de la chèvre et Thalès

**La classification naïve est un simplexe.** On range K fiches à parts égales dans K dimensions (un vecteur d'appartenance 0/1 par fiche), puis on retire la fiche moyenne et on normalise. Les K vecteurs sont alors les sommets du simplexe régulier inscrit dans la sphère unité : cos = −1/(K − 1) entre deux sommets.

**Deux longueurs pour chaque paire, et Thalès.** Pour deux vecteurs unités u et w :
- l'arête d = |u − w| (la distance entre les deux fiches) ;
- la corde c = |u + w| (de u à l'antipode de w).
- On a toujours d² + c² = 4. Le triangle (w, u, −w) est rectangle en u, d'hypoténuse le diamètre (Thalès).
- Pour le simplexe : d² = 2 + 2/(K − 1) et c² = 2 − 2/(K − 1). Les deux côtés de l'angle droit tendent vers √2 : le triangle devient isocèle, c'est la moitié d'un carré de diagonale 2.

**La corde de la chèvre est la corde c d'un simplexe.** La partie XXIV a montré r_n² = 2 − 2x₀ (Euclide), avec un plan de lentille en 1/x₀ = n + 4/3 − 112/(45n) + … Donc ρ_n = c_K pour K − 1 = 1/x₀ : la chèvre de dimension n a la corde du simplexe de la classification naïve à K = n + 2 + (N − n) dimensions. N − n est le tiers de dimension de la partie XXIV (de 0 en 1D à 1/3 à l'infini).

| n | corde ρ_n (chèvre) | n·(2 − ρ_n²) | K tel que c_K = ρ_n | K − n | 7/3 − 112/(45n) + 3856/(189n²) | arête d_K de ce simplexe |
|---:|---|---:|---:|---:|---:|---:|
| 1 | 1,0 | 1,0 | 3,0 | 2,0 | — | 1,7320508 |
| 2 | 1,15872847302 | 1,3147 | 4,042527 | 2,04253 | — | 1,6301375 |
| 3 | 1,22854486374 | 1,47203 | 5,0759968 | 2,076 | — | 1,578188 |
| 4 | 1,26807925667 | 1,5679 | 6,1023662 | 2,10237 | — | 1,5466011 |
| 8 | 1,33486242916 | 1,74514 | 10,168327 | 2,16833 | — | 1,4893429 |
| 17 | 1,37488172634 | 1,8649 | 19,231501 | 2,2315 | — | 1,4524807 |
| 24 | 1,385931575 | 1,90065 | 26,254544 | 2,25454 | 2,26505 | 1,4419409 |
| 100 | 1,40721663872 | 1,97413 | 102,31029 | 2,31029 | 2,31048 | 1,421176 |
| 1000 | 1,41350721901 | 1,99734 | 1002,3309 | 2,33086 | 2,33086 | 1,4149196 |

- Contrôle : les cordes redonnent le tableau de la partie XX (calculées ici par les calottes, là par la division d'intégrales d'Ullisch), par exemple ρ₂ = 1,15872847302 et ρ₁₀₀ = 1,40721663872.
- K − n monte de 2 (en 1D, où la corde vaut 1) vers 7/3 = 2,3333… : c'est 2 + le tiers de dimension.

**Le contrôle numérique du simplexe** (les vecteurs centrés, sans formule) :

| K | d_K mesuré | √(2K/(K − 1)) | c_K mesuré | √(2(K − 2)/(K − 1)) | d² + c² |
|---:|---:|---:|---:|---:|---:|
| 2 | 2,0000000000 | 2,0000000000 | 0,0000000000 | 0,0000000000 | 4,000000000000 |
| 3 | 1,7320508076 | 1,7320508076 | 1,0000000000 | 1,0000000000 | 4,000000000000 |
| 4 | 1,6329931619 | 1,6329931619 | 1,1547005384 | 1,1547005384 | 4,000000000000 |
| 8 | 1,5118578920 | 1,5118578920 | 1,3093073414 | 1,3093073414 | 4,000000000000 |
| 17 | 1,4577379737 | 1,4577379737 | 1,3693063938 | 1,3693063938 | 4,000000000000 |
| 100 | 1,4213381090 | 1,4213381090 | 1,4070529414 | 1,4070529414 | 4,000000000000 |
| 1000 | 1,4149211999 | 1,4149211999 | 1,4135055706 | 1,4135055706 | 4,000000000000 |

- Sans centrer, deux fiches de dimensions différentes sont exactement à √2 l'une de l'autre, pour tout K : la diagonale d'une face du cube {0, 1}^K du Venn. En retirant ce que toutes les fiches ont en commun (la moyenne), on obtient le simplexe, et le √2 devient une limite : il « s'affirme » quand le nombre de dimensions grandit.
- Le « partage équitable des aires » est ce qui rend le simplexe régulier. Avec des parts inégales, les arêtes se déforment (section 2).

## 2. Les fiches dans le Venn des dimensions

### 2.1 Avant la révision : la classification naïve, à parts inégales

Les 15 fiches occupent K = 6 dimensions sur 8 : D1 (1), D2 (4), D3 (3), D4 (1), D6 (2), D7 (4). Avec des parts égales, le simplexe régulier aurait toutes ses arêtes à √(2K/(K − 1)) = 1,5492. Le nombre effectif de dimensions (1/Σp²) vaut 4,79.

| paire de dimensions | parts | p_a + p_b | Σp² | arête mesurée | côté de √2 |
|---|---|---:|---:|---:|---|
| D1–D2 | 1 et 4 | 0,3333 | 0,2089 | 1,5139 | au-dessus |
| D1–D3 | 1 et 3 | 0,2667 | 0,2089 | 1,4574 | au-dessus |
| D1–D4 | 1 et 1 | 0,1333 | 0,2089 | 1,3636 | en dessous (lien apparent) |
| D1–D6 | 1 et 2 | 0,2000 | 0,2089 | 1,4080 | en dessous (lien apparent) |
| D1–D7 | 1 et 4 | 0,3333 | 0,2089 | 1,5139 | au-dessus |
| D2–D3 | 4 et 3 | 0,4667 | 0,2089 | 1,6424 | au-dessus |
| D2–D4 | 4 et 1 | 0,3333 | 0,2089 | 1,5139 | au-dessus |
| D2–D6 | 4 et 2 | 0,4000 | 0,2089 | 1,5745 | au-dessus |
| D2–D7 | 4 et 4 | 0,5333 | 0,2089 | 1,7206 | au-dessus |
| D3–D4 | 3 et 1 | 0,2667 | 0,2089 | 1,4574 | au-dessus |
| D3–D6 | 3 et 2 | 0,3333 | 0,2089 | 1,5117 | au-dessus |
| D3–D7 | 3 et 4 | 0,4667 | 0,2089 | 1,6424 | au-dessus |
| D4–D6 | 1 et 2 | 0,2000 | 0,2089 | 1,4080 | en dessous (lien apparent) |
| D4–D7 | 1 et 4 | 0,3333 | 0,2089 | 1,5139 | au-dessus |
| D6–D7 | 2 et 4 | 0,4000 | 0,2089 | 1,5745 | au-dessus |

**Le cadre crée des liens.** Entre deux fiches de classes a et b, la corrélation des vecteurs centrés vaut (Σp² − p_a − p_b)/√((1 − 2p_a + Σp²)(1 − 2p_b + Σp²)). Elle est positive, donc l'arête passe sous √2, exactement quand p_a + p_b < Σp² (vérifié sur les 15 paires : oui). Deux dimensions rares paraissent donc liées sans rien partager : elles ont seulement en commun de ne pas être les grosses classes. Avec des parts égales, p_a + p_b = 2/K > Σp² = 1/K : aucune paire ne passe sous √2, toutes les arêtes sont égales, et elles rejoignent √2 quand K grandit. **Le partage équitable des aires est ce qui empêche le cadre de fabriquer des corrélations.** C'est le « problème des doubles zéros » de l'écologie numérique (deux relevés paraissent semblables parce qu'il leur manque les mêmes espèces : Legendre et Legendre), de la même famille que les corrélations parasites des données à somme constante (Pearson, 1897 ; Chayes, 1960 ; Aitchison, 1986).

### 2.2 Après la révision : les fiches dans les dossiers

Chaque fiche devient un vecteur d'appartenance aux huit dossiers (une fiche peut tomber dans plusieurs). On centre, on normalise, et on compare les distances des paires qui partagent au moins un dossier (les liées) à celles des paires qui n'en partagent aucun. Deux pesées : brute, et à aires égales (chaque dossier divisé par son nombre de fiches). Le nul : 1 000 recouvrements tirés avec les mêmes tailles de dossiers et le même nombre de dossiers par fiche (curveball).

| recouvrement | pesée | paires liées | distance moyenne des liées | paires non liées | distance moyenne des non liées | non liées sous √2 | écart non liées − liées | p (nul) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| v1 | brute | 65 | 1,3162 | 40 | 1,6427 | 5 % | 0,3264 | 0,932 |
| v1 | aires égales | 65 | 1,3224 | 40 | 1,5645 | 10 % | 0,2421 | 0,961 |

- **Les deux populations se séparent, mais mécaniquement.** Les paires liées sont en moyenne à 1,3162, sous √2 = 1,4142 ; les paires sans dossier commun sont à 1,6427, au-dessus de √2, du côté de l'arête du simplexe (√(16/7) = 1,5119 pour huit dossiers à parts égales).
- **Le nul le montre** : p = 0,93. Des dossiers de mêmes tailles, tirés au hasard, séparent aussi bien. C'est la définition même d'un dossier commun qui rapproche deux fiches : cette mesure ne dit rien du contenu. Pour qu'elle parle, il faut des liens définis autrement, par exemple ceux que les agents ont trouvés par le même procédé (section 2.3).
- **Des liens du cadre restent possibles.** 5 % des paires non liées passent sous √2 en pesée brute : des fiches qui ne partagent rien, mais qui tombent dans de petits dossiers (la règle de la section 2.1, étendue aux fiches à plusieurs dossiers : P_a + P_b < Σp², où P est la somme des parts des dossiers de la fiche).

## 3. Le nerf des dossiers : ce qui se recolle, et les trous

Un sommet par dossier ; une arête quand deux dossiers partagent un élément ; un triangle quand trois en partagent un, et ainsi de suite (le procédé de Čech de la partie XX). Trois niveaux : (1) les fiches ; (2) les fiches sans les deux hasards testés 002 et 004 ; (3) les fiches et les parties. Un **triangle vide** a ses trois côtés, mais rien de commun aux trois : c'est l'observation qui manque pour les recoller.

| recouvrement | niveau | sommets, arêtes, triangles, tétraèdres | Betti b₀, b₁, b₂ | triangles vides | triangles remplis : éléments communs en moyenne | nul : b₁ moyen | nul : b₂ moyen | nul : triangles vides en moyenne | p (nul ≥ observé) |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| v1 | 1 | 8, 18, 7, 1 | 1, 5, 0 | 9 | 1,1 | 3,04 | 0,00 | 5,5 | 0,133 |
| v1 | 2 | 8, 17, 7, 1 | 1, 4, 0 | 7 | 1,1 | 2,72 | 0,00 | 4,9 | 0,266 |
| v1 | 3 | 8, 28, 36, 11 | 1, 0, 5 | 20 | 1,5 | 0,22 | 5,58 | 18,7 | 0,409 |

**v1 : les triangles vides au niveau des fiches** (9) :
- aiguilles-kakeya-perron · grain-pixels-centres · hasard-et-methode : trou du corpus (vide aussi avec les parties).
- aiguilles-kakeya-perron · grain-pixels-centres · ombres-cube-venn : trou du corpus (vide aussi avec les parties).
- bases-congruences-premiers · corde-et-dimensions · moities-et-crans : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · corde-et-dimensions · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · grain-pixels-centres · hasard-et-methode : trou du corpus (vide aussi avec les parties).
- bases-congruences-premiers · grain-pixels-centres · ombres-cube-venn : trou du corpus (vide aussi avec les parties).
- grain-pixels-centres · hasard-et-methode · lumiere-et-physique : trou du recueil (une partie les réunit, la fiche manque).
- grain-pixels-centres · hasard-et-methode · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- hasard-et-methode · lumiere-et-physique · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- Bilan v1 : 5 trous du recueil, 4 trous du corpus.
- Les fiches laissent 9 triangles vides, contre 5,5 en moyenne pour des dossiers de mêmes tailles tirés au hasard (p = 0,13) : un peu plus que le hasard, sans plus. Les trous se lisent donc un par un, comme des pistes, pas comme une preuve.
- **Avec les parties (niveau 3), les boucles se remplissent** (b₁ = 0), mais il reste b₂ = 5 cavités (nul : 5,58 en moyenne, p = 0,706). Une cavité, ce sont quatre dossiers dont les quatre triplets se recollent, sans élément commun aux quatre : un trou d'un étage plus haut. Les 6 tétraèdres creux :
  - aiguilles-kakeya-perron · bases-congruences-premiers · moities-et-crans · ombres-cube-venn
  - aiguilles-kakeya-perron · grain-pixels-centres · lumiere-et-physique · moities-et-crans
  - aiguilles-kakeya-perron · hasard-et-methode · lumiere-et-physique · moities-et-crans
  - aiguilles-kakeya-perron · hasard-et-methode · lumiere-et-physique · ombres-cube-venn
  - aiguilles-kakeya-perron · lumiere-et-physique · moities-et-crans · ombres-cube-venn
  - bases-congruences-premiers · corde-et-dimensions · hasard-et-methode · moities-et-crans


## 4. Les nouveaux tests

### 4.1 Fiche 013 : la période de 1/7 et les racines digitales de 2ⁿ, en faisant varier la base

La fiche 013 note que la période de 1/7 (142857) s'écrit avec exactement les chiffres que visitent les racines digitales de 2ⁿ (1, 2, 4, 8, 7, 5), c'est-à-dire les unités modulo 9. On fait varier la base b et le premier p : pour quels (b, p) l'ensemble des chiffres de la période de 1/p en base b est-il exactement l'ensemble des unités modulo b − 1 (les racines digitales premières avec b − 1) ?

| base b | premier p | chiffres de la période de 1/p | 2 engendre-t-il les unités modulo b − 1 ? |
|---:|---:|---|---|
| 3 | 2 | {1} | non |
| 5 | 3 | {1, 3} | non |
| 10 | 7 | {1, 2, 4, 5, 7, 8} | oui |

- Bases 3 à 60, premiers jusqu'à 400 : 3 cas. En dehors des deux cas à un ou deux chiffres (bases 3 et 5), seul (10, 7) répond, et c'est le seul où les puissances de 2 parcourent aussi toutes les unités.
- **Pourquoi la base 10.** Les chiffres absents de la période de 1/7 sont 0, 3, 6 et 9. Ce sont les d pour lesquels l'intervalle [7d/10, 7(d + 1)/10[ ne contient aucun entier de 1 à 6, et cela tient à 7 × 3 = 21 ≡ 1 (mod 10) : 3 est l'inverse de 7 modulo 10, donc 7 × 3k ≡ k et les d absents sont ceux où 7d mod 10 ≤ 3, soit 0, 3, 6, 9. Les racines digitales absentes sont les multiples de 3 parce que 9 = 3². Le même 3 joue donc deux rôles : l'inverse de 7 modulo 10, et le premier de 9 = 10 − 1. La base 10 réunit ces deux rôles, et le balayage dit qu'aucune autre base de la plage ne réunit l'équivalent.
- **Verdict.** Ce n'est pas une loi des bases, c'est un fait singulier de la base 10. Faire varier le paramètre le montre, et l'explique (le choix du test du § 10). La fiche 013 passe de « exact pour 7 » à « exact, et propre à la base 10 ».

### 4.2 Fiche 015 : les paires de premiers dans une dizaine, en faisant varier la taille N

Sous 10⁶, les dizaines dont les seuls premiers sont {1, 7} ou {3, 9} (distance 6) sont environ 2,8 fois plus nombreuses, motif par motif, que celles dont les seuls premiers sont {1, 3}, {7, 9}, {3, 7} ou {1, 9} (fiche 015). On refait le compte de 10⁴ à 10⁸, de deux façons :
- **motifs exacts** : la dizaine n'a que ces deux premiers parmi 1, 3, 7, 9 (le rapport par motif) ;
- **paires larges** : les deux sont premiers, quoi qu'il en soit des deux autres (rapport des paires à distance 6 sur les paires à distance 2, dans la même dizaine).

| N | motifs exacts {1, 7} + {3, 9} | motifs exacts {1, 3} + {7, 9} | motifs exacts {3, 7} + {1, 9} | rapport par motif | paires larges : distance 6 / distance 2 |
|---:|---:|---:|---:|---:|---:|
| 10^4 | 189 | 46 | 51 | 3,8969 | 2,0916 |
| 10^5 | 1 184 | 370 | 383 | 3,1448 | 1,9988 |
| 10^6 | 8 424 | 3 008 | 2 941 | 2,8321 | 1,9901 |
| 10^7 | 62 778 | 24 060 | 23 669 | 2,6306 | 1,9809 |
| 10^8 | 485 343 | 192 484 | 191 869 | 2,5255 | 1,9968 |

- **Le rapport par motif dérive** : 3,90 à 10⁴, 3,1448 à 10⁵ (π = 3,1416, écart 0,10 %), 2,8321 à 10⁶ (2√2 = 2,8284, écart 0,13 %), puis 2,6306 et 2,5255. Il croise π puis 2√2 en passant : ce sont deux hasards de taille. Sa vraie limite est 2, très lentement. Sur la face a ≡ 0 modulo 3, 3 et 9 sont composés d'office : l'exclusivité ne coûte rien à la moitié des paires {1, 7}, alors qu'elle coûte à toutes les paires {1, 3}, qui ne vivent que sur la face a ≡ 1. Cet avantage s'efface au rythme de la densité des premiers, en 1/ln N.
- **Le rapport des paires larges ne bouge pas** : entre 1,981 et 2,092 de 10⁴ à 10⁸. C'est 2, le rapport des séries singulières de Hardy et Littlewood, S(6)/S(2) = (3 − 1)/(3 − 2) : une paire à distance 6 a deux fois plus de chances, parce que 3 divise 6.
- **La leçon** (§ 10, le choix du test) : une grandeur qui dérive lentement croise des constantes célèbres. À une seule taille, 2√2 à 0,13 % ressemble à une découverte ; en faisant varier N, la dérive apparaît, et la loi (le 2) se lit sur l'autre compte.

### 4.3 K3 : la famille b = q² + 1 explique le cas (10, 7) (plan, § 3.2)

Pour q premier, on pose b = q² + 1 et p = q² − q + 1. Quatre propriétés se vérifient pour tout q : q² ≡ −1 (mod b), donc q est le i de la base b ; q·p ≡ 1 (mod b), donc q est l'inverse de p ; p − 1 = q(q − 1) = φ(b − 1) ; et p divise q³ + 1 = (q + 1)·p, donc la période de 1/p en base b divise 6.

| q | b = q² + 1 | p = q² − q + 1 | p premier ? | q² mod b | q·p mod b | φ(b − 1) | période de 1/p en base b | chiffres = unités mod b − 1 ? |
|---:|---:|---:|---|---:|---:|---:|---:|---|
| 2 | 5 | 3 | oui | 4 (= −1) | 1 | 2 | 2 | oui |
| 3 | 10 | 7 | oui | 9 (= −1) | 1 | 6 | 6 | oui |
| 5 | 26 | 21 | non | 25 (= −1) | 1 | 20 | — | non |
| 7 | 50 | 43 | oui | 49 (= −1) | 1 | 42 | 6 | non |
| 11 | 122 | 111 | non | 121 (= −1) | 1 | 110 | — | non |
| 13 | 170 | 157 | oui | 169 (= −1) | 1 | 156 | 6 | non |
| 17 | 290 | 273 | non | 289 (= −1) | 1 | 272 | — | non |
| 19 | 362 | 343 | non | 361 (= −1) | 1 | 342 | — | non |

- La période remplit tout le groupe des unités seulement si q(q − 1) ≤ 6, soit q = 2 (b = 5, p = 3) et q = 3 (b = 10, p = 7) : exactement les deux cas non triviaux du balayage 4.1. Au-delà, p reste premier pour q = 7 (b = 50, p = 43) et q = 13 (b = 170, p = 157), mais la période vaut 6.
- **Ce qui se recolle** : le 3 de la fiche 013 (l'inverse de 7 modulo 10) et le 3 de la partie XIX (3 ≡ i modulo 10, l'aiguille de pente i) sont le même 3. La fiche 013 et la partie XIX se recollent par la famille q² + 1.

### 4.4 T3 : la chèvre et le polygone, ordre par ordre (K1), et le seuil du centre du Venn (K10)

On écrit la lumière qui manque au polygone inscrit à N côtés, 1 − sin(x)/x = x²/6 − x⁴/120 + …, avec x = 2π/N et N = π(n + s) : l'ordre 2 donne exactement le 2/(3n²) de la chèvre (le facteur π est imposé). Il reste le décalage s.

| ordre | chèvre μ_j | polygone, s = 0 | polygone, s qui recolle l'ordre 3 |
|---:|---:|---:|---:|
| 1/n^2 | 2/3 (0,6667) | 2/3 | 0,6667 |
| 1/n^3 | -98/15 (−6,533) | 0 | −6,533 |
| 1/n^4 | 5966/105 (56,82) | -2/15 | 47,89 |
| 1/n^5 | -1698106/2835 (−599) | 0 | −311,1 |
| 1/n^6 | 247172734/31185 (7926) | 4/315 | 1890 |

- L'ordre 3 se recolle pour s = 49/10 : la chèvre et le polygone ont la même forme x²/6, et un décalage d'environ cinq dimensions rattrape l'ordre suivant. L'ordre 4 ne se recolle plus : 47,89 contre 56,82.
- **Verdict** : le même exposant et le même 1/6, pas le même ménisque. Les deux séries n'ont pas la même nature : celle de la chèvre diverge (rapports μ_(j+1)/μ_j ≈ −j·2/ln 2, partie XXIV), celle du sinus converge partout. L'obstruction est d'ordre 4 dès qu'on autorise un décalage, d'ordre 3 sans décalage. Elle désigne l'asymétrie de la coquille (partie XXIV, § 1), qu'un polygone à un seul rayon n'a pas.

**K10, le seuil du centre du Venn** (partie XXX, § 6.4). Le centre demande W_c = (2/π)·√(n(2ⁿ − 2)) pixels, le reste W_r = 4·√((2ⁿ − 2)/π). Leur rapport vaut exactement √(n/(4π)) : le centre devient le goulot à n* = 4π.
- **Pourquoi 4π.** Le centre doit loger n croisements à 2 px l'un de l'autre sur un cercle : son périmètre vaut L = 2n. Il doit aussi loger n régions d'au moins 2 × 2 px : son aire vaut A = 4n. Pour un cercle, L²/A = 4π (la constante isopérimétrique), d'où 4n² = 4π·4n, soit n* = 4π = 12,566.
- **Avec des segments.** Si les n croisements du centre sont joints par des segments, le centre est un n-gone régulier, dont la constante isopérimétrique vaut 4n·tan(π/n). Le seuil devient tan(π/n*) = 1/4, soit n* = π/arctan(1/4) = 12,824. Dans les deux cas, le centre devient le goulot dès 13 courbes.
- **Ce qui se recolle** : n·tan(π/n) est exactement la quantité de la fiche 003 (34·tan(π/34) ≈ π). Le seuil du centre du Venn et le polygone circonscrit des éventails de Perron sont la même constante isopérimétrique.

### 4.5 T7 : les trois 4/3 (K8)

On compte, pour chaque base b de 3 à 10⁶, les puissances de 2 et de 3 inférieures à b (1 compris). En base 10 : 1, 2, 4, 8 et 1, 3, 9, soit 4 et 3.

- Le rapport vaut 4/3 sur b = 10 à 16 et b = 244 à 256 seulement. Ensuite il tend vers log₂ 3 = 1,585 (le rapport du comma pythagoricien de la partie XX).
- V₃/V₂ = 4/3 est un pas de Wallis (partie III) : la suite V_(n+1)/V_n tend vers 0. Le 4/3 de 1/x₀ = n + 4/3 (partie XXIV) est une constante de la série de la corde (1 pour le simplexe, 1/3 pour le ménisque).
- **Verdict** : trois procédés différents donnent la même valeur pour de petits nombres. C'est une coïncidence de petits entiers, répliquée nulle part ailleurs ; le lien qui reste passe par log₂ 3 et les réduites de l'arbre P6 (19/12, le comma).

### 4.6 T6 : Midy en Perron, la tour 2-adique des périodes (K9)

La période de 1/p en base 10 est l'ordre L(p) de 10 modulo p. Midy demande L pair ; Midy étendu à ℓ blocs demande ℓ | L. On mesure, pour les premiers p < N (sauf 2 et 5), la part des v₂(L) = 0, 1, 2, 3… (la tour 2-adique) et la part des ℓ | L.

| base | N | L pair | v₂ = 0 | v₂ = 1 | v₂ = 2 | v₂ = 3 | 3 \| L | 5 \| L | 7 \| L |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10^3 | 0,6566 | 0,3434 | 0,3313 | 0,1627 | 0,0663 | 0,3494 | 0,2108 | 0,1446 |
| 10 | 10^4 | 0,6675 | 0,3325 | 0,3382 | 0,1695 | 0,0782 | 0,3765 | 0,2152 | 0,1434 |
| 10 | 10^5 | 0,6667 | 0,3333 | 0,3325 | 0,1659 | 0,0845 | 0,3755 | 0,2068 | 0,1443 |
| 10 | 10^6 | 0,6666 | 0,3334 | 0,3340 | 0,1660 | 0,0832 | 0,3758 | 0,2076 | 0,1457 |
| 2 | 10^6 | 0,7077 | 0,2923 | 0,2916 | 0,3329 | 0,0417 | 0,3752 | 0,2086 | 0,1458 |
| 3 | 10^6 | 0,6662 | 0,3338 | 0,3338 | 0,1657 | 0,0832 | 0,3753 | 0,2081 | 0,1460 |
| 7 | 10^6 | 0,6668 | 0,3332 | 0,3334 | 0,1665 | 0,0835 | 0,3745 | 0,2085 | 0,1459 |
| 12 | 10^6 | 0,6670 | 0,3330 | 0,3341 | 0,1660 | 0,0833 | 0,3744 | 0,2091 | 0,1461 |

- **La tour se divise par deux.** En base 10 sous 10⁶ : v₂(L) = 0, 1, 2, 3 pour 0,333, 0,334, 0,166, 0,083 des premiers. Au-delà du premier étage, chaque étage garde à peu près la moitié du précédent (1/3, 1/3, 1/6, 1/12 attendus) : un arbre de Perron sur les périodes, dont les fentes se referment de moitié à chaque étage.
- **Les aires ne sont pas égales.** La part des périodes paires vaut 0,6666 en base 10 (2/3 = 0,6667, Hasse, 1966) et 0,7077 en base 2 (17/24 = 0,7083). Le « Venn de Midy » de l'auteur est donc un Venn à aires inégales par nature : deux tiers pour les périodes paires, un tiers pour les impaires.
- **La base 2 a sa propre tour** : 0,292, 0,292, 0,333, 0,042 pour v₂ = 0 à 3. L'étage 2 y est plus lourd parce que 2 est un carré modulo p exactement quand p ≡ ±1 (mod 8) : c'est de là que vient le 17/24 de Hasse. Les bases 3, 7, 10 et 12 suivent la tour générique.
- **Midy étendu.** La part des ℓ | L vaut 0,376, 0,208 et 0,146 pour ℓ = 3, 5, 7, contre ℓ/(ℓ² − 1) = 0,375, 0,208 et 0,146 pour une base générique (valeurs attendues ; à confirmer dans la littérature sur la conjecture d'Artin).

### 4.7 T5 : la moitié de Kakeya fini, en caractéristique 2 (K4)

La partie XIV a trouvé qu'un ensemble de Kakeya du plan F_q² (une droite entière dans chacune des q + 1 directions) occupe environ la moitié du plan, et l'a expliqué par les carrés modulo q : l'involution x ↦ −x. En caractéristique 2, cette involution est l'identité. On calcule donc le minimum exact dans les corps F_q, q = 2, 3, 4, 5, 7, 8, 9 (tables d'addition et de multiplication construites par des polynômes irréductibles), avec les symétries de la partie XIV, et on compte dans l'ensemble trouvé les points couverts 1, 2 ou 3 fois.

| q | caractéristique | minimum (calculé) | q(q + 1)/2 | excès | points simples | doubles | triples | durée |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 3 | 3 | 0 | 0 | 3 | 0 | 0,0 s |
| 3 | 3 | 7 | 6 | 1 | 3 | 3 | 1 | 0,0 s |
| 4 | 2 | 10 | 10 | 0 | 0 | 10 | 0 | 0,0 s |
| 5 | 5 | 17 | 15 | 2 | 6 | 9 | 2 | 0,1 s |
| 7 | 7 | 31 | 28 | 3 | 9 | 19 | 3 | 1,9 s |
| 8 | 2 | 36 | 36 | 0 | 0 | 36 | 0 | 4,8 s |
| 9 | 3 | 49 | 45 | 4 | 12 | 33 | 4 | 21,6 s |

- **L'identité exacte.** Les q + 1 droites se coupent deux à deux en un seul point. En comptant chaque point avec sa multiplicité m_P (le nombre de droites qui y passent), 1 = m − C(m, 2) + C(m − 1, 2) pour tout m ≥ 1. On en tire |K| = q(q + 1) − C(q + 1, 2) + Σ C(m_P − 1, 2) = q(q + 1)/2 + Σ C(m_P − 1, 2).
- **La moitié vient de l'inclusion–exclusion**, tronquée à l'ordre 2 : c'est l'inégalité de Bonferroni |∪L| ≥ Σ|L| − Σ|L ∩ L′|, vraie dans toutes les caractéristiques. Elle est atteinte pour q = 2, 4, 8 : tous les points sont doubles, aucun n'est triple.
- **La parité ne compte que l'excès.** Pour q impair, le minimum dépasse la borne de (q − 1)/2, et l'ensemble optimal a exactement (q − 1)/2 points triples (Blokhuis et Mazzocca pour le minimum). Pour q pair, l'excès est nul. Les carrés modulo q (l'involution) n'expliquent donc que l'excès, pas la moitié.
- **Verdict.** La piste XIV–XX de la carte (partie XXVII, § 9) se ferme par une obstruction : la moitié de Kakeya fini et celle des hémisphères ne viennent pas du même procédé. Un autre lien s'ouvre : l'inégalité de Bonferroni, tronquée à l'ordre 1, est la correction de Bonferroni de la fiche 012 ; tronquée à l'ordre 2, elle donne la moitié de Kakeya fini. Même procédé : tronquer l'inclusion–exclusion.

### 4.8 T4 : le centre de la lumière se déplace par la palette, par l'ordre de dessin ou par le seuil ? (K6)

On classe chaque pixel d'encre (clarté L > fond + 0,1) par sa teinte OKLab, au plus près des 17 teintes h_i = 25° + 360°·i/17 de la palette du traceur, et on mesure pour chaque classe son aire visible A_i et son moment M_i = Σ (z − c) autour du centre de symétrie c.

| chroma minimal | pixels classés | étendue des phases de M_i, rotation retirée | premier harmonique des aires A_i | meilleure montée cyclique des A_i (Spearman) | p (2 000 permutations) |
|---:|---:|---:|---:|---:|---:|
| 0,04 | 1 162 689 | 6,2° | 1,9 % | 0,38 | 0,64 |
| 0,06 | 845 436 | 7,4° | 7,7 % | 0,53 | 0,19 |

- **Les couleurs suivent les courbes.** Une fois la rotation de 2π·i/17 retirée, les phases des 17 moments ne s'étalent que de quelques degrés : la classe de teinte i est bien la courbe i, et les teintes tournent dans l'ordre des rotations.
- **Pas de signature d'ordre de dessin.** Si les courbes étaient dessinées de 0 à 16, la dernière couvrant les autres à chaque croisement, l'aire visible monterait le long d'un tour. La meilleure montée cyclique reste dans le nul des permutations, et le profil des A_i change avec le chroma minimal : il mesure surtout l'efficacité du classement selon la teinte.

**Le seuil, seconde cause.** Un masque binaire donne le même poids à tout pixel d'encre : il ne voit ni la palette (aucun poids) ni l'ordre de dessin (aux croisements, l'encre reste de l'encre). Pourtant son centre bouge avec le seuil de clarté :

| masque L > fond + t | pixels | écart au centre de symétrie | direction (°, y vers le haut) |
|---:|---:|---:|---:|
| 0,02 | 2 342 258 | 0,37 px | −99 |
| 0,05 | 2 215 030 | 0,71 px | −122 |
| 0,10 | 1 988 488 | 1,26 px | −131 |
| 0,15 | 1 742 501 | 2,45 px | −131 |
| 0,20 | 1 414 736 | 4,67 px | −129 |
| 0,25 | 951 862 | 12,03 px | −130 |
| 0,30 | 557 559 | 13,75 px | −132 |
| 0,40 | 180 841 | 27,38 px | −136 |

- L'écart passe de 0,37 px (presque toute l'encre) à 27,4 px (les seuls cœurs des traits les plus clairs), dans une direction stable vers −130°. Plus le seuil est haut, plus il ne garde que les courbes claires : le seuil transforme la couleur en largeur visible, par l'anticrénelage des bords.
- **Verdict.** La cause unique « le premier harmonique des poids » ne suffit pas (K6), mais la seconde cause n'est pas l'ordre de dessin : c'est le seuil. La couleur déplace le centre par deux canaux, le poids (la pesée) et la largeur visible au-dessus d'un seuil. La phrase de la partie XXX, « tout écart vient des poids », devient « tout écart vient de la couleur, par le poids et par le seuil » ; la géométrie reste symétrique.
- **Le lien avec le sujet d'étude.** Restreindre le cadre (monter le seuil) fabrique un déplacement qui n'est pas dans la géométrie, comme le partage inégal des aires fabrique des liens (section 2.1). En astrométrie, c'est la différence entre un centroïde isophote (au-dessus d'un seuil) et un centroïde pondéré (Bertin et Arnouts, SExtractor, 1996), et la raison des corrections de chromaticité des catalogues.

### 4.9 Le masque binaire : de quoi, où, et ce que vaut 0,37 px (question de l'auteur)

- **L'image** : `venn17-pressure-dark-2000.png` (dépôt de Dzoba, copie locale ; c'est l'image de son README, celle des parties XXIX et XXX), 2000 × 2000 pixels, trois canaux de 8 bits non signés (0 à 255, type `uint8`). Le fond est une couleur exacte, RGB = (6, 6, 10) : un gris bleuté (92,7 % des pixels des bandes de 50 px au bord).
- **Le seuil, de quoi** : de la clarté perçue OKLab L (0 = noir, 1 = blanc), calculée pixel par pixel à partir des trois canaux. Le fond vaut L = 0,1246 (médiane du coin 20 × 20). Le masque est l'ensemble des pixels où L > fond + t : chacun pèse 1, les autres 0. Son centre est la moyenne des positions de ses pixels ; on le compare au centre de symétrie d'ordre 17, (999,497 ; 999,499), connu à 0,003 px (partie XXX, § 1).
- **Où** : partie XXX ([centre-venn.md](../centre-venn.md), § 1, la deuxième des six pesées, « masque de clarté OKLab (L > fond + 0,1) » ; § 2, la mesure de la moitié avec le même seuil) ; script `scripts/centre_venn.py` (section 1, liste `POIDS` ; fonction `mesure_moitie`, `seuil=0.1`) ; balayage du seuil : `scripts/revision_001.py`, sections 4.8 et 4.9 ; figure `rev001_diagonale_cadre.png`, panneau c ; fiche 018. La partie XXIX utilisait un autre masque binaire, sur la moyenne des canaux : moyenne RGB > fond + 25.

**Signé ou non signé ?** Un passage par des octets signés (−128 à 127) replierait les valeurs au-delà de 127 : l'histogramme des canaux sauterait entre 127 et 128. Il est lisse (rouge : 4 552 puis 4 377 ; bleu : 4 677 puis 4 504 ; l'écart du rapport 128/127 à ses voisins est de 0,6 % au plus). Et le calcul lui-même ne passe jamais par des entiers signés : les canaux sont lus de 0 à 255 puis divisés par 255.

**Le seuil, descendu jusqu'à zéro** :

| masque | pixels | écart au centre de symétrie | direction (°, y vers le haut) |
|---|---:|---:|---:|
| tout pixel différent du fond exact (6, 6, 10) (aucun seuil) | 2 981 328 | 0,044 px | −54 |
| L > fond + 0,001 | 2 447 266 | 0,117 px | 11 |
| L > fond + 0,002 | 2 441 864 | 0,063 px | −27 |
| L > fond + 0,005 | 2 427 167 | 0,086 px | −29 |
| L > fond + 0,010 | 2 398 326 | 0,124 px | −80 |
| L > fond + 0,015 | 2 369 380 | 0,265 px | −94 |
| L > fond + 0,020 | 2 342 258 | 0,375 px | −99 |
| L > fond + 0,030 | 2 298 524 | 0,477 px | −105 |
| L > fond + 0,050 | 2 215 030 | 0,715 px | −122 |

- **0,37 px n'est pas une constante** : c'est la valeur du balayage à t = 0,02. Sans aucun seuil, l'encre est centrée à 0,044 px près ; jusqu'à t = 0,01, l'écart reste entre 0,06 et 0,12 px (le niveau du bruit) ; au-delà, il monte avec le seuil. Rapporté au rayon du dessin (984 px), 0,37 px fait 3,8·10⁻⁴, soit 380 ppm : petit, mais cent fois la précision du centre.
- **Le zéro qui déséquilibre** : ton intuition a un vrai pendant dans l'image. Un axe de 2 000 pixels n'a pas de pixel central : le milieu tombe entre 999 et 1 000, en 999,5, comme le milieu de −128 … 127 tombe en −0,5. Qui prendrait 1 000 (= 2 000/2) pour centre se tromperait d'un demi-pixel sur chaque axe : 0,7071 px = √2/2, vers 135°. Le centre de symétrie mesuré, (999,497 ; 999,499), dit que le dessin respecte la bonne convention. Et le masque ne suit pas ce biais : sa direction est opposée en hauteur (−99° à −136°) et sa taille grandit avec le seuil. Il passe par 0,71 px à t = 0,05, à 1 % de √2/2 : encore une dérive qui croise une constante, comme les dizaines de premiers croisent π puis 2√2 (section 4.2).
- **Le 10/3** : le fond n'est pas un zéro neutre. Ses canaux valent (6, 6, 10), donc sa moyenne RGB vaut (6 + 6 + 10)/3 = 22/3, dont 10/3 viennent du bleu. Ce décalage est uniforme : il est retranché avant la pesée, et un fond uniforme n'a pas de dipôle (son centre est celui du cadre). Il agit seulement aux bords anticrénelés, où chaque courbe se mélange à ce zéro bleuté : il fait partie de l'effet du seuil. Pour le séparer, il faudrait un rendu sur un fond neutre (piste).

**Ce que le seuil change, et ce qu'il ne change pas** (la mesure de la moitié de la partie XXX, § 2, refaite à chaque seuil ; ρ est le rayon rapporté au contour, mesuré angle par angle) :

| seuil t | part de l'intérieur qui est de l'encre | encre dans le contour réduit de 1/√2 | ρ médian (1/√2 = 0,7071) | ⟨ρ²⟩ | écart du centre |
|---:|---:|---:|---:|---:|---:|
| 0,005 | 81,5 % | 49,70 % | 0,7093 | 0,5019 | 0,09 px |
| 0,020 | 78,7 % | 49,60 % | 0,7100 | 0,5028 | 0,37 px |
| 0,050 | 74,4 % | 49,53 % | 0,7105 | 0,5032 | 0,71 px |
| 0,100 | 66,8 % | 49,43 % | 0,7112 | 0,5037 | 1,26 px |
| 0,200 | 47,4 % | 49,32 % | 0,7121 | 0,5037 | 4,67 px |
| 0,300 | 18,6 % | 49,41 % | 0,7118 | 0,5008 | 13,75 px |

- Le seuil change la quantité d'encre de 81 % à 19 %, et le centre de 0,09 à 13,7 px. Mais la moitié reste à sa place : entre 49,32 % et 49,70 % de l'encre dans le contour réduit de 1/√2, ρ médian entre 0,7093 et 0,7121.
- **Pourquoi.** Le seuil change la couleur en largeur, et les couleurs tournent autour du centre : il touche le premier harmonique (le dipôle, donc le centre). La moitié ne regarde que la distance au centre, en moyenne sur toutes les courbes : l'harmonique zéro, que la rotation d'ordre 17 protège. Le résultat de la partie XXX sur la moitié est donc robuste au cadre ; ses centres de la lumière, eux, dépendent du cadre.

### 4.10 Quatre énoncés des dossiers, vérifiés avant d'être cités

- **Dossier corde, § 3.3** : E[(1 − E)^j] = (−1)^j·!j pour une loi exponentielle (!j : les dérangements 0, 1, 2, 9, 44, 265…). Vérifié pour j = 1 à 20 : oui. Le « dernier 2 » du ménisque 2/3 = 2 × 1/6 × 2 (partie XXIV) est donc −E[(1 − E)³] = !3 = 2.
- **Dossier bases, § 3.2** : Φ₆(10) = 10² − 10 + 1 = 91 = 7 × 13, et 10³ ≡ −1 (mod 91) : 1/7 et 1/13 ont la même période 6 parce qu'ils sont les deux facteurs du même polynôme cyclotomique. Vérifié : oui. C'est pourquoi la fiche 013 s'était demandé si 1/13 se comportait comme 1/7.
- **Dossier bases, § 3.2 (le lemme des chiffres)** : pour b = q² + 1 et p = q² − q + 1, les chiffres que peut prendre un développement de r/p en base b sont tous les chiffres sauf les multiples k·q (k = 0 … q). Vérifié pour q = 2 à 30 : oui. Pour q premier, ces chiffres sont exactement les unités modulo b − 1 = q² : le cas (10, 7) de la section 4.1 n'est plus un fait isolé, c'est le lemme quand la période est pleine.
- **Dossier aiguilles, § 3** : l'arbre de Perron à 8 branches de rapports (7/9, 25/42, 43/50) a l'aire exacte 0,398148148148148 = 43/108 (fonction `aire_exacte` de la partie V), sous les 2/5 de l'arbre télescopique. 2/(k + 2) est le minimum de la borne « cœur + oreilles » de la partie XXVIII, pas celui de l'aire.

### 4.11 Le « 93 % » de la défocalisation, contre un prédicteur constant (dossier lumière)

La partie XXX (§ 6.3) annonce des signes en accord avec 2 J₁(x)/x sur 93 % des 76 rayons de 15 à 90 px, avec une inversion mesurée de 16 à 21 px. Le modèle prévoit l'inversion de 9,7 à 17,7 px : sur les rayons étudiés, seulement 3 sont négatifs (15, 16, 17 px).

- Le modèle est d'accord sur 71 rayons sur 76 (93,4 %).
- Un prédicteur constant, « positif partout », l'est sur 70 (92,1 %) : c'est le taux de base.
- **Verdict** : le 93 % ne bat le taux de base que d'un rayon. La couronne inversée est réelle (de 16 à 21 px), mais cette statistique ne la teste pas : presque tous les rayons sont positifs, pour le modèle comme pour la mesure. Le bon test fait varier le rayon du flou b et l'harmonique (17, 34, 51) et vérifie que la couronne suit r entre m·b/7,016 et m·b/3,832 (dossier lumière, N4).

## 5. Le tableau des tests de la révision

| fiche ou partie | ce qui varie | verdict |
|---|---|---|
| 013 | variation de la base (3 à 60) et du premier (jusqu'à 400) | 3 cas, dont un seul non trivial : (10, 7) |
| 015 | variation de la taille N (10⁴ à 10⁸) | le rapport par motif dérive (3,90 → 2,53) ; les paires larges restent à 2 |
| 013 et XIX | la famille b = q² + 1 (q premier jusqu'à 19) | q = 2 et 3 seulement ; ailleurs période 6 |
| 011 et 003 | le seuil du centre : cercle contre n-gone | 4π = 12,566 et π/arctan(1/4) = 12,824 : 13 courbes dans les deux cas |
| recueil (4/3) | les bases de 3 à 10⁶ | 4/3 seulement pour b = 10 à 16 et b = 244 à 256 |
| recueil (Midy) | la tour 2-adique, bornes 10³ à 10⁶, bases 2, 3, 7, 10, 12 | 2/3 pair en base 10, 17/24 en base 2 ; 1/3, 1/3, 1/6, 1/12 |
| XIV et 012 | Kakeya dans F_q, q = 2 à 9 | q(q + 1)/2 exactement pour q pair ; + (q − 1)/2 points triples pour q impair |
| 006 et 007 | classes de teinte, montée cyclique, masques sans seuil puis de t = 0,001 à 0,40 | pas d'ordre de dessin ni de repli signé ; sans seuil 0,044 px, puis le seuil déplace le centre jusqu'à 27 px ; la moitié reste entre 49,3 et 49,7 % |
| dossiers corde, bases et aiguilles | quatre énoncés refaits | dérangements (j ≤ 20), Φ₆(10) = 7 × 13, lemme des chiffres (q ≤ 30), arbre de Perron 43/108 : vérifiés |
| XXX § 6.3 | le score du modèle contre un prédicteur constant | 71/76 contre 70/76 : le « 93 % » est le taux de base |

(calculs : 141 s)
