"""Defines the MathApp class responsible for user interaction"""

from calculator import  Calculator
class MathApp:
    def __init__(self):
        self._calc = Calculator()

    def run(self):
        userChoice = -1
        while userChoice != 0:
            #display the menu to the user allowing them to make a choice of what operation to run
            userChoice = self.showMenu()

            #based on the user choice run the correct method
            if userChoice == 1:
                self.runAddition()
            elif userChoice == 2:
                self.runSubtraction()
            elif userChoice == 3:
                self.runMultiplication()
            elif userChoice == 4:
                self.runDivision()
            elif userChoice == 5:
                self.runIntDivision()
            elif userChoice == 6:
                self.runDivRemainder()
            elif userChoice == 7:
                self.runQuadratic()
            elif userChoice == 8:
                self.saveToMemory()
            elif userChoice == 0:
                print("Thank you for using the Python Calculator. The application will now exit.")
            else:
                print("Invalid choice. Please select again")

    def showMenu(self):
        #print the menu
        print("Welcome to Python Math App")
        print("Which of the following artithmetic operations you would like to perform?")
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Integer Division")
        print("\t6. Remainder")
        print("\t7. Solve Quadratic")
        print("\t8. Save to memory")

        #ask the user to select one of the options
        selection = int(input("Please enter your choice [1, 2, etc]. Enter zero to exit the program: "))

        #return the option the user selected to the caller
        return selection

    def resolveUserInput(self, userInput):
        #check whether the user input is a memory location and determine which location it is
        if userInput == "M1":
            #the user specified a memory location 1 then extract its value and return it
            return self._calc.getMemoryOne()
        elif userInput == "M2":
            #the user specified a memory location 2 then extract its value and return it
            return self._calc.getMemoryTwo()
        elif userInput == "M3":
            #the user specified a memory location 3 then extract its value and return it
            return self._calc.getMemoryThree()
        else:
             #the user specified a number then convert the input to number
             return float(userInput)
    
    def runAddition(self):
        #ask the user for the numbers to add
        num1Input = input("Please enter the first number to add or a memory location (M1/M2/M3): ")
        num2Input = input("Please enter the second number to add or a memory location (M1/M2/M3): ")

        #determine the number input
        num1 = self.resolveUserInput(num1Input)
        num2 = self.resolveUserInput(num2Input)

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.add(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} + {num2} = {self._calc.getResult()}")

    def runSubtraction(self):
        #ask the user for the numbers to subtract
        num1 = self.resolveUserInput(input("Please enter the first number to subtract or a memory location (M1/M2/M3): "))
        num2 = self.resolveUserInput(input("Please enter the second number to subtract or a memory location (M1/M2/M3): "))

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.subtract(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} - {num2} = {self._calc.getResult()}")

    def runMultiplication(self):
        #ask the user for the numbers to multiply
        num1 = self.resolveUserInput(input("Please enter the first number to multiply or a memory location (M1/M2/M3): "))
        num2 = self.resolveUserInput(input("Please enter the second number to multiply or a memory location (M1/M2/M3): "))

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.multiply(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} * {num2} = {self._calc.getResult()}")

    def runDivision(self):
        #ask the user for the numbers to add
        num1 = self.resolveUserInput(input("Please enter the first number to divide or a memory location (M1/M2/M3): "))
        num2 = self.resolveUserInput(input("Please enter the second number to divide or a memory location (M1/M2/M3): "))

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.divide(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} / {num2} = {self._calc.getResult()}")

    def runIntDivision(self):
        #ask the user for the numbers to add
        num1 = self.resolveUserInput(input("Please enter the first whole number to divide or a memory location (M1/M2/M3): "))
        num2 = self.resolveUserInput(input("Please enter the second whole number to divide or a memory location (M1/M2/M3): "))

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.intDivide(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} // {num2} = {self._calc.getResult()}")

    def runDivRemainder(self):
        #ask the user for the numbers to add
        num1 = self.resolveUserInput(input("Please enter the first whole number to divide or a memory location (M1/M2/M3): "))
        num2 = self.resolveUserInput(input("Please enter the second whole number to divide or a memory location (M1/M2/M3): "))

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.calcRemainder(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} % {num2} = {self._calc.getResult()}")

    def runQuadratic(self):
        #TODO: implement interaction with user for solving a quadratic equation
        print("TODO: This is left as an exercise. You will need to use the sqrt function from the math module.")

    def saveToMemory(self):
        #ask the user in which memory slot to save the result of the last calculation
        memNo = int(input("In what memory location would you like to store the result of the last calculation? [1, 2 or 3]"))
        
        #save the last result in the appropriate memory location
        self._calc.saveResult(memNo)    