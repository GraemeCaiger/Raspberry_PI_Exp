from pms5003 import PMS5003
import RPi.GPIO as GPIO           # import RPi.GPIO module  
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(16, GPIO.OUT) # set a port/pin as an output   
GPIO.output(16, 1)       # set port/pin value to 1/GPIO.HIGH/True  

#GPIO.cleanup()                 # resets all GPIO ports used by this program  #



pms5003 = PMS5003()
# Configure the PMS5003 for Enviro+
pms5003 = PMS5003(
    device='/dev/ttyAMA0',
    baudrate=9600,
    pin_enable=38,
    pin_reset=27
)

try:
    while True:
        data = pms5003.read()
        print("PM2.5 ug/m3 (combustion particles, organic compounds, metals): {}".format(data.pm_ug_per_m3(2.5)))
except KeyboardInterrupt:
    pass