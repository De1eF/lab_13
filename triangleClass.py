import math

class Triangle(object):
    a = 0
    b = 0
    c = 0
    S = 0
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def isSet(self, a, b, c):
        eqA = self.a = a
        eqB = self.b = b
        eqC = self.c = c
        return eqA & eqB & eqC
    
    def calcSquare(self):
        p = self.a + self.b + self.c
        self.S = math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))
        
    def showSquare(self):
        print("Area of triangle is: ", self.S)
        
    def showDim(self):
        print("Dimentions of triangle are: a:", self.a, " b:", self.b, " c:", self.c)
