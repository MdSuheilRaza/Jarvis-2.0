import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(Text):
    print("    ")
    print(f"Jarvis: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")