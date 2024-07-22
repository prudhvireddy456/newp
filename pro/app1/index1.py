import pyaudio
import deepgram
import google.generativeai as genai
from deepgram import DeepgramClient,PrerecordedOptions,FileSource,SpeakOptions
import time
API_KEY='AIzaSyAexHdX9nrYFMBPTW-bYoCdXM7sclJsofo'
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-pro")
stt =DeepgramClient('4a5edcdd5405c0ed4ce6a54071404a827142ce9c')
def get_gemini_response(question):
    response=model.generate_content(question)
    return str(response.text)
def get_audio(text):
    print(text)
    response=get_gemini_response(text)
    print(response)
    SPEAK_OPTIONS = {"text": response}
    filename ='output.wav'

    # Create the directory if it does not exis
    try:
        options = SpeakOptions(
        model="aura-asteria-en",
        encoding="linear16",
        container="wav"
        )
        res=stt.speak.v('1').save(filename, SPEAK_OPTIONS, options)
    except Exception as e:
        response = None
    return str(response)