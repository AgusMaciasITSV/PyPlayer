import pyaudio
import wave
from pynput import keyboard

def grabar_audio(nombre_archivo):
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

    print("Presiona 'R' para iniciar o pausar la grabación...")
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

    archivo_wav = wave.open(nombre_archivo, 'wb')
    archivo_wav.setnchannels(canales)
    archivo_wav.setsampwidth(p.get_sample_size(formato))
    archivo_wav.setframerate(tasa_muestreo)
    archivo_wav.writeframes(b''.join(frames))
    archivo_wav.close()

    print(f"Grabación guardada como '{nombre_archivo}'.")

nombre_archivo = 'grabacion.wav'

grabar_audio(nombre_archivo)