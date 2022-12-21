from flask import Flask, render_template, flash, redirect, request
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename
from check_colors import check_colors
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
EXAMPLE_IMG = 'static/img/steve-johnson-placeholder.jpg'

app = Flask(__name__)
bootstrap = Bootstrap5()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

example_colors = [['#1878A8', '#181848'], ['#186090', '#604848'], ['#607830', '#781818'],
                  ['#F06018', '#F09030'], ['#FF9018', '#FFA830']]


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
            filepath = os.path.join(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file = f'{filepath}/{filename}'
            return render_template('index.html', colors=check_colors(file), img=file)
    return render_template('index.html', colors=example_colors, img=EXAMPLE_IMG)


if __name__ == '__main__':
    app.run(debug=True)
