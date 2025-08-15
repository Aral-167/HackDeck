# main.py

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.macros import Delay

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# 9 switches on these pins
PINS = [
    board.D7, board.D10, board.D4,
    board.D8, board.D9, board.D5,
    board.D1, board.D2, board.D3,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # Win+R → open Google
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "https://google.com", Tap(KC.ENTER)
        ),
        # Win+R → open Gmail
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "https://mail.google.com", Tap(KC.ENTER)
        ),
        # Win+R → open YouTube
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "https://youtube.com", Tap(KC.ENTER)
        ),
        # Win+R → open GitHub
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "https://github.com", Tap(KC.ENTER)
        ),
        # Win+R → open ChatGPT
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "https://chat.openai.com", Tap(KC.ENTER)
        ),
        # Win+R → open WhatsApp
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "whatsapp:", Tap(KC.ENTER)
        ),
        # Win+R → open VS Code
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(600),
            "code", Tap(KC.ENTER)
        ),

        KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
