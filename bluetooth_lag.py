import bluetooth
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

M11=7
M12=8
M21=9
M22=10

def F():                   """Rotates both the DC motors attached to a motor controller with their
                             maximum  speed  for 5 seconds"""
    
    GPIO.output(M11,GPIO.HIGH)
    GPIO.output(M21,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(M11,GPIO.LOW)
    GPIO.output(M21,GPIO.LOW)

def S():                         """  Rotates both the DC motors attached to a motor controller with 50% of their
                                      maximum  speed  """
    
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    GPIO.output(M11,GPIO.HIGH)
    GPIO.output(M21,GPIO.HIGH)
    time.sleep(5)

def T():                       """ Stops the motors that run with S() and then rotates then rotates thwm wth their maximum speed"""
    GPIO.output(M11,GPIO.LOW)
    GPIO.output(M21,GPIO.LOW)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    GPIO.output(M11,GPIO.HIGH)
    GPIO.output(M21,GPIO.HIGH)
    time.sleep(5)

def L():                       """ Stops the motors : Using here to stop motors that were running After execution of T() """
    GPIO.output(M11,GPIO.LOW)
    GPIO.output(M21,GPIO.LOW)
    GPIO.cleanup()


GPIO.setup(M11,GPIO.OUT)
GPIO.setup(M12,GPIO.OUT)
GPIO.setup(M21,GPIO.OUT)
GPIO.setup(M22,GPIO.OUT)
pwm1=GPIO.PWM(7,100)
#pwm1.start(100)
pwm2=GPIO.PWM(9,100)
#pwm2.start(100)
GPIO.output(M11,GPIO.LOW)
GPIO.output(M12,GPIO.LOW)
GPIO.output(M21,GPIO.LOW)
GPIO.output(M22,GPIO.LOW)

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port=1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address=server_socket.accept()
print("Accepted connection from" + str(address))

while 1:
      data=client_socket.recv(1024)
      print("received [%s]" % data)

      if (data == b'F'):
        F()

      elif(data == b'S'):
        S()

      elif(data == b'T'):
        T()

      elif(data == b'L'):
        L()
        break

client_socket.close()
server_socket.close()
