import random

def play():
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    user = input("Choose rock, paper, or scissors: ").lower()

    if user not in choices:
        return "Invalid choice!"

    if user == computer:
        return f"It's a tie! Both chose {computer}."
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return f"You win! {user} beats {computer}."
    else:
        return f"You lose! {computer} beats {user}."

if __name__ == "__main__":
    print(play())
