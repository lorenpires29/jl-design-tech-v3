from django.db import migrations

FOTOS={
 "placa-aco-mola-impressora-3d":(
  "Placa de aço com mola para mesa aquecida de impressora 3D — PEI + PE",
  "https://down-br.img.susercontent.com/file/sg-11134201-7rbko-lmo3bgl0m7h5c3_tn.webp"
 ),
 "filamento-pla-silk-sol3d-1kg":(
  "Filamento PLA Silk SOL3D 1 kg, 1,75 mm — brilho sedoso",
  "https://down-br.img.susercontent.com/file/br-11134207-820lr-mu1jzyp7uhoice_tn.webp"
 ),
 "filamento-pla-preto-velvet-premium-1kg":(
  "Filamento PLA Preto Velvet Premium Voolt3D 1 kg, 1,75 mm",
  "https://down-br.img.susercontent.com/file/br-11134207-820ld-ms2tczb1sb2c16_tn.webp"
 ),
 "filamento-masterprint-1kg-175mm":(
  "Filamento MasterPrint Premium PETG/PLA 1 kg, 1,75 mm — várias cores",
  "https://down-br.img.susercontent.com/file/br-11134207-820l6-mmt10la8o934cd_tn.webp"
 )
}
def vincular(apps,schema_editor):
 Produto=apps.get_model("maker_store","ProdutoAfiliado")
 for slug,(nome,foto) in FOTOS.items():
  Produto.objects.filter(slug=slug).update(nome=nome,imagem_externa=foto)

class Migration(migrations.Migration):
 dependencies=[("maker_store","0003_fotos_kits")]
 operations=[migrations.RunPython(vincular,migrations.RunPython.noop)]
