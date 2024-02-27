entrada = input('[E] Entrar ou [S] Sair: ')
senha = input('Digite a senha: ')

SenhaPermitida = '123456'


if (entrada == 'E' or entrada == 'e') and senha == SenhaPermitida:
    print('Entrar')
else:
    print('Sair')

