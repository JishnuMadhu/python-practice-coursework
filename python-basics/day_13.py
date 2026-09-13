# Recursion

#recursion function

#without return
# def nums(n):
#     if n == 0:
#         print(n)
#     else:
#         print(n)
#         nums(n-1)
# nums(10)

#with return

# def nums(n):
#     if n == 0:
#         return 0
#     else:
#         print
#         return nums(n-1)
# print(nums(15))


# def fact(n):
#    if n == 0:
#     return 1
#    else:
#     return n*fact(n-1)
# print(fact(5))

def sums(n,total_sum):
    if n == 0:
        return total_sum
    total_sum = total_sum + n
    total = sums(n-1,total_sum)
    return total

total_sum = 0
total = sums(10,total_sum)
print(total)


#lambda function

# add = lambda a:a    #lambda arguments: expression
# print(add(10))

#lambda func with condition
 
# x = lambda n : 'even' if n%2 == 0 else 'odd'
# print(x(10))


#without lamda
# list1 = [1,2,3,4,5,6,7,8,9,10]
# dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# dict1 = {}
# for i in list1:
#     dict1[i] = i*i
# print(dict1)

#with lamda using map func

# map function

# nums = [1,2,3,4,5,6,7,8,9,10]
# result = list(map(lambda x : x ** 2,nums))
# print(result)

#filter

# nums = [1,2,3,4,5,6,7,8,9,10]
# result = list(filter(lambda x : x%2 == 0,nums))
# print(result)

#names = ['apple','banana','cherry','avacado','grapes']

#1.print names starting with 'a' using filter  .startwith('a')

#2. print all names in uppercase using map

#3. print 1 to N numbers using recursion

#4. print sum of digits using recursion


#1
# result = list(filter(lambda x : x.startwith('a'),nums))
# print(result)

# #2


# #3.

# def rec():
    
# n = int(input('enter a number'))
# rec(n)







