#programa onde você tenta adivinhar o número que o computador pensou
import random
from time import sleep
n = random.randint(0, 5)
r = int(input('tente adivinhar o número que eu pensei entre 0 e 5: '))
print('PROCESSANDO...')
sleep(1)
if r == n:
    print('Você venceu, parabéns')
else:
    print(f'Você perdeu. Eu pensei no número {n} e não no {r}')
print('Obrigado Por Jogar')
