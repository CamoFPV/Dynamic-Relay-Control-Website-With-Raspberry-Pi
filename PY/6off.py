import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(22,GPIO.HIGH)
    return '<a href="./PHP/6on.php"><input type="button" class="MyButton" value="Relay 6"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay22.html', 'w')
print >> f, output
f.close()
