# polymorphism
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,otr):
        t1 = self.m1+otr.m1
        t2 = self.m2 + otr.m2

    def __sub__(self,otr):
        t1 = self.m1 - otr.m1
        t2 = self.m2-otr.m2
        return t1,t2

c1 = Student(10,20)
c2 = Student(2,15)
print(c1 - c2)


#infinite numbers can be stored using generators



