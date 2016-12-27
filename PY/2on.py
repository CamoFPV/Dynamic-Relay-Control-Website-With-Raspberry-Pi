import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(3,GPIO.OUT)
    GPIO.output(3,GPIO.LOW)
    return '<a href="./PHP/2off.php"><input type="button" class="MyButtonON" value="Relay 2"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay3.html', 'w')
print >> f, output
f.close()
