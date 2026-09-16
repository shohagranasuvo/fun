"""
A fun and interactive number guessing game.
This module provides the core logic for a game where the user
attempts to guess a randomly generated number between 1 and 100.
"""
import random
import sys

def display_welcome():
    """Display the welcome message and game instructions to the user."""
    print("=" * 50)
    print("🎉 Welcome to the Fun Number Guessing Game! 🎉")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("You have 10 attempts to guess correctly.")
    print("Let's see if you can beat the odds! 😄")
    print("=" * 50)
    print()

def get_hint(secret, guess):
    """Return a hint based on whether the guess is too high, too low, or correct."""
    if guess < secret:
        return "Too low! Try a higher number 📈"
    if guess > secret:
        return "Too high! Try a lower number 📉"
    return "Correct! You've guessed the number! 🎊"

def play_game():
    """Main game loop that handles user input and tracks attempts."""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    display_welcome()

    while attempts < max_attempts:
        try:
            user_input = sys.stdin.readline().strip()
            if not user_input:
                break
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number! 🔢")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number "
                  f"{secret_number} in {attempts} attempts! 🎉")
            print("You're a guessing genius! 🧠")
            break

        hint = get_hint(secret_number, guess)
        print(f"❌ {hint}")
        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts left.\n")

    if attempts == max_attempts and guess != secret_number:
        print(f"\n😔 Sorry, you've used all {max_attempts} attempts.")
        print(f"The number I was thinking of was {secret_number}.")
        print("Better luck next time! 🍀")

    print("\nThanks for playing! Come back anytime for more fun! 👋")

if __name__ == "__main__":
    play_game()
