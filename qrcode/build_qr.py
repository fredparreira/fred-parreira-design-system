#!/usr/bin/env python3
"""
Gera o wallpaper 1080x1920 com QR Code de WhatsApp na identidade Fred Parreira.
Uso:  python build_qr.py
Dependencias:  pip install "qrcode[pil]" pillow
Verificacao (opcional):  pip install zxing-cpp opencv-python-headless
"""
import urllib.parse
import qrcode
from qrcode.constants import ERROR_CORRECT_M
from PIL import Image, ImageDraw, ImageFont

# ====================== CONFIGURACAO (edite aqui) ======================
NUMERO  = "5534991775536"   # DDI + DDD + numero, so digitos
MENSAGEM = (
    "Oi Fred! Te conheci no evento. Seguem seus dados pra eu salvar:\n\n"
    "\U0001F464 Fred Parreira\n"
    "\U0001F680 CEO Neway Insurtech | Workshops de IA e Inovação\n"
    "\U0001F393 Mestre em Inovação (IA + Design Thinking pra resolver problemas)\n"
    "\U0001F517 LN: linkedin.com/in/parreirafrederico\n"
    "\U0001F30D IG: instagram.com/fredparreira.me\n\n"
    "Bora trocar uma ideia? ☕"
)
TITULO    = "BORA CONECTAR?"
NOME      = "FRED PARREIRA"
CARGO     = ["CEO Neway Insurtech", "Workshops de IA e Inovação"]
PILL      = "in/parreirafrederico"
INSTRUCAO = ["Aponte a câmera do seu celular", "e me mande um oi no WhatsApp"]
LEGENDA   = "Você já recebe meus dados na conversa"
SAIDA     = "Fred_QR_WhatsApp_1080x1920.png"

# ====================== IDENTIDADE VISUAL ======================
LIME  = (220, 255, 0)     # Eletric Lime #DCFF00
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (165, 165, 165)
W, H  = 1080, 1920

# Fonte: ideal de marca = Exo 2 (Black 900 / Bold). Fallback automatico.
FONT_CANDIDATES_BOLD = [
    "Exo2-Black.ttf", "Exo2-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "arialbd.ttf", "Arial Bold.ttf",
]
FONT_CANDIDATES_REG = [
    "Exo2-Regular.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "arial.ttf", "Arial.ttf",
]
def _load(cands, size):
    for c in cands:
        try:
            return ImageFont.truetype(c, size)
        except Exception:
            continue
    return ImageFont.load_default()
fb = lambda s: _load(FONT_CANDIDATES_BOLD, s)   # bold/black
fr = lambda s: _load(FONT_CANDIDATES_REG, s)    # regular

# ====================== LINK + QR ======================
link = "https://wa.me/" + NUMERO + "?text=" + urllib.parse.quote(MENSAGEM)
print("LINK:", link)

qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=20, border=4)
qr.add_data(link)
qr.make(fit=True)
print("QR version:", qr.version, "| modulos:", qr.modules_count)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# ====================== COMPOSICAO ======================
img = Image.new("RGB", (W, H), BLACK)
d = ImageDraw.Draw(img)

def ctext(y, txt, font, color, ls=0):
    return ctextx(W / 2, y, txt, font, color, ls)

def ctextx(cx, y, txt, font, color, ls=0):
    bb = d.textbbox((0, 0), txt, font=font)
    w = bb[2] - bb[0]
    d.text((cx - w / 2, y), txt, font=font, fill=color)
    return y + (bb[3] - bb[1]) + ls

def _tw(txt, font):
    bb = d.textbbox((0, 0), txt, font=font)
    return bb[2] - bb[0]

# logo FP (desenhada a esquerda do nome/pilula)
LOGO_CANDIDATES = ["../assets/logos/marca-fp-lemon.png", "assets/logos/marca-fp-lemon.png", "marca-fp-lemon.png"]
logo_img = None
for _p in LOGO_CANDIDATES:
    try:
        logo_img = Image.open(_p).convert("RGBA"); break
    except Exception:
        continue

