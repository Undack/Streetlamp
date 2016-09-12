from LampIO import SensorRead

#Catch when script is interrupted, cleanup correctly
try:
	# Main loop
	while True:
		print SensorRead()		
except KeyboardInterrupt:
	pass
