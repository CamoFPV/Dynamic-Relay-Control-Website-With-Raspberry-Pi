import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(5,GPIO.OUT)
    GPIO.output(5,GPIO.LOW)
    return '<a href="./PHP/10off.php"><input type="button" class="MyButtonON" style="margin-right: 10px" value="Relay 10"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay5.html', 'w')
print >> f, output
f.close()
