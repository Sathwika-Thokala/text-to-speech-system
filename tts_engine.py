from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(text, output_file):

    language = 'en'

    speech = gTTS(
        text=text,
        lang=language,
        slow=False
    )

    speech.save(output_file)

    print("Playing audio...")

    playsound(output_file)
