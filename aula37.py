contador = 0

while contador < 100:
    contador += 1
    if contador == 6:
        print(f'Não vou mostrar o {contador}')
        continue
    if contador >= 10 and contador <= 35:
        print(f'Não vou mostrar o {contador}')
        continue
    print(contador)