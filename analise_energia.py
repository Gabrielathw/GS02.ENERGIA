# -*- coding: utf-8 -*-
import dados_energia as d


def brl(valor):
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def num(valor, casas=1):
    return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def geracao_kwp_ano(regiao):
    return d.IRRADIACAO[regiao] * 365 * d.TAXA_DESEMPENHO


def preco_wp(kwp):
    pontos = d.PRECO_FV
    if kwp <= pontos[0][0]:
        return pontos[0][1]
    for (x0, y0), (x1, y1) in zip(pontos, pontos[1:]):
        if kwp <= x1:
            return y0 + (y1 - y0) * (kwp - x0) / (x1 - x0)
    return pontos[-1][1]


def valor_kwh_solar(tarifa):
    perda = d.FRACAO_INJETADA * d.PERCENTUAL_FIO_B * d.FIO_B
    return max(0.0, tarifa - perda)


def fator_degradacao():
    return sum((1 - d.DEGRADACAO_ANUAL) ** ano for ano in range(d.PERIODO_ANOS))


def _opcao(nome, tipo, kwh_mes_rede, investimento, custo_periodo, custo_base, descricao, kwh_base, economia_operacao):
    economia_periodo = custo_base - custo_periodo
    economia_ano = economia_periodo / d.PERIODO_ANOS
    retorno = None
    if economia_periodo > 0 and economia_operacao > 0:
        retorno = investimento / (economia_operacao / d.PERIODO_ANOS)
    return {
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "kwh_mes": kwh_mes_rede,
        "investimento": investimento,
        "custo_periodo": custo_periodo,
        "economia_periodo": economia_periodo,
        "economia_mes": economia_ano / 12,
        "retorno_anos": retorno,
        "co2_ano": kwh_mes_rede * 12 * d.FATOR_REDE_KG_KWH,
        "co2_evitado_ano": (kwh_base - kwh_mes_rede) * 12 * d.FATOR_REDE_KG_KWH,
    }


