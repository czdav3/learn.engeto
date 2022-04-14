"""
Bulls & Cows project
Author: David Tichý
"""

import random
import os
import time
from typing import Dict

import projectVars as cfg

def __main__(*args: bool):
    """
    Hlavní controller
    """

    if not args:
        greetings()
        gameMenu()


def greetings():
    """
    Pozdravení uživatele
    """
    os.system('clear')
    return print(
        'Ahoj...',
        cfg.separator,
        'Vygeneruji ti 4 náhodné čísla, které musíš uhodnout.',
        'Můžeme začít hrát hru Bulls and Cows?',
        cfg.separator,
        'Jestli jsi stálý hráč, můžeš se přihlásit pomocí příkazu "login".',
        sep="\n"
    )


def gameMenu():
    """
    Herní menu - výběr akce
    """
    print(
        'Zvol jednu z možností: [start, login, help, end]',
        cfg.separator,
        sep="\n"
    )
    select = input('Zvol: ').lower()
    if select in ['start', 's', 'run', 'play']: start(setUserData(None))
    elif select in ['login', 'user', 'acc']: start(login())
    elif select in ['help', 'h']: os.system('clear'), cfg.help(), gameMenu()
    elif select in ['end', 'e', 'exit', 'quit', 'close', 'break']: breakGame()
    else: os.system('clear'), print('Neplatná volba...'), gameMenu()


def login():
    os.system('clear')
    userFile = open('userData.txt', 'r+')
    userInput = input('Uživatelské jméno: ').lower()
    for line in userFile.readlines():
        lineSplit = line.split(';')
        if lineSplit[0].lower() == userInput:
            return setUserData(lineSplit)
    if(input('Neznámý uživatel, chcete to zkusit znovu? [y, n] ').lower() == 'y'):
        login()
    return setUserData(None)


def setUserData(data: None or Dict):
    userData = {
        'user': 'NEPŘIHLÁŠENÝ HRÁČ',
        'steps': 0,
        'games': 0,
        'wins': 0,
        'register': True,
    }
    if data:
        userData = {
            'user': data[0].upper(),
            'steps': data[1],
            'games': data[2],
            'wins': data[3],
            'register': False,
        }
        return userData
    return userData


def generateRandomNumber():
    secretNumber = set()
    while len(secretNumber) < 4:
        secretNumber.add(random.randint(1, 9))
    return tuple((i) for i in secretNumber)


def start(userData: None or Dict):
    cont = True
    userData['games'] += 1
    rndNum = generateRandomNumber()
    os.system('clear')
    while True:
        userInterface(userData)
        print(rndNum)

        if compareNumber(validNumber(), rndNum):
            userData['steps'] += 1
            userData['wins'] += 1
            if(gameContinue(userData)): start(userData)
        elif compareNumber(validNumber(), rndNum) == 'break':
            gameContinue(userData)

        userData['steps'] += 1


def compareNumber(number, secret):
    step = 0
    tupNumber = tuple((int(i)) for i in number)
    process = {'match': 0, 'exist': 0}
    os.system('clear')
    print(f'Zadané číslo: {number}')
    while step < 4:
        if tupNumber == secret:
            return True
        elif tupNumber[step] == secret[step]:
            process['match'] += 1
        elif tupNumber[step] != secret[step] and tupNumber[step] in secret:
            process['exist'] += 1
        step += 1
    print(
        f'Trefa: {process["match"]}',
        f'Existuje: {process["exist"]}',
        cfg.separator,
        sep="\n"
    )
    return False


def validNumber():
    while True:
        number = input('Hádej číslo (4): ')
        if not number.isnumeric():
            os.system('clear')
            cfg.erPrint('notNumeric')

        elif not len(number) == 4:
            os.system('clear')
            cfg.erPrint('notFourChars')

        elif number == '0000':
            return 'break'

        elif '0' in number:
            os.system('clear')
            cfg.erPrint('zeroInclude')

        elif len (set((char) for char in number)) < 4:
            os.system('clear')
            cfg.erPrint('sameNums')

        else:
            return number

def userInterface(userData: Dict):
    print(
        f'User: {userData["user"]}',
        f'Steps: {userData["steps"]}',
        f'Games: {userData["games"]}',
        f'Wins: {userData["wins"]}',
        sep='  |  ',
    )
    cfg.separator
    return True


def gameContinue(userData):
    if(input('Chcete pokračovat? [y, n]').lower() == 'y'): return True
    else: 
        if(userData['register'] and input('Chcete výsledky uložit jako nového uživatele? [y, n]').lower() == 'y'):
            userRegister()
            print('Byl jsi uložen...')
            return False
        else:
            breakGame()
    return False


def userRegister():
    userFile = open('userData.txt', 'r+')
    users = []
    for line in userFile.readlines():
        if line[-1] != '\n':
            line += '\n'
        users.append(line)
    newName = input('Zadej své jméno: ')
    newUser = newName + ';0;0;0;0\n'
    users.append(newUser)
    userFile = open('userData.txt', 'w+')
    userFile.writelines(users)
    return True


def breakGame():
    print(
        cfg.separator,
        'Konec hry. Děkuji ti za tvůj čas... :)',
        cfg.separator,
        sep="\n"
    )
    return quit()

__main__()