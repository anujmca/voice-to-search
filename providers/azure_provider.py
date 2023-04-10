import azure.cognitiveservices.speech as speechsdk

# Set up the speech configuration
speech_key = "7797b65251994e6bbee0971789508f30"
service_region = "centralindia"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

print('say something...')

# Set up the audio input
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

# Set up the speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Recognize speech and print the result
result = speech_recognizer.recognize_once()

print('Okay, I heard you. Let me process it...')

print(result.text)



class AzureProvider:
    # Set up the speech configuration
    speech_key = "7797b65251994e6bbee0971789508f30"
    service_region = "centralindia"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)


    @staticmethod
    def initialize():
        pass

    @staticmethod
    def translate_mic(): #-> SpeechRecognitionResult:
        # Set up the audio input
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

        # Set up the speech recognizer
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # Recognize speech and print the result
        result = speech_recognizer.recognize_once()

        print('Okay, I heard you. Let me process it...')

        print(result.text)

