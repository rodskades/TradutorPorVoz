# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    programa.py

DESCRIÇÃO:
    Programa que irá captar a voz a partir do microfone escolhido, traduzir para o idioma de escolha e finalmente
    apresentar o resultado na forma de uma legenda.

AUTOR:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
"""

from utils.speech_to_text import escutar, microfones
from utils.tradutor import traduzir

print("List of microfones that can be used: ")
microfones()
mic = int(input("Inform which microfone shall be used (0, 1, 2, etc..): "))
language_original = input("Inform the language of origin (en, pt, ja, etc...): ")
language_dest = input("Inform the language to translate to: ")


def main():
    text = escutar(lingua=language_original, micro=mic)
    translated = traduzir(text, de=language_original, para=language_dest)
    print(translated)
    main()


if __name__ == "__main__":
    main()
