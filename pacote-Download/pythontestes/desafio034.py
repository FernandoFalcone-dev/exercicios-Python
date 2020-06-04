wages = float(input('Qual é o salário do funcionário? R$'))
if wages <= 1250:
    novo = wages * 115 / 100
else:
    novo = wages * 110 / 100
print(f'Para quem recebia R${wages:.2f}, o aumento é R${novo:.2f}.')
