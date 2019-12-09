import time
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://ku-oss-team-merge.firebaseio.com/'}
                              )


def post(_type, value):
    ref = db.reference('sensor/' + _type)
    data = {'value': value, 'timestamp': int(time.time())}
    ref.update(data)


def get(_type):
    ref = db.reference('sensor/' + _type)
    return ref
