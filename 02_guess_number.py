# guess the number
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x} : "))
        if guess < random_number:
            print("Sorry,too low.")
        elif guess > random_number:
            print("Sorry,too high")
    print(f"Yeh,congrats.You have guessed the {random_number} correctly")


guess(10)


# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Enter a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry,guess again too Low.")
#         elif guess > random_number:
#             print("Sorry,guess again too high.")
#     print(f"yeh, congrats.You have guessed the {random_number}correctly")


# guess(10)
