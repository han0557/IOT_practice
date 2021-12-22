from lcd import drivers
import Adafruit_DHT
import time
import datetime


display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
pin = 22


try:
    while True:
        now = datetime.datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        display.lcd_display_string(now.strftime("%x%X"),1)
        display.lcd_display_string(('%.1f*C, %.1f%%' %(temperature,humidity)), 2)
        
        time.sleep(0.5)
finally:
     print("Cleaning up!")
     display.lcd_clear()


