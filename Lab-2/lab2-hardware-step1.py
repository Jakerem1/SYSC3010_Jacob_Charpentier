import sense_hat
from time import sleep, time

sense = sense_hat.SenseHat()
sense.clear()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

# Variables for convenience and readability
up_key = sense_hat.DIRECTION_UP
down_key = sense_hat.DIRECTION_DOWN
left_key = sense_hat.DIRECTION_LEFT
right_key = sense_hat.DIRECTION_RIGHT
pressed = sense_hat.ACTION_PRESSED

initial = False
sense.show_letter("T")

#Or create the letters through LED Init

def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

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
          sense.show_letter("T")
        else:
          initial = True
          sense.show_letter("A")
