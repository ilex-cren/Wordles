import re
import random
from colorama import init, Fore, Back, Style
init()

pam = open("pam_wiki.txt")
eng = open("sgb-words.txt")

def print_green(s, color=Back.GREEN, brightness=Style.NORMAL, **kwargs):
    x = f"{brightness}{color}{s}{Style.RESET_ALL}"
    return x

def print_yellow(s, color=Back.YELLOW, brightness=Style.NORMAL, **kwargs):
    x = f"{brightness}{color}{s}{Style.RESET_ALL}"
    return x

# get list of all 5-letter words in Kapampangan corpus:
all_lines = [line.rstrip() for line in pam.readlines()]
all_words = []
for line in all_lines:
    for w in line.split(' '):
        all_words.append(w)
all_5_words = []
for w in all_words:
    w = w.lower()
    if len(w) == 5 and str.isalpha(w):
       all_5_words.append(w)


# get list of all English 5-letter words:
eng_text = eng.readlines()
eng_words = [x.rstrip() for x in eng_text]

wordle_list = []
for word in all_5_words:
    if word.strip() not in wordle_list and word.strip() not in eng_text:
        wordle_list.append(word.strip())

random_wordle = random.choice(wordle_list)

def game_round(n):
    print(">Round {}<".format(str(n)))
    print("Guess the 5-letter word:")
    guess = input()
    if len(guess) != 5:
        print("Please enter a five-letter word!")
        game_round(n)
    elif guess == random_wordle:
       print(print_green(guess))
       print("Yay! you won!")
    else:
       guess_split = [char for char in guess] 
       wordle_split = [char for char in random_wordle]
       for i in range(len(guess_split)):
          if guess_split[i] == wordle_split[i]:
              guess_split[i] = print_green(guess_split[i])
          elif guess_split[i] in wordle_split:
              guess_split[i] = print_yellow(guess_split[i])
       guess = ''.join(guess_split)
       print(guess)
       if n <5:
           game_round(n+1)
       else:
           print("Game over! The word was", print_green(random_wordle))
            
game_round(1)

eng.close()
pam.close()
