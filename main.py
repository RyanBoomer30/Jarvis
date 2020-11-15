#https://www.youtube.com/watch?v=Lp9Ftuq2sVI&ab_channel=CodeWithHarry 39:00
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
#import smtplib
import time
from youtube_search import YoutubeSearch
import webbrowser
from Gmail import gmail

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 175)
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
switch = 0

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
        speak("How may I help you today")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon sir")
        speak("How may I help you today")
    else:
        speak("Good Evening sir")
        speak("How may I help you today")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.75
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        if (switch == 0):
            print("Say that again please...")
            return "None"
        elif (switch == 1):
            print("Say that again please...")
            speak("I could not hear that sir")
            return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'wake up' in query:
            switch = 1
            wishMe()
        elif 'introduce yourself' in query:
            speak("Hi, I am Jarvis, people like to think I am an AI but I am actually Ryan slave")
        elif 'look up' in query:
            search = query[query.find('look up')+8:]
            audio = "Looking up " + search
            speak(audio)
            query = query[query.find('look up'):]
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(query)
            engine.setProperty("rate", 165)
            audio = "According to Wikipedia" + results
            speak(audio)
            engine.setProperty("rate", 175)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
            speak("Opened youtube")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
            speak("Opened google")

        elif 'play' in query:
            search = query[query.find('play')+5:]
            results = YoutubeSearch(search, max_results=1).to_dict()
            for v in results:
                search_result = 'https://www.youtube.com/watch?v=' + v['id']
                webbrowser.get(chrome_path).open(search_result)

        elif 'shut down google' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, it is currently {time}")

        elif 'free' in query:
            speak("If we are not counting social media and Youtube, you average about 2 hours of free time during weekday and 6 hours during weekend")

        elif 'gmail' in query:
            gmail()

        elif 'sleep' in query:
            speak("I am going to take a nap")
            switch = 0
