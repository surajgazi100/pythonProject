from colorama import Fore
from greet import  greeting_msg
import pyttsx3
import os
from help_module import helping
from game import play_game
import random
from movie_module import play_movies
from music_module import play_music
from speak_module import speak
from whatsapp import whatsapp
from email_module import get_emailId, sending_mail
from text_module import sending_text
import webbrowser

os.system("cls")
cmd = "Enter Command: "
print("--------------------------------***---------------------------------------")

speak("Please Enter your name")
name = input(Fore.GREEN + "Enter your name: " + Fore.RESET)
msg = greeting_msg(name)
print(Fore.GREEN + msg + Fore.RESET)
speak(msg)
print(Fore.GREEN + "What can I help you." + Fore.RESET)
speak("What can I help for you.")
print()

thank = ["My pleasure ", "Anytime ", "Anything for you ", "Mention Not ", "Welcome "]
while(True):
    x = input(Fore.RED + cmd + Fore.RESET)
    x = x.lower()
    if len (x) <= 0:
        print (Fore.CYAN + "Please Enter a command" + Fore.RESET)
        speak ("Please Enter a command")

    if "bye" in x or "quit" in x or "cya" in x or "exit" in x:
        print (Fore.CYAN + "Bye!! See You Soon" + Fore.RESET)
        speak ("Bye!! See You Soon")
        exit ()
        if "help" in x:
            helping ()
            speak ("I can help you with above things")

        elif "thank you" in x or "thanks" in x:
            p = random.choice (thank) + name
            print (Fore.CYAN + p + Fore.RESET)
            speak (p)
    elif "games" in x or "game" in x:
        print(Fore.CYAN + play_game() + Fore.RESET)
        speak("Opening game")
    elif "movie" in x or "movies" in x:
        print (Fore.CYAN + "Opening Movie Menu" + Fore.RESET)
        speak ("Opening Movie Menu")
        p = play_movies ()
        print (Fore.CYAN + p + Fore.RESET)
        speak (p)
    elif "whatsapp" in x:
        whatsapp ()
    elif "mail" in x or "email" in x:
        name = x.replace ("send email to ", "")
        mail = get_emailId (name)
        if mail == '0':
            print ("Email Id not found in database, please input mail id")
            mail = input ("Enter mail: ")
            print ("Mail id inserted to database")

            print (Fore.CYAN + "Enter message to send to " + name + Fore.RESET)
            msg = input ()

            print (sending_mail (name, mail, msg))

        elif "text" in x and "msg" in x:
            number = input (Fore.CYAN + "Enter Contact Number: ")
            print (Fore.CYAN + "Enter message to send to " + number + Fore.RESET)
            msg = input ()
            print (sending_text (msg, number))
    elif "music" in x or "song" in x:
        print(Fore.CYAN + "Playing Music" + Fore.RESET)
        speak("Playing Music")
        print(Fore.CYAN + play_music() + Fore.RESET)
    elif "calci" in x or "calculator" in x:
        print (Fore.CYAN + "Opening Calculator" + Fore.RESET)
        speak ("Opening Calculator")
        os.system ("calc")
    elif ("run" in x or "execute" in x or "open" in x) and "chrome" in x:
        print (Fore.CYAN + "Opening Chrome" + Fore.RESET)
        speak ("Opening Chrome")
        os.system ("chrome")


    elif ("run" in x or "execute" in x or "open" in x) and ("editor" in x or "notepad" in x or "text" in x):
        print (Fore.CYAN + "Opening Notepad" + Fore.RESET)
        speak ("Opening Notepad")
        os.system ("notepad")

    elif ("run" in x or "execute" in x or "open" in x) and ("editor" in x or "sublime" in x or "text" in x):
        print (Fore.CYAN + "Opening Sublime" + Fore.RESET)
        speak ("Opening Sublime")
        os.system ("sublime_text")

    elif ("youtube") in x:
        webbrowser.open("youtube.com")

        speak ("Opening Youtube")


    elif ("github") in x:
        webbrowser.open ("github.com")
        speak ("Opening GitHub")


    elif ("linkedin") in x:
        print (Fore.CYAN + "Opening LinkedIn" + Fore.RESET)
        speak ("Opening Youtube")


    elif ("google") in x:
        print (Fore.CYAN + "Opening Google" + Fore.RESET)
        speak ("Opening Google")
        os.system ("chrome google.com")

    elif "do not" in x or "don't" in x or "not" in x or "dont" in x or "donot" in x:
        print (Fore.CYAN + "Okay!! I will not run this" + Fore.RESET)
        speak ("Okay!! I will not run this")

    else:
        print (Fore.CYAN + "Right Now Not Supported!! Will be availabe in future" + Fore.RESET)
        speak ("Right Now Not Supported!! Will be availabe in future")