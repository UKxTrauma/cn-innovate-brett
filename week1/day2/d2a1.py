def numinput():
    usernum = input('Please enter any number:\n')
    if usernum.isnumeric():
        usernum = int(usernum)
        print(f'''You chose {usernum}, which was originally fed to me as a string but I have kindly converted it in to a {type(usernum)}! Have another go...\n''')
        numinput()
    else:
        print("C'mon now, that's not even a number xD Try again...\n")
        numinput()
numinput()