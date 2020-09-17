import os
from colorama import Fore
from speak_module import speak

phoneBook = {'shivam': '*********', 'home': '*********'}


def whatsapp():
    speak ("Enter name of the contact")
    name = input ("Enter name of the contact: ")
    if name in phoneBook.keys ():
        number = phoneBook[name]
    else:
        print ("Name not in Contact list")
        speak ("Name not in Contact list")
        speak ("Enter Number")
        number = input ("Enter Number: ")
        phoneBook[name] = number
        print ("Number added in Phonebook")
        speak ("Number added in Phonebook")

    speak ("Enter Message")
    msg = input ("Enter Message: ")
    cmd = "chrome wa.me/91" + number + "/?text=" + msg
    os.system (cmd)
