senha = input('Digite sua senha: ')

if senha == '123456':
    print('Entrou')
elif not senha:
    print('Você não digitou nada')
else:
    print('Senha incorreta')

