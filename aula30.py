#Em Python, é convencionado que valores que devem ser constantes estejam em CAIXA ALTA.

#VARIÁVEL:
velocidade = 61
local_carro = 90

#CONSTANTE:
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Carro multado em radar 1!')