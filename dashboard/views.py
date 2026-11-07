from datetime import timedelta
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from institucional.models import MensagemContato
from catalogo.models import Produto,CliqueAnuncio
from servicos.models import SolicitacaoOrcamento
from maker_store.models import ProdutoAfiliado,CliqueAfiliado
from integracoes.models import ConexaoShopee,ExecucaoSincronizacao

@staff_member_required(login_url="login")
def inicio(request):
 periodo=request.GET.get("periodo","30")
 if periodo not in ("7","30","90"): periodo="30"
 desde=timezone.now()-timedelta(days=int(periodo))
 orcamentos=SolicitacaoOrcamento.objects.filter(criada_em__gte=desde)
 mensagens=MensagemContato.objects.filter(criada_em__gte=desde)
 conexoes=ConexaoShopee.objects.all()
 autorizadas=conexoes.filter(status="autorizada").count()
 falhas=ExecucaoSincronizacao.objects.filter(status="falha").count()
 dados={
  "periodo":periodo,
  "orcamentos":orcamentos.count(),
  "orcamentos_novos":orcamentos.filter(status="nova").count(),
  "mensagens":mensagens.count(),
  "mensagens_pendentes":mensagens.filter(lida=False).count(),
  "produtos_ativos":Produto.objects.filter(ativo=True).count(),
  "afiliados_ativos":ProdutoAfiliado.objects.filter(ativo=True,status_revisao="aprovado").count(),
  "cliques_shopee":CliqueAnuncio.objects.filter(criado_em__gte=desde).count(),
  "cliques_afiliados":CliqueAfiliado.objects.filter(criado_em__gte=desde).count(),
  "recentes":orcamentos.select_related("servico")[:8],
  "integracao_shopee":(f"{autorizadas} loja(s) autorizada(s); {conexoes.count()} conexão(ões) cadastrada(s)" if conexoes.exists() else "Não configurada — sem sincronização automática"),
  "alertas":[]
 }
 if dados["orcamentos_novos"]: dados["alertas"].append(f'{dados["orcamentos_novos"]} orçamento(s) aguardando análise')
 if falhas: dados["alertas"].append(f"{falhas} sincronização(ões) com falha")
 if dados["mensagens_pendentes"]: dados["alertas"].append(f'{dados["mensagens_pendentes"]} mensagem(ns) não lida(s)')
 return render(request,"dashboard/inicio.html",dados)
