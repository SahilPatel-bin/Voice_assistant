import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None
    return query.lower()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your custom voice assistant. How can I assist you today?")

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def open_website(website_name):
    webbrowser.open(f"https://{website_name}.com")
    speak(f"Opening {website_name}")

def open_application(app_name):
    if app_name == "notepad":
        os.system("notepad")
        speak("Opening Notepad")
    elif app_name == "calculator":
        os.system("calc")
        speak("Opening Calculator")
    else:
        speak(f"Sorry, I can't open {app_name} right now.")

def main():
    greet_user()
    while True:
        query = listen()
        
        if query is None:
            continue
        
        if "time" in query:
            tell_time()

        elif "open" in query and "website" in query:
            speak("Which website would you like to open?")
            website = listen()
            if website:
                open_website(website)

        elif "open" in query and "application" in query:
            speak("Which application would you like to open?")
            app = listen()
            if app:
                open_application(app)

        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("Sorry, I don't know how to handle that command.")

main()