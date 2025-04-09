# OOPs --> Object Oriented Programmings

"""
    1. class
    2. Object
    3. Inheritance
    4. polymorphism
    5. Encapsulation

"""

# class student:
#     def __init__(self, uname, a, d):
#         print("I'm cons")
#         self.username = uname
#         self.age = a
#         self.dept = d

#     def marks(self, mark):
#         print(f"{self.username} mark is: ", mark)

#     def __del__(self):
#         print("I'm Destructor")
    

# s1 = student("Dhanush", 20, "IT")
# s2 = student("Nithees", 19, "MECH")

# print(s1.username, s1.age)
# print(s2.username, s2.age)

# s1.marks(100)
# s2.marks(90)

# Inheritance

class grantParent:
    car = "Volvo"

    def carColor(self):
        print("Car color is Crimson")

class parent(grantParent):
    assets = 2000000

    def hairColor(self):
        print("Hair color is gray")

class child(parent, grantParent):
    marks = 100

    def hobbies(self):
        print("Hobbies is criket")

c1 = child()

print(c1.assets)

c1.hairColor()

c1.carColor()