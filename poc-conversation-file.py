import os
import io
from google.cloud import speech_v1p1beta1 as speech

from common import TwoChannelToMono

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "VoiceSearch-0f0d55cb68a9.json"
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = "C:\\Projects\\RBS\\voice-to-search\\voice-files\\volleyball-convo-94227.wav"
mono_file_name = "C:\\Projects\\RBS\\voice-to-search\\voice-files\\volleyball-convo-94227_mono.wav"
# TwoChannelToMono.convert(file_name, mono_file_name)


# Read the audio file
with io.open(mono_file_name, "rb") as audio_file:
    content = audio_file.read()

# Configure the audio settings
audio = speech.types.RecognitionAudio(content=content)
config = speech.types.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    # sample_rate_hertz=16000,
    language_code="en-US",
    enable_speaker_diarization=True,
    diarization_speaker_count=2, # Set the number of speakers to detect
)

# Send the request to the Speech-to-Text API
response = client.recognize(config=config, audio=audio)

# Print the results
for result in response.results:
    alternative = result.alternatives[0]
    print("Transcript: {}".format(alternative.transcript))
    # print("Speaker Tag: {}".format(alternative.speaker_tag))
