import serial

serialPort = serial.Serial("serial0", baudrate=9600, timeout=3.0)

while True:
	serialPort.write("say smth : ")
	rcv = port.read(10)
	serialPort.write("rnYou sent  : " + repr(rcv))
