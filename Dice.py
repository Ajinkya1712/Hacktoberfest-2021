import random
import time

user_choice = "yes"

while user_choice =="yes":

    print("Dice is rolling")
    time.sleep(1)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("Dice1 value is ", dice1)
    print("Dice2 value is ", dice2)

    user_choice = input("Do you want to continue playing yes/no :- ")


print("Thank you for playing")
