from math import hypot
co = float(input('Quanto mede o cateto oposto do triângulo? '))
ca = float(input('Quanto mede o cateto adjacente do triângulo? '))
hi = hypot(co, ca)
print(f'A medida da hipotenusa é {hi:.2f}.')
