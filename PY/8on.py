import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(9,GPIO.OUT)
    GPIO.output(9,GPIO.LOW)
    return '<a href="./PHP/8off.php"><input type="button" class="MyButtonON" value="Relay 8"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay9.html', 'w')
print >> f, output
f.close()
