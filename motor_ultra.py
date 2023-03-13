import RPi.GPIO as GPIO
import time

trig = 20
echo = 21
ir = 2
m1a = 17
m1b = 27
m2a = 10
m2b = 9

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(ir, GPIO.IN)
GPIO.setup(m1a, GPIO.OUT)
GPIO.setup(m1b, GPIO.OUT)
GPIO.setup(m2a, GPIO.OUT)
GPIO.setup(m2b, GPIO.OUT)
pwm_m1a = GPIO.PWM(m1a, 1000)
pwm_m1b = GPIO.PWM(m1b, 1000)
pwm_m2a = GPIO.PWM(m2a, 1000)
pwm_m2b = GPIO.PWM(m2b, 1000)

GPIO.setwarnings(False)

def m_c(a1,b1,a2,b2):
    pwm_m1a.start(a1)
    pwm_m1b.start(b1)
    pwm_m2a.start(a2)
    pwm_m2b.start(b2)

def ultra_distance():
    GPIO.output(trig,False)
    time.sleep(0.00002)
    GPIO.output(trig,True)
    time.sleep(0.00005)
    GPIO.output(trig,False)
    
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300)/2
    print(distance)
    return distance

try:
    while True:
        if(ultra_distance() > 10):
            m_c(20,0,20,0)
            time.sleep(1.0)
        else:
            m_c(0,0,0,0)
            time.sleep(1.0)
        

except KeyboardInterrupt:
    print("Stopped by user!")
    GPIO.cleanup()