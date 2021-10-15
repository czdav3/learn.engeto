import pprint

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

users = {
    'bob': 123,
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}

SEPARATOR = '-' * 40

user = input('Account: ')
psw = input('Password: ')

# BYPASS LOGIN
# user = 'bob'
# psw = '123'
##############

if user in users.keys() and str(users[user]) == psw:
    print(SEPARATOR)
    print(
        f'Logged...', 
        f'Welcome {user}, how are you?',
        sep="\n"
    )
    print(SEPARATOR)
else:
    print(SEPARATOR)
    print(f'Wrong acc or psw. Program die...')
    print(SEPARATOR)
    quit()

for text in TEXTS:
    print(f'TEXT [{TEXTS.index(text) + 1}]: {text[:30]}...')

select = input('Please, select your text: ')

# BYPASS SELECT TEXT
# select = '1'
##############

print(SEPARATOR)

if not select.isdigit():
    print(SEPARATOR)
    print('Wrong! Input not a number. Program die...')
    print(SEPARATOR)
    quit()

fixedSelect = int(select) - 1
textsLength = len(TEXTS) - 1

# DEBUG fixedSelect
# print(fixedSelect)
# quit()

if fixedSelect > textsLength:
    print(SEPARATOR)
    print('Wrong! This text not exist. Program die...')
    print(SEPARATOR)
    quit()

selectedText = TEXTS[fixedSelect]
wordsList = selectedText.split()
wordsCount = len(wordsList)
uppercaseWords = []
upperWords = []
lowercaseWords = []
numericWords = [] 

for word in wordsList:
    if word[0].isupper():
        uppercaseWords.append(word)

    if word.isupper():
        upperWords.append(word)

    if word.islower():
        lowercaseWords.append(word)

    if word.isnumeric():
        numericWords.append(int(word))

print(
    f'There are {wordsCount} words in the selected text.',
    f'There are {len(uppercaseWords)} titlecase words.',
    f'There are {len(upperWords)} uppercase words.',
    f'There are {len(lowercaseWords)} lowercase words.',
    f'There are {len(numericWords)} numeric strings.',
    f'The sum o all numbers {sum(numericWords)}.',
    sep="\n"
)

lengthWords = {}

for word in wordsList:
    lenght = len(word)
    if lenght not in lengthWords:
        lengthWords[lenght] = 1
        # print(f'Vytvořil jsem dict {lenght}')
    else:
        lengthWords[lenght] = lengthWords[lenght] + 1
        # print(f'Přičetl jsem do {lenght} plus 1 slovo')

maxStars = sorted(list(lengthWords.values()), reverse=True)[:1]
maxStarsNum = maxStars[0]

print(SEPARATOR)
print(
    f'{"LEN|": >5}',
    f'{"OCCURENCES": <25}',
    f'{"|NR.": <3}'
    )
print(SEPARATOR)

for position in sorted(lengthWords.keys()):
    stars = '*' * lengthWords[position]
    
    print(
        f'{position: >4}|',
        f'{stars: <25}',
        f'|{lengthWords[position]: <3}'
    )
