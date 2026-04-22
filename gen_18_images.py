import os, json, base64, urllib.request

API_KEY = os.environ.get("AZURE_API_KEY", "YOUR_API_KEY_HERE")
API_URL = "https://ba2rba-2051-resource.services.ai.azure.com/providers/blackforestlabs/v1/flux-2-pro?api-version=preview"
OUT = r"C:\Users\ba2rb\Downloads\salpre"

PROMPTS = [
    # === 01 ENCARTONNEUSE PET ===
    ("img_01a_overview.png", "Wide angle photograph of a modern clean beverage production line in a brand new factory. Stainless steel carton packaging machine, PET bottles on conveyor, bright white LED overhead lighting, spotless white epoxy floor, organized pneumatic tubing, no people, industrial product photography, sharp clean modern aesthetic"),
    ("img_01b_sensor.png", "Close-up photograph of a modern industrial photo-electric proximity sensor mounted on a clean stainless steel bracket. Sensor has purge-air fitting, IP67 housing, blue LED indicator, clean factory background with soft bokeh, no people, sharp product photography, bright modern lighting"),
    ("img_01c_guide.png", "Close-up photograph of a precision mechanical guide rail and hydraulic damper on a packaging machine. Feeler gauge showing 0.5mm gap, clean lubricated surfaces, stainless steel construction, bright modern factory lighting, no people, technical macro photography"),
    
    # === 02 PRESSE INJECTION ===
    ("img_02a_overview.png", "Wide angle photograph of a modern plastic injection molding production cell. 120-ton electric injection press with clean white and blue paint, polymer dryer hopper, inline metal detector, organized cable trays, bright clean factory with white LED lighting, no people, modern industrial photography"),
    ("img_02b_secheur.png", "Close-up photograph of a modern polymer resin dryer unit. Transparent hopper showing white plastic pellets inside, digital dewpoint display reading minus forty two degrees, clean stainless steel frame, blue status LED, bright modern lighting, no people, product photography"),
    ("img_02c_detecteur.png", "Close-up photograph of a modern inline metal detector sensor on a production line. Stainless steel rectangular frame, blue LED status light, clean conveyor belt passing through, bright modern factory background, no people, sharp industrial photography"),
    
    # === 03 AUTOMATE S7 ===
    ("img_03a_cell.png", "Wide angle photograph of a modern automation assembly cell. Small white and silver robotic pick-and-place arm, clean electrical cabinet with glass door, organized cable management in blue and gray, bright white factory lighting, no people, sleek modern industrial photography"),
    ("img_03b_s7.png", "Close-up photograph of a Siemens S7-1200 PLC module mounted on a clean DIN rail inside an electrical cabinet. Ethernet cable plugged in, status LEDs glowing green, organized wire ferrules, clean modern wiring, soft technical lighting, no people, sharp product photography"),
    ("img_03c_servo.png", "Close-up photograph of a modern servo motor with precision encoder cable. Clean metal coupling connecting to a mechanical arm, blue reflective housing, alignment marks visible, bright modern lighting, no people, technical macro photography"),
    
    # === 04 BANC TEST ===
    ("img_04a_overview.png", "Wide angle photograph of a modern automotive wire harness quality control laboratory. Clean white test bench with multiple connector fixtures, LED task lighting, organized tool shadow board on wall, bright clean room environment, no people, modern laboratory photography"),
    ("img_04b_connecteur.png", "Extreme close-up macro photograph of a brand new automotive 32-pin electrical connector. Gold-plated pins perfectly aligned, no oxidation, clean plastic housing, white background, bright even lighting, no people, technical macro photography"),
    ("img_04c_ohmmetre.png", "Close-up photograph of a modern handheld digital micro-ohmmeter with Kelvin clip probes attached. Clean LCD display showing resistance reading in milliohms, sitting on a white workbench, bright modern lighting, no people, product photography"),
    
    # === 05 HYDRAULIQUE ===
    ("img_05a_overview.png", "Wide angle photograph of a modern hydraulic press in a clean industrial workshop. Machine has clean blue and gray paint, analog pressure gauges on front panel, organized hydraulic hose routing, white LED lighting, clean floor, no people, modern industrial photography"),
    ("img_05b_manometre.png", "Close-up photograph of a modern industrial analog pressure gauge reading eighty bar. Clean glass face, stainless steel bezel, mounted on a hydraulic manifold, bright modern lighting, sharp detail, no people, technical photography"),
    ("img_05c_clapet.png", "Close-up photograph of a new hydraulic directional valve mounted on a clean manifold block. Precision-machined aluminum body, no leaks, fresh O-rings visible, clean hydraulic fittings, bright modern lighting, no people, macro product photography"),
    
    # === 06 GMAO ===
    ("img_06a_room.png", "Wide angle photograph of a modern maintenance planning office. Large printed KPI dashboard pinned to wall with magnets, clean whiteboard with color-coded maintenance schedule, organized desk with printed work orders and tablet, bright modern office lighting, no people, corporate photography"),
    ("img_06b_kpi.png", "Close-up photograph of printed paper charts and graphs pinned to a whiteboard. Bar chart showing MTBF and OEE metrics, color-coded with green and orange markers, professional printed layout, bright office lighting, no people, flat lay photography"),
    ("img_06c_planning.png", "Close-up photograph of a wall-mounted acrylic planning board. Monthly calendar grid with colored magnetic markers showing maintenance windows, work order tags clipped in slots, bright clean office lighting, no people, office detail photography")
]

def gen(fname, prompt):
    payload = json.dumps({"prompt": prompt, "model": "FLUX.2-pro", "width": 1024, "height": 1024, "n": 1}).encode('utf-8')
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    req = urllib.request.Request(API_URL, data=payload, headers=headers, method="POST")
    try:
        print(f"[START] {fname}")
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            b64 = data.get('data', [{}])[0].get('b64_json', '') or data.get('b64_json', '')
            if b64:
                img = base64.b64decode(b64)
                path = os.path.join(OUT, fname)
                with open(path, 'wb') as f:
                    f.write(img)
                print(f"[OK] {fname} {len(img)//1024}KB")
                return True
    except Exception as e:
        print(f"[FAIL] {fname}: {e}")
    return False

if __name__ == "__main__":
    ok = 0
    for fname, pr in PROMPTS:
        if gen(fname, pr):
            ok += 1
    print(f"\nDone: {ok}/{len(PROMPTS)} images")
