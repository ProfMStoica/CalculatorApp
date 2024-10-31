"""Defines the calculator class that allows client code to perform arithmetic operations"""

class Calculator:
    def __init__(self):
        self._lastResult = 0.0
        self._memOne = 0.0
        self._memTwo = 0.0
        self._memThree = 0.0