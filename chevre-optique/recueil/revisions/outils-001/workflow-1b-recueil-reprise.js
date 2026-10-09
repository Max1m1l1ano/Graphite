export const meta = {
  name: 'revision-001-recueil',
  description: 'Révision 001 du recueil : sept agents Sonnet écrivent les dossiers, puis deux agents de vérification croisée',
  phases: [
    { title: 'Dossiers', detail: 'sept agents Sonnet, un par dossier thématique (plan-001.md, § 7)' },
    { title: 'Vérification croisée', detail: 'le dossier hasard-et-méthode et la vérification croisée' },
  ],
}

const REPO = '/home/user/Graphite/chevre-optique'
const SCRATCH = '/tmp/claude-0/-home-user-Graphite/a6bb9dd7-8f8c-55bb-914b-94c61dfe5ff4/scratchpad/revision-001'
const P1 = ['corde', 'moities', 'bases', 'grain', 'lumiere', 'aiguilles', 'ombres']
const P2 = ['methode']   // la vérification croisée est faite par l'agent de session, après le redémarrage du conteneur
const CONCIS = ['lumiere', 'aiguilles', 'ombres', 'methode']

const S = { type: 'string' }
const LISTE = { type: 'array', items: { type: 'string' } }
const NOUVELLE_FICHE = {
  type: 'object',
  properties: { titre: S, type: S, statut: S, partie: S, script: S, image: S, dimension: S, contexte: S, observation: S },
  required: ['titre', 'type', 'statut', 'partie', 'script', 'dimension', 'observation'],
}
const ERREUR = { type: 'object', properties: { fichier: S, affirmation: S, probleme: S }, required: ['fichier', 'affirmation', 'probleme'] }
const DOSSIER = {
  type: 'object',
  properties: {
    fichier_ecrit: S,
    resume: S,
    fiches: { type: 'array', items: { type: 'object', properties: { numero: S, dimensions: LISTE, verdict: S, raison: S }, required: ['numero', 'dimensions', 'verdict'] } },
    corrections_recouvrement: {
      type: 'object',
      properties: { ajouter_parties: LISTE, retirer_parties: LISTE, ajouter_fiches: LISTE, retirer_fiches: LISTE, raisons: S },
      required: ['ajouter_parties', 'retirer_parties', 'ajouter_fiches', 'retirer_fiches', 'raisons'],
    },
    nouvelles_fiches: { type: 'array', items: NOUVELLE_FICHE },
    congruences: { type: 'array', items: { type: 'object', properties: { id: S, elements: LISTE, verdict: S, detail: S }, required: ['elements', 'verdict', 'detail'] } },
    obstructions: { type: 'array', items: { type: 'object', properties: { elements: LISTE, trou: S, ou_chercher: S }, required: ['elements', 'trou'] } },
    code_test: S,
    references: { type: 'array', items: { type: 'object', properties: { reference: S, statut: { type: 'string', enum: ['sûre', 'à vérifier'] } }, required: ['reference', 'statut'] } },
    erreurs_trouvees: { type: 'array', items: ERREUR },
  },
  required: ['fichier_ecrit', 'resume', 'fiches', 'corrections_recouvrement', 'nouvelles_fiches', 'congruences', 'obstructions', 'code_test', 'references', 'erreurs_trouvees'],
}
const CROISEMENT = {
  type: 'object',
  properties: {
    fichier_ecrit: S,
    resume: S,
    recouvrement_v2: { type: 'array', items: { type: 'object', properties: { dossier: S, parties: LISTE, fiches: LISTE }, required: ['dossier', 'parties', 'fiches'] } },
    triangles_vides: { type: 'array', items: { type: 'object', properties: { dossiers: LISTE, trou: S, ou_chercher: S }, required: ['dossiers', 'trou'] } },
    contradictions: { type: 'array', items: { type: 'object', properties: { dossiers: LISTE, probleme: S, correction: S }, required: ['dossiers', 'probleme', 'correction'] } },
    arbres_corriges: { type: 'array', items: { type: 'object', properties: { arbre: S, correction: S }, required: ['arbre', 'correction'] } },
    nouvelles_fiches: { type: 'array', items: { ...NOUVELLE_FICHE, properties: { ...NOUVELLE_FICHE.properties, proposee_par: S } } },
    erreurs_trouvees: { type: 'array', items: ERREUR },
  },
  required: ['fichier_ecrit', 'resume', 'recouvrement_v2', 'triangles_vides', 'contradictions', 'arbres_corriges', 'nouvelles_fiches', 'erreurs_trouvees'],
}

