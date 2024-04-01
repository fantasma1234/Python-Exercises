#programa que lê a largura e a altura de uma parede e calcula sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
l = float(input('digite a largura em metros: '))
a = float(input('digite a altura em metos: '))
area = l * a
tinta = area / 2
print(f'sua parede tem a dimensão de {l}x{a} e sua área é de {area}m²\n para pintar essa parede, voê precisa de {tinta}L de tinta')