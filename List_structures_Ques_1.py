import random

def roll_dice():

    num_dice = int(input("How many dice do you want to roll? "))
    total_sum = 0


    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total_sum += roll

    print(f"The sum of the rolls is: {total_sum}")


roll_dice()
