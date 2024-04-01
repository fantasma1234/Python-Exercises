#programa que lê o nome de uma cidade e diz se ela tem o nome Santo
cidade = str(input('digite o nome da cidade que você nasceu: ')).strip().capitalize()
print('Santo' in cidade)

#outra forma

cid = str(input('digite o nome da cidade que você nasceu')).strip()
print(cid[:5].upper() == 'SANTO')
