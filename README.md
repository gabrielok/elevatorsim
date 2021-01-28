# elevatorsim

## Objetivo
Simular o uso compartilhado de um elevador em um prédio residencial para validar algumas hipóteses, como:
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
- horários de uso do elevador e andar no qual sai (subsolo ou térreo)
- andar no qual mora
- identificador único
- tempo que passou esperando pelo elevador
#### Funções
- atualizar o tempo esperando pelo elevador
- calcular os horários de uso no dia baseado na distribuição gaussiana
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
- registrar a entrada de uma pessoa

### Simulação
A simulação inicia calculando os horários pretendidos de uso do elevador de cada morador como uma distribuição gaussiana em torno dos horários normais. Exemplo: alguém que sai todos os dias às 8h e retorna às 19h irá, em um dado dia, sair às 7h53 e retornar às 18h47. Forma-se uma lista ordenada de horários e a simulação inicia no menor horário. O elevador simula o movimento até o fim ou até outro morador chamá-lo. A ordem das paradas do elevador é armazenada em uma min heap para subida / max heap para descida.
