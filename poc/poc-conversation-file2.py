import os
from google.cloud import speech_v1p1beta1 as speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../providers/VoiceSearch-0f0d55cb68a9.json"
client = speech.SpeechClient()

speech_file = "../voice-files/spoofing-trader-conversation.wav"

with open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

diarization_config = speech.SpeakerDiarizationConfig(
    enable_speaker_diarization=True,
    min_speaker_count=2,
    max_speaker_count=10,
)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    # sample_rate_hertz=8000,
    # language_code="en-US",
    language_code="en-US",
    diarization_config=diarization_config,
)

print("Waiting for operation to complete...")
response = client.recognize(config=config, audio=audio)


for result in response.results:
    alternative = result.alternatives[0]
    print("Transcript: {}".format(alternative.transcript))
    # print("Speaker Tag: {}".format(alternative.speaker_tag))


# The transcript within each result is separate and sequential per result.
# However, the words list within an alternative includes all the words
# from all the results thus far. Thus, to get all the words with speaker
# tags, you only have to take the words list from the last result:
result = response.results[-1]

words_info = result.alternatives[0].words



# Printing out the output:
for word_info in words_info:
    print(
        "word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
    )


tag=1
speaker=""

for word_info in words_info:
    if word_info.speaker_tag==tag:
        speaker=speaker+" "+word_info.word

    else:
        print("speaker {}: {}".format(tag,speaker))
        tag=word_info.speaker_tag
        speaker=""+word_info.word

print("speaker {}: {}".format(tag,speaker))