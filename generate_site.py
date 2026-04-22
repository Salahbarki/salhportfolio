# generate_site.py - Génère le site portfolio interactif complet
import os

OUTPUT_DIR = r"C:\Users\ba2rb\Downloads\salpre\site"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# DONNÉES
# ============================================================
PROFILE = {
    "name": "Salah Eddine Barki",
    "title": "Technicien de Maintenance Industrielle",
    "id": "4882-MT",
    "contact": {
        "location": "Amiens, France",
        "phone": "+33 6 88 69 07 04",
        "email": "salahbarki.seb@gmail.com",
        "linkedin": "linkedin.com/in/salahbarki"
    },
    "summary": "Technicien de maintenance industrielle senior avec plus de 10 ans d'expérience sur des équipements automatisés et mécaniques complexes : presses injection, lignes de production agroalimentaire (PET/canettes), bancs de test automobile et utilités industrielles. Compétences transverses : électrotechnique, automatisme (Siemens S7, TIA Portal), mécanique, hydraulique et pneumatique.",
    "years": "10+",
    "companies": 7,
    "countries": 4,
    "fiches": 6
}

COMPETENCES = [
    {
        "category": "Mécanique",
        "icon": "settings_applications",
        "description": "Diagnostic et réparation de systèmes de transmission, hydrauliques et pneumatiques complexes.",
        "tags": ["Hydraulique", "Pneumatique", "Transmission", "Guidages", "Roulements"]
    },
    {
        "category": "Électrique",
        "icon": "electrical_services",
        "description": "Habilitation basse tension, câblage industriel, et dépannage de variateurs de fréquence.",
        "tags": ["BT/HT", "Schémas", "Variateurs", "Moteurs"]
    },
    {
        "category": "Automatisme (PLC)",
        "icon": "memory",
        "description": "Programmation et diagnostic sur automates Siemens S7 et supervision de process.",
        "tags": ["Siemens TIA", "Step 7", "Ladder", "PROFINET"]
    }
]

CERTIFICATIONS = [
    {"id": "CERT-H2023", "name": "Habilitation Électrique BR/BC", "status": "Validé", "statusColor": "primary"},
    {"id": "CACES-R489", "name": "Chariots de manutention", "status": "Validé", "statusColor": "primary"},
    {"id": "SST-2024", "name": "Sauveteur Secouriste du Travail", "status": "Recyclage en cours", "statusColor": "secondary"}
]

