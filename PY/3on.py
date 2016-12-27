import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    return '<a href="./PHP/3off.php"><input type="button" class="MyButtonON" value="Relay 3"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay4.html', 'w')
print >> f, output
f.close()
