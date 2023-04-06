from celery import Celery
import requests

BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'


app = Celery(__name__, broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task(name="fetch")
def fetch(URL):
    res = requests.get(URL)
    return res.json()['uuid']