# barras lime topo/rodape
d.rectangle([0, 0, W, 14], fill=LIME)
d.rectangle([0, H - 14, W, H], fill=LIME)

# --- TOPO: identidade ---
y = 150
y = ctext(y, TITULO, fb(84), LIME, ls=42)

# --- LOCKUP: logo FP a esquerda + nome / cargo / pilula ---
nome_f, cargo_f, pf = fb(58), fr(36), fb(34)
colw = _tw(NOME, nome_f)
for linha in CARGO:
    colw = max(colw, _tw(linha, cargo_f))
pillw = _tw(PILL, pf) + 110
colw = max(colw, pillw)
logo_h = 150
logo_w = int(logo_h * logo_img.width / logo_img.height) if logo_img else 0
gap = 44
groupw = colw + (logo_w + gap if logo_img else 0)
groupx = (W - groupw) // 2
colcx = groupx + (logo_w + gap if logo_img else 0) + colw / 2

block_top = y
y = ctextx(colcx, y, NOME, nome_f, WHITE, ls=14)
for linha in CARGO:
    y = ctextx(colcx, y, linha, cargo_f, GRAY, ls=8)
y += 24
# pilula
px0 = int(colcx - pillw / 2)
d.rounded_rectangle([px0, y, px0 + pillw, y + 72], radius=36, fill=LIME)
d.text((px0 + 55, y + 16), PILL, font=pf, fill=BLACK)
y += 72
if logo_img:
    lr = logo_img.resize((logo_w, logo_h), Image.LANCZOS)
    ly = int((block_top + y) / 2 - logo_h / 2)
    img.paste(lr, (groupx, ly), lr)

# --- TERCO INFERIOR: QR ---
card = 506
cx = (W - card) // 2
cy = 1179
# instrucao logo acima do card (rodape do bloco ~30px acima do card)
lh = 52
block_h = len(INSTRUCAO) * lh
iy = cy - 30 - block_h
for linha in INSTRUCAO:
    ctext(iy, linha, fb(40), WHITE); iy += lh

# card branco + QR
d.rounded_rectangle([cx, cy, cx + card, cy + card], radius=46, fill=WHITE)
qs = card - 80
img.paste(qr_img.resize((qs, qs), Image.NEAREST), (cx + 40, cy + 40))

# cantos lime
t, th, off = 66, 12, 24
def corner(px, py, hx, hy):
    xs = sorted([px, px + hx * t]); ys = sorted([py, py + hy * th])
    d.rectangle([xs[0], ys[0], xs[1], ys[1]], fill=LIME)
    xs = sorted([px, px + hx * th]); ys = sorted([py, py + hy * t])
    d.rectangle([xs[0], ys[0], xs[1], ys[1]], fill=LIME)
corner(cx - off, cy - off, 1, 1)
corner(cx + card + off, cy - off, -1, 1)
corner(cx - off, cy + card + off, 1, -1)
corner(cx + card + off, cy + card + off, -1, -1)

# marca dagua vertical na lateral direita do card (fora do QR)
WATERMARK = "feito por @fredparreira.me"
wf = fb(44)
wbb = d.textbbox((0, 0), WATERMARK, font=wf)
wm = Image.new("RGBA", (wbb[2] - wbb[0] + 8, wbb[3] - wbb[1] + 8), (0, 0, 0, 0))
ImageDraw.Draw(wm).text((4 - wbb[0], 4 - wbb[1]), WATERMARK, font=wf, fill=(165, 165, 165, 140))
wm = wm.rotate(-90, expand=True)
img.paste(wm, (cx + card + 32, cy + (card - wm.height) // 2), wm)

# legenda
ctext(cy + card + 30, LEGENDA, fr(31), GRAY)

img.save(SAIDA, "PNG")
print("Salvo:", SAIDA)
