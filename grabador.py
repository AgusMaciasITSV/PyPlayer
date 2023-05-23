import pyaudio,wave, os
from pynput import keyboard
from datetime import datetime
from os import path

def recordAudio():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y%H:%M:%S")
    dt_string = dt_string.replace("/","")
    dt_string = dt_string.replace(":","")+".wav"

    chunk = 1024  
    formato = pyaudio.paInt16  
    canales = 1  
    tasa_muestreo = 44100  

    p = pyaudio.PyAudio()  


    stream = p.open(format=formato,
                    channels=canales,
                    rate=tasa_muestreo,
                    input=True,
                    frames_per_buffer=chunk)

    print("Presiona 'R' para iniciar o pausar la grabación, y presione 'ESC' para finalizar la grabación...")
    frames = []  
    grabando = False

    def on_press(key):
        nonlocal grabando
        if key == keyboard.Key.esc:
            return False  

        if key == keyboard.KeyCode.from_char('r'):
            grabando = not grabando
            if grabando:
                print("Grabación iniciada...")
            else:
                print("Grabación pausada...")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while listener.running:
        if grabando:
            data = stream.read(chunk)
            frames.append(data)

    print("Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    p.terminate()
    saveRecord()
    archivo_wav = wave.open(f"./Recordings/{dt_string}", 'wb')
    archivo_wav.setnchannels(canales)
    archivo_wav.setsampwidth(p.get_sample_size(formato))
    archivo_wav.setframerate(tasa_muestreo)
    archivo_wav.writeframes(b''.join(frames))
    archivo_wav.close()

    return f"Grabación guardada como '{dt_string}'."
    
def saveRecord():
    if path.isdir("./Recordings"):
        pass
    else:
        os.mkdir("./Recordings")