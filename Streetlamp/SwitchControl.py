from LampIO import *

while True:
	if SwitchRead() == 1:
		LampOn()
	else:
		LampOff()
