'''DESENVOLVIDO POR: Paulo Guilherme Silva de Araújo - 1 Período de TSI'''

a = int(input('Digite o coeficiente "a": '))
b = int(input('Digite o coeficiente "b": '))

zero = float(-(b/a))

print('Sua função é:')
print(f'f(x) = {a}x + {b}\n')

print(f'O zero da função é ({zero:.2};0)')

if a > 0:
    print('Sua função é positiva (a > 0)')
    print(f'A função é positiva para todo x > {zero:.2f} e negativa para valores x < {zero:.2f}')
elif a < 0:
    print('Sua função é negativa (a < 0)')
    print(f'A função é positiva para todo x < {zero:.2f} e negativa para valores x > {zero:.2f}')

print(f'A função corta o eixo x no ponto ({zero:.2f};0)')
print(f'A função corta o eixo y no ponto (0;{b})')