import os
import whisper
from datetime import datetime


# Define the directory paths
audio_dir = "/media/disk1/2023/whisper/audios"
text_dir = "/media/disk1/2023/whisper/textos"



print('INICIO PROCESO: ', datetime.now())

model = whisper.load_model("medium")


# Loop through each file in the audio directory
for file in os.listdir(audio_dir):
    # Check if the file is an audio file
    #if file.endswith(".wav") or file.endswith(".mp3"):
    # Get the full file path
    audio_path = os.path.join(audio_dir, file)
    
    print ('Directorio: ', audio_path)
    print ('Fichero: ', file)
    # Transcribe the audio file
    print('INICIO TRANSCRIPCION FICHERO:' , file)
    print(datetime.now())
    transcribed_text = model.transcribe(audio_path)
    #transcribed_text = 'HOLA'
    
    # Get the name of the output text file
    text_file = os.path.splitext(file)[0] + ".txt"
    
    # Save the transcribed text to the text file
    text_path = os.path.join(text_dir, text_file)
    with open(text_path, "w") as f:
        f.write(transcribed_text["text"])
        f.close()    

    print('FIN TRANSCRIPCION FICHERO: ' , file)
    print(datetime.now())

print('FIN TRABAJO')
