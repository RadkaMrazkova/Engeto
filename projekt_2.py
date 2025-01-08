"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Radka Mrázková
email: radkamrazkova4@seznam.cz
"""
import random

def display_init_text():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

def generate_number():
    digits = set(range(1, 10))
    secret_number = ""
    for digit in range(4):
        selected_digit = random.choice(list(digits))
        digits.remove(selected_digit)
        secret_number += str(selected_digit)
        if digit == 0:
            digits.add(0)
    return secret_number

def play_round():
    guess = str(input())
    if not guess.isdigit():
        print("Please enter a valid integer.")
        return None
    if len(guess) != 4:
        print("Number must consist of 4 digits.")
        return None
    if guess[0] == '0':
        print("Number cannot start with 0.")
        return None
    if len(set(guess)) != 4:
        print("Number cannot contain duplicates.")
        return None
    return guess

def count_bulls(secret_number, guess):
    counter = 0
    for index in range(len(guess)):
        if guess[index] == secret_number[index]:
            counter += 1
    return counter

def count_cows(secret_number, guess):
    counter = 0
    correct_digits = set(secret_number)
    for index in range(len(guess)):
        digit = guess[index]
        if digit in correct_digits and digit != secret_number[index]:
            counter += 1
    return counter

def evaluate_guess(secret_number, guess):
    bulls = count_bulls(secret_number, guess)
    if bulls == 4:
        return True
    cows = count_cows(secret_number, guess)
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, "
          f"{cows} {'cow' if cows == 1 else 'cows'}")
    print("-----------------------------------------------")
    return False

def end_game(rounds):
    print(f"Correct, you've guessed the right number \nin {rounds} "
          f"{'guess' if rounds == 1 else 'guesses'}!")
    print("-----------------------------------------------")
    print("That's amazing!")

def play_bulls_cows():
    display_init_text()
    secret_number = generate_number()
    rounds = 0
    winner = False
    while not winner:
        guess = play_round()
        if guess is None:
            continue
        rounds += 1
        winner = evaluate_guess(secret_number, guess)
    end_game(rounds)

def main():
    play_bulls_cows()

if __name__ == "__main__":
    main()