"""Le registre des drapeaux de la révision 001 : ce que les agents ont signalé, avec sa nature et son verdict.

    python3 recueil/revisions/outils-001/drapeaux.py

Quand et pourquoi.
- Créé le 10 octobre 2026 (arc 003), après une remarque de l'auteur sur le bilan de la révision 001. Les agents
  lèvent des drapeaux, pas des erreurs, et seuls la session et l'auteur jugent une erreur (CLAUDE.md, § 10).
- Refait le même jour (arc 004), après les drapeaux de l'agent de fin d'arc 003 sur ce registre. Les verdicts sont
  réduits à quatre (confirmé, infirmé, à juger, plan). Deux colonnes sont ajoutées : « procédé court » (le drapeau se
  juge-t-il en relançant ou en comparant ?) et « correction ». Les 13 signalements de la synthèse qui n'étaient pas
  dans les sorties structurées sont ajoutés.

Ce que le script lit et écrit.
- Il lit recueil/revisions/sorties-agents-001.json : 45 signalements, dans les sept sorties structurées gardées.
- Il écrit recueil/revisions/drapeaux-001.csv, et affiche les tableaux du § 1 du bilan.
- Le CSV est réécrit à chaque passage. Un jugement se note donc dans les tables J et AUTRES ci-dessous, pas dans le
  CSV.

Les colonnes.
- « nature » : procédé court (une erreur de script ou de calcul, visible dans les résultats), association (deux
  choses reliées ou attribuées à tort, une lecture qui devient un fait), assemblage (des morceaux justes mal mis
  ensemble : notations, renvois, choix de cadre non écrits), référence, plan.
- « procédé court » : oui si le drapeau peut se juger en relançant, en recalculant ou en comparant.
- « verdict » : confirmé, infirmé, à juger (le chat de Schrödinger), plan (une erreur du plan, pas du corpus).
- « jugé par » : la session ; pour l'association et l'assemblage, la session, puis l'auteur.
- « levé le » : la fin de l'agent qui a levé le drapeau, d'après sa transcription (outils-001/stats_agents.py).
- La nature et le verdict de chaque ligne sont des jugements de la session, rendus a posteriori pour la révision 001 :
  les agents ne donnaient pas encore la nature de leurs signalements.
"""

import collections
import csv
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
REV = os.path.join(ICI, "..")
LEVE = {"corde-et-dimensions": "2026-10-07", "moities-et-crans": "2026-10-07", "bases-congruences-premiers": "2026-10-08",
        "grain-pixels-centres": "2026-10-08", "aiguilles-kakeya-perron": "2026-10-08", "ombres-cube-venn": "2026-10-09",
        "hasard-et-methode": "2026-10-09", "lumiere-et-physique": "2026-10-08"}
LONGS = {"corde-et-dimensions", "moities-et-crans", "bases-congruences-premiers", "grain-pixels-centres"}
REV1, ARC3, ARC4 = "révision 001", "2026-10-10, arc 003", "2026-10-10, arc 004"
S, A = "la session", "la session ; à confirmer par l'auteur"
PC, ASS, ASM, REF, PLAN = "procédé court", "association", "assemblage", "référence", "plan"
OUI, NON = "oui", "non"
C, J_, P = "confirmé", "à juger", "plan"

