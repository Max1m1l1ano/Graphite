"""Écrit recueil/revisions/verification-croisee-001.md à partir des sorties des agents de dossier.

    python3 croisee.py resultats_1.json [resultats_2.json …]

Le bloc JSON du § 1 (le recouvrement v2) est lu par scripts/revision_001.py pour refaire le nerf ; le § 3 reprend
les lignes v2 de resultats/revision_001.md quand elles existent (relancer ce script après revision_001.py).
"""
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/user/Graphite/chevre-optique"
SORTIE = os.path.join(REPO, "recueil", "revisions", "verification-croisee-001.md")
LIEN = {"corde": "corde-et-dimensions", "moities": "moities-et-crans", "bases": "bases-congruences-premiers",
        "grain": "grain-pixels-centres", "lumiere": "lumiere-et-physique", "aiguilles": "aiguilles-kakeya-perron",
        "ombres": "ombres-cube-venn", "methode": "hasard-et-methode"}
COURT = {"corde": "corde", "moities": "moitiés", "bases": "bases", "grain": "grain", "lumiere": "lumière",
         "aiguilles": "aiguilles", "ombres": "ombres", "methode": "méthode"}
# la raison principale de chaque correction, résumée de la sortie de l'agent (champ « raisons »)
RAISON = {
    "corde": "la corde dans un polygone (II § 9), la corde de Ptolémée de 70,81° (X § 5), la récursion d'argent (XVII), "
             "le cône à sommet imaginaire (XIX § 6), le tiers de dimension (XXVII § 6) ; les fiches de K1 et K10",
    "moities": "la lunule d'Hippocrate (VI), la grille (XV), le plateau 2^(−1/n) (XVI § 3), le tableau du grain (XXIII § 4), "
               "Borel–Padé (XXV), Perron à k = 2 (XXVIII) ; Bonferroni (fiche 012)",
    "bases": "10 − 1 = 3² (VI § 3 ter), l'aiguille (3, 1) sur la grille décalée (XV § 5), le cercle de Gauss (XVIII), "
             "le comma et 19/12 (XX § 6), 3ⁿ modulo 10 (XXII), le 4/3 de 1/x₀ (XXIV) ; le diésis (fiche 002)",
    "grain": "le grain lu en longueur ou en aire (XXIV), la série coupée au mieux (XXV), Kakeya au grain δ (XXVI), "
             "l'échelle des taux de change (XXVII § 3) ; n·tan(π/n) (fiche 003)",
    "lumiere": "Self (1983) et le doublement de l'aire (XXI § 3), l'ombre Σωⁱ et son 34-gone (XXIX § 5.4) ; "
               "le polygone circonscrit (fiche 003). Corrections relevées dans son § 8 (sa sortie structurée est perdue)",
    "aiguilles": "les trois façons de retourner l'aiguille (VIII), les trois distances (XI), la demi-case de l'hexagone (XV § 5), "
                 "l'aiguille de 50 (XXI), un bit par pas (XXIX), la fiche 011 sans sa partie (XXX § 6.4) ; les aigrettes (fiche 009)",
    "ombres": "la branche Perron de l'arbre P1 part de la partie V ; la fiche 010 est retirée : le plan la range dans P2, et elle n'a"
              " de cube que le dessin",
    "methode": "les cas d'erreur de chaîne qu'il a lus ou vérifiés : l'erratum d'Ullisch et Fraser corrigé par Meyerson (I), la « quasi-coïncidence » (V), "
               "le trou qui suit le point P (X), le « 2,8 » et T5 (XIV), les trois phrases corrigées (XXII, XXIII), Borel–Padé contre la troncature (XXV) ; "
               "la fiche 006 (une causalité établie sur l'analyse). Les quatorze autres fiches sont des cas d'audit, pas des membres",
}


def charger(fichiers):
    res = {}
    for f in fichiers:
        res.update(json.load(open(f, encoding="utf-8")))
    return res


def plan_v1():
    t = open(os.path.join(REPO, "recueil", "revisions", "plan-001.md"), encoding="utf-8").read()
    m = re.search(r"```json\n(.*?)\n```", t[t.index("### 1.9"):], re.S)
    return json.loads(m.group(1))["dossiers"]


