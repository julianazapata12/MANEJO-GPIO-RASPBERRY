import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)   
GPIO.setup(11, GPIO.OUT)  
GPIO.setup(13, GPIO.OUT)  
GPIO.setup(15, GPIO.OUT)  


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
  	opcion=input("Ingrese 1 para encender secuencia 1 \n Ingrese 2 para encender secuencia 2 \n Ingrese 3 para encender secuencia 3 \n Ingrese 4 para encender secuencia 4 \n") 
  	if opcion=="1":
  		secuencia1()
  	elif opcion=="2":
  		secuencia2()
  	elif opcion=="3":
  		secuencia3()
  	elif opcion=="4":
  		secuencia4()
  	else: 
  		False 
