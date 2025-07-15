# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# The RGB extension for a single SK6812 LED
# Assuming the data pin for the LED is connected to D6
rgb = RGB(
    pixel_pin=board.D6,
    num_pixels=1,
)
keyboard.extensions.append(rgb)

# Define your pins here for 9 switches!
# Using D0-D5 and D7-D9, leaving D6 for the LED
PINS = [
    board.D0, board.D1, board.D2,
    board.D3, board.D4, board.D5,
    board.D7, board.D8, board.D9,
]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        # Copies selected text, then opens Google
        KC.MACRO(
            Press(KC.LGUI),
            Tap(KC.R),
            Release(KC.LGUI),
            KC.MACRO_SLEEP_MS(200),
            'https://google.com',
            Tap(KC.ENTER)
        ),
        # Copies selected text, then opens YouTube
        KC.MACRO(
            Press(KC.LGUI),
            Tap(KC.R),
            Release(KC.LGUI),
            KC.MACRO_SLEEP_MS(200),
            'https://youtube.com',
            Tap(KC.ENTER)
        ),
        # Opens GitHub
        KC.MACRO(
            Press(KC.LGUI),
            Tap(KC.R),
            Release(KC.LGUI),
            KC.MACRO_SLEEP_MS(200),
            'https://github.com',
            Tap(KC.ENTER)
        ),
        # Opens ChatGPT
        KC.MACRO(
            Press(KC.LGUI),
            Tap(KC.R),
            Release(KC.LGUI),
            KC.MACRO_SLEEP_MS(200),
            'https://chat.openai.com',
            Tap(KC.ENTER)
        ),
        KC.E, KC.F,
        KC.RGB_TOG, KC.RGB_HUI, KC.RGB_SAI,  # Toggle, Hue+, Saturation+
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()