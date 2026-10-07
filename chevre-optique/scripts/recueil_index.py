"""
Le recueil : régénère l'index des observations et dit si une révision est due.

    python3 scripts/recueil_index.py

Lit recueil/observations/NNN-*.md (le tableau « champ | valeur » en tête de chaque fiche), écrit recueil/index.md et
recueil/index.csv, et compte :
- les fiches non révisées : une révision est due entre 11 et 15, en retard au-delà ;
- les arcs réponses depuis la dernière révision (recueil/arcs/arc-NNN.md) : une révision est due entre 10 et 16.
La dernière révision note les arcs qu'elle couvre sur sa première ligne : <!-- arcs: N -->.
"""

import csv
import glob
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(ICI, "..", "recueil")
CHAMPS = ["type", "statut", "partie", "document", "script", "données", "image", "dimension", "test", "arc", "révisé"]


def lire_fiche(chemin):
    with open(chemin, encoding="utf-8") as fh:
        lignes = fh.read().split("\n")
    titre = lignes[0].lstrip("# ").strip()
    champs = {}
    for l_ in lignes[1:40]:
        m = re.match(r"^\| ([^|]+?) \| (.*) \|$", l_)
        if m and m.group(1) not in ("champ", "---"):
            champs[m.group(1).strip()] = m.group(2).strip()
    return titre, champs


def sans_liens(t):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t).replace("`", "")


fiches = []
for chemin in sorted(glob.glob(os.path.join(REC, "observations", "[0-9][0-9][0-9]-*.md"))):
    titre, ch = lire_fiche(chemin)
    fiches.append((os.path.basename(chemin), titre, ch))

non_revisees = [f for f in fiches if f[2].get("révisé", "non").startswith("non")]
arcs = sorted(glob.glob(os.path.join(REC, "arcs", "arc-[0-9][0-9][0-9].md")))
revisions = sorted(glob.glob(os.path.join(REC, "revisions", "revision-[0-9][0-9][0-9].md")))
arcs_couverts = 0
if revisions:
    with open(revisions[-1], encoding="utf-8") as fh:
        m = re.search(r"<!-- arcs: (\d+) -->", fh.readline())
        arcs_couverts = int(m.group(1)) if m else 0
arcs_depuis = max(0, len(arcs) - arcs_couverts)

if len(non_revisees) > 15:
    etat = f"**révision en retard** : {len(non_revisees)} fiches non révisées (au-delà de 15)"
elif len(non_revisees) >= 11:
    etat = f"**révision due** : {len(non_revisees)} fiches non révisées (entre 11 et 15)"
elif 10 <= arcs_depuis <= 16:
    etat = f"**révision due** : {arcs_depuis} arcs depuis la dernière révision"
elif arcs_depuis > 16:
    etat = f"**révision en retard** : {arcs_depuis} arcs depuis la dernière révision"
else:
    etat = f"pas de révision due ({len(non_revisees)} fiches non révisées, {arcs_depuis} arcs depuis la dernière révision)"

md = ["# Index du recueil", "",
      "Régénéré par `python3 scripts/recueil_index.py` à partir des fiches de `observations/`. Le protocole est dans"
      " [CLAUDE.md, § 10](../CLAUDE.md) et [`README.md`](README.md).", "",
      f"- Fiches : {len(fiches)}, dont {len(non_revisees)} non révisées. Arcs réponses : {len(arcs)}"
      f" ({arcs_depuis} depuis la dernière révision). Révisions : {len(revisions)}.",
      f"- État : {etat}.", "",
      "| n° | observation | type | statut | partie | script | image | dimension | révisé |",
      "|---:|---|---|---|---|---|---|---|---|"]
for nom, titre, ch in fiches:
    num, txt = titre.split(" — ", 1) if " — " in titre else (nom[:3], titre)
    script = sans_liens(ch.get("script", "")).split(",")[0]
    image = sans_liens(ch.get("image", "—")).split(",")[0]
    md.append(f"| {num} | [{txt}](observations/{nom}) | {ch.get('type', '')} | {ch.get('statut', '').split(' (')[0]} |"
              f" {ch.get('partie', '')} | {script} | {image} | {ch.get('dimension', '').split(' ;')[0]} |"
              f" {ch.get('révisé', 'non')} |")
with open(os.path.join(REC, "index.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(md) + "\n")
with open(os.path.join(REC, "index.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["numero", "titre", "fichier"] + CHAMPS)
    for nom, titre, ch in fiches:
        num, txt = titre.split(" — ", 1) if " — " in titre else (nom[:3], titre)
        w.writerow([num, txt, f"observations/{nom}"] + [sans_liens(ch.get(c, "")) for c in CHAMPS])
print(f"{len(fiches)} fiches ({len(non_revisees)} non révisées), {len(arcs)} arcs ({arcs_depuis} depuis la dernière révision).")
print("État :", etat.replace("**", ""))
