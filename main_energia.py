# -*- coding: utf-8 -*-
import sys

import dados_energia as d
from analise_energia import AnaliseEnergia, brl, geracao_kwp_ano, num
from assistente_energia import responder
from consumo_familiar import perfil_aparelhos, perfil_conta

REGIOES = ("Sul", "Sudeste", "Nordeste", "Centro-Oeste", "Norte")
AREAS_MENU = {str(i): area for i, area in enumerate(d.AREAS, start=2)}
AVISO = "[!] Valores ESTIMADOS: não são medição nem garantia de economia."


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def ler_inteiro(mensagem, minimo, maximo, vazio=None):
    while True:
        entrada = input(mensagem).strip()
        if entrada == "" and vazio is not None:
            return vazio
        try:
            valor = int(entrada)
        except ValueError:
            print("[!] Digite um número inteiro.\n")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"[!] Digite um valor entre {minimo} e {maximo}.\n")


def ler_decimal(mensagem, minimo, maximo, vazio):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        if entrada == "":
            return vazio
        try:
            valor = float(entrada)
        except ValueError:
            print("[!] Digite um número.\n")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"[!] Digite um valor entre {minimo} e {maximo}.\n")


def ler_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).strip().upper()
        if valor in opcoes:
            return valor
        print(f"[!] Digite uma destas opções: {', '.join(opcoes)}.\n")


def questionario_aparelhos():
    while True:
        titulo("[QUANTIDADE DE CADA ELETRODOMÉSTICO]")
        print("Digite a quantidade. Se não tiver, digite 0 ou aperte Enter.\n")
        itens = {}
        for chave, (nome, _, _, _) in d.APARELHOS.items():
            itens[chave] = ler_inteiro(f"{nome}: ", 0, 100, vazio=0)
            print()
        if any(itens.values()):
            return itens
        print("[!] Informe pelo menos um aparelho.")


def criar_perfil():
    titulo("[CRIAR PERFIL FAMILIAR]")
    pessoas = ler_inteiro("\nNúmero de pessoas: ", 1, 20)

    print("\nQual é a região em que reside?")
    print("(Usada para estimar a geração de energia solar)\n")
    for i, regiao in enumerate(REGIOES, start=1):
        print(f"  {i}. {regiao}")
    regiao = REGIOES[ler_inteiro("\nEscolha (1-5): ", 1, 5) - 1]

    print("\n--- COMO CALCULAR O CONSUMO ---\n")
    print("  N = Valor da minha conta de luz")
    print("  C = Quantidade dos meus eletrodomésticos")
    modo = ler_opcao("\nDigite N ou C: ", ("N", "C"))

    if modo == "N":
        total = ler_inteiro("\nConsumo mensal da conta (kWh): ", 1, 10000)
        pergunta = f"\nTarifa por kWh, com impostos (Enter = {brl(d.TARIFA_PADRAO)}): "
        tarifa = ler_decimal(pergunta, 0.1, 5, d.TARIFA_PADRAO)
        return perfil_conta(total, pessoas, regiao, tarifa)
    return perfil_aparelhos(questionario_aparelhos(), pessoas, regiao)


def mostrar_perfil(analise):
    perfil = analise.perfil
    titulo("[PERFIL FAMILIAR - CONSUMO MENSAL]")
    print(f"Pessoas: {perfil.pessoas}")
    print(f"Região: {perfil.regiao}")
    print(f"Tarifa usada: {brl(analise.tarifa)} por kWh\n")
    for area, nome in d.AREAS.items():
        print(f"[*] {nome + ':':<24}{num(analise.areas[area]):>9} kWh\n")
    print("-" * 60)
    print(f"[>] {'CONSUMO TOTAL:':<24}{num(analise.total):>9} kWh/mês")
    print(f"[>] {'CUSTO DA ENERGIA:':<24}{brl(analise.total * analise.tarifa):>13}/mês\n")
    if perfil.modo == "conta":
        print("[i] O total vem da sua conta. A divisão por área é estimada")
        print("    e pode mudar bastante, principalmente com ar-condicionado.")
    elif perfil.modo == "aparelhos":
        print("[i] Cálculo baseado nas quantidades informadas e em um uso típico.")
    print(AVISO)


