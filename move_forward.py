import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)
import serial 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()


 


def move_forward():
    ser.write(b"19\n")

    
while True:
    ser.flush()
    move_forward()
    time.sleep(1)
