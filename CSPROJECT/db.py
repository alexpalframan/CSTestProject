import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import random
import time
def doSomething(response):
    print(response.data)

cred = credentials.Certificate(r"C:\Users\18APalframan.ACC\Documents\CS_2024\CSPROJECT\lc-cs-test-firebase-adminsdk-wis0e-808f656c77.JSON")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://lc-cs-test-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference()
ref = db.reference().child('transistor')
ref.update({'transistor':''})
ref = db.reference().child('transistor')
ref.listen(doSomething)

while True:
    x = random.randint(0,10)
    ref.update({str(int(time.time())):{'x'}})
    time.sleep(5)


