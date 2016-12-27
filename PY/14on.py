import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.LOW)
    return '<a href="./PHP/14off.php"><input type="button" class="MyButtonON" value="Relay 14"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay26.html', 'w')
print >> f, output
f.close()
