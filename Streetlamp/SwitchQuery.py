from LampIO import SwitchRead

#Catch when script is interrupted, cleanup correctly
try:
	# Main loop
	while True:
		print SwitchRead()		
except KeyboardInterrupt:
	pass
