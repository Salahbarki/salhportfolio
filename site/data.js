// data.js - Données du portfolio Salah Eddine Barki
const PROFILE = {
  name: "Salah Eddine Barki",
  title: "Technicien de Maintenance Industrielle",
  id: "4882-MT",
  contact: {
    location: "Amiens, France",
    phone: "+33 6 88 69 07 04",
    email: "salahbarki.seb@gmail.com",
    linkedin: "linkedin.com/in/salahbarki"
  },
  summary: "Technicien de maintenance industrielle senior avec plus de 10 ans d'expérience sur des équipements automatisés et mécaniques complexes : presses injection, lignes de production agroalimentaire (PET/canettes), bancs de test automobile et utilités industrielles. Compétences transverses : électrotechnique, automatisme (Siemens S7, TIA Portal), mécanique, hydraulique et pneumatique. Forte appétence pour le diagnostic structuré, l'analyse de pannes récurrentes et l'amélioration continue.",
  years: "10+",
  companies: 7,
  countries: 4,
  fiches: 6
};

const COMPETENCES = [
  {
    category: "Mécanique",
    icon: "settings_applications",
    description: "Diagnostic et réparation de systèmes de transmission, hydrauliques et pneumatiques complexes.",
    tags: ["Hydraulique", "Pneumatique", "Transmission", "Guidages", "Roulements"]
  },
  {
    category: "Électrique",
    icon: "electrical_services",
    description: "Habilitation basse tension, câblage industriel, et dépannage de variateurs de fréquence.",
    tags: ["BT/HT", "Schémas", "Variateurs", "Moteurs"]
  },
  {
    category: "Automatisme (PLC)",
    icon: "memory",
    description: "Programmation et diagnostic sur automates Siemens S7 et supervision de process.",
    tags: ["Siemens TIA", "Step 7", "Ladder", "PROFINET"]
  }
];

const CERTIFICATIONS = [
  { id: "CERT-H2023", name: "Habilitation Électrique BR/BC", status: "Validé", statusColor: "primary" },
  { id: "CACES-R489", name: "Chariots de manutention", status: "Validé", statusColor: "primary" },
  { id: "SST-2024", name: "Sauveteur Secouriste du Travail", status: "Recyclage en cours", statusColor: "secondary" }
];

