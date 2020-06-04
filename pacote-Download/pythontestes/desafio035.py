print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos PODEM formar um triângulo.')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')
