#lê um valor em metros e o exibe convertido em quilômetros (km), Hectrômetro (hm), decâmetro(dam), decímetro(dm), centímetro(cm) e milímetro(mm)
m = float(input('digite um número em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'o valor digitado foi {m}m')
print(f'o valor de {m} em km é {km}')
print(f'o valor de {m} em hm é {hm}')
print(f'o valor de {m} em dam é {dam}')
print(f'o valor de {m} em dm é {dm}')
print(f'o valor de {m} em cm é {cm}')
print(f'o valor de {m} em mm é {mm}')