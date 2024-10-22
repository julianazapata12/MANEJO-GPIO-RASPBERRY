import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)   
GPIO.setup(11, GPIO.OUT)  
GPIO.setup(13, GPIO.OUT)  
GPIO.setup(15, GPIO.OUT)  
GPIO.setup(31,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def secuencia1():
  	for x in range(3):
  		GPIO.output(7,True)
  		GPIO.output(11,True)
  		time.sleep(1)
  		GPIO.output(7,False)
  		GPIO.output(11,False)
  		time.sleep(1)
	

def secuencia2():
  	for x in range(3):
  		GPIO.output(13,True)
  		GPIO.output(15,True)
  		time.sleep(1)
  		GPIO.output(13,False)
  		GPIO.output(15,False)
  		time.sleep(1)

		
def secuencia3():
  	for x in range(6): 
  		GPIO.output(7,True)
  		GPIO.output(11,True)
  		GPIO.output(13,True)
  		GPIO.output(15,True)
  		time.sleep(0.3)
  		GPIO.output(7,False)
  		GPIO.output(11,False)
  		GPIO.output(13,False)
  		GPIO.output(15,False)
  		time.sleep(0.3)

def secuencia4():
  	for x in range(2): 
  		GPIO.output(7, True)
  		time.sleep(0.5)
  		GPIO.output(7, False)
  		time.sleep(0.5)
  		GPIO.output(11, True)
  		time.sleep(0.5)
  		GPIO.output(11, False)
  		time.sleep(0.5)
  		GPIO.output(13, True)
  		time.sleep(0.5)
  		GPIO.output(13, False)
  		time.sleep(0.5)
  		GPIO.output(15, True)
  		time.sleep(0.5)
  		GPIO.output(15, False)
  		time.sleep(0.5)

while True: 
  	if GPIO.input(37)==GPIO.LOW:
  		secuencia1()
  		time.sleep(0.5)
  	elif GPIO.input(35)==GPIO.LOW:
  		secuencia2()
  		time.sleep(0.5)
  	elif GPIO.input(33)==GPIO.LOW:
  		secuencia3()
  		time.sleep(0.5)
  	elif GPIO.input(31)==GPIO.LOW:
  		secuencia4()
  		time.sleep(0.5)
  	else: 
  		False 
