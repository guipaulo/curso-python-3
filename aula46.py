for i in range(10):
    if i == 2:
        print('i = 2 é pulado')
        continue
    
    if i == 8:
        print('i = 8, código parado, else não será executado')
        break
    
    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso')