import pyaudio, wave, subprocess, threading
from pynput import keyboard

def audio_type(file_name):
    a = file_name.split(".")[-1]
    if a == "mp3":
        print("preparando para reproducir .mp3")
        if reproductor_mp3(file_name):
            return True
    elif a == "wav":
        print("preparando para reproducir .wav")
        if reproductor_wav(file_name):
            return True

def reproductor_mp3(file_name):
    CHUNK = 1024
    lock = threading.Lock()
    is_paused = False
    is_playing = True
    is_finished = False

    # Utilizamos el comando 'ffmpeg' para convertir el archivo MP3 a WAV temporalmente
    temp_wav_file = "temp.wav"
    subprocess.run(['ffmpeg', '-i', file_name, temp_wav_file])

    with wave.open(temp_wav_file, 'rb') as wf:
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        def on_press(key):
            nonlocal is_paused, is_playing, is_finished
            if key == keyboard.KeyCode.from_char('p'):
                lock.acquire()
                is_paused = False
                is_playing = False
                is_finished = True
                lock.release() 

            if key == keyboard.KeyCode.from_char('r'):
                is_paused = not is_paused
                if is_paused:
                    lock.acquire()
                    is_playing = False
                    lock.release()
                    print("Reproduccion pausada...")
                else:
                    lock.acquire()
                    is_playing = True
                    lock.release()
                    print("Reproduccion en progreso...")

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        while listener.running:
            while is_playing and not is_finished:
                data = wf.readframes(CHUNK)
                
                if len(data) == 0:
                    is_finished = True
                    break

                if not is_paused:
                    stream.write(data)
                
            if is_finished:
                stream.close()

                p.terminate()
                return True


    # Eliminar el archivo WAV temporal
    subprocess.run(['rm', temp_wav_file])


def reproductor_wav(file_name):
    CHUNK = 1024
    lock = threading.Lock()
    is_paused = False
    is_playing = True
    is_finished = False

    with wave.open(file_name, 'rb') as wf:
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        print()

        def on_press(key):
            nonlocal is_paused, is_playing, is_finished
            if key == keyboard.KeyCode.from_char('p'):
                lock.acquire()
                is_paused = False
                is_playing = False
                is_finished = True
                lock.release() 

            if key == keyboard.KeyCode.from_char('r'):
                is_paused = not is_paused
                if is_paused:
                    lock.acquire()
                    is_playing = False
                    lock.release()
                    print("Reproduccion pausada...")
                else:
                    lock.acquire()
                    is_playing = True
                    lock.release()
                    print("Reproduccion en progreso...")

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        while listener.running:
            while is_playing and not is_finished:
                data = wf.readframes(CHUNK)
                
                if len(data) == 0:
                    is_finished = True
                    break

                if not is_paused:
                    stream.write(data)
                
            if is_finished:
                stream.close()

                p.terminate()
                return True