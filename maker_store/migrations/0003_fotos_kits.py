from django.db import migrations,models

FOTOS={
 "kit-ferramentas-impressora-3d-9-pecas":(
  "Kit de Ferramentas para Impressora 3D 9 Peças – Acabamento, Remoção de Suportes e Manutenção de Impressora",
  "https://down-br.img.susercontent.com/file/br-11134207-820l9-mr7wb7c5gume41_tn.webp"
 ),
 "kit-ferramentas-impressora-3d-ate-60-pecas":(
  "Kit Ferramentas para Impressora 3D Até 60 Peças para Impressão 3D Rebarbação Limpeza e Acabamento",
  "https://down-br.img.susercontent.com/file/br-11134207-820l8-mt4z6tljzimda6_tn.webp"
 )
}
def vincular(apps,schema_editor):
 Produto=apps.get_model("maker_store","ProdutoAfiliado")
 for slug,(nome,foto) in FOTOS.items():
  Produto.objects.filter(slug=slug).update(nome=nome,imagem_externa=foto)

class Migration(migrations.Migration):
 dependencies=[("maker_store","0002_seed_vitrine")]
 operations=[
  migrations.AddField(model_name="produtoafiliado",name="imagem_externa",field=models.URLField(blank=True,help_text="URL HTTPS da foto original do parceiro",max_length=1000)),
  migrations.RunPython(vincular,migrations.RunPython.noop)
 ]
