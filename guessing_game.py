import random
import time

def display_welcome():
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
    if guess < secret:
        return "Too low! Try a higher number 📈"
    elif guess > secret:
        return "Too high! Try a lower number 📉"
    else:
        return "Correct! You've guessed the number! 🎊"

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    display_welcome()

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number! 🔢")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts! 🎉")
            print("You're a guessing genius! 🧠")
            break
        else:
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