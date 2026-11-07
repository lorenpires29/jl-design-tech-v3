# Design System oficial V3 — herdado da branch v2

**Fonte de verdade visual:** branch `v2` do próprio repositório. **Não substituir pelo tema genérico dos protótipos preliminares em `docs/v3/modulos/*/prototipos`**. A V3 deve reutilizar os estilos e componentes da V2, refatorando apenas o necessário.

## Arquivos de referência na V2
- [Tokens de cor e espaçamento](../../../../blob/v2/static/css/tokens.css) — `static/css/tokens.css`
- `static/css/components.css` — componentes do site público.
- `static/css/admin-components.css` — formulários, tabelas, ações e estados vazios.
- `static/css/admin.css`, `static/css/app.css` — estrutura e layout.
- `static/css/navigation.css` — navegação e logo administrativa.
- `templates/base.html` — cabeçalho, navegação e rodapé públicos.
- `templates/superuser/base.html` — shell administrativo.
- `templates/components/admin_sidebar.html` — sidebar e links administrativos.
- `static/js/admin-menu.js` — comportamento do menu.

## Tokens reais extraídos da V2
| Token | Valor |
|---|---|
| `--bg` | `#080d22` |
| `--surface` | `#101936` |
| `--surface-raised` | `#162143` |
| `--border` | `#2b3960` |
| `--text` | `#f7f8ff` |
| `--text-muted` | `#a5b4d4` |
| `--primary` | `#a735f5` |
| `--primary-hover` | `#8f22df` |
| `--success` | `#32c99a` |
| `--warning` | `#ffbd59` |
| `--danger` | `#f05278` |
| `--radius-sm/md/lg` | `8px / 12px / 18px` |

**Botão primário V2:** gradiente `linear-gradient(90deg, #8322ed, #c936ff)`. **Fontes:** DM Sans e Space Grotesk. **Logo administrativa:** 50 × 50 px, `object-fit: contain`. **Inputs administrativos:** fundo `#0b1332`, borda `#3c4b78` e raio 8 px.

## Regras de reutilização
- Home: manter estrutura visual aprovada, hero e coleção, refinando sem redesign.
- Admin: sidebar fixa/recolhível, menu consistente, cards, tabelas, campos, feedback, modal de confirmação e toasts; conferir implementações mais recentes antes de extrair componentes.
- Criar `base_public.html`, `base_admin.html` e componentes compartilhados a partir das referências da V2, sem carregar templates Django internos personalizados.
- Manter acessibilidade, estados vazio/erro/carregando, responsividade e testes de regressão visual.
- Os HTMLs em `prototipos/` são **wireframes preliminares**: seus valores de cor não são normativos; atualizar as UIs para corresponder à V2 antes de aprovar ou implementar.

## Critério de aceitação
**DADO** um novo módulo V3, **QUANDO** sua UI for criada, **ENTÃO** deverá usar os tokens, tipografia, navegação e componentes da V2, com diferenças justificadas e aprovadas.
