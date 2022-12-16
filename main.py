from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

file_path = "static/img/example_colors/"
example_colors = [['1878A8.png', '181848.png'], ['186090.png', '604848.png'], ['607830.png', '781818.png'],
                  ['F06018.png', 'F09030.png'], ['FF9018.png', 'FFA830.png']]


@app.route("/")
def home():
    colors = example_colors
    return render_template('index.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
