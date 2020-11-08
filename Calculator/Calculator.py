import math
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Multiplication import multiply
from Calculator.square import squaring
from Calculator.squareroot import rooting

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def root(self, a, b):
        self.result = rooting(a)
        return self.result