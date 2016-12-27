import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.LOW)
    return '<a href="./PHP/4off.php"><input type="button" class="MyButtonON" value="Relay 4"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay17.html', 'w')
print >> f, output
f.close()
