import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def something_Changed(response):
    print(response.event_type)
    print(response.data)
    
cred = credentials.Certificate("C:/Users/imale/Documents/Schoolwork/Computer Science/CSTestProject-main/lc-cs-test-firebase-adminsdk-wis0e-d90fe5e569.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lc-cs-test-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference().child('temperature log')
my_ref = ref.listen(something_Changed)
