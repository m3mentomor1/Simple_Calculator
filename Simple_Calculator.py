
# -------------------------------------------------------
# File Name: Simple_Calculator.py
# -------------------------------------------------------
# Date Finished: 07-11-2022
# -------------------------------------------------------
# Description:
# This is a simple 4 operation arithmetic calculator
# that calculates the sum, difference, product, & 
# quotient of 2 user-inputted numbers.
# -------------------------------------------------------

import sys

print("\n---------- Simple Arithmetic Calculator ----------\n")

def menu_options():
    print("Select an operation to perform:\n", 
          "1 - Addition\n", 
          "2 - Subtraction\n",
          "3 - Multiplication\n",
          "4 - Division\n",
          "5 - Exit/Terminate Program\n")


def menu_input():
    while True:
        try:
            menu_input.menu_choice = int(input("Enter choice: "))
            
            if menu_input.menu_choice < 1:
                print("Invalid choice! Try again.\n")
            
            elif menu_input.menu_choice > 5:
                print("Invalid choice! Try again.\n")
            
            else:
                break
        except:
            print("Invalid choice! Try again.\n")


separator = "--------------------------------------------------"


def num_input():
    
    print(separator)
    
    while True:
        try:
            num_input.num1 = float(input("Enter 1st number: "))
            break
        except:
            print("Invalid input! Try again.\n")

    while True:
        try:
            num_input.num2 = float(input("Enter 2nd number: "))
            break
        except:
            print("Invalid input! Try again.\n")
    
    print(separator)


def calculation():
    
    menu_options()
    menu_input()

    if menu_input.menu_choice == 1:
        num_input()
        
        print(num_input.num1, "+", num_input.num2,
             "=", num_input.num1 + num_input.num2)    # Calculates the sum
        
        print(separator, "\n\n")
        calculation()
            
    elif menu_input.menu_choice == 2:
        num_input()
        
        print(num_input.num1, "-", num_input.num2,
             "=", num_input.num1 - num_input.num2)    # Calculates the difference 
        
        print(separator, "\n\n")
        calculation()

    elif menu_input.menu_choice == 3:
        num_input()
        
        print(num_input.num1, "×", num_input.num2,
             "=", num_input.num1 * num_input.num2)    # Calculates the product
        
        print(separator, "\n\n")
        calculation()

    elif menu_input.menu_choice == 4:
        num_input()
        
        print(num_input.num1, "÷", num_input.num2,
             "=", num_input.num1 / num_input.num2)    # Calculates the quotient
        
        print(separator, "\n\n")
        calculation()

    elif menu_input.menu_choice == 5:
        print(separator)
        sys.exit("Program terminated!\n")

calculation()

