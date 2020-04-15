values = []
c1 = c2 = 0

for c in range(0, 9):
    values.append(int(input(f'Digite um valor para [{c1}, {c2}]: ')))
    c2 += 1
    if c2 == 3:
        c1 += 1
        c2 = 0

print('-=' * 30)
for i, c in enumerate(values):
    print(f'[  {c}  ]', end='')
    if i == 2 or i == 5:
        print()
