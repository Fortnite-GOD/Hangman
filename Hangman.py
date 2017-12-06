
#Dunlap, Chase
#11/10/2017
#This is hangman... Need I say more?

import random
import os

#functions
def get_choice():
    while True:
        print("(1) Make a word up and have your friend guess it")
        print("(2) Pick from a selection of catagories and guess a word that the computer gives you.")
        choice = input()

        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        else:
            print("Please put 1 or 2")
            print(" ")

def intro():
    print(""" _  _  _, _, _ _, _  _,   __, _,   _, , _   _,_  _, _, _  _, _, _  _, _, _
 |  | /_\ |\ | |\ | /_\   |_) |   /_\ \ |   |_| / \ |\ | / _ |\/| /_\ |\ |
 |/\| | | | \| | \| | |   |   | , | |  \|   | | |~| | \| \ / |  | | | | \|
 ~  ~ ~ ~ ~  ~ ~  ~ ~ ~   ~   ~~~ ~ ~   )   ~ ~ ~ ~ ~  ~  ~  ~  ~ ~ ~ ~  ~
                                       ~' """)

def get_name():
    print("Hey what's your name?")
    name = input()
    return name

def nor_puzzle():
    print("Alright, you're about to play hangman.")
    print(" ")
    print("Put a word down for you're friend to guess don't let them see it.")
    puzzle = input()
    puzzle = puzzle.lower()
    print("""












































      """)
    return puzzle

def comp_puzzle():
    file_names = os.listdir('data')

    for i, f in enumerate(file_names):
        print(str(i) + ") " + f)

    choice = input("Which one?")
    choice = int(choice)

    file = "data/" + file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    category = lines[0]
    puzzle = random.choice(lines[1:])

    return puzzle

            
def get_solved(puzzle, guesses):
    solved = ""
    special_characters = " !@#$%^&*()_+{}|:\"?><,./1234567890-=[];'\\`"

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        elif letter in special_characters:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    alphabet = "abcdefghijklmanopqrstuvwxyz"
    while True:
        guess = input("Take a Guess:")
        guess = guess.lower()
        if len(guess) >= 2:
            print("Please type 1 letter only")
        elif guess not in alphabet:
            print("Please put a letter.")
        else:
            return guess

def get_image(turns):
    if turns == 6:
        image = ("""___________
    |         |
    |         
    |        
    |        
    |
    |
    _____________""")
    elif turns == 5:
        image = ("""    ___________
    |         |
    |         0
    |      
    |        
    |
    |
    _____________""")
    elif turns == 4:
        image = ("""    ___________
    |         |
    |         0
    |         |
    |        
    |
    |
    _____________""")
    elif turns == 3:
        image = ("""    ___________
    |         |
    |         0
    |        /|
    |        
    |
    |
    _____________""")
    elif turns == 2:
        image = ("""    ___________
    |         |
    |         0
    |        /|\\
    |
    |
    |
    _____________""")
    elif turns == 1:
        image = ("""    ___________
    |         |
    |         0
    |        /|\\
    |        /
    |
    |
    _______________""")
    else:
        image = ("""    ___________
    |         |
    |         0
    |        /|\\
    |        / \\
    |
    |
    _______________""")
    return image

    

def display_board(solved, used, image):
    print(" ")
    print(solved)
    print(" ")
    print("Used letters:")
    print(used)
    print(" ")
    print(image)
    

def show_result(turns, puzzle):
    if turns == 0:
        print("You lose you normie. REEEEEEEEEEEEE!")
        print("The word was " + puzzle + ".")
    else:
        print("You Win!")

def play_again(player_name):
    while True:
        print(" ")
        decision = input("Would you like to play again, " + player_name + "? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print(" ")
            print("I don't understand. Please enter 'y' or 'n'.")

def play(choice):

    if choice == 1:
        puzzle = nor_puzzle()
    elif choice == 2:
        puzzle = comp_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    turns = 6
    used = ""

    print(solved)

    while solved != puzzle and turns != 0:
        letter = get_guess()
        used += letter

        if letter not in puzzle:
            print("Wrong")
            turns -= 1

        guesses += letter
        solved = get_solved(puzzle, guesses)
        image = get_image(turns)
        display_board(solved, used, image)
        
    show_result(turns, puzzle)

def end():
    print("""  _, _,_  _,  _, __,   __, _,_ _, _ _,   _, __,   , ,    ,  _,     _, _  , __,
 / ` |_| /_\ (_  |_    | \ | | |\ | |   /_\ |_)   | |  / | |_   / ~ )/ \ | _/ 
 \ , | | | | , ) |     |_/ | | | \| | , | | |     | | /  |   ) /   / \ / | /~ 
  ~  ~ ~ ~ ~  ~  ~~~   ~   `~' ~  ~ ~~~ ~ ~ ~     ~ ~    ~ ~~     ~~~ ~  ~    """)

#game starts here

intro()

choice = get_choice()

player_name = get_name()

playing = True

while playing:
    play(choice)
    playing = play_again(player_name)

end()

