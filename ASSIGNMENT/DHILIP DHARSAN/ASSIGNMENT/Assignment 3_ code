import time
import RPi.GPIO as GPIO       
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


while True:
	GPIO.output(11,True)  ## Turn on redLed
	time.sleep(1)         ## Wait for one second
	GPIO.output(11,False) ## Turn off redLed
	time.sleep(1)         ## Wait for one second
	GPIO.output(12,True)  ## Turn on yellowLed
	time.sleep(1)         ## Wait for one second
	GPIO.output(12,False) ## Turn off yellowLed
	time.sleep(1)         ## Wait for one second
	GPIO.output(13,True)  ## Turn on greenLed
	time.sleep(1)         ## Wait for one second
	GPIO.output(13,False) ## Turn off greenLed
	time.sleep(1)         ## Wait for one second
