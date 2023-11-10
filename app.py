
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '헤이 헤이 모두들 모두들 모두들 안녕 안녕 내가 내가 내가 내가 누군지 아니 아니 아니 아니 아니'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)

    return result

