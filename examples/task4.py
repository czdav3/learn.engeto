# Ukladani jmena
jmeno = input('Zadej jméno: ')

# Tisk jmena
print(f'Ukládám "{jmeno}" do var jmeno...')

# Ukladani prijmeni
prijmeni = input('Zadej příjmení: ')

# Tisk prijmeni
print(f'Ukládám "{prijmeni}" do var prijmeni...')

# Vytvoreni a tisk promenne cele_jmeno
cele_jmeno = jmeno + ' ' + prijmeni
print(f'Celé jméno: {cele_jmeno}')

# Vytvoreni a tisk promenne delka_jmena
pocet = len(cele_jmeno)
print(f'Délka jména: {pocet}')

# Tisk ohranicene promenne cele_jmeno
print('=' * 10)
print(cele_jmeno)
print('=' * 10)
