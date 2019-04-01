from flask import Flask, render_template

app = Flask(__name__)

import os

@app.route('/')
def main() -> 'html':
    return render_template('main.html', the_title='메인화면')


if __name__ == '__main__':

    # app.run(debug=True)

    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=80, debug=True)
