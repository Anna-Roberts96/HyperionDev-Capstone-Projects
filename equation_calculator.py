# Program calculates equations and writes equations and answers to a file
# Use of try/except blocks to determine number input is integer
# If/elif/else blocks used to recognise operation used in equation
# Once prompted, program stops asking user for equations

import os

print("This program is designed to be a simple calculator.")
print("\nI am going to ask you for a number, followed by an operation and then another number\n")

with open('name holder', 'a+') as file:
    file.write("\nHere are all of the equations you have entered:\n\n")

    while True:      
        try:
            num_first = int(input("Enter the first number: "))
        except ValueError:
            print("That wasn't a valid integer, please try again")
            num_first = int(input("Enter the first number: "))
        operator = input("Enter an operator, like '+', 'x', '/', or '-' : ")
        try:
            num_second = int(input("Enter the second number: "))
        except ValueError:
            print("That wasn't a valid integer, please try again")
            num_second = int(input("Enter the second number: "))

        if operator == "+":
            answer = (num_first + num_second)
            equation = ("{} + {} = {}".format(num_first, num_second, answer))
            print("The answer to " + equation)
            file.write(equation + "\n\n")
            action = input("\nWould you like to continue entering equations? Enter 'Yes' or 'No' ")
            action = action.lower()
            if action == "yes":
                continue
            elif action == "no":
                break
            else:
                print("That wasn't a valid answer, please try again")
        
        elif operator == "x" or operator == "X" or operator == "*":
            answer = (num_first * num_second)
            equation = ("{} * {} = {}".format(num_first, num_second, answer))
            print("The answer to " + equation)
            file.write(equation + "\n\n")
            action = input("\nWould you like to continue entering equations? Enter 'Yes' or 'No' ")
            action = action.lower()
            if action == "yes":
                continue
            elif action == "no":
                break
            else:
                print("That wasn't a valid answer, please try again")

        elif operator == "/":
            if num_second == 0:
                num_second = int(input("Please enter a divisible number that is not zero: "))
                answer = (num_first / num_second)
                equation = ("{} / {} = {}".format(num_first, num_second, answer))
                print("The answer to " + equation)
                file.write(equation + "\n\n")
                action = input("\nWould you like to continue entering equations? Enter 'Yes' or 'No' ")
                action = action.lower()
                if action == "yes":
                    continue
                elif action == "no":
                    break
                else:
                    print("That wasn't a valid answer, please try again")
            else:
                answer = (num_first / num_second)
                equation = ("{} / {} = {}".format(num_first, num_second, answer))
                print("The answer to " + equation)
                file.write(equation + "\n\n")
                action = input("\nWould you like to continue entering equations? Enter 'Yes' or 'No' ")
                action = action.lower()
                if action == "yes":
                    continue
                elif action == "no":
                    break
                else:
                    print("That wasn't a valid answer, please try again")

        elif operator == "-":
            answer = (num_first - num_second)
            equation = ("{} - {} = {}".format(num_first, num_second, answer))
            print("The answer to " + equation)
            file.write(equation + "\n\n")
            action = input("\nWould you like to continue entering equations? Enter 'Yes' or 'No' ")
            action = action.lower()
            if action == "yes":
                continue
            elif action == "no":
                break
            else:
                print("That wasn't a valid answer, please try again")
        else:
            print("That wasn't a valid operation, please try again!")
            continue

# Asks user to name file equations are stored to, file re-named
# Try/except/finally block used to open file for user to read contents
print("\n\nI have something to admit.\n") 
print("I have been saving all of your equations with a valid operator to a file.\n")
file_name = input("\nWhat would you like to call this file? ")
os.rename('name holder', file_name)

while True:

    file_name = input("\nEnter the name of what you just called your file: ")
    file = None
    try:
        file = open(file_name, 'r+')
        lines = file.read()
        print(lines)
        break
    except FileNotFoundError as error:
        print("\nThe file you are trying to open doesn't exist")
        print(error)
        file_name = input("\nEnter the name of what you just called your file")
        continue
    finally:
        if file is not None:
            file.close()
            break

