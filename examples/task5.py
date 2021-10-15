# vstupni hodnoty
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

# uvitani uzivatele
print('VITEJTE U NASI APLIKACE DESTINATIO!')
print(cara)
print(nabidka)
print(cara)

# vkladani udaju
destinace = int(input('Zvol destinaci: ')) - 1
jmeno = input('Jméno: ')
prijmeni = input('Příjmení: ')
email = input('Váš email: ')

# uprava zadanych hodnot

# vypisovani vystupu
print(f"""{cara}
DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {mesta[destinace]}, CENA JIZDNEHO: {ceny[destinace]},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.
{cara}""")
