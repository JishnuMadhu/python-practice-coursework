#File handling

# a = 10
# print(a) #in this code, a will only store 10 when the programming (ram, rom):need for file handling

#read   :when using read command, the txt file should exit, other commands does not needed and they will create new file if that file not exist
#write  :replace the existing content with the given content
#append :add the given content with the existing content

#read

# file = open('demo.txt','r')
# print(file.read())
# file.close()

# #write

# # file = open('demo.txt','w')
# # file.write('Hello World')
# # file.close()

# #append

# file = open('demo.txt','a')
# file.write('123\n')
# file.close()


#Q read name and age of 10 students and write it to a file


# mine
file = open('demo1.txt','a')
for i in range(1,11):
    name = input(f'enter student name {i}: ')
    age = input(f'age: ')
    file.write(name)
    file.write(': ')
    file.write(str(age))
    file.write('\n')
file.close()

#sir

# file = open('demo1.txt','a')
# for i in range(1,3  ):
#     name = input(f'enter student name {i}: ')
#     age = input(f'age: ')
#     file.write(name + ' '+ str(age) + '\n')
# file.close()




# with open('demo.txt','r') as file:            # diff from above is that this will auto close 
#     print(file.read())


# with open('demo1.txt','r') as file:            
#     print(file.readlines())
 

with open('dem.txt','r') as file:

    line = file.readlines()
    for i in range(len(line)):
        name = line[i]
        name_and_age = (name.strip('\n'))
        name_with_age = name_and_age.split(' ')
        print(name_and_age)
        print(name_with_age[0])
        print(name_with_age[1])

        
