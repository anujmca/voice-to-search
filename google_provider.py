import io
import os

import speech_recognition as sr
from google.cloud import speech


class GoogleProvider:
    config = speech.RecognitionConfig(
        language_code="en",
    )

    @staticmethod
    def initialize():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "VoiceSearch-0f0d55cb68a9.json"

    @staticmethod
    def translate_uri(uri) -> speech.RecognizeResponse:
        audio = speech.RecognitionAudio(
            uri=uri,
        )

        client = speech.SpeechClient()

        # Synchronous speech recognition request
        response = client.recognize(config=GoogleProvider.config, audio=audio)

        return response

    @staticmethod
    def translate_mic() -> speech.RecognizeResponse:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('say something...')
            r.adjust_for_ambient_noise(source)
            content = r.listen(source)
            print('Okay, I heard you. Let me process it...')
            audio = speech.RecognitionAudio(content=content.get_wav_data())


        client = speech.SpeechClient()

        # Synchronous speech recognition request
        response = client.recognize(config=GoogleProvider.config, audio=audio)

        return response
