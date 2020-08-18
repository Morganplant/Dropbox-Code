from gtts import gTTS 
import subprocess

def Speach(text):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("Speach.mp3") 
    subprocess.call(["afplay", "Speach.mp3"])

Speach('hello World!')