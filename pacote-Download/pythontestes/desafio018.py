import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O valor do seno desse ângulo é {sen:.2f}')
print(f'O valor do cosseno desse ângulo é {cos:.2f}')
print(f'O valor da tangente desse ângulo é {tang:.2f}')
