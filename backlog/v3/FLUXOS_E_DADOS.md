# Fluxos, fonte de verdade e arquitetura de dados

## Venda própria
Home/Produto → anúncio oficial Shopee → checkout Shopee → importação autorizada por API → pedido externo local (espelho) → relatório. O clique de saída não cria pedido nem prova conversão.

## Afiliados
Admin cria AffiliateProduct → ativo → Maker Store pública → clique externo registrado → parceiro. Cliques não são vendas confirmadas.

## Orçamentos
Serviço → solicitação validada/anexo → protocolo → análise administrativa → proposta → eventual negociação/compra via canal definido. Orçamento não é pedido pago.

## Shopee
OAuth/autorização conforme permissões disponíveis → guardar tokens no servidor → mapear shop_id, item_id/model_id → sincronização incremental → upsert único (shop_id, order_sn) → histórico de status → reconciliação e alertas. Webhook somente quando oficialmente disponível e com assinatura validada. Verificar documentação atual e elegibilidade antes de desenvolver endpoints.

## Dados sugeridos
CatalogProduct, Category, ProductImage, ShopeeListing, AffiliateProduct, OutboundClick, Service, QuoteRequest, QuoteAttachment, ShopeeShop, ExternalOrder, ExternalOrderItem, OrderStatusEvent, SyncRun, AuditEvent, UserRole.

## Segurança e qualidade
Tokens fora do Git e do frontend; isolamento de serviços; PostgreSQL em produção; jobs assíncronos; timeouts/retry; testes por módulo e E2E; backup antes de migração; observabilidade e controle de permissões.