class AnaliseEnergia:
    def __init__(self, perfil):
        self.perfil = perfil
        self.areas = perfil.por_area()
        self.total = perfil.total
        self.tarifa = perfil.tarifa
        self.geracao_kwp = geracao_kwp_ano(perfil.regiao)
        self.kwh_compensavel = max(0.0, self.total - d.CONSUMO_MINIMO_KWH)
        self.kwp_casa = self.kwh_compensavel * 12 / self.geracao_kwp

    def _custo_rede(self, kwh_mes):
        return kwh_mes * 12 * self.tarifa * d.PERIODO_ANOS

    def _custo_conta(self, kwh_mes):
        return self._custo_rede(max(kwh_mes, d.CONSUMO_MINIMO_KWH))

    def _fv(self, kwh_mes, mult_preco=1.0, mult_geracao=1.0):
        kwp = kwh_mes * 12 / self.geracao_kwp
        porte_cobrado = max(kwp, d.PORTE_MINIMO_FV_KWP)
        investimento = porte_cobrado * 1000 * preco_wp(porte_cobrado) * mult_preco
        energia = kwh_mes * 12 * fator_degradacao() * mult_geracao
        economia = energia * valor_kwh_solar(self.tarifa)
        extras = investimento * (
            d.TROCA_INVERSOR_FV + d.MANUTENCAO_ANUAL_FV * d.PERIODO_ANOS
        )
        return kwp, investimento, economia, extras

    def _eficiencia_area(self, area):
        kwh = self.areas[area]
        itens = self.perfil.itens
        fator = self.perfil.fator
        if kwh <= 0:
            return None
        if area == "iluminacao":
            trocar = itens.get("lampada_fluorescente", 0) + itens.get("lampada_incandescente", 0)
            if not trocar:
                return None
            lampadas = trocar + itens.get("lampada_led", 0)
            novo = lampadas * d.APARELHOS["lampada_led"][2] * fator
            return "Trocar lâmpadas por LED", novo, trocar * d.LED_PRECO, d.LED_VIDA_ANOS
        if area == "climatizacao":
            qtd = itens.get("ar_condicionado", 0)
            if not qtd:
                return None
            reducao = self.perfil.kwh_item("ar_condicionado") * d.INVERTER_REDUCAO
            return "Trocar por ar-condicionado inverter", kwh - reducao, qtd * d.INVERTER_PRECO, d.INVERTER_VIDA_ANOS
        if area == "aquecimento_agua":
            novo = kwh * d.MINUTOS_BANHO_META / d.MINUTOS_BANHO_ATUAL
            return f"Reduzir o banho para {d.MINUTOS_BANHO_META} minutos", novo, 0, d.PERIODO_ANOS
        if area == "refrigeracao":
            qtd = itens.get("geladeira", 0) + itens.get("freezer", 0)
            novo = kwh * (1 - d.GELADEIRA_REDUCAO)
            return "Trocar por modelo mais eficiente", novo, qtd * d.GELADEIRA_PRECO, d.GELADEIRA_VIDA_ANOS
        if area == "eletronicos":
            novo = kwh * (1 - d.ELETRONICOS_REDUCAO)
            return "Desligar da tomada com filtro de linha", novo, d.ELETRONICOS_PRECO, d.ELETRONICOS_VIDA_ANOS
        novo = kwh * (1 - d.COZINHA_REDUCAO)
        return "Usar com carga cheia e menos tempo ligado", novo, 0, d.PERIODO_ANOS

    def comparar_area(self, area):
        kwh = self.areas[area]
        if kwh <= 0:
            return []
        base = self._custo_rede(kwh)
        opcoes = [_opcao("Manter como está", "atual", kwh, 0, base, base, "Situação atual", kwh, 0)]

        efic = self._eficiencia_area(area)
        if efic:
            nome, novo, inv, vida = efic
            custo = self._custo_rede(novo) + inv * d.PERIODO_ANOS / vida
            operacao = base - self._custo_rede(novo)
            opcoes.append(_opcao(nome, "eficiencia", novo, inv, custo, base, "Reduz o consumo do uso atual", kwh, operacao))

        if area == "aquecimento_agua":
            inv = d.AQUECEDOR_BASE + d.AQUECEDOR_POR_PESSOA * self.perfil.pessoas
            novo = kwh * (1 - d.AQUECEDOR_FRACAO_SOLAR)
            custo = self._custo_rede(novo) + inv * d.PERIODO_ANOS / d.AQUECEDOR_VIDA_ANOS
            operacao = base - self._custo_rede(novo)
            opcoes.append(_opcao("Aquecedor solar de água", "renovavel", novo, inv, custo, base, "Fonte renovável: solar térmica", kwh, operacao))
        else:
            kwp = kwh * 12 / self.geracao_kwp
            porte_casa = max(self.kwp_casa, kwp, d.PORTE_MINIMO_FV_KWP)
            inv = kwp * 1000 * preco_wp(porte_casa)
            energia = kwh * 12 * fator_degradacao()
            extras = inv * (d.TROCA_INVERSOR_FV + d.MANUTENCAO_ANUAL_FV * d.PERIODO_ANOS)
            economia = energia * valor_kwh_solar(self.tarifa)
            custo = base - economia + inv + extras
            opcoes.append(_opcao("Parcela de energia solar", "renovavel", 0.0, inv, custo, base, "Fonte renovável: parte de um sistema da casa", kwh, economia - extras))
        return opcoes

    def melhor_area(self, area):
        candidatas = [
            o for o in self.comparar_area(area)
            if o["tipo"] != "atual" and o["economia_periodo"] > 0
        ]
        if not candidatas:
            return None
        return min(candidatas, key=lambda o: (o["retorno_anos"], -o["economia_periodo"]))

    def _medidas_baixo_custo(self):
        medidas = []
        for area in d.AREAS:
            for opcao in self.comparar_area(area):
                if opcao["tipo"] != "eficiencia" or opcao["economia_periodo"] <= 0:
                    continue
                if opcao["retorno_anos"] <= 3:
                    medidas.append((area, opcao))
        return medidas

    def plano_casa(self):
        base = self._custo_conta(self.total)
        opcoes = [_opcao("Manter como está", "atual", self.total, 0, base, base, "Situação atual", self.total, 0)]

        medidas = self._medidas_baixo_custo()
        kwh_efic = self.total - sum(self.areas[a] - o["kwh_mes"] for a, o in medidas)
        inv_efic = sum(o["investimento"] for _, o in medidas)
        custo_inv = sum(o["custo_periodo"] - self._custo_rede(o["kwh_mes"]) for _, o in medidas)
        if medidas:
            opcoes.append(_opcao(
                "Eficiência de baixo custo", "eficiencia", kwh_efic, inv_efic,
                self._custo_conta(kwh_efic) + custo_inv, base,
                "; ".join(o["nome"] for _, o in medidas), self.total,
                base - self._custo_conta(kwh_efic),
            ))

        if self.kwh_compensavel > 0:
            opcoes.append(self._opcao_solar("Energia solar fotovoltaica", self.total, 0, 0, base))
            if medidas and kwh_efic > d.CONSUMO_MINIMO_KWH:
                opcoes.append(self._opcao_solar("Eficiência + energia solar", kwh_efic, inv_efic, custo_inv, base))

        if self.areas["aquecimento_agua"] > 0:
            inv = d.AQUECEDOR_BASE + d.AQUECEDOR_POR_PESSOA * self.perfil.pessoas
            novo = self.total - self.areas["aquecimento_agua"] * d.AQUECEDOR_FRACAO_SOLAR
            custo = self._custo_conta(novo) + inv * d.PERIODO_ANOS / d.AQUECEDOR_VIDA_ANOS
            operacao = base - self._custo_conta(novo)
            opcoes.append(_opcao("Aquecedor solar de água", "renovavel", novo, inv, custo, base, "Reduz o uso do chuveiro elétrico", self.total, operacao))
        return opcoes

    def _opcao_solar(self, nome, kwh_inicial, inv_extra, custo_extra, base):
        compensar = max(0.0, kwh_inicial - d.CONSUMO_MINIMO_KWH)
        kwp, inv, economia, extras = self._fv(compensar)
        custo = self._custo_conta(kwh_inicial) - economia + inv + extras + custo_extra
        descricao = f"Sistema de {num(kwp, 2)} kWp"
        operacao = base - self._custo_conta(kwh_inicial) + economia - extras
        opcao = _opcao(nome, "renovavel", min(kwh_inicial, d.CONSUMO_MINIMO_KWH), inv + inv_extra, custo, base, descricao, self.total, operacao)
        opcao["kwp"] = kwp
        opcao["geracao_ciclo_co2_ano"] = compensar * 12 * d.FATOR_FV_CICLO_KG_KWH
        return opcao

    def retorno_solar_conservador(self):
        if self.kwh_compensavel <= 0:
            return None
        _, inv, economia, extras = self._fv(self.kwh_compensavel, 1.30, 0.85)
        anual = (economia - extras) / d.PERIODO_ANOS
        return inv / anual if anual > 0 else None

    def recomendacao(self):
        opcoes = self.plano_casa()
        primeira = next((o for o in opcoes if o["tipo"] == "eficiencia"), None)
        viaveis = [
            o for o in opcoes
            if o["tipo"] == "renovavel"
            and o["economia_periodo"] > 0
            and o["retorno_anos"] is not None
            and o["retorno_anos"] <= 10
            and o.get("kwp", 1) >= 1
        ]
        investimento = max(viaveis, key=lambda o: o["economia_periodo"]) if viaveis else None
        return primeira, investimento
