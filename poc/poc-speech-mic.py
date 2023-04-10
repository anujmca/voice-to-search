from providers.google_provider import *
from common import *


GoogleProvider.initialize()
response = GoogleProvider.translate_mic()
common_functions.print_response(response)