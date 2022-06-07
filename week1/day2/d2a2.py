from random import choice as r

main_cast = [
'Angelina Jolie',
'James McAvoy',
'Morgan Freeman',
'Terence Stamp',
'Thomas Kretschmann',
'Common',
'Kristen Hager',
'Marc Warren',
"David O'Hara",
'Konstantin Khabenskiy',
'Dato Bakhtadze',
'Chris Pratt',
'Lorna Scott',
'Sophiya Haque',
'Brian Caspe',
"Mark O'Neal",
'Bridget McManus',
'Bob Ari',
]
director_and_writers = [
'Timur Bekmambetov',
'Michael Brandt',
'Derek Haas',
'Chris Morgan',
]
quotes = [
"Wesley: (sarcastically before shooting a victim) I'm sorry!", #0
'''Barry: [after Wesley rants at Janice] Yeah, that was great, bro! Who's the man?\n
(Wesley smashes his keyboard against Barry's face. Bloodstained keys fly past spelling "FUCK YO", the final "U" being one of his molars)\n
Wesley: I'm the man!''', #1
'''Wesley: [voice-over] You know when you have a dream and you're half-awake, but still in the fringe of your brain, and when you open your eyes you're so damn glad it was a dream?\n
(gun falls out of Wesley's pants)\nWesley: [voice-over] This was nothing like that.''', #2
"Wesley: [to Sloan] Do you make sweaters, or do you kill people?" #3
]
def imdb_rand():
    global running
    user_input = input("Please choose between a random cast member, director/writer or a quote from the 2008 movie Wanted:\n[A] Cast Member\n[B] Write/Director\n[C] Quote\n").upper()
    if user_input == 'A':
        print(r(main_cast))
        again = input('Would you like another go?\n[Y]\n[N]\n').upper()
        if again == 'Y':
            imdb_rand()
        elif again == 'N':
            ("Thanks for trying me out.")
            running = False
        else:
            print("I didn't catch that! I'll take you back to the start.")
            imdb_rand()
    elif user_input == 'B':
        print(r(director_and_writers))
        again = input('Would you like another go?\n[Y]\n[N]\n').upper()
        if again == 'Y':
            imdb_rand()
        elif again == 'N':
            ("Thanks for trying me out.")
            running = False
        else:
            print("I didn't catch that! I'll take you back to the start.")
            imdb_rand()
    elif user_input == 'C':
        print(r(quotes))
        again = input('Would you like another go?\n[Y]\n[N]\n').upper()
        if again == 'Y':
            imdb_rand()
        elif again == 'N':
            ("Thanks for trying me out.")
            running = False
        else:
            print("I didn't catch that! I'll take you back to the start.")
            imdb_rand()
    else:
        print("I didn't catch that! Please try again, this time with the letter 'A', 'B, or 'C'.")
        imdb_rand()
running = True
while running:
    imdb_rand()