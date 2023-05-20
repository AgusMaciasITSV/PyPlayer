#import pyaudio, pynput
import os,sys
from pynput.keyboard import Key, Controller

#=========================SECCION DE FUNCIONES=========================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

keyboard = Controller()


def list_files():
    print("list files")
    files = os.listdir("./Audios")
    print("archivos en la carpeta Audios:")
    print(files)

#=========================SECCION DE MENUS=========================
#-------------------------Menu de seleccion de audio-------------------------
def browseMenu():
    browseSO = str(f"""
 ____  __     __   _  _     __   _  _  ____  __  __  
(  _ \(  )   / _\ ( \/ )   / _\ / )( \(    \(  )/  \ 
 ) __// (_/\/    \ )  /   /    \) \/ ( ) D ( )((  O )
(__)  \____/\_/\_/(__/    \_/\_/\____/(____/(__)\__/     
    {"-"*75}


    a) Open new file audio.
    z) Back to main menu""")
    browseS = browseSO
    while True:
        clear()
        print(browseS)
        x = input()
        browseS = browseSO
        if x == "a":
            browseS = browseS+"\n\nFlag1"
        elif x == "z":
            break
        else:
            browseS = browseS+"\n\n**Inserte una tecla valida"

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
            recordS = recordS+"\n\nFlag1"
        elif x == "s":
            recordS = recordS+"\n\nFlag2"
        elif x == "z":
            break
        else:
            recordS = recordS+"\n\n**Inserte una tecla valida"

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
