# -*- coding: utf-8 -*-
from dados_energia import (
    APARELHOS,
    AREAS,
    DIAS_RESFRIAMENTO,
    KWH_BANHO_PESSOA_MES,
    TARIFA_PADRAO,
)


class PerfilConsumo:
    def __init__(self, pessoas, regiao, itens, modo, tarifa=TARIFA_PADRAO, total_conta=None):
        self.pessoas = pessoas
        self.regiao = regiao
        self.itens = {chave: qtd for chave, qtd in itens.items() if qtd > 0}
        self.modo = modo
        self.tarifa = tarifa
        soma = sum(self._kwh_sem_ajuste(c, q) for c, q in self.itens.items())
        self.fator = total_conta / soma if total_conta else 1.0

    def _kwh_sem_ajuste(self, chave, quantidade):
        if chave == "chuveiro":
            return KWH_BANHO_PESSOA_MES * self.pessoas
        _, area, kwh, _ = APARELHOS[chave]
        if area == "climatizacao":
            kwh *= DIAS_RESFRIAMENTO[self.regiao] / 365
        return kwh * quantidade

    def kwh_item(self, chave):
        return self._kwh_sem_ajuste(chave, self.itens[chave]) * self.fator

    def por_area(self):
        areas = {area: 0.0 for area in AREAS}
        for chave in self.itens:
            areas[APARELHOS[chave][1]] += self.kwh_item(chave)
        return areas

    @property
    def total(self):
        return sum(self.por_area().values())


def _itens_tipicos(pessoas):
    area_m2 = 20 + 25 * pessoas
    comodos = max(2, round(area_m2 / 20))
    return {
        "geladeira": 1,
        "chuveiro": 1,
        "televisao": 1 if pessoas < 4 else 2,
        "microondas": 1,
        "airfryer": 1,
        "lavadora_roupas": 1,
        "ferro": 1,
        "roteador": 1,
        "notebook": 1,
        "lampada_fluorescente": max(3, round(area_m2 / 10)),
        "ventilador": max(1, comodos - 2),
    }


def perfil_conta(total_kwh, pessoas, regiao, tarifa=TARIFA_PADRAO):
    return PerfilConsumo(pessoas, regiao, _itens_tipicos(pessoas), "conta", tarifa, total_kwh)


def perfil_aparelhos(itens, pessoas, regiao):
    return PerfilConsumo(pessoas, regiao, itens, "aparelhos")
