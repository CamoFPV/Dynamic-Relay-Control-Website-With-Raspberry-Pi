import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(6,GPIO.OUT)
    GPIO.output(6,GPIO.HIGH)
    return '<a href="./PHP/11on.php"><input type="button" class="MyButton" value="Relay 11"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay6.html', 'w')
print >> f, output
f.close()
