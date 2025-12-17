import speech_recognition as sr
import time
import musicLibrary
import webbrowser as wb
import pyttsx3  # text to speech 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(txt):
    engine.say(txt)
    engine.runAndWait()
def process_command(c):
    if"open google" in c.lower():
        wb.open("https://google.com")
    elif"open youtube" in c.lower():
        wb.open("https://youtube.com")
    elif"open linkedin" in c.lower():
        wb.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        wb.open(link)


    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    # listen for the wake word Jarvis 
    while True:
        r = sr.Recognizer()
        
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening ...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                print("Wake word detected.")
                speak("Yes ma'am. I'm listening.")

                # listen for command 
                with sr.Microphone() as source:
                     print("Jarvis is active")
                     recognizer.adjust_for_ambient_noise(source)
                     audio = r.listen(source)
                     command = r.recognize_google(audio)

                     process_command(command)


        except Exception as e:
            print("Error")
    
