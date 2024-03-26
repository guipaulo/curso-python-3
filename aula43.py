texto = 'Python'
novo_texto = ''

i = 0
while i < len(texto):
    print(texto[i], i)
    i += 1

for letra in texto:
    print(letra)

for letra in texto:
    novo_texto += f'*{letra}'

print(novo_texto)