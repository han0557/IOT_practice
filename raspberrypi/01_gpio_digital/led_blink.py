import RPi.GPIO as GPIO
import time

LED_PIN_RED = 6
# LED_PIN_GREEN =22
# LED_PIN_YELLOW=2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
# GPIO.setup(LED_PIN_YELLOW, GPIO.OUT)
# GPIO.setup(LED_PIN_RED, GPIO.OUT)

# while(1):
GPIO.output(LED_PIN_RED, GPIO.HIGH)
#     print("RED led on")
time.sleep(1)
GPIO.output(LED_PIN_RED, GPIO.LOW)
#     print("RED led off")
time.sleep(1)

#     GPIO.output(LED_PIN_YELLOW, GPIO.HIGH)
#     print("Yello led on")
#     time.sleep(0.05)
#     GPIO.output(LED_PIN_YELLOW, GPIO.LOW)
#     print("Yello led off")
#     time.sleep(0.05)

#     GPIO.output(LED_PIN_GREEN, GPIO.HIGH)
#     print("Green led on")
#     time.sleep(0.05)
#     GPIO.output(LED_PIN_GREEN, GPIO.LOW)
#     print("Greenled off")
#     time.sleep(0.05)
    

GPIO.cleanup()