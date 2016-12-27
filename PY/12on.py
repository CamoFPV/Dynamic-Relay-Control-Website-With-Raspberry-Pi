import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.LOW)
    return '<a href="./PHP/12off.php"><input type="button" class="MyButtonON" value="Relay 12"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay13.html', 'w')
print >> f, output
f.close()
