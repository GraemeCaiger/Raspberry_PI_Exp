""" read me
    turning off servo is for preventing jitter on cheap servo but it does not give continious torqe to that location
    angle conversion is 2 +(angle/18) for angle between 0 and 180
"""
import RPi.GPIO as GPIO
import time

#set gpio numbering mode
GPIO.setmode(GPIO.BOARD)

#set pin 40 as output and pwm
GPIO.setup(40,GPIO.OUT)
servo_1 = GPIO.PWM(40,50) # pin 40 50 Hz pulse

# Start pwm running but with a value of 0 (pulse off)
servo_1.start(0)
print("waiting for 2 seconds")
time.sleep(2)

#move the servo
print("Rotating 180 degrees in 10 steps")

duty = 2

#duty 2-10 -> 0-180 degrees  duty cycle is just the percenage of time HIGH vs low for a pulse. there is an offset here because servos actually have a threshold pulse for which the pulse must belarger than before it will accept a value. 
while duty<=12:
    servo_1.ChangeDutyCycle(duty)
    time.sleep(0.3) # code enhnaces smootheness by giving time to get to locaiton. 
    servo_1.ChangeDutyCycle(0) # no pulse stops trying to move it 
    time.sleep(0.7)
    duty = duty + 1

time.sleep(2)
print("turning back to 90 degrees for 2 seconds" )
servo_1.ChangeDutyCycle(7)
time.sleep(0.5) # travel time wait
servo_1.ChangeDutyCycle(0)
time.sleep(1.5)

print("Turning back to zero")
servo_1.ChangeDutyCycle(2)
time.sleep(0.5)
servo_1.ChangeDutyCycle(0)

#clean up
servo_1.stop()
GPIO.cleanup()
print("goodbye")