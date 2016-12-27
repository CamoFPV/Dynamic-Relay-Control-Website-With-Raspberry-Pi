import RPi.GPIO as GPIO

def lights_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(6,GPIO.OUT)
    GPIO.output(6,GPIO.LOW)
    return '<a href="./PHP/11off.php"><input type="button" class="MyButtonON" value="Relay 11"></a>'

output = lights_off()
f = open('/var/www/html/DATA/Relay6.html', 'w')
print >> f, output
f.close()
