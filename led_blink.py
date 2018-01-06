from gpiozero import LED
import time
 
led = LED(20)
led.blink(on_time=1.0, off_time=1.0, n=10, background=False)

