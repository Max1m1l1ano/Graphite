# La lumière et les analogies physiques : ce que l'optique et la chèvre partagent exactement

*Agent « lumiere » (Sonnet), révision 001, 2026-10-08. Dossier du plan, § 1.5. Statuts : **démontré**, **calculé**, **classique** (la littérature), **ma lecture**, **ouvert**. « Hors dépôt » : calcul de l'agent, fait dans un dossier temporaire ; aucun script du dépôt n'a été lancé. Les chemins ont été vérifiés avec `ls`.*

## Pour lire ce dossier

- Les quatre dossiers déjà écrits ne sont pas répétés. T4 en détail : [`grain-pixels-centres.md`](grain-pixels-centres.md), § 3.5. FTM50 en dimension n et point de Rayleigh : [`moities-et-crans.md`](moities-et-crans.md), N3 et N10. Col g_n de la chèvre : [`corde-et-dimensions.md`](corde-et-dimensions.md), F5. Diésis et comma : [`bases-congruences-premiers.md`](bases-congruences-premiers.md), N6.
- `scripts/revision_001.py` et `resultats/revision_001.md` ont déjà T1 à T7, le T4 (§ 4.8 et 4.9) et le nerf. Je ne les refais pas.
- Une « fiche proposée » n'a pas encore de numéro : l'agent de session la numérotera.

## En bref

