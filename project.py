import speech_recognition as sr
import webbrowser
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
NEWS_API_KEY = "YOUR API KEY"

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_key ="YOUR API KEY")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis. Give short responses."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
    elif "news" in c:
        r = requests.get(f"https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}")
        data = r.json()
        headlines = [article["title"] for article in data["results"]]
        for h in headlines:
            print(h)
            speak(h)
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    try:
        speak("Initializing Jarvis....")
    except Exception as e:
        print("Speak failed:", e)

    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            word = r.recognize_google(audio)
            print("You said:", word)
            if word.lower() == "jarvis":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source, timeout=10, phrase_time_limit=10)
                    word = r.recognize_google(audio)
                processCommand(word)
        except sr.UnknownValueError:
            print("Could not understand, try again")
        except sr.WaitTimeoutError:
            print("Timeout, no speech detected")
        except Exception as e:
            print("Error:", type(e).__name__, e)



