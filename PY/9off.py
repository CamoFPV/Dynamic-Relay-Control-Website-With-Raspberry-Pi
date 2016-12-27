import RPi.GPIO as GPIO

def lights_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.HIGH)
    return '<a href="./PHP/9on.php"><input type="button" class="MyButton" style="margin-right: 10px" value="Relay 9"></a>'

output = lights_on()
f = open('/var/www/html/DATA/Relay11.html', 'w')
print >> f, output
f.close()
