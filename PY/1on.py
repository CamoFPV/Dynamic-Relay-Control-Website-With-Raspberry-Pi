import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2,GPIO.OUT)
    GPIO.output(2,GPIO.LOW)
    return '<a href="./PHP/1off.php"><input type="button" class="MyButtonON" value="Relay 1"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay2.html', 'w')
print >> f, output
f.close()
