	
import serial
import RPi.GPIO as GPIO   
import os, time
 
GPIO.setmode(GPIO.BOARD)
# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

#use below line for python
port.write('AT'+'\r')
rcv = port.read(10)
print (port.read(10))

#use below line for pytho3rcv = port.read(10)
#port.write(('AT'+'\r\n').encode('utf-8'))
#rcv = port.read(10)
#print (rcv)

#turnon GPS module
port.write('AT+CGPSPWR=1')
rcv=port.read(10)
print (rcv)

port.write('AT=CGPSSTATUS?')
rcv=port.read(10)
print (rcv)
