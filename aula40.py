while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Selecione um operador [+-/*]: ')
    numeros_validos = None
    num1 = 0
    num2 = 0

    try:
        num1 = float(numero1)
        num2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta...\n')
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('WTF?')

    sair = input('Quer sair? [S]: ').lower().startswith('s')

    if sair:
        break
    else:
        continue