- **Trois liens forts.**
  1. Les trois 34 (aigrettes, ombre Σωⁱ, éventails de Perron) sont un seul fait : μ_N ∪ (−μ_N) = μ_2N si N est impair. Démontré, vérifié pour N = 3 à 20 (K2).
  2. La forme de Newton x·x′ = c revient cinq fois : lentille, œil de poisson, jumeaux de la chèvre, fantômes des pixels, complément du Venn.
  3. Le centre de la lumière est le dipôle H₁ des poids (Wielen, HD, Venn). Avec les couleurs mesurées, une cause ne suffit pas (la luminance échoue d'un facteur 18) ; l'ordre de dessin est écarté (T4) ; une palette presque isoluminante et le seuil suffisent.
- **Trois trous.** (1) La palette réelle et le code de rendu de l'image de référence ne sont pas publiés. (2) D8 n'a aucune chaîne propre : neuf fiches proposées, dont trois en D8 ; les catalogues à source unique (Gaia) rangent le déplacement induit par la couleur dans le bruit ou dans le point zéro, à tester. (3) Le « 93 % » de la défocalisation (XXX § 6.3) est le taux de base d'un prédicteur constant.
- **Recouvrement.** Ajouter les parties XXI et XXIX et la fiche 003 ; ne rien retirer.

## 1. La question directrice et la projection sur D1–D8

### 1.1 La question

Quelles lois optiques et physiques suivent exactement le même procédé que la géométrie de la chèvre et du Venn, et que transportent-elles : une valeur, une prédiction, une méthode de mesure ?

### 1.2 Ma réponse, en six points (ma lecture, appuyée sur les sections 3 à 6)

1. **L'aire de la lentille est la machine commune** (I § 6). La FTM d'un objectif parfait, l'obscuration d'une éclipse, le vignettage d'un cran et la chèvre plane sont une seule fonction F(δ, k). La FTM50 est l'équation de Kepler avec e = 1 : ψ − sin ψ = π/2. Démontré, classique.
2. **La phase en r² fabrique zones, anneaux et moirés** (VIII, IX, XVII). Les zones de Fresnel, les anneaux de Newton et le repliement des pixels sont le même retard r²/2f, replié à un tour près. Démontré.
3. **La forme de Newton x·x′ = c revient cinq fois** (VIII § 5, IX § 3, XVII § 3, XVIII § 6, XXX § 3). Démontré chaque fois ; les constantes c ne sont reliées que par des changements d'unité (§ 5.2).
4. **Le cône à sommet imaginaire** (XIX § 6) relie la chèvre infinie, le cube qui tourne et le faisceau gaussien (Deschamps, 1971). Démontré. Le col g_n et le doublement de l'aire à la distance de Rayleigh (Self, 1983) sont déjà des fiches proposées par les dossiers corde et moitiés.
5. **Le barycentre pesé.** Un polygone aux poids inégaux a un dipôle H₁ (Wielen, HD, Venn). Structure ; T4 lève l'obstruction K6 sous condition (§ 3.3).
6. **La parité 2N.** Les aigrettes, l'ombre du cube et les éventails de Perron comptent la même orbite, de taille 2N si N est impair (§ 5.1). Démontré.

Aucun mécanisme physique commun n'est affirmé dans le corpus, et c'est correct (CLAUDE.md, § 1) : c'est une question ouverte, pas une objection.

### 1.3 La projection sur D1–D8 (ma lecture)

| D4 optique | D8 physique | D3 grain | D6 symétries | D7 méthode |
|---:|---:|---:|---:|---:|
| 0,5 | 0,2 | 0,1 | 0,1 | 0,1 |

Le plan donne D4 0,6, D8 0,3, D3 0,1. Je baisse D4 et D8 de 0,1 chacun : D8 parce que le cône (Deschamps, Self) est aussi traité par les dossiers corde et moitiés ; D6 pour K2 (l'orbite d'un groupe, l'ombre du cube) ; D7 pour trois leçons de méthode (le seuil, le taux de base, la variation du paramètre).

## 2. Les chaînes de production (script → résultats → figures → document)

Chemins relatifs à la racine du dépôt : `scripts/`, `resultats/`, `figures/`. Les numéros de section des résultats ne sont pas ceux des documents (par exemple `pixels_longitudes.md` § 5–6 est le § 6–7 du document).

| partie | script (sections, fonctions) | résultats | figures | ce que la chaîne produit |
|---|---|---|---|---|
| I § 6 | `calculs.py` § 6 ; `figures.py` (`fig_optique`, `fig_newton`, `fig_eclipse`) | `resultats.md` § 6 | `fig7_optique`, `fig8_anneaux_newton`, `fig9_eclipses` | FTM50 = 0,4039727533 ν_c ; Airy 0,534832 λN ; éclipses 32,6 à 44,5 % ; Newton ρ₁ = 0,768 mm (R = 1 m) |
| II § 3, 9 | `calculs_archimede.py` ; `figures_archimede.py` | `archimede.md` § 4, 9 | `b4_menisque` | corde du polygone inscrit 1,158728 − 0,99/n², circonscrit + 0,49/n² ; aigrettes N ou 2N |
| VIII | `foyer_fibonacci.py` § 1–8 (`ftm`, `ftm_min`, `rayon_maxwell`, `deux_foyers`) | `foyer_fibonacci.md` § 1–8 | `h1_foyer_menisques` a–f, `h2_fibonacci` a–d | FTM50 s = 0,807946 ; FTO négative dès 0,6416 λ ; œil de poisson à 7·10⁻⁸ ; foyers u₁ + u₂ = N |
| IX | `moire_fibonacci.py` § 1–5 | `moire_fibonacci.md` § 1–3 | `i1_moire_fibonacci`, `i2_optique_racines` | centres fantômes x_m = m·R²/(2u), retrouvés à 0,2 px (144 anneaux) ; 1/z₁ + 1/z₂ = 1/z_N |
| X § 1, 6 | `carre_ptolemee.py` § 1, 6 | `carre_ptolemee.md` § 1, 5 | `j1_carre_ptolemee` | le « trou » de ±24,18° autour de 29,05° suit le point P et le seuil de rayon 3 ; plan hyperbolique |
| XI § 3–4 | `angle_or_aiguilles.py` § 3–4 | `angle_or_aiguilles.md` § 3–4 | `k1_angle_or_aiguilles` d, e | spectre des 55 anneaux (21, 34, 13, 76…), répliques u + 55k, zéros en 55k ; 8 composantes : 0,885 ; 40 : 0,971 |
| XII § 1, 4 | `lentille_144.py` § 1, 3 | `lentille_144.md` § 1, 3 | `l1_lentille_144` | foyers 55,03 et 88,97 sur 144 anneaux : 55/144 et 89/144 de tour |
| XIII § 1–4 | `perron_dephasage.py` § 1–4 | `perron_dephasage.md` § 1–4 | `m1_perron_dephasage` a–e | nœuds d'aiguilles (|a − b| ↔ a + b) ; Fourier = rotation de 90°, à 5·10⁻¹⁶ |
| XVII § 5 | `recursion_argent.py` § 4 | `recursion_argent.md` § 4 | `q2_newton_polyedres` a, b | 1/R_eff = √2 ∓ 1 aux deux contacts ; rapport des anneaux 2,411 → √2 + 1 |
| XVIII § 6–7 | `pixels_longitudes.py` § 5–6 | `pixels_longitudes.md` § 5–6 | `r2_longitudes_lumiere` a–f | fantômes s²·m (lame) et (N/2π)(m₂, −m₁)/|m|² (étoile) ; produit s²N/2π = 1 145,9 ; flou σ = 0,7 px |
| XIX § 6 | `bases_objets.py` § 4 | `bases_objets.md` § 4 | `t2_trait_cone_thales` c, d, f | r² = w₀² + θ²z² : chèvre ∞ (col 1, pente 1), cube (1/√2, √2), laser (w₀, λ/πw₀) |
| XX § 4, 6 | `sphere_faisceaux.py` § 4, 6 | `sphere_faisceaux.md` § 4, 6 | `u2_cartes_losange` b, c, e, f | fantômes |m| = 1 à 11,46 px et |m| = √2 à 8,10 px ; distance de deux directions au hasard → √2 |
| XXVIII § 3.3 | `octaedre_perron_venn.py` § 3 (`polygone`, `tf_polygone`, `aigrettes`) | `octaedre_perron_venn.md` § 3 | `ac3_venn17` c–f | 97,74 % de lumière ; 10, 6, 14, 8, 16, 34, 18 aigrettes pour 5, 6, 7, 8, 16, 17, 18 lames |
| XXX § 1.2, 4.5, 5, 6.1, 6.3 | `centre_venn.py` § 1, 4, 5, 6 (`dipole`, `POIDS`, `harmo_cercle`, `drizzle`) | `centre_venn.md` § 1, 4, 5, 6 | `ae1` a, b ; `ae2` e, f ; `ae3` a–d | six centres de la lumière (0,61 à 46,07 px) ; 70 aigrettes = 34 + 36 ; drizzle au quart de pixel ; inversion de 16 à 21 px |
| révision | `revision_001.py` § 4.8, 4.9 | `revision_001.md` § 4.8, 4.9 | `rev001_diagonale_cadre` c | T4 : pas d'ordre de dessin (p = 0,64) ; le seuil déplace le centre de 0,044 à 27,4 px ; la moitié reste à 49,3–49,7 % |

**Les quatre chaînes, dans l'ordre.**
- **A, la lentille** : I → II → VIII → IX → X → XI → XII → XIII. De l'aire de la lentille aux zones de Fresnel, au moiré, au spectre des anneaux de Fibonacci et au Perron tourné.
- **B, le contact et les pixels** : XVII → XVIII. Les anneaux de Newton aux deux foyers, puis les fantômes de la lame de zones et de l'étoile de Siemens.
- **C, le faisceau** : XIX → XX. L'hyperboloïde, le losange de √2, les directions au hasard.
- **D, le Venn** : XXVIII → XXX. Le diaphragme à 17 lames, puis le centre, la diffraction, le drizzle et la défocalisation. XXX relie D à A (Hopkins, VIII), à B (Siemens, XVIII) et à A encore (moirés, IX, dans le § 6.1).

**Points faibles.**
- XXX ne tourne qu'avec la copie du dépôt de Dzoba. Le code de rendu de l'image à 17 courbes n'est pas publié (`grain-pixels-centres.md` § 3.5.1) : les poids de XXX § 1.2 sont mesurés, pas connus.
- Le seuil de 0,6416 λ (VIII § 3) est donné « sans référence trouvée » : je le confirme (§ 3.1).
- Le « 93 % » de XXX § 6.3 ne teste pas ce qu'il annonce (§ 6.2).
- Trois fois, un seuil de visualisation fabrique un motif : le trou de X § 1 (seuil de rayon 3), le dipôle du masque de XXX (seuil de clarté), le 93 % (taux de base).

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 Ce qui est établi

- **Classique, recalculé ici** : FTM50 : ν₅₀ = 0,40397275329955 ν_c (`resultats.md` § 6 : 0,4039727533) ; Airy : 50 % à 0,534832 λN, premier anneau noir à 1,21967 λN avec 83,78 % ; éclipses : 32,6 % à 44,5 % pour Lune/Soleil de 0,90 à 1,08 (centre lunaire au bord) ; lumière du 17-gone 0,977388 ; cos⁴ 67,5° = 0,021447, soit 5,54 crans ; Newton : 0,768 mm ; (128/125)·lumière = 1 en N = 16,6959.
- **Calculé ici, confirmé** : la FTO défocalisée devient négative à partir de W₂₀ = 0,6416294 λ (VIII § 3 : 0,6416 λ). Deuxième méthode, indépendante : l'autocorrélation FFT de la pupille exp(2πi·W₂₀ρ²) donne 0,642 λ, à la précision de la grille. Mes recherches ne trouvent pas cette valeur publiée ; Hopkins (1955) est bien *Proc. R. Soc. A* 231, 91–103 (à vérifier : sa convention de W₂₀).
- **Démontré ici** : pour tout masque de N zones égales, I(N − u) = I(u) sur l'axe (fiche proposée N2) ; K2 pour N = 3 à 20 (§ 5.1).
- **Calculé** : le modèle de T4 (§ 3.3).

**Ce qui reste ouvert.**
- Le bras de levier G du dipôle : 379 px mesurés contre 181 à 260 ajustés (`grain-pixels-centres.md` § 3.7).
- La zone d'inversion de l'étoile de Siemens du Venn : prévue de 9,7 à 17,7 px, vue de 16 à 21 px (§ 5.2, § 6.1 N4).
- Les 17 couleurs comme 17 éclairages structurés, au-delà du facteur 2 du drizzle (XXX § 6.1, « non tenté »).
- Les constantes de la forme de Newton (f², R², ½, s²N/2π, R²/2) : reliées seulement par le cercle R/√2 pour deux d'entre elles (XXX § 3).

### 3.2 Les analogies physiques, une par une (question 2)

Pour chaque ligne : ce qui est **partagé exactement**, ce qui est **transporté**, ce qui reste **ouvert** (CLAUDE.md, § 1).

| analogie (où) | partagé exactement | transporté | ouvert |
|---|---|---|---|
| Anneaux de Newton (I § 6.1 ; XVII § 5) | lame d'air t = ρ²/2R_eff, 1/R_eff = 1/R₁ − κ₂ ; anneaux sombres ρ_m = √(mλR_eff), aires égales πλR_eff (classique) | contact de la chèvre : 1/R_eff = √2 ∓ 1, rapport des anneaux √2 + 1 ; l'anneau 2^j est à (√2)^j : les crans | aucune expérience (deux sphères, pas deux disques) ; pas d'anneaux en dimension n |
| Éclipses (I § 6.3 ; XIX § 7) | obscuration = F(δ, k) ; quatre contacts = tangences ; cônes d'ombre = tangentes communes ; Thalès (sou à 2,11 m) | la configuration de la chèvre exige Lune/Soleil = 1,1587 ; le réel plafonne à 1,06–1,08, soit 32,6 à 44,5 % | catalogue réel des éclipses non utilisé : à calculer |
| FTM (I § 6.4 ; VIII § 3 ; XXX § 4.5) | FTM = aire commune de deux pupilles décalées = lentille de la chèvre ; FTM50 : Kepler, e = 1 | « la moitié de l'aire du disque » est le critère de netteté ; 92 cycles/mm à f/8 | FTM50 en dimension n (dossier moitiés, N3) ; aucun mécanisme commun avec le Venn |
| Fresnel (VIII § 2, 4, 7) | retard r²/2f ; zones √(kλf), aires égales ; I = 4 sin²(πu) ; lame de zones : foyers ±f, 1/π² chacun | lentille de Fibonacci à deux foyers (u₁ + u₂ = N) ; facettes géodésiques (0,29 R/ν²) | « un seul mécanisme » (VIII § 9) : cinq égalités, pas de théorie ; facette « en phase » : ν ≈ 1 500 |
| Œil de poisson de Maxwell (VIII § 5 ; X § 6) | n = n₀/(1 + r²/R²) : rayons = grands cercles de la sphère ; P′ = −R²P/|P|² (7·10⁻⁸ sur 18 rayons) | l'inversion x·x′ = R² : jumeaux, stéréographie (rayon √2) ; jumeau hyperbolique 2/(1 − r²) | imagerie parfaite au-delà de la diffraction (Leonhardt, 2009) : discutée, non utilisée |
| Deschamps (XIX § 6) | r² = w₀² + θ²z² = θ²\|z + iz_R\|² ; chèvre ∞ : ρ = \|d + i\| ; cube : √2\|z + i/2\| ; w₀θ = λ/π | piquet sur la clôture = distance de Rayleigh : largeur √2·w₀, phase de Gouy 45° | mécanisme physique de la chèvre : non affirmé ; col g_n (dossier corde, F5) |
| Self (XXI § 3) | à z_R : aire × 2, intensité au centre ÷ 2 ; x′ = f²x/(x² + z_R²) donne x·x′ = f²/2 (vérifié) | le ½ des jumeaux d·d′ = ½ ; le cran √2 | le « produit de Newton » est celui de Self, pas celui de la chèvre : même ½, autre objet (dossier moitiés, N10) |
| Wielen (XXX § 1.2) | photocentre = barycentre pesé par les flux de la bande ; changer de bande le déplace | le dipôle H₁ des poids ; six pesées, 0,61 à 46,07 px | le bras de levier G ; un second canal (le seuil) ; la source de l'idée (§ 6.2) |
| HD (XXX § 1.2) | géométrie symétrique + poids inégaux → dipôle : H₂ rien, HD (5,85 ± 0,17)·10⁻⁴ D (Trefler et Gush, 1968) | le schéma qualitatif | mécanisme autre (électrons et noyaux) ; rapport au calcul « naïf » : à calculer |
| Hopkins (VIII § 3 ; XXX § 6.3) | FTO défocalisée = TF de la lentille ; négative dès 0,6416 λ ; limite géométrique 2J₁(x)/x | étoile de Siemens à m rayons : inversion entre m·b/7,016 et m·b/3,832, soit 9,7 à 17,7 px pour m = 17 et b = 4 | vue de 16 à 21 px ; le « 93 % » ne teste rien (§ 6.2) ; varier b et m |
| Drizzle (XXX § 6.1) | échantillonnages décalés de quantités connues → échantillonnage fin (Fruchter et Hook, 2002) ; ici les 17 rotations | centre au quart de pixel ; 1 px d'erreur : 50,2 % d'incohérence ; environ 2 courbes de plus (18,99 → 20,85 à 2 000 px) | les 17 couleurs au-delà du facteur 2 : non tenté |
| Gustafsson (XXX § 6.1) | motifs d'éclairage connus (les moirés de IX) ramènent les hautes fréquences dans la bande ; × 2 (2000) | même plafond que le sinc du pixel (zéro à 1 cycle/px) | microscopie non linéaire (Gustafsson, 2005), au-delà de × 2 : non utilisée |
| Friedel (XXX § 5) | image réelle ⇒ \|F(k)\| = \|F(−k)\| ; avec l'ordre 17 : C₁₇ × C₂ = C₃₄ ; encre : 17, 34, 51, 68 ; spectre : multiples de 34 | l'ordre 2N du spectre (K2) | une phase impaire casse la symétrie (N9) ; les 36 aigrettes intérieures (+4,0°) |
| Planck (XX § 8) | rien : postulat (CLAUDE.md, § 7) ; arithmétique : 10⁻⁵⁰ m = 6·10⁻¹⁶ ℓ_P ; photon de 2·10²⁵ J, r_s = 3·10⁻¹⁹ m ; r_s = λ vers √(4π) ℓ_P | ce que le postulat implique (50 chiffres, 2·10⁵⁰ dimensions) | aucune conséquence mesurable : rien à tester |
| IA (XX § 6) | cos entre deux directions ∝ (1 − t²)^((d−3)/2) ; plat en 3D (Archimède) ; distance → √2 (1,275 en d = 2 ; 1,414 en d = 4 096) | la chèvre ∞ : √2, distance typique de deux notions sans rapport | plongements réels anisotropes : distance < √2 avant centrage (N7) |

### 3.3 T4 : une cause (la palette) ou deux (palette et ordre de dessin) ? (question 5)

**Déjà fait ailleurs.** `resultats/revision_001.md` § 4.8–4.9 (classes de teinte, aires visibles, balayage du seuil) et `grain-pixels-centres.md` § 3.5 (témoins, contraste d'ordre, palette isoluminante). Ici : le modèle, ses prédictions, et mon ajustement sur les six écarts de `resultats/centre_venn.md` § 1.

**Le modèle.** La courbe i est la rotation de 2πi/17 de la courbe 0 (T4 : les phases des 17 moments ne s'étalent que de 6° à 7°). Chaque courbe a un poids w_i (sa couleur, selon la pesée) et une aire visible A_i. Avec ω = e^(2πi/17) et H₁(v) = Σ vᵢωⁱ/Σ vᵢ, le centre de la lumière est à G·H₁(w·A) du centre de symétrie, G étant un bras de levier complexe commun. Au premier ordre :
- **une cause** : écart = G·H₁(w) ;
- **deux causes** : écart = G·[H₁(w) + H₁(A)] = G·H₁(w) + X.
- Un masque binaire pèse 1 tout pixel d'encre : H₁(w) = 0, et l'union de l'encre ne dépend pas de l'ordre. Les deux modèles prédisent donc 0 pour les deux masques, vus à 1,26 et 13,58 px : les masques ne parlent que du seuil (`revision_001.md` § 4.9).

**Une cause, avec les couleurs mesurées** (calculé hors dépôt sur `venn17-pressure-dark-2000.png`, quatre estimations des 17 couleurs ; poids = F − fond ; un seul G ajusté sur Y, L, moyenne RGB et énergie) :

| couleurs estimées par | G (px) | résidu RMS, une cause | résidu RMS, deux causes | X (px) | dipôle d'aires nécessaire |
|---|---:|---:|---:|---|---:|
| A : 5 % les plus clairs (script XXX) | 263 à −88° | 6,4 | 3,9 | 7,9 à −71° | 2,8 % |
| B : 5 % les plus saturés | 252 | 10,1 | 3,4 | 11,7 à −128° | 5,3 % |
| C : 10 % les plus saturés | 247 | 11,3 | 4,1 | 13,1 à −124° | 5,9 % |
| D : 50 % les plus saturés | 190 | 14,9 | 6,8 | 19,0 à −109° | 9,3 % |

- **Non, une cause ne suffit pas avec ces couleurs.** Avec A, l'énergie (46,9 px prédits, 46,1 observés) et la moyenne RGB (27,1 contre 33,1 px) sont retrouvées, avec les bonnes directions (à 3° près). La clarté L a le bon module (5,1 contre 4,5 px) mais pas la direction (−178° contre −134°). **La luminance Y échoue** : 10,8 px à +136° prédits, 0,61 px à −172° observés. Pour 0,61 px avec G ≈ 260 px, il faudrait |H₁(Y)| ≈ 0,23 % ; les couleurs mesurées en donnent 4,1 % (jusqu'à 12,5 %).
- **Test sans bras de levier.** Le rapport des écarts Y/E vaut 0,0132 (0,61/46,07). Les dipôles mesurés prédisent 0,23, soit 17 fois plus ; une luminance constante prédirait 0,003 (`grain-pixels-centres.md` § 3.5.4). Les directions relatives, libres de G, échouent aussi : Y et L sont à 55° et 47° de la prédiction.
- **Avec deux causes**, le résidu baisse (3,4 à 6,8 px), mais X change de direction d'une estimation à l'autre (−71° à −128°), et il lui faudrait un dipôle d'aires de 2,8 à 9,3 %. X absorbe surtout l'erreur d'estimation des couleurs. Le sens de la rotation (ωⁱ ou ω⁻ⁱ) ne change pas le résidu à une cause (6,3 px dans les deux cas) : les phases de H₁ sont fragiles, le modèle repose sur les modules.

**Ce que le modèle à deux causes prédit pour la luminance.** Y = G·[H₁(Y) + H₁(A)]. Pour 0,6 px, l'ordre doit annuler le dipôle de luminance : H₁(A) ≈ −H₁(Y), soit 4,1 % en module (estimation A). Pour des aires qui montent de la première à la dernière courbe dessinée, A_i = A₀(1 + a(i − 8)/8) et H₁(A) = (a/8)/(ω − 1), de module 0,340·a et de phase −100,6° + 21,18°·k (k : indice de la première courbe dessinée). Il faut donc a ≈ 12 % : la dernière courbe aurait 27 % d'aire visible de plus que la première. La phase dépend de k, donc elle ne départage pas ; le module et la montée, si.

**Ce que T4 mesure.** Pas d'ordre : la meilleure montée cyclique des A_i reste dans le nul (p = 0,64 et 0,19). Contraste d'ordre C = −6,0 ± 1,5 %, comme les témoins sans ordre (−6,4 ; −8,0), contre +14,8 et +8,6 % pour deux PNG du traceur rendus de 0 à n − 1 (`grain-pixels-centres.md` § 3.5.3). Le seuil déplace le centre de 0,044 px (sans seuil) à 27,4 px (t = 0,40) ; la moitié reste à 49,3–49,7 %.

**Verdict sur K6.** L'ordre de dessin est écarté. La seconde cause du plan est la palette elle-même : une palette presque isoluminante (Y₀ de 0,30 à 0,36) redonne les quatre pesées à 1,4–2,0 px, et le seuil la révèle (une clarté constante ne produirait aucun effet de seuil). Les « 5 % de pixels les plus clairs de chaque teinte » biaisent les poids : l'inversion de K6 vient de ce choix, pas de la physique. Reste ouvert : la palette réelle et le code de rendu, que le dépôt de Dzoba ne publie pas (`plotter_svg.py` écrit les courbes de 0 à n − 1 avec L = 0,58 par défaut, mais l'image à 17 courbes n'en vient pas).

## 4. Les fiches du dossier : verdict, test, et la partie qui portait déjà le lien

### 4.1 Fiche 002 : (128/125) × la lumière du 17-gone ≈ 1, à 845 ppm

- **Verdict : hasard, avec sa loi.** (128/125)·sinc(2π/N) = 1 en N = 16,6959 (vérifié) ; la pente vaut 2,7·10⁻³ par unité de N ; l'entier le plus proche, 17, est à 0,304. Pour une constante prise au hasard, le zéro tombe aussi près d'un entier avec la probabilité 0,61 : la distance en ppm d'un tel passage est uniforme sur [0 ; 1 400 ppm environ], et 845 est au rang 0,6 (calculé hors dépôt). Fiche proposée N8.
- **Test.** Variation du paramètre (déjà dans la fiche : « N = 16,70 ») et ce calcul de probabilité.
- **La partie qui portait le lien.** XXVIII § 3.3 pour la lumière (97,74 %, 2π²/(3·17²), 0,033 cran) ; XXVI § 2.5 pour le diésis ; XXIX § 5.5 et XXX § 7 pour le test.
- **Place dans l'arbre P3.** Oui pour *la lumière* : 1 − sinc x = x²/6 − x⁴/120 + …, avec x = 2π/N, est l'intégrale d'un profil de courbure ½ (0,022612 exact, 0,022767 pour x²/6 : 0,7 % d'écart). Le *diésis* est du triangle P6 (troisième écart des trois distances, `bases-congruences-premiers.md` N6) ; le *verdict* est celui de P7. La fiche est un nœud de trois arbres ; seul P3 la porte par un calcul de la partie.
- **Dimensions** : D7, D4, D2.

### 4.2 Fiche 006 : le centre de la lumière bouge selon la façon de la peser

- **Verdict : structure, causalité précisée.** L'analogie du photocentre tient : partagé exactement, le barycentre pesé (H₁) ; transporté, l'écart entre deux pesées révèle l'inégalité des poids ; ouvert, le bras de levier. La causalité change : ni l'ordre de dessin (écarté), ni les couleurs mesurées (qui donnent une luminance 17 fois trop grande) ; la palette de conception, presque isoluminante, et le seuil (§ 3.3).
- **Test.** Mesure contre le budget (0,003 px : les six écarts sont des mesures), puis T4.
- **La partie qui portait le lien.** XXX § 1.2 (Wielen, HD) ; la correction de la chaîne est dans `revision_001.md` § 4.8–4.9.
- **Place dans l'arbre P8.** Elle n'y est pas à sa place. Le triangle de P8 est un cône à sommet imaginaire (col, pente, distance de Rayleigh) ; le photocentre n'a rien de tel. Le plan le soupçonnait (§ 2.2, « ma lecture »). **Je propose de détacher la branche « photocentre » de P8** et d'en faire un neuvième triangle, « le barycentre pesé » (H₁ : binaire, HD, Venn), posé en D8 contre D3. La fiche 006 reste aussi sur la branche des biais de chaîne de P7 (007 → 006 → T4).
- **Dimensions** : D3, D8, D7.

### 4.3 Fiche 009 : le Venn diffracte comme un diaphragme à 17 lames, 34 + 34 aigrettes

- **Verdict : structure, et cas de K2.** Les 34 aigrettes du contour sont l'orbite d'une direction sous ⟨2π/17, π⟩ (§ 5.1). « Friedel double l'ordre » n'est exact que pour N impair : pour N pair, le demi-tour est déjà dans le groupe. Un Venn symétrique à n ≥ 3 courbes a n premier, donc impair (Henderson, 1963) : le spectre a toujours l'ordre 2n (22, 26, 34, 38, 46 pour 11, 13, 17, 19, 23). Les 36 aigrettes intérieures sont une seconde orbite du même groupe, avec sa phase propre : +4,0° d'un côté, −6,6° de l'autre, et 4,0 + 6,6 = 10,6 = 180°/17.
- **Test.** Séparer les sources (déjà fait : contour seul 34, cœur seul 85 % dans la seconde famille) et K2 (N = 3 à 20).
- **La partie qui portait le lien.** XXVIII § 3.3–3.4 (les 34 aigrettes, les 17 éventails) et XXIX § 5.4 (le 34-gone de l'ombre).
- **Place dans l'arbre P1.** Par K2, pas par la branche du cube. Les 34 aigrettes de la fiche viennent du *contour* de l'image, un 17-gone choisi par le dessin (XXIX § 1.2) ; le 34-gone de l'ombre Σωⁱ est un autre objet, régulier, de côté 1, qui a les mêmes directions. Les deux sont des orbites du même groupe : la fiche est sur la branche de la parité, à ajouter à P1 comme « section globale ».
- **Dimensions** : D4, D6.

## 5. Les congruences et les obstructions

### 5.1 K2 : les trois 34, vérifiés pour N = 3 à 20 (question 4)

**Résultat** (calculé hors dépôt, 25 s ; aigrettes par la transformée de Fourier exacte du N-gone, comme XXVIII § 3.3) :

| N | aigrettes | côtés de l'ombre Σωⁱ | éventails de Perron, recouvrement min–max |
|---|---:|---|---|
| 3, 5, …, 19 (impairs) | 2N | 2N, tous de longueur 1 | 1–1 : chaque direction une fois |
| 4, 6, …, 20 (pairs) | N | N, tous de longueur 2 | 0–2 : la moitié des directions deux fois, l'autre jamais |

Les 18 valeurs de N suivent la règle (exemples : 6, 10, 34, 38 aigrettes pour 3, 5, 17, 19 lames ; 4, 6, 18, 20 pour 4, 6, 18, 20). Les arêtes de l'ombre sont égales à 10⁻⁶ près : c'est un polygone régulier. XXVIII § 3.3–3.4 avait 7 valeurs pour les aigrettes et N = 16, 17 pour les éventails ; XXIX § 5.4 avait N = 17 pour l'ombre.

**Pourquoi (démontré).** Les trois objets comptent l'orbite d'une direction sous le groupe engendré par la rotation 2π/N et le demi-tour. Pour N impair, −1 n'est pas une racine N-ième de l'unité : μ_N ∪ (−μ_N) = μ_2N, donc 2N directions (ce groupe est cyclique d'ordre 2N, car 2 est inversible modulo N). Pour N pair, −μ_N = μ_N : N directions.
- Les aigrettes sont perpendiculaires aux côtés d'un polygone convexe, des deux côtés.
- Les côtés de l'ombre sont les vecteurs ±ωⁱ.
- Les axes des éventails sont 2πj/N modulo π, soit π·(2j mod N)/N.

**Friedel, même chose.** L'encre a des harmoniques multiples de N, et la réalité de l'image ajoute le demi-tour : C_N × C₂. Pour N impair, c'est C_2N ; pour N pair, c'est C_N, et le doublement est invisible.

**Obstruction : aucune** pour une ouverture réelle. C'est une section globale, vraie sur trois dossiers (lumière, aiguilles, ombres). Réserve : avec une phase, une ouverture sans centre de symétrie (N impair) perd la symétrie centrale du spectre ; le nombre de directions reste 2N, les deux bouts d'une aigrette deviennent inégaux (N9).

### 5.2 Mes congruences et obstructions

- **L1, la forme de Newton, cinq fois** (VIII § 5, IX § 3, XVII § 3, XVIII § 6, XXX § 3). *Se recolle* : chaque fois une inversion x ↦ c/x, avec retournement dans l'œil de poisson. Les constantes : f² (lentille ; limite φ² et φ avec f = 1, (φ² − 1)(φ − 1) = 1), R² (Maxwell), ½ (jumeaux), s²N/2π (fantômes), R²/2 (complément). *Obstruction* : aucune condition de cocycle ne relie ces constantes ; composer deux inversions de même centre et de rayons a et b est une homothétie de rapport (b/a)², pas l'identité. Établi : le complément et les jumeaux ont le même cercle fixe R/√2 (XXX § 3). Ouvert : y rattacher la lentille, Maxwell et les fantômes. Fiche proposée N6.
- **L2, crans et anneaux.** Les diaphragmes f/1, 1,4, 2, 2,8 sont les rayons des anneaux de Newton 1, 2, 4, 8 (ρ_m² ∝ m) : même loi, aire proportionnelle. *Obstruction* : les crans comptent en binaire, les niveaux du Venn en binomiale (XXX § 4.1) ; ils ne coïncident qu'au premier cran.
- **L3, Hopkins et Siemens.** La FTO défocalisée se recolle à 2J₁(x)/x quand W₂₀ grandit (VIII § 3 : premiers zéros 0,3049, 0,2033, 0,1525, 0,0762 contre 0,300, 0,193, 0,084 pour W₂₀ = 0,75, 1, 2 λ). *Obstruction* : sous 0,6416 λ, aucun zéro ; et, dans le Venn, la zone d'inversion est décalée vers l'extérieur (16–21 px contre 15–17,7 px visibles au-delà du trou). Ma lecture : les veines ne sont pas radiales ; leur vecteur d'onde a une composante radiale, donc |k| ≥ N/(2πr), et le même x = 2π|k|b arrive à un r plus grand. Test : une étoile de Siemens exacte, puis une spirale (N4).
- **L4, K6** : voir § 3.3. Les sections locales (une pesée chacune) se recollent avec un seul G si la palette est isoluminante ; l'obstruction qui reste est celle des masques (le seuil).

## 6. Les trous

### 6.1 Les trous du recueil : fiches nouvelles proposées (question 3 : les trois premières relèvent de D8)

Chaque fiche : type ; statut ; partie ; script et section ; image ; dimension.

**N5. Le photocentre de N sources symétriques est G·H₁(poids) ; N = 2 redonne le déplacement des étoiles doubles** (D8, puis D3).
Analogie ; structure ; XXX § 1.2 ; `centre_venn.py` § 1 (`dipole`, `POIDS`), `revision_001.py` § 4.8 ; `ae1_centre_moitie.png` a, b.
Pour N sources aux sommets d'un polygone régulier, le barycentre est G·H₁(w), avec H₁ = Σwᵢωⁱ/Σwᵢ. Pour N = 2, H₁ = (w₀ − w₁)/(w₀ + w₁) et G = a/2 : c'est le photocentre d'une binaire (Wielen). Le test de ce schéma est le rapport de deux pesées, libre du bras de levier : Y/E observé 0,0132, prédit 0,23 par les couleurs mesurées et 0,003 par une palette isoluminante ; les directions relatives libres de G échouent de 55° (Y) et 47° (L) avec les couleurs mesurées. Répliquer : les binaires CID de SDSS (Pourbaix et al., 2004), décalages entre bandes contre fractions de flux : à calculer.

**N7. Deux directions au hasard sont à √2 : exact en isotrope, faux pour les plongements réels** (D8, puis D1).
Analogie ; à tester ; XX § 6 ; `sphere_faisceaux.py` § 6 ; `u2_cartes_losange.png` f.
La densité du cosinus est ∝ (1 − t²)^((d−3)/2) ; la distance moyenne vaut 1,275 (d = 2), 1,327 (3), 1,397 (10), 1,413 (100), 1,414 (1 000) (`sphere_faisceaux.md` § 6). Les plongements réels sont anisotropes (Ethayarajh, 2019 ; Mu et Viswanath, 2018 : un vecteur moyen commun) : le cosinus moyen de deux mots au hasard n'est pas nul et la distance est sous √2 avant centrage. Test : répliquer sur un objet indépendant (CLAUDE.md, § 10), c'est-à-dire mesurer la moyenne et la dispersion des cosinus de paires au hasard dans un plongement réel, avant et après centrage, contre 0 ± 1/√d : à calculer.

**N9. Friedel et Bijvoet : le doublement 17 → 34 exige une ouverture réelle** (D8, puis D4, D6).
Analogie ; à tester ; XXX § 5 ; `centre_venn.py` § 5 (`harmoniques`) ; `ae2_diaphragmes_diffraction.png` f.
Le spectre d'une image réelle est centrosymétrique (Friedel, 1913), d'où les multiples de 34 (K2). En cristallographie, la diffusion anomalale rend les facteurs complexes et sépare les paires de Friedel (différences de Bijvoet). Test : donner à un 17-gone une phase de défocalisation (W₂₀ = 1 λ) et mesurer l'harmonique angulaire 17 de |F|² : nulle pour une ouverture réelle, non nulle avec la phase. À calculer.

**N1. Les trois 34 sont un seul fait : C_N × {±1} est cyclique d'ordre 2N si et seulement si N est impair** (D6, D4, D5).
Analogie ; exact ; XXVIII § 3.3–3.4, XXIX § 5.4, XXX § 5 ; `octaedre_perron_venn.py` § 3 (`polygone`, `tf_polygone`, `aigrettes`), test au § 7 ; `ac3_venn17.png` d, e, f.
Voir § 5.1. Test : variation de N (3 à 20, fait). Avec Henderson : un Venn symétrique a un spectre d'ordre 2n.

**N2. Tout masque de N zones égales a ses foyers par paires, I(N − u) = I(u)** (D4).
Fait amusant ; exact ; VIII § 7 et IX § 3 ; `foyer_fibonacci.py` § 7 (`intensite_axe`, `deux_foyers`) ; `h2_fibonacci.png` b.
Sur l'axe, en approximation de Fresnel, I(u) = 4 sin²(πu/N)·|Σ_k t_k e^(2iπu(k + ½)/N)|². Quand u devient N − u, le sinus ne change pas et la somme devient moins son conjugué : l'égalité vaut pour tout masque (vérifié sur 2 000 masques, 3·10⁻¹²). La symétrie ne vient donc pas de Fibonacci : VIII § 7 lit dans F_(j−2) + F_(j−1) = F_j « la condition » de la symétrie. La lame de Fresnel est le point fixe u = N/2 ; ce que Fibonacci fait de propre, c'est deux pics égaux près de F_(j−2) et F_(j−1) (21,0840 et 33,9160 pour 55 anneaux). Test : identité (précision) et variation du masque.

**N3. Le contraste d'une pupille circulaire défocalisée s'inverse à partir de W₂₀ = 0,6416 λ** (D4, D8).
Fait amusant ; calculé (intégrale de Hopkins : 0,6416294 λ ; autocorrélation FFT : 0,642 λ) ; VIII § 3 ; `foyer_fibonacci.py` § 3 (`ftm`, `ftm_min`) ; `h1_foyer_menisques.png` d.
Le premier changement de signe est vers ν/ν_c ≈ 0,489, avec la convention φ = 2πW₂₀ρ². Aucune valeur publiée trouvée ; la convention de Hopkins est à vérifier. Test : pousser la précision (identité) et changer de convention.

**N4. Le « 93 % » de la défocalisation du Venn est le taux de base d'un prédicteur constant** (D7, puis D4).
Hasard ; calculé (arithmétique sur `centre_venn.md` § 6 ; à refaire avec les tableaux) ; XXX § 6.3 ; `centre_venn.py` § 6 (`harmo_cercle`, `GAIN`, `ACC_SIGNE`) ; `ae3_grains_hasard.png` d.
76 rayons fiables, de 15 à 90 px ; zone d'inversion mesurée de 16 à 21 px, donc au plus 6 rayons négatifs. Prédire « positif » partout est juste sur au moins 70 rayons de 76 (92 %) ; le modèle de Hopkins fait 93 %. Le phénomène est réel (une couronne de contraste inversé), la statistique ne le teste pas. Test : varier b (2, 4, 6, 8 px) et l'harmonique (17, 34, 51, d'amplitudes 0,026, 0,015, 0,018) : la couronne doit suivre r ∈ (m·b/7,016 ; m·b/3,832). Répliquer sur les dessins à 11 et 13 courbes du dépôt de Dzoba.

**N6. La forme de Newton x·x′ = c revient cinq fois** (D4, D1, D6).
Analogie ; exact ; VIII § 5, IX § 3, XVII § 3, XVIII § 6, XXX § 3 ; `foyer_fibonacci.py` § 5, `moire_fibonacci.py` § 4, `recursion_argent.py` § 2, `pixels_longitudes.py` § 5, `centre_venn.py` § 3 ; `r2_longitudes_lumiere.png` a, b, d.
Voir § 5.2, L1. Test : variation de s, N, f (déjà dans les scripts).

**N8. Le ppm d'un passage par 1 d'une famille continue est uniforme : les 845 ppm de la fiche 002 sont au rang 0,6** (D7, D4).
Hasard ; calculé ; XXIX § 5.5, XXX § 7 ; `revision_001.py` (à ajouter), `centre_venn.py` § 7 (`varie`) ; `ae3_grains_hasard.png` f.
Voir § 4.1. Le test de variation du paramètre donne une probabilité exacte pour toute constante comparée à une famille indexée par un entier. À refaire sur les 31 constantes de XXIX § 5.5 : à calculer.

### 6.2 Les trous du corpus : erreurs et imprécisions trouvées

- **« 93 % des signes » (XXX § 6.3 et « En bref » ; CLAUDE.md, § 6, « inversion aux zéros de J₁ (93 %) »).** C'est le taux de base (N4). À réécrire : « une couronne inversée de 16 à 21 px, prévue de 9,7 à 17,7 px ».
- **Titre de Wielen (1996), `centre-venn.md`, Sources.** Le titre donné (« Detecting and analyzing double stars by their color-induced displacement ») n'est pas celui de *A&A* 314, 679 : « Searching for VIMs: an astrometric method to detect the binary nature of double stars with a variable component » (recherche web de l'agent ; à vérifier sur ADS). L'article traite les VIMs et les CID ; l'idée du CID est créditée à Christy et al. (1983) dans la version publiée de Pourbaix et al. (2004), à Wielen dans sa version arXiv. À écrire : « Wielen (1996) ; idée plus ancienne (à vérifier) ».
- **`README.md`, § 7 : « Analogies, pas équivalences … ne prouvent rien »** (le cas n = 0, la fonction de la chèvre g(x) = sin x − x cos x = x²j₁(x), le nombre d'argent). Cela contredit CLAUDE.md, § 1. À réécrire en trois temps : partagé (la fonction, l'intégrale de t sin t), transporté (les zéros de tan x = x, la diffusion par une sphère), ouvert.
- **`foyer-fibonacci.md`, § 7, dernier point : « la récurrence de Fibonacci est exactement la condition pour que les deux foyers soient symétriques ».** La symétrie vaut pour tout masque (N2). La récurrence dit où tombent les foyers, pas qu'ils sont symétriques.
- **`pixels-longitudes.md`, § 7 : « quand on l'enlève (le Nikon D800E) ».** À vérifier : à ma connaissance, la lame passe-bas n'est pas ôtée, son effet est annulé par une seconde lame.
- **K2 dans le plan, § 3.2 : « pas d'obstruction ».** Vrai pour une ouverture réelle ; la réserve de la phase est au § 5.1.

### 6.3 Les trous des données publiées (question 7)

**Gaia, la couleur et la source unique.**
- *L'observation du corpus.* Le centre de la lumière d'une figure symétrique aux poids inégaux se déplace avec la bande (XXX § 1.2 ; N5) : c'est le déplacement induit par la couleur (CID).
- *Ce que disent les sources lues* (recherche web, 2026-10-08 : extraits, pas les articles entiers).
  - Wielen (1996) : le CID demande au moins deux filtres ; le texte évoque Hipparcos et le futur Gaia pour les VIMs.
  - Pourbaix, Ivezić, Knapp, Gunn et Lupton (2004), *A&A* 423, 755 : première application réussie, sur SDSS ; 419 candidats dans la version arXiv (DR1), 346 dans la version publiée (DR2) ; la plupart ressemblent à une naine blanche et une étoile plus tardive que K7.
  - Lindegren et al. (2021), *A&A* 649, A4 : le point zéro des parallaxes de Gaia EDR3 dépend de la magnitude G, de la couleur (ν_eff pour les solutions à 5 paramètres, pseudocouleur pour celles à 6) et de la latitude écliptique ; médiane des quasars : −17 µas ; correction « provisoire », valable pour 6 < G < 21.
  - Belokurov et al. (2020, arXiv:2003.05467) : le RUWE se lit comme une amplitude de balancement entre le centre de lumière et le centre de masse, proportionnelle à la séparation pour des périodes allant jusqu'à quelques années.
- *Ce que rangent dans le bruit les catalogues à source unique* (ma lecture, à vérifier dans la documentation de Gaia).
  1. Le balancement du photocentre d'une paire non résolue : dans l'excès de bruit et le RUWE.
  2. La partie qui ne balance pas (parallaxe et mouvement propre du photocentre) : un *biais*, pas du bruit.
  3. La différence de couleur entre les composantes : l'astrométrie de Gaia est mesurée en bande G (lumière blanche, à vérifier) ; la couleur du mélange est un seul nombre (ν_eff) ; la fonction de point zéro n'a pas le RUWE parmi ses entrées (ma lecture de son interface publique). Le CID, lui, demande deux bandes.
- *Ce qui manque.* Des positions *par bande* (G, BP, RP) ou une comparaison entre bandes. Les mesures par époque de DR4 (date cible annoncée : 2 décembre 2026, à vérifier sur la page de l'ESA) seront en G.
- *Où chercher.* Les binaires résolues ou à orbite connue (binaires à éclipses de référence : Stassun et Torres, 2021, à vérifier), le CID de SDSS refait avec les positions de Gaia, et le test sans bras de levier de N5 : le rapport des décalages entre deux bandes contre les fractions de flux.

**Autres trous de mon domaine.**
- *L'IA* : l'anisotropie des plongements est publiée, le lien avec √2 ne l'est pas (N7).
- *Le drizzle* : le gain de « environ 2 courbes » (XXX § 6.4) n'est pas comparé aux limites publiées du drizzle (réglage de la taille de goutte, corrélation du bruit : à vérifier).

**Références citées** (sûre / à vérifier).
- Sûres : L. Lindegren et al., *A&A* 649, A4 (2021), DOI 10.1051/0004-6361/202039653 (numéro d'article repris du plan) ; R. Wielen, *A&A* 314, 679 (1996) ; D. Pourbaix et al., *A&A* 423, 755 (2004), DOI 10.1051/0004-6361:20040346 ; H. H. Hopkins, *Proc. R. Soc. A* 231, 91–103 (1955) ; G. A. Deschamps, *Electron. Lett.* 7, 684–685 (1971) ; S. A. Self, *Appl. Opt.* 22, 658–661 (1983) ; A. S. Fruchter et R. N. Hook, *PASP* 114, 144 (2002) ; M. G. L. Gustafsson, *J. Microsc.* 198, 82–87 (2000) et *PNAS* 102, 13081 (2005) ; Elhage et al., « Toy Models of Superposition » (2022).
- À vérifier : Belokurov et al., *MNRAS* 496 (2020), volume et pages (arXiv:2003.05467 trouvé) ; Gaia Collaboration, Arenou et al., *A&A* 674, A34 (2023) ; Halbwachs et al., *A&A* 674, A9 (2023) ; Stassun et Torres, *ApJ* 907, L33 (2021) ; Christy et al. (1983) et Sorokin et Tokovinin (1985), cités comme origine du CID par des sources secondaires ; Trefler et Gush, *PRL* 20, 703 (1968) (repris du corpus) ; G. Friedel, *C. R. Acad. Sci.* 157, 1533 (1913) (repris du corpus) ; Ethayarajh, EMNLP-IJCNLP (2019) ; Mu et Viswanath, ICLR (2018) ; Bijvoet, Peerdeman et van Bommel, *Nature* 168, 271 (1951).

## 7. Le code minimal du test qui me concerne (T4, côté « deux causes », et K2)

T4 existe déjà dans `scripts/revision_001.py` (§ 4.8–4.9). Voici ce qui s'y ajoute, testé hors dépôt (K2 : 25 s ; ajustement : instantané ; seuil de Hopkins : 1 s), sans résultat écrit.

```python
import math, numpy as np
from scipy import integrate, optimize
from scipy.spatial import ConvexHull

# K2 : N = 3..20. Attendu, pour les trois objets : N pair -> N ; N impair -> 2N.
def aigrettes(N, K=400.0, nth=36000):                    # TF exacte du N-gone (somme sur les côtés)
    t = math.pi/2 + 2*math.pi*np.arange(N)/N; P = np.c_[np.cos(t), np.sin(t)]
    Th, Rs = np.meshgrid(np.linspace(0, 2*math.pi, nth, endpoint=False), np.linspace(.8*K, 1.2*K, 41))
    KX, KY = Rs*np.cos(Th), Rs*np.sin(Th); F = 0
    for j in range(N):
        a, b = P[j], P[(j+1) % N]; e = b-a; lg = math.hypot(*e); u = e/lg; n = np.array([u[1], -u[0]]); m = (a+b)/2
        F = F + (KX*n[0]+KY*n[1])*lg*np.exp(-1j*(KX*m[0]+KY*m[1]))*np.sinc((KX*u[0]+KY*u[1])*lg/(2*math.pi))
    p = (np.abs(F/(KX**2+KY**2))**2*Rs**2).mean(0)
    return int(((p > np.roll(p, 1)) & (p >= np.roll(p, -1)) & (p > .2*p.max())).sum())

def cotes_ombre(N):                                      # côtés du contour de S -> somme des ω^i, i dans S
    z = np.zeros(1, complex)
    for x in np.exp(2j*np.pi*np.arange(N)/N): z = np.r_[z, z+x]
    v = np.c_[z.real, z.imag]; v = v[ConvexHull(v).vertices]; cr = lambda a, b: a[0]*b[1]-a[1]*b[0]
    return sum(abs(cr(v[k]-v[k-1], v[(k+1) % len(v)]-v[k])) > 1e-9 for k in range(len(v)))

def eventails(N, ech=20000):                             # N éventails d'ouverture π/N aux angles 2πj/N, modulo π
    th = (np.arange(ech)+.5)/ech*math.pi
    m = sum(np.abs(((th-(2*math.pi*j/N) % math.pi+math.pi/2) % math.pi)-math.pi/2) < math.pi/(2*N)-1e-12 for j in range(N))
    return int(m.min()), int(m.max())                    # N impair : (1, 1) ; N pair : (0, 2)

# T4 : une cause ou deux. COUL, FONDS : comme dans centre_venn.py § 1 ; ECART : écarts observés (x + i·y, y vers le haut)
# pour 'Y', 'L', 'mo', 'E' (resultats/centre_venn.md § 1).
OM = np.exp(2j*np.pi*np.arange(17)/17)
h1 = lambda w: (np.asarray(w, float)*OM).sum()/np.sum(w)         # premier harmonique complexe des poids

def deux_causes(COUL, FONDS, ECART):
    ks = ("Y", "L", "mo", "E"); fo = dict(Y=FONDS["Y"], L=FONDS["L"], mo=FONDS["MO"], E=FONDS["E"])
    h = np.array([h1([c[k]-fo[k] for c in COUL]) for k in ks]); o = np.array([ECART[k] for k in ks])
    G1 = (h.conj()*o).sum()/(abs(h)**2).sum()                    # une cause : obs = G·H1
    A = np.c_[h, np.ones(4)]; (G2, X), *_ = np.linalg.lstsq(A, o, rcond=None)    # deux causes : obs = G·H1 + X
    rms = lambda r: math.sqrt((abs(r)**2).mean())
    return dict(H1=h, G=G1, rms1=rms(G1*h-o), G2=G2, X=X, rms2=rms(A@[G2, X]-o), H1_aires=X/G2,
                # ordre 0 -> 16, A_i = A0(1 + a(i-8)/8) : H1(A) = (a/8)/(ω-1), module 0,340·a, phase -100,6° + 21,18°·k
                phases_scie=[math.degrees(np.angle(np.exp(2j*np.pi*k/17)/(OM[1]-1))) for k in range(17)])
# À brancher sur revision_001.py § 4.8 : H1 des aires visibles A_i (module ET phase), et le rapport
# |ECART['Y']| / |ECART['E']| contre |H1[Y]| / |H1[E]| (libre du bras de levier).

# N2 : I(N-u) = I(u) pour tout masque t de N zones égales (preuve : S(N-u) = -conj S(u)).
def I_axe(t, u):
    S = (t[None, :]*np.exp(2j*np.pi*np.outer(u, np.arange(len(t))+.5)/len(t))).sum(1)
    return 4*np.sin(np.pi*u/len(t))**2*np.abs(S)**2

# N3 : seuil d'inversion de la FTO défocalisée (Hopkins). Contrôle : autocorrélation FFT de exp(2πi·W20·ρ²) sur un disque.
def fto(d, w20):                                         # d = 2ν/ν_c ; lentille = deux disques unité décalés de d
    f = lambda x: 2*math.sqrt(max(0.0, 1-(abs(x)+d/2)**2))*math.cos(4*math.pi*w20*d*x)
    return integrate.quad(f, -(1-d/2), 1-d/2, limit=400, epsabs=1e-13)[0]/math.pi

def minimum_fto(w20):
    nus = np.linspace(.01, .99, 200); v = [fto(2*n, w20) for n in nus]; i = int(np.argmin(v))
    return optimize.minimize_scalar(lambda n: fto(2*n, w20), bounds=(nus[max(i-1, 0)], nus[min(i+1, 199)]), method="bounded").fun

seuil_hopkins = lambda: optimize.brentq(minimum_fto, .60, .70, xtol=1e-7)      # le minimum change de signe au seuil
```

## 8. Les corrections au recouvrement

- **Ajouter les parties XXI et XXIX.**
  - XXI § 3 est le seul document qui traite Self (1983) : le doublement de l'aire, le ½ du produit de Newton ; la question 2 du plan le demande.
  - XXIX § 5.4 donne l'ombre Σωⁱ et son 34-gone, deuxième des trois 34 de K2 ; XXIX § 1.2 décrit la chaîne de l'image mesurée par T4.
- **Ajouter la fiche 003** (34·tan(π/34) ≈ π) : le polygone *circonscrit* à 34 côtés est le pendant de la lumière du polygone *inscrit* de la fiche 002 (mêmes N = 17 et 2N = 34) ; arbre P3 du plan.
- **Ne rien retirer.** XII n'apporte que son § 4 d'optique (les foyers 55,03 et 88,97) : lien faible mais exact. 006 et 009 gardent leur place.
- **Effet sur le nerf** (calculé hors dépôt ; mon implémentation redonne les 9 et 20 triangles vides de la v1). XXI seule fait passer les triangles vides du niveau fiches + parties de 20 à 18 ; XXIX ne change rien ; 003 laisse 9 triangles vides au niveau des fiches, mais l'un se remplit (lumière · méthode · ombres) et un autre apparaît (aiguilles · grain · lumière).
- **Arbres du plan, § 2.2.** (a) Détacher la branche « photocentre » de P8 en un triangle « barycentre pesé » (D8 contre D3). (b) Pour 002 : P3 par la lumière seule, P6 par le diésis, P7 par le verdict. (c) Pour 009 : P1 par K2. (d) Ajouter à P1 la ligne de K2, « section globale » de la parité.
