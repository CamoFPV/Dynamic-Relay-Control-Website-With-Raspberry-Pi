import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)
    return '<a href="./PHP/16off.php"><input type="button" class="MyButtonON" value="Relay 16"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay20.html', 'w')
print >> f, output
f.close()
