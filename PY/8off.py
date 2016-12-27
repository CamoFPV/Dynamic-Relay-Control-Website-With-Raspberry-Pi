import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(9,GPIO.OUT)
    GPIO.output(9,GPIO.HIGH)
    return '<a href="./PHP/8on.php"><input type="button" class="MyButton" value="Relay 8"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay9.html', 'w')
print >> f, output
f.close()
