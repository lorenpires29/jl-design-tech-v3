# Correção de estáticos — desenvolvimento e testes

Erro reproduzido por relato: `ValueError: Missing staticfiles manifest entry for 'css/site.css'` e HTTP 500 na home, causado pelo armazenamento com manifesto ativo sem `collectstatic`.

Em desenvolvimento, `DJANGO_DEBUG=True` é agora o padrão local e `StaticFilesStorage` dispensa manifesto. Em produção, definir obrigatoriamente `DJANGO_DEBUG=False`, `DJANGO_SECRET_KEY` forte e `DJANGO_ALLOWED_HOSTS`, e executar `python manage.py collectstatic --noinput` no build; `CompressedManifestStaticFilesStorage` permanece habilitado em produção.

Verificação local:

```powershell
python manage.py check
python manage.py test
python manage.py runserver
```

Se `DJANGO_DEBUG=False` estiver configurado na sessão do PowerShell, executar `$env:DJANGO_DEBUG='True'` para desenvolvimento. A mudança não altera nem apaga o banco de dados.

**Status:** correção aplicada no código; testes CI e validação visual ainda pendentes.
