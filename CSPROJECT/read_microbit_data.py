import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

while True:
    mb_temperature = str(ser.readline().decode('utf-8'))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    print(mb_temperature)
    if mb_temperature.isdigit():
        print("Write to FB")
    else:
        print("Check data source.")