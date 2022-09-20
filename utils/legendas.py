# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    utils.legendas.py

DESCRIÇÃO:
    Módulo para organizar a legenda a partir de um texto recebido.

AUTOR:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>

"""


def subtitle(label, text, h=700):
    label.config(text=text)
    label.master.overrideredirect(True)
    label.master.geometry(f"+400+{h}")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "black")

# O programa principal deve ter o label definido da seguinte forma:
# label = tk.Label(text="", font=('Consolas', '30'), fg='DarkOrange2', bg='black')
