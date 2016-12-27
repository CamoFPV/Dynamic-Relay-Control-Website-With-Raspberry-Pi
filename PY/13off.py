import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(19,GPIO.OUT)
    GPIO.output(19,GPIO.HIGH)
    return '<a href="./PHP/13on.php"><input type="button" class="MyButton" value="Relay 13"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay19.html', 'w')
print >> f, output
f.close()
