#programa que lê o comprimento de três segmentos de reta e diz se eles podem ou não formar um triângulo
r1 = float(input('entre com o primeiro segmento: '))
r2 = float(input('entre com o segundo segmento: '))
r3 = float(input('entre com o terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('os segmentos podem formar um triângulo')
else:
    print('os segmentos não podem formar um triângulo')