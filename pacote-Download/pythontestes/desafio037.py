num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[1;31mBINÁRIO\033[m
[ 2 ] converter para \033[1;32mOCTAL\033[m
[ 3 ] converter para \033[1;33mHEXADECIMAL\033[m''')
escolha = int(input('Sua opção é: '))
if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente de novo.')
