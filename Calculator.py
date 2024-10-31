"""Defines the calculator class that allows client code to perform arithmetic operations"""

class Calculator:
    def __init__(self):
        self._lastResult = 0.0
        self._memOne = 0.0
        self._memTwo = 0.0
        self._memThree = 0.0

    def getLastResult(self):
        return self._lastResult
    
    def setLastResult(self, newLastResult):
        self._lastResult = newLastResult

    def getMemoryOne(self):
        return self._memOne
    
    def setMemoryOne(self, newMemOne):
        self._memOne = newMemOne

    #TODO: define the rest of the accessor and mutator methods

    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

    def intDivide(num1, num2):
        return num1 // num2

    def calcRemainder(num1, num2):
        return num1 % num2
    
    def  solveQuadratic(a, b, c):
        #TODO: use the formula to determine the roots taking in consideration that it might not have a solution. 
        pass

