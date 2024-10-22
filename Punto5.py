import RPi.GPIO as GPIO 
import time 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.OUT)

while True :
  	if GPIO.input(5):
  		GPIO.output(7,False)
  	else:
  		print("pulsador presionado")
  		GPIO.output(7,True)
