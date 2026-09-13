#1.print letters at even index

string1= 'jishnumadhu'
length= len(string1)
for i in  range(0,length,2):
    print(string1[i])



#2.print letters at odd index in reverse order

string1= 'jishnumadhu'
length= len(string1)
for i in range(length-1,-1,-1):
    if i % 2 != 0:
        print(string1[i])


#3.print vowels in a given string

string1= 'jishnumadhu'
length= len(string1)
for i in range(0,length):
    if string1[i] in 'aeiou':
        print(string1[i])

#4.count of vowels in a given string

string1= 'jishnumadhu'
length= len(string1)
count= 0
for i in range(0,length):
    if string1[i] in 'aeiou':
        count +=1
print(count)