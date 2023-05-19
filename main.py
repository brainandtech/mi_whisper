import whisper


from datetime import datetime


#Fecha actual

now = datetime.now()
print(now)

model = whisper.load_model("medium")
'''
result = model.transcribe("ignacio.m4a")
result = model.transcribe("audio66.mp3")
'
result = model.transcribe("validacion1.mkv")
# Guarda el texto en un fichero

# abre un fichero en modo escritura llamado "fichero.txt"
f = open ('fichero.txt','w')
f.write(result["text"])
f.close()

#print(result["text"])

'''





# leer todos los archivos de un directorio
import os
import glob

#for fichero in glob.glob("*.mkv"):
for fichero in glob.glob("*.mkv"):
    print('INICIO TRANSCRIPCION FICHERO: ' , fichero)
    print(datetime.now())
    result = model.transcribe(fichero)
    f = open (fichero+'.txt','w')
    f.write(result["text"])
    f.close()
    print('FIN TRANSCRIPCION FICHERO: ' , fichero)
    print(datetime.now())

 print('FIN TRABAJO')

'''
result1 = model.transcribe("jairo1.mkv")
f1 = open ('jairo1.txt','w')
f1.write(result1["text"])
f1.close()

now1 = datetime.now()
print(now1)



result2 = model.transcribe("jairo2.mkv")
f2 = open ('jairo2.txt','w')
f2.write(result2["text"])
f2.close()

now2 = datetime.now()
print(now2)

'''