# (dossier, rang dans erreurs_trouvees) → (nature, procédé court, verdict, jugé par, jugé quand, correction, raison)
J = {
    ("corde-et-dimensions", 1): (PC, OUI, C, S, REV1, "partielle", "XXIII § 1 : la note de correction est dans lentilles-boules-grain.md ; resultats/lentilles_boules_grain.md (l. 17) garde 0,6668 et 0,6661, que le script réécrit"),
    ("corde-et-dimensions", 2): (PC, OUI, J_, "", "", "", "signalée : figure x1, panneau e (sphère ou boule)"),
    ("corde-et-dimensions", 3): (ASM, NON, J_, "", "", "", "signalée : α_n et β ont deux sens (I, XX, XXII, XXV)"),
    ("corde-et-dimensions", 4): (PC, OUI, C, S, REV1, "partielle", "fiche 010 corrigée ; centre-venn.md, § 4.3 (l. 279), et la légende de la figure ae2, panneau d (scripts/centre_venn.py), disent encore « chaque anneau »"),
    ("corde-et-dimensions", 5): (ASS, OUI, J_, "", "", "", "signalée : XVI § 2, « la même proximité » (46 fois plus étroite, (A))"),
    ("corde-et-dimensions", 6): (REF, OUI, J_, "", "", "", "signalée : README § 9, le nom de la revue de Fraser en 1984"),
    ("corde-et-dimensions", 7): (PLAN, OUI, P, S, REV1, "", "vérification croisée, § 5.3 : six fichiers manquaient à la liste de lecture"),
    ("corde-et-dimensions", 8): (PLAN, OUI, P, S, REV1, "", "vérification croisée, § 5.3 : K1, refait par T3 (l'obstruction est à l'ordre 4)"),
    ("moities-et-crans", 1): (PC, OUI, C, S, REV1, "partielle", "même correction que D04"),
    ("moities-et-crans", 2): (ASS, OUI, J_, "", "", "", "signalée : V § 3, l'aire ½ pour deux rapports indépendants (calcul exact de l'agent, (A))"),
    ("moities-et-crans", 3): (ASS, OUI, C, A, REV1, "partielle", "XIV § 5 et XXVII § 9 : la moitié vient de l'inclusion–exclusion (T5) ; carte-connexions.md, § 9 (l. 327), et aiguille-grille.md (l. 224) gardent « les carrés modulo q »"),
    ("moities-et-crans", 4): (ASS, OUI, C, A, REV1, "faite", "CLAUDE.md § 6 précisé : le minimum de la borne, pas de l'aire (43/108, § 4.10)"),
    ("moities-et-crans", 5): (PC, OUI, C, S, REV1, "faite", "la liste des statuts de recueil/README.md complétée par « calculé » (commit 2324dd9)"),
    ("bases-congruences-premiers", 1): (PC, OUI, C, S, REV1, "faite", "XI : 222,5° = 89/144 de tour"),
    ("bases-congruences-premiers", 2): (PC, OUI, C, S, REV1, "faite", "XIX § 4 corrigée et recalculée"),
    ("bases-congruences-premiers", 3): (ASM, OUI, C, A, REV1, "faite", "XVIII § 8 : le renvoi vers XIX est ajouté"),
    ("grain-pixels-centres", 1): (ASS, OUI, C, A, REV1, "faite", "XXX § 1.1 : la palette du traceur n'est pas celle de l'image"),
    ("grain-pixels-centres", 2): (ASS, NON, C, A, REV1, "faite", "XXIX § 1.2 : une lecture, que le README de Dzoba ne dit pas"),
    ("grain-pixels-centres", 3): (ASM, NON, J_, "", "", "", "signalée : XXIX § 2.3 et § 5.2, XXX § 2.5 (un choix qui devient une donnée)"),
    ("grain-pixels-centres", 4): (ASM, OUI, J_, "", "", "", "signalée : XXIX § 4 (des longueurs et des aires dans le même tableau)"),
    ("grain-pixels-centres", 5): (ASS, NON, J_, "", "", "", "signalée avec la précédente : « un bit par pas »"),
    ("grain-pixels-centres", 6): (PC, OUI, J_, "", "", "", "signalée : XVIII § 4, la loi des 8R exacte (A)"),
    ("grain-pixels-centres", 7): (ASM, NON, J_, "", "", "", "signalée : XXIII et XXIV, le plan de la lentille écrit deux fois"),
    ("aiguilles-kakeya-perron", 1): (PC, OUI, J_, "", "", "", "signalée : XIV § 6, le produit culmine à 2,83 puis baisse (A)"),
    ("aiguilles-kakeya-perron", 2): (ASS, OUI, C, A, REV1, "faite", "même correction que D12"),
    ("aiguilles-kakeya-perron", 3): (ASS, OUI, C, A, REV1, "faite", "XXVIII, En bref : l'aire des arbres télescopiques"),
    ("aiguilles-kakeya-perron", 4): (PC, OUI, J_, "", "", "", "signalée : XXVIII § 3.5, imprécision mineure"),
    ("aiguilles-kakeya-perron", 5): (REF, OUI, J_, "", "", "", "signalée : les deux « Córdoba (1977) »"),
    ("aiguilles-kakeya-perron", 6): (ASM, OUI, J_, "", "", "", "signalée : la numérotation des sections (X, XVII, XIX, XXVIII)"),
    ("ombres-cube-venn", 1): (PLAN, OUI, P, S, REV1, "", "recouvrement v2 : la partie V est ajoutée au dossier"),
    ("ombres-cube-venn", 2): (PLAN, OUI, P, S, REV1, "", "recouvrement v2 : la fiche 010 est retirée du dossier"),
    ("ombres-cube-venn", 3): (PLAN, OUI, P, S, REV1, "", "la liste de lecture du plan omettait quatre fichiers"),
    ("ombres-cube-venn", 4): (ASS, NON, J_, "", "", "", "signalée : XXIX § 5.3, « épaisseur constante »"),
    ("ombres-cube-venn", 5): (PC, OUI, J_, "", "", "", "signalée : XXIX § 2.2, la dérive à 23 courbes"),
    ("ombres-cube-venn", 6): (PC, OUI, C, S, REV1, "faite", "fiche 004, section Révision 001 : la variation va jusqu'à 23 courbes"),
    ("ombres-cube-venn", 7): (ASS, NON, J_, "", "", "", "signalée : XXX § 3 et § 9 (le Venn antipodal, exclu à 17 au sens fort, (A))"),
    ("ombres-cube-venn", 8): (ASS, NON, J_, "", "", "", "un désaccord entre deux dossiers (ombres contre moitiés : la réflexion de l'équateur), absent de la vérification croisée, § 5.2"),
    ("ombres-cube-venn", 9): (ASM, OUI, J_, "", "", "", "signalée avec D29 : la numérotation des sections (XXIX, XXI, XXVIII)"),
    ("hasard-et-methode", 1): (ASM, OUI, J_, "", "", "", "signalée : XXIX § 5.5, « ppm » au sens du logarithme (2 852 contre 2 856 au sens relatif)"),
    ("hasard-et-methode", 2): (ASS, OUI, J_, "", "", "", "signalée : VI § 3 bis, δ₂ ≈ δ₃ jamais testé"),
    ("hasard-et-methode", 3): (PC, OUI, C, S, ARC4, "faite", "la ligne « test » de la fiche 004 dit maintenant « un certificat par n » ; la fiche 022 le disait déjà"),
    ("hasard-et-methode", 4): (ASS, OUI, C, A, REV1, "faite", "tranché par l'intervention : l'ordre de dessin ne déplace le centre que de 0,26 px (scripts/revision_001.py, § 4.12)"),
    ("hasard-et-methode", 5): (ASS, OUI, J_, "", "", "", "signalée : XXVII § 1.3, le prédicteur d'Adamic–Adar (A)"),
    ("hasard-et-methode", 6): (ASM, NON, J_, "", "", "", "signalée : le facteur de Bonferroni (1 240), un choix de cadre"),
    ("hasard-et-methode", 7): (PC, OUI, C, S, ARC3, "à faire", "une fragilité réelle : un repli silencieux sur 410 ; les résultats actuels n'en souffrent pas (λ = 402, lu sur 7 lignes)"),
}

