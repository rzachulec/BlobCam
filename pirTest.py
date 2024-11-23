from gpiozero import MotionSensor

pir = MotionSensor(4) # Tutaj wpisać numer wg. użytego pinu GPIO

while True:
	pir.wait_for_motion()
	print("You moved")
	pir.wait_for_no_motion()