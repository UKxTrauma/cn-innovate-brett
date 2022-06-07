alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]
for letter in alphabet:
    print(letter)

def numinput():
    usernum = input('Please enter a number from 1 to 26:\n')
    if usernum.isnumeric() == True:
        usernum = int(usernum)
        if usernum in range(1,27):
            print(f"You chose {usernum}, which corresponds to the letter {alphabet[usernum-1].upper()}! Have another go...\n")
            numinput()
        else:
            print("Pretty sure that wasn't one of your options xD Try again...\n")
            numinput()
    else:
        print("C'mon now, that's not even a number xD Try again...\n")
        numinput()
numinput()