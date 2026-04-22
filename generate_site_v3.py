# generate_site_v3.py - Couleurs exactes image.png + font clean
import os

OUTPUT_DIR = r"C:\Users\ba2rb\Downloads\salpre\site_v3"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PROFILE = {
    "name": "Salah Eddine Barki",
    "title": "Technicien de Maintenance Industrielle",
    "id": "4882-MT",
    "contact": {
        "location": "Amiens, France",
        "phone": "+33 6 88 69 07 04",
        "email": "salahbarki.seb@gmail.com"
    },
    "summary": "Technicien de maintenance industrielle senior avec plus de 10 ans d'expérience sur des équipements automatisés et mécaniques complexes : presses injection, lignes de production agroalimentaire (PET/canettes), bancs de test automobile et utilités industrielles. Compétences transverses : électrotechnique, automatisme (Siemens S7, TIA Portal), mécanique, hydraulique et pneumatique. Forte appétence pour le diagnostic structuré, l'analyse de pannes récurrentes et l'amélioration continue.",
    "years": "10+",
    "companies": 7,
    "countries": 4,
    "fiches": 6
}

COMPETENCES = [
    {"category": "Mécanique", "icon": "settings_applications", "description": "Diagnostic et réparation de systèmes de transmission, hydrauliques et pneumatiques complexes.", "tags": ["Hydraulique", "Pneumatique", "Transmission", "Guidages", "Roulements"]},
    {"category": "Électrique", "icon": "electrical_services", "description": "Habilitation basse tension, câblage industriel, et dépannage de variateurs de fréquence.", "tags": ["BT/HT", "Schémas", "Variateurs", "Moteurs"]},
    {"category": "Automatisme (PLC)", "icon": "memory", "description": "Programmation et diagnostic sur automates Siemens S7 et supervision de process.", "tags": ["Siemens TIA", "Step 7", "Ladder", "PROFINET"]}
]

CERTIFICATIONS = [
    {"id": "CERT-H2023", "name": "Habilitation Électrique BR/BC", "status": "Validé"},
    {"id": "CACES-R489", "name": "Chariots de manutention", "status": "Validé"},
    {"id": "SST-2024", "name": "Sauveteur Secouriste du Travail", "status": "Recyclage en cours"}
]

