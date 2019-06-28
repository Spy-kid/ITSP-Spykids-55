import bluetooth
#import sys
import time
import RPi.GPIO as GPIO

def zero():
    print("zero")
    p.ChangeDutyCycle(9.4)    #9.4 for 60 degrees rotation
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

def full():
    print("full")
    p.ChangeDutyCycle(11)    #11 for 180 degrees rotation
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

def thirty():
    print("thirty")
    p.ChangeDutyCycle(3.1)  #3.1 for 30 degrees rotation
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

pwmpin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmpin, GPIO.OUT)
p = GPIO.PWM(pwmpin ,50)
p.start(2.5)
p.ChangeDutyCycle(0)

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=1

server_socket.bind(("",port))

server_socket.listen(1)


client_socket,address=server_socket.accept()

print("Accepted Connection from " + str(address))

while 1:

      data=client_socket.recv(1024)

      print("received [%s]" % data)

      if(data == b'Z'):
        zero()

      elif(data == b'F'):
        full()

      elif(data == b'T'):
        thirty()

      elif(data == b'S'):
        break

p.stop()
GPIO.cleanup()
client_socket.close()
server_socket.close()
