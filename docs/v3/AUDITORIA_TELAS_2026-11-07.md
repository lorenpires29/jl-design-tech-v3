# Auditoria estática das telas — 07/11/2026

**Escopo:** 18 templates HTML, CSS principal, JS de navegação, rotas e views públicas, dashboard, autenticação, Maker Store e catálogo. Esta é uma **inspeção de código**, não um teste visual executado no navegador. Não marcar telas como homologadas.

## Inventário

| Tela/template | Verificação | Pendências ou observações |
|---|---|---|
| base.html | Header, menu responsivo, mensagens, footer | Menu público com vários destinos; conferir estados mobile, contraste e navegação por teclado |
| institucional/home.html | Hero, destaques e CTA | Hero promocional fixo de Natal; CTA “Solicitar orçamento” aponta para contato, não para formulário de orçamento |
| institucional/sobre.html | Conteúdo institucional | Homologar copy, espaçamento e mobile |
| institucional/contato.html | Formulário POST com CSRF e erros | Conferir feedback, persistência e acessibilidade |
| catalogo/lista.html | Busca, categorias, ordenação, paginação | Verificar URLs de filtro, vazio, imagens e mobile |
| catalogo/detalhe.html | Dados e links Shopee | Verificar destino, registro de clique, estados sem anúncio |
| components/product_card.html | Componente reutilizado | Conferir tamanhos de imagens e responsividade |
| servicos/lista.html | Busca e paginação | Conferir grid, conteúdo e empty state |
| servicos/detalhe.html | Conteúdo e CTA orçamento | Conferir vínculo do serviço selecionado |
| servicos/solicitar.html | Formulário POST, arquivo, erros | Validar tamanho, tipo real de anexo, limites e persistência |
| servicos/sucesso.html | Confirmação | Rota de sucesso é pública e não prova envio anterior |
| maker_store/vitrine.html | Busca, filtros, cards e paginação | Aviso público de comissão ainda presente; alinhar copy aprovada; verificar URLs externas das fotos |
| maker_store/detalhe.html | Foto, preço e botão | Se URL é vitrine geral, botão diz “Abrir vitrine Shopee”; links individuais ainda pendentes |
| contas/login.html | Login e reset | Validar redirect seguro, erros, acessibilidade e proteção contra abuso |
| contas/form.html | Cadastro, perfil e redefinição | Template genérico; conferir títulos, validação e regras por fluxo |
| contas/reset_enviado.html | Mensagem neutra | E-mail real não configurado por padrão |
| contas/reset_concluido.html | Confirmação e CTA | Homologar UX |
| dashboard/inicio.html | KPIs, filtro, sidebar e alertas | Links do menu não são condicionados às permissões individuais; sidebar existe só nesta tela; integração ainda descrita como não configurada mesmo após criação de modelos |

## Lacunas de telas

- Módulos 07 e 08: gestão pelo Django Admin, não pelo painel customizado V2.
- Módulos 09 e 10: apenas modelos/admin; faltam páginas personalizadas de conexões, sincronizações e pedidos.
- Módulos 11 e 12: sem templates próprios implementados.
- Nenhuma evidência de screenshots ou testes end-to-end cross-browser/mobile para as 18 telas.

## Qualidade / execução

- Último workflow verificado: https://github.com/lorenpires29/jl-design-tech-v3/actions/runs/42396160918 — **failure**.
- `config/settings.py` foi corrigido para staticfiles simples com DEBUG local, mas isso ainda não prova resolução integral dos testes.
- Não há comprovação de homologação das 118 USs contra protótipos e regras originais.

## Ordem recomendada

1. Corrigir CI e executar testes completos de views/templates/URLs, migrações e arquivos estáticos.
2. Corrigir inconsistências de navegação, permissões, CTA e textos.
3. Implementar layout administrativo V2 consistente em todas as telas de gestão.
4. Testar fluxos de formulário, arquivo, autenticação, status e persistência.
5. Capturar evidências visuais desktop/tablet/mobile e homologar por US.

**Resultado:** nenhuma tela deve ser marcada como “100% validada” somente com esta inspeção estática.
