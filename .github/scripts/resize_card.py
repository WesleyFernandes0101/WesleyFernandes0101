"""Envolve o card de horários (340x200) em uma moldura 350x215,
para ficar do mesmo tamanho do card de linguagens ao lado."""
import re, sys

src, dst = sys.argv[1], sys.argv[2]
W, H = 350, 215
svg = open(src, encoding="utf-8").read()

# traduz os textos do card para português
TRADUCOES = {
    r"Commits \(UTC [^)]*\)": "Commits por horário",
    r"per day hour": "hora do dia",
}
for de, para in TRADUCOES.items():
    svg = re.sub(de, para, svg)

# tamanho original do card
w = float(re.search(r'<svg[^>]*\bwidth="([\d.]+)', svg).group(1))
h = float(re.search(r'<svg[^>]*\bheight="([\d.]+)', svg).group(1))
scale = min(W / w, H / h)
nw, nh = w * scale, h * scale
x, y = (W - nw) / 2, (H - nh) / 2

inner = re.sub(r'^\s*<\?xml[^>]*\?>', '', svg).strip()
inner = re.sub(r'(<svg[^>]*?)\s(?:width|height)="[\d.]+"', r'\1', inner, count=1)
inner = re.sub(r'(<svg[^>]*?)\s(?:width|height)="[\d.]+"', r'\1', inner, count=1)
inner = re.sub(r'<svg',f'<svg x="{x:.2f}" y="{y:.2f}" width="{nw:.2f}" height="{nh:.2f}"', inner, count=1)

out = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
       f'<rect width="{W}" height="{H}" rx="5" fill="#282a36"/>{inner}</svg>')
open(dst, "w", encoding="utf-8").write(out)
