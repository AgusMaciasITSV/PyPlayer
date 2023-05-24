import pyaudio, pynput,os,sys,shutil
from pynput.keyboard import Key, Controller
from tkinter import filedialog
from os import path
from grabador import recordAudio
from reproductor import audio_type
#=========================SECCION DE FUNCIONES=========================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def listFiles():
    if path.isdir("./Audios"):
        files = os.listdir("./Audios")
        x = ""
        i = 0
        for y in files:
            i +=1
            x = x+f"\n{i}. "+y
        return x
    else:
        os.mkdir("./Audios")
        files = os.listdir("./Audios")
        return "No hay ningun audio añadido!\n"

def listRecordings():
    if path.isdir("./Recordings"):
        files = os.listdir("./Recordings")
        x = ""
        i = 0
        for y in files:
            i +=1
            x = x+f"\n{i}. "+y
        if x == "":
            return "No hay ningun audio añadido!\n"
        else:
            return x
    else:
        os.mkdir("./Recordings")
        files = os.listdir("./Recordings")
        return "No hay ningun audio añadido!\n"
    

def addFile():
    file = filedialog.askopenfile(mode='r', filetypes=[('MP3', '*.mp3'), ('WAV', '*.wav')])
    if file:
        filepath = os.path.abspath(file.name)
        print(filepath)
        shutil.copy(filepath, "./Audios")

def selectableFile(fileList,input):
    try:
        y = int(input)
        x = fileList[y-1]
        return True
    except IndexError:
        return False
    except TypeError:
        return False
    
def selectedFile(fileList,input):
    y = int(input)
    x = fileList[y-1]
    return x
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
    files = os.listdir("./Audios")
    while True:
        #clear()
        print(browseS)
        x = input()
        if x == "a":
            addFile()
            browseS = browseSO+listFiles()+"\nArchivo añadido satisfactoriamente"+"\n"
        elif x == "z":
            break
        elif selectableFile(files,x):
            browseS = browseSO+"\nFLAG: El archivo puede ser seleccionado"+"\n"
            print("nache1")
            selected_file = files[int(x)-1]
            audio_path = os.path.join("./Audios", selected_file)
            audio_type(audio_path)
            print("nache")
        else:
            browseS = browseS+"\n\n**Inserte una tecla o numero valido"+"\n"

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
            clear()
            recordS = recordS+f"\n\n{recordAudio()}\n"
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

z) Back to record audio menu

Audio list:
    """)

    recordingsS = recordingsSO+listRecordings()+"\n"
    files = os.listdir("./Recordings")
    while True:
        clear()
        print(recordingsS)
        x = input()
        if x == "z":
            break
        elif selectableFile(files,x):
            recordingsS = recordingsSO+"\nFLAG: El archivo puede ser seleccionado"+"\n"
            #selectedFile(files,x) ---> devuelve un string con el nombre del archivo
        else:
            recordingsS = recordingsSO+"\n\n**Inserte una tecla o numero valido"+"\n"


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