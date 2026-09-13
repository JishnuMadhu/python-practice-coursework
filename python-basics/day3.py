#membership operator

"""string1= 'jishnu'
num = int(input('Enter a number: '))  #type of input function is always a string
print(type(num))"""


#using in
char = input('Enter a letter: ')
if char in 'aeiouAEIOU':
    print('vowel')
else:
    print('consonants')

#using not in

char = input('Enter a letter: ')
vowels = 'aeiouAEIOU'
if char not in vowels:
    print('consonants')
else:
    print('vowels')




