# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    utils.speech_to_text.py

DESCRIÇÃO:
    Módulo para reconhecimento de fala com a biblioteca speech_recognition.

AUTOR:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>

"""

import speech_recognition as sr

rec = sr.Recognizer()


def microfones():
    """
    Esta função imprime todos os microfones disponíveis em uma lista.
    Na instância sr.Microphone(x), x deve ser o número na lista do microfone desejado de se usar.
    :return: print
    """
    lista = sr.Microphone().list_microphone_names()  # Lista de microfones disponíveis conectados ao computador.
    for i in range(len(lista)):
        print(f"{i}: {lista[i]}")


def escutar(lingua="pt-BR", micro=1):
    """
    Esta função capta e transforma em texto o áudio do microfone
    :param lingua: str
    :param micro: int
    :return: str
    """
    try:
        with sr.Microphone(micro) as mic:
            rec.adjust_for_ambient_noise(mic, duration=0.5)
            print("Next line.")
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language=lingua)
    except sr.UnknownValueError:
        texto = escutar()
    return texto


if __name__ == "__main__":
    text = escutar()
    print(text.capitalize())
