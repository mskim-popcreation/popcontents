from flask import Flask

app = Flask(__name__)

import os

@app.route('/')
def hello_world():
    return 'Helloasdfasdf Woradfld!'


if __name__ == '__main__':

    # app.run(debug=True)

    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=80, debug=True)
