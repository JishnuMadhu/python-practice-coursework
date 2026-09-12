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

movie = random.choice(malayalam_movies)
movie = movie.lower()


# char_chance = 6
# movie_chance = 2
guessed_letters = []
movie_as_list = list(movie)


print(movie_as_list)
print()

for i in movie_as_list:
    if i == ' ':
        print(' ',end = " ")
    else:
        print('_',end=' ')
print()



def guess_char(c):
    if c.lower() in movie_as_list:
        guessed_letters.append(c)
        for letter in movie_as_list:
            if letter in guessed_letters:
                print(letter,end='')
            elif letter == ' ':
                    print(' ',end='')
            else:
                    print('_',end=' ')



        
char_guess = input('ente your character:-')
guess_char(char_guess)


# # def guess(movie_guess):
# #     if movie_guess.lower() == movie.lower():
# #         print('Congragulation!!!! You Won')
# #     else:
# #         movie_chance = movie_chance - 1
# #         print(f'Wrong guess, you have {movie_chance} chances left')



# # movie_guess = input('enter the movie name:-')
# # guess(movie_guess)

    


    