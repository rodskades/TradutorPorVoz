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


def escutar(lingua="pt-BR", micro=1):
    """
    Esta função capta e transforma em texto o áudio do microfone
    :param lingua: str
    :param micro: int
    :return: str
    """
    try:
        with sr.Microphone(micro) as mic:
            rec.adjust_for_ambient_noise(mic)
            print("Next line.")
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language=lingua)
    except sr.UnknownValueError:
        escutar()
    return texto


if __name__ == "__main__":
    text = escutar()
    print(text.capitalize())
