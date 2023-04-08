from google_provider import *
from common import *


audio_file_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.flac"

GoogleProvider.initialize()
response = GoogleProvider.translate_uri(audio_file_uri)
common_functions.print_response(response)