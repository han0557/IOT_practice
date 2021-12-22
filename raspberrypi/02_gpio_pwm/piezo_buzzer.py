import RPi.GPIO as GPIO
import time

BUZZER=18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUZZER, GPIO.OUT)

melo = {'도' :262,
        '레' : 294,   
        '미' : 330, 
        '파' : 349, 
        '솔' : 392, 
        '라' : 440, 
        '시' : 494,
        '무' : 1}


a = "솔솔라라솔솔미무솔솔미미레무솔솔라라솔솔미무솔미레미도"    

pwm = GPIO.PWM(BUZZER, 262)

for i in a:
    pwm.start(99)
    pwm.ChangeFrequency(melo[i])
    time.sleep(0.5)
    pwm.stop()
    time.sleep(0.2)

GPIO.cleanup