import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import random
import time


ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

cred = credentials.Certificate("C:/Users/imale/Documents/Schoolwork/Computer Science/CSTestProject-main/lc-cs-test-firebase-adminsdk-wis0e-d90fe5e569.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lc-cs-test-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference()
ref.update({'temperature_log':''})
ref = db.reference().child('temperature log')

source = input("Please input the source of our data")


while True:
    mb_temperature = str(ser.readline().decode('utf-8'))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    if mb_temperature.isdigit():
        ref.update({str(int(time.time())): {'Temperature':mb_temperature, 'Location': source}})
    
    else:
        print("Check data source.")
    time.sleep(5)


