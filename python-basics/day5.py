#1. print 1 to 10
"""for i in range(1,11):
    if i % 2 == 0:
        print(i)"""

#2.print 10 to 1 in reverse

"""for i in range(10,0,-1):
    print(i)"""

#3.print numbers divisible by 3 and 5(1 to 100)



#4.find sum of first 10 natural numbers using for loop

'''sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)'''

#5.find sum of fist n even numbers using for loop

"""sum = 0
n = int(input("enter value for n: "))
for i in range(1,n*2+1):
    if i % 2 == 0:
        sum = sum + i
print(sum)"""

#6. find factorial of a number using for loop (6=6*5*4*3*2*1)
fact = 1
'''n = int(input("enter value for n: "))
if n > 0:
    for i in range(n,0,-1):
        fact = fact * i
    print(fact)
elif n == 0:
    print(fact)
else: 
    print("not possible")'''



#7.print multiplication table of a number using for loop

'''n = int(input("enter value for n: "))
for i in range(1,11):
    print(f'{i} x {n} = {i*n}')'''


# string traversal using for loop

string1 = 'jishnumadhu'
"""for i in range(0,5):
    print(string1[i])"""


"""for i in range(len(string1)-1,-1,-1):
    print(string1[i])
"""

#print letters at even index


#print letters at odd index in reverse order

#print vowels in a given string

#count of vowels in a given string