FICHES = [
    {"num": "01", "id": "INT-2024-001", "titre": "Panne récurrente encartonneuse — Ligne PET", "entreprise": "Coca-Cola Europacific Partners", "lieu": "Grigny (91)", "type": "CURATIF URGENT", "typeColor": "urgent", "date": "15 Juil 2024", "duree": "00h 45m", "tech": "4882-MT", "equip": "Encartonneuse / casseuse de colis — Ligne remplissage bouteilles PET 2L — Cadence 60 000 b/h", "contexte": "Ligne critique approvisionnant la grande distribution. Production 22h/jour. Tout arrêt >20 min = risque rupture de stock client.", "symptome": "Défaut HMI n°402 'PRODUIT_COINCÉ_ENTRÉE' toutes les 8–12 min. Accumulation de 15–18 colis rejetés/heure en sortie fardeleuse. Opérateurs forcés de redémarrer manuellement à chaque arrêt.", "diagnostic": "Vérification électrique : alimentation capteur photoélectrique d'entrée produit = 24 V stable. Signal logique oscillant anormalement : la diode de l'automate clignote au lieu de rester allumée fixe.<br><br>Analyse sur TIA Portal (programme automate Siemens) : dans le bloc de gestion encartonneuse, le bit de validation produit est conditionné directement par le signal capteur sans temporisation d'antirebond. L'oscillation du faisceau (probablement due à la condensation/buée ambiante près de la ligne froide) crée des fronts parasites interprétés comme des produits valides.<br><br>Vérification mécanique : jeu butée d'entrée produit anormalement large (environ 3 mm au lieu du réglage usuel ~0,5 mm). Amortisseur usé qui ne freine plus correctement le produit.", "actions": ["CONSIGNATION : Arrêt électrique + pneumatique de la zone. Condamnateur cadenas apposé. Signalisation verticale de zone de maintenance.", "ÉLECTRIQUE : Remplacement du capteur photoélectrique par un modèle plus robuste avec purge d'air intégrée (anti-buée), adapté à l'environnement humide proche de la ligne froide. Remplacement du câble d'alimentation par un câble blindé pour éviter les perturbations électromagnétiques des variateurs voisins.", "MÉCANIQUE : Dépose de la butée d'entrée. Remplacement de l'amortisseur hydraulique usé par un neuf. Recalage de la butée au jeu de 0,5 mm. Serrage de la boulonnerie au couple avec clé dynamométrique.", "AUTOMATISME (TIA Portal) : Ajout d'une temporisation de 50 ms dans le programme automate sur le signal du capteur avant validation du bit 'produit présent'. Recalage du décalage servo-pousseur.", "ESSAIS : Démarrage de la ligne. Run de 45 min à cadence nominale. Comptage des rejets : 2 colis rejetés sur 45 min (contre 12–15 avant).", "GMAO : Création d'un ordre de travail récurrent 'Contrôle capteur + butée encartonneuse' tous les 3 mois."], "resultat": "Temps d'arrêt moyen réduit de ~40 min à 8 min (–80%). Taux de rejets divisé par 5 (17/h → 3/h). Zero arrêt forcé opérateur pendant les 3 semaines suivantes.", "metriques": [{"label": "MTTR Avant", "value": "40 min"}, {"label": "MTTR Après", "value": "8 min"}, {"label": "Rejets", "value": "–80%"}, {"label": "Dispo.", "value": "+12%"}], "pieces": [{"name": "Capteur photoélectrique anti-buée", "ref": "Modèle avec purge", "qty": 1}, {"name": "Amortisseur hydraulique", "ref": "Standard industriel", "qty": 1}, {"name": "Câble blindé 5 conducteurs", "ref": "Standard", "qty": 1}], "outillage": ["Clé dynamométrique", "Multimètre", "TIA Portal", "Cales de réglage"]},
    {"num": "02", "id": "INT-2023-042", "titre": "Mise en service presse injection + auxiliaires", "entreprise": "TE Connectivity", "lieu": "Tanger (Maroc)", "type": "INSTALLATION", "typeColor": "normal", "date": "Juin 2023", "duree": "02j 00h", "tech": "4882-MT", "equip": "Presse injection 120 tonnes + sécheur de granulés + trémie + détecteur de métal", "contexte": "Relocalisation complète d'une cellule d'injection dans un nouveau hall de production. Objectif : production client automobile en J+2.", "symptome": "Aucun — Nouvelle installation. Objectif : démarrage qualité premier jet, cycle stable <20 secondes.", "diagnostic": "Analyse pré-installation : vérification de la compatibilité des arrivées électriques (400V triphasé + neutre + terre), hydrauliques (120 bar) et eau de refroidissement (20 °C).", "actions": ["TRANSPORT & POSE : Dépose de l'outillage. Transport chariot élévateur. Pose sur 4 plots anti-vibratoires. Nivellement au niveau à bulle puis affinage au laser.", "RACCORDEMENTS ÉLECTRIQUE : branchement 400V tri + N + T. Vérification terre au multimètre : résistance <1 Ω.", "RACCORDEMENTS HYDRAULIQUE : raccordement flexibles. Essai pression statique 10% au-dessus nominale pendant 10 min : aucune fuite.", "SÉCHEUR : Mise en service. Objectif point de rosée ≤ –40 °C. Lecture après 45 min : –42 °C.", "DÉTECTEUR MÉTAL : Installation en amont de la trémie. Validation détection 10/10, aucun faux positif.", "PARAMÉTRAGE CYCLE : Réglage vitesse injection, pression maintien, temps refroidissement. Batch test 500 pièces.", "CONTRÔLE QUALITÉ : 0 pièce hors tolérance sur les 500.", "DOCUMENTATION & FORMATION : PV de recette signé. Formation 3 opérateurs."], "resultat": "Mise en production J+2. Cycle 18,5 s moyenne. 0 défaut qualité. Checklist 42 points créée et réutilisée.", "metriques": [{"label": "Délai", "value": "J+2"}, {"label": "Cycle", "value": "18.5 s"}, {"label": "Qualité", "value": "100%"}, {"label": "Checklist", "value": "42 pts"}], "pieces": [{"name": "Plots anti-vibratoires", "ref": "Standard", "qty": 4}, {"name": "Huile hydraulique ISO VG 46", "ref": "Shell Tellus S2 MX", "qty": 120}], "outillage": ["Niveau laser", "Multimètre", "Débitmètre", "Pied à coulisse digital"]},
    {"num": "03", "id": "INT-2023-038", "titre": "Débogage & optimisation programme automate", "entreprise": "TE Connectivity", "lieu": "Tanger (Maroc)", "type": "AUTOMATISME", "typeColor": "normal", "date": "Mars 2023", "duree": "04h 30m", "tech": "4882-MT", "equip": "Cellule assemblage connectique — Automate Siemens S7-1200 + HMI + servo", "contexte": "Cellule critique assemblage connecteurs automobile. Cadence nominale 220 pièces/heure. OEE mensuel affiché en baisse (72% vs objectif 85%).", "symptome": "Temps de cycle mesuré au chronomètre : 28–30 s au lieu des 16–17 s nominaux. Alarme HMI fréquente 'Timeout bras robot zone pick'. Arrêts 3–4 fois par heure.", "diagnostic": "Connexion sur TIA Portal en ligne avec l'automate. Le temps d'exécution du bloc de gestion robot est anormalement long (8 s mesurés, contre 3–4 s attendu).<br><br>Analyse pas à pas : temporisation de sécurité réglée à 8 s alors que mouvement réel du bras dure 5,5 s. Temporisation trop conservative bloque la suite du cycle.<br><br>Capteur proximité 'pince OK' clignote légèrement. Support desserré (jeu 2 mm). Code séquentiel bloquant.", "actions": ["MÉCANIQUE : Réglage support capteur. Serrage écrou + contre-écrou nylstop. Signal désormais stable.", "PROGRAMMATION TIA PORTAL : Réduction tempo sécurité 8 s → 6,5 s. Ajout antirebond 35 ms.", "OPTIMISATION CODE : Parallélisation phases compatibles (descente+fermeture pince ; montée+translation). Suppression temporisations redondantes.", "SURVEILLANCE : Ajout compteur cycles + alarme auto si dérive >10%.", "HMI : Écran diagnostic 'Temps de cycle' temps réel.", "SÉCURITÉ & DOC : Sauvegarde programme sur serveur avec commentaires.", "VALIDATION : Run 4 h. Résultats : 16,2–17,1 s. Aucune alarme Timeout."], "resultat": "Cycle 28,5→16,8 s (–41%). OEE 72%→84% (+12 pts). Alarmes 3,4/h→<1/h.", "metriques": [{"label": "Cycle Avant", "value": "28.5 s"}, {"label": "Cycle Après", "value": "16.8 s"}, {"label": "OEE", "value": "+12 pts"}, {"label": "Capacité", "value": "+70%"}], "pieces": [{"name": "Écrou nylstop M8", "ref": "Standard", "qty": 2}], "outillage": ["TIA Portal V16", "Chronomètre", "Clé dynamométrique micro", "Multimètre"]},
    {"num": "04", "id": "INT-2022-017", "titre": "Analyse cause racine — Banc de test électrique", "entreprise": "Kromberg & Schubert", "lieu": "Kénitra (Maroc)", "type": "RCA & QUALITÉ", "typeColor": "urgent", "date": "Nov 2022", "duree": "01j 00h", "tech": "4882-MT", "equip": "Banc de test électrique (continuité, isolation, résistance) — Ligne faisceaux 32 voies", "contexte": "Ligne faisceaux moteur pour client automobile. Production 2 000 pièces/jour. Just-in-time : aucun stock tampon autorisé.", "symptome": "Taux de rejet test continuité anormal : 12% sur une même référence. Normalement stable autour de 1–2%. Conséquence : 240+ pièces rebutées/jour.", "diagnostic": "Analyse données 15 jours : dérive lente résistance mesurée. Tolérance <10 mΩ. Valeurs départ 3–5 mΩ → dérive 8–12 mΩ.<br><br>Pareto sur 342 pièces rebutées : ~2/3 pins oxydés (14/32), 1/4 câbles piquage usés.<br><br>Inspection : dernier nettoyage pins non documenté (>6 mois). Hotte filtre saturé : 80 vs 120 m³/h requis. Fumées soudure contaminent contacts.", "actions": ["ARRÊT & TRI : Retri batch complet. 94% bonnes / 6% rebut confirmé.", "REMPLACEMENT CONNECTEUR : Dépose pins oxydés. Pose connecteur neuf.", "RÉGLAGE MÉCANIQUE : Pression air 3,2→4,0 bar. Test 50 insertions : aucune marque.", "MAINTENANCE EXTRACTION : Remplacement filtre charbon. Débit remonté à 130 m³/h.", "MODIFICATION PROCÉDURE : Nettoyage pins 2 semaines + QC mensuel micro-ohmètre.", "FORMATION : 2 opérateurs + 1 technicien.", "CONTRÔLE RÉGULIER : Test gabarit 32/32 pins tous les matins."], "resultat": "Rejet 12,3%→1,1% moyenne 30 jours. Économie ~220 pièces/jour. QC temps –60%.", "metriques": [{"label": "Rejet Avant", "value": "12.3%"}, {"label": "Rejet Après", "value": "1.1%"}, {"label": "Pièces/jour", "value": "+220"}, {"label": "Temps QC", "value": "-60%"}], "pieces": [{"name": "Connecteur adaptateur 32 voies", "ref": "Constructeur banc", "qty": 1}, {"name": "Filtre charbon hotte", "ref": "500×300×50 mm F7", "qty": 1}], "outillage": ["Micro-ohmètre", "Débitmètre", "Brosse fibre de verre", "Manomètre"]},
    {"num": "05", "id": "INT-2024-089", "titre": "Dépannage hydraulique presse découpe / pliage", "entreprise": "Sovireso", "lieu": "Saint-Laurent-sur-Sèvre (85)", "type": "CURATIF MÉCANIQUE", "typeColor": "urgent", "date": "Avr 2024", "duree": "03h 20m", "tech": "4882-MT", "equip": "Presse hydraulique découpe/pliage — Vérin double effet Ø100/70 mm — Centrale 80 bar", "contexte": "Machine unique sur site pour découpe tôlerie fine. Pas de machine de remplacement. Programme client : 480 pièces/jour.", "symptome": "Perte brutale de pression descente rapide. Manomètre : 80→30 bar. Bruit violent 'coup de bélier'. Arrêt depuis 2 h.", "diagnostic": "Mesures manomètres : pompe 80 bar stable, descente 32 bar (anormal, devrait ~78–80), montée 78 bar (normal). Panne circuit descente.<br><br>Auscultation : coup de bélier accumulateur côté montée.<br><br>Clapet anti-retour : morceau joint écrasé coincé dans siège. Huile 68°C vs 55°C normale. Filtre retour encrassé. Accumulateur précharge azote 12 vs 65 bar, membrane fissurée.", "actions": ["CONSIGNATION & VIDANGE : Arrêt moteur pompe. Vidange 120 L huile.", "CLAPET ANTI-RETOUR : Dépose. Nettoyage siège pâte à roder. Remplacement joint torique. Serrage croisé vis au couple.", "ACCUMULATEUR : Remplacement complet. Précharge vérifiée 65 bar. Contrôle 24 h : 0 perte.", "FILTRATION : Remplacement filtre retour + aspiration. Huile neuve ISO VG 46. Purge 10 cycles lents.", "POMPE : Inspection palettes. Jeu 0,12 mm (max 0,15). Révision programmée 6 mois.", "MISE EN PRESSION : Paliers 20→40→80 bar, 5 min chacun. 0 fuite. Température 48°C OK.", "ESSAIS SOUS CHARGE : Découpe acier 2 mm, 50 cycles. 80 bar stable ±2. Disparition coups de bélier."], "resultat": "3h20 vs prévision 7h. Production relancée jour même. Pression stable 80 bar. À-coups supprimés.", "metriques": [{"label": "Durée", "value": "3h20"}, {"label": "Prévision", "value": "7h00"}, {"label": "Pression", "value": "80 bar"}, {"label": "Temp.", "value": "48 °C"}], "pieces": [{"name": "Joint torique clapet", "ref": "NBR 90SH Ø12×2", "qty": 1}, {"name": "Accumulateur hydropneumatique", "ref": "HAB 1-330", "qty": 1}, {"name": "Filtre retour 25 µm", "ref": "MP Filtri", "qty": 1}, {"name": "Huile hydraulique ISO VG 46", "ref": "Shell Tellus S2 MX", "qty": 120}], "outillage": ["Clé dynamométrique", "Stéthoscope mécanique", "Comparateur", "Manomètre de contrôle"]},
    {"num": "06", "id": "INT-2023-015", "titre": "Planification maintenance annuelle & pilotage GMAO", "entreprise": "TE Connectivity", "lieu": "Tanger (Maroc)", "type": "PLANIFICATION", "typeColor": "normal", "date": "Jan–Déc 2023", "duree": "12 mois", "tech": "4882-MT", "equip": "Site industriel complet : 142 équipements (injection, assemblage, test, utilités, bâtiment)", "contexte": "Site de 450 personnes, production 24h/5j. Objectif groupe : taux réalisation maintenance préventive >90% et réduction arrêts imprévus de 25%.", "symptome": "Préventif année N : 68% (233/342 OT). Arrêts imprévus 23% temps production. Coûts +12%. MTBF 420 h.", "diagnostic": "Pareto causes report : 45% conflit production, 30% pièces indisponibles, 15% sous-traitant indisponible.<br><br>Absence classification ABC : compresseur air 8 bar (critique) et éclairage bureau même fréquence préventif.<br><br>MTBF par famille : presses injection 380 h (faible), bancs test 620 h (moyen), utilités 850 h (bon).", "actions": ["COLLECTE & ANALYSE : Export GMAO + supervision. Croisement Excel + dashboard.", "CLASSIFICATION ABC : Classe A (14%, ~20 machines) = critique → mensuel/bimestriel. Classe B (32%, ~45) → trimestriel. Classe C (54%, ~77) → semestriel/annuel.", "PLANNING INTÉGRÉ : 12 mois GMAO, fenêtres négociées production. Conflits 45%→8%.", "APPROVISIONNEMENT : Stock sécurité A. Délai pièces critiques 5j→2j.", "SOUS-TRAITANCE : Achats groupés. Appel d'offres 3 fournisseurs. Coûts –18%.", "KPI MENSUEL : Taux préventif, MTBF, MTTR, coût/tonne, top 3 pannes.", "PROJETS : 5 projets soumis, 3 validés (variateurs obsolètes, suivi vibration, formation automatisme)."], "resultat": "Préventif 68%→94%. Arrêts –28%. MTBF 420→610 h (+45%). Coûts –15% sous-traitance, –8% pièces.", "metriques": [{"label": "Préventif", "value": "68→94%"}, {"label": "Arrêts", "value": "-28%"}, {"label": "MTBF", "value": "+45%"}, {"label": "Coûts", "value": "-15%"}], "pieces": [], "outillage": ["Excel", "GMAO SAP PM", "Power BI", "Tableau de bord KPI"]}
]


