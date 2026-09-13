# 1. merge two dictionaries


# d1 = {'a':10,'b':20,'c':30}
# d2 = {'b':50,'c':30,'d':40}

# d3 = {}

# for i in d1:
#     d3[i] = d1[i]

# for i in d2:
#     if i in d3:
#         d3[i] = d3[i] + d2[i]
#     else:
#         d3[i] = d2[i]
# print(d3)
    


# 2.find the second largest numbers

# numbers = [10,25,15,40,25,30,40]

# largest = 0
# second = -1

# for i in numbers:
#     if i>largest:
#         largest = i
# for i in numbers:
#     if i > second and i<largest:
#         second = i
# print(second)


# 3.move zeros to the end

numbers = [0,5,0,2,8,0,3]

n = len(numbers)

a = 0
b = n-1
for i in numbers:
    if i == 0:
        


