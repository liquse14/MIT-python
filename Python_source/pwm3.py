import RPi.GPIO as GPIO
import time

LED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)

pwm = GPIO.PWM(LED,100)
#GPIO.PWM(BCM number,Frequency)
pwm.start(0)
#Duty Cycle=0

try:
        while True :
                    for value in range(0,1024) :
# 0 <=value<1024 반복문
                        pwm.ChangeDutyCycle(value / 10.23)
#ChangeDutyCylce(pwm값)
                        time.sleep(0.005)
except:
    pwm.stop()
    GPIO.cleanup()