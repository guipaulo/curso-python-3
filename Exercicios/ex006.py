n1, n2, n3 = input().split(' ')

iN1 = int(n1)
iN2 = int(n2)
iN3 = int(n3)

lista = [iN1, iN2, iN3]
listaS = sorted(lista)
print(f'{listaS[-1]} eh o maior')