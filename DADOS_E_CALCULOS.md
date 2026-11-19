# Dados e cálculos

## Dados e fontes

| Código | Dado | Valor | Fonte |
|---|---|---|---|
| F1, F2 | Tarifa residencial sem tributos, distribuição e tributos | R$ 0,849/kWh, R$ 0,262/kWh e 22,9% | [ANEEL, InfoTarifas mar/2026](https://cenarioenergia.com.br/wp-content/uploads/2026/03/17032026_infoTARIFA_MAR_2026.pdf) |
| F3 | Fio B não compensado a partir de 2028 | 90% | [Lei 14.300/2022, resumo](https://canalsolar.com.br/tarifacao-fio-b-lei-14-300/) |
| F4 | Consumo mínimo cobrado, ligação bifásica | 50 kWh/mês | [REN ANEEL 1.000/2021, art. 291](https://www.legisweb.com.br/legislacao/?id=490988) |
| F5 | Irradiação solar aproximada, em kWh/m².dia | Sul 4,57; Sudeste 5,05; Centro-Oeste 5,07; Norte 4,65; Nordeste 5,46 | [Atlas Brasileiro de Energia Solar, INPE](https://labren.ccst.inpe.br/atlas_2017.html) |
| F6 | Preço do sistema solar instalado, 2025 | R$ 3,62/Wp (2 kWp); R$ 2,84/Wp (4 kWp); R$ 2,31/Wp (8 kWp) | [Greener, via pv magazine](http://www.pv-magazine-brasil.com/2025/09/30/com-queda-de-precos-sistemas-residenciais-ampliam-representatividade-em-gd-diz-greener/) |
| F7 | Emissão da rede elétrica, 2023 | 0,0385 kgCO2/kWh | [MCTI, via eixos](https://eixos.com.br/brasil-tem-menor-taxa-de-emissao-de-carbono-na-geracao-eletrica-em-onze-anos/) |
| F8 | Emissão da energia solar no ciclo de vida | 0,041 kgCO2e/kWh | [IPCC AR5 WGIII, Anexo III](https://www.ipcc.ch/report/ar5/wg3/) |
| F9 | Consumo típico dos aparelhos | Valores em `dados_energia.py` | [Procel, tabela publicada pela Enel](https://enel.com.br/content/dam/enel-br/enel_distribuicao/enel_distribuicao_goias/Folheto_DicasDeEconomia_Goias.pdf) |

## Premissas estimadas


| Código | Premissa | Valor |
|---|---|---|
| P1 | Energia solar enviada à rede | 70% |
| P2, P3 | Desempenho do sistema e perda anual | 75% e 0,5% |
| P4 | Manutenção solar e troca do inversor | 1% ao ano e 15% do investimento |
| P5 | Banho por pessoa | 8 minutos; meta de 5 minutos |
| P6 | Dias de resfriamento por ano | Sul 60; Sudeste 90; Centro-Oeste 150; Nordeste 210; Norte 240 |
| P7 | Aquecedor solar | R$ 3.000 + R$ 1.000 por pessoa; cobre 70%; dura 20 anos |
| P8 | Medidas de eficiência | LED: R$ 15 cada; inverter: R$ 3.000 e -35%; geladeira ou freezer: R$ 3.000 e -25%; eletrônicos: R$ 60 e -10%; cozinha e lavanderia: -10% |
| P9 | Potências sem dado na tabela F9 | LED 9 W; incandescente 60 W; notebook 50 W; roteador 10 W; ferro 600 W |
| P10 | Menor sistema solar orçado | 1 kWp |

## Cálculos

```text
Energia (kWh/mês) = potência (kW) x horas por dia x dias por mês
Tarifa com tributos = 0,849 / (1 - 0,229) = R$ 1,10/kWh
Chuveiro = 4,5 kW x (8/60 h) x 30 dias = 18 kWh por pessoa/mês
Geração solar por kWp/ano = irradiação x 365 x 0,75
Sistema solar (kWp) = (consumo mensal - 50) x 12 / geração por kWp
Valor do kWh solar = 1,10 - (0,70 x 0,90 x 0,262) = R$ 0,935
Retorno = investimento / economia anual
CO2 da rede = kWh por ano x 0,0385
```

## Exemplo

Família simulada no Sudeste, com 4 pessoas e **314,2 kWh/mês**: geladeira, chuveiro elétrico, 2 TVs, micro-ondas, air fryer, máquina de lavar, ferro, roteador, notebook, 12 lâmpadas fluorescentes, 4 ventiladores e 1 ar-condicionado.

Geração: 5,05 x 365 x 0,75 = 1.382 kWh/kWp ao ano. Sistema solar: (314,2 - 50) x 12 / 1.382 = **2,29 kWp**.

| Opção | Investimento | Custo em 25 anos | Economia | Retorno |
|---|---:|---:|---:|---:|
| Manter como está | R$ 0 | R$ 103.670 | - | - |
| Eficiência de baixo custo | R$ 240 | R$ 88.266 | R$ 15.403 | 0,4 ano |
| Energia solar | R$ 8.038 | R$ 45.114 | R$ 58.556 | 3,0 anos |
| Eficiência + solar | R$ 7.002 | R$ 40.860 | R$ 62.810 | 2,5 anos |
| Aquecedor solar | R$ 7.000 | R$ 95.788 | R$ 7.882 | 10,5 anos |

## Justificativas

- **Custo:** começar pela eficiência exige pouco dinheiro e dá retorno rápido. Eficiência + solar teve a maior economia no exemplo, mas pede investimento inicial.
- **Viabilidade:** a solar depende de imóvel próprio ou autorização, telhado sem sombra, estrutura adequada e aprovação da distribuidora.
- **Impacto ambiental:** consumir menos reduz emissões. Como a rede brasileira emite pouco, a solar ajuda mais na conta do que na redução média de CO2, e seus equipamentos exigem fabricação e descarte adequados.


