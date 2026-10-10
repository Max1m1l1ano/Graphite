"""Le registre des drapeaux de la révision 001 : ce que les agents ont signalé, avec sa nature et son verdict.

    python3 recueil/revisions/outils-001/drapeaux.py

Créé le 10 octobre 2026 (arc 003), après une remarque de l'auteur sur le bilan de la révision 001 : les agents
lèvent des drapeaux, pas des erreurs, et seuls la session et l'auteur jugent une erreur (CLAUDE.md, § 10). Le bilan
comptait des « erreurs trouvées » par heure ; ce script remplace ce compte par le verdict de chaque drapeau.

Lit recueil/revisions/sorties-agents-001.json (les 45 signalements des sept sorties structurées gardées ; celle de
lumière est perdue). Écrit recueil/revisions/drapeaux-001.csv, et affiche les deux tableaux du § 1 du bilan.

La nature et le verdict de chaque drapeau sont des jugements de la session, écrits ci-dessous avec leur raison :
- nature : « procédé court » (un script, un nombre, un libellé, un format : se juge en relançant ou en comparant),
  « association » (deux choses reliées ou attribuées à tort, une lecture qui devient un fait), « assemblage » (des
  morceaux justes mal mis ensemble : notations, renvois, choix de cadre non écrits), « référence », « plan » ;
- verdict : « confirmé » (corrigé après vérification), « infirmé » (pas une erreur), « à juger » (le chat de
  Schrödinger), « plan » (une erreur du plan, prise en compte dans le recouvrement v2 ou la vérification croisée),
  « réglé ailleurs » (dans une fiche ou par un test).
"""

import collections
import csv
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
REV = os.path.join(ICI, "..")
LEVE = {"corde-et-dimensions": "2026-10-07", "moities-et-crans": "2026-10-07", "bases-congruences-premiers": "2026-10-08",
        "grain-pixels-centres": "2026-10-08", "aiguilles-kakeya-perron": "2026-10-08", "ombres-cube-venn": "2026-10-09",
        "hasard-et-methode": "2026-10-09"}
LONGS = {"corde-et-dimensions", "moities-et-crans", "bases-congruences-premiers", "grain-pixels-centres"}
REV1, ARC3 = "révision 001", "2026-10-10, arc 003"
SESSION, AUTEUR = "la session", "la session ; à confirmer par l'auteur"

