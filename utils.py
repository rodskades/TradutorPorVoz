"""
Módulo para reconhecimento de fala.
"""

import speech_recognition as sr

rec = sr.Recognizer()


def microfones():
    """
    Esta função imprime todos os microfones disponíveis em uma lista.
    Na instância sr.Microphone(x), x deve ser o número na lista do microfone desejado de se usar.
    :return: print
    """
    print(sr.Microphone().list_microphone_names())  # Lista de microfones disponíveis conectados ao computador.


def escutar():
    """
    Esta função capta e transforma em texto o áudio do microfone
    :return: str
    """
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("You may start / Pode começar a falar.")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
    return texto


if __name__ == "__main__":
    text = escutar()
    print(text.capitalize())
