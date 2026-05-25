import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Voice speed
engine.setProperty("rate", 170)

# Select voice
voices = engine.getProperty("voices")

engine.setProperty(
    "voice",
    voices[0].id
)

# Speak function
def speak(text):

    print(f"\nJARVIS: {text}\n")

    engine.say(text)

    engine.runAndWait()