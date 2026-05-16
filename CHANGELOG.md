# Changelog

Todas as mudancas relevantes deste design system serao documentadas aqui.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-13

### Adicionado
- Estrutura inicial do design system Fred Parreira
- **Tokens**: colors.json, typography.json, spacing.json, tokens.css com 20+ variaveis CSS canonicas
- **Componentes CSS**:
  - typography.css (display, body, mono, quote, bignumber, highlights)
  - buttons.css (cta, primary, dark, outline, ghost)
  - cards.css (card, card-quote, card-number, mockups carrossel/square/deck/story/banner-li)
  - badges.css (badge, pill em variacoes lime/dark/outline)
  - all.css (entry point com Google Fonts Exo 2 + Inter)
- **Assets**: 14 logos PNG/JPG oficiais (FP monogram, wordmark, lockup, objetos inteligentes, foto, capa LinkedIn)
- **Docs**: brandbook.html interativo com toggles de fundo, exportacao PDF, e 32 mockups
- **Examples**: carrossel-capa.html, post-linkedin.html, slide-deck.html
- Tipografia: Exo 2 (Black 900 / Bold 700) + Brix (com fallback Inter) + Courier
- Paleta: 4 cores primarias (Eletric Lime + Black + White + Gray) + 6 complementares
- Tabela canonica de combinacoes de fundo aprovadas por logo

### Combinacoes de fundo aprovadas (oficial)
- `marca-fp-lemon.png` -> Preto (melhor) | Branco | Cinza
- `marca-fp-preto.png` -> Branco (melhor) | Lemon | Off-white
- `assinatura-lemon.png` -> Preto (melhor) | Cinza
- `assinatura-preta.png` -> Branco (melhor) | Lemon (muito bom) | Off-white
- `marca-completa-lemon-branca.png` -> Preto (melhor) | Cinza
- `marca-completa-lemon-preta.png` -> Branco (melhor) | Off-white
- `marca-completa-preta-lemon.png` -> Branco (melhor) | Lemon | Off-white

### Origem
- Migrado da skill `idvisual-fred-parreira` v1.0
- Estruturado seguindo padrao W3C Design Tokens Community Group format
