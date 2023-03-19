# class Car:

#     area = 0
#     arr = [1, 2]

#     def music(self):
#         run_the_music
#     def steering(self):
#         move_the_direction

# toyota = Car() # object
# premio = Car()

# Method
class Calculator:

    def __init__(self, a, b): # class constructor
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    
calc = Calculator(12, 24)
s = calc.add()
m = calc.sub()
print(s, m)

