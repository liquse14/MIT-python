import RPi.GPIO as GPIO     # GPIO 제어 모듈
import time                 # time 모듈

LED=17

GPIO.setmode(GPIO.BCM)      # BCM모드 설정
GPIO.setup(LED,GPIO.OUT)    # OUTPUT(출력) 설정

try:
    while True:
        GPIO.output(LED,False)
        print("LED OFF...")
        time.sleep(0.5)
        
        GPIO.output(LED,True)
        print("LED ON...")
        time.sleep(0.5)
        
except :
    GPIO.cleanup()
    print("end")