FICHES = [
    {
        "num": "01", "id": "INT-2024-001", "titre": "Panne récurrente encartonneuse — Ligne PET",
        "entreprise": "Coca-Cola Europacific Partners", "lieu": "Grigny (91)",
        "type": "CURATIF URGENT", "typeColor": "secondary",
        "date": "15 Juil 2024", "duree": "00h 45m", "tech": "4882-MT",
        "equip": "Encartonneuse / casseuse de colis — Ligne remplissage bouteilles PET 2L — Cadence 60 000 b/h",
        "contexte": "Ligne critique approvisionnant la grande distribution. Production 22h/jour. Tout arrêt >20 min = risque rupture de stock client.",
        "symptome": "Défaut HMI n°402 'PRODUIT_COINCÉ_ENTRÉE' toutes les 8–12 min. Accumulation de 15–18 colis rejetés/heure en sortie fardeleuse. Opérateurs forcés de redémarrer manuellement à chaque arrêt.",
        "diagnostic": """Vérification électrique : alimentation capteur photoélectrique d'entrée produit = 24 V stable. Signal logique oscillant anormalement : la diode de l'automate clignote au lieu de rester allumée fixe.

Analyse sur TIA Portal (programme automate Siemens) : dans le bloc de gestion encartonneuse, le bit de validation produit est conditionné directement par le signal capteur sans temporisation d'antirebond. L'oscillation du faisceau (probablement due à la condensation/buée ambiante près de la ligne froide) crée des fronts parasites interprétés comme des produits valides.

Vérification mécanique : jeu butée d'entrée produit anormalement large (environ 3 mm au lieu du réglage usuel ~0,5 mm). Amortisseur usé qui ne freine plus correctement le produit.

Vérification servo : en mode manuel, le pousseur arrive en butée 2–3 mm en retard par rapport à la consigne affichée sur l'écran. Dérive mécanique liée au jeu de la butée.""",
        "actions": [
            "CONSIGNATION : Arrêt électrique + pneumatique de la zone. Condamnateur cadenas apposé. Signalisation verticale de zone de maintenance.",
            "ÉLECTRIQUE : Remplacement du capteur photoélectrique par un modèle plus robuste avec purge d'air intégrée (anti-buée), adapté à l'environnement humide proche de la ligne froide. Remplacement du câble d'alimentation par un câble blindé pour éviter les perturbations électromagnétiques des variateurs voisins. Vérification : signal désormais stable, diode automate allumée fixe.",
            "MÉCANIQUE : Dépose de la butée d'entrée. Remplacement de l'amortisseur hydraulique usé par un neuf. Recalage de la butée au jeu de 0,5 mm (vérifié à la cale/lame de 0,5 mm). Serrage de la boulonnerie au couple avec clé dynamométrique.",
            "AUTOMATISME (TIA Portal) : Ajout d'une temporisation de 50 ms dans le programme automate sur le signal du capteur avant validation du bit 'produit présent'. Cela filtre les oscillations parasites dues à l'humidité sans impacter le temps de cycle. Recalage du décalage servo-pousseur (ajustement du paramètre de position dans le variateur). Validation par mouvements manuels : le pousseur arrive pile en butée avec le convoyeur.",
            "ESSAIS : Démarrage de la ligne. Run de 45 min à cadence nominale. Comptage des rejets : 2 colis rejetés sur 45 min (contre 12–15 avant). Aucun arrêt forcé opérateur. Monitoring via l'écran HMI : le compteur de défaut 402 reste à 0.",
            "GMAO : Création d'un ordre de travail récurrent 'Contrôle capteur + butée encartonneuse' tous les 3 mois (au lieu de l'annuel constructeur). Mise à jour de la gamme de maintenance dans la base informatique du site."
        ],
        "resultat": "Temps d'arrêt moyen réduit de ~40 min à 8 min (–80%). Taux de rejets divisé par 5 (17/h → 3/h). Zero arrêt forcé opérateur pendant les 3 semaines suivantes. Procédure de maintenance préventive mise à jour et appliquée sur les 3 autres lignes du site.",
        "metriques": [
            {"label": "MTTR Avant", "value": "40 min", "icon": "timer"},
            {"label": "MTTR Après", "value": "8 min", "icon": "timer"},
            {"label": "Rejets", "value": "–80%", "icon": "trending_down"},
            {"label": "Dispo.", "value": "+12%", "icon": "check_circle"}
        ],
        "pieces": [
            {"name": "Capteur photoélectrique anti-buée", "ref": "Modèle avec purge", "qty": 1},
            {"name": "Amortisseur hydraulique", "ref": "Standard industriel", "qty": 1},
            {"name": "Câble blindé 5 conducteurs", "ref": "Standard", "qty": 1}
        ],
        "outillage": ["Clé dynamométrique", "Multimètre", "TIA Portal", "Cales de réglage"]
    },
    {
        "num": "02", "id": "INT-2023-042", "titre": "Mise en service presse injection + auxiliaires",
        "entreprise": "TE Connectivity", "lieu": "Tanger (Maroc)",
        "type": "INSTALLATION", "typeColor": "primary",
        "date": "Juin 2023", "duree": "02j 00h", "tech": "4882-MT",
        "equip": "Presse injection 120 tonnes + sécheur de granulés + trémie + détecteur de métal",
        "contexte": "Relocalisation complète d'une cellule d'injection dans un nouveau hall de production. Objectif : production client automobile en J+2 (just-in-time, aucun stock tampon).",
        "symptome": "Aucun — Nouvelle installation. Objectif : démarrage qualité premier jet, cycle stable <20 secondes.",
        "diagnostic": "Analyse pré-installation : vérification de la compatibilité des arrivées électriques (400V triphasé + neutre + terre), hydrauliques (120 bar) et eau de refroidissement (20 °C). Plan de pose transmis par le constructeur. Vérification du niveau d'huile hydraulique et de la propreté des circuits.",
        "actions": [
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
        "resultat": "Mise en production effective en J+2 (mardi matin après déménagement vendredi). Cycle stable mesuré : 18,5 s moyenne (objectif <20 s). 0 défaut qualité sur les 500 pièces de validation. Checklist de mise en service de 42 points créée et partagée à l'équipe : 2 autres presses relocalisées le trimestre suivant en réutilisant la même procédure.",
        "metriques": [
            {"label": "Délai", "value": "J+2", "icon": "event"},
            {"label": "Cycle", "value": "18.5 s", "icon": "speed"},
            {"label": "Qualité", "value": "100%", "icon": "verified"},
            {"label": "Checklist", "value": "42 pts", "icon": "checklist"}
        ],
        "pieces": [
            {"name": "Plots anti-vibratoires", "ref": "Standard", "qty": 4},
            {"name": "Huile hydraulique ISO VG 46", "ref": "Shell Tellus S2 MX", "qty": 120}
        ],
        "outillage": ["Niveau laser", "Multimètre", "Débitmètre", "Pied à coulisse digital"]
    },
    {
        "num": "03", "id": "INT-2023-038", "titre": "Débogage & optimisation programme automate",
        "entreprise": "TE Connectivity", "lieu": "Tanger (Maroc)",
        "type": "AUTOMATISME", "typeColor": "primary",
        "date": "Mars 2023", "duree": "04h 30m", "tech": "4882-MT",
        "equip": "Cellule assemblage connectique — Automate Siemens S7-1200 + HMI + servo",
        "contexte": "Cellule critique assemblage connecteurs automobile. Cadence nominale 220 pièces/heure. OEE mensuel affiché en baisse (72% vs objectif 85%).",
        "symptome": "Temps de cycle mesuré au chronomètre : 28–30 s au lieu des 16–17 s nominaux. Alarme HMI fréquente 'Timeout bras robot zone pick'. Arrêts 3–4 fois par heure. Opérateurs obligés de redémarrer manuellement (perte ~2 min à chaque fois).",
        "diagnostic": """Connexion sur TIA Portal en ligne avec l'automate. Monitoring des blocs de programme.

Le temps d'exécution du bloc de gestion robot est anormalement long (8 secondes mesurées sur l'outil de diagnostic intégré, contre 3–4 s attendu).

Analyse pas à pas du programme : une temporisation de sécurité est réglée à 8 secondes alors que le mouvement réel du bras robot dure environ 5,5 s (mesuré au chronomètre et confirmé par le suivi des signaux d'entrées/sorties). La temporisation est donc trop conservative et bloque inutilement la suite du cycle.

Bit de validation 'pince OK' : capteur de proximité qui détecte la pièce clignote légèrement au lieu d'être fixe. Inspection mécanique : le support du capteur est légèrement desserré (jeu de 2 mm). Le capteur détecte parfois, parfois pas => le programme attend indéfiniment le signal stable.

Programmation non optimisée : les mouvements du bras sont strictement séquentiels (un à la fois) alors que certains mouvements compatibles pourraient être faits en parallèle (ex: monter le bras tout en le déplaçant latéralement, avec sécurité de hauteur).""",
        "actions": [
            "MÉCANIQUE : Réglage du support capteur de proximité. Resserrement de l'écrou de fixation au couple (contre-écrou nylstop pour éviter le desserrage). Vérification : le signal 'pince OK' est désormais stable et fixe (diode verte allumée en continu).",
            "PROGRAMMATION TIA PORTAL : Ajustement de la temporisation de sécurité : réduction de 8 s à 6,5 s (marge de sécurité de 1 s au-dessus du temps mesuré réel 5,5 s). Ajout d'une petite temporisation d'antirebond de 35 ms sur le signal capteur dans le programme pour éliminer les éventuelles micro-oscillations résiduelles.",
            "OPTIMISATION CODE : Réécriture partielle du bloc de gestion mouvements : parallélisation des phases compatibles (descente + fermeture pince ; montée + translation latérale avec interlock de hauteur pour la sécurité). Suppression de temporisations redondantes.",
            "SURVEILLANCE : Ajout d'un compteur de cycles dans le programme avec alarme automatique si le temps moyen dépasse 10% de la valeur nominale (détection précoce de dérive).",
            "HMI : Création d'un écran de diagnostic 'Temps de cycle' affichant le temps réel, la moyenne glissante sur 50 cycles, et le nombre d'alarmes 'Timeout'. Accessible aux opérateurs pour monitoring autonome.",
            "SÉCURITÉ & DOCUMENTATION : Sauvegarde du programme modifié sur le serveur du site avec commentaires détaillés dans chaque section (date, nature modif, nom). Export papier du bloc modifié pour classeur maintenance.",
            "VALIDATION : Run de 4 heures à cadence max. Monitoring temps cycle via HMI et chronomètre externe. Résultats : 16,2 s (min) — 16,8 s (moyenne) — 17,1 s (max). Aucune alarme 'Timeout' durant les 4 heures."
        ],
        "resultat": "Temps de cycle moyen : 28,5 s → 16,8 s (–41%). Capacité effective passée de ~126 à 214 pièces/heure. OEE cellule : 72% → 84% (+12 points). Alarme 'Timeout' : 3–4 arrêts/h → 0 sur 4 h test, puis <1 arrêt/h en production continue. Maintenance autonome sur ces paramètres désormais (formation interne réalisée).",
        "metriques": [
            {"label": "Cycle Avant", "value": "28.5 s", "icon": "timer"},
            {"label": "Cycle Après", "value": "16.8 s", "icon": "timer"},
            {"label": "OEE", "value": "+12 pts", "icon": "trending_up"},
            {"label": "Capacité", "value": "+70%", "icon": "speed"}
        ],
        "pieces": [{"name": "Écrou nylstop M8", "ref": "Standard", "qty": 2}],
        "outillage": ["TIA Portal V16", "Chronomètre", "Clé dynamométrique micro", "Multimètre"]
    },
    {
        "num": "04", "id": "INT-2022-017", "titre": "Analyse cause racine — Banc de test électrique",
        "entreprise": "Kromberg & Schubert", "lieu": "Kénitra (Maroc)",
        "type": "RCA & QUALITÉ", "typeColor": "secondary",
        "date": "Nov 2022", "duree": "01j 00h", "tech": "4882-MT",
        "equip": "Banc de test électrique (continuité, isolation, résistance) — Ligne faisceaux 32 voies",
        "contexte": "Ligne faisceaux moteur pour client automobile. Production 2 000 pièces/jour. Just-in-time : aucun stock tampon autorisé. Tolérance client <2% de rebut test.",
        "symptome": "Taux de rejet test continuité anormal : 12% sur une même référence produite depuis plusieurs jours sans changement d'outillage. Normalement stable autour de 1–2%. Conséquence : 240+ pièces rebutées/jour. Risque blocage ligne client.",
        "diagnostic": """Analyse des données de test des 15 derniers jours (extraites du système informatique du banc) : dérive lente et progressive de la résistance mesurée au test de continuité. Tolérance : <10 mΩ. Valeurs de départ 3–5 mΩ → dérive progressive 8–12 mΩ → dépassement du seuil = rebut.

Pareto des causes de rebut sur 342 pièces rebutées : ~2/3 liés aux broches de contact du connecteur adaptateur du banc (pins), 1/4 liés aux câbles de piquage usés, le reste divers.

Inspection visuelle des pins : 14 des 32 pins présentent une oxydation noire visible (couche de CuO). Cause probable : absence de nettoyage régulier des pins dans la gamme de maintenance (le dernier nettoyage n'était pas documenté, probablement >6 mois).

Hotte d'extraction des fumées de soudure au poste amont : filtre saturé, débit d'aspiration faible (mesuré au débitmètre : 80 m³/h au lieu des ~120 m³/h nécessaires). Les fumées de soudure contenant des résidus de flux dérivent vers le banc de test et contaminent progressivement les contacts.

Mesure au micro-ohmètre : pins oxydés = 15–45 mΩ. Pins nettoyés à la brosse + alcool = <2 mΩ.""",
        "actions": [
            "ARRÊT & TRI : Arrêt immédiat du banc de test. Consignation électrique 24V + 500V isolation. Signalisation. Récupération du batch produit depuis la dernière validation qualité OK : retri manuel complet. 94% des pièces déclarées bonnes après contrôle visuel + test au micro-ohmètre portable, 6% rebut confirmé.",
            "REMPLACEMENT CONNECTEUR : Dépose du jeu de pins oxydés. Pose d'un connecteur adaptateur neuf (référence constructeur du banc). Serrage des bagues de verrouillage.",
            "RÉGLAGE MÉCANIQUE : Vérin de mise en position du banc : réglage de la pression d'air de 3,2 bar à 4,0 bar (lu sur le manomètre intégré). Vérification à la jauge analogique : 4,0 bar ±0,1. Test de 50 insertions/retraits : aucune marque sur le plastique (pas de déformation des broches).",
            "MAINTENANCE EXTRACTION : Remplacement du filtre charbon de la hotte d'aspiration. Nettoyage de la roue du ventilateur. Graissage des paliers. Mesure post-intervention : débit remonté à 130 m³/h (>120 requis). Ajout d'une hotte aspirante mobile en renfort ponctuel sur le poste de soudure amont pour réduire la dérive à la source.",
            "MODIFICATION PROCÉDURE & GMAO : Modification de la gamme de maintenance préventive : ajout d'un nettoyage des pins de test à la brosse fibre de verre + alcool isopropylique toutes les 2 semaines (au lieu de jamais/non documenté). Ajout d'un contrôle qualité mensuel : mesure au micro-ohmètre sur 5 pins choisies au hasard. Seuil d'alerte <5 mΩ.",
            "FORMATION : Création fiche réflexe opérateur : si dérive >6 mΩ sur 3 tests consécutifs → arrêt immédiat + appel maintenance. Formation de 2 opérateurs + 1 technicien à la nouvelle procédure.",
            "CONTRÔLE RÉGULIER : Mise en place d'un test gabarit 32/32 pins tous les matins avant démarrage de la ligne (détection précoce oxydation ou déformation mécanique)."
        ],
        "resultat": "Taux de rejet test continuité : 12,3% → 1,1% moyenne sur 30 jours (stable sous le seuil client 2%). Économie : ~220 pièces/jour sauvées. Procédure RCA formalisée (diagramme Ishikawa + 5 pourquoi) partagée aux 4 lignes test du site et aux sous-traitants internes. Temps de contrôle qualité départ réduit de 25 min/batch à 10 min/batch.",
        "metriques": [
            {"label": "Rejet Avant", "value": "12.3%", "icon": "warning"},
            {"label": "Rejet Après", "value": "1.1%", "icon": "check_circle"},
            {"label": "Pièces/jour", "value": "+220", "icon": "trending_up"},
            {"label": "Temps QC", "value": "-60%", "icon": "timer"}
        ],
        "pieces": [
            {"name": "Connecteur adaptateur 32 voies", "ref": "Constructeur banc", "qty": 1},
            {"name": "Filtre charbon hotte", "ref": "500×300×50 mm F7", "qty": 1}
        ],
        "outillage": ["Micro-ohmètre", "Débitmètre", "Brosse fibre de verre", "Manomètre"]
    },
    {
        "num": "05", "id": "INT-2024-089", "titre": "Dépannage hydraulique presse découpe / pliage",
        "entreprise": "Sovireso", "lieu": "Saint-Laurent-sur-Sèvre (85)",
        "type": "CURATIF MÉCANIQUE", "typeColor": "secondary",
        "date": "Avr 2024", "duree": "03h 20m", "tech": "4882-MT",
        "equip": "Presse hydraulique découpe/pliage — Vérin double effet Ø100/70 mm — Centrale 80 bar",
        "contexte": "Machine unique sur site pour découpe tôlerie fine (acier 0,8–2 mm, inox 1–1,5 mm). Pas de machine de remplacement. Programme client : 480 pièces/jour.",
        "symptome": "Perte brutale de pression lors de la descente rapide vers position pliage. Manomètre principal : chute de 80 bar à ~30 bar. Bruit violent type 'coup de bélier' à chaque inversion descente/montée. Arrêt machine. Production interrompue depuis 2 heures.",
        "diagnostic": """Mesures aux manomètres multi-points :
- Pression côté pompe (amont filtre) : 80 bar stable.
- Pression côté descente (amont vérin tige) : 32 bar (anormal, devrait être ~78–80 bar).
- Pression côté montée : 78 bar (normal).
→ Panne localisée côté circuit descente.

Auscultation au stéthoscope mécanique : bruit de coup de bélier localisé au niveau de l'accumulateur hydropneumatique côté montée. Fréquence synchrone avec l'inversion du cycle.

Démontage du clapet anti-retour sur la ligne de descente : présence d'un petit morceau de joint torique écrasé coincé dans le siège du clapet (corps étranger). Le joint du clapet est partiellement dégradé, probablement à cause de la température de l'huile plus élevée que la normale.

Température huile mesurée au thermomètre de cuve : 68 °C (normalement <55 °C en exploitation régulière). Cause surchauffe : le filtre de retour est très encrassé (noir et plein de limaille) => la pompe force dans un circuit bouché => surchauffe + dégradation des joints.

Vérification de l'accumulateur hydropneumatique : précharge d'azote mesurée au manomètre de contrôle = 12 bar (normalement ~65 bar pour ce modèle). La membrane interne est visiblement fissurée (trace d'huile dans la partie gaz lors du démontage de contrôle).""",
        "actions": [
            "CONSIGNATION & VIDANGE : Arrêt moteur pompe au disjoncteur. Condamnateur cadenas + panneau 'Ne pas démarrer — Maintenance'. Vidange des 120 L d'huile dans bac de récupération homologué.",
            "CLAPET ANTI-RETOUR : Dépose complète du clapet de la ligne descente. Nettoyage du siège en carbure à la pâte à roder (grain fin) jusqu'à surface plane et brillante. Test d'étanchéité : remplissage au kérosène, aucune goutte ne passe en 30 secondes. Remplacement du joint torique et du joint plat d'étanchéité par des neufs. Remontage : serrage croisé des vis au couple (clé dynamométrique).",
            "ACCUMULATEUR : Remplacement complet de l'accumulateur (vase + précharge). Précharge vérifiée au manomètre de contrôle : 65 bar. Contrôle 24 h après : aucune perte de pression (étanchéité OK).",
            "FILTRATION : Remplacement du filtre retour (très noir et encrassé) par un neuf. Remplacement du filtre d'aspiration. Remplissage huile neuve conforme spécification constructeur (viscosité ISO VG 46). Purge du circuit par 10 cycles lents sans charge (montée/descente manuelle lente) pour évacuer l'air.",
            "POMPE : Dépose partielle pour inspection des palettes internes. Jeu latéral mesuré au comparateur : 0,12 mm (tolérance max constructeur 0,15 mm). => Acceptable, mais programmation d'une révision dans 6 mois (préventif opportuniste).",
            "MISE EN PRESSION : Montée progressive par paliers (20 bar → 40 bar → 80 bar), 5 min à chaque palier pour détecter d'éventuelles fuites. Contrôle aux raccords avec papier absorbant : aucune fuite. Température huile après 30 min de fonctionnement : 48 °C (OK).",
            "ESSAIS SOUS CHARGE : Découpe de tôle acier 2 mm, 50 cycles continus. Pression affichée : 80 bar stable ±2 bar sur tout le cycle. Disparition complète des coups de bélier (vérifié au stéthoscope + capteur vibration portable)."
        ],
        "resultat": "Intervention réalisée en 3 h 20 (prévision constructeur 1 journée = 7 h). Production relancée le jour même. Pression rétablie à 80 bar stable sur cycle complet descente/montée/pliage. À-coups hydrauliques supprimés. Maintenance préventive avancée : remplacement huile + filtres programmés avec 2 mois d'avance. Révision pompe programmée dans la GMAO.",
        "metriques": [
            {"label": "Durée", "value": "3h20", "icon": "timer"},
            {"label": "Prévision", "value": "7h00", "icon": "schedule"},
            {"label": "Pression", "value": "80 bar", "icon": "speed"},
            {"label": "Temp.", "value": "48 °C", "icon": "thermostat"}
        ],
        "pieces": [
            {"name": "Joint torique clapet", "ref": "NBR 90SH Ø12×2", "qty": 1},
            {"name": "Accumulateur hydropneumatique", "ref": "HAB 1-330", "qty": 1},
            {"name": "Filtre retour 25 µm", "ref": "MP Filtri", "qty": 1},
            {"name": "Huile hydraulique ISO VG 46", "ref": "Shell Tellus S2 MX", "qty": 120}
        ],
        "outillage": ["Clé dynamométrique", "Stéthoscope mécanique", "Comparateur", "Manomètre de contrôle"]
    },
    {
        "num": "06", "id": "INT-2023-015", "titre": "Planification maintenance annuelle & pilotage GMAO",
        "entreprise": "TE Connectivity", "lieu": "Tanger (Maroc)",
        "type": "PLANIFICATION", "typeColor": "primary",
        "date": "Jan–Déc 2023", "duree": "12 mois", "tech": "4882-MT",
        "equip": "Site industriel complet : 142 équipements (injection, assemblage, test, utilités, bâtiment)",
        "contexte": "Site de 450 personnes, production 24h/5j. Objectif groupe : taux réalisation maintenance préventive >90% et réduction arrêts imprévus de 25% sur l'exercice.",
        "symptome": "Taux réalisation maintenance préventive année N : 68% (233 ordres de travail réalisés sur 342 planifiés). Les arrêts imprévus représentent 23% du temps de production disponible. Coût maintenance en croissance +12% par rapport au budget. MTBF moyen site : 420 heures (benchmark industrie connectique ~650 h).",
        "diagnostic": """Analyse des données de la GMAO et de la supervision des 12 derniers mois :
- 342 ordres de travail préventifs planifiés, 233 réalisés (68%), 109 reportés.
- Pareto des causes de report : ~45% = conflit avec production (pas de fenêtre machine disponible), ~30% = pièces détachées non disponibles (délai d'approvisionnement 5–7 jours), ~15% = sous-traitant spécialisé indisponible.

Absence de classification des équipements par criticité : tous traités avec la même priorité. Exemple : le compresseur d'air 8 bar (critique, arrêt = arrêt tout le site) et un éclairage de bureau avaient la même fréquence de préventif. Le temps de maintenance était mal réparti.

Analyse MTBF par famille d'équipements : presses injection 380 h (faible), bancs test 620 h (moyen), utilités 850 h (bon). Aucun plan d'action spécifique sur les presses.""",
        "actions": [
            "COLLECTE & ANALYSE : Export des données GMAO (ordres réalisés, reports, coûts). Export des données supervision (arrêts, codes défauts, durées). Croisement dans Excel avec tableau de bord simplifié (graphiques tendance, top 5 pannes du mois).",
            "CLASSIFICATION CRITICITÉ ABC (méthode RCM simplifiée) : Classe A (14% des équipements, ~20 machines) = critique production + sécurité + environnement. → Préventif mensuel ou bimestriel. Stock de pièces critiques en local (capteurs de rechange, vannes, joints courants). Ex : presses injection, compresseur air principal, tour aéroréfrigérant principal. Classe B (32%, ~45 machines) = important mais remplaçable ou redondant. → Préventif trimestriel. Approvisionnement pièces sous 48 h. Classe C (54%, ~77 machines) = standard / non critique. → Préventif semestriel ou annuel. Curatif à la demande.",
            "PLANNING ANNUEL INTÉGRÉ : Création du planning 12 mois dans la GMAO avec fenêtres fixes négociées avec le chef de production : samedi matin (4 h pour A), arrêts planifiés trimestriels (8 h pour grandes révisions), périodes de vacances (révisions lourdes). Les conflits production ont chuté de 45% à 8%.",
            "APPROVISIONNEMENT : Négociation avec fournisseurs locaux pour réduire les délais. Création d'un stock de sécurité classe A (capteurs inductifs et photoélectriques de remplacement, vannes 5/2, joints toriques standards). Délai moyen pièces critiques : 5 j → 2 j.",
            "SOUS-TRAITANCE : Regroupement des interventions par lots (ex: thermographie annuelle, étalonnage des instruments, révision des pompes spécialisées). Appel d'offres 3 fournisseurs. Réduction des coûts sous-traitance : –18%.",
            "PILOTAGE KPI : Création d'un tableau de bord mensuel affiché au local maintenance et partagé avec la production : taux de réalisation du préventif (%), MTBF (heures) et MTTR (minutes) par classe d'équipement, coût maintenance par tonne produite, top 3 pannes du mois + actions en cours.",
            "PROJETS D'AMÉLIORATION : Élaboration et soumission de 5 projets d'amélioration : remplacement de 2 variateurs obsolètes, mise en place d'un suivi vibration sur 3 groupes critiques, formation interne automatisme pour 3 techniciens. 3 projets sur 5 validés par la direction et réalisés en interne."
        ],
        "resultat": "Taux de réalisation préventif : 68% → 94% (année N+1), objectif groupe 90% dépassé. Arrêts imprévus : –28% vs année N (production gagne ~340 heures/an de disponibilité). MTBF site : 420 h → 610 h (+45%), rapproché du benchmark industrie. Coûts maintenance : –15% sous-traitance (achats groupés) et –8% pièces (stock optimisé + négociation). 3 projets amélioration réalisés en interne avec retour sur investissement <18 mois.",
        "metriques": [
            {"label": "Préventif", "value": "68%→94%", "icon": "check_circle"},
            {"label": "Arrêts", "value": "-28%", "icon": "trending_down"},
            {"label": "MTBF", "value": "+45%", "icon": "speed"},
            {"label": "Coûts", "value": "-15%", "icon": "savings"}
        ],
        "pieces": [],
        "outillage": ["Excel", "GMAO SAP PM", "Power BI", "Tableau de bord KPI"]
    }
]

# ============================================================
# HEADER COMMUN (Tailwind Config + Nav)
# ============================================================
COMMON_HEAD = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Work+Sans:wght@700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<style>
    .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }}
    .material-symbols-outlined.filled {{ font-variation-settings: 'FILL' 1; }}
