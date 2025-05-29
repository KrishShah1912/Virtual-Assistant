import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
from openai import OpenAI
from gtts import gTTS

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "9020ade6da8843fa83665ac80218ba08"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system" , "content" :"you are a virtual assistant Jarvis just like Alexa and Google Cloud, Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return (completion.choices[0].message)

    
def processCommand(c):
    if "open google"in c.lower():
        webbrowser.open("http://google.com")
        speak("Opening google")
    elif "open facebook"in c.lower():
        webbrowser.open("http://facebook.com")
        speak("Opening facebook")
    elif "open youtube"in c.lower():
        webbrowser.open("http://youtube.com")
        speak("Opening youtube")
    elif "open whatsapp"in c.lower():
        webbrowser.open("http://whatsapp.com")
        speak("Opening whatsapp")
    elif "open linkedin"in c.lower():
        webbrowser.open("http://linkedin.com")
        speak("Opening linkedin")
    elif "open instagram"in c.lower():
        webbrowser.open("http://instagram.com")
        speak("Opening instagram")
    elif "open snapchat"in c.lower():
        webbrowser.open("http://snapchat.com")
        speak("Opening snapchat")
    elif"open netflix"in c.lower():
        webbrowser.open("http://netflix.com")
        speak("Opening netflix")
    elif"open prime"in c.lower():
        webbrowser.open("https://www.primevideo.com/collection/IncludedwithPrime")
        speak("Opening Prime video")
    elif"open jiohotstar"in c.lower():
        webbrowser.open("http://jiohotstar.com")
        speak("Opening jiohotstar")
    elif"open sonyliv"in c.lower():
        webbrowser.open("http://sonyliv.com")
        speak("Opening sonyliv")
    elif"open gmail"in c.lower():
        webbrowser.open("http://gmail.com")
        speak("Opening gmail")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak(f"Yes Playing song {song}")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle this request
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Your Virtual Assistant Jarvis...")
    while True:
        # Listen for the wake up word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()


        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if (word.lower()== "jarvis"):
                speak("Yeah")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))