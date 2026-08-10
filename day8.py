#dictionary

dict1 = {'name':'sai',
         'age':20,
         'place':'hyd'}
print(type(dict))
print(dict1['name'])
dict1['name'] = 'sai kiran'
print(dict1['name'])


# dict1 = {'age':20,'place':'hyd'}
# dict1['name'] = 'sai kiran'
# dict1['age'] = 21
# dict1[322] = 'djsdk'

# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

for i in dict1.items():
    print(i)

# dict1.update({'name':'vipin','age':28})
# dict1.pop('age')
# dict1.popitem()  #remove last item from the dict
# print((dict1)
# dict1.clear())
# print(dict1.get('email','not found')) #if we ask to get a key which is not in the dict, it will not show error but prints None


# keys = ['name','age','place']
# dict2 = dict.fromkeys(keys,0)
# print(dict2)   this will create a new dict with given keys and all the values will be 0 and mostly used in filling forms in website


keys = [1,2,3,4,5,6,7,8,9,10]
# dict1 = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}


# #print even keys and their valurs
for key,value in dict1.items():
    if key % 2 == 0:
        print(f)

#2.find largest value and its key

#3.dict1 = {'phy':50,'che':60,'math':70}
#   find total marks
# print marks >=60