# ============================================================
# COLORS based on image.png analysis:
# Header navy: #3e496e, Text: #1c1c1c, BG: #fbfbfb, Accent: #ecedf1, #b9bdca
# ============================================================
HEADER = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
<style>
:root {{
  --bg: #fbfbfb;
  --surface: #f5f6f8;
  --surface-2: #ecedf1;
  --surface-3: #e2e4e9;
  --text: #1c1c1c;
  --text-secondary: #5a5d66;
  --text-muted: #8e9199;
  --header-bg: #3e496e;
  --header-text: #ffffff;
  --accent: #b9bdca;
  --accent-2: #ecedf1;
  --urgent: #c45c3e;
  --urgent-bg: #fdf2ef;
  --normal: #3e496e;
  --normal-bg: #f0f1f5;
  --border: #e2e4e9;
  --radius: 6px;
  --shadow: 0 1px 3px rgba(0,0,0,0.04);
  --shadow-card: 0 2px 8px rgba(0,0,0,0.06);
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.55;
  font-size: 14px;
  -webkit-font-smoothing: antialiased;
}}
a {{ text-decoration: none; color: inherit; }}
.container {{ max-width: 1200px; margin: 0 auto; padding: 0 32px; }}

/* TOP BAR */
.topbar {{
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 56px;
  background: var(--header-bg);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  z-index: 100;
}}
.topbar-brand {{
  font-size: 15px;
  font-weight: 700;
  color: var(--header-text);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}}
