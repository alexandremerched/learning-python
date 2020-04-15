values = []
c1 = c2 = sp = s3c = m2l = 0

for c in range(0, 9):
    values.append(int(input(f'Digite um valor para [{c1}, {c2}]: ')))
    c2 += 1
    if c2 == 3:
        c1 += 1
        c2 = 0

for c in values:
    if c % 2 == 0:
        sp += c

for pos, v in enumerate(values[3:6]):
    if pos == 0:
        m2l = v
    elif v > m2l:
        m2l = v

print('-=' * 30)
for i, c in enumerate(values):
    print(f'[  {c}  ]', end='')
    if i == 2 or i == 5 or i == 8:
        s3c += c
        print()
print('-=' * 30)    
print(f'A soma dos valores pares é {sp}\nA soma dos valores da terceira coluna é {s3c}\nO maior valor da segunda linha é {m2l}.')
