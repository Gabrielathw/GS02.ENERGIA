# Citizen Assist AI - Energia para Famílias

Soluções em Energias Renováveis e Sustentáveis para a Global Solution.

## Integrantes
GABRIELA CAMPOS - RM: 572738
LAURAA PÍCARI - RM: 569914
LUCAS NEVES - RM: 572679


## Público e problema

O público são famílias brasileiras que querem entender a conta de luz antes de mudar hábitos ou investir em energia.

A necessidade energética é o consumo elétrico da casa. Muitas famílias não sabem quais usos pesam mais nem se uma troca compensa. O assistente transforma o consumo em orientações com custo, retorno, impacto ambiental e limitações.

## Funcionalidades de energia

- Calcula o consumo de duas formas: valor da conta de luz ou quantidade de eletrodomésticos.
- Separa o consumo em iluminação, climatização, água quente, refrigeração, eletrônicos, cozinha e lavanderia.
- Compara manter a situação atual, usar medidas de eficiência e adotar fontes solares.
- Calcula investimento, custo em 25 anos, economia, retorno e CO2 da energia da rede.
- Responde perguntas no **Citizen Assist AI** usando os resultados do perfil da família.

## Exemplo de resultado

Família simulada no Sudeste: 4 pessoas, 1 geladeira, 1 chuveiro elétrico, 2 televisões, 1 ar-condicionado, 4 ventiladores, 12 lâmpadas fluorescentes e outros aparelhos comuns. O consumo é de **314,2 kWh/mês**, com tarifa de R$ 1,10/kWh.

| Opção | Investimento | Economia em 25 anos | Retorno |
|---|---:|---:|---:|
| Eficiência de baixo custo | R$ 240 | R$ 15.403 | 0,4 ano |
| Energia solar fotovoltaica (2,29 kWp) | R$ 8.038 | R$ 58.556 | 3,0 anos |
| Eficiência + energia solar (1,87 kWp) | R$ 7.002 | R$ 62.810 | 2,5 anos |
| Aquecedor solar de água | R$ 7.000 | R$ 7.882 | 10,5 anos |

No cenário conservador, com preço 30% maior e geração 15% menor, a energia solar sozinha retorna em cerca de 4,7 anos.

!Esses valores são estimativas e não garantem economia.!

## Integração ao assistente

A opção **9 - Perguntar ao Citizen Assist AI** usa assistente_energia.py. A função responder(pergunta, analise) recebe a pergunta e os resultados calculados para aquela família.

Exemplo de pergunta: `Vale a pena colocar energia solar?`

A resposta traz a orientação, os números do perfil, as condições e o limite da estimativa.


## Limitações

- O consumo varia com aparelho, clima e hábitos.
- A tarifa padrão é uma média estimada; a conta da família deve prevalecer.
- Os preços mudam por região e fornecedor.
- A divisão por áreas no modo da conta de luz é estimada.
- Inflação, reajustes de tarifa e financiamento não foram incluídos.
- A solução é orientativa e não substitui projeto técnico.
