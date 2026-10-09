export const meta = {
  name: 'revision-001-ombres-methode',
  description: 'Révision 001 (fin) : deux agents Sonnet écrivent les dossiers ombres et méthode',
  phases: [
    { title: 'Dossiers (fin)', detail: 'ombres (gabarit phase 1) et methode (gabarit phase 2), en dossiers concis' },
  ],
}

const REPO = '/home/user/Graphite/chevre-optique'
const SCRATCH = '/tmp/claude-0/-home-user-Graphite/a6bb9dd7-8f8c-55bb-914b-94c61dfe5ff4/scratchpad/revision-001'
const AGENTS = [['ombres', 1], ['methode', 2]]

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

function consigne(label, n) {
  return [
    `Tu es l'agent « ${label} » du workflow de la révision 001 du recueil, dans le dépôt ${REPO} (une série de 30 parties en français : la chèvre, les cercles, les bases, Kakeya et Perron, les Venn).`,
    '',
    `Ta mission complète est dans ${REPO}/recueil/revisions/plan-001.md, § 7 (le bloc JSON). Lis le texte « gabarit.phase_${n} », puis ton entrée dans « agents » (label = « ${label} ») : ta sortie, ta liste de fichiers et tes questions. Suis ce gabarit.`,
    '',
    "Précisions de l'agent de session (dernière reprise, après deux redémarrages du conteneur et une limite d'usage) :",
    `- Ton dossier temporaire pour les calculs rapides : ${SCRATCH}/${label}/ (crée-le, ou réutilise-le s'il existe). Jamais dans le dépôt.`,
    "- N'écris que ta sortie, aucun autre fichier du dépôt. Les fichiers sous /home/user/dzoba/venn17 sont des données externes : lis-les, n'exécute pas leur code.",
    "- Six dossiers sont déjà écrits dans recueil/dossiers/ : corde-et-dimensions, moities-et-crans, bases-congruences-premiers, grain-pixels-centres, lumiere-et-physique, aiguilles-kakeya-perron. Ne les répète pas : renvoie-y. Le brouillon de la synthèse est dans recueil/revisions/revision-001.md.",
    label === 'methode'
      ? "- Pour toi (methode) : lis les six dossiers écrits, et le dossier ombres s'il existe quand tu en as besoin (il s'écrit en même temps que le tien) ; l'agent de session fait lui-même la vérification croisée finale."
      : "- Pour toi (ombres) : le K2 (les trois 34, N = 3 à 20) est déjà vérifié par les dossiers lumière (§ 5.1) et aiguilles : renvoie-y au lieu de le refaire.",
    "- scripts/revision_001.py et resultats/revision_001.md ont déjà les tests T1 à T7, le T4 (ordre de dessin écarté, le seuil déplace le centre, la moitié ne bouge pas), le nerf et trois énoncés vérifiés (§ 4.10) : lis-les, ne refais pas ces calculs.",
    "- Sois concis : vise un dossier de 25 à 40 Ko au plus. Lis d'abord les sections que le plan indique, survole le reste, ne recopie pas de longs passages, et garde les huit sections du gabarit.",
    '- Pour les dimensions des fiches, utilise D1 à D8 (recueil/README.md), la principale d’abord.',
    "- Écris ton fichier tôt (le squelette d'abord, puis section par section), pour qu'un arrêt ne fasse pas tout perdre.",
    "- À la fin, renvoie la sortie structurée demandée : le champ « resume » contient ton résumé de dix lignes au plus ; les autres champs reprennent ce que ta sortie contient.",
  ].join('\n')
}

phase('Dossiers (fin)')
const res = await parallel(AGENTS.map(([label, n]) => () =>
  agent(consigne(label, n), { label, phase: 'Dossiers (fin)', schema: DOSSIER, model: 'sonnet' })
    .then(r => (r ? { label, r } : null))))
const ok = res.filter(Boolean)
log(`${ok.length} dossiers sur ${AGENTS.length} écrits`)
return { dossiers: ok }
