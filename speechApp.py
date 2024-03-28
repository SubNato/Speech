#Install the below to be able to use and access imports.

#pip install pyttsx3
#pip3 install speechrecognition
#pip install setuptools


#This code will accept user speech, convert it to text and after use that repeat it to the user.

import speech_recognition as speech
import pyttsx3


#Below is the speech to text section of code
def recorder():
    recognizer = speech.Recognizer()     #Only initialize one at a time, or it won't be initialized correctly
    while(1):
        try:
        
            with speech.Microphone() as mic:
            
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                return text

        except speech.RequestError as e:
            print("Could not parse results {0}".format (e))
    
    return

def outputSpeech(text):
    speech = pyttsx3.init()
    
    speech.say(text)
    speech.runAndWait()
    return


while(1):
    text = recorder()
    outputSpeech(text)