.topbar-nav {{
  display: flex;
  gap: 28px;
}}
.topbar-nav a {{
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.65);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 4px 0;
  border-bottom: 2px solid transparent;
  transition: all 0.15s;
}}
.topbar-nav a:hover, .topbar-nav a.active {{
  color: #fff;
  border-bottom-color: #fff;
}}

/* SIDEBAR */
.sidebar {{
  position: fixed;
  top: 56px; left: 0; bottom: 0;
  width: 240px;
  background: #fff;
  border-right: 1px solid var(--border);
  padding: 24px 0;
  z-index: 90;
}}
.sidebar-profile {{
  padding: 0 24px 20px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
}}
.sidebar-name {{
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
}}
.sidebar-title {{
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 2px;
  font-weight: 500;
}}
.sidebar-nav {{
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 0 12px;
}}
.sidebar-nav a {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: var(--radius);
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
  transition: all 0.12s;
}}
.sidebar-nav a:hover {{
  background: var(--surface-2);
  color: var(--text);
}}
.sidebar-nav a.active {{
  background: var(--header-bg);
  color: #fff;
  font-weight: 600;
}}
.sidebar-nav a svg {{
  width: 18px; height: 18px;
  opacity: 0.7;
}}
.sidebar-footer {{
  padding: 16px 24px 0;
  border-top: 1px solid var(--border);
  margin-top: auto;
}}
.sidebar-footer a {{
  display: block;
  text-align: center;
  padding: 10px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  font-size: 12px;
  font-weight: 600;
  color: var(--header-bg);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}}
.sidebar-footer a:hover {{
  background: var(--surface-3);
}}

/* MAIN */
.main {{
  margin-left: 240px;
  margin-top: 56px;
  min-height: calc(100vh - 56px);
  padding: 32px;
}}

