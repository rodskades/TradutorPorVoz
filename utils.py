"""
Módulo para reconhecimento de fala.
"""

import speech_recognition as sr

rec = sr.Recognizer()

# print(sr.Microphone().list_microphone_names())  # Lista de microfones disponíveis conectados ao computador.

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("You may start / Pode começar a falar.")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
