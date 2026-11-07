# US-03-02-06 — Anexar Referencias Com Validacao

**Módulo:** Serviços e Orçamentos  
**Épico:** Solicitacoes De Orcamento  
**Status de implementação:** Código-base existente no módulo; aderência desta US ainda não homologada  
**Status da especificação:** Reformulada conforme template 1.0; **proposta sujeita a conferência com a US original e homologação**.  
**Referência original:** [Consultar requisitos históricos](https://github.com/lorenpires29/pedidos_jldesign/blob/e5cf82928c085349b23e4edbeedb93b4b7a5a8f1/docs/v3/modulos/03-servicos-orcamentos/epicos/02-solicitacoes-de-orcamento/US-03-02-06-anexar-referencias-com-validacao.md).

## Estória de usuário

**EU COMO:** visitante ou cliente da JL Design Tech.

**DESEJO:** anexar referencias com validacao, respeitando as permissões e as regras do módulo Serviços e Orçamentos.

**COM O OBJETIVO DE:** registrar informações válidas para utilização no sistema.

## Protótipo / referência de interface

**Protótipo de tela obrigatório — pendente:** preparar tela no design system escuro JL Design Tech V2/V3, com cabeçalho, breadcrumb, campos e estados vazio/carregando/erro/sucesso, modal de confirmação quando aplicável. Não há imagem de protótipo validada anexada a esta US.

**Título da tela:** Anexar Referencias Com Validacao.  
**Caminho de navegação (breadcrumb):** Site > Serviços > Orçamentos > Anexar Referencias Com Validacao.  
**Estados previstos:** inicial, sem resultados (quando aplicável), carregando, validação inválida, sucesso e falha.

## Especificação de campos

| Campo / label | Tipo | Preenchimento | Estado inicial | Origem, opções e validações |
|---|---|---|---|---|
| Nome / título | Texto | Obrigatório | Vazio | Máximo proposto 180 caracteres; não aceitar apenas espaços |
| Descrição | Texto longo | Condicionado | Vazio | Validar conteúdo e tamanho no formulário |
| Categoria / vínculo | Seleção única | Condicionado | Selecione | Carregar opções do banco e validar permissão |
| Ativo | Booleano | Opcional | Inativo | Publicar somente após validação |
| Serviço | Seleção única | Condicionado | Selecione | Origem: serviços ativos |
| Solicitante / contato | Texto | Condicionado | Vazio | Validar formato e obrigatoriedade conforme formulário |

**Visibilidade e seleção:** campos condicionados aparecem somente no contexto da operação; combos são de seleção única salvo especificação contrária. Campos de resultado são somente leitura. Valores únicos devem ser validados no banco quando o modelo exigir. As restrições de tamanho e arquivo ainda precisam ser confrontadas com o código e a US original antes da homologação.

## Regras de negócio e validações

- **Autorização:** somente perfis autorizados podem executar operações administrativas; usuários sem permissão não podem consultar ou alterar dados restritos.
- **Consistência:** verificar a existência do registro, os vínculos e os estados permitidos antes de executar a ação.
- **Persistência:** salvar somente dados validados; não persistir alterações ao cancelar.
- **Erros:** mostrar mensagem compreensível sem divulgar dados sensíveis ou detalhes internos. Em falhas, preservar o estado consistente do cadastro.
- **Rastreabilidade:** para operações administrativas relevantes, prever identificação do responsável e data/hora; confirmar se há auditoria efetivamente implementada.



## Botões e ações

**Salvar/Cadastrar** (ação prática; valida e persiste); **Cancelar** (link; retorna à listagem sem salvar).

**Navegação após sucesso:** voltar à consulta ou apresentar detalhe atualizado; preservar filtros quando aplicável.  
**Navegação após erro:** permanecer na operação, destacar o campo ou motivo da falha, sem perda indevida de dados.

## Critérios de aceitação

**Critério — Acesso e navegação**

**DADO** que o usuário possui o perfil exigido para a funcionalidade,  
**QUANDO** acessar Site > Serviços > Orçamentos,  
**ENTÃO** o sistema deve disponibilizar a ação **Anexar Referencias Com Validacao** com título, breadcrumb e controles correspondentes.  
**SE** não possuir permissão, **ENTÃO** deve impedir o acesso e a operação.

**Critério — Execução da funcionalidade**

**DADO** que os dados e pré-condições da funcionalidade são válidos,  
**QUANDO** o usuário solicitar **anexar referencias com validacao**,  
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
