#L10-Server web cu control vizual
#import picamera
#camera=picamera.PiCamera()

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

GPIO.output(7,1)
#camera.capture("/var/www/html/imag1.jpg")

