import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.direct import DirectPins
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

# Direct-pin setup (no matrix)
keyboard.matrix = DirectPins(
    pins=(
        board.GP26,  # SW1 -> W
        board.GP27,  # SW2 -> A
        board.GP28,  # SW3 -> S
        board.GP29,  # SW4 -> D
    ),
    orientation=DiodeOrientation.COL2ROW,
)

# Keymap (single layer)
keyboard.keymap = [
    [
        KC.W,
        KC.A,
        KC.S,
        KC.D,
    ]
]

if __name__ == '__main__':
    keyboard.go()
