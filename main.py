from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
bootstrap = Bootstrap5()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

example_colors = [['1878A8.png', '181848.png'], ['186090.png', '604848.png'], ['607830.png', '781818.png'],
                  ['F06018.png', 'F09030.png'], ['FF9018.png', 'FFA830.png']]


# check the file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part!')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file!')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html', colors=example_colors)


if __name__ == '__main__':
    app.run(debug=True)
