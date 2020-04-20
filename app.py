from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'aaaaaa'


if __name__ == '__main__':
    app.run()
