# Módulo 07 — Administração do Catálogo

Implementado sobre o Django Admin com persistência no banco já existente: CRUD de categorias, produtos e anúncios Shopee; listagem, pesquisa, filtros, paginação, detalhes e edição; prévia da imagem; publicação/despublicação e destaques em lote; validação de URLs Shopee no salvamento; contagem de anúncios e cliques; bloqueio de publicação em lote quando a categoria estiver inativa. Exclusão de categoria com produtos vinculados é impedida pela relação PROTECT.

Rotas: `/admin/catalogo/categoria/`, `/admin/catalogo/produto/`, `/admin/catalogo/anuncioshopee/`.

Testes escritos em `catalogo/tests_admin.py`. Execução e homologação visual pendentes. O cadastro via Django Admin não é ainda um painel administrativo customizado com componentes V2. A disponibilidade de anúncio e produto deve ser verificada em produção.
