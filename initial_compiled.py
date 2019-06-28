import bluetooth
import sys
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Phase=0
Front_left=7
Front_right=11
Back_left=9
Back_right=13
Front_left_other=8
Front_right_other=12
Back_left_other=10
Back_right_other=14
m11=17
m12=23
m21=24
m22=25

def left_side_forward():
    print ("FORWARD LEFT")
    p.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 90):
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        pwm1.ChangeDutyCycle(70)
        pwm2.ChangeDutyCycle(70)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)

    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        pwm1.ChangeDutyCycle(70)
        pwm2.ChangeDutyCycle(70)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)

    Phase=90

def right_side_forward():
    print ("FORWARD RIGHT")
    p.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 90):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       pwm3.ChangeDutyCycle(70)
       pwm4.ChangeDutyCycle(70)
       GPIO.output(Front_left,GPIO.HIGH)
       GPIO.output(Front_right,GPIO.HIGH)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)
   
    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        pwm3.ChangeDutyCycle(70)
        pwm4.ChangeDutyCycle(70)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)

    Phase=90

def forward():
    print ("FORWARD")
    p.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(3.1)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 90):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       GPIO.output(Front_left,GPIO.HIGH)
       GPIO.output(Front_right,GPIO.HIGH)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)
    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.ouput(Back_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)

    Phase=90

def left_side_reverse():
    print ("BACKWARD LEFT")
    p.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 90):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       pwm1.ChangeDutyCycle(70)
       pwm2.ChangeDutyCycle(70)
       GPIO.output(Front_left,GPIO.HIGH)
       GPIO.output(Front_right,GPIO.HIGH)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)

    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        pwm1.ChangeDutyCycle(70)
        pwm2.ChangeDutyCycle(70)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        GPIO.ouput(Back_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)

    Phase=90

def right_side_reverse():
    print ("BACKWARD RIGHT")
    p.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 90):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       pwm3.ChangeDutyCycle(70)
       pwm4.ChangeDutyCycle(70)
       GPIO.output(Front_left,GPIO.HIGH)
       GPIO.output(Front_right,GPIO.HIGH)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)

    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        pwm3.ChangeDutyCycle(70)
        pwm4.ChangeDutyCycle(70)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)

    Phase=90

def reverse():
    print ("BACKWARD")
    p.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(9.5)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 90):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)   
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       GPIO.output(Front_left,GPIO.HIGH)
       GPIO.output(Front_right,GPIO.HIGH)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)

    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.output(Back_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)

    Phase=90

def up():
    print ("UP")
    p.ChangeDutyCycle(11)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(11)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(11)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(11)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 0):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       GPIO.output(Front_left,GPIO.HIGH)
       GPIO.output(Front_right,GPIO.HIGH)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)

    elif (Phase == 180):
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)
        time.sleep(0.00343)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)

    else:
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)
        time.sleep(0.00172)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)

    Phase=0

def glide():
    print ("GLIDE")
    p.ChangeDutyCycle(11)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(11)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(11)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(11)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 0):
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)

    elif (Phase == 180):
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)
        time.sleep(0.00343)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)

    else:
       GPIO.output(Front_left,GPIO.LOW)
       GPIO.output(Front_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)
       GPIO.output(Back_left,GPIO.HIGH)
       GPIO.output(Back_right,GPIO.HIGH)
       time.sleep(0.00172)
       GPIO.output(Back_left,GPIO.LOW)
       GPIO.output(Back_right,GPIO.LOW)

    Phase=0

