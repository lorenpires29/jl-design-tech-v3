# US-08-01-05 — Desativar Ou Excluir Oferta Afiliada

**Módulo:** Administração de Afiliados  
**Épico:** Crud De Ofertas Afiliadas  
**Status de implementação:** Código-base existente no módulo; aderência desta US ainda não homologada  
**Status da especificação:** Reformulada conforme template 1.0; **proposta sujeita a conferência com a US original e homologação**.  
**Referência original:** [Consultar requisitos históricos](https://github.com/lorenpires29/pedidos_jldesign/blob/e5cf82928c085349b23e4edbeedb93b4b7a5a8f1/docs/v3/modulos/08-admin-afiliados/epicos/01-crud-de-ofertas-afiliadas/US-08-01-05-desativar-ou-excluir-oferta-afiliada.md).

## Estória de usuário

**EU COMO:** administrador autorizado da JL Design Tech.

**DESEJO:** desativar ou excluir oferta afiliada, respeitando as permissões e as regras do módulo Administração de Afiliados.

**COM O OBJETIVO DE:** impedir que registros indevidos permaneçam disponíveis e manter a rastreabilidade.

## Protótipo / referência de interface

**Protótipo de tela obrigatório — pendente:** preparar tela no design system escuro JL Design Tech V2/V3, com cabeçalho, breadcrumb, campos e estados vazio/carregando/erro/sucesso, modal de confirmação quando aplicável. Não há imagem de protótipo validada anexada a esta US.

**Título da tela:** Desativar Ou Excluir Oferta Afiliada.  
**Caminho de navegação (breadcrumb):** Administração > Maker Store > Desativar Ou Excluir Oferta Afiliada.  
**Estados previstos:** inicial, sem resultados (quando aplicável), carregando, validação inválida, sucesso e falha.

## Especificação de campos

| Campo / label | Tipo | Preenchimento | Estado inicial | Origem, opções e validações |
|---|---|---|---|---|
| Registro | Identificador | Obrigatório | Registro selecionado | Deve existir e estar acessível |
| Confirmação | Booleano / modal | Obrigatório | Não confirmado | Exigir confirmação explícita |
| Motivo | Texto | Condicionado | Vazio | Exigir quando a regra de negócio definir; máximo proposto 500 caracteres |
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

**Excluir/Desativar/Cancelar** (ação prática; abre modal); **Confirmar** (ação prática; persiste alteração após validar vínculos); **Cancelar** (ação de tela; fecha modal sem alterar dados).

**Navegação após sucesso:** voltar à consulta ou apresentar detalhe atualizado; preservar filtros quando aplicável.  
**Navegação após erro:** permanecer na operação, destacar o campo ou motivo da falha, sem perda indevida de dados.

## Critérios de aceitação

**Critério — Acesso e navegação**

**DADO** que o usuário possui o perfil exigido para a funcionalidade,  
**QUANDO** acessar Administração > Maker Store,  
**ENTÃO** o sistema deve disponibilizar a ação **Desativar Ou Excluir Oferta Afiliada** com título, breadcrumb e controles correspondentes.  
**SE** não possuir permissão, **ENTÃO** deve impedir o acesso e a operação.

**Critério — Execução da funcionalidade**

**DADO** que os dados e pré-condições da funcionalidade são válidos,  
**QUANDO** o usuário solicitar **desativar ou excluir oferta afiliada**,  
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
