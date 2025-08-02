import random

def call_random_number_game():
    guess = random.randint(1,100)
    return guess

def UserGuess():
    user_guess = int(input("🤔Guess random number between 1 and 100 : "))
    return user_guess

def main():
    print("\n🥳Welcome to the Random Number Guessing Game!🥳\n")
    value = call_random_number_game()
    user_guess = UserGuess()


    while True:
        if user_guess == value:
            print("Congratulations!🎊🎉 You guessed the correct number.🥳👏🏻\n")
            return
        elif user_guess < 1 or user_guess >100:
            print("Your guess is invalid🥲. Please guess a number between 1 and 100.\n")
            user_guess = UserGuess()
        elif user_guess < value:
            print("Your guess is low.😅 Try again.\n")
            user_guess = UserGuess()
        elif user_guess > value:
            print("Your guess is high.😅 Try again.\n")
            user_guess = UserGuess()


main()
print("🙏🏻Thanks for playing the Random Number Guessing Game!🙇🏻‍♀️\n")