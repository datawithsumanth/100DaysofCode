"""
Date: 09-11-2023
Author: Sumanth S Kumar
Title: Simple Calculator
Description: The simple calc lets the user add, subtract, multiply or divide
two numbers that are provided as inputs from the user.
"""

from art import calculator_logo

def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mul(number1, number2):
    return number1 * number2

def div(number1, number2):
    return round(number1 / number2, 1)

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print(calculator_logo)
    repeat = 'y'
    first_number = float(input("What's the first number?: "))
    for i in operations:
        print(i)

    while repeat == 'y':
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        op_selected = operations[operation]
        result = op_selected(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n tp start a new calculation\n")
        if repeat == 'y':
            first_number = result
        else:
            repeat == 'n'

    calculator()

calculator()

