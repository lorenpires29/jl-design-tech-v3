# US-04-02-01 — Importar Produtos Validados Da Collshp

**Módulo:** Maker Store  
**Épico:** Curadoria Inicial  
**Status de implementação:** Código-base existente no módulo; aderência desta US ainda não homologada  
**Status da especificação:** Reformulada conforme template 1.0; **proposta sujeita a conferência com a US original e homologação**.  
**Referência original:** [Consultar requisitos históricos](https://github.com/lorenpires29/pedidos_jldesign/blob/e5cf82928c085349b23e4edbeedb93b4b7a5a8f1/docs/v3/modulos/04-maker-store/epicos/02-curadoria-inicial/US-04-02-01-importar-produtos-validados-da-collshp.md).

## Estória de usuário

**EU COMO:** visitante ou cliente da JL Design Tech.

**DESEJO:** importar produtos validados da collshp, respeitando as permissões e as regras do módulo Maker Store.

**COM O OBJETIVO DE:** executar a operação de forma segura, verificável e sem duplicidade.

## Protótipo / referência de interface

**Fluxo técnico / integração:** desenhar contrato de entrada, saída, estados e erros; protótipo visual dispensável somente se não houver interface.

**Título da tela:** Importar Produtos Validados Da Collshp.  
**Caminho de navegação (breadcrumb):** Site > Maker Store > Produto > Importar Produtos Validados Da Collshp.  
**Estados previstos:** inicial, sem resultados (quando aplicável), carregando, validação inválida, sucesso e falha.

## Especificação de campos

| Campo / label | Tipo | Preenchimento | Estado inicial | Origem, opções e validações |
|---|---|---|---|---|
| Origem / destino | Texto ou referência | Condicionado | Não definido | Validar existência, autorização e domínio quando URL |
| Identificador da operação | Texto | Condicionado | Gerado pelo sistema | Impedir processamento duplicado quando aplicável |
| Resultado | Situação | Somente leitura | Pendente | Registrar sucesso ou erro sem expor segredos |
| Parceiro | Seleção única | Condicionado | Selecione | Origem: Parceiro ativo |
| URL de destino | URL | Condicionado | Vazio | HTTPS e domínio autorizado; não pressupor URL individual |
| Status de revisão | Seleção única | Condicionado | Pendente | Pendente, aprovado ou rejeitado |
| Preço informativo | Número decimal | Opcional | Vazio | Não negativo; até 2 casas decimais |

**Visibilidade e seleção:** campos condicionados aparecem somente no contexto da operação; combos são de seleção única salvo especificação contrária. Campos de resultado são somente leitura. Valores únicos devem ser validados no banco quando o modelo exigir. As restrições de tamanho e arquivo ainda precisam ser confrontadas com o código e a US original antes da homologação.

## Regras de negócio e validações

- **Autorização:** somente perfis autorizados podem executar operações administrativas; usuários sem permissão não podem consultar ou alterar dados restritos.
- **Consistência:** verificar a existência do registro, os vínculos e os estados permitidos antes de executar a ação.
- **Persistência:** salvar somente dados validados; não persistir alterações ao cancelar.
- **Erros:** mostrar mensagem compreensível sem divulgar dados sensíveis ou detalhes internos. Em falhas, preservar o estado consistente do cadastro.
- **Rastreabilidade:** para operações administrativas relevantes, prever identificação do responsável e data/hora; confirmar se há auditoria efetivamente implementada.
- **Maker Store:** não exibir avisos promocionais sobre comissão nem a frase sobre abertura da vitrine geral nos detalhes públicos. URL da vitrine geral é provisória; não afirmar que se trata de link individual do produto.


## Botões e ações

**Executar/Validar** (ação prática; verifica permissão, entrada e idempotência quando aplicável); **Consultar resultado** (link; abre status); **Cancelar** (ação de tela, quando aplicável).

**Navegação após sucesso:** voltar à consulta ou apresentar detalhe atualizado; preservar filtros quando aplicável.  
**Navegação após erro:** permanecer na operação, destacar o campo ou motivo da falha, sem perda indevida de dados.

## Critérios de aceitação

**Critério — Acesso e navegação**

**DADO** que o usuário possui o perfil exigido para a funcionalidade,  
**QUANDO** acessar Site > Maker Store > Produto,  
**ENTÃO** o sistema deve disponibilizar a ação **Importar Produtos Validados Da Collshp** com título, breadcrumb e controles correspondentes.  
**SE** não possuir permissão, **ENTÃO** deve impedir o acesso e a operação.

**Critério — Execução da funcionalidade**

**DADO** que os dados e pré-condições da funcionalidade são válidos,  
**QUANDO** o usuário solicitar **importar produtos validados da collshp**,  
**ENTÃO** o sistema deve executar a operação uma única vez e refletir o estado atualizado.

**Critério — Dados inválidos e vínculos**

**DADO** que um campo obrigatório, referência, vínculo ou condição de negócio está inválido,  
**QUANDO** o usuário tentar concluir a operação,  
**ENTÃO** o sistema deve impedir a conclusão, apresentar mensagem objetiva e não persistir estado inconsistente.

**Critério — Cancelamento e integridade**

**DADO** que o usuário iniciou a operação,  
**QUANDO** acionar **Cancelar** antes de confirmar,  
**ENTÃO** o sistema não deve aplicar a alteração e deve retornar à tela anterior ou fechar o modal.

**Critério — Testabilidade e homologação**

**DADO** que a implementação esteja disponível no ambiente de teste,  
**QUANDO** forem executados cenários de sucesso, erro, permissão e regressão,  
**ENTÃO** os resultados devem corresponder aos critérios desta US e às regras históricas confirmadas.  
**E** o protótipo e a experiência visual devem ser homologados quando a US envolver interface.

> **Pontos de validação obrigatórios:** confrontar esta proposta com a referência original, definir valores e mensagens específicas, revisar protótipo e testar no ambiente real. A existência de código não significa aprovação desta US.
