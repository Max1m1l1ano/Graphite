export const meta = {
  name: 'revision-001-recueil',
  description: 'Révision 001 du recueil : un agent Sonnet par dossier thématique, puis une vérification croisée',
  phases: [
    { title: 'Dossiers', detail: 'un agent Sonnet par dossier : relit scripts, données et figures, écrit le dossier' },
    { title: 'Vérification croisée', detail: 'relit tous les dossiers : couverture, erreurs, liens entre dossiers, trous' },
  ],
}

const DOSSIER_SCHEMA = {"type": "object", "properties": {"fichier_ecrit": {"type": "string"}, "parties": {"type": "array", "items": {"type": "string"}}, "fiches": {"type": "array", "items": {"type": "object", "properties": {"numero": {"type": "string"}, "dimensions": {"type": "array", "items": {"type": "string"}}, "raison": {"type": "string"}}, "required": ["numero", "dimensions", "raison"]}}, "liens": {"type": "array", "items": {"type": "object", "properties": {"de": {"type": "string"}, "vers": {"type": "string"}, "nature": {"type": "string", "enum": ["même procédé", "congruence", "causalité", "corrélation", "analogie à tester", "hasard testé"]}, "partage_exact": {"type": "string"}, "transporte": {"type": "string"}, "ouvert": {"type": "string"}, "preuve": {"type": "string"}}, "required": ["de", "vers", "nature", "partage_exact", "preuve"]}}, "triangle_du_bas": {"type": "object", "properties": {"branches": {"type": "array", "items": {"type": "string"}}, "groupe_commun": {"type": "string"}, "disque": {"type": "string"}, "statut": {"type": "string"}}, "required": ["branches", "groupe_commun", "disque", "statut"]}, "obstructions": {"type": "array", "items": {"type": "object", "properties": {"elements": {"type": "array", "items": {"type": "string"}}, "ce_qui_ne_se_recolle_pas": {"type": "string"}, "trou": {"type": "string"}, "ou_chercher": {"type": "string"}}, "required": ["elements", "ce_qui_ne_se_recolle_pas", "trou"]}}, "nouveaux_tests": {"type": "array", "items": {"type": "object", "properties": {"nom": {"type": "string"}, "but": {"type": "string"}, "calcul": {"type": "string"}, "si_structure": {"type": "string"}, "si_hasard": {"type": "string"}, "resultat_rapide": {"type": "string"}}, "required": ["nom", "but", "calcul", "si_structure", "si_hasard"]}}, "trous_publies": {"type": "array", "items": {"type": "object", "properties": {"sujet": {"type": "string"}, "reference": {"type": "string"}, "statut": {"type": "string", "enum": ["référence sûre", "à vérifier"]}, "pourquoi": {"type": "string"}}, "required": ["sujet", "reference", "statut", "pourquoi"]}}, "observations_nouvelles": {"type": "array", "items": {"type": "object", "properties": {"titre": {"type": "string"}, "type": {"type": "string"}, "contexte": {"type": "string"}, "script": {"type": "string"}, "image": {"type": "string"}, "statut": {"type": "string"}}, "required": ["titre", "type", "contexte", "script", "statut"]}}, "erreurs_trouvees": {"type": "array", "items": {"type": "object", "properties": {"fichier": {"type": "string"}, "affirmation": {"type": "string"}, "probleme": {"type": "string"}}, "required": ["fichier", "affirmation", "probleme"]}}}, "required": ["fichier_ecrit", "parties", "fiches", "liens", "triangle_du_bas", "obstructions", "nouveaux_tests", "trous_publies", "observations_nouvelles", "erreurs_trouvees"]}
const VERIF_SCHEMA = {"type": "object", "properties": {"parties_sans_dossier": {"type": "array", "items": {"type": "string"}}, "fiches_sans_dossier": {"type": "array", "items": {"type": "string"}}, "erreurs": {"type": "array", "items": {"type": "object", "properties": {"dossier": {"type": "string"}, "affirmation": {"type": "string"}, "probleme": {"type": "string"}, "correction": {"type": "string"}}, "required": ["dossier", "affirmation", "probleme", "correction"]}}, "liens_entre_dossiers": {"type": "array", "items": {"type": "object", "properties": {"dossiers": {"type": "array", "items": {"type": "string"}}, "element_commun": {"type": "string"}, "nature": {"type": "string"}}, "required": ["dossiers", "element_commun", "nature"]}}, "trous_commentes": {"type": "array", "items": {"type": "object", "properties": {"dossiers": {"type": "array", "items": {"type": "string"}}, "trou": {"type": "string"}, "ou_chercher": {"type": "string"}}, "required": ["dossiers", "trou", "ou_chercher"]}}, "tests_prioritaires": {"type": "array", "items": {"type": "string"}}, "remarques": {"type": "string"}}, "required": ["parties_sans_dossier", "fiches_sans_dossier", "erreurs", "liens_entre_dossiers", "trous_commentes", "tests_prioritaires", "remarques"]}
const SCRATCH = '/tmp/claude-0/-home-user-Graphite/a6bb9dd7-8f8c-55bb-914b-94c61dfe5ff4/scratchpad/revision-001'
const REPO = '/home/user/Graphite/chevre-optique'

const tous = args.agents
const estDossier = a => typeof a.dossier === 'string' && a.dossier.startsWith('recueil/dossiers/')
const dossiers = tous.filter(estDossier)
const verifs = tous.filter(a => !estDossier(a))