const FICHES = [
  {
    num: "01",
    id: "INT-2024-001",
    titre: "Panne récurrente encartonneuse — Ligne PET",
    entreprise: "Coca-Cola Europacific Partners",
    lieu: "Grigny (91)",
    type: "CURATIF URGENT",
    typeColor: "secondary",
    date: "15 Juil 2024",
    duree: "00h 45m",
    tech: "4882-MT",
    equip: "Encartonneuse / casseuse de colis — Ligne remplissage bouteilles PET 2L — Cadence 60 000 b/h",
    contexte: "Ligne critique approvisionnant la grande distribution. Production 22h/jour. Tout arrêt >20 min = risque rupture de stock client.",
    symptome: "Défaut HMI n°402 'PRODUIT_COINCÉ_ENTRÉE' toutes les 8–12 min. Accumulation de 15–18 colis rejetés/heure en sortie fardeleuse. Opérateurs forcés de redémarrer manuellement à chaque arrêt.",
    diagnostic: `Vérification électrique : alimentation capteur photoélectrique d'entrée produit = 24 V stable. Signal logique oscillant anormalement : la diode de l'automate clignote au lieu de rester allumée fixe.

Analyse sur TIA Portal (programme automate Siemens) : dans le bloc de gestion encartonneuse, le bit de validation produit est conditionné directement par le signal capteur sans temporisation d'antirebond. L'oscillation du faisceau (probablement due à la condensation/buée ambiante près de la ligne froide) crée des fronts parasites interprétés comme des produits valides.

Vérification mécanique : jeu butée d'entrée produit anormalement large (environ 3 mm au lieu du réglage usuel ~0,5 mm). Amortisseur usé qui ne freine plus correctement le produit.

Vérification servo : en mode manuel, le pousseur arrive en butée 2–3 mm en retard par rapport à la consigne affichée sur l'écran. Dérive mécanique liée au jeu de la butée.`,
    actions: [
      "CONSIGNATION : Arrêt électrique + pneumatique de la zone. Condamnateur cadenas apposé. Signalisation verticale de zone de maintenance.",
      "ÉLECTRIQUE : Remplacement du capteur photoélectrique par un modèle plus robuste avec purge d'air intégrée (anti-buée), adapté à l'environnement humide proche de la ligne froide. Remplacement du câble d'alimentation par un câble blindé pour éviter les perturbations électromagnétiques des variateurs voisins. Vérification : signal désormais stable, diode automate allumée fixe.",
      "MÉCANIQUE : Dépose de la butée d'entrée. Remplacement de l'amortisseur hydraulique usé par un neuf. Recalage de la butée au jeu de 0,5 mm (vérifié à la cale/lame de 0,5 mm). Serrage de la boulonnerie au couple avec clé dynamométrique.",
      "AUTOMATISME (TIA Portal) : Ajout d'une temporisation de 50 ms dans le programme automate sur le signal du capteur avant validation du bit 'produit présent'. Cela filtre les oscillations parasites dues à l'humidité sans impacter le temps de cycle. Recalage du décalage servo-pousseur (ajustement du paramètre de position dans le variateur). Validation par mouvements manuels : le pousseur arrive pile en butée avec le convoyeur.",
      "ESSAIS : Démarrage de la ligne. Run de 45 min à cadence nominale. Comptage des rejets : 2 colis rejetés sur 45 min (contre 12–15 avant). Aucun arrêt forcé opérateur. Monitoring via l'écran HMI : le compteur de défaut 402 reste à 0.",
      "GMAO : Création d'un ordre de travail récurrent 'Contrôle capteur + butée encartonneuse' tous les 3 mois (au lieu de l'annuel constructeur). Mise à jour de la gamme de maintenance dans la base informatique du site."
    ],
    resultat: "Temps d'arrêt moyen réduit de ~40 min à 8 min (–80%). Taux de rejets divisé par 5 (17/h → 3/h). Zero arrêt forcé opérateur pendant les 3 semaines suivantes. Procédure de maintenance préventive mise à jour et appliquée sur les 3 autres lignes du site.",
    metriques: [
      { label: "MTTR Avant", value: "40 min", icon: "timer" },
      { label: "MTTR Après", value: "8 min", icon: "timer" },
      { label: "Rejets", value: "-80%", icon: "trending_down" },
      { label: "Disponibilité", value: "+12%", icon: "check_circle" }
    ],
    pieces: [
      { name: "Capteur photoélectrique anti-buée", ref: "N/A — Modèle avec purge", qty: 1 },
      { name: "Amortisseur hydraulique", ref: "Standard industriel", qty: 1 },
      { name: "Câble blindé 5 conducteurs", ref: "Standard", qty: 1 }
    ],
    outillage: ["Clé dynamométrique", "Multimètre", "TIA Portal", "Cales de réglage"]
  },
  {
    num: "02",
    id: "INT-2023-042",
    titre: "Mise en service presse injection + auxiliaires",
    entreprise: "TE Connectivity",
    lieu: "Tanger (Maroc)",
    type: "INSTALLATION",
    typeColor: "primary",
    date: "Juin 2023",
    duree: "02j 00h",
    tech: "4882-MT",
    equip: "Presse injection 120 tonnes + sécheur de granulés + trémie + détecteur de métal",
    contexte: "Relocalisation complète d'une cellule d'injection dans un nouveau hall de production. Objectif : production client automobile en J+2 (just-in-time, aucun stock tampon).",
    symptome: "Aucun — Nouvelle installation. Objectif : démarrage qualité premier jet, cycle stable <20 secondes.",
    diagnostic: "Analyse pré-installation : vérification de la compatibilité des arrivées électriques (400V triphasé + neutre + terre), hydrauliques (120 bar) et eau de refroidissement (20 °C). Plan de pose transmis par le constructeur. Vérification du niveau d'huile hydraulique et de la propreté des circuits.",
    actions: [
      "TRANSPORT & POSE : Dépose de l'outillage (moule 24 cavités) avant déplacement. Transport chariot élévateur avec fourches allongées et sangles de levage. Pose sur 4 plots anti-vibratoires. Nivellement au niveau à bulle puis affinage au laser (écart <0,2 mm sur toute la longueur). Alignement visuel de l'axe presse avec le convoyeur amont (cordeau + règle de mécanicien).",
      "RACCORDEMENTS ÉLECTRIQUE : branchement 400V tri + N + T via arrivée dédiée au tableau divisionnaire. Vérification terre au multimètre : résistance <1 Ω (conforme norme).",
      "RACCORDEMENTS HYDRAULIQUE : raccordement flexibles sur centrale hydraulique du hall. Serrage des raccords au couple. Essai pression statique 10% au-dessus de la nominale pendant 10 min : aucune fuite constatée.",
      "EAU REFROIDISSEMENT : raccordement circuits moule (fixe et mobile) sur tour aéroréfrigérant. Température consigne 80 °C côté fixe, 75 °C côté mobile. Débit contrôlé à la vanne : 8 L/min circuit A, 12 L/min circuit B.",
      "SÉCHEUR : Mise en service du sécheur de granulés plastiques. Objectif point de rosée ≤ –40 °C (matière PA66 très hygroscopique). Après 45 min de fonctionnement, lecture du point de rosée sur l'afficheur : –42 °C. Vérification à la sonde thermométrique : température air chauffé 80 °C en sortie vers trémie.",
      "DÉTECTEUR MÉTAL : Installation en amont de la trémie. Réglage de la sensibilité : test avec morceaux de fer, cuivre, aluminium. Validation : détection 10/10, aucun faux positif sur passage de granulés vides. Serrage des écrous de fixation + vérification blindage câble.",
      "PARAMÉTRAGE CYCLE : Réglage vitesse injection, pression de maintien, temps de refroidissement et ouverture moule selon la fiche de paramètres du moule (transmise par le bureau d'études). Premier cycle : réglage du coussin de fin de course. Batch test de 500 pièces.",
      "CONTRÔLE QUALITÉ : Mesure dimensionnelle des premières pièces au pied à coulisse digital (tolérance connecteur ±0,05 mm). Résultat : 0 pièce hors tolérance sur les 500.",
      "DOCUMENTATION & FORMATION : Rédaction du PV de recette (procès-verbal de mise en service) signé par Production + Qualité + Maintenance. Formation de 3 opérateurs : démarrage/arrêt, changement de référence (objectif 8 min), lecture des alarmes HMI."
    ],
    resultat: "Mise en production effective en J+2 (mardi matin après déménagement vendredi). Cycle stable mesuré : 18,5 s moyenne (objectif <20 s). 0 défaut qualité sur les 500 pièces de validation. Checklist de mise en service de 42 points créée et partagée à l'équipe : 2 autres presses relocalisées le trimestre suivant en réutilisant la même procédure.",
    metriques: [
      { label: "Délai", value: "J+2", icon: "event" },
      { label: "Cycle", value: "18.5 s", icon: "speed" },
      { label: "Qualité", value: "100%", icon: "verified" },
      { label: "Checklist", value: "42 pts", icon: "checklist" }
    ],
    pieces: [
      { name: "Plots anti-vibratoires", ref: "Standard", qty: 4 },
      { name: "Huile hydraulique ISO VG 46", ref: "Shell Tellus S2 MX", qty: 120 }
    ],
    outillage: ["Niveau laser", "Multimètre", "Débitmètre", "Pied à coulisse digital"]
  },
  {
    num: "03",
    id: "INT-2023-038",
    titre: "Débogage & optimisation programme automate",
    entreprise: "TE Connectivity",
    lieu: "Tanger (Maroc)",
    type: "AUTOMATISME",
    typeColor: "primary",
    date: "Mars 2023",
    duree: "04h 30m",
    tech: "4882-MT",
    equip: "Cellule assemblage connectique — Automate Siemens S7-1200 + HMI + servo",
    contexte: "Cellule critique assemblage connecteurs automobile. Cadence nominale 220 pièces/heure. OEE mensuel affiché en baisse (72% vs objectif 85%).",
    symptome: "Temps de cycle mesuré au chronomètre : 28–30 s au lieu des 16–17 s nominaux. Alarme HMI fréquente 'Timeout bras robot zone pick'. Arrêts 3–4 fois par heure. Opérateurs obligés de redémarrer manuellement (perte ~2 min à chaque fois).",
    diagnostic: `Connexion sur TIA Portal en ligne avec l'automate. Monitoring des blocs de programme.

Le temps d'exécution du bloc de gestion robot est anormalement long (8 secondes mesurées sur l'outil de diagnostic intégré, contre 3–4 s attendu).

Analyse pas à pas du programme : une temporisation de sécurité est réglée à 8 secondes alors que le mouvement réel du bras robot dure environ 5,5 s (mesuré au chronomètre et confirmé par le suivi des signaux d'entrées/sorties). La temporisation est donc trop conservative et bloque inutilement la suite du cycle.

Bit de validation 'pince OK' : capteur de proximité qui détecte la pièce clignote légèrement au lieu d'être fixe. Inspection mécanique : le support du capteur est légèrement desserré (jeu de 2 mm). Le capteur détecte parfois, parfois pas => le programme attend indéfiniment le signal stable.

Programmation non optimisée : les mouvements du bras sont strictement séquentiels (un à la fois) alors que certains mouvements compatibles pourraient être faits en parallèle (ex: monter le bras tout en le déplaçant latéralement, avec sécurité de hauteur).`,
    actions: [
      "MÉCANIQUE : Réglage du support capteur de proximité. Resserrement de l'écrou de fixation au couple (contre-écrou nylstop pour éviter le desserrage). Vérification : le signal 'pince OK' est désormais stable et fixe (diode verte allumée en continu).",
      "PROGRAMMATION TIA PORTAL : Ajustement de la temporisation de sécurité : réduction de 8 s à 6,5 s (marge de sécurité de 1 s au-dessus du temps mesuré réel 5,5 s). Ajout d'une petite temporisation d'antirebond de 35 ms sur le signal capteur dans le programme pour éliminer les éventuelles micro-oscillations résiduelles.",
      "OPTIMISATION CODE : Réécriture partielle du bloc de gestion mouvements : parallélisation des phases compatibles (descente + fermeture pince ; montée + translation latérale avec interlock de hauteur pour la sécurité). Suppression de temporisations redondantes.",
      "SURVEILLANCE : Ajout d'un compteur de cycles dans le programme avec alarme automatique si le temps moyen dépasse 10% de la valeur nominale (détection précoce de dérive).",
      "HMI : Création d'un écran de diagnostic 'Temps de cycle' affichant le temps réel, la moyenne glissante sur 50 cycles, et le nombre d'alarmes 'Timeout'. Accessible aux opérateurs pour monitoring autonome.",
      "SÉCURITÉ & DOCUMENTATION : Sauvegarde du programme modifié sur le serveur du site avec commentaires détaillés dans chaque section (date, nature modif, nom). Export papier du bloc modifié pour classeur maintenance.",
      "VALIDATION : Run de 4 heures à cadence max. Monitoring temps cycle via HMI et chronomètre externe. Résultats : 16,2 s (min) — 16,8 s (moyenne) — 17,1 s (max). Aucune alarme 'Timeout' durant les 4 heures."
    ],
    resultat: "Temps de cycle moyen : 28,5 s → 16,8 s (–41%). Capacité effective passée de ~126 à 214 pièces/heure. OEE cellule : 72% → 84% (+12 points). Alarme 'Timeout' : 3–4 arrêts/h → 0 sur 4 h test, puis <1 arrêt/h en production continue. Maintenance autonome sur ces paramètres désormais (formation interne réalisée).",
    metriques: [
      { label: "Cycle Avant", value: "28.5 s", icon: "timer" },
      { label: "Cycle Après", value: "16.8 s", icon: "timer" },
      { label: "OEE", value: "+12 pts", icon: "trending_up" },
      { label: "Capacité", value: "+70%", icon: "speed" }
    ],
    pieces: [
      { name: "Écrou nylstop M8", ref: "Standard", qty: 2 }
    ],
    outillage: ["TIA Portal V16", "Chronomètre", "Clé dynamométrique micro", "Multimètre"]
  },
  {
    num: "04",
    id: "INT-2022-017",
    titre: "Analyse cause racine — Banc de test électrique",
    entreprise: "Kromberg & Schubert",
    lieu: "Kénitra (Maroc)",
    type: "RCA & QUALITÉ",
    typeColor: "secondary",
    date: "Nov 2022",
    duree: "01j 00h",
    tech: "4882-MT",
    equip: "Banc de test électrique (continuité, isolation, résistance) — Ligne faisceaux 32 voies",
    contexte: "Ligne faisceaux moteur pour client automobile. Production 2 000 pièces/jour. Just-in-time : aucun stock tampon autorisé. Tolérance client <2% de rebut test.",
    symptome: "Taux de rejet test continuité anormal : 12% sur une même référence produite depuis plusieurs jours sans changement d'outillage. Normalement stable autour de 1–2%. Conséquence : 240+ pièces rebutées/jour. Risque blocage ligne client.",
    diagnostic: `Analyse des données de test des 15 derniers jours (extraites du système informatique du banc) : dérive lente et progressive de la résistance mesurée au test de continuité. Tolérance : <10 mΩ. Valeurs de départ 3–5 mΩ → dérive progressive 8–12 mΩ → dépassement du seuil = rebut.

Pareto des causes de rebut sur 342 pièces rebutées : ~2/3 liés aux broches de contact du connecteur adaptateur du banc (pins), 1/4 liés aux câbles de piquage usés, le reste divers.

Inspection visuelle des pins : 14 des 32 pins présentent une oxydation noire visible (couche de CuO). Cause probable : absence de nettoyage régulier des pins dans la gamme de maintenance (le dernier nettoyage n'était pas documenté, probablement >6 mois).

Hotte d'extraction des fumées de soudure au poste amont : filtre saturé, débit d'aspiration faible (mesuré au débitmètre : 80 m³/h au lieu des ~120 m³/h nécessaires). Les fumées de soudure contenant des résidus de flux dérivent vers le banc de test et contaminent progressivement les contacts.

Mesure au micro-ohmètre : pins oxydés = 15–45 mΩ. Pins nettoyés à la brosse + alcool = <2 mΩ.`,
    actions: [
      "ARRÊT & TRI : Arrêt immédiat du banc de test. Consignation électrique 24V + 500V isolation. Signalisation. Récupération du batch produit depuis la dernière validation qualité OK : retri manuel complet. 94% des pièces déclarées bonnes après contrôle visuel + test au micro-ohmètre portable, 6% rebut confirmé.",
      "REMPLACEMENT CONNECTEUR : Dépose du jeu de pins oxydés. Pose d'un connecteur adaptateur neuf (référence constructeur du banc). Serrage des bagues de verrouillage.",
      "RÉGLAGE MÉCANIQUE : Vérin de mise en position du banc : réglage de la pression d'air de 3,2 bar à 4,0 bar (lu sur le manomètre intégré). Vérification à la jauge analogique : 4,0 bar ±0,1. Test de 50 insertions/retraits : aucune marque sur le plastique (pas de déformation des broches).",
      "MAINTENANCE EXTRACTION : Remplacement du filtre charbon de la hotte d'aspiration. Nettoyage de la roue du ventilateur. Graissage des paliers. Mesure post-intervention : débit remonté à 130 m³/h (>120 requis). Ajout d'une hotte aspirante mobile en renfort ponctuel sur le poste de soudure amont pour réduire la dérive à la source.",
      "MODIFICATION PROCÉDURE & GMAO : Modification de la gamme de maintenance préventive : ajout d'un nettoyage des pins de test à la brosse fibre de verre + alcool isopropylique toutes les 2 semaines (au lieu de jamais/non documenté). Ajout d'un contrôle qualité mensuel : mesure au micro-ohmètre sur 5 pins choisies au hasard. Seuil d'alerte <5 mΩ.",
      "FORMATION : Création fiche réflexe opérateur : si dérive >6 mΩ sur 3 tests consécutifs → arrêt immédiat + appel maintenance. Formation de 2 opérateurs + 1 technicien à la nouvelle procédure.",
      "CONTRÔLE RÉGULIER : Mise en place d'un test gabarit 32/32 pins tous les matins avant démarrage de la ligne (détection précoce oxydation ou déformation mécanique)."
    ],
    resultat: "Taux de rejet test continuité : 12,3% → 1,1% moyenne sur 30 jours (stable sous le seuil client 2%). Économie : ~220 pièces/jour sauvées. Procédure RCA formalisée (diagramme Ishikawa + 5 pourquoi) partagée aux 4 lignes test du site et aux sous-traitants internes. Temps de contrôle qualité départ réduit de 25 min/batch à 10 min/batch.",
    metriques: [
      { label: "Rejet Avant", value: "12.3%", icon: "warning" },
      { label: "Rejet Après", value: "1.1%", icon: "check_circle" },
      { label: "Pièces/jour", value: "+220", icon: "trending_up" },
      { label: "Temps QC", value: "-60%", icon: "timer" }
    ],
    pieces: [
      { name: "Connecteur adaptateur 32 voies", ref: "Constructeur banc", qty: 1 },
      { name: "Filtre charbon hotte", ref: "500×300×50 mm F7", qty: 1 }
    ],
    outillage: ["Micro-ohmètre", "Débitmètre", "Brosse fibre de verre", "Manomètre"]
  },
  {
    num: "05",
    id: "INT-2024-089",
    titre: "Dépannage hydraulique presse découpe / pliage",
    entreprise: "Sovireso",
    lieu: "Saint-Laurent-sur-Sèvre (85)",
    type: "CURATIF MÉCANIQUE",
    typeColor: "secondary",
    date: "Avr 2024",
    duree: "03h 20m",
    tech: "4882-MT",
    equip: "Presse hydraulique découpe/pliage — Vérin double effet Ø100/70 mm — Centrale 80 bar",
    contexte: "Machine unique sur site pour découpe tôlerie fine (acier 0,8–2 mm, inox 1–1,5 mm). Pas de machine de remplacement. Programme client : 480 pièces/jour.",
    symptome: "Perte brutale de pression lors de la descente rapide vers position pliage. Manomètre principal : chute de 80 bar à ~30 bar. Bruit violent type 'coup de bélier' à chaque inversion descente/montée. Arrêt machine. Production interrompue depuis 2 heures.",
    diagnostic: `Mesures aux manomètres multi-points :
- Pression côté pompe (amont filtre) : 80 bar stable.
- Pression côté descente (amont vérin tige) : 32 bar (anormal, devrait être ~78–80 bar).
- Pression côté montée : 78 bar (normal).
→ Panne localisée côté circuit descente.

Auscultation au stéthoscope mécanique : bruit de coup de bélier localisé au niveau de l'accumulateur hydropneumatique côté montée. Fréquence synchrone avec l'inversion du cycle.

Démontage du clapet anti-retour sur la ligne de descente : présence d'un petit morceau de joint torique écrasé coincé dans le siège du clapet (corps étranger). Le joint du clapet est partiellement dégradé, probablement à cause de la température de l'huile plus élevée que la normale.

Température huile mesurée au thermomètre de cuve : 68 °C (normalement <55 °C en exploitation régulière). Cause surchauffe : le filtre de retour est très encrassé (noir et plein de limaille) => la pompe force dans un circuit bouché => surchauffe + dégradation des joints.

Vérification de l'accumulateur hydropneumatique : précharge d'azote mesurée au manomètre de contrôle = 12 bar (normalement ~65 bar pour ce modèle). La membrane interne est visiblement fissurée (trace d'huile dans la partie gaz lors du démontage de contrôle).`,
    actions: [
      "CONSIGNATION & VIDANGE : Arrêt moteur pompe au disjoncteur. Condamnateur cadenas + panneau 'Ne pas démarrer — Maintenance'. Vidange des 120 L d'huile dans bac de récupération homologué.",
      "CLAPET ANTI-RETOUR : Dépose complète du clapet de la ligne descente. Nettoyage du siège en carbure à la pâte à roder (grain fin) jusqu'à surface plane et brillante. Test d'étanchéité : remplissage au kérosène, aucune goutte ne passe en 30 secondes. Remplacement du joint torique et du joint plat d'étanchéité par des neufs. Remontage : serrage croisé des vis au couple (clé dynamométrique).",
      "ACCUMULATEUR : Remplacement complet de l'accumulateur (vase + précharge). Précharge vérifiée au manomètre de contrôle : 65 bar. Contrôle 24 h après : aucune perte de pression (étanchéité OK).",
      "FILTRATION : Remplacement du filtre retour (très noir et encrassé) par un neuf. Remplacement du filtre d'aspiration. Remplissage huile neuve conforme spécification constructeur (viscosité ISO VG 46). Purge du circuit par 10 cycles lents sans charge (montée/descente manuelle lente) pour évacuer l'air.",
      "POMPE : Dépose partielle pour inspection des palettes internes. Jeu latéral mesuré au comparateur : 0,12 mm (tolérance max constructeur 0,15 mm). => Acceptable, mais programmation d'une révision dans 6 mois (préventif opportuniste).",
      "MISE EN PRESSION : Montée progressive par paliers (20 bar → 40 bar → 80 bar), 5 min à chaque palier pour détecter d'éventuelles fuites. Contrôle aux raccords avec papier absorbant : aucune fuite. Température huile après 30 min de fonctionnement : 48 °C (OK).",
      "ESSAIS SOUS CHARGE : Découpe de tôle acier 2 mm, 50 cycles continus. Pression affichée : 80 bar stable ±2 bar sur tout le cycle. Disparition complète des coups de bélier (vérifié au stéthoscope + capteur vibration portable)."
    ],
    resultat: "Intervention réalisée en 3 h 20 (prévision constructeur 1 journée = 7 h). Production relancée le jour même. Pression rétablie à 80 bar stable sur cycle complet descente/montée/pliage. À-coups hydrauliques supprimés. Maintenance préventive avancée : remplacement huile + filtres programmés avec 2 mois d'avance. Révision pompe programmée dans la GMAO.",
    metriques: [
      { label: "Durée", value: "3h20", icon: "timer" },
      { label: "Prévision", value: "7h00", icon: "schedule" },
      { label: "Pression", value: "80 bar", icon: "speed" },
      { label: "Temp.", value: "48 °C", icon: "thermostat" }
    ],
    pieces: [
      { name: "Joint torique clapet", ref: "NBR 90SH Ø12×2", qty: 1 },
      { name: "Accumulateur hydropneumatique", ref: "HAB 1-330", qty: 1 },
      { name: "Filtre retour 25 µm", ref: "MP Filtri", qty: 1 },
      { name: "Huile hydraulique ISO VG 46", ref: "Shell Tellus S2 MX", qty: 120 }
    ],
    outillage: ["Clé dynamométrique", "Stéthoscope mécanique", "Comparateur", "Manomètre de contrôle"]
  },
  {
    num: "06",
    id: "INT-2023-015",
    titre: "Planification maintenance annuelle & pilotage GMAO",
    entreprise: "TE Connectivity",
    lieu: "Tanger (Maroc)",
    type: "PLANIFICATION",
    typeColor: "primary",
    date: "Jan–Déc 2023",
    duree: "12 mois",
    tech: "4882-MT",
    equip: "Site industriel complet : 142 équipements (injection, assemblage, test, utilités, bâtiment)",
    contexte: "Site de 450 personnes, production 24h/5j. Objectif groupe : taux réalisation maintenance préventive >90% et réduction arrêts imprévus de 25% sur l'exercice.",
    symptome: "Taux réalisation maintenance préventive année N : 68% (233 ordres de travail réalisés sur 342 planifiés). Les arrêts imprévus représentent 23% du temps de production disponible. Coût maintenance en croissance +12% par rapport au budget. MTBF moyen site : 420 heures (benchmark industrie connectique ~650 h).",
    diagnostic: `Analyse des données de la GMAO et de la supervision des 12 derniers mois :
- 342 ordres de travail préventifs planifiés, 233 réalisés (68%), 109 reportés.
- Pareto des causes de report : ~45% = conflit avec production (pas de fenêtre machine disponible), ~30% = pièces détachées non disponibles (délai d'approvisionnement 5–7 jours), ~15% = sous-traitant spécialisé indisponible.

Absence de classification des équipements par criticité : tous traités avec la même priorité. Exemple : le compresseur d'air 8 bar (critique, arrêt = arrêt tout le site) et un éclairage de bureau avaient la même fréquence de préventif. Le temps de maintenance était mal réparti.

Analyse MTBF par famille d'équipements : presses injection 380 h (faible), bancs test 620 h (moyen), utilités 850 h (bon). Aucun plan d'action spécifique sur les presses.`,
    actions: [
      "COLLECTE & ANALYSE : Export des données GMAO (ordres réalisés, reports, coûts). Export des données supervision (arrêts, codes défauts, durées). Croisement dans Excel avec tableau de bord simplifié (graphiques tendance, top 5 pannes du mois).",
      "CLASSIFICATION CRITICITÉ ABC (méthode RCM simplifiée) : Classe A (14% des équipements, ~20 machines) = critique production + sécurité + environnement. → Préventif mensuel ou bimestriel. Stock de pièces critiques en local (capteurs de rechange, vannes, joints courants). Ex : presses injection, compresseur air principal, tour aéroréfrigérant principal. Classe B (32%, ~45 machines) = important mais remplaçable ou redondant. → Préventif trimestriel. Approvisionnement pièces sous 48 h. Classe C (54%, ~77 machines) = standard / non critique. → Préventif semestriel ou annuel. Curatif à la demande.",
      "PLANNING ANNUEL INTÉGRÉ : Création du planning 12 mois dans la GMAO avec fenêtres fixes négociées avec le chef de production : samedi matin (4 h pour A), arrêts planifiés trimestriels (8 h pour grandes révisions), périodes de vacances (révisions lourdes). Les conflits production ont chuté de 45% à 8%.",
      "APPROVISIONNEMENT : Négociation avec fournisseurs locaux pour réduire les délais. Création d'un stock de sécurité classe A (capteurs inductifs et photoélectriques de remplacement, vannes 5/2, joints toriques standards). Délai moyen pièces critiques : 5 j → 2 j.",
      "SOUS-TRAITANCE : Regroupement des interventions par lots (ex: thermographie annuelle, étalonnage des instruments, révision des pompes spécialisées). Appel d'offres 3 fournisseurs. Réduction des coûts sous-traitance : –18%.",
      "PILOTAGE KPI : Création d'un tableau de bord mensuel affiché au local maintenance et partagé avec la production : taux de réalisation du préventif (%), MTBF (heures) et MTTR (minutes) par classe d'équipement, coût maintenance par tonne produite, top 3 pannes du mois + actions en cours.",
      "PROJETS D'AMÉLIORATION : Élaboration et soumission de 5 projets d'amélioration : remplacement de 2 variateurs obsolètes, mise en place d'un suivi vibration sur 3 groupes critiques, formation interne automatisme pour 3 techniciens. 3 projets sur 5 validés par la direction et réalisés en interne."
    ],
    resultat: "Taux de réalisation préventif : 68% → 94% (année N+1), objectif groupe 90% dépassé. Arrêts imprévus : –28% vs année N (production gagne ~340 heures/an de disponibilité). MTBF site : 420 h → 610 h (+45%), rapproché du benchmark industrie. Coûts maintenance : –15% sous-traitance (achats groupés) et –8% pièces (stock optimisé + négociation). 3 projets amélioration réalisés en interne avec retour sur investissement <18 mois.",
    metriques: [
      { label: "Préventif", value: "68%→94%", icon: "check_circle" },
      { label: "Arrêts", value: "-28%", icon: "trending_down" },
      { label: "MTBF", value: "+45%", icon: "speed" },
      { label: "Coûts", value: "-15%", icon: "savings" }
    ],
    pieces: [],
    outillage: ["Excel", "GMAO SAP PM", "Power BI", "Tableau de bord KPI"]
  }
];
