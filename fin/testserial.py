import serial
ser = serial.Serial('/dev/ttyAMA0')
print(ser.name)
