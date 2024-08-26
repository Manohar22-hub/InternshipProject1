
import speech_recognition as sr
import sounddevice as sd


def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None
    return command.lower()



import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

from datetime import datetime
def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")


def voice_typing():
    text = listen_command()
    if text:
        with open("voice_typing.txt", "a") as file:
            file.write(text + "\n")
        speak("Text has been written to the file.")


import webbrowser

def open_website(site_name):
    if "google" in site_name:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "youtube" in site_name:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    # Add more websites as needed

import os

def launch_application(app_name):
    if "notepad" in app_name:
        os.system("notepad")
        speak("Launching Notepad")
    elif "calculator" in app_name:
        os.system("calc")
        speak("Launching Calculator")
    # Add more applications as needed

import wikipedia

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for this query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find any information on this topic.")

def main():
    while True:
        command = listen_command()
        if command is None:
            continue

        if "time" in command:
            tell_time()
        elif "type" in command:
            voice_typing()
        elif "open" in command:
            open_website(command)
        elif "launch" in command:
            launch_application(command)
        elif "search" in command:
            search_wikipedia(command.replace("search", "").strip())
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't catch that. Please try again.")

if __name__ == "__main__":
    speak("Hello,I am Voice Assistance 2  How can I help you today?")
    main()


