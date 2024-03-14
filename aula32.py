"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

if numero.isdigit():
    n_int = int(numero)
    if n_int % 2 == 0:
        print('O número é par!')
    else:
        print('O número é impar!')
else:
    print('Valor digitado não é um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Qual é a hora? ')
entrada_int = int(entrada)
if entrada_int >= 0 and entrada_int <= 11:
    print('Bom dia!')
elif entrada_int >= 12 and entrada_int <= 17:
    print('Boa tarde!')
elif entrada_int >= 18 and entrada_int <= 23:
    print('Boa noite!')
else:
    print('Horra errada!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal!')
elif len(nome) > 6:
    print('Seu nome é muito grande!')