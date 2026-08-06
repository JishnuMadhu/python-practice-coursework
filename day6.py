#list : collection of different datatypes (list is immutable)

# list1 = [1,1,2,3,4,5,'sdfgh',3.5,[1,2,3,4],[1,2,3,4],True]
# print(list1[6][2])  #to access elments which is inside another element of a list we use [][]
# print(list1[0:8:2])


# #tuple : collection of different datatypes (tuple is immutable)
# tuple1 = (1,1,2,3,4,5,'sdfgh',3.5,[1,2,3,4],[1,2,3,4],True)

# for i in tuple1:
#     print(i)




#print even numbers from a list

# list2 = [1,2,3,4,5,6,7,8]
# for i in list2:
#     if i % 2 == 0:
#         print(i)


#print sum of all numbers in a list

# list2 = [1,2,3,4,5,6,7,8]
# sum = 0
# for i in list2:
#     sum += i
# print(sum)

#print elements at odd index from a list

# list2 = [1,2,3,4,5,6,7,8]
# length = len(list2)
# for i in range(0,length):
#     if i % 2 != 0:
#         print(list2[i])

#print all the elements in a list in reverse order

# list2 = [1,2,3,4,5,6,7,8]
# print(list2[7::-1])

#print sum of odd nos in a list

# list2 = [1,2,3,4,5,6,7,11]
# odd_sum = 0
# for i in list2:
#     if i % 2 != 0:
#         odd_sum += i
# print(odd_sum)


# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers.append(11)    # (value) value will be added to the end of the list)
# numbers.insert(0,0)   #(position,value) value will be added to the given position

# numbers.remove(10)
# numbers.pop(0)

# numbers.clear()

# numbers.extend([11,12,13,14])  #study diff btw append and extend 
# numbers = numbers + list1

# string1 = 'hi' +' '+ 'hello'


# print(numbers)


# main_list = [1,2,3,4,5,6,7,8,9,10]
# even = []
# odd = []
# for i in main_list:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'even elements are : {even}')
# print(f'odd elements are : {odd}')

#remove duplicates and add to a new list


# list1 = [1,1,2,2,3,4,5,5,6,7,8,9,9,10,'a','a']
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list1)
# print(list2)

#continue pass break

for i in range(1,11):
    if i == 5 or i == 7:
        #continue
        break
    else:
        print(i)

