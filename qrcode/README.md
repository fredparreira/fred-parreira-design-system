# QR Code WhatsApp — Wallpaper de Evento (Fred Parreira)

Wallpaper vertical **1080×1920** com um QR Code que, ao ser escaneado, abre o WhatsApp da pessoa **já conversando com você**, com uma mensagem pronta contendo seus dados. Pensado para usar como **protetor de tela / papel de parede** em eventos de networking.

Este repositório entrega duas formas de gerar a imagem:

1. **`index.html`** — página geradora no navegador. Edite os textos, a mensagem e o número, veja o preview ao vivo e clique para **exportar o PNG**. Pode ser publicada no GitHub Pages.
2. **`build_qr.py`** — script Python que recria o mesmo wallpaper de forma programática (ideal para automação/CI).

---

## Como o QR funciona

O QR codifica um **link `wa.me`** (deep link oficial do WhatsApp):

```
https://wa.me/<NUMERO>?text=<MENSAGEM_URL_ENCODED>
```

- `<NUMERO>` = DDI + DDD + número, **somente dígitos** (ex.: `5534991775536`).
- `<MENSAGEM>` = texto pré-preenchido, **codificado em URL** (`encodeURIComponent` no JS / `urllib.parse.quote` no Python).
- Ao escanear, abre a conversa **com você**, com a mensagem digitada. A pessoa só toca em enviar — e você recebe o número dela. Ela fica com seus dados escritos no histórico.

> **Não é vCard.** O fluxo é abrir o WhatsApp, não a agenda. O contato é salvo quando a pessoa toca no seu nome dentro da conversa.

### Por que a mensagem é enxuta
Cada caractere entra no QR. Mensagens longas elevam a **versão** do QR (mais módulos, mais denso) e dificultam a leitura **de tela**. A mensagem padrão gera um QR **versão 17 (85×85 módulos)** com correção de erro **M**, que escaneia bem de tela de celular a curta distância.

---

## Especificação visual

| Item | Valor |
|---|---|
| Dimensões | 1080 × 1920 px (9:16) |
| Fundo | Preto `#000000` |
| Cor de destaque | Eletric Lime `#DCFF00` |
| Texto secundário | Cinza `#A5A5A5` |
| Card do QR | Branco `#FFFFFF`, cantos arredondados raio 46 |
| Fonte (marca) | **Exo 2** — Black 900 (título), Bold/ExtraBold (nome, instrução, pílula); fallback Arial/Liberation Sans |
| Barras lime | Topo e rodapé, 14 px de altura |

### Geometria dos elementos

| Elemento | Posição / tamanho |
|---|---|
| Título (`BORA CONECTAR?`) | y≈150, 84 px, peso 900, lime |
| Nome (`FRED PARREIRA`) | abaixo do título, 58 px, peso 800, branco |
| Cargo (linhas) | 36 px, regular, cinza, entrelinha ~46 px |
| Pílula (`in/...`) | retângulo lime, raio 36, altura 72, texto 34 px preto |
| Instrução (2 linhas) | 40 px, bold, branco, logo acima do card |
| Card do QR | 506 × 506 px, centralizado em x, **topo y=1179** (terço inferior, livre de notificações) |
| QR dentro do card | área `card−80`, com quiet zone de 4 módulos |
| Cantos lime (ticks) | comprimento 66, espessura 12, deslocamento 24 do card |
| Legenda | 31 px, regular, cinza, 30 px abaixo do card |

### Parâmetros do QR

| Parâmetro | Valor |
|---|---|
| Correção de erro | **M** (Medium, ~15%) |
| Quiet zone (borda) | 4 módulos |
| Cor dos módulos | Preto sobre branco (alto contraste) |
| Versão resultante (msg padrão) | 17 (85×85 módulos) |

---

## Rodando o script Python

```bash
pip install "qrcode[pil]" pillow
python build_qr.py
# gera: Fred_QR_WhatsApp_1080x1920.png
```

Edite o bloco **CONFIGURAÇÃO** no topo de `build_qr.py` para trocar número, mensagem e textos.

### Verificar se o QR está legível (opcional)

```bash
pip install zxing-cpp opencv-python-headless
python -c "import cv2, zxingcpp; r=zxingcpp.read_barcodes(cv2.imread('Fred_QR_WhatsApp_1080x1920.png')); print(r[0].text if r else 'NAO LEU')"
```

---

## Publicando a página no GitHub Pages

1. Suba `index.html` na raiz do repositório.
2. Settings → Pages → Branch `main` / `/root` → Save.
3. Acesse `https://<seu-usuario>.github.io/<repo>/`.

A página usa **Exo 2** (Google Fonts) e a biblioteca **qrcode-generator** via CDN, com fallback. Funciona em qualquer navegador moderno; o QR é desenhado em `<canvas>` e exportado como PNG localmente (nada é enviado a servidores).

---

## Dicas de uso no evento

- Deixe o **brilho da tela no máximo** e desligue o modo escuro/economia ao exibir o QR.
- O QR fica no **terço inferior** de propósito: o relógio e as notificações do topo não o cobrem.
- Teste escaneando com 2–3 celulares diferentes antes do evento.

---

## Estrutura do repositório

```
.
├── index.html      # página geradora (edita textos + exporta PNG)
├── build_qr.py     # gerador programático (Python)
└── README.md       # esta documentação
```

---

## Script `build_qr.py` (referência completa)

```python
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
    "\U0001F517 LinkedIn: linkedin.com/in/parreirafrederico\n\n"
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
    bb = d.textbbox((0, 0), txt, font=font)
    w = bb[2] - bb[0]
    d.text(((W - w) / 2, y), txt, font=font, fill=color)
    return y + (bb[3] - bb[1]) + ls

# barras lime topo/rodape
d.rectangle([0, 0, W, 14], fill=LIME)
d.rectangle([0, H - 14, W, H], fill=LIME)

# --- TOPO: identidade ---
y = 150
y = ctext(y, TITULO, fb(84), LIME, ls=42)
y = ctext(y, NOME, fb(58), WHITE, ls=14)
for linha in CARGO:
    y = ctext(y, linha, fr(36), GRAY, ls=8)
y += 24
# pilula LinkedIn
pf = fb(34)
bb = d.textbbox((0, 0), PILL, font=pf); pw = bb[2] - bb[0]
px0 = (W - (pw + 110)) // 2
d.rounded_rectangle([px0, y, px0 + pw + 110, y + 72], radius=36, fill=LIME)
d.text((px0 + 55, y + 16), PILL, font=pf, fill=BLACK)

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

# legenda
ctext(cy + card + 30, LEGENDA, fr(31), GRAY)

img.save(SAIDA, "PNG")
print("Salvo:", SAIDA)

```
