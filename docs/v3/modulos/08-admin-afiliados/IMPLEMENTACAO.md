# Módulo 08 — Administração de Afiliados

Implementado sobre o Django Admin com dados reais já existentes: CRUD de parceiros, categorias e ofertas; pesquisa e filtros; prévia da imagem original/local; URL HTTPS validada por domínio permitido; revisão pendente/aprovado/rejeitado; ações em lote para aprovar/publicar, rejeitar/despublicar, destacar; cliques registrados, pesquisáveis e somente leitura. O cadastro dos seis produtos da Collshp permanece intacto.

Rotas: `/admin/maker_store/parceiro/`, `/admin/maker_store/categoriaafiliado/`, `/admin/maker_store/produtoafiliado/`, `/admin/maker_store/cliqueafiliado/`.

Testes escritos em `maker_store/tests_admin.py`. Execução e homologação visual pendentes. A checagem de URL valida formato/domínio, **não** verifica se o anúncio remoto está disponível. Importação automática e links individuais Shopee ainda pendentes; os seis itens apontam à vitrine geral. O cadastro via Django Admin não é ainda um painel administrativo customizado com componentes V2.
