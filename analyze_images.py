from PIL import Image
import os

for name in ['image.png', 'image copy.png', 'image copy 2.png']:
    p = os.path.join(r'C:\Users\ba2rb\Downloads\salpre', name)
    if not os.path.exists(p):
        print(f'\n=== {name}: NOT FOUND ===')
        continue
    img = Image.open(p)
    print(f'\n=== {name} ===')
    print(f'Size: {img.size}')
    print(f'Mode: {img.mode}')
    small = img.resize((100, 100))
    if small.mode != 'RGB':
        small = small.convert('RGB')
    colors = small.getcolors(10000)
    if colors:
        colors.sort(key=lambda x: x[0], reverse=True)
        top = colors[:10]
        print('Top colors (count, hex):')
        for count, rgb in top:
            print(f'  #{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}  count={count}')
    pixels = list(small.getdata())
    avg_r = sum(p[0] for p in pixels) / len(pixels)
    avg_g = sum(p[1] for p in pixels) / len(pixels)
    avg_b = sum(p[2] for p in pixels) / len(pixels)
    brightness = (avg_r + avg_g + avg_b) / 3
    if brightness < 80:
        mood = 'DARK'
    elif brightness > 200:
        mood = 'LIGHT'
    else:
        mood = 'MID'
    print(f'Average brightness: {brightness:.1f}/255 -> {mood}')
    print(f'RGB avg: ({avg_r:.0f}, {avg_g:.0f}, {avg_b:.0f})')
    # Saturation hints
    maxc = max(avg_r, avg_g, avg_b)
    minc = min(avg_r, avg_g, avg_b)
    saturation = (maxc - minc) / maxc if maxc > 0 else 0
    print(f'Saturation hint: {saturation:.2f}')
    # Grid sample for layout
    w, h = small.size
    print('Grid sample (corner colors):')
    for y in range(0, h, 25):
        row = []
        for x in range(0, w, 25):
            r, g, b = small.getpixel((x, y))
            row.append(f'{r:02x}{g:02x}{b:02x}')
        print('  ' + ' '.join(row[:4]))
