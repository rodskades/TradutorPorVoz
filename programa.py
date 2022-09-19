"""
Programa principal de tradução.
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