# Les signalements de la synthèse absents des sorties structurées :
# (source, dossier, fichier, affirmation, nature, procédé court, verdict, jugé par, jugé quand, correction, raison)
AUTRES = [
    ("texte du dossier (sortie perdue)", "lumiere-et-physique", "centre-venn.md (En bref, § 6.3) ; CLAUDE.md § 6",
     "« 93 % des signes en accord » avec la défocalisation", ASS, OUI, C, A, REV1, "faite",
     "c'est le taux de base : 71 rayons sur 76, contre 70 pour un prédicteur constant (§ 4.11)"),
    ("texte des dossiers", "lumiere-et-physique ; hasard-et-methode", "figure ae3, panneau d ; resultats/centre_venn.md § 6",
     "le « 93 % » répété sans son taux de base", ASM, OUI, C, A, REV1, "faite",
     "la légende et les résultats donnent le taux de base (« positif partout » : 92 %) ; script de la partie XXX relancé"),
    ("texte du dossier", "hasard-et-methode", "centre-venn.md (En bref, § 7.2, figure ae3 panneau f) ; CLAUDE.md § 10",
     "« la précision poussée et la variation du paramètre ne se trompent jamais »", ASS, OUI, C, A, REV1, "faite",
     "la précision ne peut que confirmer ou s'abstenir, et trois verdicts (C1, C2, E4) sont écrits à la main"),
    ("texte du dossier (sortie perdue)", "lumiere-et-physique", "centre-venn.md, Sources", "le titre de Wielen (1996), A&A 314",
     REF, OUI, J_, "", "", "", "signalée : à vérifier sur ADS"),
    ("texte du dossier (sortie perdue)", "lumiere-et-physique", "README.md § 7", "« Analogies, pas équivalences… ne prouvent rien »",
     ASM, NON, J_, "", "", "", "signalée : contredit CLAUDE.md § 1"),
    ("texte du dossier (sortie perdue)", "lumiere-et-physique", "foyer-fibonacci.md (partie VIII), § 7",
     "la récurrence de Fibonacci fait la symétrie des deux foyers", ASS, NON, J_, "", "", "",
     "signalée : la symétrie vaut pour tout masque ; Fibonacci dit où les foyers tombent"),
    ("texte du dossier (sortie perdue)", "lumiere-et-physique", "pixels-longitudes.md (partie XVIII), § 7",
     "le Nikon D800E ôte la lame passe-bas", REF, OUI, J_, "", "", "", "signalée : il en annule l'effet par une seconde lame (à vérifier)"),
    ("texte du dossier", "bases-congruences-premiers", "recueil/observations/014", "« (−2)^(3/2) ≡ −i modulo 3 »",
     ASS, NON, J_, "", "", "", "signalée : la phrase réunit 2^(3/2) (≡ −i dans F₉) et (−2)^(3/2) (±1 dans F₉) ; une question pour l'auteur (bilan, § 10.7)"),
    ("vérification croisée, § 5.3", "grain-pixels-centres ; test T4", "recueil/revisions/plan-001.md, K6",
     "la seconde cause du centre est l'ordre de dessin", PLAN, OUI, P, S, REV1, "", "écartée deux fois (T4 : p = 0,64 ; grain : contraste d'ordre de −6,0 %)"),
    ("vérification croisée, § 5.3", "aiguilles-kakeya-perron", "recueil/revisions/plan-001.md, K7",
     "le « 2,8 » de Perron sur une grille est une constante", PLAN, OUI, P, S, REV1, "", "une pente : le produit culmine à 2,83 puis baisse"),
    ("vérification croisée, § 5.3", "grain-pixels-centres", "recueil/revisions/plan-001.md, K10",
     "le polygone inscrit donne le seuil du centre", PLAN, OUI, P, S, REV1, "", "12,295 (inscrit), 12,824 (n-gone de même aire), 12,566 (cercle) : les trois donnent 13 courbes"),
    ("vérification croisée, § 5.3", "hasard-et-methode", "recueil/revisions/plan-001.md, T6", "Midy « en Perron »",
     PLAN, NON, P, S, REV1, "", "la division par deux à chaque étage est la loi de toute valuation 2-adique"),
    ("vérification croisée, § 5.3", "hasard-et-methode", "recueil/revisions/plan-001.md, T1 et T8", "T1 et T8 font varier un paramètre",
     PLAN, NON, P, S, REV1, "", "ce sont des nuls ; celui de T1 garde les marges"),
]

