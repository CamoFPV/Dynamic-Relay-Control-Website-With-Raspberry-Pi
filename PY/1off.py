import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2,GPIO.OUT)
    GPIO.output(2,GPIO.HIGH)
    return '<a href="./PHP/1on.php"><input type="button" class="MyButton" value="Relay 1"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay2.html', 'w')
print >> f, output
f.close()
