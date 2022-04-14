"""
Bulls & Cows project
Author: David Tichý
"""

import random
import os
import time
from typing import Dict

import projectVars as cfg


def main(*args: bool):
    """
    Main controller...
    """
    if not args:
        greetings()
        gameMenu()
    gameRun(gameConfig())


def setUserData(data: None or Dict, controll: bool):
    """
    Nastavení uživatele, pokud existuje

    Args:
        data (None or Dict): Pokud neexistuje = NONE, pokud existuje = data ve slovníku
        controll (bool): Controller pro přihlásit / nepřihlásit
    """
    global userData
    if controll:
        userData = {
                'user': data[0].upper(),
                'steps': data[1],
                'games': data[2],
                'wins': data[3],
                'loss': data[4],
                'loggedIn': True,
            }
    else: userData = {'loggedIn': False}
    return True


def selectUser():
    """
    Hledá a vytahuje uživatele pokud existuje v souboru userData.txt
    """
    usersFile = open('userData.txt', 'r+')
    userInput = loginUserForm()
    for line in usersFile.readlines():
        lineSplit = line.split(',')
        if lineSplit[0].lower() == userInput:
            setUserData(lineSplit, True)
            print('You are logged...')
            time.sleep(3)
            return True
        else: setUserData(None, False)
    print('This user not exists...')
    time.sleep(3)
    return True


def loginUserForm() -> str:
    """
    Zadání uživatelského jména

    Returns:
        str: vrací zadanou hodnotu
    """
    return input('User name: ').lower()


def greetings():
    """
    Pozdravení uživatele...
    """
    os.system('clear')
    print(
        'Hello there...',
        cfg.separator,
        'I\'ve generated a random 4 digit number for you.',
        'Let\'s play a bulls and cows game.',
        cfg.separator,
        'If you want login to your account, type "login"...',
        sep='\n'
        )


def gameMenu():
    """
    Menu - výběr akce...
    """
    print(
        'Type any value: [start, login, help, end]',
        cfg.separator,
        sep="\n"
    )
    select = input('Your choice: ').lower()
    if select in ['start', 's', 'run', 'play']: setUserData(None, False)
    elif select in ['login', 'user', 'acc']: selectUser()
    elif select in ['help', 'h']: cfg.help()
    elif select in ['end', 'e', 'exit', 'quit', 'close', 'break']: breakGame()
    else: os.system('clear'), print('Invalid value...'), gameMenu()


def generateRandomNumber() -> tuple:
    """
    Generování náhodného čísla pro hru...
    Prvně jako SET kvůli omezení duplicit, poté převádí a vrací tuple.

    Returns:
        tuple: Vrací tuple se 4 indexi - každý index obsahuje 1 číslo
    """
    secretNumber = set()
    while len(secretNumber) < 4:
        secretNumber.add(random.randint(1, 9))
    return tuple((i) for i in secretNumber)


def gameConfig() -> dict:
    """
    Nastavení hry - generování čísla, idikace rozjeté hry...
    """
    settings = {
        'secretNumber': generateRandomNumber(),
        'run': True,
    }
    return settings


def gameRun(settings):
    """
    Cyklus hry

    Args:
        settings dict('run'): indikace rozjeté hry, nastavuje ve funkci gameConfig()
    """
    while settings['run']:
        gameReuslts(tryNumber(settings), settings)


# def tryNumberError(step: int, e: str):
#     os.system('clear')
#     step += 5
#     return step, cfg.erPrint(e)


def userInterface():
    """
    Pokud je uživatel registrován a přihlášen, vypisuje jeho data:
    Jméno uživatele | celkové kroky | celkové hry | výhry | prohry
    """
    if userData['loggedIn']:
        print(
            f'User: {userData["user"]}',
            f'Steps: {userData["steps"]}',
            f'Games: {userData["games"]}',
            f'Wins: {userData["wins"]}',
            f'Loss: {userData["loss"]}',
            sep='  |  ',
        )
        cfg.separator
    return True


def tryNumber(settings: tuple):
    """
    Funkce hádání čísla.

    Args:
        settings (tuple): nastavení hry

    Returns:
        [type]: [description]
    """
    os.system('clear')
    rounds = 0
    step = 0
    while settings['run']:
        step += 1
        if step >= 25: cfg.tipPrint('endGame')
        userInterface()
        typeNumber = input('Type number (4): ')

        if not typeNumber.isnumeric():
            os.system('clear')
            cfg.erPrint('notNumeric')
            step += 5
            continue

        elif not len(typeNumber) == 4:
            os.system('clear')
            cfg.erPrint('notFourChars')
            step += 5
            continue

        elif typeNumber == '0000':
            breakGame()

        elif '0' in typeNumber:
            os.system('clear')
            cfg.erPrint('zeroInclude')
            step += 5
            continue

        elif len(set((char) for char in typeNumber)) < 4:
            os.system('clear')
            cfg.erPrint('sameNums')
            step += 5
            continue

        else:
            rounds += 1
            os.system('clear')
            settings['run'] = compareNumbers(typeNumber, settings['secretNumber'])

    return rounds


def compareNumbers(number: str, secret: tuple):
    step = 0
    tupNumber = tuple((int(i)) for i in number)
    process = {'match': 0, 'exist': 0}
    os.system('clear')
    print(f'Typed number: {number}')
    while step < 4:
        if tupNumber == secret:
            return False
        elif tupNumber[step] == secret[step]:
            process['match'] += 1
        elif tupNumber[step] != secret[step] and tupNumber[step] in secret:
            process['exist'] += 1
        step += 1
    print(
        f'Match: {process["match"]}',
        f'Exist: {process["exist"]}',
        sep="\n"
    )
    return True


def gameReuslts(steps, settings):
    os.system('clear')
    print(
        cfg.separator,
        f'You win in {steps} steps...',
        settings['secretNumber'],
        cfg.separator,
        sep="\n"
    )
    runGameAgain()


def runGameAgain():
    while True:
        reply = input('Play again? (yes/no)')
        if reply in ['yes', 'ye', 'y']:
            main(user['loggedIn'])
        elif reply in ['no', 'n']:
            os.system('clear')
            breakGame()


def breakGame():
    print(
        cfg.separator,
        'End game, thank you for your time... :)',
        cfg.separator,
        sep="\n"
    )
    quit()


main()