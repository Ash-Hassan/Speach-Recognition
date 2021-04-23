import numpy as np
from scipy.io import wavfile
from python_speech_features import mfcc
import speech_recognition as sr

recognize = sr.Recognizer()
with sr.Microphone() as source:
    print("Now Recording...")
    recognize.adjust_for_ambient_noise(source)
    audio = recognize.record(source, duration=10)
    print("Done Now Converting....")
print(recognize.recognize_google(audio))

with open("Output.wav", "wb") as f:
    f.write(audio.get_wav_data())
f.close()
print("File has been Made")