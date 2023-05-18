#import pyaudio, pynput
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    clear()
    print("-"*75)
    print("""
        ____              ____     __                               
       / __ \   __  __   / __ \   / /  ____ _   __  __  ___    _____
      / /_/ /  / / / /  / /_/ /  / /  / __ `/  / / / / / _ \  / ___/
     / ____/  / /_/ /  / ____/  / /  / /_/ /  / /_/ / /  __/ / /    
    /_/       \__, /  /_/      /_/   \__,_/   \__, /  \___/ /_/     
             /____/                          /____/                 
    """)
    print("-"*75)
    print("""
    a) Play audio
    b) Open audio file
    c) Record audio file via microphone
    """)

def browseMenu():
    clear()
    print("""
 ____  __     __   _  _     __   _  _  ____  __  __  
(  _ \(  )   / _\ ( \/ )   / _\ / )( \(    \(  )/  \ 
 ) __// (_/\/    \ )  /   /    \) \/ ( ) D ( )((  O )
(__)  \____/\_/\_/(__/    \_/\_/\____/(____/(__)\__/     
    """)
    print("-"*75)
    print("""
    
    """)
def recordMenu():
    pass

mainMenu()
