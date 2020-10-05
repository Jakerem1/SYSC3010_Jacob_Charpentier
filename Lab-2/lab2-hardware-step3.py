#In this example we are using the sensehat as the main hardware, and the LED display to
#represent the output, I am measuring the temperature as that is the goal for
#our final project, then recording it and outputing it to both a display and a database
#through thingspeak.

#This program is based off the tutorial by edureka! on youtube in the video, IoT Tutorial
#for Beginners|Internet of Things (IoT) | Iot Training | IoT Technology | Edureka, at
#https://www.youtube.com/watch?v=UrwbeOilc68

#The temperature reading is too high because it is on top of the CPU, in the project this
#will have to be solved, likely by cable connection instead of mounting connection.
from sense_hat import SenseHat
import time
from time import asctime

sense = SenseHat()

while True:
    #Only interested in the temperature currently
    temp = round(sense.get_temperature())
    message = ' T=%dC ' %(temp)
    
    #This would be changed to an LCD display, assuming multiple accessories can be paired at once
    sense.show_message(message, scroll_speed=(0.1), text_colour=[255,0,0], back_colour=[0,0,0])
    
    #This is an example of storing data, in the project it would be replaced with thingspeak
    log = open('temperature.txt',"a")
    now = str(asctime())
    log.write(now+' '+ message + "/n")
    print(message)
    log.close()
    
    #This is so that it checks every minute
    time.sleep(30) 