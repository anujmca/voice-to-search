import os
import speech_recognition as sr



class SphinxProvider:
    @staticmethod
    def transcript_file():
        # Create a recognizer object
        r = sr.Recognizer()
        speech_file = "../voice-files/spoofing-trader-conversation.wav"
        file = sr.AudioFile(speech_file)

        with file as source:
            audio = r.record(source)
            print(f'sphinx: {r.recognize_sphinx(audio, language="en-Us")}')

    @staticmethod
    def transcript_mic():
        r = sr.Recognizer()

        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Speak something...")
            audio = r.listen(source)

        # Recognize speech using Sphinx
        try:
            text = r.recognize_sphinx(audio, language="en-Us")
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech")
        except sr.RequestError as e:
            print(f"Error: {e}")



SphinxProvider.transcript_file()