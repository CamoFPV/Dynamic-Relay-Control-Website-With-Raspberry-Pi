#!/usr/bin/env python
# IMPORT NECESSARY LIBRARIES
import RPi.GPIO as GPIO
import time

# INITIALIZE THE GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

# TURN ON RELAY 1
GPIO.output(2,1)
GPIO.output(3,1)
GPIO.output(4,1)
GPIO.output(17,1)
GPIO.output(27,1)
GPIO.output(22,1)
GPIO.output(10,1)
GPIO.output(9,1)
GPIO.output(11,1)
GPIO.output(5,1)
GPIO.output(6,1)
GPIO.output(13,1)
GPIO.output(19,1)
GPIO.output(26,1)
GPIO.output(21,1)
GPIO.output(20,1)

# CLEAN UP GPIO
# GPIO.cleanup()

a = open('/var/www/html/DATA/Relay2.html', 'w')
print >> a, '<a href="./PHP/1off.php"><input type="button" class="MyButton" value="Relay 1"></a>'
a.close()

b = open('/var/www/html/DATA/Relay3.html', 'w')
print >> b, '<a href="./PHP/2off.php"><input type="button" class="MyButton" value="Relay 2"></a>'
b.close()

c = open('/var/www/html/DATA/Relay4.html', 'w')
print >> c, '<a href="./PHP/3off.php"><input type="button" class="MyButton" value="Relay 3"></a>'
c.close()

d = open('/var/www/html/DATA/Relay17.html', 'w')
print >> d, '<a href="./PHP/4off.php"><input type="button" class="MyButton" value="Relay 4"></a>'
d.close()

e = open('/var/www/html/DATA/Relay27.html', 'w')
print >> e, '<a href="./PHP/5off.php"><input type="button" class="MyButton" value="Relay 5"></a>'
e.close()

f = open('/var/www/html/DATA/Relay22.html', 'w')
print >> f, '<a href="./PHP/6off.php"><input type="button" class="MyButton" value="Relay 6"></a>'
f.close()

g = open('/var/www/html/DATA/Relay10.html', 'w')
print >> g, '<a href="./PHP/7off.php"><input type="button" class="MyButton" value="Relay 7"></a>'
g.close()

h = open('/var/www/html/DATA/Relay9.html', 'w')
print >> h, '<a href="./PHP/8off.php"><input type="button" class="MyButton" value="Relay 8"></a>'
h.close()

i = open('/var/www/html/DATA/Relay11.html', 'w')
print >> i, '<a href="./PHP/9off.php"><input type="button" class="MyButton" value="Relay 9"></a>'
i.close()

j = open('/var/www/html/DATA/Relay5.html', 'w')
print >> j, '<a href="./PHP/10off.php"><input type="button" class="MyButton" value="Relay 10"></a>'
j.close()

k = open('/var/www/html/DATA/Relay6.html', 'w')
print >> k, '<a href="./PHP/11off.php"><input type="button" class="MyButton" value="Relay 11"></a>'
k.close()

l = open('/var/www/html/DATA/Relay13.html', 'w')
print >> l, '<a href="./PHP/12off.php"><input type="button" class="MyButton" value="Relay 12"></a>'
l.close()

m = open('/var/www/html/DATA/Relay19.html', 'w')
print >> m, '<a href="./PHP/13off.php"><input type="button" class="MyButton" value="Relay 13"></a>'
m.close()

n = open('/var/www/html/DATA/Relay26.html', 'w')
print >> n, '<a href="./PHP/14off.php"><input type="button" class="MyButton" value="Relay 14"></a>'
n.close()

o = open('/var/www/html/DATA/Relay21.html', 'w')
print >> o, '<a href="./PHP/15off.php"><input type="button" class="MyButton" value="Relay 15"></a>'
o.close()

p = open('/var/www/html/DATA/Relay20.html', 'w')
print >> p, '<a href="./PHP/16off.php"><input type="button" class="MyButton" value="Relay 16"></a>'
p.close()
