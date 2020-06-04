viagem = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar sua viagem de {viagem}km.')
v1 = viagem * 0.50
v2 = viagem * 0.45
if viagem <= 200:
    print(f'E o preço da sua passagem será de R${v1:.2f}.')
else:
    print(f'E o preço da sua passagem já com a promoção será R${v2:.2f}.')