/* HERO */
.hero {{
  background: linear-gradient(135deg, #3e496e 0%, #2a3352 100%);
  margin: -32px -32px 32px;
  padding: 48px 32px;
  color: #fff;
}}
.hero-label {{
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: rgba(255,255,255,0.6);
  margin-bottom: 12px;
}}
.hero h1 {{
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin-bottom: 16px;
}}
.hero p {{
  font-size: 15px;
  line-height: 1.7;
  color: rgba(255,255,255,0.75);
  max-width: 640px;
}}
.hero-stats {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 32px;
  max-width: 560px;
}}
.hero-stat {{
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: var(--radius);
  padding: 16px;
  text-align: center;
}}
.hero-stat-num {{
  font-size: 26px;
  font-weight: 800;
  color: #fff;
}}
.hero-stat-label {{
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(255,255,255,0.55);
  margin-top: 4px;
}}
.hero-actions {{
  display: flex;
  gap: 12px;
  margin-top: 28px;
}}
.btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: var(--radius);
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  cursor: pointer;
  transition: all 0.15s;
  border: none;
}}
.btn-primary {{
  background: #fff;
  color: var(--header-bg);
}}
.btn-primary:hover {{
  background: var(--surface-2);
}}
.btn-outline {{
  background: transparent;
  color: #fff;
  border: 1px solid rgba(255,255,255,0.3);
}}
.btn-outline:hover {{
  border-color: #fff;
  background: rgba(255,255,255,0.08);
}}

/* SECTION */
.section-title {{
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}}
.section-title::before {{
  content: '';
  width: 4px;
  height: 20px;
  background: var(--header-bg);
  border-radius: 2px;
}}

/* CARDS GRID */
.cards-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 16px;
  margin-bottom: 32px;
}}
.card {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow-card);
  transition: all 0.15s;
}}
.card:hover {{
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  transform: translateY(-1px);
}}
.card-icon {{
  width: 36px; height: 36px;
  background: var(--surface-2);
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
  font-size: 18px;
}}
.card h3 {{
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 8px;
}}
.card p {{
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 14px;
}}
.card-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}}
.tag {{
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  background: var(--surface-2);
  color: var(--text-secondary);
  border-radius: 4px;
  border: 1px solid var(--border);
}}

/* TABLE */
.table-wrap {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  margin-bottom: 32px;
}}
.table-header {{
  display: grid;
  grid-template-columns: 100px 1fr 120px;
  padding: 12px 20px;
  background: var(--header-bg);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: rgba(255,255,255,0.8);
}}
.table-row {{
  display: grid;
  grid-template-columns: 100px 1fr 120px;
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
  font-size: 13px;
  align-items: center;
}}
.table-row:last-child {{ border-bottom: none; }}
.table-row:nth-child(even) {{ background: var(--surface); }}
.table-id {{ font-family: 'SF Mono', monospace; font-size: 12px; color: var(--text-muted); font-weight: 500; }}
.table-status {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
}}
.status-dot {{
  width: 7px; height: 7px;
  border-radius: 50%;
  display: inline-block;
}}

/* JOURNAL CARDS */
.journal-grid {{
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 24px;
}}
.filters {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  height: fit-content;
  position: sticky;
  top: 80px;
}}
.filters h3 {{
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border);
}}
.filter-group {{
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 20px;
}}
.filter-item {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--text-secondary);
  cursor: pointer;
}}
.filter-item:hover {{ color: var(--text); }}
.filter-check {{
  width: 16px; height: 16px;
  border: 1.5px solid var(--border);
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  color: #fff;
}}
.filter-check.checked {{
  background: var(--header-bg);
  border-color: var(--header-bg);
}}

/* ENTRY CARD */
.entry-card {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow);
  transition: all 0.15s;
  margin-bottom: 16px;
}}
.entry-card:hover {{
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
}}
.entry-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}}
.entry-meta {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
}}
.entry-type {{
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 4px 10px;
  border-radius: 4px;
  border: 1px solid;
}}
.entry-type.urgent {{
  background: var(--urgent-bg);
  color: var(--urgent);
  border-color: rgba(196,92,62,0.2);
}}
.entry-type.normal {{
  background: var(--normal-bg);
  color: var(--normal);
  border-color: rgba(62,73,110,0.2);
}}
.entry-card h2 {{
  font-size: 17px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 10px;
  letter-spacing: -0.01em;
}}
.entry-card p {{
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 16px;
}}
.entry-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid var(--border);
  font-size: 12px;
  color: var(--text-muted);
}}
.entry-link {{
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--header-bg);
  display: flex;
  align-items: center;
  gap: 6px;
}}
.entry-link:hover {{ text-decoration: underline; }}

/* INTERVENTION DETAIL */
.back-link {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--header-bg);
  margin-bottom: 24px;
  padding: 8px 14px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: #fff;
}}
.back-link:hover {{ background: var(--surface); }}

.int-header {{
  border-bottom: 1px solid var(--border);
  padding-bottom: 24px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 16px;
}}
.int-type {{
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--urgent);
  margin-bottom: 10px;
}}
.int-header h1 {{
  font-size: 28px;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
  color: var(--text);
}}
.int-id {{
  font-size: 13px;
  color: var(--text-muted);
  margin-top: 6px;
  font-family: 'SF Mono', monospace;
}}
.int-meta-right {{
  text-align: right;
}}
.int-meta-right div {{
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: flex-end;
}}

.int-grid {{
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 24px;
}}

.panel {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  margin-bottom: 16px;
}}
.panel-header {{
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}}
.panel-header h2 {{
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text);
}}
.panel-body {{
  padding: 20px;
}}
.panel-body p {{
  font-size: 13px;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 12px;
}}
.panel-body p strong {{
  color: var(--text);
  font-weight: 600;
}}

.problem-panel .panel-header {{ background: var(--urgent-bg); }}
.problem-panel .panel-header h2 {{ color: var(--urgent); }}
.result-panel .panel-header {{ background: var(--normal-bg); }}
.result-panel .panel-header h2 {{ color: var(--normal); }}

.action-list {{
  display: flex;
  flex-direction: column;
  gap: 12px;
}}
.action-item {{
  display: flex;
  gap: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}}
