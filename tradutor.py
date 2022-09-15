"""
Módulo para lidar com o Google Translate.
"""

from googletrans import Translator


tradutor = Translator()


def traduzir(text, de='pt', para='en'):
    """
    Esta função recebe um texto e retorna sua tradução para uma linguagem desejada.
    :param text: str
    :param de: str
    :param para: str
    :return: str
    """
    traduzido = tradutor.translate(text, src=de, dest=para)
    return traduzido.text.capitalize()


if __name__ == "__main__":
    texto = traduzir('Olá este é um teste', de='pt', para='en')
    print(texto)
