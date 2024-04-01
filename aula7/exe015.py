dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
total = (60 * dias) + (km * 0.15)
print(f'O total a pagar é de R${total:.2f}')