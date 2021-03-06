#auto feeder
 
#Code to run automatic fish feeder
import RPi.GPIO as GPIO
import time

import datetime

#camera config
from picamera import PiCamera
camera = PiCamera()
#adjust camera rotation
camera.rotation=180


for i in range(24): #####the number of times the code will iterate

    time.sleep(5)
    GPIO.setmode(GPIO.BOARD)

    control_pins=[7,11,13,15]

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)

    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]

#rotate stepper motor

    for j in range(73): ##########360 = 512
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

    GPIO.cleanup()

    #create string for current date and time
    now = str(datetime.datetime.now())
#take photo and save
#Preview for 2 seconds then capture photo.
    #camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/Desktop/ChumPics/ChumPic%s%d.jpg' % (now,i+1))
    #camera.stop_preview()

#tweet messages with images

    message= "Hello Chum! Eat up! %s %d" % (now,i+1)
    print("Tweeted: %s %s %d" % (message, now, i+1))
    time.sleep(500)#####MAKE THIS 86400 for 24 HOURS
