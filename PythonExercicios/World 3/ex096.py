def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')
    

print('\nControle de Terrenos')
print('-' * 20)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

área(l, c)
