import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.HIGH)
    return '<a href="./PHP/5on.php"><input type="button" class="MyButton" value="Relay 5"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay27.html', 'w')
print >> f, output
f.close()
