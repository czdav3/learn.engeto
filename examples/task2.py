# Cenik
mercedes    = 150000
rolls_royce = '400000'
vybava = 50000

dva_mb = mercedes * 2
mbrr = mercedes + int(rolls_royce)
better_rr = (int(rolls_royce) + vybava) + (int(rolls_royce) + vybava)
better_mb = mercedes + vybava
discount = input('Zadejte slevu MB: ')

print(f'Cena za dva MB: {dva_mb}')
print(f'Cena za MB a Rolls-Royce: {mbrr}')
print(f'Cena za dva Rolls-Royce s výbavou: {better_rr}')
print(f'Cena za MB s výbavou: {better_mb}')
print(f'Cena za MB po slevě: {mercedes - int(discount)}')