# (dossier, rang dans erreurs_trouvees) → (nature, verdict, jugé par, jugé quand, raison)
J = {
    ("corde-et-dimensions", 1): ("procédé court", "confirmé", SESSION, REV1, "XXIII § 1 corrigée : du bruit de double précision"),
    ("corde-et-dimensions", 2): ("procédé court", "à juger", "", "", "signalée : figure x1, panneau e (sphère ou boule)"),
    ("corde-et-dimensions", 3): ("assemblage", "à juger", "", "", "signalée : α_n et β ont deux sens (I, XX, XXII, XXV)"),
    ("corde-et-dimensions", 4): ("procédé court", "confirmé", SESSION, REV1, "fiche 010 corrigée (titre et texte) ; les valeurs par niveau restent à refaire"),
    ("corde-et-dimensions", 5): ("association", "à juger", "", "", "signalée : XVI § 2, « la même proximité »"),
    ("corde-et-dimensions", 6): ("référence", "à juger", "", "", "signalée : README § 9, le nom de la revue de Fraser en 1984"),
    ("corde-et-dimensions", 7): ("plan", "plan", SESSION, REV1, "vérification croisée, § 5.3 : six fichiers manquaient à la liste de lecture"),
    ("corde-et-dimensions", 8): ("plan", "plan", SESSION, REV1, "vérification croisée, § 5.3 : K1, refait par T3 (obstruction à l'ordre 4)"),
    ("moities-et-crans", 1): ("procédé court", "confirmé", SESSION, REV1, "fiche 010 corrigée, avec le drapeau de corde"),
    ("moities-et-crans", 2): ("procédé court", "à juger", "", "", "signalée : V § 3, l'aire ½ pour deux rapports indépendants (A)"),
    ("moities-et-crans", 3): ("association", "confirmé", AUTEUR, REV1, "XIV § 5 et XXVII § 9 corrigées : la moitié vient de l'inclusion–exclusion (T5)"),
    ("moities-et-crans", 4): ("association", "confirmé", AUTEUR, REV1, "CLAUDE.md § 6 précisé : le minimum de la borne, pas de l'aire (43/108)"),
    ("moities-et-crans", 5): ("procédé court", "confirmé", SESSION, REV1, "la liste des statuts de recueil/README.md est complétée par « calculé » (commit 2324dd9)"),
    ("bases-congruences-premiers", 1): ("procédé court", "confirmé", SESSION, REV1, "XI corrigée : 222,5° = 89/144 de tour"),
    ("bases-congruences-premiers", 2): ("procédé court", "confirmé", SESSION, REV1, "XIX § 4 corrigée et recalculée"),
    ("bases-congruences-premiers", 3): ("assemblage", "confirmé", AUTEUR, REV1, "XVIII § 8 : le renvoi vers XIX est ajouté"),
    ("grain-pixels-centres", 1): ("association", "confirmé", AUTEUR, REV1, "XXX § 1.1 corrigée : la palette du traceur n'est pas celle de l'image"),
    ("grain-pixels-centres", 2): ("association", "confirmé", AUTEUR, REV1, "XXIX § 1.2 corrigée : une lecture, que le README de Dzoba ne dit pas"),
    ("grain-pixels-centres", 3): ("assemblage", "à juger", "", "", "signalée : XXIX § 2.3 et § 5.2, XXX § 2.5 (un choix qui devient une donnée)"),
    ("grain-pixels-centres", 4): ("association", "à juger", "", "", "signalée : XXIX § 4 (des longueurs et des aires dans le même tableau)"),
    ("grain-pixels-centres", 5): ("association", "à juger", "", "", "signalée avec la précédente : « un bit par pas »"),
    ("grain-pixels-centres", 6): ("procédé court", "à juger", "", "", "signalée : XVIII § 4, la loi des 8R exacte (A)"),
    ("grain-pixels-centres", 7): ("assemblage", "à juger", "", "", "signalée : XXIII et XXIV, le plan de la lentille écrit deux fois"),
    ("aiguilles-kakeya-perron", 1): ("procédé court", "à juger", "", "", "signalée : XIV § 6, le produit culmine à 2,83 puis baisse (A)"),
    ("aiguilles-kakeya-perron", 2): ("association", "confirmé", AUTEUR, REV1, "CLAUDE.md § 6 précisé, avec le drapeau de moitiés"),
    ("aiguilles-kakeya-perron", 3): ("association", "confirmé", AUTEUR, REV1, "XXVIII, En bref, précisé : l'aire des arbres télescopiques"),
    ("aiguilles-kakeya-perron", 4): ("procédé court", "à juger", "", "", "signalée : XXVIII § 3.5, imprécision mineure"),
    ("aiguilles-kakeya-perron", 5): ("référence", "à juger", "", "", "signalée : les deux « Córdoba (1977) »"),
    ("aiguilles-kakeya-perron", 6): ("assemblage", "à juger", "", "", "signalée : la numérotation des sections (X, XVII, XIX, XXVIII)"),
    ("ombres-cube-venn", 1): ("plan", "plan", SESSION, REV1, "recouvrement v2 : la partie V est ajoutée au dossier"),
    ("ombres-cube-venn", 2): ("plan", "plan", SESSION, REV1, "recouvrement v2 : la fiche 010 est retirée du dossier"),
    ("ombres-cube-venn", 3): ("plan", "plan", SESSION, REV1, "la liste de lecture du plan omettait quatre fichiers"),
    ("ombres-cube-venn", 4): ("association", "à juger", "", "", "signalée : XXIX § 5.3, « épaisseur constante »"),
    ("ombres-cube-venn", 5): ("procédé court", "à juger", "", "", "signalée : XXIX § 2.2, la dérive à 23 courbes"),
    ("ombres-cube-venn", 6): ("procédé court", "réglé ailleurs", SESSION, REV1, "fiche 004, section Révision 001 : la variation va jusqu'à 23 courbes"),
    ("ombres-cube-venn", 7): ("association", "à juger", "", "", "signalée : XXX § 3 et § 9 (le Venn antipodal, exclu à 17 au sens fort) (A)"),
    ("ombres-cube-venn", 8): ("association", "à juger", "", "", "jamais jugé : porte sur le dossier moitiés (la réflexion de l'équateur), pas sur le corpus"),
    ("ombres-cube-venn", 9): ("assemblage", "à juger", "", "", "signalée avec aiguilles : la numérotation des sections (XXIX, XXI, XXVIII)"),
    ("hasard-et-methode", 1): ("procédé court", "à juger", "", "", "signalée : XXIX § 5.5, « ppm » au sens du logarithme"),
    ("hasard-et-methode", 2): ("association", "à juger", "", "", "signalée : VI § 3 bis, δ₂ ≈ δ₃ jamais testé"),
    ("hasard-et-methode", 3): ("procédé court", "réglé ailleurs", SESSION, REV1, "fiche 004, section Révision 001 : 35,8 % est un des quatre certificats"),
    ("hasard-et-methode", 4): ("association", "réglé ailleurs", SESSION, REV1, "tranché par l'intervention (scripts/revision_001.py, § 4.12)"),
    ("hasard-et-methode", 5): ("association", "à juger", "", "", "signalée : XXVII § 1.3, le prédicteur d'Adamic–Adar (A)"),
    ("hasard-et-methode", 6): ("assemblage", "à juger", "", "", "signalée : le facteur de Bonferroni (1 240), un choix de cadre"),
    ("hasard-et-methode", 7): ("procédé court", "infirmé", SESSION, ARC3,
                               "pas une erreur des résultats (λ = 402 est bien lu, sur 7 lignes) ; une fragilité : un repli silencieux sur 410"),
}

