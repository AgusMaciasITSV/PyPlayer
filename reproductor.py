import pyaudio, wave, subprocess
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
    grabando = False
    stream = None

    def iniciar_pausar_reproduccion():
        global grabando
        grabando = not grabando
        if grabando:
            print("Reproducción iniciada...")
        else:
            print("Reproducción pausada...")

    def finalizar_reproduccion(stream):
        global grabando
        grabando = False
        print("Reproducción finalizada.")
        stream.stop_stream()
        stream.close()

    def on_press(key):
        if key == keyboard.Key.esc:
            return False

        if key == keyboard.KeyCode.from_char('r'):
            iniciar_pausar_reproduccion()

        return True

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    with wave.open(file_name, 'rb') as wf:
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while listener.running:
            if grabando:
                stream.write(data)
            else:
                # Si no se está grabando, se lee el siguiente chunk del archivo para avanzar en la reproducción
                data = wf.readframes(CHUNK)

            if len(data) == 0:
                finalizar_reproduccion(stream)
                break

    listener.stop()
    p.terminate()