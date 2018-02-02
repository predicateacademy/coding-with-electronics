from gpiozero import Button
import tts
import time

# - create our buttons
b1 = Button(5, pull_up=True)

# - button press event callbacks
def pressed_b1() :
	tts.speak("ouch. that hurt.")

# - register callbacks with button
b1.when_pressed = pressed_b1

# - main loop. just sleep to keep program alive
while True:
	time.sleep(1)
