import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)
    return '<a href="./PHP/4on.php"><input type="button" class="MyButton" value="Relay 4"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay17.html', 'w')
print >> f, output
f.close()
