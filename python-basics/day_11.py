# Exception Handling
#    intenration error cannot be resolved
# try except

# a = 10
# b = 10
# try:
#     c = a/b
# except NameError: #this will execute if name error is raised
#     print('a is not defined')
# except ZeroDivisionError,FileExistsError:  #this will execute if name error or file exist error if raised
#     print('zero division error')
# except:     #this will execute if any other error is raised    (not write another specific except errors after final except: )
#     print('something went wrong')
# else:       #this sill execute if no exception is raised
#     print(c)
# finally:    #this sill execute irrespective of exception is raised or not
#     print('execution completed')



# try:
#     with open('dem.txt','r') as file:
#         line = file.readlines()
#     for i in range(len(line)):
#         name = line[i]
#         name_and_age = (name.strip('\n'))
#         name_with_age = name_and_age.split(' ')
#         print(name_and_age)
#         print(name_with_age[0])
#         print(name_with_age[1])
# except FileNotFoundError :
#     print('this file not exist')

def add():
    print('addition')
    print('-------------------------------')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number '))
    print(a+b)

def sub():
    print('subtraction')
    print('-------------------------------')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print(a-b)

def mul():
    print('multiplication')
    print('-------------------------------')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print(a*b)

def div():
       print('division')
       print('-------------------------------')
       try:
            a = int(input('Enter first number: '))
            b = int(input('Enter second number: '))
            print(a/b)
       except ZeroDivisionError:
            print('Cant divide by zero')
            div()

def operations():
    print('1.Add\t2.Sub\t3.mul\t4.div\t5.exit')
    print('-------------------------------')

    choice = int(input('Enter your choice: '))
    choice_box = [1,2,3,4,5]
    if choice not in choice_box:
        print("Invalid choice!!!")
        operations()
    else:
        return choice
s = True
while s:
    choice = operations()

    if choice == 1:
        add()
    elif choice ==2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        exit()
    else:
        print('Invalid choice!')
    print('--------------')
    while s:
        cont = input('Do you want to continue? (y/n): ')
        if cont == 'n':
            s = False
        elif cont == 'y':
            break
        else:
            print('Invalid choice!!!')



