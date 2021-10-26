# 
# Rock, Paper, Scissors, Lizard, Spock Game
# Author: David 'CzDaV3' Tichý
# 

import os
import random

clear = lambda: os.system('clear')

roundCount = 0
winCount = 0
printLine = '=' * 50
keepPlaying = True
playebleActions = ('rock', 'paper', 'scissors', 'lizard', 'spock')
keepAttempts = 0

clear()
print(
    f'',
    printLine,
    f'Rock, Paper, Scissors, Lizard, Spock Game'.center(len(printLine)),
    printLine,
    f'',
    sep='\n'
)

player = input('What\'s your name? ')
# Bypass input select name
# player = 'David'

while keepPlaying:

    selectAttempts = 0
    while selectAttempts < 3:
        playerAction = input('Select an action: ')
        roundCount = roundCount + 1
        if(playerAction in playebleActions):
            break
        else:
            selectAttempts = selectAttempts + 1
            print(f'Bad select ({selectAttempts} / 3). Please again...')
            if(selectAttempts == 3):
                print('Too much wrong selects...')
                quit()

    aiAction = random.choice(playebleActions)

    print(
        f'AI select: {aiAction}',
        sep='\n'
    )

    if(playerAction == 'scissors' and aiAction == 'paper'):
        print('\nScissors cuts Paper\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'paper' and aiAction == 'rock'):
        print('\nPaper covers Rock\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'rock' and aiAction == 'lizard'):
        print('\nRock crushes Lizard\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'lizard' and aiAction == 'spock'):
        print('\nLizard poisons Spock\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'spock' and aiAction == 'scissors'):
        print('\nSpock smashes Scissors\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'scissors' and aiAction == 'lizard'):
        print('\nScissors decapitates Lizard\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'lizard' and aiAction == 'paper'):
        print('\nLizard eats Paper\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'paper' and aiAction == 'spock'):
        print('\nPaper disproves Spock\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'spock' and aiAction == 'rock'):
        print('\nSpock vaporizes Rock\nYou win...\n')
        winCount = winCount + 1
    elif(playerAction == 'rock' and aiAction == 'scissors'):
        print('\nRock crushes Scissors\nYou win...\n')
        winCount = winCount + 1

    elif(aiAction == 'scissors' and playerAction == 'paper'):
        print('\nScissors cuts Paper\nYou lose...\n')
    elif(aiAction == 'paper' and playerAction == 'rock'):
        print('\nPaper covers Rock\nYou lose...\n')
    elif(aiAction == 'rock' and playerAction == 'lizard'):
        print('\nRock crushes Lizard\nYou lose...\n')
    elif(aiAction == 'lizard' and playerAction == 'spock'):
        print('\nLizard poisons Spock\nYou lose...\n')
    elif(aiAction == 'spock' and playerAction == 'scissors'):
        print('\nSpock smashes Scissors\nYou lose...\n')
    elif(aiAction == 'scissors' and playerAction == 'lizard'):
        print('\nScissors decapitates Lizard\nYou lose...\n')
    elif(aiAction == 'lizard' and playerAction == 'paper'):
        print('\nLizard eats Paper\nYou lose...\n')
    elif(aiAction == 'paper' and playerAction == 'spock'):
        print('\nPaper disproves Spock\nYou lose...\n')
    elif(aiAction == 'spock' and playerAction == 'rock'):
        print('\nSpock vaporizes Rock\nYou lose...\n')
    elif(aiAction == 'rock' and playerAction == 'scissors'):
        print('\nRock crushes Scissors\nYou lose...\n')

    elif(playerAction == aiAction):
        print('\nSame select.\nTry again?\n')
        roundCount = roundCount - 1

    print(
        f'SCORE:',
        f'{player} wins: {winCount} - AI wins: {roundCount - winCount}',
        f'',
        sep='\n'
    )

    # Keep playing function
    print('Keep playing?')
    print(
        'If you continue in play, enter "yes" or "y".',
        'Otherwise, enter "no" or "n".',
        sep='\n'
    )

    while True:
        keepPlayingAnswer = input()
        if(keepPlayingAnswer.lower() in ['yes', 'y']):
            keepPlaying = True
            clear()
            break
        elif(keepPlayingAnswer.lower() in ['no', 'n']):
            print('Good game. Good bye... :)')
            keepPlaying = False
            break
        else:
            keepAttempts = keepAttempts + 1
            print(f'Wrong input ({keepAttempts} / 3). Try again.')
            if(keepAttempts == 3):
                print('Too much wrong inputs...')
                quit()