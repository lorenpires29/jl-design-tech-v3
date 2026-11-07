# Implementação do Módulo 03 — Serviços e Orçamentos

**Código implementado:** serviços publicados e pesquisáveis, página de detalhes, formulário público de solicitação, vínculo a serviço ativo, validação de campos e prazo, upload de PDF/PNG/JPG até 5 MB com checagem de assinatura, persistência, feedback de sucesso, gestão via Django Admin, status, notas internas e arquivamento sem exclusão.

**Rotas:** `/servicos/`, `/servicos/<slug>/`, `/orcamento/solicitar/`, `/orcamento/recebido/`, `/admin/`.

**Testes:** `python manage.py test servicos` — execução no GitHub Actions pendente de confirmação.

**Limites:** envio de e-mail, precificação automática, geração de PDF comercial, múltiplos anexos, antivírus e armazenamento privado não implementados. O arquivo de referência deve ser tratado como dado sensível; antes de deploy público, usar armazenamento privado com controle de acesso, limite de upload no proxy e varredura antimalware. No desenvolvimento local o acesso ao arquivo usa MEDIA_URL. Não publicar o módulo de anexos em produção sem essas proteções.
