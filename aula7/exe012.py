#programa que calcula o novo valor de um produto na promoção
n = float(input('qual é o preço do produto? '))
desconto = float(input('quanto é o desconto? '))
p = n * desconto / 100
novo = n - p
print(f'o produto que antes custava {n:.2F}, depois da promoção de {desconto}% de desconto agora está custando {novo:.2f}')