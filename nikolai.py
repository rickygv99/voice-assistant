import speech_recognition as sr
import pyttsx3 as tts

import actions

BOT_NAME = "Nikolai"

# Initialization
r = sr.Recognizer()
engine_tts = tts.init()
print("Finished initializing. Say something into the microphone!")

while True:
    # Speech recognition
    with sr.Microphone() as source:
      audio = r.listen(source)

    try:
        input = r.recognize_sphinx(audio)

        if len(input) == 0:
            continue

        print(f"You: {input.capitalize()}")
    except sr.UnknownValueError:
        print(f"{BOT_NAME} could not understand what you said.")
    except sr.RequestError as e:
        print(f"Internal {BOT_NAME} error: {e}")

    # Query / command processing
    if input == "stop" or input == "end":
        break
    response = actions.execute(input)

    # Text to speech output
    print(f"{BOT_NAME}: {response}")
    engine_tts.say(str(response))
    engine_tts.runAndWait()
