#L10-Server web cu control vizual
#import picamera
#camera=picamera.PiCamera()

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)

GPIO.output(5,0)
#camera.capture("/var/www/html/imag1.jpg")

