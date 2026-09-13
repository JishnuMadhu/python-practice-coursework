1.

# *****
# *   *
# *   *
# *   *
# *****

n =int(input('enter a number: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == 1 or j == n or i == 1 or i == n:
            print('*', end ='')
        else:
            print(' ',end ='')
    print()





2.
    #     *
    #    ***
    #   *****
    #  *******
    # ********* 


n =int(input("enter a numbet"))
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end = '')
    for k in range(1,i * 2):
        print("*",end = '')
    print()