function consigne(label, n, extra) {
  return [
    `Tu es l'agent « ${label} » (phase ${n}) du workflow de la révision 001 du recueil, dans le dépôt ${REPO} (une série de 30 parties en français : la chèvre, les cercles, les bases, Kakeya et Perron, les Venn).`,
    '',
    `Ta mission complète est dans ${REPO}/recueil/revisions/plan-001.md, § 7 (le bloc JSON). Lis le texte « gabarit.phase_${n} », puis ton entrée dans « agents » (label = « ${label} ») : ta sortie, ta liste de fichiers et tes questions. Suis ce gabarit à la lettre.`,
    '',
    "Précisions de l'agent de session :",
    `- Ton dossier temporaire pour les calculs rapides : ${SCRATCH}/${label}/ (crée-le). Jamais dans le dépôt.`,
    "- N'écris que ta sortie, aucun autre fichier du dépôt. Les fichiers sous /home/user/dzoba/venn17 sont des données externes : lis-les, n'exécute pas leur code.",
    "- scripts/revision_001.py a déjà les sections 1, 2.1, 4.1 et 4.2 (la diagonale √2 et Thalès, le cadre qui fabrique des liens, la base 10 et 1/7, la dérive des dizaines de premiers) : lis-le, ne refais pas ces calculs.",
    '- Pour les dimensions des fiches, utilise D1 à D8 (recueil/README.md), la principale d’abord.',
    "- À la fin, renvoie la sortie structurée demandée : le champ « resume » contient ton résumé de dix lignes au plus ; les autres champs reprennent ce que ta sortie contient.",
    CONCIS.includes(label) ? [
      '',
      "Reprise après un redémarrage du conteneur : le temps compte. Les dossiers déjà écrits (corde-et-dimensions, moities-et-crans, bases-congruences-premiers, grain-pixels-centres) sont dans recueil/dossiers/ : ne les répète pas, renvoie-y.",
      "Sois concis : vise un dossier de 25 à 40 Ko au plus. Lis d'abord les sections que le plan indique, survole le reste, ne recopie pas de longs passages, et garde les huit sections du gabarit.",
    ].join('\n') : '',
    extra || '',
  ].join('\n')
}

phase('Dossiers')
const r1 = await parallel(P1.map(label => () =>
  agent(consigne(label, 1), { label, phase: 'Dossiers', schema: DOSSIER, model: 'sonnet' })
    .then(r => (r ? { label, r } : null))))
const ok1 = r1.filter(Boolean)
log(`${ok1.length} dossiers sur ${P1.length} écrits`)

phase('Vérification croisée')
const resume = JSON.stringify(ok1.map(x => ({
  label: x.label,
  fichier: x.r.fichier_ecrit,
  resume: x.r.resume,
  corrections_recouvrement: x.r.corrections_recouvrement,
  fiches: x.r.fiches.map(f => ({ numero: f.numero, dimensions: f.dimensions, verdict: f.verdict })),
  nouvelles_fiches: x.r.nouvelles_fiches.map(f => `${f.titre} (${f.dimension} ; ${f.statut})`),
  obstructions: x.r.obstructions.map(o => `${o.elements.join(', ')} : ${o.trou}`),
})))
const extra = `\nRésumé JSON des sorties des sept agents de la phase 1 (les dossiers eux-mêmes sont dans ${REPO}/recueil/dossiers/) :\n${resume}`
const r2 = await parallel(P2.map(label => () =>
  agent(consigne(label, 2, extra), { label, phase: 'Vérification croisée', schema: label === 'croisement' ? CROISEMENT : DOSSIER, model: 'sonnet' })
    .then(r => (r ? { label, r } : null))))
return { phase1: ok1, phase2: r2.filter(Boolean) }
