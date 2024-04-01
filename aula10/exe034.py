#programa que lê o salário de um funcionário e diz de quanto vai ser o seu aumento
salario = float(input('digite o sálario do funcionário: R$'))
if salario <= 1250:
    aumento = salario * 15 / 100
    novo = aumento + salario
else:
    aumento = salario * 10 / 100
    novo = aumento + salario
print(f'o sálario do funcionário que antes era \033[33m{salario:.2f}\033[m agora vai passar a ser \033[34m{novo:.2f}\033[m')