import pyaudio, pynput
import os,sys,shutil
from pynput.keyboard import Key, Controller
from tkinter import filedialog
from os import path
#=========================SECCION DE FUNCIONES=========================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def listFiles():
    files = os.listdir("./Audios")
    x = ""
    for y in files:
        x = x+"\n"+y
    return x

def listRecordings():
    if path.isdir("./Recordings"):
        files = os.listdir("./Recordings")
        x = ""
        for y in files:
            x = x+"\n"+y
        return x
    else:
        os.mkdir("./Recordings")
        files = os.listdir("./Recordings")
        x = ""
        for y in files:
            x = x+"\n"+y
        return x
    

def addFile():
    file = filedialog.askopenfile(mode='r', filetypes=[('MP3', '*.mp3'), ('WAV', '*.wav')])
    if file:
        filepath = os.path.abspath(file.name)
        print(filepath)
        shutil.copy(filepath, "./Audios")


#=========================SECCION DE MENUS=========================
#-------------------------Menu de seleccion de audio-------------------------
def browseMenu():
    browseSO = str(f"""
 ____  __     __   _  _     __   _  _  ____  __  __  
(  _ \(  )   / _\ ( \/ )   / _\ / )( \(    \(  )/  \ 
 ) __// (_/\/    \ )  /   /    \) \/ ( ) D ( )((  O )
(__)  \____/\_/\_/(__/    \_/\_/\____/(____/(__)\__/     
{"-"*75} 

    a) Open new file audio
    z) Back to main menu

    Audio list:
""")
    browseS = browseSO+listFiles()

    while True:
        clear()
        print(browseS)
        x = input()
        if x == "a":
            addFile()
            browseS = browseSO+listFiles()+"\nArchivo añadido satisfactoriamente"+"\n"
        elif x == "z":
            break
        else:
            browseS = browseS+"\n\n**Inserte una tecla valida"+"\n"

#-------------------------Menu de grabacion-------------------------
def recordMenu():
    recordSO = str(f"""
 ____  ____  ___  __  ____  ____     __   _  _  ____  __  __  
(  _ \(  __)/ __)/  \(  _ \(    \   / _\ / )( \(    \(  )/  \ 
 )   / ) _)( (__(  O ))   / ) D (  /    \) \/ ( ) D ( )((  O )
(__\_)(____)\___)\__/(__\_)(____/  \_/\_/\____/(____/(__)\__/ 
{"-"*75}

        a)Start Recording
        s)Open recordings
        z)Back to main menu
        """)
    recordS = recordSO
    while True:
        clear()
        print(recordS)
        x = input()
        recordS = recordSO
        if x == "a":
            recordS = recordS+"\n\nFlag1"+"\n"
        elif x == "s":
            recordingsMenu()
        elif x == "z":
            break
        else:
            recordS = recordS+"\n\n**Inserte una tecla valida"+"\n"

#-------------------------Menu de grabaciones-------------------------
def recordingsMenu():
    recordingsSO = str(f"""
 ____  ____  ___  __  ____  ____  __  __ _   ___   ____ 
(  _ \(  __)/ __)/  \(  _ \(    \(  )(  ( \ / __) / ___)
 )   / ) _)( (__(  O ))   / ) D ( )( /    /( (_ \ \___ \ 
(__\_)(____)\___)\__/(__\_)(____/(__)\_)__) \___/ (____/
{"-"*75}
    
    a) Flag 1
    z) Back to record audio menu

    Audio list:
    """)

    recordingsS = recordingsSO+listRecordings()+"\n"

    while True:
        clear()
        print(recordingsS)
        x = input()
        if x == "a":
            recordingsS = recordingsSO+listRecordings()+"\nFlag 1\n"
        elif x == "z":
            break
        else:
            recordingsS = recordingsSO+"\n\n**Inserte una tecla valida"+"\n"


#-------------------------Menu principal-------------------------
def mainMenu():
    menuSO = str(f"""
{"-"*75}
        ____              ____     __                               
       / __ \   __  __   / __ \   / /  ____ _   __  __  ___    _____
      / /_/ /  / / / /  / /_/ /  / /  / __ `/  / / / / / _ \  / ___/
     / ____/  / /_/ /  / ____/  / /  / /_/ /  / /_/ / /  __/ / /    
    /_/       \__, /  /_/      /_/   \__,_/   \__, /  \___/ /_/     
             /____/                          /____/                 
{"-"*75}

    a) Open audio file
    s) Record audio file via microphone
    z) Exit
    """)
    menuS = menuSO
    while True:
        clear()
        print(menuS)
        x = input()
        menuS = menuSO
        if x == "a":
            browseMenu()
        elif x == "s":
            recordMenu()
        elif x == "z":
            sys.exit()
        else:
            menuS = menuS+"\n\n**Inserte una tecla valida"

mainMenu()