def mostrar_opcao(indice, opcao):
    print(f"\n{indice}. {opcao['nome']}")
    print(f"   {opcao['descricao']}\n")
    print(f"   Investimento inicial: {brl(opcao['investimento'])}")
    print(f"   Energia da rede: {num(opcao['kwh_mes'])} kWh/mês")
    print(f"   Custo em {d.PERIODO_ANOS} anos: {brl(opcao['custo_periodo'])}")
    if opcao["tipo"] != "atual":
        print(f"   Economia em {d.PERIODO_ANOS} anos: {brl(opcao['economia_periodo'])}")
        if opcao["retorno_anos"] is None:
            print("   Retorno: não se paga no período")
        elif opcao["investimento"] == 0:
            print("   Retorno: imediato")
        else:
            print(f"   Retorno: {num(opcao['retorno_anos'])} anos")
    print(f"   CO2 da rede: {num(opcao['co2_ano'])} kg/ano")


def comparar_area(analise, area):
    titulo(f"[COMPARAÇÃO: {d.AREAS[area].upper()}]")
    opcoes = analise.comparar_area(area)
    if not opcoes:
        print("\nNão há consumo nessa área no seu perfil.")
        return
    for indice, opcao in enumerate(opcoes, start=1):
        mostrar_opcao(indice, opcao)
    melhor = analise.melhor_area(area)
    print("\n" + "-" * 60)
    if melhor:
        print(f"[>] Melhor primeiro passo: {melhor['nome']}")
    else:
        print("[>] Nas premissas usadas, nenhuma troca compensa agora.")
    print("[i] A energia solar é vendida como sistema da casa; aqui aparece só a parte desta área.")
    print(AVISO)


def relatorio(analise):
    titulo(f"[COMPARAÇÃO DA CASA EM {d.PERIODO_ANOS} ANOS]")
    print(f"Geração solar estimada: {num(analise.geracao_kwp, 0)} kWh por kWp ao ano")
    for indice, opcao in enumerate(analise.plano_casa(), start=1):
        mostrar_opcao(indice, opcao)
    primeira, investimento = analise.recomendacao()
    titulo("[RECOMENDAÇÃO]")
    if primeira:
        print(f"\n1. Comece por: {primeira['descricao']}.")
    if investimento:
        print(f"\n2. Se puder investir: {investimento['nome']}.")
        print("   Condições: imóvel próprio, telhado sem sombra e orçamento local.")
    conservador = analise.retorno_solar_conservador()
    if conservador:
        print(f"\n[i] Solar no cenário conservador: retorno de {num(conservador)} anos")
        print("    (preço 30% maior e geração 15% menor).")
    print("\n[i] O CO2 considera a energia da rede. A fabricação dos painéis também")
    print("    emite CO2; por isso o ganho solar é maior na conta do que no clima.")
    print(AVISO)


def conversar(analise):
    titulo("[CITIZEN ASSIST AI - ENERGIA]")
    print("Faça uma pergunta. Exemplo: Como reduzir minha conta?")
    print("Aperte Enter para voltar.")
    while True:
        pergunta = input("\nVocê: ").strip()
        if not pergunta:
            return
        print("\nCitizen Assist AI:\n")
        print(responder(pergunta, analise))


def menu():
    analise = None
    while True:
        titulo("[>] CITIZEN ASSIST AI - ENERGIA PARA FAMÍLIAS")
        if analise is None:
            print("1. Criar perfil familiar")
            print("0. Sair")
            opcao = ler_opcao("\nDigite a opção: ", ("1", "0"))
            if opcao == "1":
                analise = AnaliseEnergia(criar_perfil())
                print("\n[OK] Perfil criado!")
                mostrar_perfil(analise)
                continue
            print("\n[OK] Até logo!")
            return

        print("1. Ver perfil familiar")
        for numero, area in AREAS_MENU.items():
            print(f"{numero}. Comparar: {d.AREAS[area]}")
        print("8. Comparar opções da casa")
        print("9. Perguntar ao Citizen Assist AI")
        print("10. Criar novo perfil")
        print("0. Sair")
        opcao = ler_opcao("\nDigite a opção: ", tuple(str(i) for i in range(11)))
        if opcao == "1":
            mostrar_perfil(analise)
        elif opcao in AREAS_MENU:
            comparar_area(analise, AREAS_MENU[opcao])
        elif opcao == "8":
            relatorio(analise)
        elif opcao == "9":
            conversar(analise)
        elif opcao == "10":
            analise = AnaliseEnergia(criar_perfil())
            mostrar_perfil(analise)
        else:
            print("\n[OK] Até logo!")
            return


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    menu()
