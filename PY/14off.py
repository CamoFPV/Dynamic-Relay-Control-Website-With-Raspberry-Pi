import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.HIGH)
    return '<a href="./PHP/14on.php"><input type="button" class="MyButton" value="Relay 14"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay26.html', 'w')
print >> f, output
f.close()
