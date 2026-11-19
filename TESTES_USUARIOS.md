# Testes com usuários

Os testes usam **pessoas reais** e **famílias simuladas**. As casas, os consumos e as contas abaixo são fictícios. Assim, ninguém precisa informar dados pessoais.

Preencha os registros somente depois de aplicar cada teste. Identifique os participantes apenas como P1, P2, P3 e P4.

## Como aplicar

Tempo previsto: cerca de 10 minutos por pessoa.

1. Explique: "Estamos testando o programa, não você. Pode dizer o que ficou confuso."
2. Abra o terminal na pasta do projeto e execute `python main_energia.py`.
3. Leia a situação e passe os dados do cenário.
4. Deixe a pessoa usar o programa. Ajude apenas se ela travar e anote onde isso aconteceu.
5. Faça as perguntas finais e registre as respostas com as palavras dela.

Os valores de conferência são para quem aplica o teste. Não mostre antes de a pessoa responder.

## Cenário 1 - Família que informa seus aparelhos

**Situação:** "Você mora com mais duas pessoas no Nordeste e quer saber como reduzir a conta."

**Dados para digitar**

| Pergunta | Resposta |
|---|---|
| Criar perfil | `1` |
| Número de pessoas | `3` |
| Região | `3` (Nordeste) |
| Forma de cálculo | `C` |
| Geladeira, Micro-ondas, Air fryer, Televisão, Chuveiro elétrico | `1` em cada |
| Ventilador | `2` |
| Lâmpada LED | `6` |
| Roteador de internet, Máquina de lavar roupas | `1` em cada |
| Demais aparelhos | Enter |

**Tarefas**

1. Abrir a opção `8` e dizer qual caminho escolheria.
2. Abrir a opção `9` e perguntar: `Como posso reduzir minha conta de luz?`

**Conferência**

- Consumo: 199,2 kWh/mês, cerca de R$ 219,13.
- Primeiro passo: banho de 5 minutos, filtro de linha e uso com carga cheia.
- Eficiência de baixo custo: R$ 60 de investimento e economia de cerca de R$ 27,91 por mês.
- Energia solar: R$ 4.336,42 de investimento e retorno de 2,9 anos.

## Cenário 2 - Família que mora de aluguel

**Situação:** "Você mora com outra pessoa no Sul, em uma casa alugada. Sua conta mostra 180 kWh e tarifa de R$ 1,05."

**Dados para digitar**

| Pergunta | Resposta |
|---|---|
| Criar perfil | `1` |
| Número de pessoas | `2` |
| Região | `1` (Sul) |
| Forma de cálculo | `N` |
| Consumo mensal | `180` |
| Tarifa | `1,05` |

**Tarefas**

1. Abrir a opção `1` e dizer o que significa o aviso sobre a divisão por área.
2. Abrir a opção `9` e perguntar: `Moro de aluguel. Vale a pena colocar energia solar?`
3. Dizer o que faria depois de ler a resposta.

**Conferência**

- Consumo: 180,0 kWh/mês, R$ 189,00.
- Solar: 1,25 kWp, R$ 4.514,01 e retorno de 3,7 anos.
- A resposta deve avisar que quem mora de aluguel normalmente não consegue instalar.

## Cenário 3 - Família grande sem ar-condicionado

**Situação:** "Sua família tem cinco pessoas e mora no Sudeste. Vocês não têm ar-condicionado e querem descobrir o que mais pesa na conta."

**Dados para digitar**

| Pergunta | Resposta |
|---|---|
| Criar perfil | `1` |
| Número de pessoas | `5` |
| Região | `2` (Sudeste) |
| Forma de cálculo | `C` |
| Geladeira, Micro-ondas, Air fryer, Chuveiro elétrico | `1` em cada |
| Televisão, Ventilador | `2` em cada |
| Lâmpada fluorescente | `9` |
| Notebook, Roteador de internet, Máquina de lavar roupas, Ferro de passar | `1` em cada |
| Demais aparelhos | Enter |

**Tarefas**

1. Dizer qual área mais pesa no consumo.
2. Abrir a opção `4` e comparar as alternativas para água quente.
3. Abrir a opção `9` e perguntar: `O chuveiro gasta muito?`

