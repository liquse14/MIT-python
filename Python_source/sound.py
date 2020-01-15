import RPi.GPIO as GPIO
import time
SPEAKER = 25
C=261.63
D=293.66
E=329.63
F=349.23
G=391.00
A=440.00

notes=[
    [G,8],[G,8],[A,8],[A,8],[G,8],[G,8],[E,4],
    [G,8],[G,8],[E,8],[E,8],[E,8],[D,2],
    [G,8],[G,8],[A,8],[A,8],[G,8],[G,8],[E,4],
    [G,8],[E,8],[D,8],[E,8],[C,2]
    ]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SPEAKER,GPIO.OUT)
pwm=GPIO.PWM(SPEAKER,0.1)
pwm.start(50)
try:
    for i in notes:
        pwm.ChangeDutyCycle(50)
        pwm.ChangeFrequency(i[0])
        time.sleep(4/i[1]-0.01)
        pwm.ChangeDutyCycle(0)
        time.sleep(0.01)
except:
     print("error or Pessed [ctrl-c]")
finally:
    pwm.stop()
    GPIO.cleanup()
    pint("end")
                 