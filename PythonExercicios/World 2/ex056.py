m_old = 0
man_name = ''
man_old = 0
c_woman = 0

for i in range(1, 5):
    print("----- {}ª PESSOA -----".format(i))
    name = input("Nome: ")
    old = int(input("Idade: "))
    gender = input("Sexo [M/F]: ")
    
    m_old += old
    
    if gender == 'M' and old > man_old:
        man_name = name
        man_old = old 
    if gender == 'F' and old < 20:
        c_woman += 1
    
print("""
A média de idade do grupo é de {} anos
O homem mais velho tem {} anos e se chama {}
Ao todo são {} mulher(es) com menos de 20 anos""".format(m_old / 4, man_old, man_name, c_woman))