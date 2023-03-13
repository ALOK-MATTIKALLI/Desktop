# from xml.dom.expatbuilder import theDOMImplementation
import RPi.GPIO as GPIO
import time

trig = 20
echo = 21
ir = 2
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(ir, GPIO.IN)

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
    return distance

def ir_out():
    if (GPIO.input(ir) == 1):
        return 1
    else:
        return 0

try:
    while True:
        if (ir_out() == 1):
            ultra_dist = ultra_distance()
            print("Distance = %0.4f cms"%(ultra_dist) + "ir present")
            time.sleep(0.2)
        else:
            ultra_dist = ultra_distance()
            print("Distance = %0.4f cms"%(ultra_dist) + "ir absent")
            time.sleep(0.2)
        

except KeyboardInterrupt:
    print("Stopped by user!")
    GPIO.cleanup()