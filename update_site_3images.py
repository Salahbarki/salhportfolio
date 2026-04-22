import os, re

SITE_DIR = r"C:\Users\ba2rb\Downloads\salpre\site_v2"

IMAGES = {
    '01': ['img_01a_overview.png', 'img_01b_sensor.png', 'img_01c_guide.png'],
    '02': ['img_02a_overview.png', 'img_02b_secheur.png', 'img_02c_detecteur.png'],
    '03': ['img_03a_cell.png', 'img_03b_s7.png', 'img_03c_servo.png'],
    '04': ['img_04a_overview.png', 'img_04b_connecteur.png', 'img_04c_ohmmetre.png'],
    '05': ['img_05a_overview.png', 'img_05b_manometre.png', 'img_05c_clapet.png'],
    '06': ['img_06a_room.png', 'img_06b_kpi.png', 'img_06c_planning.png'],
}

for num in IMAGES:
    path = os.path.join(SITE_DIR, f'intervention_{num}.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find any div containing img_0X
    rx = re.compile(r'<div[^>]*>\s*<img\s+src="\.\.\/img_' + num + r'[^"]*"[^/]*/?>\s*</div>')
    m = rx.search(content)
    if m:
        # Build 3-image grid
        grid = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px;">\n'
        for img in IMAGES[num]:
            grid += f'                                <div style="border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;height:160px;">\n'
            grid += f'                                    <img src="../{img}" alt="Technical photo" style="width:100%;height:100%;object-fit:cover;" />\n'
            grid += f'                                </div>\n'
        grid += '                            </div>'
        
        content = content[:m.start()] + grid + content[m.end():]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[OK] intervention_{num}.html')
    else:
        print(f'[WARN] intervention_{num}.html — no img block found')

print("\nSite updated.")
