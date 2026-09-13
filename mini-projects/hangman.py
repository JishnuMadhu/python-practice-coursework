#HANG MAN GAME

import random


print('hangman game')

malayalam_movies = [
    "Drishyam", "Drishyam 2", "Premam", "Bangalore Days", "Charlie",
    "Kumbalangi Nights", "Lucifer", "Ustad Hotel", "Spadikam", "Kilukkam",
    "Chithram", "Godfather", "Narasimham", "Pulimurugan", "Angamaly Diaries",
    "Maheshinte Prathikaram", "Jallikattu", "Virus", "Ayyappanum Koshiyum",
    "Kammatipaadam", "Vikramadithyan", "Amar Akbar Anthony", "Devasuram",
    "Aaraam Thampuran", "Kilichundan Mampazham", "CID Moosa", "Meesa Madhavan",
    "Rajamanikyam", "Punjabi House", "Runway", "Nadodikkattu", "Sandesham",
    "Ramji Rao Speaking", "Godha", "Neram", "North 24 Kaatham", "Traffic",
    "Memories", "Mumbai Police", "Anjaam Pathira", "Joji", "Nayattu", "Malik",
    "Hridayam", "Jana Gana Mana", "Minnal Murali", "Bheeshma Parvam",
    "Romancham", "RDX", "Manjummel Boys", "Aavesham", "Aadujeevitham",
    "Premalu", "Bramayugam", "Thudarum", "Chemmeen", "Nirmalyam",
    "Elippathayam", "Kireedam", "Kottayam Kunjachan", "His Highness Abdullah",
    "Aniyathipraavu", "Niram", "Vietnam Colony", "The King", "Valyettan",
    "Ravanaprabhu", "Naran", "Pokkiri Raja", "Anwar", "Salt N Pepper",
    "Beautiful", "Diamond Necklace", "22 Female Kottayam", "Ohm Shanthi Oshaana",
    "Mayaanadhi", "Sudani From Nigeria", "Thattathin Marayathu", "Uyare",
    "Helen", "Android Kunjappan", "Parava", "Two Countries", "Trance",
    "Driving Licence", "Classmates", "Njan Prakashan", "Oppam", "Pathemari",
    "Sufiyum Sujatayum", "Churuli", "Action Hero Biju", "Vellimoonga", "Aadu",
    "Thallumaala", "Manichitrathazhu", "Vandanam", "In Harihar Nagar",
    "Run Baby Run", "Jacobinte Swargarajyam"
]

movie = random.choice(malayalam_movies) #genetate random movie
movie = movie.lower()


char_chance = 6
movie_chance = 2
movie_as_list = list(movie)
guessed_letters = []


print(movie_as_list)

for i in movie_as_list:  #print '_'s 
    if i == ' ':
        print('  ',end = " ")
    else:
        print('_',end=' ')
print()



def guess_char(c):
        guessed_letters.append(c)

        for letter in movie_as_list:
            if letter in guessed_letters:
                print(letter,end='')
            elif letter == ' ':
                    print('  ',end='')
            else:
                    print('_',end=' ')
        print()
        
def check_win():
    for letter in movie_as_list:
        if letter == ' ':
            continue
        if letter not in guessed_letters:
            return False
    return True


while True:
    ch = int(input('1. Guess a lettern\n2. Guess the movie:-'))
    
    #to guess letters
    
    if ch == 1 and char_chance >0:
        char_guess = input('enter your character:-')
        if char_guess.lower() in movie_as_list:
            guess_char(char_guess.lower())
            if check_win():
                print(f'🎉 Congratulations!!!!!! You Won!\nThe movie was: {movie}')
                break

        else:
            char_chance = char_chance-1
            print(f'❌ Wrong letter!\nLetter chances left: {char_chance}\n')

    #to guess the movie
    
    elif ch == 2 and movie_chance >0:
         movie_guess = input('enter the movie name:-')

         if movie_guess.lower() == movie.lower():
              print(f'🎉 Congratulations!!!!!! You Won!\nThe movie was: {movie}')
              break
         else:
              movie_chance = movie_chance -1
              print(f'❌ Wrong movie!\nMovie chances left: {movie_chance}\n')
    elif ch not in [1,2]:
         print('invalid choice!!! Please enter correct choice!!!')

    if char_chance ==0 and movie_chance ==0:
         print(f'GAME OVER\nThe movie was {movie}')
         break


    