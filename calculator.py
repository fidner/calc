# PYTHON CALCULATOR

print("█▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█\n█▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄\n\n")

import time 

redo = True

def again():
    done = True
    while done:
        time.sleep(0.5)
        ans = input("Do you want to run another calculation? y/n \n")
        if ans.lower() == "y":
            done = False 
            again = True
        elif ans.lower() == "n":
            done = False
            again = False
        else:
            print("Invalid input, try again\n")
    return again

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0] 
    for num in numbers[1:]: 
        result -= num 
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Cannot divide by zero"
        result /= num
    return result

while redo:
    time.sleep(1)
    userInput = input(f"Options:\n- Type 'add' for addition\n- Type 'subtract' for subtraction\n- Type 'divide' for division\n- Type 'multiply' for multiplication\n \nType 'quit' to stop the code.\n")
    operators = ["add", "subtract", "divide", "multiply"]
    if userInput.lower() == "quit":
        break
    elif userInput.lower() in operators:
        inputtedValues = input("Please enter any amount of values. Seperate each value with a single space.\n")
        values = [int(x) for x in inputtedValues.split()]
        if userInput.lower() == "add":
            time.sleep(0.5)
            print("Answer: ", add(values))
            time.sleep(0.5)
            redo = again()
        elif userInput.lower() == "subtract":
            time.sleep(0.5)
            print("Answer: ", subtract(values))
            time.sleep(0.5)
            redo = again()
        elif userInput.lower() == "divide":
            time.sleep(0.5)
            print("Answer: ", divide(values))
            time.sleep(0.5)
            redo = again()
        elif userInput.lower() == "multiply":
            time.sleep(0.5)
            print("Answer: ", multiply(values))
            time.sleep(0.5)
            redo = again()
    else:
        print("Invalid input, try again. one\n")