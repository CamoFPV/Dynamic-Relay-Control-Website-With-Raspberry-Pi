import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.HIGH)
    return '<a href="./PHP/15on.php"><input type="button" class="MyButton" value="Relay 15"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay21.html', 'w')
print >> f, output
f.close()
