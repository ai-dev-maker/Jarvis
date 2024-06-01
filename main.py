import speech_recognition as sr
import pyttsx3
import time
import webbrowser


def open_youtube():
    webbrowser.open("https://www.youtube.com/")


def open_chatGPT():
    webbrowser.open("https://chatgpt.com/")


def open_gdrive():
    webbrowser.open("https://drive.google.com/drive/u/0/my-drive")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"{query}")
            return query.lower()
        except sr.UnknownValueError:
            print("UnknownValueError")
            return None
        except sr.RequestError as e:
            print(f"Error recognition service: {e}")
            return None


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    print(f"Say: {text}")
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        command = listen()
        if command:
            if "jarvis" in command:
                if "open" in command:
                    if "youtube" in command:
                        speak('One moment, sir.')
                        open_youtube()
                    if "chat" in command:
                        speak('One moment, sir.')
                        open_chatGPT()
                    if "drive" in command:
                        speak('One moment, sir.')
                        open_gdrive()
                if "well" in command:
                    if "done" in command:
                        speak("Thank you, sir.")
                if "goodbye" in command:
                    speak("Okay, sir.")
                    exit()


if __name__ == "__main__":
    main()
