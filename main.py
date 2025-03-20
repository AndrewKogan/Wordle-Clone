import random
from os import system, name
from termcolor import colored
def create_word(): # chooses a random 5-letter word from the "Words" file
    words = []
    possibilities = open("Words.txt")
    for w in possibilities:
        words.append(w.rstrip())
    r = random.randint(0, len(words) - 1)
    possibilities.close()
    random_word = words[r]
    return random_word.upper()

def guess_word_compare(guess_letters, correct_letters):
    for i in range(5):
        dupe = ['nada']
        if guess_letters[i] == correct_letters[i]:
            #make green
            print(colored(guess_letters[i], 'green'), end = ' | ')
        else:
            yellow = False
            x = 0
            for b in range(5):
                if guess_letters[i] == correct_letters[b] and not(dupe[x] == guess_letters[i]):
                    #make yellow
                    print(colored(guess_letters[i], 'yellow'), end = ' | ')
                    dupe.append(guess_letters[i])
                    yellow = True
                    x = len(dupe) - 1
            if yellow == False:
                print(colored(guess_letters[i], 'grey'), end = ' | ')
#main program
print("Welcome to Word Guesser Game Party")
x = create_word()
correct_word_list = [letter for letter in x.upper()]
print()
print("You have 6 chances to guess the correct 5 letter word.")
print("Each letter in the word you guess will become either green, yellow, or gray.")
print()
print("Green means that the letter is in the word and is in the correct spot.")
print("Yellow means that the letter is in the word, but not in the correct spot.")
print("And gray means that the letter is not in the word. Good luck!")
print()
lives = 6
guess = "nada"
while lives > 0 and guess != x:
    guess = input("Guess a 5 letter word:")
    guess_list = [letter for letter in guess.upper()]
    while len(guess_list) != 5:
        print("That is not a 5 letter word")
        guess = input("Guess a 5 letter word:")
        guess_list = [letter for letter in guess.upper()]
    lives = lives - 1
    print(colored(lives,'red'), 'lives left')
    print('-------------------')
    guess_word_compare(guess_list, correct_word_list)
    print()
    print('-------------------')
    guess = guess.upper()
    if guess == x:
        print("You Win!")
    elif lives == 0:
        print("You Lose!")
        print("The word was:", x)
