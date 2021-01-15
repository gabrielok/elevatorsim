# elevatorsim

## Objetivo
Simular o uso compartilhado de um elevador em um prédio residencial para determinar algumas hipóteses, como:
1. Retornar ao térreo automaticamente após um determinado período de tempo aumenta o consumo energético, porém reduz o tempo médio de espera dos usuários
2. Retornar a um determinado andar automaticamente é mais eficiente que ao térreo (em termos energéticos ou de tempo de espera), e o andar ótimo pode ser calculado para cada prédio baseado no perfil de uso dos moradores

## Lógica do programa
### CLASSES
### 1. Prédio
#### Atributos
- elevador
- pessoas
- número de andares
- número de andares de garagem
- altura entre andares
### 2. Pessoa
#### Atributos
- frequência de uso do elevador
- horários de uso do elevador
### 3. Elevador
#### Atributos
- velocidade máxima
- aceleração máxima
- jerk máximo
- passageiros
- trajeto
- capacidade máxima
- posição em metros
#### Funções
- calcular o trajeto a ser percorrido baseado nos andares requisitados
- calcular o tempo entre paradas no trajeto
- calcular o gasto energético do trajeto

### Simulação
A simulação inicia calculando os horários pretendidos de uso do elevador de cada morador como uma distribuição gaussiana em torno dos horários normais. Exemplo: alguém que sai todos os dias às 8h e retorna às 19h irá, em um dado dia, sair às 7h53 e retornar às 18h47. Então, o dia começa no horário em que o primeiro morador chama o elevador e passa 1 minuto por vez. A cada passo, o programa verifica a posição do elevador e passa uma lista de moradores que o chamaram.
