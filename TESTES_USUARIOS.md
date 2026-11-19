# Testes com usuários

As casas, os consumos e as contas abaixo são fictícios. 

## Como aplicar


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

1. Abrir a opção 8 e dizer qual caminho escolheria.
2. Abrir a opção 9 e perguntar: `Como posso reduzir minha conta de luz?`

**Conferência**

- Consumo: 199,2 kWh/mês, cerca de R$ 219,13.
- Primeiro passo: banho de 5 minutos, filtro de linha e uso com carga cheia.
- Eficiência de baixo custo: R$ 60 de investimento e economia de cerca de R$ 27,91 por mês.
- Energia solar: R$ 4.336,42 de investimento e retorno de 2,9 anos.
  
------------------------------------------------------------------------------------------------------------------------------------------------
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

------------------------------------------------------------------------------------------------------------------------------------------------
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
2. Abrir a opção 4 e comparar as alternativas para água quente.
3. Abrir a opção 9 e perguntar: `c`

**Conferência**

- Consumo: 281,6 kWh/mês, cerca de R$ 309,79.
- Maior área: aquecimento de água, com 90,0 kWh/mês.
- Banho de 5 minutos: economia de cerca de R$ 37,12 por mês, sem investimento.
- Aquecedor solar: R$ 8.000 e retorno de 9,6 anos.

------------------------------------------------------------------------------------------------------------------------------------------------
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

1. Abrir a opção ` e comparar as alternativas.
2. Abrir a opção 9 e perguntar: `Vale a pena trocar o ar-condicionado?`
3. Dizer se a resposta respondeu à pergunta.

**Conferência**

- Consumo: 506,1 kWh/mês, cerca de R$ 556,72.
- Climatização: 198,5 kWh/mês.
- Ar-condicionado inverter: R$ 6.000 e retorno de 6,9 anos.
- Parcela solar da climatização: R$ 5.240,32 e retorno de 2,6 anos.


## Registro dos testes

| Participante | Cenário | Concluiu sem ajuda? | Entendeu a orientação? | Utilidade (1 a 5) | Comentário recebido |
|---|---|---|---|---|---|
| P1 | 1 | SIM | SIM | 4 | Orientação de como reduzir, no que investir e as limitações |
| P2 | 2 | SIM | SIM | 5 | Uma solução com energia solar, as condições para implementar e as limitações |
| P3 | 3 | SIM | SIM | 5 | Confirmação de que o chuveiro gasta muito |
| P4 | 4 | Mais ou Menos | SIM | 3 | Passou a comparação e possibilidades. |
