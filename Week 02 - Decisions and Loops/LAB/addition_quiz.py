"""
Addition quiz

step 1 : generate two singlen digit integers
step 2 : Prompt the student to answer the question
step 3 : check the answer

"""
import random

while True:
    num1 = random.randint(1 , 9)
    num2 = random.randint(1 , 9)
    answer = int(input(f"Answer  for {num1} + {num2}: "))
    if answer == num1 + num2:
        print("correct")
        break
    else:
        print("Try again")
