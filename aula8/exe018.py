#programa que calcula o seno, cosseno e a tangente de um ângulo
import math
angulo = float(input('digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'o ângulo de {angulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'o ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'o ângulo de {angulo} tem a tangente de {tangente:.2f}')