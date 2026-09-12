#when we return multiple values , it will return as a tuple

# x = 'dhf'
# def add():
#     a = 10
#     b = 20
#     c = a+b 
#     return c
# x = (add())
# print(x)


# x = 'dhf'
# def add():
#     a = 10
#     b = 20
#     c = a+b #if not return ,it will print None
# x = (add())
# print(x)

# def add():
#     a = 10
#     b = 20
#     c = a+b 
#     return 10,'adfj',True  #if multiple return values, it will return as a tuple (10,'adfj',True)
# x = add()
# print(x)


# def add(b,a,c,d,e):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
# x = 10
# y = 20
# add(x,y,'dfg',True,10.5)


# def add(b,a,c=0):  #if there is not value passed at function call for c, it will take that c=0 value otherwise it will take passed value 
                     #positional arguments must come before keyword arguments (that is, keyword arguments must be written from the last and if we skip one a)
                     #Because Python doesn't allow a positional argument to come after a keyword argument
# x = 10
# y = 20
# add(x,y)

#arguments: positional arguments: matched arguments with parameters by order of arguments given
#           keyword arguments: matches arguments with parameters by using same keyword names 

#There are two different rules, one for the function definition and one for the function call.
#
#In the function definition: In the function definition: Parameters without default values must come before parameters with default values.

#                            In the function call: Positional arguments must come before keyword arguments.


# #keyword argument
# def add(b,a,c,d,e):
#     print(a)
#     print(b)
#     print(c)



#1.Create a function to calculate students total mark and average

# def student1(name,phy,math,che):
#     total_mark = phy+math+che
#     avg = total_mark/3
#     return name,total_mark,avg

# name = 'jishnu'
# phy = 60
# math = 80
# che = 70

# student_details = student1(name,phy,math,che)
# print(student_details)


#sir

# def student(name,m1,m2,m3):
#    total = m1+m2+m3
#    avg = total/3
#    print(f'student name is {name} and total mark is {total} and average is {avg}')

# student('jishnu',10,20,30)


# # def student1(phy,math,che):
# #     total_mark = phy+math+che
# #     avg = total_mark/3
# #     return total_mark,avg

# #print multiplication tavle of a number using funcition
# def mul_table(n):
#     for i in range(1,11):
#       print(f'{i} X {n} = {i*n}')

# n = int(input('enter a number: '))
# mul_table(n)


# def nums(*args):  #no mater how many arguments come, we can receive them all using *args
#    print(args)

# def nums(**kwargs):   
#    print(kwargs)  #it will print it as dictionary, use for loop if you dont want to print as a dict

# nums(a=12,b=20,c=30,d=40)

def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")


