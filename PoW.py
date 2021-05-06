import random

    
def guessHash():
    userInput = input("Please enter a 3 digit Hash using capital letters, upper letters, symbols and numbers or write MENU to get back to main menu: ")
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
    userBalance = []
    
    if userHash == "MENU":
        userChoose()
    elif not int(len(userHash)) == 3:
        print("Plese neither use more nor less than 3gits to create the hash")
        run()
    else:
        print("You choose " + userHash)
        print("The new hash has been created: """ + hash)
        if userHash == hash:
            print("Great! You won!")
            userBalance.append(hash)
            return userBalance
        else:
            print("Keep trying!")
            run()
            return userBalance


def userChoose():
    print("""
1. Play
2. Check my balance""")
    userChoise = int(input("What do you wanna do?: "))
    
    if userChoise == 1:
        run()
    elif userChoise == 2: 
        print("Your current balance is: ")
        userChoose()
    else: 
        print("Please select a valid entry")
        userChoose()


if __name__ == '__main__':
    print("""
        Welcome to PoW simulator.
        You gotta guess what will be the next hash.
        If you do it then you'll be rewarded.
        Otherwise you gotta keep trying. 
    """)

userChoose()

    
    
