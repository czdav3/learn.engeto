"""
Bulls & Cows project
Author: David Tichý
"""

import random
import os

import projectVars as cfg


def main():
    greetings()
    gameRun(gameConfig())


def greetings():
    os.system('clear')
    print(
        'Hello there...',
        cfg.separator,
        'I\'ve generated a random 4 digit number for you.',
        'Let\'s play a bulls and cows game.',
        cfg.separator,
        sep='\n'
        )
    input('Press enter to start game...')
    

def generateRandomNumber() -> tuple:
    secretNumber = set()
    while len(secretNumber) < 4:
        secretNumber.add(random.randint(1, 9))
    return tuple((i) for i in secretNumber)


def gameConfig() -> dict:
    settings = {
        'secretNumber': generateRandomNumber(),
        'user': '',
        'run': True,
    }
    return settings


def gameRun(settings):
    while settings['run']:
        gameReuslts(tryNumber(settings), settings)


def tryNumber(settings: tuple):
    os.system('clear')
    rounds = 0
    step = 0
    while settings['run']:
        step += 1
        if step >= 25: cfg.tipPrint('endGame')
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
    print(tupNumber, secret, sep="\n")
    return True


def gameReuslts(steps, settings):
    os.system('clear')
    print(
        cfg.separator,
        f'You win in {steps} steps...',
        cfg.separator,
        sep="\n"
    )
    runGameAgain()


def runGameAgain():
    while True:
        reply = input('Play again? (yes/no)')
        if reply in ['yes', 'ye', 'y']:
            main()
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