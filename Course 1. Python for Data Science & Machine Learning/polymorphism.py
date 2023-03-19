# Method Overriding
class Calculator: # Parent Class
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    
class Sum(Calculator): # Child Class
    def add(self, a, b, c): # method overriding
        return a+b+c
    
# my_calc = Sum()
# s = my_calc.add(12, 24)
# print(s)

# Method Overloading
class Employee:
    def __init__(self, name):
        self.name = name

    def income(self, money):
        self.money = money
        print(money)

        if money == None:
            print(f"{self.name} is poor enough")
        else:
            print(f"{self.name} is not poor")

me = Employee("Plabon")
me.income(94)