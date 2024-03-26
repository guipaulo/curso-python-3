frase = 'Python é uma linguagem de programação multiparadigma. ' \
'Python foi criado por Guido van Rossum'

print(frase.count('Python'))

i = 0
apareceu_mais_vezes = 0
letra_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu = letra_atual
    i += 1

print(f'A letra que apareceu mais vezes foi {letra_apareceu} que apareceu {apareceu_mais_vezes}x')