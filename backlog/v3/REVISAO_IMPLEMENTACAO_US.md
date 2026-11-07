# Auditoria de implementação e regressão — 07/11/2026

## Critério de análise

Padrão do template 1.0: EU COMO / DESEJO / COM O OBJETIVO; protótipo obrigatório para tela; título, breadcrumb, campos com tipo, obrigatoriedade, estado, visibilidade e validação; regras de negócio; botões; critérios de aceitação por último. Evidência de código, teste automatizado e homologação visual são avaliações distintas.

## Achados confirmados no código

- **CI:** execução 42331700160 falhou em `python manage.py makemigrations --check --dry-run`; `python manage.py check` passou; os testes nem chegaram a executar. A origem exata do drift de migração ainda precisa ser apurada a partir do log detalhado do job.
- **Maker Store:** `maker_store/migrations/0002_seed_vitrine.py` cria parceiro `collshp` e categoria `filamentos`. O teste `maker_store/tests.py` tentava criá-los novamente, gerando colisão de unicidade. Ajustado para reutilizar registros existentes.
- **Admin de afiliados:** ações de aprovação e rejeição já estão presentes. Não há prova de que o conjunto completo de USs 08 esteja homologado.
- **Admin catálogo:** ações de publicação, filtros e gestão de anúncios já estão presentes. Ainda utiliza Django Admin, não a interface V2 customizada.
- **Shopee:** os seis produtos de vitrine possuem URLs da vitrine geral, não URLs individuais. Não há integração OAuth, sincronização de vendas nem importação automática implementadas.
- **Protótipos:** o backlog reformulado contém descrições e pendências, não protótipos visuais completos por US.

## Validação por módulo

| Módulo | Código encontrado | Situação da aderência às USs |
|---|---|---|
| 01 | Institucional | Requer conferência individual e homologação visual |
| 02 | Catálogo público | Requer testes de listagem, filtros, links e segurança |
| 03 | Serviços e orçamentos | Requer testes de formulário, anexos e permissões |
| 04 | Maker Store | Correção de fixture de testes; imagens e vitrine já cadastradas |
| 05 | Contas | Requer testes de acesso, recuperação de senha e envio real |
| 06 | Dashboard | Requer testes de autorização, métricas e UX |
| 07 | Admin Catálogo | Django Admin disponível; painel customizado pendente |
| 08 | Admin Afiliados | Django Admin disponível; painel customizado pendente |
| 09 | Integração Shopee | OAuth/sincronização pendentes; apenas links locais existentes |
| 10–12 | Backlog | Não homologados; verificar cada fluxo antes de marcar implementado |

## Próximos gates

- Resolver drift de migrações no CI e obter `makemigrations --check --dry-run` verde.
- Executar `python manage.py test` integralmente e corrigir falhas restantes.
- Confrontar USs reformuladas com referências históricas e especificar mensagens/limites exatos.
- Criar e validar protótipos para cada US de interface.
- Só então marcar uma US como validada/homologada.
