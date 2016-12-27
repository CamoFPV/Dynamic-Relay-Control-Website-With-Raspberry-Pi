import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.LOW)
    return '<a href="./PHP/5off.php"><input type="button" class="MyButtonON" value="Relay 5"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay27.html', 'w')
print >> f, output
f.close()
