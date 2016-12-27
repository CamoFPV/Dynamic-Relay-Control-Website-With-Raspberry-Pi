import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.HIGH)
    return '<a href="./PHP/3on.php"><input type="button" class="MyButton" value="Relay 3"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay4.html', 'w')
print >> f, output
f.close()
