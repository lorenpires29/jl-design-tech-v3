# Módulo 09 — Primeira etapa técnica

Implementados modelos e migrações de ConexaoShopee, VinculoAnuncio e ExecucaoSincronizacao, com administração restrita, estado inicial **não configurada**, unicidade de vínculo por loja/anúncio e histórico de execuções somente leitura.

**Não implementado:** autorização OAuth, callback, armazenamento seguro de tokens, renovação, revogação efetiva, consulta da API Shopee, sincronização agendada, retentativas e importação de arquivo. Não marcar US-09-01 ou US-09-03 como concluídas. O status "autorizada" não pode ser alterado manualmente pelo Django Admin para simular conexão. O vínculo ativo exige conexão autorizada.

Testes criados; execução no CI pendente. Não usar dados fictícios de venda.
