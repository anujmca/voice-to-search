import azure.cognitiveservices.speech as speechsdk

# Set up the speech configuration
speech_key = "speech_key"
service_region = "service region"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set up the audio input
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

# Set up the speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Recognize speech and print the result
result = speech_recognizer.recognize_once()
print(result.text)
