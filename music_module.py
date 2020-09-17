import os
import random
from colorama import Fore

music_path = 'Music'
musics = os.listdir (r"D:\audio")


def play_music():
    p = random.choice (musics)
    os.startfile ("Aaina - Dil Ne Dil Se Kya Kaha" + p)
    return ("Playing one of my favourite song")