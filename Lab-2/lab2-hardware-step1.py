import sense_hat
from time import sleep, time

sense = sense_hat.SenseHat()
sense.clear()

# Variables for convenience and readability
up_key = sense_hat.DIRECTION_UP
down_key = sense_hat.DIRECTION_DOWN
left_key = sense_hat.DIRECTION_LEFT
right_key = sense_hat.DIRECTION_RIGHT
pressed = sense_hat.ACTION_PRESSED

initial = False
sense.show_letter("J")

####
# Main Loop
####

while True:
  # Clear joystick events
  sense.stick.get_events()
  events = sense.stick.get_events()
  if events:
    for e in events:

      if (e.direction ==  up_key or e.direction ==  down_key or e.direction ==  left_key or e.direction ==  right_key) and e.action == pressed:
        if initial == True:
          initial = False
          sense.show_letter("J")
        else:
          initial = True
          sense.show_letter("C")
