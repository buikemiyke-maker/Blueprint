"""
Firmware: 6-Key Macropad with Rotary Encoder
MCU: Seeed XIAO RP2040
Framework: KMK (CircuitPython)

Key layout:
Q  W  E
A  S  D
"""

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.direct import DirectPins
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# =========================
# Direct GPIO keys
# =========================
# Order MUST match physical wiring order
keyboard.matrix = DirectPins(
    pins=(
        board.GP26,  # SW1 -> Q
        board.GP27,  # SW2 -> W
        board.GP28,  # SW3 -> E
        board.GP29,  # SW4 -> A
        board.GP6,   # SW5 -> S
        board.GP7,   # SW6 -> D
    ),
    orientation=DiodeOrientation.COL2ROW,
)

# =========================
# Keymap (QWEASD)
# =========================
keyboard.keymap = [
    [
        KC.Q,
        KC.W,
        KC.E,
        KC.A,
        KC.S,
        KC.D,
    ]
]

# =========================
# Rotary Encoder
# =========================
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# Encoder pins: (A, B, Switch)
encoder.pins = (
    (board.GP0, board.GP1, board.GP2),
)

# Encoder behavior
encoder.map = [
    (
        KC.VOLD,  # Rotate CCW
        KC.VOLU,  # Rotate CW
        KC.MUTE,  # Press
    )
]

keyboard.go()