</style>
<script id="tailwind-config">
    tailwind.config = {{
        darkMode: "class",
        theme: {{
            extend: {{
                "colors": {{
                    "surface-container": "#eceeee",
                    "primary-container": "#1b4f72",
                    "on-error-container": "#93000a",
                    "on-tertiary-fixed-variant": "#3a4856",
                    "primary-fixed": "#cce5ff",
                    "on-secondary": "#ffffff",
                    "inverse-surface": "#2e3131",
                    "surface-dim": "#d8dada",
                    "on-surface-variant": "#41474e",
                    "on-secondary-fixed": "#351000",
                    "tertiary": "#283643",
                    "on-secondary-container": "#5c2000",
                    "on-primary-fixed-variant": "#154b6d",
                    "outline": "#72787f",
                    "surface": "#f8fafa",
                    "surface-container-high": "#e6e8e8",
                    "surface-bright": "#f8fafa",
                    "primary": "#003857",
                    "surface-container-lowest": "#ffffff",
                    "error-container": "#ffdad6",
                    "surface-container-low": "#f2f4f4",
                    "secondary": "#a23f00",
                    "surface-tint": "#326286",
                    "inverse-primary": "#9dcbf4",
                    "on-primary-fixed": "#001e31",
                    "tertiary-container": "#3e4d5a",
                    "on-background": "#191c1d",
                    "primary-fixed-dim": "#9dcbf4",
                    "on-tertiary-container": "#aebdcd",
                    "on-tertiary": "#ffffff",
                    "outline-variant": "#c1c7cf",
                    "on-secondary-fixed-variant": "#7c2e00",
                    "error": "#ba1a1a",
                    "surface-variant": "#e1e3e3",
                    "tertiary-fixed": "#d5e4f5",
                    "on-error": "#ffffff",
                    "background": "#f8fafa",
                    "on-primary-container": "#92c0e9",
                    "surface-container-highest": "#e1e3e3",
                    "secondary-fixed-dim": "#ffb595",
                    "on-surface": "#191c1d",
                    "secondary-container": "#fc7127",
                    "on-primary": "#ffffff",
                    "on-tertiary-fixed": "#0e1d29",
                    "inverse-on-surface": "#eff1f1",
                    "secondary-fixed": "#ffdbcd",
                    "tertiary-fixed-dim": "#b9c8d8"
                }},
                "borderRadius": {{
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
                }},
                "spacing": {{
                    "stack-sm": "8px",
                    "unit": "4px",
                    "margin": "40px",
                    "gutter": "24px",
                    "stack-md": "16px",
                    "container-max": "1200px",
                    "stack-lg": "32px"
                }},
                "fontFamily": {{
                    "h2": ["Inter"],
                    "data-mono": ["Inter"],
                    "h3": ["Inter"],
                    "label-caps": ["Work Sans"],
                    "body-md": ["Inter"],
                    "body-lg": ["Inter"],
                    "h1": ["Inter"]
                }},
                "fontSize": {{
                    "h2": ["32px", {{"lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "600"}}],
                    "data-mono": ["14px", {{"lineHeight": "1.4", "fontWeight": "500"}}],
                    "h3": ["24px", {{"lineHeight": "1.3", "fontWeight": "600"}}],
                    "label-caps": ["12px", {{"lineHeight": "1", "letterSpacing": "0.1em", "fontWeight": "700"}}],
                    "body-md": ["16px", {{"lineHeight": "1.5", "fontWeight": "400"}}],
                    "body-lg": ["18px", {{"lineHeight": "1.6", "fontWeight": "400"}}],
                    "h1": ["48px", {{"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700"}}]
                }}
            }}
        }}
    }}
</script>
</head>
'''

TOP_NAV = '''
<!-- TopAppBar -->
<header class="bg-slate-50 dark:bg-slate-950 font-sans tracking-tight uppercase font-bold text-xs docked full-width top-0 border-b border-slate-300 dark:border-slate-800 flat no shadows flex justify-between items-center w-full px-10 h-16 fixed z-50 pl-64">
    <div class="flex items-center gap-6">
        <span class="text-xl font-black text-sky-900 dark:text-sky-100 uppercase tracking-widest">TechMaintenance Pro</span>
        <nav class="hidden md:flex items-center gap-6 ml-8">
            <a class="{journal_active} text-slate-500 dark:text-slate-400 hover:text-sky-800 dark:hover:text-sky-300 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors opacity-80 duration-75" href="journal.html">Journal</a>
            <a class="{cert_active} text-slate-500 dark:text-slate-400 hover:text-sky-800 dark:hover:text-sky-300 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors" href="index.html#certifications">Certifications</a>
            <a class="{cv_active} text-slate-500 dark:text-slate-400 hover:text-sky-800 dark:hover:text-sky-300 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors" href="contact.html">CV & Contact</a>
            <a class="{home_active} text-slate-500 dark:text-slate-400 hover:text-sky-800 dark:hover:text-sky-300 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors" href="index.html">Accueil</a>
        </nav>
    </div>
    <div class="flex items-center gap-4 text-sky-900 dark:text-sky-400">
        <button class="hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors p-2 rounded-DEFAULT"><span class="material-symbols-outlined">settings</span></button>
        <button class="hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors p-2 rounded-DEFAULT"><span class="material-symbols-outlined">account_circle</span></button>
    </div>
</header>
'''

SIDE_NAV = '''
<!-- SideNavBar -->
<aside class="bg-slate-100 dark:bg-slate-900 font-sans text-sm font-medium tracking-wide fixed left-0 top-0 h-screen border-r w-64 border-slate-300 dark:border-slate-800 flat no shadows flex flex-col h-full py-6 z-40 pt-20">
    <div class="px-6 pb-6 border-b border-slate-300 dark:border-slate-800 mb-4 flex flex-col gap-2">
        <span class="text-lg font-bold text-sky-900 dark:text-sky-100">{name}</span>
        <span class="text-xs text-slate-500">ID: {tech_id}</span>
        <div class="w-12 h-12 rounded-full border-2 border-sky-900 dark:border-sky-400 mt-2 bg-sky-100 flex items-center justify-center text-sky-900 font-bold text-lg">SB</div>
    </div>
    <nav class="flex flex-col flex-grow">
        <a class="{overview_active} px-4 py-3 hover:bg-slate-200 dark:hover:bg-slate-800 flex items-center gap-3" href="index.html"><span class="material-symbols-outlined">dashboard</span> Overview</a>
        <a class="{interventions_active} px-4 py-3 hover:bg-slate-200 dark:hover:bg-slate-800 flex items-center gap-3" href="journal.html"><span class="material-symbols-outlined">build</span> Interventions</a>
        <a class="px-4 py-3 hover:bg-slate-200 dark:hover:bg-slate-800 flex items-center gap-3 text-slate-600 dark:text-slate-400" href="#"><span class="material-symbols-outlined">architecture</span> Schematics</a>
        <a class="px-4 py-3 hover:bg-slate-200 dark:hover:bg-slate-800 flex items-center gap-3 text-slate-600 dark:text-slate-400" href="#"><span class="material-symbols-outlined">description</span> Documentation</a>
    </nav>
    <div class="px-4 py-4">
        <a href="contact.html" class="block w-full bg-slate-200 text-sky-900 py-2 text-xs font-bold uppercase tracking-wider hover:bg-slate-300 transition-colors border border-slate-300 text-center">Download CV</a>
    </div>
    <div class="border-t border-slate-300 dark:border-slate-800 mt-auto pt-4 flex flex-col">
        <a class="px-4 py-3 hover:bg-slate-200 dark:hover:bg-slate-800 flex items-center gap-3 text-slate-600 dark:text-slate-400" href="contact.html"><span class="material-symbols-outlined">settings_input_component</span> Contact</a>
        <span class="px-4 py-3 flex items-center gap-3 text-slate-400"><span class="material-symbols-outlined">logout</span> Logout</span>
    </div>
</aside>
'''

FOOTER = '''
<!-- Footer -->
<footer class="bg-slate-50 dark:bg-slate-950 font-sans text-[10px] uppercase tracking-tighter text-slate-500 w-full border-t border-slate-300 dark:border-slate-800 py-8 px-10 flex flex-col md:flex-row justify-between items-center gap-4 ml-64 mt-auto">
    <span>© 2024 {name} — Technicien Maintenance Industrielle | Portfolio Interactif</span>
    <div class="flex items-center gap-4">
        <a class="text-slate-500 hover:text-orange-600 dark:hover:text-orange-400 transition-colors" href="#">Safety Protocols</a>
        <a class="text-slate-500 hover:text-orange-600 dark:hover:text-orange-400 transition-colors" href="#">Technical Certifications</a>
        <a class="text-slate-500 hover:text-orange-600 dark:hover:text-orange-400 transition-colors" href="contact.html">Contact</a>
    </div>
</footer>
'''

# ============================================================
# PAGE 1: INDEX (Accueil)
# ============================================================
def build_index():
    nav = TOP_NAV.format(
        journal_active="", cert_active="", cv_active="", home_active="text-sky-900 dark:text-sky-400 border-b-2 border-sky-900 dark:border-sky-400 pb-1 hover:bg-slate-100 dark:hover:bg-slate-900"
    )
    side = SIDE_NAV.format(
        name=PROFILE["name"], tech_id=PROFILE["id"],
        overview_active="bg-sky-900 text-white dark:bg-sky-400 dark:text-slate-950 rounded-none border-l-4 border-orange-500 font-bold scale-95 duration-100",
        interventions_active="text-slate-600 dark:text-slate-400"
    )
    
    comp_cards = ""
    for c in COMPETENCES:
        tags_html = "\n".join([f'<span class="bg-surface-container text-primary border border-outline-variant font-label-caps text-label-caps px-2 py-1 rounded">{t}</span>' for t in c["tags"]])
        comp_cards += f'''
            <div class="bg-surface-container-lowest border border-outline-variant rounded p-stack-md flex flex-col gap-stack-md hover:bg-surface-container-low transition-colors">
                <div class="flex items-center gap-3 text-primary">
                    <span class="material-symbols-outlined text-[32px]">{c["icon"]}</span>
                    <h3 class="font-h3 text-h3 text-on-surface">{c["category"]}</h3>
                </div>
                <p class="font-body-md text-body-md text-on-surface-variant flex-grow">{c["description"]}</p>
                <div class="flex flex-wrap gap-2 mt-auto">{tags_html}</div>
            </div>
        '''
    
    cert_rows = ""
    for cert in CERTIFICATIONS:
        dot_color = "bg-primary" if cert["statusColor"] == "primary" else "bg-secondary-container"
        cert_rows += f'''
            <div class="grid grid-cols-12 font-data-mono text-data-mono p-3 border-b border-outline-variant bg-surface-container-lowest items-center">
                <div class="col-span-3 text-on-surface-variant">{cert["id"]}</div>
                <div class="col-span-6 text-on-surface">{cert["name"]}</div>
                <div class="col-span-3 text-right flex items-center justify-end gap-2">
                    <span class="w-2 h-2 {dot_color} inline-block"></span> {cert["status"]}
                </div>
            </div>
        '''
    
    body = f'''
<body class="bg-background text-on-background antialiased flex flex-col min-h-screen">
    {nav}
    {side}
    <main class="ml-64 mt-16 flex-grow bg-surface">
        <!-- Hero Section -->
        <section class="w-full bg-surface-container py-24 px-margin border-b border-outline-variant">
            <div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-12 gap-gutter items-center">
                <div class="col-span-1 md:col-span-6 flex flex-col gap-stack-lg">
                    <div class="flex flex-col gap-stack-sm">
                        <span class="font-label-caps text-label-caps text-secondary-container uppercase tracking-widest">Technicien Supérieur</span>
                        <h1 class="font-h1 text-h1 text-on-surface">Expertise en Maintenance Industrielle</h1>
                        <p class="font-body-lg text-body-lg text-on-surface-variant mt-4">{PROFILE["summary"]}</p>
                    </div>
                    <div class="flex flex-row gap-4">
                        <a href="journal.html" class="bg-primary text-on-primary font-label-caps text-label-caps px-8 py-4 rounded hover:bg-surface-tint transition-colors flex items-center gap-2 border border-primary">
                            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">assignment</span>
                            Journal des Pannes
                        </a>
                        <a href="contact.html" class="bg-surface text-primary border border-primary font-label-caps text-label-caps px-8 py-4 rounded hover:bg-surface-container-low transition-colors">
                            Voir le CV
                        </a>
                    </div>
                </div>
                <div class="col-span-1 md:col-span-6 bg-surface-container-high border border-outline-variant rounded p-8 flex flex-col items-center justify-center text-center gap-stack-md">
                    <div class="grid grid-cols-2 gap-gutter w-full">
                        <div class="bg-surface-container-lowest border border-outline-variant rounded p-stack-md text-center">
                            <div class="font-h3 text-h3 text-secondary-container">{PROFILE["years"]}</div>
                            <div class="font-label-caps text-label-caps text-on-surface-variant mt-1">ANNÉES</div>
                        </div>
                        <div class="bg-surface-container-lowest border border-outline-variant rounded p-stack-md text-center">
                            <div class="font-h3 text-h3 text-secondary-container">{PROFILE["companies"]}</div>
                            <div class="font-label-caps text-label-caps text-on-surface-variant mt-1">ENTREPRISES</div>
                        </div>
                        <div class="bg-surface-container-lowest border border-outline-variant rounded p-stack-md text-center">
                            <div class="font-h3 text-h3 text-secondary-container">{PROFILE["countries"]}</div>
                            <div class="font-label-caps text-label-caps text-on-surface-variant mt-1">PAYS</div>
                        </div>
                        <div class="bg-surface-container-lowest border border-outline-variant rounded p-stack-md text-center">
                            <div class="font-h3 text-h3 text-secondary-container">{PROFILE["fiches"]}</div>
                            <div class="font-label-caps text-label-caps text-on-surface-variant mt-1">FICHES</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Compétences Clés -->
        <section class="w-full py-24 px-margin bg-surface">
            <div class="max-w-container-max mx-auto flex flex-col gap-stack-lg">
                <div class="flex items-center gap-4 border-b border-outline-variant pb-stack-sm">
                    <span class="w-2 h-2 bg-secondary-container"></span>
                    <h2 class="font-h2 text-h2 text-on-surface">Compétences Clés</h2>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">{comp_cards}</div>
            </div>
        </section>
        <!-- Certifications & About -->
        <section id="certifications" class="w-full py-24 px-margin bg-surface-container border-t border-outline-variant">
            <div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-12 gap-gutter">
                <div class="col-span-1 md:col-span-7 flex flex-col gap-stack-lg">
                    <div class="flex items-center gap-4 border-b border-outline-variant pb-stack-sm">
                        <span class="w-2 h-2 bg-primary"></span>
                        <h2 class="font-h2 text-h2 text-on-surface">Certifications Techniques</h2>
                    </div>
                    <div class="border border-outline-variant rounded bg-surface-container-lowest overflow-hidden">
                        <div class="grid grid-cols-12 bg-primary text-on-primary font-label-caps text-label-caps p-3 border-b border-outline-variant">
                            <div class="col-span-3">ID</div>
                            <div class="col-span-6">Désignation</div>
                            <div class="col-span-3 text-right">Statut</div>
                        </div>
                        {cert_rows}
                    </div>
                </div>
                <div class="col-span-1 md:col-span-5 flex flex-col gap-stack-lg">
                    <div class="flex items-center gap-4 border-b border-outline-variant pb-stack-sm">
                        <span class="w-2 h-2 bg-outline"></span>
                        <h2 class="font-h2 text-h2 text-on-surface">À propos</h2>
                    </div>
                    <div class="bg-surface-container-lowest border border-outline-variant rounded p-stack-md h-full flex flex-col">
                        <p class="font-body-md text-body-md text-on-surface-variant mb-4">
                            Avec plus de 10 ans d'expérience sur le terrain dans l'industrie lourde et manufacturière, j'apporte une approche méthodique à la résolution de problèmes. Mon objectif est de minimiser les temps d'arrêt machine tout en appliquant les protocoles de sécurité les plus stricts.
                        </p>
                        <div class="mt-auto border-t border-outline-variant pt-4 flex justify-between items-center">
                            <span class="font-data-mono text-data-mono text-on-surface">ID: {PROFILE["id"]}</span>
                            <a href="contact.html" class="text-primary font-label-caps text-label-caps hover:text-secondary-container transition-colors uppercase flex items-center gap-1">
                                Profil Complet <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    {FOOTER.format(name=PROFILE["name"])}
</body>
'''
    return COMMON_HEAD.format(title="Portfolio Maintenance — Salah Eddine Barki") + body + "</html>"


# ============================================================
# PAGE 2: JOURNAL (Liste des interventions)
# ============================================================
def build_journal():
    nav = TOP_NAV.format(
        journal_active="text-sky-900 dark:text-sky-400 border-b-2 border-sky-900 dark:border-sky-400 pb-1 hover:bg-slate-100 dark:hover:bg-slate-900",
        cert_active="", cv_active="", home_active=""
    )
    side = SIDE_NAV.format(
        name=PROFILE["name"], tech_id=PROFILE["id"],
        overview_active="text-slate-600 dark:text-slate-400",
        interventions_active="bg-sky-900 text-white dark:bg-sky-400 dark:text-slate-950 rounded-none border-l-4 border-orange-500 font-bold scale-95 duration-100"
    )
    
    cards = ""
    for f in FICHES:
        top_color = "bg-secondary" if f["typeColor"] == "secondary" else "bg-primary"
        icon = "warning" if f["typeColor"] == "secondary" else "check_circle"
        filled = "" if f["typeColor"] == "secondary" else "filled"
        cards += f'''
            <article class="bg-surface-container-lowest border border-outline-variant rounded-DEFAULT relative overflow-hidden flex flex-col group hover:border-primary transition-colors duration-200">
                <div class="absolute top-0 left-0 w-full h-1 {top_color}"></div>
                <div class="p-6 flex flex-col flex-grow">
                    <header class="flex justify-between items-start mb-stack-sm">
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined {filled} text-{f["typeColor"]} text-[20px]">{icon}</span>
                            <span class="font-data-mono text-data-mono text-on-surface-variant">{f["date"]} // {f["duree"]}</span>
                        </div>
                        <div class="font-label-caps text-label-caps text-primary border border-outline-variant bg-surface-container-low px-2 py-1 uppercase">{f["type"]}</div>
                    </header>
                    <h2 class="font-h3 text-h3 text-primary mb-stack-sm group-hover:text-surface-tint transition-colors">{f["titre"]}</h2>
                    <p class="font-body-md text-body-md text-on-surface mb-stack-md flex-grow">{f["symptome"][:160]}...</p>
                    <div class="mt-auto border-t border-outline-variant pt-4 flex justify-between items-center">
                        <span class="font-data-mono text-data-mono text-on-surface-variant text-sm">{f["entreprise"]} — {f["lieu"]}</span>
                        <a href="intervention.html?id={f["num"]}" class="font-label-caps text-label-caps text-primary hover:text-secondary flex items-center gap-1 transition-colors">
                            View Full Log <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                        </a>
                    </div>
                </div>
            </article>
        '''
    
    body = f'''
<body class="bg-background text-on-background antialiased flex flex-col min-h-screen">
    {nav}
    {side}
    <main class="ml-64 mt-16 flex-grow p-margin bg-surface">
        <div class="mb-stack-lg border-b border-outline-variant pb-stack-md flex justify-between items-end">
            <div>
                <h1 class="font-h1 text-h1 text-primary tracking-tight">Journal of Interventions</h1>
                <p class="font-body-md text-body-md text-on-surface-variant mt-stack-sm max-w-2xl">Official log of technical maintenance procedures, repairs, and system calibrations across active industrial sectors.</p>
            </div>
            <span class="font-data-mono text-data-mono text-on-surface-variant">{len(FICHES)} ENTRIES</span>
        </div>
        <div class="grid grid-cols-12 gap-gutter">
            <!-- Sidebar Filters -->
            <aside class="col-span-12 md:col-span-3 lg:col-span-2 space-y-stack-md">
                <div class="bg-surface-container-low border border-outline-variant p-4 rounded-DEFAULT">
                    <h3 class="font-label-caps text-label-caps text-on-surface-variant mb-stack-md border-b border-outline-variant pb-2">SYSTEM CATEGORY</h3>
                    <div class="space-y-stack-sm">
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <div class="w-4 h-4 border border-outline bg-surface group-hover:border-primary flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-primary opacity-0 group-hover:opacity-100">check</span></div>
                            <span class="font-data-mono text-data-mono text-on-surface">Hydraulics</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <div class="w-4 h-4 border border-primary bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-on-primary">check</span></div>
                            <span class="font-data-mono text-data-mono text-primary font-bold">Electrical</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <div class="w-4 h-4 border border-outline bg-surface group-hover:border-primary flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-primary opacity-0 group-hover:opacity-100">check</span></div>
                            <span class="font-data-mono text-data-mono text-on-surface">Pneumatics</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <div class="w-4 h-4 border border-outline bg-surface group-hover:border-primary flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-primary opacity-0 group-hover:opacity-100">check</span></div>
                            <span class="font-data-mono text-data-mono text-on-surface">Automatisme</span>
                        </label>
                    </div>
                </div>
                <div class="bg-surface-container-low border border-outline-variant p-4 rounded-DEFAULT">
                    <h3 class="font-label-caps text-label-caps text-on-surface-variant mb-stack-md border-b border-outline-variant pb-2">STATUS</h3>
                    <div class="space-y-stack-sm">
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <div class="w-4 h-4 border border-outline bg-surface group-hover:border-primary flex items-center justify-center"></div>
                            <span class="font-data-mono text-data-mono text-on-surface flex items-center gap-2"><div class="w-2 h-2 bg-secondary"></div> Active</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <div class="w-4 h-4 border border-outline bg-surface group-hover:border-primary flex items-center justify-center"></div>
                            <span class="font-data-mono text-data-mono text-on-surface flex items-center gap-2"><div class="w-2 h-2 bg-primary"></div> Resolved</span>
                        </label>
                    </div>
                </div>
            </aside>
            <!-- Cards Grid -->
            <div class="col-span-12 md:col-span-9 lg:col-span-10 grid grid-cols-1 xl:grid-cols-2 gap-gutter">
                {cards}
            </div>
        </div>
    </main>
    {FOOTER.format(name=PROFILE["name"])}
</body>
'''
    return COMMON_HEAD.format(title="Journal — TechMaintenance Pro") + body + "</html>"


# ============================================================
# PAGE 3: INTERVENTION (Détail)
# ============================================================
def build_intervention():
    # Génère le squelette JS qui charge dynamiquement les données
    nav = TOP_NAV.format(
        journal_active="text-sky-900 dark:text-sky-400 border-b-2 border-sky-900 dark:border-sky-400 pb-1 hover:bg-slate-100 dark:hover:bg-slate-900",
        cert_active="", cv_active="", home_active=""
    )
    side = SIDE_NAV.format(
        name=PROFILE["name"], tech_id=PROFILE["id"],
        overview_active="text-slate-600 dark:text-slate-400",
        interventions_active="bg-sky-900 text-white dark:bg-sky-400 dark:text-slate-950 rounded-none border-l-4 border-orange-500 font-bold scale-95 duration-100"
    )
    
    body = f'''
<body class="bg-background text-on-background antialiased flex flex-col min-h-screen">
    {nav}
    {side}
    <main class="ml-64 mt-16 flex-grow p-margin bg-surface">
        <!-- Contextual Back Action -->
        <div class="mb-stack-lg">
            <a href="journal.html" class="inline-flex items-center gap-2 font-label-caps text-label-caps text-primary hover:text-secondary transition-colors border border-outline px-3 py-2 bg-surface-container-lowest">
                <span class="material-symbols-outlined text-[16px]">arrow_back</span>
                RETOUR AUX INTERVENTIONS
            </a>
        </div>
        <!-- Page Header -->
        <div class="border-b border-outline pb-stack-md mb-stack-lg flex flex-col md:flex-row md:justify-between md:items-end gap-stack-md" id="page-header">
            <div>
                <div class="font-label-caps text-label-caps text-secondary mb-stack-sm flex items-center gap-2">
                    <span class="w-2 h-2 bg-secondary block"></span> <span id="type-badge">...</span>
                </div>
                <h1 class="font-h1 text-h1 text-primary" id="int-title">...</h1>
                <p class="font-body-lg text-body-lg text-on-surface-variant mt-unit" id="int-id">...</p>
            </div>
            <div class="flex flex-col md:text-right gap-unit">
                <div class="font-data-mono text-data-mono text-on-surface-variant flex items-center md:justify-end gap-2">
                    <span class="material-symbols-outlined text-[16px]">calendar_today</span> <span id="int-date">...</span>
                </div>
                <div class="font-data-mono text-data-mono text-on-surface-variant flex items-center md:justify-end gap-2">
                    <span class="material-symbols-outlined text-[16px]">timer</span> Durée: <span id="int-duree">...</span>
                </div>
                <div class="font-data-mono text-data-mono text-on-surface-variant flex items-center md:justify-end gap-2">
                    <span class="material-symbols-outlined text-[16px]">engineering</span> Tech: <span id="int-tech">...</span>
                </div>
            </div>
        </div>
        <!-- 12-Col Grid Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
            <!-- Left Column (Narrative & Process) -->
            <div class="lg:col-span-8 space-y-gutter">
                <!-- Le Problème -->
                <section class="bg-surface-container-lowest border border-outline rounded relative overflow-hidden">
                    <div class="absolute top-0 left-0 w-full h-1 bg-error"></div>
                    <div class="p-gutter">
                        <h2 class="font-label-caps text-label-caps text-error border-b border-outline-variant pb-stack-sm mb-stack-md flex items-center gap-2 uppercase">
                            <span class="material-symbols-outlined text-[18px]">warning</span> Le Problème
                        </h2>
                        <p class="font-body-md text-body-md text-on-surface mb-stack-md" id="int-symptome">...</p>
                        <div class="bg-surface p-stack-md border border-outline flex gap-4 items-center">
                            <span class="material-symbols-outlined text-error text-[32px]">sensors</span>
                            <div class="flex-1">
                                <div class="font-label-caps text-label-caps text-on-surface-variant mb-unit">Contexte Opérationnel</div>
                                <div class="flex justify-between items-center border-b border-outline-variant pb-1">
                                    <span class="font-data-mono text-data-mono">Équipement</span>
                                    <span class="font-data-mono text-data-mono text-error font-bold" id="int-equip-short">...</span>
                                </div>
                                <div class="flex justify-between items-center pt-1">
                                    <span class="font-data-mono text-data-mono text-on-surface-variant text-sm">Site</span>
                                    <span class="font-data-mono text-data-mono text-on-surface-variant text-sm" id="int-lieu">...</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <!-- Diagnostic -->
                <section class="bg-surface-container-lowest border border-outline rounded">
                    <div class="p-gutter">
                        <h2 class="font-label-caps text-label-caps text-primary border-b border-outline-variant pb-stack-sm mb-stack-md flex items-center gap-2 uppercase">
                            <span class="material-symbols-outlined text-[18px]">troubleshoot</span> Diagnostic
                        </h2>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-stack-md mb-stack-md">
                            <div>
                                <p class="font-body-md text-body-md text-on-surface" id="int-diagnostic">...</p>
                            </div>
                            <div class="bg-surface-container-low border border-outline-variant p-stack-md flex flex-col items-center justify-center text-center">
                                <span class="material-symbols-outlined text-primary text-[48px] mb-2">psychology</span>
                                <div class="font-label-caps text-label-caps text-on-surface-variant">Méthode RCA</div>
                                <div class="font-data-mono text-data-mono text-primary mt-1">5 Pourquoi + Pareto + Ishikawa</div>
                            </div>
                        </div>
                    </div>
                </section>
                <!-- Solution Apportée -->
                <section class="bg-surface-container-lowest border border-outline rounded">
                    <div class="p-gutter">
                        <h2 class="font-label-caps text-label-caps text-primary border-b border-outline-variant pb-stack-sm mb-stack-md flex items-center gap-2 uppercase">
                            <span class="material-symbols-outlined text-[18px]">build</span> Solution Apportée
                        </h2>
                        <div class="space-y-stack-sm" id="int-actions">
                        </div>
                    </div>
                </section>
                <!-- Résultat -->
                <section class="bg-surface-container-lowest border border-outline rounded relative overflow-hidden">
                    <div class="absolute top-0 left-0 w-full h-1 bg-primary"></div>
                    <div class="p-gutter">
                        <h2 class="font-label-caps text-label-caps text-primary border-b border-outline-variant pb-stack-sm mb-stack-md flex items-center gap-2 uppercase">
                            <span class="material-symbols-outlined text-[18px]">verified</span> Résultat
                        </h2>
                        <p class="font-body-md text-body-md text-on-surface mb-stack-md" id="int-resultat">...</p>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-unit" id="int-metriques">
                        </div>
                    </div>
                </section>
            </div>
            <!-- Right Column (Technical Data Metadata) -->
            <aside class="lg:col-span-4 space-y-gutter">
                <!-- Équipement Info -->
                <div class="bg-surface-container border border-outline rounded p-gutter">
                    <h3 class="font-label-caps text-label-caps text-primary border-b border-outline-variant pb-stack-sm mb-stack-md uppercase">Spécifications Équipement</h3>
                    <ul class="space-y-stack-sm">
                        <li class="flex justify-between border-b border-outline-variant pb-unit">
                            <span class="font-body-md text-body-md text-on-surface-variant">Système</span>
                            <span class="font-data-mono text-data-mono text-on-surface" id="meta-equip">...</span>
                        </li>
                        <li class="flex justify-between border-b border-outline-variant pb-unit">
                            <span class="font-body-md text-body-md text-on-surface-variant">Localisation</span>
                            <span class="font-data-mono text-data-mono text-on-surface" id="meta-lieu">...</span>
                        </li>
                        <li class="flex justify-between border-b border-outline-variant pb-unit">
                            <span class="font-body-md text-body-md text-on-surface-variant">Entreprise</span>
                            <span class="font-data-mono text-data-mono text-on-surface" id="meta-entreprise">...</span>
                        </li>
                        <li class="flex justify-between pb-unit">
                            <span class="font-body-md text-body-md text-on-surface-variant">Indice Criticité</span>
                            <span class="font-data-mono text-data-mono text-error font-bold bg-error-container px-2 py-0.5 border border-error">Tier 1 - Vital</span>
                        </li>
                    </ul>
                </div>
                <!-- Pièces Remplacées -->
                <div class="bg-surface-container border border-outline rounded p-gutter">
                    <h3 class="font-label-caps text-label-caps text-primary border-b border-outline-variant pb-stack-sm mb-stack-md uppercase">Inventaire Pièces</h3>
                    <div class="space-y-unit" id="int-pieces">
                    </div>
                </div>
                <!-- Outillage -->
                <div class="bg-surface-container border border-outline rounded p-gutter">
                    <h3 class="font-label-caps text-label-caps text-primary border-b border-outline-variant pb-stack-sm mb-stack-md uppercase">Matériel Déployé</h3>
                    <div class="flex flex-wrap gap-2" id="int-outillage">
                    </div>
                </div>
            </aside>
        </div>
    </main>
    {FOOTER.format(name=PROFILE["name"])}
    <script src="data.js"></script>
    <script>
        const params = new URLSearchParams(window.location.search);
        const id = params.get('id');
        const fiche = FICHES.find(f => f.num === id) || FICHES[0];
        
        document.getElementById('type-badge').textContent = fiche.type;
        document.getElementById('int-title').textContent = fiche.titre;
        document.getElementById('int-id').textContent = 'Rapport d\'intervention technique #' + fiche.id;
        document.getElementById('int-date').textContent = fiche.date;
        document.getElementById('int-duree').textContent = fiche.duree;
        document.getElementById('int-tech').textContent = fiche.tech;
        document.getElementById('int-symptome').textContent = fiche.symptome;
        document.getElementById('int-equip-short').textContent = fiche.equip.substring(0, 40) + '...';
        document.getElementById('int-lieu').textContent = fiche.lieu;
        document.getElementById('int-diagnostic').innerHTML = fiche.diagnostic.replace(/\\n/g, '<br><br>');
        document.getElementById('int-resultat').textContent = fiche.resultat;
        document.getElementById('meta-equip').textContent = fiche.equip.substring(0, 50) + '...';
        document.getElementById('meta-lieu').textContent = fiche.lieu;
        document.getElementById('meta-entreprise').textContent = fiche.entreprise;
        
        // Actions
        const actionsDiv = document.getElementById('int-actions');
        fiche.actions.forEach((action, i) => {{
            const div = document.createElement('div');
            div.className = 'flex gap-3 border-b border-outline-variant pb-stack-sm';
            div.innerHTML = '<span class="font-data-mono text-data-mono text-secondary shrink-0">' + String(i+1).padStart(2, '0') + '.</span><p class="font-body-md text-body-md text-on-surface">' + action + '</p>';
            actionsDiv.appendChild(div);
        }});
        
        // Métriques
        const metriquesDiv = document.getElementById('int-metriques');
        fiche.metriques.forEach(m => {{
            const div = document.createElement('div');
            div.className = 'bg-surface p-stack-sm border border-outline flex flex-col justify-center items-center text-center';
            div.innerHTML = '<span class="material-symbols-outlined text-primary mb-1">' + m.icon + '</span><div class="font-label-caps text-label-caps text-on-surface-variant mb-unit">' + m.label + '</div><div class="font-h3 text-h3 text-primary">' + m.value + '</div>';
            metriquesDiv.appendChild(div);
        }});
        
        // Pièces
        const piecesDiv = document.getElementById('int-pieces');
        fiche.pieces.forEach(p => {{
            const div = document.createElement('div');
            div.className = 'bg-surface-container-lowest border border-outline p-stack-sm flex items-start gap-3';
            div.innerHTML = '<div class="bg-surface p-1.5 border border-outline-variant mt-0.5"><span class="material-symbols-outlined text-on-surface-variant text-[18px]">settings</span></div><div><div class="font-body-md text-body-md font-bold text-on-surface leading-tight mb-1">' + p.name + '</div><div class="flex justify-between items-center w-full gap-4"><span class="font-data-mono text-data-mono text-on-surface-variant text-sm">Réf: ' + p.ref + '</span><span class="font-data-mono text-data-mono text-on-surface text-sm">Qté: ' + p.qty + '</span></div></div>';
            piecesDiv.appendChild(div);
        }});
        
        // Outillage
        const outillageDiv = document.getElementById('int-outillage');
        fiche.outillage.forEach(o => {{
            const div = document.createElement('div');
            div.className = 'border border-outline bg-surface px-2 py-1 flex items-center gap-1';
            div.innerHTML = '<span class="material-symbols-outlined text-[14px] text-primary">build</span><span class="font-label-caps text-label-caps text-primary">' + o + '</span>';
            outillageDiv.appendChild(div);
        }});
    </script>
</body>
'''
    return COMMON_HEAD.format(title="Intervention Detail — TechMaintenance Pro") + body + "</html>"


# ============================================================
# PAGE 4: CONTACT
# ============================================================
def build_contact():
    nav = TOP_NAV.format(
        journal_active="", cert_active="", cv_active="text-sky-900 dark:text-sky-400 border-b-2 border-sky-900 dark:border-sky-400 pb-1 hover:bg-slate-100 dark:hover:bg-slate-900", home_active=""
    )
    side = SIDE_NAV.format(
        name=PROFILE["name"], tech_id=PROFILE["id"],
        overview_active="text-slate-600 dark:text-slate-400",
        interventions_active="text-slate-600 dark:text-slate-400"
    )
    
    body = f'''
<body class="bg-background text-on-background min-h-screen flex flex-col font-body-md">
    {nav}
    {side}
    <main class="flex-grow w-full max-w-container-max mx-auto px-margin py-stack-lg flex flex-col md:flex-row gap-gutter ml-64 mt-16">
        <!-- Left Column: Context & CV -->
        <div class="w-full md:w-1/3 flex flex-col gap-stack-lg">
            <div>
                <h1 class="font-h1 text-h1 text-primary mb-stack-sm">Connect</h1>
                <p class="font-body-lg text-body-lg text-on-surface-variant">Ready to discuss structural integrity and precision maintenance.</p>
            </div>
            <!-- CV Download Card -->
            <div class="bg-surface-container-low border border-outline-variant p-stack-md rounded-DEFAULT flex flex-col items-center justify-center text-center gap-stack-sm relative overflow-hidden group">
                <div class="absolute top-0 left-0 w-full h-unit bg-secondary-container"></div>
                <span class="material-symbols-outlined text-4xl text-primary mb-2">description</span>
                <h3 class="font-h3 text-h3 text-primary">Technical Blueprint</h3>
                <p class="font-body-md text-body-md text-on-surface-variant mb-stack-md">Comprehensive overview of methodologies, certifications, and operational history.</p>
                <a href="../Portfolio_Salah_Barki_v4.pdf" download class="bg-primary text-on-primary font-label-caps text-label-caps uppercase px-6 py-3 rounded-DEFAULT hover:bg-surface-tint transition-colors w-full flex items-center justify-center gap-2">
                    <span class="material-symbols-outlined text-sm">download</span>
                    Télécharger mon CV
                </a>
            </div>
            <!-- Contact Info -->
            <div class="flex flex-col gap-unit">
                <div class="flex items-center gap-3 p-3 border border-outline-variant rounded-DEFAULT bg-surface-container-lowest">
                    <span class="material-symbols-outlined text-primary">phone</span>
                    <span class="font-data-mono text-data-mono text-on-surface">{PROFILE["contact"]["phone"]}</span>
                </div>
                <div class="flex items-center gap-3 p-3 border border-outline-variant rounded-DEFAULT bg-surface-container-lowest">
                    <span class="material-symbols-outlined text-primary">mail</span>
                    <span class="font-data-mono text-data-mono text-on-surface">{PROFILE["contact"]["email"]}</span>
                </div>
                <div class="flex items-center gap-3 p-3 border border-outline-variant rounded-DEFAULT bg-surface-container-lowest">
                    <span class="material-symbols-outlined text-primary">location_on</span>
                    <span class="font-data-mono text-data-mono text-on-surface">{PROFILE["contact"]["location"]}</span>
                </div>
            </div>
            <!-- Certifications Reinforcement -->
            <div class="mt-auto pt-stack-md">
                <h4 class="font-label-caps text-label-caps text-outline uppercase mb-stack-sm">Verified Credentials</h4>
                <div class="flex flex-wrap gap-unit">
                    <span class="bg-surface border border-outline-variant px-2 py-1 font-label-caps text-label-caps text-primary uppercase">ISO 9001</span>
                    <span class="bg-surface border border-outline-variant px-2 py-1 font-label-caps text-label-caps text-primary uppercase">PLC Adv.</span>
                    <span class="bg-surface border border-outline-variant px-2 py-1 font-label-caps text-label-caps text-primary uppercase">Hydraulics II</span>
                    <span class="bg-surface border border-outline-variant px-2 py-1 font-label-caps text-label-caps text-primary uppercase">LOTO</span>
                </div>
            </div>
        </div>
        <!-- Right Column: Contact Form -->
        <div class="w-full md:w-2/3">
            <div class="bg-surface border border-outline-variant rounded-DEFAULT p-stack-lg h-full">
                <div class="flex items-center gap-2 mb-stack-md border-b border-outline-variant pb-stack-sm">
                    <span class="w-3 h-3 bg-secondary-container"></span>
                    <h2 class="font-h2 text-h2 text-primary">Initiate Contact</h2>
                </div>
                <form class="flex flex-col gap-stack-md" onsubmit="event.preventDefault(); alert('Message envoyé ! Je vous recontacte rapidement.');">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-stack-md">
                        <div class="flex flex-col gap-1">
                            <label class="font-label-caps text-label-caps text-on-surface-variant uppercase" for="id_name">Nom / Société</label>
                            <input class="border border-outline-variant bg-surface-container-lowest p-3 rounded-DEFAULT focus:outline-none focus:border-2 focus:border-primary font-data-mono text-data-mono text-on-surface transition-all" id="id_name" placeholder="Votre nom..." type="text"/>
                        </div>
                        <div class="flex flex-col gap-1">
                            <label class="font-label-caps text-label-caps text-on-surface-variant uppercase" for="id_email">Email</label>
                            <input class="border border-outline-variant bg-surface-container-lowest p-3 rounded-DEFAULT focus:outline-none focus:border-2 focus:border-primary font-data-mono text-data-mono text-on-surface transition-all" id="id_email" placeholder="votre@email.com" type="email"/>
                        </div>
                    </div>
                    <div class="flex flex-col gap-1">
                        <label class="font-label-caps text-label-caps text-on-surface-variant uppercase" for="id_subject">Sujet</label>
                        <select class="border border-outline-variant bg-surface-container-lowest p-3 rounded-DEFAULT focus:outline-none focus:border-2 focus:border-primary font-data-mono text-data-mono text-on-surface transition-all appearance-none cursor-pointer" id="id_subject">
                            <option>Proposition d'emploi</option>
                            <option>Consultation technique</option>
                            <option>Collaboration</option>
                            <option>Autre</option>
                        </select>
                    </div>
                    <div class="flex flex-col gap-1">
                        <label class="font-label-caps text-label-caps text-on-surface-variant uppercase" for="id_message">Message</label>
                        <textarea class="border border-outline-variant bg-surface-container-lowest p-3 rounded-DEFAULT focus:outline-none focus:border-2 focus:border-primary font-data-mono text-data-mono text-on-surface transition-all resize-y" id="id_message" placeholder="Votre message..." rows="6"></textarea>
                    </div>
                    <div class="flex justify-end mt-stack-sm">
                        <button class="bg-primary text-on-primary font-label-caps text-label-caps uppercase px-8 py-3 rounded-DEFAULT hover:bg-surface-tint transition-colors border border-transparent flex items-center gap-2" type="submit">
                            Transmit Data
                            <span class="material-symbols-outlined text-sm">send</span>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </main>
    {FOOTER.format(name=PROFILE["name"])}
</body>
'''
    return COMMON_HEAD.format(title="Contact & CV — TechMaintenance Pro") + body + "</html>"


# ============================================================
# GÉNÉRATION
# ============================================================
if __name__ == "__main__":
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index())
    print(f"[OK] index.html")
    
    with open(os.path.join(OUTPUT_DIR, "journal.html"), "w", encoding="utf-8") as f:
        f.write(build_journal())
    print(f"[OK] journal.html")
    
    with open(os.path.join(OUTPUT_DIR, "intervention.html"), "w", encoding="utf-8") as f:
        f.write(build_intervention())
    print(f"[OK] intervention.html")
    
    with open(os.path.join(OUTPUT_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(build_contact())
    print(f"[OK] contact.html")
    
    # Copier data.js dans le dossier site
    import shutil
    shutil.copy(r"C:\Users\ba2rb\Downloads\salpre\data.js", os.path.join(OUTPUT_DIR, "data.js"))
    print(f"[OK] data.js copié")
    
    print("\n=== SITE INTERACTIF COMPLET GÉNÉRÉ ===")
    print(f"Dossier: {OUTPUT_DIR}")
    print("Ouvrez index.html dans votre navigateur pour tester.")
