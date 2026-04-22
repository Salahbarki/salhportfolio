import os

IMG_DIR = r'C:\Users\ba2rb\Downloads\salpre'
SITE_DIR = r'C:\Users\ba2rb\Downloads\salpre\site_v2'

images = {
    '01': 'img_01_encartonneuse.png',
    '02': 'img_02_presse_injection.png',
    '03': 'img_03_automate_s7.png',
    '04': 'img_04_banc_test.png',
    '05': 'img_05_hydraulique.png',
    '06': 'img_06_gmao.png',
}

old_block = '''<div class="bg-surface-container-low border border-outline-variant p-stack-md flex flex-col items-center justify-center text-center">
                                <span class="material-symbols-outlined text-primary text-[48px] mb-2">psychology</span>
                                <div class="font-label-caps text-label-caps text-on-surface-variant">Méthode RCA</div>
                                <div class="font-data-mono text-data-mono text-primary mt-1">5 Pourquoi + Pareto + Ishikawa</div>
                            </div>'''

for num, img in images.items():
    path = os.path.join(SITE_DIR, f'intervention_{num}.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_block in content:
        new_block = f'<div style="border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;height:220px;max-height:220px;">\n                                <img src="../{img}" alt="Technical photo" style="width:100%;height:100%;object-fit:cover;" />\n                            </div>'
        content = content.replace(old_block, new_block)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[OK] intervention_{num}.html')
    else:
        print(f'[WARN] intervention_{num}.html — block not found')