.action-item:last-child {{ border-bottom: none; padding-bottom: 0; }}
.action-num {{
  font-family: 'SF Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--urgent);
  min-width: 28px;
}}
.action-text {{
  font-size: 13px;
  line-height: 1.7;
  color: var(--text-secondary);
}}

.metrics-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-top: 16px;
}}
.metric-box {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  text-align: center;
}}
.metric-label {{
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin-bottom: 6px;
}}
.metric-value {{
  font-size: 22px;
  font-weight: 800;
  color: var(--header-bg);
}}

/* RIGHT SIDEBAR PANELS */
.side-panel {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 16px;
}}
.side-panel h3 {{
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border);
}}
.side-row {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
  font-size: 13px;
}}
.side-row:last-child {{ border-bottom: none; }}
.side-label {{ color: var(--text-secondary); }}
.side-value {{
  color: var(--text);
  font-weight: 600;
  font-family: 'SF Mono', monospace;
  font-size: 12px;
}}

.piece-item {{
  display: flex;
  gap: 12px;
  padding: 10px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  margin-bottom: 8px;
}}
.piece-icon {{
  width: 32px; height: 32px;
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}}
.piece-name {{
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
}}
.piece-ref {{
  font-size: 11px;
  color: var(--text-muted);
  font-family: 'SF Mono', monospace;
  margin-top: 2px;
}}

.tool-tag {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 10px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  color: var(--text-secondary);
  margin: 0 6px 6px 0;
}}

/* CONTACT */
.contact-grid {{
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 24px;
}}
.contact-info {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}
.contact-row {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  font-size: 13px;
  color: var(--text-secondary);
}}
.contact-row strong {{
  color: var(--text);
  font-weight: 600;
}}

.form-group {{
  margin-bottom: 16px;
}}
.form-group label {{
  display: block;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  margin-bottom: 6px;
}}
.form-group input,
.form-group select,
.form-group textarea {{
  width: 100%;
  padding: 12px 14px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: #fff;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  color: var(--text);
  transition: all 0.15s;
}}
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {{
  outline: none;
  border-color: var(--header-bg);
  box-shadow: 0 0 0 3px rgba(62,73,110,0.08);
}}

/* FOOTER */
.footer {{
  margin-left: 240px;
  padding: 24px 32px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: var(--text-muted);
}}
.footer a {{
  color: var(--text-muted);
  margin-left: 20px;
  font-size: 12px;
}}
.footer a:hover {{ color: var(--text); }}

