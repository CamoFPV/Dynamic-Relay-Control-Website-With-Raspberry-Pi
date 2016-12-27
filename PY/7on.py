import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(10,GPIO.OUT)
    GPIO.output(10,GPIO.LOW)
    return '<a href="./PHP/7off.php"><input type="button" class="MyButtonON" value="Relay 7"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay10.html', 'w')
print >> f, output
f.close()
