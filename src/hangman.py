"""
A simple Hangman game.
The user tries to guess a secret word one letter at a time.
"""
import random
import sys

def get_secret_word():
    """Return a random word from a predefined list."""
    words = ["python", "programming", "computer", "algorithm", "developer",
             "keyboard", "internet", "software", "database", "interface"]
    return random.choice(words)

def display_game_state(word, guessed_letters, attempts_left):
    """Print the current progress of the word and the remaining attempts."""
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\nWord: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Attempts left: {attempts_left}")

def play_hangman():
    """Main game loop for Hangman."""
    secret_word = get_secret_word()
    guessed_letters = set()
    attempts_left = 6

    print("=" * 50)
    print("😵 Welcome to the Hangman Game! 😵")
    print("=" * 50)
    print("Try to guess the secret word before you run out of attempts!")

    while attempts_left > 0:
        display_game_state(secret_word, guessed_letters, attempts_left)

        try:
            user_input = sys.stdin.readline().strip().lower()
            if not user_input:
                break
            if len(user_input) != 1 or not user_input.isalpha():
                print("Please enter a single letter! 🔤")
                continue
        except EOFError:
            break

        letter = user_input

        if letter in guessed_letters:
            print(f"You already guessed '{letter}'! Try another one. 🔄")
            continue

        guessed_letters.add(letter)

        if letter in secret_word:
            print(f"Nice! '{letter}' is in the word. ✅")
            # Check if all letters are guessed
            if all(l in guessed_letters for l in secret_word):
                print(f"\n🎉 Congratulations! You guessed the word: {secret_word}! 🎉")
                return True
        else:
            attempts_left -= 1
            print(f"Oops! '{letter}' is not in the word. ❌")

    if attempts_left == 0:
        print(f"\n😔 Game over! You ran out of attempts.")
        print(f"The secret word was: {secret_word}")
        return False

    print("\nThanks for playing! 👋")
    return False

if __name__ == "__main__":
    play_hangman()
