from os import system

import requests

# Hangman stages
hangman = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
    +---+
    |   |
    O   |
         |
         |
         |
=========''', '''
    +---+
    |   |
    O   |
    |   |
         |
         |
=========''', '''
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
   /|\  |
         |
         |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
         |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
         |
=========''']


# Get a word from https://random-word-api.herokuapp.com/word and return it
def random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    word = response.json()[0]
    return word


def clear_console():
    system('cls')


def main():
    print("Welcome to the hangman game!")

    # Choice between random or custom word
    while True:
        print("Do you want to play with a random word or a custom word?")
        print("1. Random word")
        print("2. Custom word")
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            pass

    if choice == 1:
        word = random_word()
    elif choice == 2:
        word = input("Enter your word: ")
    else:
        print("Invalid choice!")
        return

    # Create a list with the letters of the word
    word_letters = list(word)
    # A list with the letters that the user has guessed
    guessed_letters = []
    # A list with the letters that the user has guessed incorrectly
    wrong_letters = []

    # The game loop
    while True:
        # Print the hangman stage
        print(hangman[len(wrong_letters)])

        # Print the word with the guessed letters
        for letter in word_letters:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

        # Print the wrong letters
        print("Wrong letters:", end=" ")
        for letter in wrong_letters:
            print(letter, end=" ")
        print()

        # Ask the user for a letter
        letter = input("Enter a letter: ")

        if len(letter) != 1:
            print("You can only enter one letter!")
            continue

        # Check if the letter is in the word
        if letter in word_letters:
            # Check if the letter has already been guessed
            if letter in guessed_letters:
                print("You have already guessed this letter!")
            else:
                guessed_letters.append(letter)
        else:
            # Check if the letter has already been guessed
            if letter in wrong_letters:
                print("You have already guessed this letter!")
            else:
                wrong_letters.append(letter)

        # Check if the user has won
        if set(word_letters) == set(guessed_letters):
            print("You win!")
            break

        # Check if the user has lost
        if len(wrong_letters) == len(hangman):
            print("You lose! The word was", word)
            break


if __name__ == '__main__':
    main()
