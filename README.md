# Fred Parreira · Design System

> Design System oficial da marca pessoal Fred Parreira. Tokens, componentes CSS, assets visuais e documentação completa para construir materiais on-brand em qualquer plataforma.

[![Version](https://img.shields.io/badge/version-1.0.0-DCFF00?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-595959?style=flat-square)](LICENSE)

## O que está aqui

Este repositório é a **fonte única de verdade** da identidade Fred Parreira. Contém:

- **Design Tokens** (cores, tipografia, espaçamento) em JSON estruturado e CSS compilado
- **Componentes CSS** reutilizáveis (botões, cards, badges, tipografia)
- **Assets visuais** (14 logos PNG/JPG oficiais da designer)
- **Documentação** completa com brandbook interativo
- **Exemplos** prontos para copiar e adaptar (carrossel, post LinkedIn, slide de deck)

## Instalação

### Via clone do repositório

```bash
git clone https://github.com/SEU-USER/fred-parreira-design-system.git
cd fred-parreira-design-system
```

### Como CDN (uma vez publicado)

```html
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/gh/SEU-USER/fred-parreira-design-system/components/all.css">
```

### Como dependência local

```html
<link rel="stylesheet" href="path/to/fred-parreira-design-system/components/all.css">
```

## Uso rápido

### 1. Importe os tokens

Em qualquer arquivo CSS:

```css
@import url('tokens/tokens.css');

.minha-classe {
  background: var(--fp-primary);  /* Eletric Lime */
  color: var(--fp-dark);
  font-family: var(--fp-font-display);
  font-weight: var(--fp-weight-black);
}
```

### 2. Use os componentes prontos

```html
<!-- Importa tudo (tokens + componentes + Google Fonts) -->
<link rel="stylesheet" href="components/all.css">

<!-- Tipografia -->
<h1 class="fp-display-xl">Inovar não é sobre tecnologia.</h1>
<p class="fp-body">É sobre <span class="fp-highlight">gente</span>.</p>

<!-- Botões -->
<button class="fp-btn-cta">BORA COMEÇAR?</button>
<a href="#" class="fp-btn-outline">Saiba mais</a>

<!-- Cards -->
<div class="fp-card-quote">
  <p class="quote-text">"Se apaixone pelo problema, não pela solução."</p>
  <p class="quote-author">— Fred Parreira</p>
</div>

<!-- Number datapoint -->
<div class="fp-card-number">
  <span class="number">+R$20M</span>
  <p class="label">captados em fomento P&D</p>
  <p class="source">// Portugal 2030 + FAPEMIG</p>
</div>

<!-- Badges & pills -->
<span class="fp-badge fp-badge-lime">PALESTRA AO VIVO</span>
<span class="fp-pill fp-pill-lime">BORA!</span>
```

## Estrutura

```
fred-parreira-design-system/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── package.json
│
├── tokens/                ← Design Tokens
│   ├── colors.json        ← cores estruturadas (W3C Design Tokens format)
│   ├── typography.json    ← tipografia estruturada
│   ├── spacing.json       ← espaçamento e radius
│   └── tokens.css         ← variáveis CSS compiladas (--fp-*)
│
├── components/            ← Componentes CSS
│   ├── typography.css     ← .fp-display-*, .fp-body, .fp-quote
│   ├── buttons.css        ← .fp-btn-cta, .fp-btn-primary, .fp-btn-outline
│   ├── cards.css          ← .fp-card, .fp-card-quote, .fp-card-number
│   ├── badges.css         ← .fp-badge, .fp-pill
│   └── all.css            ← entry point (importa tudo)
│
├── assets/
│   └── logos/             ← 14 logos PNG/JPG oficiais da designer
│
├── docs/                  ← brandbook interativo (HTML)
│   └── index.html
│
└── examples/              ← HTML prontos para copiar
    ├── carrossel-capa.html
    ├── post-linkedin.html
    └── slide-deck.html
```

## Tokens principais

### Cores

| Token | Valor | Uso |
|---|---|---|
| `--fp-primary` | `#DCFF00` | Eletric Lime · CTAs, destaques, números-gigantes |
| `--fp-dark` | `#000000` | Preto puro · fundos premium, texto sobre fundo claro |
| `--fp-light` | `#FFFFFF` | Branco · fundos didáticos, texto sobre fundo escuro |
| `--fp-gray` | `#595959` | Cinza médio · texto secundário, divisores |
| `--fp-warm-light` | `#E7DCC5` | Off-white quente · alternativa suave |

Proporção sugerida: **60% neutros + 30% lime + 10% complementares**.

### Tipografia

- **Display:** `var(--fp-font-display)` → Exo 2 (Google Fonts)
- **Body:** `var(--fp-font-body)` → Brix, fallback Inter
- **Mono:** `var(--fp-font-mono)` → Courier New

Pesos canônicos:
- `--fp-weight-black: 900` → títulos maiores
- `--fp-weight-bold: 700` → subtítulos, CTAs
- `--fp-weight-regular: 400` → corpo
- `--fp-weight-light: 300` → legendas

## Logos · combinações aprovadas

Cada logo tem combinações de fundo aprovadas. Consulte `docs/index.html` (brandbook) para a tabela completa. Resumo:

| Logo | ★ Melhor sobre | Também funciona | Jamais |
|---|---|---|---|
| `marca-fp-lemon.png` | **Preto** | Branco · Cinza | Lemon · Off-white |
| `marca-fp-preto.png` | **Branco** | Lemon · Off-white | Preto · Cinza |
| `assinatura-lemon.png` | **Preto** | Cinza | Branco · Lemon · Off-white |
| `assinatura-preta.png` | **Branco** | Lemon (muito bom) · Off-white | Preto · Cinza |
| `marca-completa-lemon-branca.png` | **Preto** | Cinza | Branco · Lemon · Off-white |
| `marca-completa-lemon-preta.png` | **Branco** | Off-white | Preto · Cinza · Lemon |
| `marca-completa-preta-lemon.png` | **Branco** | Lemon · Off-white | Preto · Cinza |

## Documentação

A documentação completa está em `docs/index.html`. Abra direto no navegador para ver:

- Brandbook visual interativo
- Toggle de fundos para testar logos
- 32 mockups de aplicação (Carrossel, LinkedIn, Apresentações, Instagram)
- Regras de diagramação e linguagem visual
- Exportação em PDF do brandbook completo

## Princípios da marca

1. **Inovação não é sobre tecnologia. É sobre gente.** Tagline central.
2. **Contraste é a marca registrada visual.** Eletric Lime + Black puro.
3. **Uma ideia central por slide.** Espaço em branco é elemento ativo.
4. **Mineiridade acessível.** *"Bora"* sim, *"sinergia disruptiva"* jamais.
5. **Copiloto Criativo.** IA potencializa o humano, jamais substitui.

## Roadmap

- [ ] v1.1 — Mais variações de componentes (loaders, dividers, tooltips)
- [ ] v1.2 — Sub-temas (light/dark mode formal)
- [ ] v1.3 — React components (opcional)
- [ ] v2.0 — Integração com Figma via Style Dictionary

Veja [CHANGELOG.md](CHANGELOG.md) para histórico de versões.

## Contribuir

Este é um design system de marca pessoal. Sugestões e ajustes são bem-vindos via Issues. Pull Requests devem manter:
- Aderência aos tokens existentes (jamais introduzir cores fora da paleta)
- Documentação atualizada (README + docs/)
- Examples HTML que demonstrem o novo componente

## Licença

MIT — veja [LICENSE](LICENSE).

## Contato

**Fred Parreira** · CEO Neway InsurTech · M.Sc. em Inovação UFTM

- E-mail: parreira.frederico@gmail.com
- LinkedIn: [linkedin.com/in/parreirafrederico](https://linkedin.com/in/parreirafrederico)
- Instagram: [@fredparreira.me](https://instagram.com/fredparreira.me)
- Podcast: UberHub Podcast
