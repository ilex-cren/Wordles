# Wordle game in Kapampangan
import re
import random
from colorama import init, Fore, Back, Style
init()

f = open("sgb-words.txt")

def print_green(s, color=Fore.GREEN, brightness=Style.NORMAL, **kwargs):
    x = f"{brightness}{color}{s}{Style.RESET_ALL}"
    return x

def print_yellow(s, color=Fore.YELLOW, brightness=Style.NORMAL, **kwargs):
    x = f"{brightness}{color}{s}{Style.RESET_ALL}"
    return x

text = f.readlines()
words = [x.rstrip() for x in text]

wordle_list = []
for word in words:
    wordle_list.append(word.strip())

random_wordle = random.choice(wordle_list)

def game_round(n):
    print(">Try #{}<".format(str(n)))
    print("Guess the 5-letter word:")
    guess = input()
    def verify_guess(guess):
        if len(guess) != 5:
             print("Please enter a five-letter word!")
             guess = input()
             verify_guess(guess)
        elif guess not in wordle_list:
            print("Word not recognized.")
            guess = input()
            verify_guess(guess)
        return guess
    guess = verify_guess(guess)
    if guess == random_wordle:
       print(print_green(guess))
       print("Yay! you won!")
    else:
       guess_split = [char for char in guess] 
       wordle_split = [char for char in random_wordle]
       number_green = 0  # number of chars in the correct place
       number_yellow = 0 # number of chars in the word but in the wrong place
       for i in range(len(guess_split)):
          if guess_split[i] == wordle_split[i]:
              number_green += 1
          elif guess_split[i] in wordle_split:
              number_yellow +=1
       guess = ''.join(guess_split)
       print(print_green(str(number_green)), print_yellow(str(number_yellow)))
       if n <12:
           game_round(n+1)
       else:
           print("Game over! The word was", print_green(random_wordle))
            
game_round(1)
f.close()

