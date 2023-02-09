import math
# task1
class Persone: 
    def __init__(self, name):
        self.name = name
    
    def printName(self):
        print(self.name)

# task2
class Shape:
    def printArea():
        print(0)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def printArea(self):
        print(self.side*self.side)

# task3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def printArea(self):
        print(self.width*self.length)

# task4
class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def showCoordinates(self):
        print(self.x, self.y, sep=',')
    def changeCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
    def colculate(self,second):
        length = math.sqrt((second.x - self.x)**2 + (second.y - self.y)**2)
        print(length)

# task5
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, addMoney):
        self.balance = self.balance + addMoney
    def withdraw(self, takeMoney):
        if self.balance >= takeMoney:
            self.balance = self.balance - takeMoney
        else:
            print('there os not enough money!')
    def showBalanace(self):
        print(self.balance)

p1 = Persone('Dimash')
p1.printName()

s1 = Square(5)
s1.printArea()

r1 = Rectangle(5, 6)
r1.printArea()

o1 = Object(1, 2)
o1.showCoordinates()
o1.changeCoordinates(3,4)
o1.showCoordinates()
o2 = Object(0,0)
o1.colculate(o2)

b1 = BankAccount('Dimash', 100000)
b1.showBalanace()
b1.deposit(20000)
b1.showBalanace()
b1.withdraw(150000)
b1.withdraw(15000)
b1.showBalanace()
