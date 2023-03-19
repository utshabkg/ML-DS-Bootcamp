class Calculator: # Parent Class
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    
class Sum(Calculator): # Child Class
    def add(self, a, b, c): # method overriding
        return a+b+c
    
my_calc = Sum()
s = my_calc.add(12, 24)
print(s)