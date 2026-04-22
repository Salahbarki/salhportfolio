import re

filepath = r"C:\Users\ba2rb\Downloads\salpre\site_v4\journal.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace opening <article class="log-card ...> with <a href="intervention_XX.html" class="log-card ...>
content = re.sub(
    r'<article class="log-card([^"]*)"([^>]*)>',
    lambda m: f'<a href="intervention_{m.group(2).split("INT-")[1][:4] if "INT-" in m.group(2) else "01"}.html" class="log-card{m.group(1)}"{m.group(2)}>',
    content
)

# Actually better approach: replace article with a but we need the href. 
# Let's do it intervention by intervention using simpler string replacement
for i in range(1, 12):
    num = f"{i:02d}"
    old_open = f'<article class="log-card'
    # We need to find and replace each article with the correct href

# Better: read the file and replace each article block
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

output = []
article_lines = []
in_article = False
article_idx = 1

for line in lines:
    if '<article class="log-card' in line:
        in_article = True
        article_lines = [line]
        continue
    if in_article:
        article_lines.append(line)
        if '</article>' in line:
            block = ''.join(article_lines)
            # extract intervention number from Detail link
            m = re.search(r'href="intervention_(\d+)\.html"', block)
            if m:
                href = f"intervention_{m.group(1)}.html"
            else:
                href = f"intervention_{article_idx:02d}.html"
            block = block.replace('<article ', f'<a href="{href}" ')
            block = block.replace('</article>', '</a>')
            # Replace the inner Detail link
            block = re.sub(r'<a href="intervention_\d+\.html">Détail →</a>', '<span class="detail-link">Détail →</span>', block)
            output.append(block)
            in_article = False
            article_lines = []
            article_idx += 1
        continue
    output.append(line)

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(output)

print("[OK] site_v4/journal.html patched")