**Conferência**

- Consumo: 281,6 kWh/mês, cerca de R$ 309,79.
- Maior área: aquecimento de água, com 90,0 kWh/mês.
- Banho de 5 minutos: economia de cerca de R$ 37,12 por mês, sem investimento.
- Aquecedor solar: R$ 8.000 e retorno de 9,6 anos.

## Cenário 4 - Família com ar-condicionado

**Situação:** "Sua família tem quatro pessoas, mora no Norte e usa dois aparelhos de ar-condicionado."

**Dados para digitar**

| Pergunta | Resposta |
|---|---|
| Criar perfil | `1` |
| Número de pessoas | `4` |
| Região | `5` (Norte) |
| Forma de cálculo | `C` |
| Geladeira, Freezer, Micro-ondas, Chuveiro elétrico | `1` em cada |
| Televisão, Ar-condicionado | `2` em cada |
| Ventilador | `1` |
| Lâmpada fluorescente | `8` |
| Computador de mesa, Roteador de internet, Máquina de lavar roupas, Ferro de passar | `1` em cada |
| Demais aparelhos | Enter |

**Tarefas**

1. Abrir a opção `3` e comparar as alternativas.
2. Abrir a opção `9` e perguntar: `Vale a pena trocar o ar-condicionado?`
3. Dizer se a resposta respondeu à pergunta.

**Conferência**

- Consumo: 506,1 kWh/mês, cerca de R$ 556,72.
- Climatização: 198,5 kWh/mês.
- Ar-condicionado inverter: R$ 6.000 e retorno de 6,9 anos.
- Parcela solar da climatização: R$ 5.240,32 e retorno de 2,6 anos.

## Perguntas finais

1. O que o programa recomendou para essa família?
2. Qual seria sua primeira ação?
3. Algum termo ficou difícil? Qual?
4. A resposta deixou claro que os valores são estimativas?
5. De 1 a 5, quanto a orientação ajudaria em uma decisão real?
6. O que você mudaria?

## Registro dos testes

| Participante | Cenário | Concluiu sem ajuda? | Entendeu a orientação? | Utilidade (1 a 5) | Comentário recebido | Dificuldade observada | Ajuste realizado |
|---|---|---|---|---|---|---|---|
| P1 | 1 | | | | | | |
| P2 | 2 | | | | | | |
| P3 | 3 | | | | | | |
| P4 | 4 | | | | | | |

## Verificação técnica dos cenários

Executada em 18/11/2026, com entradas automáticas no programa e **sem participantes**. Esta seção confere o funcionamento e os cálculos; ela não substitui os testes com usuários.

| Cenário | Entradas | Resultado observado | Valores conferidos | Situação |
|---|---|---|---:|---|
| 1 | 3 pessoas, Nordeste, aparelhos | 199,2 kWh/mês; R$ 219,13; orientação de reduzir o banho; solar de R$ 4.336,42 com retorno de 2,9 anos | 7 de 7 | Aprovado |
| 2 | 2 pessoas, Sul, conta de 180 kWh, tarifa R$ 1,05 | 180,0 kWh/mês; R$ 189,00; solar de 1,25 kWp; aviso para quem mora de aluguel | 7 de 7 | Aprovado |
| 3 | 5 pessoas, Sudeste, aparelhos, sem ar-condicionado | 281,6 kWh/mês; R$ 309,79; água quente com 90,0 kWh/mês; banho menor economiza R$ 37,12/mês | 6 de 6 | Aprovado |
| 4 | 4 pessoas, Norte, aparelhos, 2 ar-condicionados | 506,1 kWh/mês; R$ 556,72; climatização com 198,5 kWh/mês; inverter com retorno de 6,9 anos | 7 de 7 | Aprovado com ressalva |

**Ressalva do cenário 4:** os cálculos estão corretos, mas à pergunta `Vale a pena trocar o ar-condicionado?` o assistente recomenda a parcela de energia solar e não diz diretamente se a troca compensa.

As 11 verificações de `test_calculos.py` também passaram.

## Conclusão

Principais aprendizados: PREENCHER

Ajustes feitos depois dos testes: PREENCHER
