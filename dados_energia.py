# -*- coding: utf-8 -*-
"""Dados e premissas. Os códigos [F1], [P1] etc. estão em DADOS_E_CALCULOS.md."""

PERIODO_ANOS = 25

# [F1] 849 R$/MWh sem tributos; [F2] ICMS 18,0% e PIS/Cofins 4,9% por dentro
TARIFA_SEM_TRIBUTOS = 0.849
ALIQUOTA_TRIBUTOS = 0.18 + 0.049
TARIFA_PADRAO = round(TARIFA_SEM_TRIBUTOS / (1 - ALIQUOTA_TRIBUTOS), 2)

# [F1] componente de distribuição, usado como aproximação do Fio B
FIO_B = 0.262
# [F3] percentual do Fio B não compensado a partir de 2028
PERCENTUAL_FIO_B = 0.90
# [P1] parcela da geração solar injetada na rede
FRACAO_INJETADA = 0.70
# [F4] custo de disponibilidade da ligação bifásica com três condutores
CONSUMO_MINIMO_KWH = 50

# [F5] média aproximada da irradiação global horizontal, em kWh/m².dia
IRRADIACAO = {
    "Sul": 4.57,
    "Sudeste": 5.05,
    "Nordeste": 5.46,
    "Centro-Oeste": 5.07,
    "Norte": 4.65,
}
# [P2] desempenho global do sistema fotovoltaico
TAXA_DESEMPENHO = 0.75
# [P3] perda anual de geração
DEGRADACAO_ANUAL = 0.005
# [F6] preço instalado por porte: (kWp, R$/Wp)
PRECO_FV = ((2, 3.62), (4, 2.84), (8, 2.31))
# [P10] menor sistema considerado no orçamento
PORTE_MINIMO_FV_KWP = 1.0
# [P4] manutenção anual e troca do inversor, como fração do investimento
MANUTENCAO_ANUAL_FV = 0.01
TROCA_INVERSOR_FV = 0.15

# [F7] fator médio do Sistema Interligado Nacional em 2023
FATOR_REDE_KG_KWH = 0.0385
# [F8] mediana do ciclo de vida da fotovoltaica em telhado
FATOR_FV_CICLO_KG_KWH = 0.041

# [F9] chuveiro de 4.500 W por 32 min/dia; [P5] 8 min por pessoa
KWH_BANHO_PESSOA_MES = 4.5 * (8 / 60) * 30
MINUTOS_BANHO_ATUAL = 8
MINUTOS_BANHO_META = 5

# [P6] dias de uso de ar-condicionado e ventilador por ano
DIAS_RESFRIAMENTO = {
    "Sul": 60,
    "Sudeste": 90,
    "Nordeste": 210,
    "Centro-Oeste": 150,
    "Norte": 240,
}

# [P7] aquecedor solar de água
AQUECEDOR_BASE = 3000
AQUECEDOR_POR_PESSOA = 1000
AQUECEDOR_FRACAO_SOLAR = 0.70
AQUECEDOR_VIDA_ANOS = 20

# [P8] medidas de eficiência
LED_PRECO = 15
LED_VIDA_ANOS = 10
INVERTER_REDUCAO = 0.35
INVERTER_PRECO = 3000
INVERTER_VIDA_ANOS = 12
GELADEIRA_REDUCAO = 0.25
GELADEIRA_PRECO = 3000
GELADEIRA_VIDA_ANOS = 12
ELETRONICOS_REDUCAO = 0.10
ELETRONICOS_PRECO = 60
ELETRONICOS_VIDA_ANOS = 5
COZINHA_REDUCAO = 0.10

AREAS = {
    "iluminacao": "Iluminação",
    "climatizacao": "Climatização",
    "aquecimento_agua": "Aquecimento de água",
    "refrigeracao": "Refrigeração",
    "eletronicos": "Eletrônicos",
    "cozinha_lavanderia": "Cozinha e lavanderia",
}

# chave: (nome, área, kWh/mês por unidade, origem)
APARELHOS = {
    "geladeira": ("Geladeira", "refrigeracao", 56.9, "F9"),
    "freezer": ("Freezer", "refrigeracao", 54.0, "F9"),
    "microondas": ("Micro-ondas", "cozinha_lavanderia", 14.0, "F9"),
    "airfryer": ("Air fryer", "cozinha_lavanderia", 6.8, "F9"),
    "televisao": ("Televisão", "eletronicos", 30.5, "F9"),
    "chuveiro": ("Chuveiro elétrico", "aquecimento_agua", 0.0, "F9"),
    "ar_condicionado": ("Ar-condicionado", "climatizacao", 142.3, "F9"),
    "ventilador": ("Ventilador", "climatizacao", 17.3, "F9"),
    "lampada_led": ("Lâmpada LED", "iluminacao", 1.35, "P9"),
    "lampada_fluorescente": ("Lâmpada fluorescente", "iluminacao", 2.3, "F9"),
    "lampada_incandescente": ("Lâmpada incandescente", "iluminacao", 9.0, "P9"),
    "computador": ("Computador de mesa", "eletronicos", 15.1, "F9"),
    "notebook": ("Notebook", "eletronicos", 7.5, "P9"),
    "roteador": ("Roteador de internet", "eletronicos", 7.2, "P9"),
    "lavadora_roupas": ("Máquina de lavar roupas", "cozinha_lavanderia", 1.8, "F9"),
    "lavadora_loucas": ("Lava-louças", "cozinha_lavanderia", 30.9, "F9"),
    "ferro": ("Ferro de passar", "cozinha_lavanderia", 7.2, "P9"),
    "forno": ("Forno elétrico", "cozinha_lavanderia", 15.0, "F9"),
    "cooktop": ("Fogão elétrico (cooktop)", "cozinha_lavanderia", 68.6, "F9"),
    "cafeteira": ("Cafeteira expresso", "cozinha_lavanderia", 23.8, "F9"),
    "panela_eletrica": ("Panela elétrica", "cozinha_lavanderia", 22.0, "F9"),
    "bomba_agua": ("Bomba d'água", "cozinha_lavanderia", 7.2, "F9"),
}
