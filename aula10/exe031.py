#programa que lê e a distância de uma viagem e diz quanto você terá que pagar
km = float(input('entre com o valor da distância da sua viagem: '))
if km <= 200:
    total = km * 0.5
    print('você terá que pagar \033[32mR${:.2f}\033[m'.format(total))
else:
    total = km * 0.45
    print('você terá que pagar \033[32mR${:.2f}\033[m'.format(total))