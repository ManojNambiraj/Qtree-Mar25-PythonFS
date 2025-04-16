class admin:
    def __init__(self, m1, m2):
        self.__mark1 = m1
        self.mark2 = m2

    def setMark1(self, um1):
        self.__mark1 = um1
    
    def getMark1(self):
        return self.__mark1

s1 = admin(0, 70)

s1.setMark1(99)

print(s1.getMark1())