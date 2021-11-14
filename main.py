from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from time import sleep
import usb_hid, board

keyboard = Keyboard(usb_hid.devices)
led = DigitalInOut(board.GP25)
led.direction = Direction.OUTPUT

sleep(10)
keyboard.press(Keycode.ALT, Keycode.F4)
sleep(0.1)
keyboard.release(Keycode.ALT, Keycode.F4)
led.value = True
sleep(1)
led.value = False