A, B, C = (input()).split(' ')

fA = float(A)
fB = float(B)
fC = float(C)
pi = 3.14159

AreaTriangulo = (fA * fC)/2
AreaCirculo = pi * (fC**2)
AreaTrapezio = ((fA + fB) * fC)/2
AreaQuadrado = fB**2
AreaRetangulo = fA * fB

print(f'TRIANGULO: {AreaTriangulo:.3f}')
print(f'CIRCULO: {AreaCirculo:.3f}')
print(f'TRAPEZIO: {AreaTrapezio:.3f}')
print(f'QUADRADO: {AreaQuadrado:.3f}')
print(f'RETANGULO: {AreaRetangulo:.3f}')