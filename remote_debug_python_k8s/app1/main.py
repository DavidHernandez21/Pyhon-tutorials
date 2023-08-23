import os

import requests
from fastapi import FastAPI

app = FastAPI()

API = os.environ.get('API', '')


@app.get('/')
def sample_endpoint():
    r = requests.get(f'{API}/api/test')
    return {'data': r.json()}
