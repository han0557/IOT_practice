from lcd import drivers
import RPi.GPIO as GPIO
import time
import cv2
import threading


#opencv 설정
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("camera open faild")
    exit()

#초음파 센서 설정
TRIG_PIN = 4
ECHO_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

#피에조 부저 설정

BUZZER_PIN = 12
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 262)

#LCD 설정
display = drivers.Lcd()

#CAMERA 설정

#스위치 설정
BUTTON_PIN = 8
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#############스래드용 카메라 함수###################
def camera():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == 13:   
            break

camerath = threading.Thread(target = camera, args=())#스래드 선언
###################################################

try:
    camerath.start()##스래드 작동
    while True:
        val = GPIO.input(BUTTON_PIN)
        print(val)
########################초음파 센서 작동 코드##############################
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()
        duration_time = stop - start # 시간계산
        distance = duration_time * 17160 #거리
        print(distance)
##########################################################################
        if(val ==1):
            if (distance > 100): #문열림 상황
                pwm.start(70) # 피에조 부저 on
                display.lcd_display_string("Enemy Coming!!", 1)
                display.lcd_display_string("Warning!!",2)
                display.lcd_display_string("Warning!!",3)
                time.sleep(3)
                pwm.stop() # 피에조 부저 off
                display.lcd_clear()
            elif(distance <=100):
                time.sleep(1)
                
        elif(val == 0):
            display.lcd_display_string("Access!", 1)
            display.lcd_display_string("Access!", 2)
            display.lcd_display_string("Access!", 3)
            time.sleep(8)
            print('resting')
            display.lcd_clear()
            continue


finally:
    GPIO.cleanup()
    print("cleanup and exit")
    cap.release()
    cv2.destroyAllWindows()
    display.lcd_clear()