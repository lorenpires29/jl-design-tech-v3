from decimal import Decimal
from django.db import migrations

VITRINE="https://collshp.com/lorenpires993?view=storefront"
PRODUTOS=[
 ("kit-ferramentas-impressora-3d-9-pecas","Kit de Ferramentas para Impressora 3D — 9 peças","ferramentas","Ferramentas para impressão 3D, conjunto de 9 peças exibido na vitrine.", "39.90"),
 ("kit-ferramentas-impressora-3d-ate-60-pecas","Kit de Ferramentas para Impressora 3D — até 60 peças","ferramentas","Kit de ferramentas para impressão 3D, anunciado na vitrine como conjunto de até 60 peças.", "95.00"),
 ("placa-aco-mola-impressora-3d","Placa de Aço com Mola para Impressora 3D","acessorios","Placa de aço com mola para impressão 3D. Verifique compatibilidade e dimensões com o vendedor.", "69.38"),
 ("filamento-pla-silk-sol3d-1kg","Filamento PLA Silk SOL3D — 1 kg, 1,75 mm","filamentos","Filamento PLA Silk SOL3D, 1 kg, diâmetro 1,75 mm, acabamento sedoso; cores variáveis.", "94.05"),
 ("filamento-pla-preto-velvet-premium-1kg","Filamento PLA Preto Velvet Premium — 1 kg, 1,75 mm","filamentos","Filamento PLA Preto Velvet Premium, 1 kg, diâmetro 1,75 mm.", "99.66"),
 ("filamento-masterprint-1kg-175mm","Filamento MasterPrint — 1 kg, 1,75 mm","filamentos","Filamento MasterPrint, 1 kg, 1,75 mm. O anúncio exibido menciona PETG/PLA; confirme o material exato na loja parceira.", "69.90"),
]

def criar(apps,schema_editor):
 Parceiro=apps.get_model("maker_store","Parceiro")
 Categoria=apps.get_model("maker_store","CategoriaAfiliado")
 Produto=apps.get_model("maker_store","ProdutoAfiliado")
 parceiro,_=Parceiro.objects.get_or_create(slug="collshp",defaults={"nome":"Vitrine Shopee / Collshp","ativo":True})
 nomes={"ferramentas":"Ferramentas de impressão 3D","acessorios":"Acessórios de impressão 3D","filamentos":"Filamentos 3D"}
 categorias={}
 for slug,nome in nomes.items():
  categorias[slug],_=Categoria.objects.get_or_create(slug=slug,defaults={"nome":nome,"ativa":True})
 for slug,nome,categoria,descricao,preco in PRODUTOS:
  Produto.objects.get_or_create(slug=slug,defaults={
   "parceiro":parceiro,"categoria":categorias[categoria],"nome":nome,"descricao":descricao,
   "url_destino":VITRINE,"preco_informativo":Decimal(preco),
   "status_revisao":"aprovado","ativo":True,"destaque":False
  })

class Migration(migrations.Migration):
 dependencies=[("maker_store","0001_initial")]
 operations=[migrations.RunPython(criar,migrations.RunPython.noop)]
