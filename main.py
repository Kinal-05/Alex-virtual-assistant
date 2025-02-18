import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

import musicLibrary

# pip install pocketshpinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "295e6880d70d43dc9d7961ff7b49619f"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #PArse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #Print the headlines
            for article in articles:
                speak(article['title'])


def listen_for_wake_word():
    """Continuously listens for the wake word 'Alex'."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening for 'Alex'...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=None)  # Always listening
                word = recognizer.recognize_google(audio).lower()
                print(f"Heard: {word}")

                if "alex" in word:
                    speak("Yes?")
                    listen_for_command()
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError:
                speak("Sorry, I'm having trouble connecting.")
            except Exception as e:
                print(f"Error: {e}")

def listen_for_command():
    """Listens for a command after hearing 'Alex'."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")

        try:
            audio = recognizer.listen(source, timeout=5)  # Give 5 seconds to speak
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            processCommand(command)
        except sr.UnknownValueError:
            speak("I didn't catch that. Can you repeat?")
        except sr.RequestError:
            speak("I'm having trouble connecting.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    speak("Initializing Alex...")
    listen_for_wake_word()