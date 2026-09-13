#sets :  unordered
#        does not allow duplicates
#        treats true and 1 as same
#        false and 0 as same
#        indexing ?

set1 = {1,2,3,4,5,6,7,8,9,10}

# str3 = '3'
# print(type(str3))
# int4 = int(str3)
# print(type(int4))



#set methods

set1.remove(1)
print(set1)
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))  #set1 | set2
print(set1.intersection(set2)) #set1 & set2
print(set1.difference(set2)) #set1 - set2

