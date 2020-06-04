from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
guess = int(input("Em que número eu pensei? "))
print('PROCESSANDO...')
sleep(3)
if guess == num:
    print('PARABÉNS, você acertou!')
else:
    print(f'Desculpe, o número que pensei foi {num} e não {guess}')
