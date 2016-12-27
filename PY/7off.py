import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(10,GPIO.OUT)
    GPIO.output(10,GPIO.HIGH)
    return '<a href="./PHP/7on.php"><input type="button" class="MyButton" value="Relay 7"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay10.html', 'w')
print >> f, output
f.close()
