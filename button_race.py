from gpiozero import Button
import sys
import time
goal = 100
pushes = 0


start_time = 0

# - button press event callbacks
def pressed_b1() :
   global start_time
   global pushes

   if pushes == 0:
      start_time = time.time()

        
   pushes = pushes + 1
   print pushes
   if pushes == goal:
      print('Completed in ' + str(time.time()-start_time) + ' seconds.')
      sys.exit(0)

# - create our buttons
b1 = Button(5, pull_up=True)


# - register callbacks with button
b1.when_pressed = pressed_b1

# - main loop. just sleep to keep program alive
while True:
	time.sleep(1)
