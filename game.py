import os
import random

games_path = 'Game'
games = os.listdir(r"C:\Users\SURAJ\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Autodesk")

def play_game():
    game = random.choice(games)
    game = "Game\\" + game
    cmd = "start " + game
    os.system(cmd)
    return "Opening game"