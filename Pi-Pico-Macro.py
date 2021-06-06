#import librarys
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

#define both buttons
button1 = DigitalInOut(board.GP2)
button1.direction = Direction.INPUT
button1.pull = Pull.DOWN

button2 = DigitalInOut(board.GP3)
button2.direction = Direction.INPUT
button2.pull = Pull.DOWN

#initialize the keyboard
keyboard = Keyboard(usb_hid.devices)

while True:
    if button1.value:                           #look if button1 is pressed
        keyboard.press(Keycode.CONTROL)         #press control key
        keyboard.send(Keycode.C)                #press and release "C" key
        keyboard.release(Keycode.CONTROL)       #release control key
        time.sleep(0.5)                         #0.5s debounce time

    if button2.value:                           #look if button2 is pressed
        keyboard.press(Keycode.CONTROL)         #press control key
        keyboard.send(Keycode.V)                #press and release "V" key
        keyboard.release(Keycode.CONTROL)       #release control key
        time.sleep(0.5)                         #0.5s debounce time