"""
Bulls & Cows project
Autor: David Tichý
"""

import random
import os
import time

import projectVars as cfg


def main(*args: bool):
    """
    Hlavní spouštěč programu...
    """

    greetings()
    setGameConfig()
    menu()


def greetings():
    """
    Pozdravení hráče...
    """

    os.system('clear')
    print(
        'Vítej ve hře Bulls & Cows...',
        cfg.separator,
        'Vygeneruji 4 náhodné čísla (bez duplicit).',
        'Ty musíš uhodnout které čísla a jejich pořadí.',
        'Tak co? Jsi připraven na hru?',
        cfg.separator,
        sep='\n'
    )


def menu():
    """
    Herní menu, na výběr z možností:
        start = začít hru
        login = načíst uživatelské data a hrát za uživatele
        help = pravidla hry a možnosti programu
        end = ukončení hry
    """

    print(
        'Zvol některou z možností: [start, login, help, end]',
        cfg.separator,
        sep="\n"
    )
    select = input('Zvol možnost: ').lower()
    if select in ['start', 's', 'run', 'play']: pass
    elif select in ['login', 'user', 'acc']: login()
    elif select in ['help', 'h']: help()
    elif select in ['end', 'e', 'exit', 'quit', 'close', 'break']: endGame()
    else: os.system('clear'), print('Nesprávný výběr, zkus to prosím znovu...'), menu()


def setGameConfig() -> dict:
    """
    Nastavení herních dat jako uživatel, tajné číslo apod...
    """
    global gameConfig
    gameConfig = {
        'secretNumber': None,
        'user': None,
        'steps': None,
        'games': None,
        'wins': None,
        'loss': None,
        'loggedIn': False,
    }


def generateSecretNumber() -> tuple:
    """
    Generování náhodného čísla pro hru...
    Prvně jako SET kvůli omezení duplicit, poté převádí a vrací tuple.

    Returns:
        tuple: Vrací tuple se 4 indexi - každý index obsahuje 1 číslo
    """
    secretNumber = set()
    while len(secretNumber) < 4:
        secretNumber.add(random.randint(1, 9))
    gameConfig['secretNumber'] = tuple((i) for i in secretNumber)


def login():
    pass


def endGame():
    """
    Ukončení programu.
    """
    print(
        cfg.separator,
        'Konec hry, díky za tvůj čas. :)',
        cfg.separator,
        sep="\n"
    )
    quit()


def help():
    """
    Výpis pravidel a nápovědy programu...
    """
    menu()

main()

