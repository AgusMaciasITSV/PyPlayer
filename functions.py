#import pyaudio, pynput
import os
from pynput.keyboard import Key, Controller
#-------------------------Menu principal-------------------------
def mainMenu():
    clear()
    print(f"""
    {"-"*75}
        ____              ____     __                               
       / __ \   __  __   / __ \   / /  ____ _   __  __  ___    _____
      / /_/ /  / / / /  / /_/ /  / /  / __ `/  / / / / / _ \  / ___/
     / ____/  / /_/ /  / ____/  / /  / /_/ /  / /_/ / /  __/ / /    
    /_/       \__, /  /_/      /_/   \__,_/   \__, /  \___/ /_/     
             /____/                          /____/                 
    {"-"*75}

    b) Open audio file
    c) Record audio file via microphone
    d) Exit
    """)
    

#-------------------------Menu de seleccion de audio-------------------------
def browseMenu(): 
    clear()
    print(f"""
 ____  __     __   _  _     __   _  _  ____  __  __  
(  _ \(  )   / _\ ( \/ )   / _\ / )( \(    \(  )/  \ 
 ) __// (_/\/    \ )  /   /    \) \/ ( ) D ( )((  O )
(__)  \____/\_/\_/(__/    \_/\_/\____/(____/(__)\__/     
    {"-"*75}


    o) Open new file audio.
    a) Back to main menu""")


#-------------------------Menu de grabacion-------------------------
def recordMenu():
    print(f"""
 ____  ____  ___  __  ____  ____     __   _  _  ____  __  __  
(  _ \(  __)/ __)/  \(  _ \(    \   / _\ / )( \(    \(  )/  \ 
 )   / ) _)( (__(  O ))   / ) D (  /    \) \/ ( ) D ( )((  O )
(__\_)(____)\___)\__/(__\_)(____/  \_/\_/\____/(____/(__)\__/ 
{"-"*75}

    1)Start Recording
    2)Open recordings
    3)Back to main menu
    """)


#=========================SECCION DE FUNCIONES=========================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

keyboard = Controller()





mainMenu()
