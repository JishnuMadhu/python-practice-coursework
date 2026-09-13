"""i = 0
while i <= 10:
    print(i)
    i  = i + 1
print('end of loop')"""

#print 10 to 1

"""i = 10
while i >= 1:
    print(i)
    i = i - 1
print('end of loop')"""

#find sum of first 10 natural numbers

"""i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)"""



#print multiplication table of a number

"""num = int(input("Enter a number "))
i = 1
while i <= 10:
    print(i, "*",num, "= ", i * num)
    i = i + 1"""


#print even nos between 10 to 20

"""i =10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i = i + 1"""



#print first n even numbers
"""
i = 2
n = int(input("Enter a number "))
print(f'First {n} even numbers')
while i <= n*2:
    if i % 2 == 0:
            print(i)
    i = i + 1"""



#create a simple authentication system using while
# loop and if else statement(print the entered username and password and repeatedly ask correct username and password if entered wrong)

username = 'jishnu123'
password = '12345678'
success = False
while success == False:
    user = input("Enter username: ")
    passw = input("Enter password: ")
    if user == username and passw == password:
        success = True                                break is not alwaws good if there are another whiel loops inside main one
        print("Authentication successful")
    else:
        print("Wrong username and password")
        print(user)
        print(passw)
        print("Enter correct username and password")
