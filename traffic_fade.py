from gpiozero import PWMLED
 
r = PWMLED(23)
r.pulse(fade_in_time=1.0, fade_out_time=1.0)
y = PWMLED(12)
y.pulse(fade_in_time=1.0, fade_out_time=1.0)
g = PWMLED(21)
g.pulse(fade_in_time=1.0, fade_out_time=1.0, background=False)
