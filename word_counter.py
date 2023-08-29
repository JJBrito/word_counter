# -*- coding: utf-8 -*-

# Imports
import string
import PySimpleGUI as sg

# Layout
sg.theme('DarkPurple4')
layout = [
    [sg.Text('Text'), sg.Input(key='text')],
    [sg.Button('Calculate')]
]

# Window
janela = sg.Window('Word Counter', layout)

# Logic test
while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Calculate':
        test_string = values['text']

        if not test_string:
            sg.popup_error("Required field!")
        else:
            res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])
            sg.popup("Word count: " + str(res))
# Main
janela.close()
