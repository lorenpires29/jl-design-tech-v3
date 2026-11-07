# Módulo 06 — Dashboard Administrativo

**Implementado:** painel restrito a staff, cartões com contagens reais de mensagens, orçamentos, cliques e produtos, filtro de período 7/30/90 dias para métricas temporais, alertas de pendências locais, lista de orçamentos recentes, navegação administrativa e menu lateral fixo recolhível. Paleta oficial V2 preservada.

**Integração Shopee:** status apresentado explicitamente como não configurado; não inventa horário de sincronização nem vendas. Cliques externos não são receita.

**Limites:** o painel usa permissão staff global e o Django Admin para operações. Controle de acesso granular por módulo, persistência de preferência do menu e dados de sincronização externa ficam pendentes. Homologação visual e CI pendentes.

**Rotas:** /painel/. **Testes:** python manage.py test dashboard
