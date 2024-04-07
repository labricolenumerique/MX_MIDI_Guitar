import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

switch = digitalio.DigitalInOut(board.D29)
switch.switch_to_input(pull=digitalio.Pull.UP)
print(switch.value)

if(switch.value == False):
    print("D29 selected")
