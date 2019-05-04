from picamera import PiCamera
from time import sleep

camera = PiCamera()

#adjust camera rotation
camera.rotation=180

#adjust camera transperancy alph 0 to 225
#camera.start_preview(alpha=200)

#stream video for 10 seconds
camera.start_preview()
sleep(10)
camera.stop_preview()

#Preview for 5 seconds then capture photo. need at least 2 seconds for sensors
#sleep(5)
#camera.capture('/home/pi/Desktop/CAMKEL.jpg')
#camera.stop_preview()

#capture 5 photos in a row
#camera.start_preview()
#for i in range(5):
#    sleep(5)
#    camera.capture('/home/pi/Desktop/BURST%s.jpg' % i)
#camera.stop_preview()

#record video for 10 seconds
#camera.start_preview()
#camera.start_recording('/home/pi/Desktop/CAMKEL.h264')
#sleep(10)
#camera.stop_recording()
#camera.stop_preview()
