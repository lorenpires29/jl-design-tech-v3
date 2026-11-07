# Módulo 04 — Maker Store: implementação inicial

## Entregue
- Vitrine pública responsiva, busca, filtros por categoria e parceiro, paginação, página de oferta e aviso claro de afiliação.
- Redirecionamento para links HTTPS de domínios parceiros permitidos, com contagem de cliques independente de vendas.
- Curadoria via Django Admin: parceiros, categorias, produtos, status pendente/aprovado/rejeitado, publicação e destaque. Produtos não aprovados não podem ser publicados.
- Testes automatizados escritos em `maker_store/tests.py`.

## Pendências para completar o épico de curadoria
- Importação automática da Collshp não está implementada: a plataforma não disponibilizou nesta implementação uma API verificada. O cadastro e revisão são manuais no Django Admin; não foi feita importação fictícia.
- Revisão de direitos de uso das imagens, verificação de disponibilidade/preços em tempo real e testes E2E em navegador.
- A origem de cada imagem deve ser verificada manualmente antes de publicar.

## Endereços
- `/maker-store/` — vitrine
- `/maker-store/<slug>/` — detalhes
- `/admin/maker_store/` — gestão

## Execução
`python manage.py migrate` e `python manage.py test maker_store`.
