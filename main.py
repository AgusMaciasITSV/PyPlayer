from pynput import keyboard
from tkinter import filedialog
import os
import shutil

def add_file():
    print("add file")
    file = filedialog.askopenfile(mode='r', filetypes=[('MP3', '*.mp3')])
    if file:
        filepath = os.path.abspath(file.name)
        print(filepath)
        shutil.copy(filepath, "./Audios")
        print("archivo añadido a la carpeta Audios")

def list_files():
    print("list files")
    files = os.listdir("./Audios")
    print("archivos en la carpeta Audios:")
    print(files)
    

print("Iniciando...")
opcion = input("Seleccione una opcion:\n1. Agregar archivo\n2. Ver archivos\n3. Salir\n")
if opcion == "1":
    add_file()
elif opcion == "2":
    list_files()
elif opcion == "3":
    print("Saliendo...")
    exit()