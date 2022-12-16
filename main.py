from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
