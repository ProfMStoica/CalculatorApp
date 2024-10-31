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
            #TODO: implement the rest of the user choices for the rest of the arithmetic operation
            #TODO: add an option to save the result of a calculation to memory
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
        #TODO: add the rest of the operations

        #ask the user to select one of the options
        selection = int(input("Please enter your choice [1, 2, etc]. Enter zero to exit the program: "))

        #return the option the user selected to the caller
        return selection

    def runAddition(self):
        #TODO: Modify the code to allow the use to type M1/M2/M3 to specify a memory location 
        #which should then be used in the arithmetic operation
        #ask the user for the numbers to add
        num1 = float(input("Please enter the first number to add: "))
        num2 = float(input("Please enter the second number to add: "))

        #perform the addition using the calculator object (stored in a field variable)
        self._calc.add(num1, num2)

        #inform the user what the result of the addition is
        print(f"{num1} + {num2} = {self._calc.getResult()}")

    def runSubtraction(self):
        #TODO: implement interaction with user for subtraction
        pass

    def runMultiplication(self):
        #TODO: implement interaction with user for multiplication

        pass

    def runDivision(self):
        #TODO: implement interaction with user for division

        pass

    def runIntDivision(self):
        #TODO: implement interaction with user for integer division

        pass

    def runDivRemainder(self):
        #TODO: implement interaction with user for remainder of integer division

        pass

    def runQuadratic(self):
        #TODO: implement interaction with user for solving a quadratic equation

        pass
