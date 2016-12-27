import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(22,GPIO.LOW)
    return '<a href="./PHP/6off.php"><input type="button" class="MyButtonON" value="Relay 6"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay22.html', 'w')
print >> f, output
f.close()
