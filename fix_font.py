import os, glob

DIR = r"C:\Users\ba2rb\Downloads\salpre\site_v2"

for path in glob.glob(os.path.join(DIR, "*.html")):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ensure Inter font is enforced on body
    if "font-family: 'Inter'" not in content:
        content = content.replace(
            '</head>',
            "<style>body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif !important;}</style>\n</head>"
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    print(os.path.basename(path))

print("Done — Industrial colors kept, Inter font enforced.")
