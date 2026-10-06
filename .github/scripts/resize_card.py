"""Envolve o card de horários (340x200) em uma moldura 390x215,
para ficar do mesmo tamanho do card de linguagens ao lado."""
import re, sys

src, dst = sys.argv[1], sys.argv[2]
W, H = 390, 215
svg = open(src, encoding="utf-8").read()

# tamanho original do card
w = float(re.search(r'<svg[^>]*\bwidth="([\d.]+)', svg).group(1))
h = float(re.search(r'<svg[^>]*\bheight="([\d.]+)', svg).group(1))
scale = H / h
nw = w * scale
x = (W - nw) / 2

inner = re.sub(r'^\s*<\?xml[^>]*\?>', '', svg).strip()
inner = re.sub(r'(<svg[^>]*?)\s(?:width|height)="[\d.]+"', r'\1', inner, count=1)
inner = re.sub(r'(<svg[^>]*?)\s(?:width|height)="[\d.]+"', r'\1', inner, count=1)
inner = re.sub(r'<svg',f'<svg x="{x:.2f}" y="0" width="{nw:.2f}" height="{H}"', inner, count=1)

out = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
       f'<rect width="{W}" height="{H}" rx="5" fill="#282a36"/>{inner}</svg>')
open(dst, "w", encoding="utf-8").write(out)
