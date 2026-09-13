# HANG MAN GAME

import random

print("HANG MAN GAME")
print()

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

char_chance = 6
movie_chance = 2
guessed_letters = []
movie_as_list = list(movie)


def display_movie():
    for letter in movie_as_list:
        if letter in guessed_letters:
            print(letter, end=" ")
        elif letter == " ":
            print("  ", end=" ")
        else:
            print("_", end=" ")
            
    print()


def guess_char(c):
    c = c.lower()
    guessed_letters.append(c)
    display_movie()




def check_win():
    for letter in movie_as_list:
        if letter == " ":
            continue
        if letter not in guessed_letters:
            return False
    return True


print("Guess the movie:")
display_movie()
print()



while True:

    print(f"Letter chances: {char_chance}")
    print(f"Movie chances: {movie_chance}")
    print()
    ch = int(input("1. Guess a letter\n2. Guess the movie\nEnter your choice: "))
    if ch == 1:

        if char_chance > 0:
            char_guess = input("Enter your character: ").lower()
            if len(char_guess) != 1:
                print("Please enter only one character.\n")
                continue

            if char_guess in guessed_letters:
                print("You already guessed that letter!\n")
                continue

            if char_guess in movie_as_list:

                guess_char(char_guess)

                print("Correct letter!\n")
                if check_win():
                    print(f"🎉 Congratulations!!!!!! You Won!")
                    print(f"The movie was: {movie}")
                    break
            else:
                char_chance = char_chance - 1
                print(f"❌ Wrong letter!")
                print(f"Letter chances left: {char_chance}\n")

        else:
            print("Your letter chances are over!")
            print("try to guess the movie.\n")

    elif ch == 2:

        if movie_chance > 0:
            movie_guess = input("Enter the movie name: ").lower()

            if movie_guess == movie:

                print()
                print("🎉 Congratulations!!!!!! You Won!")
                print(f"The movie was: {movie}")
                break

            else:
                movie_chance = movie_chance - 1
                print("❌ Wrong movie!")
                print(f"Movie chances left: {movie_chance}\n")

        else:
            print("Your movie guessing chances are over!")
            print("You can still guess letters.\n")
            
    else:
        print("Invalid choice! Please enter 1 or 2.\n")

    if char_chance == 0 and movie_chance == 0:
        print("\nGAME OVER!")
        print(f"The movie was: {movie}")
        break