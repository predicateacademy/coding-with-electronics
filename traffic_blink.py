from gpiozero import LED
 
r = LED(23)
r.blink(on_time=1.0, off_time=1.0)
y = LED(12)
y.blink(on_time=1.0, off_time=1.0)
g = LED(21)
g.blink(on_time=1.0, off_time=1.0, background=False)
