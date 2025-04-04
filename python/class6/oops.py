"""

    OOPs -> Object Oriented Programmings

    1. class
    2. object
    3. Inheritance
    4. Encapsulation
    5. Polymorphism

"""

class Person:
    def __init__(self, a, b, c):     # Constructor Method
        self.a = a
        self.b = b
        self.c = c

    def demo(self):
        print("It'a Demo method:", self.a)

p1 = Person("1500", "hi", True)

# print(p1.a, p1.b, p1.c)

p1.demo()

p2 = Person("25000", "Good Boy", False)

# print(p2.a, p2.b, p2.c)

p2.demo()