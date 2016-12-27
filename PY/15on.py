import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
    return '<a href="./PHP/15off.php"><input type="button" class="MyButtonON" value="Relay 15"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay21.html', 'w')
print >> f, output
f.close()
