import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["apple", "banana", "cherry", "date", "grape"]
answer = list(random.choice(word_list))
letters_guessed = ['_' for i in range(0, len(answer))]
guesses_left = 7

while answer != letters_guessed and guesses_left != 0:
    clear()
    guess = input("Please guess an alphabet\n")
    print(" ".join(letters_guessed))
    if guess in answer:
        print(f"{guess} was present in the word")
        for j in range(0, len(answer)):
            if answer[j] == guess:
                letters_guessed[j] = guess
        print(" ".join(letters_guessed))
    else:
        guesses_left -= 1
        print(f"Sorry, {guess} was not present in the word")
        print(" ".join(letters_guessed))
        print(f"You have {guesses_left} guesses left")
        print(stages[guesses_left])


if answer == letters_guessed:
    print("You won!")
else:
    print("You lost!")
