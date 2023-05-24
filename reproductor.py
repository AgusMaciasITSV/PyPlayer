import pyaudio, wave, subprocess

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

    with wave.open(file_name, 'rb') as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        p = pyaudio.PyAudio()

        # Open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Play samples from the wave file (3)
        while True:
            data = wf.readframes(CHUNK)
            if len(data) == 0:
                # Finalizar la reproducción cuando se llega al final del archivo
                break

            # Verificar el valor ingresado por terminal
            user_input = input("Ingrese 'p' para pausar, 'r' para reanudar, o 'f' para finalizar: ")
            if user_input == 'p':
                # Pausar la reproducción
                while user_input != 'r':
                    user_input = input("Ingrese 'r' para reanudar: ")
            elif user_input == 'f':
                # Finalizar la reproducción
                break

            # Escribir los datos en el stream para reproducir el audio
            stream.write(data)

        # Cerrar stream (4)
        stream.close()

        # Liberar los recursos del sistema de PortAudio (5)
        p.terminate()