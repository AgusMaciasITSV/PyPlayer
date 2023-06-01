import pyaudio, wave, subprocess, threading
from pynput import keyboard

def audio_type(file_name):
    a = file_name.split(".")[-1]
    if a == "mp3":
        print("preparando para reproducir .mp3")
        reproductor_mp3(file_name)
    elif a == "wav":
        print("preparando para reproducir .wav")
        reproductor_wav(file_name)

def reproductor_mp3(file_name):
    CHUNK = 1024

    # Utilizamos el comando 'ffmpeg' para convertir el archivo MP3 a WAV temporalmente
    temp_wav_file = "temp.wav"
    subprocess.run(['ffmpeg', '-i', file_name, temp_wav_file])

    # Abrir el archivo WAV temporal para reproducción
    with wave.open(temp_wav_file, 'rb') as wf:
        # Instanciar PyAudio e inicializar los recursos del sistema de PortAudio
        p = pyaudio.PyAudio()

        # Abrir el stream de reproducción
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Reproducir las muestras del archivo WAV
        while len(data := wf.readframes(CHUNK)):
            stream.write(data)

        # Cerrar el stream
        stream.close()

        # Liberar los recursos del sistema de PortAudio
        p.terminate()

    # Eliminar el archivo WAV temporal
    subprocess.run(['rm', temp_wav_file])


def reproductor_wav(file_name):
    CHUNK = 1024
    lock = threading.Lock()
    is_paused = False
    is_finished = False

    with wave.open(file_name, 'rb') as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        p = pyaudio.PyAudio()

        # Open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        def on_press(key):
            nonlocal is_paused
            if key == keyboard.KeyCode.from_char('p'):
                lock.acquire()
                is_paused = False
                is_finished = True
                lock.release() 

            if key == keyboard.KeyCode.from_char('r'):
                is_paused = not is_paused
                if is_paused:
                    lock.acquire()
                    is_paused = True
                    lock.release()
                    print("Reproduccion pausada...")
                else:
                    lock.acquire()
                    is_paused = False
                    lock.release()
                    print("Reproduccion en progreso...")

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        while listener.running:
        # Play samples from the wave file (3)
            while True:
                data = wf.readframes(CHUNK)
                
                if len(data) == 0:
                    # Finalizar la reproducción cuando se llega al final del archivo
                    break
                    is_finished = True

                # Escribir los datos en el stream para reproducir el audio
                if not is_paused and not is_finished:
                    stream.write(data)
                
            # Cerrar stream (4)
            if is_finished:
                stream.close()

                # Liberar los recursos del sistema de PortAudio (5)
                p.terminate()