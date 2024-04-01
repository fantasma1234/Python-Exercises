#programa que lê o cateto adjacente e o cateto oposto de um triângulo retângulo e faz a hipotenusa
import math
cateto1 = float(input('entre com o valor do cateto adjacente: '))
cateto2 = float(input('entre com o valor do cateto oposto: '))
hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2)) #sem o comando hypot
print(f'a hipotenusa é igual a {hipotenusa:.2f}')

#outra forma

ca = float(input('entre com o valor do cateto adjacente: '))
co = float(input('entre com o valor do cateto oposto: '))
hi = math.hypot(ca, co) #com o comando hypot (o comando hypot calcula a hipotenusa)
print(f'a hipotenusa é igual a {hi:.2f}')