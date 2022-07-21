import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
from selenium import webdriver
#if you wnt to add gui intro use this #make another file and put it in same folder
from gui import play_gif

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'coding' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

#paste your file or apllication path
        elif 'play music' in query:
            music_dir = 'C:\Program Files\music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing music")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'visual studio' in query:
            visualstudio = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019.lnk'
            speak("opening visual studio")
            os.startfile(visualstudio)

        elif 'my computer' in query:
            codepath = 'C:\Program Files'
            speak("opening my computer")
            os.startfile(codepath)

        elif 'movies' in query:
            movies = 'D:\movies'
            speak("opening movies")
            os.startfile(movies)

        elif 'software' in query:
            software = 'D:\softwares'
            speak("opening software")
            os.startfile(software)
            
        elif 'notepad' in query:
            notepad = 'F:\plans.txt'
            speak("opening notepad")
            os.startfile(notepad)
            
        elif 'chrome' in query:
            chrome = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
            speak("opening chrome")
            os.startfile(chrome)

        elif 'run' in query:
            run = r'C:\Users\Azan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Run.lnk'
            speak("opening run")
            os.startfile(run)
            
        elif 'cmd' in query:
            cmd = r'C:\Users\Azan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk'
            speak("opening cmd")
            os.startfile(cmd)
            
        elif 'weather'in query:
            driver = webdriver.Chrome()
            speak("opening weather")
            driver.get("https://www.timeanddate.com/weather/pakistan/sialkot")
            


            
        elif 'goodbye' in query:
            speak("good bye")
            sys.exit()
            
            
        elif 'restart' in query:
            speak("restarting")
            os.system("shutdown /r /t 1")
            
        elif 'shutdown'in query:
                speak("shutting down")
                os.system("shutdown /s /t 1")
    
        
