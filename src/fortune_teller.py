import random

def get_fortune():
    fortunes = [
        "Your future is bright, wear shades.",
        "A surprise gift is coming your way.",
        "The computer says 'no' for now, try again later.",
        "Success is in your code, keep debugging.",
        "Today is a good day to push to main.",
        "You will find a great snack in the kitchen."
    ]
    return random.choice(fortunes)

if __name__ == "__main__":
    print(f"Fortune: {get_fortune()}")
