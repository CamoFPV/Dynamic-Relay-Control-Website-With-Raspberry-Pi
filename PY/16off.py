import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.HIGH)
    return '<a href="./PHP/16on.php"><input type="button" class="MyButton" value="Relay 16"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay20.html', 'w')
print >> f, output
f.close()
