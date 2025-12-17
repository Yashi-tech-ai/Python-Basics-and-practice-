import pyttsx3
import time

engine = pyttsx3.init()

def speak(txt):
    engine.say(txt)
    engine.runAndWait()

speak("Yes ma'am")
time.sleep(1)
speak("I am your assistant.")
