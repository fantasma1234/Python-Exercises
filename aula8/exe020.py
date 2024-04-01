#programa que sorteia a ordem de quem apresenta primeiro o trabalho 
import random
nome1 = str(input('entre com o primeiro nome: '))
nome2 = str(input('entre com o segundo nome: '))
nome3 = str(input('entre com o terceiro nome: '))
nome4 = str(input('entre com o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
sorte = random.shuffle(lista)
print(f'a ordem de apresentação vai ser {lista}')