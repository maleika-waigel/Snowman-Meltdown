import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current game state, including the ASCII art
    and the secret word with underscores for unguessed letters.
    """
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def is_valid_guess(guess):
    """Checks whether the guess is a single alphabetic character."""
    return guess.isalpha() and len(guess) == 1


def play_game():
    """Runs the Snowman Meltdown game and manages the game state."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < len(STAGES) - 1:
        guess = input("Guess a letter: ").lower()
        if is_valid_guess(guess):
            if guess in secret_word and guess not in guessed_letters:
                guessed_letters.append(guess)
            if guess not in secret_word:
                mistakes += 1
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations, you saved the snowman!")
                return
        else:
            print("False input")

        # print("You guessed:", guess)
        display_game_state(mistakes, secret_word, guessed_letters)

    print(f"Game Over! The word was: {secret_word}")