# Pré-cadastro da vitrine Shopee / Collshp

Origem: duas capturas de tela enviadas pela proprietária, em 06/11/2026. Link da vitrine: https://collshp.com/lorenpires993?view=storefront

## Seis produtos distintos identificados
| Produto | Preço mostrado no print |
|---|---:|
| Kit de Ferramentas para Impressora 3D — 9 peças | R$ 39,90 |
| Kit de Ferramentas para Impressora 3D — até 60 peças | R$ 95,00 |
| Placa de aço com mola para impressora 3D | R$ 69,38 |
| Filamento PLA Silk SOL3D 1 kg 1,75 mm | R$ 94,05 |
| Filamento PLA Preto Velvet Premium 1 kg 1,75 mm | R$ 99,66 |
| Filamento MasterPrint 1 kg 1,75 mm (material exato a conferir) | R$ 69,90 |

Aparecem duas vezes nos prints o kit de até 60 peças e o filamento PLA Silk; foram deduplicados.

A migração `maker_store/migrations/0002_seed_vitrine.py` cria registros **idempotentes** e os publica na vitrine local após `python manage.py migrate`. Não sobrescreve produtos existentes com os mesmos slugs.

**Limitações importantes:** os nomes dos anúncios foram truncados nas capturas; os títulos foram normalizados e as descrições mantidas conservadoras. Os preços são históricos dos prints, não preços em tempo real. Os prints não revelam links individuais; por isso os seis produtos apontam para a vitrine geral, com aviso explícito na página de detalhes. As fotos individuais não foram extraídas/cadastradas; permanecem placeholders até obter imagens autorizadas. Não declarar importação automática ou sincronização Shopee.
