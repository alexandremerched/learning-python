n = int(input("Digite um número: "))
d = 0

for i in range(1, n+1):
    if n % i == 0:
        print('\033[32m', end='')
        d += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(n, d))

if n == 2:
    print("ele é PRIMO")
else:
    print("ele não é PRIMO")
