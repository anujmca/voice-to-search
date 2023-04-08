import io
import os

from google.cloud import speech

class common_functions:
    @staticmethod
    def print_response(response: speech.RecognizeResponse):
        for result in response.results:
            common_functions.print_result(result)


    @staticmethod
    def print_result(result: speech.SpeechRecognitionResult):
        best_alternative = result.alternatives[0]
        print("-" * 80)
        print(f"language_code: {result.language_code}")
        print(f"transcript:    {best_alternative.transcript}")
        print(f"confidence:    {best_alternative.confidence:.0%}")


class TwoChannelToMono:

    @staticmethod
    def convert(input_file_path, output_file_path):
        from pydub import AudioSegment
        sound = AudioSegment.from_wav(input_file_path)
        sound = sound.set_channels(1)
        sound.export(output_file_path, format="wav")