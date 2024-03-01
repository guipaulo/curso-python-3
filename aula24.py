nome = 'Otávio'

print(nome[2])
print(nome[-4])

print('á' in nome)
print('vio' in nome)
print('á' not in nome)

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')