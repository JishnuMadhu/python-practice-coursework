# class Car:

#     def __init__(self,cname,ccolor):
#         self.name = cname
#         self.color = ccolor

#     def start(self): #methods
#         print(f"{self.name} has started")

#     def stop(self):
#         print(f"{self.name} has stopped")

# c1 = Car("Maruthi 800",'red')
# c2 = Car("City",'Black')
# print(c1.name)
# print(c2.name)
# c1.start()
# c2.start()

# #initialise and obj  __init__()

# #create a student class 
# #6 attributes: name, m1,m2,m3,m4,m5

# #sum_of_marks()
# #average of marks()
# #details()


# class Student:
#     def __init__(self,name,m1,m2,m3,m4,m5):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5

#     def sum_of_marks(self):
#           self.sum = self.m1 + self.m2+self.m3+self.m4+self.m5

#     def avg_of_marks(self):
#           self.avg = (self.m1 + self.m2+self.m3+self.m4+self.m5)/5

#     def details(self):
#          print(f'{self.name} got {self.m1} out of 50 for maths')
#          print(f'{self.name} got {self.m2} out of 50 for physics')
#          print(f'{self.name} got {self.m3} out of 50 for chemistry')
#          print(f'{self.name} got {self.m4} out of 50 for biology')
#          print(f'{self.name} got {self.m5} out of 50 for english')
#          print(f'{self.name} got {self.m1} out of 50 for maths')
#          print(f'{self.name} got {self.m1} out of 50 for maths')



class Point():

    def __init__(self):
        self.x = 0
        self.y = 0
    def reset(self):
        self.x = 0
        self.y = 0
    def move(self,del_x,del_y):
        self.x = del_x
        self.y = del_y

    def xmove(self,move_x):
        self.x = move_x
    def ymove(self,move_y):
        self.y = move_y

c1 = Point()
c1.move(7,8)
print(c1.x,c1.y)
c1.reset()
print(c1.x,c1.y)
c1.xmove(232)
print(c1.x,c1.y)
c1.ymove(2332)
print(c1.x,c1.y)


