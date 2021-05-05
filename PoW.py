import random


def guessHash():
    print("""
        PoW simulator.
        You gotta guess what will be the next hash.
        If you do it then you'll be rewarded.
        Otherwise you gotta keep trying. 
    """)
    userInput = input("Please enter a 3 digit Hash using capital letters, upper letters, symbols and numbers: ")
    return userInput

def hashCreation():
    capitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    upperLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',' v', 'w', 'x', 'y', 'z']
    symbols = ['!', '#', '$', '&', '/', '(', ')', '%', '?']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    setCharacters = capitalLetters + upperLetters + symbols + numbers

    hash = []

    for i in range(3):
        randomCharacter = random.choice(setCharacters)
        hash.append(randomCharacter)

    hash = "".join(hash)
    return hash


def run():
    hash = hashCreation()
    userHash = guessHash()
    print('You choose ' + userHash)
    print('The new hash has been created: ' + hash)


if __name__ == '__main__':
    run()
