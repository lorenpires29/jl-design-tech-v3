# JL Design Tech V3

Novo projeto Django independente. Módulo 01 (Home, Sobre, Contato) e Módulo 02 (Catálogo, categorias, detalhes, pesquisa e links Shopee). Documentação do planejamento em [docs/v3](docs/v3/README.md).

## Rodar localmente

```bash
python -m venv .venv
pip install -r requirements.txt
# configure DJANGO_DEBUG=True e DJANGO_SECRET_KEY no ambiente
python manage.py migrate
python manage.py createsuperuser
python manage.py test
python manage.py runserver
```

O projeto não usa checkout interno. Imagens e produtos podem ser cadastrados pelo Django Admin. Testes incluídos, mas ainda não executados neste ambiente. A documentação histórica e protótipos originais podem ser encontrados no pacote de reconstrução.
