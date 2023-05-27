import random

# Creating a number guessing game with python

# Constants for level turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Creating a check answer function
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Guess is high")
        return turns - 1
    elif guess < answer:
        print("Guess is low")
        return turns - 1
    else:
        print(f"You've got it, the number i was thinking of was {answer}")


# Creating a function for a difficulty level
def set_difficulty():
    level = input("Choose a difficulty level, type 'Easy' or 'Hard': ").title()
    if level == "Easy":
        return EASY_LEVEL_TURNS
    elif level == "Hard":
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(answer)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining")
        guess = int(input("Make a Guess "))
        turns = check_answer(guess, answer, turns)
        print("Guess again")
        if turns == 0:
            print("Sorry, you've run out of guesses, you loose!")
            return


game()
