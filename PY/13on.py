import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(19,GPIO.OUT)
    GPIO.output(19,GPIO.LOW)
    return '<a href="./PHP/13off.php"><input type="button" class="MyButtonON" value="Relay 13"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay19.html', 'w')
print >> f, output
f.close()
