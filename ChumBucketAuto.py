
#Code to run automatic fish feeder
import RPi.GPIO as GPIO
import time

import datetime

#twitter config
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)




#auto feeder

for i in range(3):

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


    for j in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

    GPIO.cleanup()

    now = str(datetime.datetime.now())
    message= "Hello Chum! %s %d" % (now,i+1)

    twitter.update_status(status=message)

    print("Tweeted: %s %s %d" % (message, now, i+1))


