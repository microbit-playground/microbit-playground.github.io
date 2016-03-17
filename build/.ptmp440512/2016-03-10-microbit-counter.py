###                Downloaded From                
###           www.microbit-playground.co.uk           
from microbit import *

while True:
	display.scroll(str(button_a.get_presses()))
	sleep(10)
