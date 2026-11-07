# Módulo 10 — Primeira etapa técnica

Implementados modelos de pedido externo, itens e histórico de status, restrição única por loja/identificador externo, administração somente leitura, e serviço `conciliar_pedido` para importação explícita autorizada com transação atômica e atualização idempotente de status. Não são armazenados CPF, e-mail, telefone ou endereço de compradores.

**Não implementado:** conexão Shopee real, importador de arquivos com validação de origem, automação de atualização de status, detecção automática de divergências e telas V2 de consulta com filtros por período. Não há pedidos reais cadastrados por esta alteração. Os registros só aparecem quando uma integração autorizada ou importador confiável chamar o serviço.

Testes unitários criados; execução no CI pendente.
