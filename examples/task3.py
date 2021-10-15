string = 'indexování'

# Extrahuj a vytiskni prvních 5 písmen
prvnich_pet = string[:5]
print(f'Prvních 5 písmen: {prvnich_pet}')

# Extrahuj a vytiskni posledních 5 písmen
poslednich_pet = string[5:]
print(f'Posledních 5 písmen: {poslednich_pet}')

# Extrahuj a vytiskni každé 3 písmeno
kazde_treti = string[::3]
print(f'Každé 3. písmeno (počínaje prvním): {kazde_treti}')
