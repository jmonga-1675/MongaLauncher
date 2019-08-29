import struct
import serial
import math
import time
import xbox

arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
controler = xbox.Joystick()

lastTrigVal = 0
while not controler.Back():
    trigVal = controler.rightTrigger()
    trigVal = int(round(trigVal * 255, 0))
    if trigVal != lastTrigVal:
        lastTrigVal = trigVal
        print("Sending val: ", trigVal)
        arduino.write(struct.pack('>2B', trigVal))
arduino.write(struct.pack('>B', 0))
