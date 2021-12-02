separator = '-' * 40
colRed = '\033[31m'
colBlue = '\033[34m'
colWhite = '\033[0m'

tipsMsgs = {
    'endGame': f'{colBlue}** Tip: If you type 0000, end the game... **{colWhite}',
}

errorMsgs = {
    'notNumeric': f'{colRed}!! Warning: Not isnumeric() please type again... !!{colWhite}',
    'notFourChars': f'{colRed}!! Warning: Not len() == 4, please type again... !!{colWhite}',
    'zeroInclude': f'{colRed}!! Warning: typeNumber var have zero... !!{colWhite}',
    'sameNums': f'{colRed}!! Warning: typeNumber var have same numbers... !!{colWhite}',
}

def erPrint(where: str) -> print:
    return print(errorMsgs[where])

def tipPrint(where: str) -> print:
    return print(tipsMsgs[where])