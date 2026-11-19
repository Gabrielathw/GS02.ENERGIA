# -*- coding: utf-8 -*-
import unicodedata

import dados_energia as d
from analise_energia import brl, num

LIMITE = (
    "Limite: é uma estimativa, não uma garantia de economia. "
    "Confirme com sua conta de luz e com orçamentos da sua região."
)

TEMAS = (
    ("iluminacao", ("lampada", "luz acesa", "iluminacao", "led")),
    ("aquecimento_agua", ("chuveiro", "banho", "agua quente", "aquecedor")),
    ("climatizacao", ("ar condicionado", "ar-condicionado", "ventilador", "climatizacao")),
    ("refrigeracao", ("geladeira", "freezer", "refrigeracao")),
    ("eletronicos", ("televisao", "tv", "computador", "notebook", "tomada", "eletronico")),
    ("cozinha_lavanderia", ("micro", "air fryer", "airfryer", "forno", "maquina", "ferro", "cozinha")),
)


def _normalizar(texto):
    sem_acento = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in sem_acento if not unicodedata.combining(c))


def _contem(texto, termos):
    palavras = texto.replace("?", " ").replace(",", " ").split()
    return any((t in texto) if len(t) > 3 else (t in palavras) for t in termos)


def _resposta_area(analise, area):
    nome = d.AREAS[area]
    kwh = analise.areas[area]
    if kwh <= 0:
        return f"{nome}: não há consumo nessa área no seu perfil, então não há o que recomendar."
    linhas = [f"{nome}: cerca de {num(kwh)} kWh por mês ({brl(kwh * analise.tarifa)})."]
    melhor = analise.melhor_area(area)
    if melhor:
        retorno = "imediato" if melhor["investimento"] == 0 else f"cerca de {num(melhor['retorno_anos'])} anos"
        linhas.append(
            f"Orientação: {melhor['nome']}. Economia estimada de {brl(melhor['economia_mes'])} por mês; "
            f"investimento de {brl(melhor['investimento'])}; retorno {retorno}."
        )
    else:
        linhas.append("Orientação: nas premissas usadas, nenhuma troca compensa agora.")
    return "\n\n".join(linhas + [LIMITE])


def _resposta_solar(analise):
    solar = next((o for o in analise.plano_casa() if o["nome"] == "Energia solar fotovoltaica"), None)
    if not solar:
        return "Seu consumo não passa do mínimo cobrado na conta, então a energia solar não reduziria a fatura.\n\n" + LIMITE
    conservador = analise.retorno_solar_conservador()
    texto = (
        f"Energia solar: seria preciso um sistema de cerca de {num(solar['kwp'], 2)} kWp, "
        f"com investimento estimado de {brl(solar['investimento'])}. "
        f"Economia média de {brl(solar['economia_mes'])} por mês em {d.PERIODO_ANOS} anos; "
        f"retorno de {num(solar['retorno_anos'])} anos"
    )
    if conservador:
        texto += f" (ou {num(conservador)} anos em um cenário conservador)"
    return (
        texto + ".\n\nCondições: telhado próprio, sem sombra, estrutura adequada e aprovação da "
        "distribuidora. Quem mora de aluguel normalmente não consegue instalar.\n\n" + LIMITE
    )


def _resposta_plano(analise):
    primeira, investimento = analise.recomendacao()
    partes = [f"Sua casa consome cerca de {num(analise.total)} kWh por mês ({brl(analise.total * analise.tarifa)})."]
    if primeira:
        partes.append(f"Primeiro passo: {primeira['descricao']}. Economia estimada de {brl(primeira['economia_mes'])} por mês.")
    if investimento:
        partes.append(
            f"Se puder investir: {investimento['nome']}, por {brl(investimento['investimento'])}, "
            f"com retorno de cerca de {num(investimento['retorno_anos'])} anos."
        )
    return "\n\n".join(partes + [LIMITE])


def _resposta_ambiente(analise):
    return (
        f"Pelo fator médio da rede, sua casa está ligada a cerca de "
        f"{num(analise.total * 12 * d.FATOR_REDE_KG_KWH, 0)} kg de CO2 por ano.\n\n"
        "A eletricidade brasileira já é relativamente limpa. Por isso, a energia solar pesa mais na "
        "conta do que no CO2: sua fabricação também gera emissões. Economizar energia é a medida "
        "ambiental mais direta.\n\n" + LIMITE
    )


def responder(pergunta, analise):
    texto = _normalizar(pergunta)
    if _contem(texto, ("fonte", "referencia", "de onde")):
        return "Os dados e as fontes estão em DADOS_E_CALCULOS.md, com links e premissas identificadas."
    if _contem(texto, ("co2", "carbono", "ambiental", "meio ambiente", "poluicao")):
        return _resposta_ambiente(analise)
    for area, termos in TEMAS:
        if _contem(texto, termos):
            return _resposta_area(analise, area)
    if _contem(texto, ("solar", "placa", "painel", "fotovoltaic")):
        return _resposta_solar(analise)
    if _contem(texto, ("economizar", "reduzir", "conta", "gasto", "consumo", "recomenda", "vale a pena")):
        return _resposta_plano(analise)
    return "Posso ajudar com: conta de luz, chuveiro, lâmpadas, ar-condicionado, geladeira, energia solar, CO2 e fontes."
