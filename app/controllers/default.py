from app import app
from flask import render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app.controllers.processing import allowed_file, img_click
#from processing import crl, img_click, ratio, script


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            up=file.save(os.path.join(app.config['UPLOAD_FOLDER'], "output.png"))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('index.html')

@app.route('/uploads/<filename>', methods=["GET","POST"])
def uploaded_file(filename):

    if request.method == 'POST':
        x = request.form['x1']
        y = request.form['y1']
        x2 = request.form['x2']
        y2 = request.form['y2']
        return redirect(url_for('process', x=x, y=y, x2=x2, y2=y2))

    return render_template('result.html')

@app.route('/process/<x>:<y>:<x2>:<y2>', methods=["GET"])
def process(x, y, x2, y2):
    d = img_click("app/static/data/output.png",x,y,x2,y2)
    return render_template('process.html', x=x, y=y, x2=x2, y2=y2, d=d)

@app.route('/stl/', methods=["POST"])
def stl():
    return '''<button onclick="">Gerar G-CODE</button>'''
