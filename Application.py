"""The Application module is responsible for the interaction with the user"""
import Calculator

#ask the user for two numbers
num1Input = input("Please enter the first number")
num2Input = input ("Please enter the second number")

#use the calculator module to add them
sum = Calculator.add(num1Input, num2Input)

#let the user know what the sum of the two numbers is
print(f"{num1Input} + {num2Input} = {sum}")