def lignes_nerf_v2():
    """Les lignes v2 du § 3 de resultats/revision_001.md (tableau et listes), si le script les a écrites."""
    p = os.path.join(REPO, "resultats", "revision_001.md")
    if not os.path.exists(p):
        return [], []
    t = open(p, encoding="utf-8").read()
    t = t[t.index("## 3."):t.index("## 4.")]
    tab = [x for x in t.splitlines() if x.startswith("| v2 |")]
    m = re.search(r"(\*\*v2 : les triangles vides.*?)(?=\n\*\*v\d|\Z)", t, re.S)
    bloc = m.group(1).rstrip().splitlines() if m else []
    return tab, bloc


def main():
    res = charger(sys.argv[1:])
    v1 = plan_v1()
    v2 = json.load(open(os.path.join(ICI, "v2.json"), encoding="utf-8"))["dossiers"]
    compact = open(os.path.join(ICI, "v2_compact.json"), encoding="utf-8").read().rstrip()
    n1p, n1f = sum(len(v["parties"]) for v in v1.values()), sum(len(v["fiches"]) for v in v1.values())
    n2p, n2f = sum(len(v["parties"]) for v in v2.values()), sum(len(v["fiches"]) for v in v2.values())
    presents = [k for k in LIEN if k in res]
    manquants = [k for k in LIEN if k not in res]
    tab, bloc = lignes_nerf_v2()
    sept = subprocess.run([sys.executable, os.path.join(ICI, "fiches_par_dimension.py")] + sys.argv[1:],
                          capture_output=True, text=True, check=True).stdout.rstrip()
    m = re.match(r"(\d+) fiches proposées par (\d+) dossiers", sept)
    n_prop = int(m.group(1))
    n_deja = sum(int(x) for x in re.findall(r"^\| D\d [^|]*\| \d+ \| (\d+) \|$", sept, re.M))
    hub = sorted({f for v in v2.values() for f in v["fiches"]},
                 key=lambda f: -sum(f in v["fiches"] for v in v2.values()))[0]
    n_hub = sum(hub in v["fiches"] for v in v2.values())

    L = []
    a = L.append
    a("# Vérification croisée de la révision 001 : le recouvrement v2, les doublons et les contradictions")
    a("")
    a("Le plan ([`plan-001.md`](plan-001.md), § 5) confiait cette vérification à un neuvième agent. Deux redémarrages du conteneur"
      " et une limite d'usage l'en ont empêché ; je l'ai faite moi-même. Je me suis servi des sorties structurées des agents de dossier"
      " (leurs corrections du recouvrement, leurs verdicts sur les fiches, leurs congruences, leurs erreurs trouvées et leurs fiches"
      " proposées) et de la lecture des dossiers. La synthèse est [`revision-001.md`](revision-001.md). Le nerf v2 est recalculé par"
      " [`scripts/revision_001.py`](../../scripts/revision_001.py), qui lit le bloc JSON du § 1.")
    if manquants:
        a("")
        a(f"*Dossiers encore en cours d'écriture : {', '.join(COURT[k] for k in manquants)}. Leurs lignes seront ajoutées.*")
    a("")
    a("## En bref")
    a("")
    n_aj_f = sum(1 for k in presents if res[k]["corrections_recouvrement"]["ajouter_fiches"])
    retraits = [(k, x) for k in presents for x in res[k]["corrections_recouvrement"]["retirer_parties"]
                + res[k]["corrections_recouvrement"]["retirer_fiches"]]
    txt_r = ("aucun n'a rien retiré" if not retraits else
             "un seul a retiré quelque chose (" + ", ".join(f"{COURT[k]} : la {'fiche' if x.strip().isdigit() else 'partie'} {x.strip()}"
                                                       for k, x in retraits) + ")")
    a(f"- **Le recouvrement v2.** Chaque agent a ajouté des parties à son dossier, {NOMBRES.get(n_aj_f, n_aj_f)} y ont ajouté des fiches,"
      f" et {txt_r}. Les huit dossiers passent de {n1p} à {n2p} appartenances de parties, et de {n1f} à {n2f} appartenances de"
      " fiches (§ 1).")
    a(f"- **{NOMBRES[len(DOUBLONS)].capitalize()} résultats ont été trouvés deux ou trois fois, chacun par son propre calcul.** Ce sont des confirmations (§ 5.1).")
    a(f"- **La fiche {hub} est la plus partagée du recueil** : {n_hub} dossiers sur 8 la contiennent dans le recouvrement v2.")
    a("- **Le nerf v2** (§ 3) : les 4 trous du corpus de v1 sont refermés ; au niveau des fiches, il reste 11 triangles vides, autant que"
      " le hasard, dont 9 passent par le dossier bases. C'est là que de nouvelles fiches compteraient le plus.")
    a("- **Trois désaccords entre agents, qui deviennent des précisions :** le « 2,8 » de Perron (une pente, pas une constante), la palette"
      " du Venn (mesurée ou de conception) et la fiche 005 (§ 5.2).")
    a(f"- **Le plan lui-même avait {NOMBRES[len(PLAN)]} erreurs,** trouvées par les agents et par les tests (§ 5.3).")
    a(f"- **{n_prop} fiches proposées**, dont {n_deja} déjà faites par la révision (un test du script ou une des fiches 016 à 021) ; elles"
      " sont classées par dimension au § 7.")
    a("")
    a("## 1. Le recouvrement v2")
    a("")
    a("| dossier | parties ajoutées | fiches ajoutées | la raison principale |")
    a("|---|---|---|---|")
    for k in LIEN:
        if k not in res:
            a(f"| [{COURT[k]}](../dossiers/{LIEN[k]}.md) | *(en cours)* | | |")
            continue
        c = res[k]["corrections_recouvrement"]
        ap = ", ".join(x.strip() for x in c["ajouter_parties"]) or "—"
        af = ", ".join(re.sub(r"\D", "", x).zfill(3) for x in c["ajouter_fiches"] if re.sub(r"\D", "", x)) or "—"
        retire = c["retirer_parties"] + c["retirer_fiches"]
        r = RAISON[k] + (f" ; retire : {', '.join(retire)}" if retire and not all(x in RAISON[k] for x in retire) else "")
        a(f"| [{COURT[k]}](../dossiers/{LIEN[k]}.md) | {ap} | {af} | {r} |")
    a("")
    a("**Une précaution.** Chaque agent a estimé l'effet de ses propres corrections sur le nerf (corde : 9 → 14 triangles vides au niveau"
      " des fiches ; grain : 9 → 6 ; aiguilles : 11 → 13 ; moitiés : 20 → 17 au niveau des fiches et des parties ; ombres : 10 → 11 en"
      " retirant la fiche 010). Ces estimations ne"
      " s'additionnent pas : chacune change un seul dossier. Le nerf v2, avec toutes les corrections ensemble, est au § 3.")
    a("")
    a("Le bloc lu par le script, au format du § 1.9 du plan :")
    a("")
    a("```json")
    a(compact)
    a("```")
    a("")
    a("## 2. Les congruences, vues par plusieurs dossiers")
    a("")
    a("Une congruence est vérifiée quand deux sections locales se recollent sur ce qu'elles partagent (revision-001.md, § 6). Ici,"
      " on regarde si les dossiers qui l'ont traitée sont d'accord.")
    a("")
    a("| | dossiers et tests | ce qu'ils trouvent | accord |")
    a("|---|---|---|---|")
    for ligne in K_LIGNES:
        a(ligne)
    a("")
    a("**Les congruences nouvelles des agents** (la plus forte de chaque dossier ; chacun a sa table au § 5) :")
    for ligne in NOUVELLES:
        a(ligne)
    a("")
    a("## 3. Les triangles vides : v1 contre v2")
    a("")
    if tab:
        a("Résultats : [`resultats/revision_001.md`](../../resultats/revision_001.md), § 3. Mêmes trois niveaux que pour v1 :"
          " (1) les fiches ; (2) les fiches sans les deux hasards testés 002 et 004 ; (3) les fiches et les parties.")
        a("")
        a("| recouvrement | niveau | sommets, arêtes, triangles, tétraèdres | Betti b₀, b₁, b₂ | triangles vides | triangles remplis :"
          " éléments communs en moyenne | nul : b₁ moyen | nul : b₂ moyen | nul : triangles vides en moyenne | p (nul ≥ observé) |")
        a("|---|---|---|---|---:|---:|---:|---:|---:|---:|")
        t1 = open(os.path.join(REPO, "resultats", "revision_001.md"), encoding="utf-8").read()
        for x in t1.splitlines():
            if x.startswith("| v1 |"):
                a(x)
        for x in tab:
            a(x)
        a("")
        for x in bloc:
            a(x)
        a("")
        for x in LECTURE_NERF:
            a(x)
    else:
        a("*À calculer : relancer `python3 scripts/revision_001.py`, puis ce générateur.*")
    a("")
    a("## 4. Les arbres corrigés")
    a("")
    a("Figure : [`rev001_perron_venn.png`](../../figures/rev001_perron_venn.png), panneau b. Le tableau complet est au § 5 de la synthèse ;"
      " ici, ce qui change, et qui le dit.")
    a("")
    a("| arbre | disque | ce qui change | dossiers et tests |")
    a("|---|---|---|---|")
    for ligne in ARBRES:
        a(ligne)
    a("")
    a("## 5. Les doublons et les contradictions")
    a("")
    a("### 5.1 Trouvé deux fois : des confirmations")
    a("")
    for ligne in DOUBLONS:
        a(ligne)
    a("")
    a("### 5.2 Les désaccords entre agents")
    a("")
    for ligne in DESACCORDS:
        a(ligne)
    a("")
    a("### 5.3 Les erreurs du plan")
    a("")
    for ligne in PLAN:
        a(ligne)
    a("")
    a("## 6. Les trous dans les données publiées")
    a("")
    for ligne in TROUS:
        a(ligne)
    a("")
    a("## 7. Les nouvelles fiches, classées par dimension")
    a("")
    a("Chaque dossier propose ses fiches au § 6.1, avec leur type, leur statut, leur script et leur image. Elles ne sont pas écrites dans le"
      " recueil : on les écrira quand une partie les reprendra (revision-001.md, § 10). La colonne « puis » donne les dimensions"
      " voisines ; « déjà fait » renvoie au test ou à la fiche de la révision qui la recouvre.")
    a("")
    a(sept)
    a("")
    open(SORTIE, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("écrit", SORTIE, f"({len(presents)} dossiers ; {n2p} parties, {n2f} fiches ; {n_prop} fiches proposées)")


NOMBRES = {3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"}
K_LIGNES = [
    "| K1 | corde ; T3 | se recolle aux ordres 2 et 3 avec le décalage n → n + 49/10 ; obstruction à l'ordre 4 | accord. Le plan disait"
    " « dès l'ordre 3 », vrai seulement sans décalage |",
    "| K2 | lumière, aiguilles, moitiés, ombres | les trois 34 (aigrettes, ombre Σωⁱ, éventails) sont un seul fait pour N impair ; calculé"
    " pour N = 3 à 20 par deux agents (A) | accord à quatre. Moitiés ajoute l'obstruction en Kakeya fini (en caractéristique 2,"
    " x ↦ −x est l'identité) ; lumière ajoute la réserve de la phase (une ouverture complexe casse la symétrie de Friedel) |",
    "| K3 | bases ; § 4.3 | se recolle par la famille q² + 1 et le lemme des chiffres, démontré pour tout q ≥ 2 | accord |",
    "| K4 | moitiés, aiguilles, méthode ; T5 | obstruction : deux procédés, Bonferroni pour Kakeya fini et l'involution pour les"
    " hémisphères | accord à quatre. La piste XIV–XX se ferme. Méthode ajoute que les deux troncatures de Bonferroni bornent en sens"
    " opposés : l'ordre 1 majore (le p corrigé), l'ordre 2 minore (la taille de Kakeya) |",
    "| K5 | bases, ombres | bases : obstruction, aucune transformation connue entre le 17 de Henderson et le 17 de i | **ombres trouve"
    " une implication** : si i existe modulo n (n ≡ 1 mod 4), aucun Venn simple et symétrique n'a le complément pour symétrie. Un tel"
    " Venn serait antipodal, et la parité des croisements dans le plan projectif exige C(n, 2) impair. Impossible à 17 ; à 19 et 23,"
    " ni exclu ni construit. K5 se recolle donc en partie, par une implication, pas par une transformation |",
    "| K6 | grain, lumière, méthode ; T4 | le centre de la lumière suit la palette ; la seconde cause est le seuil, pas l'ordre de"
    " dessin | **désaccord partiel** (§ 5.2), tranché sur un système modèle : méthode refait l'expérience sur un Venn à 13 courbes"
    " de palette connue, et G·H₁ prédit l'écart sans paramètre libre (vérifié, § 4.12). La palette réelle de l'image à 17 courbes"
    " reste ouverte |",
    "| K7 | moitiés, grain, aiguilles | se recolle pour la pente : un cran, soit un facteur 2 sur l'exposant | accord sur la pente."
    " Deux obstructions nouvelles : le « 2,8 » n'est pas une constante (aiguilles) ; l'aire ½ de Perron à 4 branches n'est pas un"
    " effet de cran (moitiés). La cause commune du logarithme reste ouverte (grain) |",
    "| K8 | corde, bases, méthode ; T7 | une coïncidence de petits entiers | accord à trois. Ce qui se recolle passe par log₂ 3 et le"
    " comma (19/12) |",
    "| K9 | bases, méthode ; T6 | se recolle en une tour 2-adique, à aires inégales | bases ajoute l'enchevêtrement fixé par la"
    " réciprocité quadratique (A). **Méthode : « se recolle trivialement »** : la division par deux est la loi de toute valuation"
    " 2-adique, et aucun invariant de Perron (l'aire 2/(k + 2)) n'y passe. La synthèse est corrigée |",
    "| K10 | corde, grain ; § 4.4 | exact : c'est l'isopérimétrie | accord, avec une précision du dossier grain : le seuil vaut"
    " 4π·(s/a)² pour des croisements espacés de a et des régions de côté s. Le 13 vient du choix a = s = 2 px (§ 5.2) |",
]
NOUVELLES = [
    "- *Corde.* Le triangle de Thalès de la partie XXIV (§ 5) est le triangle du simplexe de la classification : (PQ, QP′) = (c_K, d_K),"
    " avec K − 1 = 1/x₀ (exact). Et la part de la clôture broutée vaut 2α_n/360°, avec cos α_n = x₀ : 39,34 % en est le cas n = 2.",
    "- *Moitiés.* Le cercle R/√2 est fixé par trois gestes (le miroir d'aire, l'inversion des jumeaux, la dilatation d'un cran), en toute"
    " dimension (exact). Les écarts à la moitié sont des miroirs : ½ − 1/√(2πn) sur la clôture, ½ + 1/√(2πn) sur le volume (calculé).",
    "- *Bases.* Le dernier chiffre d'un premier dit si le nombre d'or existe modulo p ; le cocycle se ferme sur 3, 9, 7 (démontré).",
    "- *Grain.* La loi des 8R de la partie XVIII et le budget de la moitié du Venn de la partie XXX se recollent exactement"
    " (8⌊R + ½⌋ et 8⌊r⌋ + 4).",
    "- *Aiguilles.* i ≡ a/c (mod b) de la partie XIX et l'aiguille primitive (a, c) de norme b = a² + c² de la partie XIV se recollent"
    " entièrement. Les coupes de Perron et les niveaux du Venn se recollent sur le cube {0, 1}ⁿ, avec une obstruction : binaire contre"
    " binomial.",
    "- *Lumière.* Tout masque de N zones égales a ses foyers par paires, I(N − u) = I(u) (vérifié sur 2 000 masques) : la symétrie"
    " de la partie VIII ne vient pas de Fibonacci.",
    "- *Ombres.* La face que choisit a modulo 3 dans la fiche 015 est une restriction du cube (la fibre au-dessus de 0), pas une"
    " ombre. Et 3 est le seul premier impair, étranger à 10, qui divise une différence de deux chiffres des unités (6 = 7 − 1 = 9 − 3) :"
    " c'est le facteur 2 de Hardy et Littlewood pour l'écart 6, la limite de la dérive de la fiche 021. La face de la fiche 015 et le"
    " 2 de la fiche 021 sont le même 3.",
    "- *Ombres.* Les périodes de Gauss du 17-gone sont les ombres Σωⁱ des régions fixées par un sous-groupe de (ℤ/17)* ; 4 ≡ i engendre"
    " celui d'ordre 4 (calculé à 10⁻¹⁵).",
    "- *Méthode.* Les quatre tests à tolérance sont des seuils sur le seul écart d (128 < 186 < 806 < 259 000 ppm) : ils sont"
    " totalement ordonnés, et leur cocycle est trivial. Or l'étiquette « structure » ou « hasard » n'est pas une fonction de d : rangés"
    " par écart, les six cas non triviaux du banc alternent S C S S S C. Aucun seuil ne peut les séparer.",
]
LECTURE_NERF = [
    "**Ce que les corrections ont changé** (ma lecture des tableaux ci-dessus).",
    "- *Les 4 trous du corpus de v1 sont refermés.* Ils passaient tous par le grain. Les parties ajoutées par les agents (XXIV à XXVII"
    " pour le grain, XIV et XXV pour méthode, XXIX et XXX pour aiguilles, XV et XVIII pour bases) donnent une partie commune à ces"
    " triplets. C'étaient des trous de la lecture du plan, pas du corpus.",
    "- *Au niveau des fiches, v2 laisse 11 triangles vides*, autant que des dossiers de mêmes tailles tirés au hasard (10,1 en moyenne,"
    " p = 0,44). Tous sont des trous du recueil : une partie réunit les trois dossiers, la fiche manque.",
    "- *Le dossier bases est dans 9 des 11 triangles vides, et dans les 10 tétraèdres creux.* Ses six fiches touchent peu les autres"
    " dossiers : une seule fiche commune avec corde (014), grain (001), lumière (002) ou moitiés (005), aucune avec aiguilles. C'est"
    " le sujet que le recueil relie le moins au reste, et c'est là que de nouvelles fiches compteraient le plus. Par exemple, celle"
    " que propose le dossier corde : les facteurs 2 des polynômes de la chèvre comptent les retenues de la base 2 (Kummer).",
    "- *Un trou ouvert par une correction.* En retirant la fiche 010, ombres ouvre le triangle corde · moitiés · ombres : la 010 le"
    " cachait. Il demande une fiche du cercle R/√2, celle des trois gestes que propose le dossier moitiés.",
    "- *Avec les parties (niveau 3)*, plus aucun triangle vide (20 en v1), et une seule cavité, b₂ = 1 (0,05 en moyenne pour le nul,"
    " p = 0,047). C'est le seul indicateur du nerf qui sorte du hasard, de justesse, et c'est un test parmi une dizaine : à surveiller,"
    " pas une découverte. Le dossier ombres rappelle que le nerf n'est pas la réunion (36 intersections non contractiles sur 166,"
    " dans la v2 à six corrections qu'il a lue) : cette cavité est une propriété du classement, pas du corpus.",
    "- *Ce que ça dit des révisions suivantes.* Une correction d'agent referme des trous du corpus (on lit mieux le corpus) et en"
    " déplace vers le recueil (il manque des fiches). Le nerf sert donc à dire où écrire les prochaines fiches : entre bases et les"
    " autres dossiers, et sur le cercle R/√2.",
]
ARBRES = [
    "| P1 l'ombre du cube {0, 1}ⁿ | D6 | une branche de la parité, les trois 34 (K2) ; un cube et huit regards, tous déjà écrits dans le"
    " corpus ; la fiche 015 y entre par une restriction, pas par une ombre ; les périodes de Gauss sont des ombres ; la branche Perron"
    " part de la partie V | lumière, aiguilles, moitiés, ombres |",
    "| P2 la moitié | D1 | un seul cercle R/√2, fixé par trois gestes ; la branche « Kakeya fini » se détache (Bonferroni) | moitiés ; T5 |",
    "| P3 le terme x²/6 | D1 | même 1/6, obstruction à l'ordre 4 ; le « dernier 2 » du ménisque compte les dérangements de 3 |"
    " corde ; T3 ; § 4.10 |",
    "| P4 le quart de tour i modulo b | D2 | la famille q² + 1, le lemme des chiffres, Φ₆(10) = 7 × 13, le dernier chiffre et le nombre"
    " d'or | bases ; § 4.3 et 4.10 |",
    "| P5 le budget en bits | D3 | le seuil isopérimétrique, la loi des 8R ; K7 tient pour la pente seulement | grain, aiguilles ; § 4.4 |",
    "| P6 les réduites et les trois distances | D2 | le diésis et le comma, deux écarts du même théorème ; la demi-case (Pick) pour l'or,"
    " l'argent, Farey et l'hexagone | bases, aiguilles |",
    "| P7 la loi de l'écart | D7 | sa réserve : une dérive peut croiser une constante (π, 2√2) | § 4.2 et 4.9 |",
    "| P8 le cône à sommet imaginaire | D8 | la branche « photocentre » se détache : il n'a ni col ni distance de Rayleigh ; la forme de"
    " Newton x·x′ = c revient cinq fois | lumière |",
    "| **P9 (nouveau)** le barycentre pesé | D8, contre D3 et D7 | le centre de la lumière est le premier harmonique des poids, G·H₁ ;"
    " le seuil en est un second canal ; établi par intervention sur un Venn à 13 courbes de palette connue | lumière, grain, méthode ;"
    " T4 ; fiche 018 |",
]
DOUBLONS = [
    "- **La fiche 010.** Corde et moitiés, chacun par son calcul, trouvent que 39,34 % n'est exact que pour le cercle du bord : la part"
    " monte quand on rentre (39,57 % pour l'anneau de rayon 0,99 ; 39,52 % au niveau 4 du dessin à aire égale). La fiche est corrigée."
    " Ombres la retire de son dossier : elle n'a de cube que le dessin. En la retirant, il ouvre un triangle vide, corde · moitiés ·"
    " ombres : la fiche 010 cachait ce trou, qui demande une fiche du cercle R/√2 (celle des trois gestes, proposée par moitiés).",
    "- **K2, les trois 34.** Lumière et aiguilles l'ont calculé chacun pour N = 3 à 20 ; moitiés l'a relié à x ↦ −x.",
    "- **K4, la moitié de Kakeya fini.** Moitiés, aiguilles et le test T5 concluent tous trois à deux procédés.",
    "- **Le minimum 2/(k + 2).** Moitiés (pour k = 2, l'aire vaut ½ sur tout un segment de rapports) et aiguilles (pour k = 3,"
    " 43/108 < 2/5, vérifié au § 4.10) trouvent chacun que c'est le minimum de la borne, pas celui de l'aire. La partie V l'avait vu"
    " en nombres (0,3981). CLAUDE.md et la partie XXVIII sont précisés.",
    "- **La palette comme cause du centre de la lumière.** Grain et lumière l'ont trouvée tous deux ; ils ne s'accordent pas sur les"
    " détails (§ 5.2). Méthode tranche le statut : la cause est établie par intervention sur un système modèle (le Venn à 13"
    " courbes repeint, refait au § 4.12 du script) ; sur l'image à 17 courbes, la palette n'est encore qu'ajustée.",
    "- **Le « 93 % » et le banc d'essai.** Lumière a montré que le 93 % est le taux de base ; méthode, que le « 10/10 » de la variation"
    " est en partie écrit à la main. Deux erreurs de la même partie XXX, trouvées par deux chemins : un score cité sans son témoin.",
]
DESACCORDS = [
    "1. **K7 : le « 2,8 » de Perron sur une grille.** Le dossier grain tient l'analogie pour « confirmée » avec cette valeur. Le dossier"
    " aiguilles la calcule plus loin : « part × log₂ n » culmine à 2,83 (n = 256), puis baisse à 2,57 (n = 65 536). Les deux ont raison"
    " sur la pente ; la valeur n'est pas une constante. Verdict : se recolle pour la pente, pas pour les valeurs.",
    "2. **K6 : quelle palette ?** Les deux dossiers disent que les couleurs mesurées (les 5 % de pixels les plus clairs de chaque teinte)"
    " ne suffisent pas : avec elles, les directions relatives des écarts ratent de 55° (luminance) et 47° (clarté) (lumière, (A)).",
    "   - Le dossier grain ajuste une palette de conception presque isoluminante (Y₀ = 0,30 à 0,36) et un facteur G de 181 à 194 px."
    " Il retrouve les quatre pesées continues à 1,4 – 2,0 px près, et leurs phases à 6° près ; il conclut « obstruction levée sous"
    " condition ».",
    "   - Mais il note lui-même deux restes : le bras de levier mesuré vaut 379 px, deux fois le G ajusté ; et les masques du modèle"
    " vont de 1 à 17 px quand les mesures vont de 0,4 à 27 px, avec des directions décalées de 10° à 40°.",
    "   - Le dossier lumière garde le statut « structure, à tester » : le rapport des pesées Y/E vaut 0,0132, entre 0,003 (palette"
    " isoluminante) et 0,23 (couleurs mesurées).",
    "   - **Le dossier méthode a fait le rendu de contrôle** (§ 3.6 ; refait par le script de la révision, § 4.12) : sur le Venn à 13 courbes du traceur, de palette et d'ordre"
    " connus, repeint par son propre rendu, G·H₁ prédit l'écart **sans paramètre libre** (2,08 px prédits, 2,05 à 2,20 observés,"
    " phases à 11° près), et quatre autres ordres de dessin ne déplacent le centre que de 0,3 px au plus. À luminance égale, l'écart"
    " en luminance tombe à 0,13 px quand ceux de la moyenne RGB et de l'énergie restent à 2,3 et 1,6 px : le motif de l'image à"
    " 17 courbes.",
    "   - Mon verdict : la loi est établie par intervention sur un système modèle, et la lecture du dossier grain (une palette presque"
    " isoluminante) en sort renforcée. Sur l'image à 17 courbes, la palette reste ajustée, faute du code de rendu. Le test T4 a"
    " ajouté un second canal, le seuil (fiche 018) ; le témoin du dossier méthode montre qu'un effet de seuil signe une grandeur"
    " seuillée qui varie d'une courbe à l'autre.",
    "3. **La fiche 005.** Moitiés trouve « miroir + complément » en tête dans les 18 certificats, à 1,5 à 2,3 fois le hasard, et"
    " conclut « hasard testé, cause ouverte » (A). Bases la juge « compatible avec le hasard ». Le calcul de moitiés (son § 7.3) est"
    " à refaire avant de trancher.",
    "4. **Pas un désaccord : la fiche 014.** Corde y voit un lien faible, par les nombres (√2, 2/√3, √(3/2)) ; bases, un lien exact"
    " avec F₉. Ils parlent de deux parties de la fiche.",
    "5. **Une précision de K10.** Le seuil vaut n* = 4π·(s/a)², pour des croisements espacés de a et des régions de côté s. Avec"
    " a = s = 2 px (le choix de la partie XXX), on trouve 4π et 13 courbes ; avec a/s = 1,5, le seuil tombe à 5,6 courbes ; avec"
    " a/s = 0,5, il monte à 50,3. L'isopérimétrie est la loi ; le 13 est le cadre. C'est exactement ton sujet d'étude : la restriction"
    " du cadre fixe le nombre qu'on observe.",
]
PLAN = [
    "- *K1* : « obstruction dès l'ordre 3 ». Vrai sans décalage ; avec le décalage s = 49/10, l'ordre 3 se recolle et l'obstruction est à"
    " l'ordre 4 (corde, refait par T3).",
    "- *K6* : la seconde cause proposée, l'ordre de dessin, est écartée deux fois (T4 : p = 0,64 ; grain : contraste d'ordre −6,0 %,"
    " comme les témoins). La seconde cause est le seuil.",
    "- *K7* : le « 2,8 » pris pour une constante (aiguilles).",
    "- *K10* : le polygone inscrit du plan donne n* = 12,295 ; le n-gone de même aire du script, 12,824 ; le cercle, 12,566. Les trois"
    " donnent 13 courbes (grain).",
    "- *La liste de lecture de l'agent corde* oubliait six fichiers, dont carte-connexions.md et archimede.md (corde).",
    "- *T6* : « Midy en Perron ». La division par deux à chaque étage est la loi de toute valuation 2-adique, pas un invariant de"
    " Perron (méthode). La synthèse est corrigée.",
    "- *T1 et T8* sont des nuls (la dernière ligne de la table du § 10), pas des variations du paramètre ; et le nul de T1 garde les"
    " marges, ce qui le rend conservateur quand la structure est dans les tailles des dossiers (méthode).",
]
TROUS = [
    "La synthèse en fait le tableau (revision-001.md, § 9), et chaque dossier a le sien (§ 6.3). La vérification croisée ajoute ceci :"
    " **quatre trous sont désignés par deux dossiers ou plus à la fois**, ce qui les rend plus sûrs.",
    "- *La chaîne de rendu des images de Venn* (grain, lumière) : la palette, l'espace de mélange, l'anticrénelage et l'ordre de"
    " dessin des PNG à 17 courbes ne sont pas publiés. C'est aussi ce qui bloque K6.",
    "- *Le déplacement induit par la couleur* (lumière, grain) : pour N sources colorées en symétrie d'ordre N, le centre dépend du"
    " poids et du seuil. À répliquer sur les binaires « CID » de SDSS (Pourbaix et al., 2004) : à calculer.",
    "- *Les constantes de Perron et de Kakeya au grain fini* (aiguilles, moitiés, grain) : pas de table publiée des rapports optimaux,"
    " ni de la constante entre π/2 et π·ln 2.",
    "- *Ce que le dépôt de Dzoba ne publie pas* (ombres, méthode, grain) : la moitié des croisements et les croisements par niveau, la"
    " symétrie par le complément, le profil des défauts par rang, l'histogramme des degrés, l'ordre de dessin et le code de rendu. Les six"
    " certificats à 23 courbes sont publiés (Zenodo) mais pas lus : k₁, N_l et la part des triangles s'y liraient.",
    "",
    "**Les références à vérifier**, relevées par plusieurs dossiers : le titre de Wielen (1996) ; le nom de la revue de Fraser en 1984 ;"
    " les deux articles « Córdoba (1977) » ; le Nikon D800E ; la référence exacte des corrections de chromaticité de Gaia.",
]

if __name__ == "__main__":
    main()
