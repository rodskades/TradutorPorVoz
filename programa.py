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
from utils.legendas import subtitle
import tkinter as tk

print("List of microfones that can be used: ")
microfones()
mic = int(input("Inform which microfone shall be used (0, 1, 2, etc..): "))
print("Input the languages to translate from -> to. Can be en, pt, ja, etc. See documentation for more. ")
language_original = input("Inform the language of origin: ")
language_dest = input("Inform the language to translate to: ")

label = tk.Label(text="", font=('Consolas', '30'), fg='DarkOrange2', bg='black')


def main():
    text = escutar(lingua=language_original, micro=mic)
    # print(text)
    traduzido = traduzir(text, de=language_original, para=language_dest)
    if len(traduzido) > 30:
        tmp1 = traduzido.split()
        tmp2 = {1: ' '.join(tmp1[0:int(len(tmp1) / 2)]), 3: ' '.join(tmp1[int(len(tmp1) / 2)::])}
        new_txt = ' '
        if len(tmp2[1]) > 30:
            tmp3 = dict()
            for i in tmp2.keys():
                tmp4 = tmp2[i].split()
                tmp3[i] = ' '.join(tmp4[0:int(len(tmp4) / 2)])
                tmp3[i+1] = ' '.join(tmp4[int(len(tmp4) / 2)::])
            for i in tmp3.keys():
                new_txt += tmp3[i] + '\n'
            subtitle(label, new_txt, 600)
        else:
            for i in tmp2.keys():
                new_txt += tmp2[i] + '\n'
            subtitle(label, new_txt)
    else:
        subtitle(label, traduzido)
    label.pack()
    label.after(50, lambda: main())
    label.mainloop()


if __name__ == "__main__":
    main()
