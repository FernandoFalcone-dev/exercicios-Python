import random
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
ordem = [a, b, c, d]
random.shuffle(ordem)
print(f'A ordem de apresentação será {ordem}.')
