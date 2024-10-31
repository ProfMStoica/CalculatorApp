"""The Application module is responsible for the interaction with the user"""
import Calculator

#ask the user for two numbers
num1Input = input("Please enter the first number: ")
firstNum = float(num1Input)
num2Input = input ("Please enter the second number: ")
secondNum = float(num2Input)

#use the calculator module to add them
result = Calculator.add(firstNum, secondNum)

#let the user know what the sum of the two numbers is
print(f"{firstNum} + {secondNum} = {result}")
