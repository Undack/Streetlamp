from LampIO import *

while True:
	if SensorRead() > 2000:
		LampOn()
	else:
		LampOff()
