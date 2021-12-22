import spidev
import RPi.GPIO as GPIO
import time

Pin = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin, GPIO.OUT)

spi = spidev.SpiDev()

spi.open(0, 0)

spi.max_speed_hz = 100000

def analog_read(channel):
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        ldr_value = analog_read(0)
        print("LDR Value: %d" % ldr_value)
        if ldr_value<=512:
            GPIO.output(Pin, GPIO.HIGH)
        else : 
            GPIO.output(Pin, GPIO.LOW)
        time.sleep(0.5)    
finally:
    spi.close()
    GPIO.cleanup()