const STRUCTURE = [
  '# Dossier : <titre>',
  '',
  'Révision 001 (2026-10-07). Plan : [plan-001.md](../revisions/plan-001.md). Synthèse : [revision-001.md](../revisions/revision-001.md).',
  '',
  '## La question directrice',
  '## Ce que le dossier englobe   (un tableau : partie | document | script | figures | résultats, avec des liens relatifs ../../)',
  '## Les fiches du recueil   (chaque fiche : son numéro, son lien ../observations/…, et ce qu’elle apporte ici)',
  '## Les branches et le triangle du bas   (les chaînes qui se rejoignent, le groupe ou le procédé commun, le disque où il se place)',
  '## Ce qui se recolle et ce qui ne se recolle pas   (les congruences, avec ce qui est partagé exactement, ce qui est transporté et ce qui reste ouvert ; puis les obstructions et le trou que chacune désigne)',
  '## Les nouveaux tests proposés',
  '## Les trous dans les données publiées',
  '## Sources',
].join('\n')

function promptDossier(a) {
  return [
    `Tu es l'agent « ${a.label} » de la révision 001 du recueil du dépôt ${REPO} (une série de 30 parties en français : la chèvre, les cercles, les bases, Kakeya et Perron, les Venn).`,
    '',
    `Ta tâche : écrire le dossier thématique ${a.dossier}.`,
    '',
    'Lis d’abord :',
    '- CLAUDE.md : les § 1 (une analogie soutenue par le même procédé est un résultat), 6, 6 bis et 10 (le recueil, la révision, le choix du test) ;',
    '- recueil/revisions/plan-001.md : la section de ton dossier, la structure « en Perron » et les congruences à tester ;',
    '- recueil/README.md et recueil/index.md.',
    '',
    'Puis lis ces fichiers (scripts, données, figures, documents, fiches) :',
    ...a.fichiers.map(f => `- ${f}`),
    '',
    'Réponds à ces questions dans le dossier :',
    ...a.questions.map((q, i) => `${i + 1}. ${q}`),
    '',
    'Règles :',
    `- Écris UN SEUL fichier, ${a.dossier}. Ne modifie aucun autre fichier du dépôt.`,
    `- Pour un calcul rapide, travaille dans ${SCRATCH}/${a.label}/ (crée-le) avec python3 ; ne lance pas de script lourd du dépôt.`,
    '- Chaque nombre doit venir d’un fichier resultats/… (cite-le) ou de ton calcul (mets le résultat dans le champ resultat_rapide du test). N’invente rien.',
    '- Vérifie chaque chemin avec ls avant de l’écrire.',
    '- Pour chaque lien, dis ce qui est partagé exactement, ce qui est transporté, et ce qui reste ouvert. Ne dis pas « coïncidence » sans avoir cherché le lien dans les parties (CLAUDE.md, § 6 bis) ; un hasard testé est un résultat, pas un mot à éviter.',
    '- Références : seulement celles dont tu es sûr ; sinon, marque « à vérifier ».',
    '- Français simple, phrases courtes. Si tu t’adresses à l’auteur, tutoie-le.',
    '',
    'Structure du dossier :',
    STRUCTURE,
    '',
    'Quand le fichier est écrit, renvoie la sortie structurée demandée. Dans « fiches », donne pour chaque fiche de ton dossier les dimensions (D1 à D8 du recueil) qu’elle touche vraiment, la principale d’abord, avec la raison.',
  ].join('\n')
}

function promptVerif(v, resume) {
  return [
    `Tu es l'agent de vérification croisée « ${v.label} » de la révision 001 du recueil du dépôt ${REPO}.`,
    '',
    `Ton rôle : ${v.dossier}.`,
    '',
    'Lis CLAUDE.md (§ 6, 6 bis et 10), recueil/revisions/plan-001.md, recueil/index.md, puis tous les fichiers de recueil/dossiers/.',
    'Lis aussi :',
    ...v.fichiers.map(f => `- ${f}`),
    '',
    'Réponds à ces questions :',
    ...v.questions.map((q, i) => `${i + 1}. ${q}`),
    '',
    'Voici le résumé des sorties des agents de dossier (JSON) :',
    resume,
    '',
    'Règles : ne modifie aucun fichier. Vérifie les nombres des dossiers contre les fichiers resultats/… cités. Signale chaque partie (I à XXX) et chaque fiche (001 à 015) qui ne tombe dans aucun dossier. Pour chaque trou, dis où chercher les données qui manquent.',
  ].join('\n')
}

phase('Dossiers')
const res = await parallel(dossiers.map(a => () =>
  agent(promptDossier(a), { label: a.label, phase: 'Dossiers', schema: DOSSIER_SCHEMA, model: 'sonnet' })
    .then(r => (r ? { label: a.label, dossier: a.dossier, r } : null))))
const ok = res.filter(Boolean)
log(`${ok.length} dossiers sur ${dossiers.length} écrits`)

phase('Vérification croisée')
const resume = JSON.stringify(ok.map(x => ({
  dossier: x.dossier, parties: x.r.parties, fiches: x.r.fiches.map(f => f.numero),
  triangle: x.r.triangle_du_bas, obstructions: x.r.obstructions,
})))
const vs = await parallel(verifs.map(v => () =>
  agent(promptVerif(v, resume), { label: v.label, phase: 'Vérification croisée', schema: VERIF_SCHEMA, model: 'sonnet' })))
return { dossiers: ok, verifications: vs.filter(Boolean) }
