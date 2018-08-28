	
import serial   
import os, time
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

#use below line for pytho 
port.write('AT'+'\r\n')
rcv = port.read(10)
print (rcv)

#use below line for pytho3rcv = port.read(10)
port.write(('AT'+'\r\n').encode('utf-8'))
rcv = port.read(10)
print (rcv)