sorties = json.load(open(os.path.join(REV, "sorties-agents-001.json"), encoding="utf-8"))["dossiers"]
lignes = []
for dossier, s in sorties.items():
    for rang, e in enumerate(s.get("erreurs_trouvees", []), 1):
        nature, verdict, juge, quand, raison = J[(dossier, rang)]
        lignes.append({"id": f"D{len(lignes) + 1:02d}", "dossier": dossier, "rang": rang, "leve_le": LEVE[dossier],
                       "fichier": e.get("fichier", ""), "affirmation": e.get("affirmation", ""), "nature": nature,
                       "verdict": verdict, "juge_par": juge, "juge_quand": quand, "raison": raison})
assert len(lignes) == len(J) == 45, len(lignes)

with open(os.path.join(REV, "drapeaux-001.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(lignes[0]))
    w.writeheader()
    w.writerows(lignes)

VERDICTS = ["confirmé", "infirmé", "à juger", "plan", "réglé ailleurs"]
print("| dossiers | drapeaux | " + " | ".join(VERDICTS) + " |")
for nom, groupe in (("longs", [x for x in lignes if x["dossier"] in LONGS]),
                    ("concis", [x for x in lignes if x["dossier"] not in LONGS]), ("tous", lignes)):
    c = collections.Counter(x["verdict"] for x in groupe)
    print(f"| {nom} | {len(groupe)} | " + " | ".join(str(c[v]) for v in VERDICTS) + " |")
print()
print("| nature | drapeaux | " + " | ".join(VERDICTS) + " |")
for nature in ["procédé court", "association", "assemblage", "référence", "plan"]:
    groupe = [x for x in lignes if x["nature"] == nature]
    c = collections.Counter(x["verdict"] for x in groupe)
    print(f"| {nature} | {len(groupe)} | " + " | ".join(str(c[v]) for v in VERDICTS) + " |")
print()
print("à confirmer par l'auteur :", ", ".join(x["id"] for x in lignes if x["juge_par"] == AUTEUR))
