while True:
    gender = input('Digite seu gênero [M/F]: ')
    if gender == 'M' or gender == 'F':
        print('OK')
        break
    else:
        print('Por favor, digite M ou F: ')
        