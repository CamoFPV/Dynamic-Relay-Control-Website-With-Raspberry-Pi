import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.LOW)
    return '<a href="./PHP/9off.php"><input type="button" class="MyButtonON" style="margin-right: 10px" value="Relay 9"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay11.html', 'w')
print >> f, output
f.close()