/* RESPONSIVE */
@media (max-width: 900px) {{
  .sidebar {{ display: none; }}
  .main {{ margin-left: 0; }}
  .footer {{ margin-left: 0; }}
  .int-grid {{ grid-template-columns: 1fr; }}
  .journal-grid {{ grid-template-columns: 1fr; }}
  .contact-grid {{ grid-template-columns: 1fr; }}
  .hero h1 {{ font-size: 28px; }}
  .hero-stats {{ grid-template-columns: repeat(2, 1fr); }}
  .metrics-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
</style>
</head>
'''

TOPBAR = '''
<div class="topbar">
  <div class="topbar-brand">TechMaintenance Pro</div>
  <nav class="topbar-nav">
    <a href="index.html" class="{home_class}">Accueil</a>
    <a href="journal.html" class="{journal_class}">Journal</a>
    <a href="contact.html" class="{contact_class}">Contact</a>
  </nav>
</div>
'''

SIDEBAR = '''
<aside class="sidebar">
  <div class="sidebar-profile">
    <div class="sidebar-name">{name}</div>
    <div class="sidebar-title">{title}</div>
  </div>
  <nav class="sidebar-nav">
    <a href="index.html" class="{home_class}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
      Overview
    </a>
    <a href="journal.html" class="{journal_class}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
      Interventions
    </a>
    <a href="index.html#certifications">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      Certifications
    </a>
    <a href="contact.html">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      Contact
    </a>
  </nav>
  <div class="sidebar-footer" style="margin-top:auto;">
    <a href="contact.html">Télécharger CV</a>
  </div>
</aside>
'''

FOOTER = '''
<footer class="footer">
  <span>© 2024 {name} — Technicien Maintenance Industrielle</span>
  <div>
    <a href="index.html">Accueil</a>
    <a href="journal.html">Journal</a>
    <a href="contact.html">Contact</a>
  </div>
</footer>
'''


def build_page(title, active, content):
    home = 'active' if active == 'home' else ''
    journal = 'active' if active == 'journal' else ''
    contact = 'active' if active == 'contact' else ''
    
    topbar = TOPBAR.format(home_class=home, journal_class=journal, contact_class=contact)
    sidebar = SIDEBAR.format(name=PROFILE["name"], title=PROFILE["title"], home_class=home, journal_class=journal)
    footer = FOOTER.format(name=PROFILE["name"])
    
    return HEADER.format(title=title) + f'''
<body>
{topbar}
{sidebar}
<main class="main">
{content}
</main>
{footer}
</body>
</html>'''


# ============================================================
# INDEX
# ============================================================
def build_index():
    comp_cards = ""
    for c in COMPETENCES:
        tags = " ".join([f'<span class="tag">{t}</span>' for t in c["tags"]])
        comp_cards += f'''
        <div class="card">
          <div class="card-icon">{c["icon"][:1]}</div>
          <h3>{c["category"]}</h3>
          <p>{c["description"]}</p>
          <div class="card-tags">{tags}</div>
        </div>'''
    
    cert_rows = ""
    for cert in CERTIFICATIONS:
        dot = "background:#4a7c59" if "Validé" in cert["status"] else "background:#c9a227"
        cert_rows += f'''
        <div class="table-row">
          <div class="table-id">{cert["id"]}</div>
          <div style="color:var(--text);font-weight:500;">{cert["name"]}</div>
          <div class="table-status"><span class="status-dot" style="{dot}"></span> {cert["status"]}</div>
        </div>'''
    
    content = f'''
<div class="hero">
  <div class="container" style="padding:0;">
    <div class="hero-label">Technicien Supérieur</div>
    <h1>Expertise en Maintenance Industrielle</h1>
    <p>{PROFILE["summary"]}</p>
    <div class="hero-stats">
      <div class="hero-stat"><div class="hero-stat-num">{PROFILE["years"]}</div><div class="hero-stat-label">Années</div></div>
      <div class="hero-stat"><div class="hero-stat-num">{PROFILE["companies"]}</div><div class="hero-stat-label">Entreprises</div></div>
      <div class="hero-stat"><div class="hero-stat-num">{PROFILE["countries"]}</div><div class="hero-stat-label">Pays</div></div>
      <div class="hero-stat"><div class="hero-stat-num">{PROFILE["fiches"]}</div><div class="hero-stat-label">Fiches</div></div>
    </div>
    <div class="hero-actions">
      <a href="journal.html" class="btn btn-primary">Journal des Pannes</a>
      <a href="contact.html" class="btn btn-outline">Voir le CV</a>
    </div>
  </div>
</div>

<div class="section-title">Compétences Clés</div>
<div class="cards-grid">
{comp_cards}
</div>

<div id="certifications" class="section-title">Certifications Techniques</div>
<div class="table-wrap">
  <div class="table-header">
    <div>ID</div>
    <div>Désignation</div>
    <div style="text-align:right;">Statut</div>
  </div>
{cert_rows}
</div>
'''
    return build_page("Portfolio — Salah Eddine Barki", "home", content)


# ============================================================
# JOURNAL
# ============================================================
def build_journal():
    entries = ""
    for f in FICHES:
        tc = "urgent" if f["typeColor"] == "urgent" else "normal"
        short = f['symptome'][:140] + "..." if len(f['symptome']) > 140 else f['symptome']
        entries += f'''
        <div class="entry-card">
          <div class="entry-header">
            <div class="entry-meta">
              <span>{f["date"]}</span>
              <span style="color:var(--border);">|</span>
              <span>{f["duree"]}</span>
            </div>
            <span class="entry-type {tc}">{f["type"]}</span>
          </div>
          <h2>{f["titre"]}</h2>
          <p>{short}</p>
          <div class="entry-footer">
            <span>{f["entreprise"]} — {f["lieu"]}</span>
            <a href="intervention_{f["num"]}.html" class="entry-link">Voir le détail →</a>
          </div>
        </div>'''
    
    content = f'''
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:24px;">
  <div>
    <h1 style="font-size:28px;font-weight:800;letter-spacing:-0.02em;">Journal of Interventions</h1>
    <p style="font-size:13px;color:var(--text-muted);margin-top:6px;">Official log of technical maintenance procedures, repairs, and system calibrations.</p>
  </div>
  <span style="font-size:12px;color:var(--text-muted);font-family:monospace;">{len(FICHES)} ENTRIES</span>
</div>

<div class="journal-grid">
  <div class="filters">
    <h3>System Category</h3>
    <div class="filter-group">
      <label class="filter-item"><div class="filter-check checked">✓</div> Electrical</label>
      <label class="filter-item"><div class="filter-check"></div> Hydraulics</label>
      <label class="filter-item"><div class="filter-check"></div> Pneumatics</label>
      <label class="filter-item"><div class="filter-check"></div> Automatisme</label>
    </div>
    <h3>Status</h3>
    <div class="filter-group">
      <label class="filter-item"><div class="filter-check checked">✓</div> Resolved</label>
      <label class="filter-item"><div class="filter-check checked">✓</div> Active</label>
    </div>
  </div>
  <div>
{entries}
  </div>
</div>
'''
    return build_page("Journal — TechMaintenance Pro", "journal", content)


# ============================================================
# INTERVENTION
# ============================================================
def build_intervention(f):
    actions_html = ""
    for i, a in enumerate(f["actions"]):
        actions_html += f'''<div class="action-item"><span class="action-num">{str(i+1).zfill(2)}.</span><span class="action-text">{a}</span></div>'''
    
    metrics_html = ""
    for m in f["metriques"]:
        metrics_html += f'''<div class="metric-box"><div class="metric-label">{m["label"]}</div><div class="metric-value">{m["value"]}</div></div>'''
    
    pieces_html = ""
    for p in f["pieces"]:
        pieces_html += f'''
        <div class="piece-item">
          <div class="piece-icon">⚙</div>
          <div>
            <div class="piece-name">{p["name"]}</div>
            <div class="piece-ref">Réf: {p["ref"]} | Qté: {p["qty"]}</div>
          </div>
        </div>'''
    if not pieces_html:
        pieces_html = '<div style="font-size:12px;color:var(--text-muted);">Aucune pièce remplacée</div>'
    
    tools_html = ""
    for t in f["outillage"]:
        tools_html += f'<span class="tool-tag">🔧 {t}</span>'
    
    tc = "urgent" if f["typeColor"] == "urgent" else "normal"
    
    content = f'''
<a href="journal.html" class="back-link">← Retour aux interventions</a>

<div class="int-header">
  <div>
    <div class="int-type">{f["type"]}</div>
    <h1>{f["titre"]}</h1>
    <div class="int-id">Rapport d'intervention technique #{f["id"]}</div>
  </div>
  <div class="int-meta-right">
    <div>📅 {f["date"]}</div>
    <div>⏱ {f["duree"]}</div>
    <div>🔧 Tech: {f["tech"]}</div>
  </div>
</div>

<div class="int-grid">
  <div>
    <div class="panel problem-panel">
      <div class="panel-header"><h2>⚠ Le Problème</h2></div>
      <div class="panel-body">
        <p><strong>Contexte :</strong> {f["contexte"]}</p>
        <p><strong>Symptôme :</strong> {f["symptome"]}</p>
        <div style="background:var(--surface);border:1px solid var(--border);padding:14px 16px;border-radius:var(--radius);display:flex;gap:14px;align-items:center;margin-top:12px;">
          <span style="font-size:22px;">📡</span>
          <div>
            <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-muted);margin-bottom:4px;">Équipement concerné</div>
            <div style="font-size:13px;color:var(--text);font-weight:600;">{f["equip"][:55]}...</div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="panel">
      <div class="panel-header"><h2>🔍 Diagnostic</h2></div>
      <div class="panel-body">
        <p>{f["diagnostic"]}</p>
      </div>
    </div>
    
    <div class="panel">
      <div class="panel-header"><h2>🔧 Solution Apportée</h2></div>
      <div class="panel-body">
        <div class="action-list">
{actions_html}
        </div>
      </div>
    </div>
    
    <div class="panel result-panel">
      <div class="panel-header"><h2>✓ Résultat</h2></div>
      <div class="panel-body">
        <p>{f["resultat"]}</p>
        <div class="metrics-grid">
{metrics_html}
        </div>
      </div>
    </div>
  </div>
  
  <aside>
    <div class="side-panel">
      <h3>Spécifications Équipement</h3>
      <div class="side-row"><span class="side-label">Système</span><span class="side-value">{f["equip"][:30]}...</span></div>
      <div class="side-row"><span class="side-label">Localisation</span><span class="side-value">{f["lieu"]}</span></div>
      <div class="side-row"><span class="side-label">Entreprise</span><span class="side-value">{f["entreprise"]}</span></div>
      <div class="side-row"><span class="side-label">Criticité</span><span class="side-value" style="color:var(--urgent);">Tier 1 — Vital</span></div>
    </div>
    
    <div class="side-panel">
      <h3>Inventaire Pièces</h3>
{pieces_html}
    </div>
    
    <div class="side-panel">
      <h3>Matériel Déployé</h3>
      <div style="display:flex;flex-wrap:wrap;">
{tools_html}
      </div>
    </div>
  </aside>
</div>
'''
    return build_page(f"{f['titre']} — TechMaintenance Pro", "journal", content)


# ============================================================
# CONTACT
# ============================================================
def build_contact():
    content = f'''
<div class="contact-grid">
  <div>
    <h1 style="font-size:28px;font-weight:800;letter-spacing:-0.02em;margin-bottom:8px;">Contact</h1>
    <p style="font-size:14px;color:var(--text-secondary);margin-bottom:24px;">Ready to discuss structural integrity and precision maintenance.</p>
    
    <div style="background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;margin-bottom:20px;">
      <div style="font-size:32px;margin-bottom:8px;">📄</div>
      <h3 style="font-size:16px;font-weight:700;margin-bottom:6px;">Technical Blueprint</h3>
      <p style="font-size:13px;color:var(--text-secondary);margin-bottom:16px;">Comprehensive overview of methodologies, certifications, and operational history.</p>
      <a href="../Portfolio_Salah_Barki_v5.pptx" download class="btn btn-primary" style="width:100%;justify-content:center;">Télécharger mon CV</a>
    </div>
    
    <div class="contact-info">
      <div class="contact-row"><span>📱</span> <strong>{PROFILE["contact"]["phone"]}</strong></div>
      <div class="contact-row"><span>✉️</span> <strong>{PROFILE["contact"]["email"]}</strong></div>
      <div class="contact-row"><span>📍</span> <strong>{PROFILE["contact"]["location"]}</strong></div>
    </div>
    
    <div style="margin-top:20px;">
      <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-muted);margin-bottom:12px;">Verified Credentials</div>
      <div style="display:flex;flex-wrap:wrap;gap:6px;">
        <span class="tag">ISO 9001</span>
        <span class="tag">PLC Adv.</span>
        <span class="tag">Hydraulics II</span>
        <span class="tag">LOTO</span>
      </div>
    </div>
  </div>
  
  <div style="background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div class="section-title" style="margin-bottom:20px;">Envoyer un message</div>
    <form onsubmit="event.preventDefault();alert('Message envoyé !');">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <div class="form-group">
          <label>Nom / Société</label>
          <input type="text" placeholder="Votre nom..."/>
        </div>
        <div class="form-group">
          <label>Email</label>
          <input type="email" placeholder="votre@email.com"/>
        </div>
      </div>
      <div class="form-group">
        <label>Sujet</label>
        <select>
          <option>Proposition d'emploi</option>
          <option>Consultation technique</option>
          <option>Collaboration</option>
          <option>Autre</option>
        </select>
      </div>
      <div class="form-group">
        <label>Message</label>
        <textarea rows="5" placeholder="Votre message..."></textarea>
      </div>
      <div style="text-align:right;">
        <button type="submit" class="btn btn-primary">Envoyer →</button>
      </div>
    </form>
  </div>
</div>
'''
    return build_page("Contact — TechMaintenance Pro", "contact", content)


if __name__ == "__main__":
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index())
    print("[OK] index.html")
    
    with open(os.path.join(OUTPUT_DIR, "journal.html"), "w", encoding="utf-8") as f:
        f.write(build_journal())
    print("[OK] journal.html")
    
    with open(os.path.join(OUTPUT_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(build_contact())
    print("[OK] contact.html")
    
    for fi in FICHES:
        with open(os.path.join(OUTPUT_DIR, f"intervention_{fi['num']}.html"), "w", encoding="utf-8") as f:
            f.write(build_intervention(fi))
        print(f"[OK] intervention_{fi['num']}.html")
    
    # Copy server
    import shutil
    shutil.copy(r"C:\Users\ba2rb\Downloads\salpre\site_v2\server.js", os.path.join(OUTPUT_DIR, "server.js"))
    print("\n=== SITE V3 GÉNÉRÉ ===")
    print(f"Dossier: {OUTPUT_DIR}")
    print("Pour lancer le serveur: node server.js")
