import math

'''DESENVOLVIDO POR: Paulo Guilherme Silva de Araújo - 1 Período de TSI'''

a = float(input('Digite o coeficiente "a": '))

while a == 0:
    print('O coeficiente "a" não pode ser 0!')
    a = float(input('Digite o coeficiente "a": '))

    if a != 0:
        break

b= float(input('Digite o coeficiente "b": '))
c = float(input('Digite o coeficiente "c": '))

print(f'Sua função é {a}x² + {b}x + {c}')

delta = (b**2) - 4*(a*c)

try:
    Raiz1 = (-b - math.sqrt(delta)) / (2*a)
    Raiz2 = (-b + math.sqrt(delta)) / (2*a)
except ValueError:
    print('Não é possivel calcular raiz quadrada de números negativos')

Xvertice = -b/(2*a)
Yvertice = -delta/(4*a)


if a < 0:
    print('Seu gráfico é uma parábola com a concavidade voltada para baixo')
elif a > 0:
    print('Seu gráfico é uma parábola com a concavidade voltada para cima')

if delta > 0:
    print('Sua função possui 2 raizes reais')
    print(f'Suas raizes são {Raiz2:.2f} e {Raiz1:.2f}')
elif delta == 0:
    print('Sua função possui 1 raiz real')
    print(f'Sua raiz é {Raiz1:.2f}')
elif delta < 0:
    print('Sua função não possui raizes reais')

print(f'O vertice da parábola é o ponto ({Xvertice:.2f};{Yvertice:.2f})')

if a < 0 and delta > 0:
    print(f'A função é positiva sempre que x >= {Raiz2:.2f} e x <= {Raiz1:.2f}')
elif a < 0 and delta == 0:
    print(f'A função nunca é positiva. É negativa para valores menores ou maiores que {Raiz1}')
elif a < 0 and delta < 0:
    print(f'A função nunca é positiva. Não possui raizes.')

if a > 0 and delta > 0:
    print(f'A função é negativa sempre que x >= {Raiz2:.2f} e x <= {Raiz1:.2f}')
elif a > 0 and delta == 0:
    print(f'A função nunca é negativa. É positiva para valores menores ou maiores que {Raiz1:.2f}')
elif a > 0 and delta < 0:
    print(f'A função nunca é negativa. Não possui raizes.')