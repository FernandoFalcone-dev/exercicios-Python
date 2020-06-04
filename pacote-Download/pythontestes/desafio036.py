vc = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('Em quantos anos você pode pagar? '))
pm = vc / tempo / 12
print(f'Para pagar uma casa no valor de R${vc} em {tempo} anos a prestação será R${pm:.2f}.')
if pm <= (30 * salario)/100:
    print('Ok, seu empréstimo foi aceito.')
else:
    print('Me desculpe, seu empréstimo foi negado.')
