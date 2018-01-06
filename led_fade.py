from gpiozero import PWMLED

led = PWMLED(20)

# n = None pulses forever
led.pulse(fade_in_time=1.0, fade_out_time=1.0, n=5, background=False)

