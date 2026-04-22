import os
import glob

# HTML files to patch
html_files = glob.glob(r"C:\Users\ba2rb\Downloads\salpre\*.html")

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Skip if already patched
    if 'nav-toggle' in content:
        print(f"[SKIP] {os.path.basename(filepath)}")
        continue
    
    # Add hidden checkbox + hamburger button before </header>
    old = "  </div>\n</header>"
    new = """  </div>
  <input type="checkbox" id="nav-toggle" hidden/>
  <label for="nav-toggle" class="menu-btn" aria-label="Menu">☰</label>
  <nav class="mobile-nav">
    <label for="nav-toggle" class="mobile-nav-close" aria-label="Fermer">×</label>
    <a href="index.html">01 · Overview</a>
    <a href="journal.html">02 · Journal</a>
    <a href="contact.html">03 · Contact</a>
  </nav>
</header>"""
    content = content.replace(old, new)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] {os.path.basename(filepath)}")

print("\nAll HTML files patched.")
