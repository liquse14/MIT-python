import RPi.GPIO as GPIO
import time

LED1 = 17
LED2 = 18
LED3 = 27
LED4 = 22

LED=[LED1,LED2,LED3,LED4]
delay = 0.1
GPIO.setmode(GPIO.BCM)

for i in LED :
        GPIO.setput(i,GPIO.OUT)
try :
    while True:
        for i in LED:
            GPIO.output(i,True)
            time.sleep(delay)
            GPIO.output(i,False)
            dleay-=0.001
            if delay <=0:
                delay=0.1
except:
    GPIO.cleanup()
    print("end")

