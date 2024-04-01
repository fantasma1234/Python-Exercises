#programa que lê a velocidade de um veiculo e mostra se o motorista deverá pagar uma multa
v = float(input('qual a velocidade do carro? '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Você foi multado. Você deverá pagar uma multa de R$ {multa:.2f} ')
else:
    print('Está andando na velocidade permitida')