def hover():
    print ("HOVER")
    p.ChangeDutyCycle(11)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(11)
    time.sleep(0.5)
    q.ChangeDutyCycle(0)
    r.ChangeDutyCycle(11)
    time.sleep(0.5)
    r.ChangeDutyCycle(0)
    s.ChangeDutyCycle(11)
    time.sleep(0.5)
    s.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    time.sleep(0.5)
    global Phase

    if (Phase == 0):
      GPIO.output(Front_left,GPIO.LOW)
      GPIO.output(Front_right,GPIO.LOW)
      GPIO.output(Back_left,GPIO.LOW)
      GPIO.output(Back_right,GPIO.LOW)
      GPIO.output(Front_left,GPIO.HIGH)
      GPIO.output(Front_right,GPIO.HIGH)
      time.sleep(0.00343)
      GPIO.output(Back_left,GPIO.HIGH)
      GPIO.output(Back_right,GPIO.HIGH)

    elif (Phase == 180):
        GPIO.output(Front_left,GPIO.LOW)
        GPIO.output(Front_right,GPIO.LOW)
        GPIO.output(Back_left,GPIO.LOW)
        GPIO.output(Back_right,GPIO.LOW)
        GPIO.output(Front_left,GPIO.HIGH)
        GPIO.output(Front_right,GPIO.HIGH)
        GPIO.output(Back_left,GPIO.HIGH)
        GPIO.output(Back_right,GPIO.HIGH)

    else:
      GPIO.output(Front_left,GPIO.LOW)
      GPIO.output(Front_right,GPIO.LOW)
      GPIO.output(Back_left,GPIO.LOW)
      GPIO.output(Back_right,GPIO.LOW)
      GPIO.output(Front_left,GPIO.HIGH)
      GPIO.output(Front_right,GPIO.HIGH)
      time.sleep(0.00172)
      GPIO.output(Back_left,GPIO.HIGH)
      GPIO.output(Back_right,GPIO.HIGH)

    Phase=180

def stop():
    print ("STOP")
    GPIO.output(Front_left,GPIO.LOW)
    GPIO.output(Front_right,GPIO.LOW)
    GPIO.output(Back_left,GPIO.LOW)
    GPIO.output(Back_right,GPIO.LOW)
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    GPIO.cleanup()

GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.setup(Front_right, GPIO.OUT)
GPIO.setup(Front_left, GPIO.OUT)
GPIO.setup(Back_right, GPIO.OUT)
GPIO.setup(Back_left, GPIO.OUT)
GPIO.setup(Front_right_other, GPIO.OUT)
GPIO.setup(Front_left_other, GPIO.OUT)
GPIO.setup(Back_right_other, GPIO.OUT)
GPIO.setup(Back_left_other, GPIO.OUT)
pwm1=GPIO.PWM(7,100)
pwm2=GPIO.PWM(9,100)
pwm3=GPIO.PWM(11,100)
pwm4=GPIO.PWM(13,100)
GPIO.output(Front_right, GPIO.LOW)
GPIO.output(Front_left, GPIO.LOW)
GPIO.output(Back_right, GPIO.LOW)
GPIO.output(Back_left, GPIO.LOW)
GPIO.output(Front_right_other, GPIO.LOW)
GPIO.output(Front_left_other, GPIO.LOW)
GPIO.output(Back_right_other, GPIO.LOW)
GPIO.output(Back_left_other, GPIO.LOW)
p = GPIO.PWM(m11,50)
q = GPIO.PWM(m12,50)
r = GPIO.PWM(m21,50)
s = GPIO.PWM(m22,50)
p.start(2.5)
p.ChangeDutyCycle(0)
q.start(2.5)
q.ChangeDutyCycle(0)
r.start(2.5)
r.ChangeDutyCycle(0)
s.start(2.5)
s.ChangeDutyCycle(0)

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port=1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address=server_socket.accept()
print ("Accepted Connection from" + str(address))

while 1:

      data=client_server.recv(1024)

      print("received [%s]" % data)

      if(data == b'F'):
        forward()

      elif(data == b'B'):
        reverse()

      elif(data == b'U'):
        up()

      elif(data == b'G'):
        glide()

      elif(data == b'H'):
        hover()

      elif(data == b'P'):
        right_side_forward()

      elif(data == b'Q'):
        left_side_forward()

      elif(data == b'M'):
        right_side_reverse()

      elif(data == b'Z'):
        left_side_reverse()

      elif(data == b'S'):
        stop()
        break

client_socket.close()
server_socket.close()
