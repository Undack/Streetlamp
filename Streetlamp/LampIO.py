def LampOn():
	import RPi.GPIO as GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, 1)

def LampOff():
	import RPi.GPIO as GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, 0)
	
def SensorRead():
	import RPi.GPIO as GPIO
	import time
	GPIO.setwarnings(False)
	count = 0
	GPIO.setmode(GPIO.BCM)
  
	#Output on the pin for 
	GPIO.setup(4, GPIO.OUT)
	GPIO.output(4, GPIO.LOW)
	time.sleep(0.1)

	#Change the pin back to input
	GPIO.setup(4, GPIO.IN)
  
	#Count until the pin goes high
	while (GPIO.input(4) == GPIO.LOW):
		count += 1
	GPIO.cleanup()
	
	return count
	
def SwitchRead():
	import RPi.GPIO as GPIO
	import time
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	time.sleep(0.1)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#Because i use the internal pull up resistor, the switch reads low
	#when it's high, this bit swaps that to make it less confusing 
	if GPIO.input(18) == False:
		SwitchState = 1
	else:
		SwitchState = 0
	return SwitchState
	GPIO.cleanup()
