#calcula o aumento do salário de uma pessoa 
salario = float(input('quanto o funcionario ganha de salário? '))
aumento = float(input('quanto é o aumento do salário do funcionario, em porcentagem? '))
p = salario * aumento / 100
novo = salario + p
print(f'esse trabalhador ganha {salario:.2f} por mês, se ele recebesse um almento de {aumento:.2f}% ele passaria a ganhar {novo:.2f} ')