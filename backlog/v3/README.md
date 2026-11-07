# JL Design Tech V3 — Índice de implementação

Branch **v3**. A reconstrução é incremental: **não considerar protótipos como backend implementado**. A Home anterior é a referência aprovada; compras próprias finalizam na Shopee, mediante link válido; dados de pedidos somente por integração oficial autorizada.

## Padrão visual
- Home: preservar estrutura atual, hero “Nossa nova fase está no ar”, coleção, categorias e destaques.
- Admin: fundo azul-marinho quase preto, cards azul-escuro, roxo/magenta, sidebar fixa recolhível, logo 50×50, tabelas, toasts e confirmação de exclusão.
- Todos os protótipos são HTML estático, responsivo e sem dados reais.

## Índice de módulos
- [01-home-institucional — Home e institucional](./modulos/01-home-institucional/ESPECIFICACAO.md) (3 telas, 3 US e protótipos individuais)
- [02-catalogo — Catálogo próprio](./modulos/02-catalogo/ESPECIFICACAO.md) (3 telas, 3 US e protótipos individuais)
- [03-servicos-orcamentos — Serviços e orçamentos](./modulos/03-servicos-orcamentos/ESPECIFICACAO.md) (3 telas, 3 US e protótipos individuais)
- [04-maker-store — JL Maker Store](./modulos/04-maker-store/ESPECIFICACAO.md) (2 telas, 2 US e protótipos individuais)
- [05-contas — Contas e acesso](./modulos/05-contas/ESPECIFICACAO.md) (3 telas, 3 US e protótipos individuais)
- [06-dashboard — Dashboard administrativo](./modulos/06-dashboard/ESPECIFICACAO.md) (2 telas, 2 US e protótipos individuais)
- [07-admin-catalogo — Administração do catálogo](./modulos/07-admin-catalogo/ESPECIFICACAO.md) (3 telas, 3 US e protótipos individuais)
- [08-admin-afiliados — Administração de afiliados](./modulos/08-admin-afiliados/ESPECIFICACAO.md) (2 telas, 2 US e protótipos individuais)
- [09-integracao-shopee — Integração Shopee](./modulos/09-integracao-shopee/ESPECIFICACAO.md) (3 telas, 3 US e protótipos individuais)
- [10-pedidos-shopee — Pedidos externos](./modulos/10-pedidos-shopee/ESPECIFICACAO.md) (2 telas, 2 US e protótipos individuais)
- [11-relatorios — Relatórios](./modulos/11-relatorios/ESPECIFICACAO.md) (2 telas, 2 US e protótipos individuais)
- [12-configuracoes — Configurações e auditoria](./modulos/12-configuracoes/ESPECIFICACAO.md) (2 telas, 2 US e protótipos individuais)

## Ordem sugerida
Base e autenticação → Home e catálogo → Maker Store e orçamentos → painel administrativo → integração Shopee → pedidos → relatórios → testes E2E e deploy.

## Critério geral de pronto
Cada US precisa de teste de renderização, permissões, persistência, fluxo principal, erro, estado vazio, responsividade e revisão visual. Não considerar clique como venda; não marcar pagamento sem dado oficial Shopee.
