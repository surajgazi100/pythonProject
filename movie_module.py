import os
import random
from colorama import Fore

movie_path = 'Movie'
movies = os.listdir (r"E:\data\LAPTOP-FOFTCQV4 03-08-2020 08.45.59")


def dis_Movies():
    print (Fore.RED + "******* Show Movies List ********" + Fore.RESET)
    i = 1
    for x in movies:
        print (Fore.BLUE + str (i) + ") " + x + Fore.RESET)
        i += 1


def play_movies():
    dis_Movies ()
    print ()
    print (Fore.RED + "Press 1 to Enter Movie Number you want to play" + Fore.RESET)
    print (Fore.RED + "Press 2 to play any random Movie" + Fore.RESET)
    print (Fore.RED + "Press 3 Exit from this menu" + Fore.RESET)
    x = int (input ("Enter Your Choice: "))
    if x == 1:
        p = int (input (Fore.BLUE + "Enter Movie Number: " + Fore.RESET))
        os.startfile ("Movie\\" + movies[p - 1])
        return ("Playing ", movies[p - 1])

    elif x == 2:
        p = random.choice (movies)
        os.startfile ("Movie\\" + p)
        return ("Playing one of my favourite movie")

    elif x == 3:
        pass

    else:
        print (Fore.RED + "Invalid Input!!" + Fore.RESET)
        play_movies ()