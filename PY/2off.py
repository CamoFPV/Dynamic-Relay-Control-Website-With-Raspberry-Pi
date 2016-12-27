import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(3,GPIO.OUT)
    GPIO.output(3,GPIO.HIGH)
    return '<a href="./PHP/2on.php"><input type="button" class="MyButton" value="Relay 2"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay3.html', 'w')
print >> f, output
f.close()
