vel = float(input('Velocidade do carro: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Parabéns, continue dirigindo com cautela!')
else:
    print(f'Você recebeu uma multa! O valor que deverá ser pago é de R${multa:.2f}.')
