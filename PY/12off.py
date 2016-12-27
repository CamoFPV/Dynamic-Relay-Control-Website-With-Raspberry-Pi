import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.HIGH)
    return '<a href="./PHP/12on.php"><input type="button" class="MyButton" value="Relay 12"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay13.html', 'w')
print >> f, output
f.close()
