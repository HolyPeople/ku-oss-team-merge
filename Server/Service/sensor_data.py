import time
from firebase_admin import credentials, db
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)


def update(_type, value):
    ref = db.reference('sensor/' + _type)
    data = {'value': value, 'timestamp': int(time.time())}
    ref.update(data)
