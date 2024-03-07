print(1234)
print(456)

num = input('Vou dobrar o número: ')

try:
    num_float = float(num)
    print(f'O dobro de {num_float} = {num_float*2:.2f}')
except:
    print('Isso não é um número')

#if num.isdigit():
 #   num_float = float(num)
  #  print(f'O dobro de {num_float} = {num_float*2:.2f}')
#else:
 #   print('Isso não é um número')