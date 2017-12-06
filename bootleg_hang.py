#This is going to be a very bootleg version of hang man it might not even be done
import time

#varibles

word = "jazz man"
guesses = ''
turns = 10

#functions
def did_win(word, guesses):
    failed = 0
    for char in word:
        if char in guesses:
            print (char),
        else:
            print ("_"),
            failed += 1
    if failed == 0:        
        print ("You won")
        reasult = 1
        playing = 0

def did_lose(guesses,word,turns):
    recent_guess = input("guess a character or the word, but if you guess the word you only get one guess:")
    guesses += recent_guess                    
    if recent_guess not in word:
        if len(recent_guess) >= 2:
            if recent_guess != word:
                print("That's not my word.")
                turns = 0
            else:
                print("Hey that's my word!, You win!")
                reasult = 1
                playing = 0
        else:
            turns -= 1        
            print ("Wrong")   
            print ("You have", + turns, 'more guesses') 
        if turns == 0:           
            print ("You Lose")
            reasult = 0
            playing = 0

def get_name():
    name = input("What is your name? ")
    print ("Hello, " + name + ", Time to play hangman!")
    print (" ")
    time.sleep(1)
    print ("Start guessing...")
    time.sleep(0.5)

def play(turns, word, guesses):
    playing = 1
    while playing == 1:
        did_win(word, guesses)
        did_lose(guesses,word,turns)
    return reasult

def give_word(reasult, word):
    if reasult == 0:
        print("My word is, '" + word + "'")
    else:
        print(" ")
    

#game starts here
get_name()
reasult = play(turns, word, guesses)
give_word(reasult, word)