CHAMPS = ["id", "source", "dossier", "rang", "leve_le", "fichier", "affirmation", "nature", "procede_court",
          "verdict", "juge_par", "juge_quand", "correction", "raison"]
sorties = json.load(open(os.path.join(REV, "sorties-agents-001.json"), encoding="utf-8"))["dossiers"]
lignes = []
for dossier, s in sorties.items():
    for rang, e in enumerate(s.get("erreurs_trouvees", []), 1):
        nat, pc, ver, par, quand, cor, raison = J[(dossier, rang)]
        lignes.append(dict(zip(CHAMPS, [f"D{len(lignes) + 1:02d}", "sortie structurée", dossier, rang, LEVE[dossier],
                                        e.get("fichier", ""), e.get("affirmation", ""), nat, pc, ver, par, quand, cor, raison])))
assert len(lignes) == len(J) == 45, len(lignes)
for src, dossier, fichier, aff, nat, pc, ver, par, quand, cor, raison in AUTRES:
    lignes.append(dict(zip(CHAMPS, [f"D{len(lignes) + 1:02d}", src, dossier, "", LEVE[dossier.split(" ; ")[0]],
                                    fichier, aff, nat, pc, ver, par, quand, cor, raison])))

with open(os.path.join(REV, "drapeaux-001.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=CHAMPS)
    w.writeheader()
    w.writerows(lignes)

VERDICTS = [C, "infirmé", J_, P]


def ligne(nom, groupe):
    c = collections.Counter(x["verdict"] for x in groupe)
    return f"| {nom} | {len(groupe)} | " + " | ".join(str(c[v]) for v in VERDICTS) + " |"


structurees = [x for x in lignes if x["source"] == "sortie structurée"]
print("| dossiers (sorties structurées) | drapeaux | " + " | ".join(VERDICTS) + " |")
print(ligne("longs", [x for x in structurees if x["dossier"] in LONGS]))
print(ligne("concis", [x for x in structurees if x["dossier"] not in LONGS]))
print(ligne("les 45", structurees))
print(ligne("avec les 13 de la synthèse", lignes))
print()
print("| nature | drapeaux | " + " | ".join(VERDICTS) + " | se juge par procédé court |")
for nat in [PC, ASS, ASM, REF, PLAN]:
    g = [x for x in lignes if x["nature"] == nat]
    print(ligne(nat, g)[:-1] + f"| {sum(x['procede_court'] == OUI for x in g)} |")
print()
print("à confirmer par l'auteur :", ", ".join(x["id"] for x in lignes if x["juge_par"] == A))
print("corrections partielles ou à faire :", ", ".join(f"{x['id']} ({x['correction']})" for x in lignes if x["correction"] in ("partielle", "à faire")))
