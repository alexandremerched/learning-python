a = input('Digite algo: ')


def yorn(boolean):
    if boolean is True:
        return "sim"
    else:
        return "não"


print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', yorn(a.isspace()))
print('É um número?', yorn(a.isnumeric()))
print('É alfabético?', yorn(a.isalpha()))
print('É alfanúmerico?', yorn(a.isalnum()))
print('Está em maiúculas?', yorn(a.isupper()))
print('Está em minúsculas?', yorn(a.islower()))
print('Ésta capitalizada?', yorn(a.istitle()))
