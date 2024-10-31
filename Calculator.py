"""Defines the calculator class that allows client code to perform arithmetic operations"""

class Calculator:
    def __init__(self):
        self._result = 0.0
        self._memOne = 0.0
        self._memTwo = 0.0
        self._memThree = 0.0

    def getResult(self):
        return self._result
    
    def getMemoryOne(self):
        return self._memOne
    
    def setMemoryOne(self, newMemOne):
        self._memOne = newMemOne

    def getMemoryTwo(self):
        return self._memTwo
    
    def setMemoryTwo(self, newMemTwo):
        self._memOne = newMemTwo

    def getMemoryThree(self):
        return self._memThree
    
    def setMemoryThree(self, newMemThree):
        self._memOne = newMemThree        
    #TODO: define the rest of the accessor and mutator methods

    def add(self, num1, num2):
        self._result = num1 + num2
        return self._result;

    def subtract(self, num1, num2):
        self._result = num1 - num2
        return self._result

    def multiplyself(self, num1, num2):
        self._result = num1 * num2
        return self._result

    def divide(self, num1, num2):
        self._result = num1 / num2
        return self._result

    def intDivide(self, num1, num2):
        self._result = num1 // num2
        return self._result

    def calcRemainder(self, num1, num2):
        self._result = num1 % num2
        return self._result
    
    def  solveQuadratic(self, a, b, c):
        #TODO: use the formula to determine the roots taking in consideration that it might not have a solution. 
        pass

    def saveResult(self, memNo):
        if memNo == 1:
            self._memOne = self._result
        elif memNo == 2:
            self._memTwo = self._result
        elif memNo == 3:
            self._memThree = self.result
        else:
            #the memory number is incorrect
            print("Incorrect memory number. The result was not saved")
        


