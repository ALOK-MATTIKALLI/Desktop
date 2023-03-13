
from xml.dom.expatbuilder import theDOMImplementation
import RPi.GPIO as GPIO
import time

m1a = 17
m1b = 27
m2a = 10
m2b = 9

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(m1a, GPIO.OUT)
GPIO.setup(m1b, GPIO.OUT)
GPIO.setup(m2a, GPIO.OUT)
GPIO.setup(m2b, GPIO.OUT)
pwm_m1a = GPIO.PWM(m1a, 100)
pwm_m1b = GPIO.PWM(m1b, 100)
pwm_m2a = GPIO.PWM(m2a, 100)
pwm_m2b = GPIO.PWM(m2b, 100)

GPIO.setwarnings(False)            #do not show any warnings
11
def m_c(a2,b2,a1,b1):
    pwm_m1a.start(a1)
    pwm_m1b.start(b1)
    pwm_m2a.start(a2)
    pwm_m2b.start(b2)

try:
    while 1:
        # forward
        m_c(20,0,20,0)
        time.sleep(1.0)
        m_c(0,0,0,0)
        time.sleep(0.5)
        # back
        m_c(0,20,0,20)
        time.sleep(1.0) 
        m_c(0,0,0,0)
        time.sleep(0.5)
        # right
        m_c(0,0,20,0)
        time.sleep(1.0)
        m_c(0,0,0,0)
        time.sleep(0.5)
        # left
        m_c(20,0,0,0)
        time.sleep(1.0)
        m_c(0,0,0,0)
        time.sleep(0.5)

except (KeyboardInterrupt):
    print("Stopped by user!")
    GPIO.cleanup()