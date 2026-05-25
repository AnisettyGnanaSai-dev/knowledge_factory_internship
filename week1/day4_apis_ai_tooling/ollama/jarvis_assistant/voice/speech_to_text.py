import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("\nListening...\n")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print(f"You: {text}")

        return text

    except sr.UnknownValueError:

        return None

    except sr.RequestError:

        return None