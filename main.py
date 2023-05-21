from pynput import keyboard
from tkinter import filedialog
import os
import shutil

from functions import clear

import wave
import sys
import pyaudio


def reproducer():
    print("mp3 reproducer")
    chunk = 1024
    p = pyaudio.PyAudio()
    clear()
    print("Seleccione el archivo a reproducir:")
    files = os.listdir("./Audios")
    cont = 1
    for file in files:
        print(str(cont) + ": " + file)
        cont = cont + 1
    reproduce = input()
    cont2 = 1
    aud = ""
    for file in files:
        print(cont2)
        if cont2 == int(reproduce):
            print("nache")
            aud = file
        cont2 = cont2 + 1
    nombre_audio = r"./Audios/" + aud
    print(nombre_audio)
    
    print("Reproduciendo...\n **Controles:**\nPausar: p\nDespausar: o\nFinalizar reproducción: i")
    
    def on_press(key):
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.KeyCode.from_char('p'):
            pause()
        elif key == keyboard.KeyCode.from_char('o'):
            resume()
        elif key == keyboard.KeyCode.from_char('i'):
            stop()

        listener = keyboard.Listener(on_press=on_press)

        listener.start()

        while True:
            pass

    def pause():
        mixer.music.pause()
    def resume():
        mixer.music.unpause()
    def stop():
        stream.stop_stream()
        stream.close()




print("Iniciando...")
opcion = input("Seleccione una opcion:\n1. Agregar archivo\n2. Ver archivos\n3. Reproducir audio\n4. Salir")
if opcion == "1":
    add_file()
elif opcion == "2":
    list_files()
elif opcion == "3":
    reproducer()
elif opcion == "4":
    print("Saliendo...")
    exit()