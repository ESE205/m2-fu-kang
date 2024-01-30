import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Debug = '-debug' in sys.argv
if Debug:
    sys.argv.remove('-debug')


LED_PIN = 7
SWITCH_PIN = 12


Rate = 1
Duration = 15


if len(sys.argv) > 1:
    Rate = int(sys.argv[1])
if len(sys.argv) > 2:
    Duration = int(sys.argv[2])


GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

start_time = time.time()

while time.time() - start_time <= Duration:

    switch_state = GPIO.input(SWITCH_PIN)
    

    if switch_state:
        GPIO.output(LED_PIN, not GPIO.input(LED_PIN)) 
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
    

    with open('data.txt', 'a') as data:
        current_time = time.time()
        data.write(f'{current_time:1.0f} {switch_state}\n')
        if Debug:
            print(f'Time: {current_time:1.0f}, Switch State: {switch_state}')

    time.sleep(Rate)

GPIO.cleanup()
