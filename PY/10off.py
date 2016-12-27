import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(5,GPIO.OUT)
    GPIO.output(5,GPIO.HIGH)
    return '<a href="./PHP/10on.php"><input type="button" class="MyButton" style="margin-right: 10px" value="Relay 10"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay5.html', 'w')
print >> f, output
f.close()
