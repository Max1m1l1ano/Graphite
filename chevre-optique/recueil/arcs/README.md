# Les arcs réponses : données brutes

Un **arc réponse** va d'un message de l'auteur à la réponse finale. Chaque message est une chaîne. On la classe d'abord dans une seule dimension (D1 à D8, voir [`../README.md`](../README.md)).

**À la fin de chaque arc, avant le message final à l'auteur**, on envoie un agent Sonnet (outil Agent, `model: "sonnet"`). Il relie cet arc et le précédent et exporte les données brutes de l'arc :
- `arc-NNN.md` : le récit ;
- `arc-NNN.csv` : une ligne par production.

## Colonnes de `arc-NNN.csv`

`arc, ordre, horodatage, message, script, entree, sortie, type_sortie, partie, dimension, observation, commit`

- `ordre` : rang chronologique dans l'arc (1, 2, 3…).
- `type_sortie` : `resultats`, `figure`, `document`, `fiche`, `config` (CLAUDE.md, README) ou `donnees_externes`.
- `observation` : le numéro de fiche du recueil, s'il y en a une.

## Gabarit de la demande à l'agent Sonnet

> Tu es l'agent de fin d'arc du dépôt `chevre-optique`. Lis `CLAUDE.md` (§ 10), `recueil/README.md`, le fichier de l'arc précédent (`recueil/arcs/arc-<N−1>.md`, s'il existe) et ce que l'arc a produit. La liste suit : les messages de l'auteur et un résumé de ce qui a été fait, les commits (`git log`), et les fichiers ajoutés ou modifiés (`git show --stat <commits>`). Puis écris :
>
> 1. **`recueil/arcs/arc-<N>.md`**, avec dans l'ordre :
>    - (a) le message de l'auteur, résumé, et sa dimension principale ;
>    - (b) les liens de continuité avec l'arc précédent : ce qui est repris, prolongé, corrigé ;
>    - (c) les scripts de l'arc, regroupés, et pour chacun les données qu'il produit ;
>    - (d) les chaînes de production de données (script → résultats → figures → document), dans l'ordre chronologique, chacune expliquée en deux ou trois phrases ;
>    - (e) un tableau script ↔ images ↔ documents ;
>    - (f) les observations du recueil nées pendant l'arc ;
>    - (g) le partage des aires : quelle part de chaque dimension l'arc a occupée, comparée à l'arc précédent, comme les régions d'un Venn des arcs ;
>    - (h) ce qui est resté ouvert.
> 2. **`recueil/arcs/arc-<N>.csv`**, avec les colonnes ci-dessus, une ligne par production.
>
> Ne modifie aucun autre fichier. Vérifie chaque chemin avec `ls` avant de l'écrire. Écris en français, simplement.
