s_m_18 = s_h = s_m_m_20 = 0

while True:
    gender = input("\nDigite o gênero da pessoa [M/F]: ").upper()
    old = int(input("Digite a idade da pessoa: "))
    
    if old > 18:
        s_m_18 += 1
    
    if gender == 'M':
        s_h += 1
        
    if gender == 'F' and old < 20:
        s_m_m_20 += 1
           
    on_off = input("\nVocê quer continuar [S/N]: ").upper()
    
    if on_off == 'N':
        break
    
print(f"{s_m_18} pessoa(s) com mais de 18 anos\n{s_h} homem(s)\n{s_m_m_20} mulher(es) com menos de 20 anos")