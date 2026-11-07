# Módulo 05 — Contas e Autenticação

**Implementado:** cadastro com e-mail único, login, logout POST, perfil autenticado, edição de dados, recuperação e redefinição de senha por token nativo do Django, autenticação de sessão e CSRF. Gestão de usuários, ativação/desativação, grupos e permissões via Django Admin. Histórico de ações administrativas consultável em LogEntry.

**Limites:** cadastro público cria apenas usuários comuns, sem staff ou superuser. E-mails de recuperação usam backend de console no desenvolvimento; configurar SMTP antes de produção. Exclusão de contas deve seguir política de retenção/LGPD; não há rotina de anonimização automatizada. Proteção contra força bruta/rate limiting ainda pendente antes de produção. O histórico LogEntry cobre ações pelo Admin, não todas as alterações feitas em outras interfaces.

**Rotas:** /conta/cadastro/, /conta/entrar/, /conta/sair/ (POST), /conta/perfil/, /conta/senha/recuperar/.

**Testes:** python manage.py test contas
