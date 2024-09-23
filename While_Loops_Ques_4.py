import random

def guessing_game():

    target_number = random.randint(1, 10)

    print("I have drawn a number between 1 and 10. Try to guess it!")

    while True:
        user_input = input("Enter your guess (1-10): ")

        try:
            guess = int(user_input)

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print("Correct! You guessed the right number!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

guessing_game()
