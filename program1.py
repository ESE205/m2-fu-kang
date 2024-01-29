import RPi.GPIO as GPIO
from time import sleep
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1=12
pinLED=7

GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pinLED, GPIO.OUT, initial=GPIO.LOW)

start_time = time.time()

while True:
    if not GPIO.input(pin1):
        GPIO.output(pinLED, GPIO.LOW)
    if GPIO.input(pin1):
        GPIO.output(pinLED, GPIO.HIGH)
    if time.time() - start_time > 10:
        break
       

GPIO.cleanup()

