from app import app
from flask import render_template
#from processing import crl, img_click, ratio, script


@app.route("/", methods=["GET","POST"])
def index():    
<<<<<<< Updated upstream
    return render_template('index.html')
=======
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

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('result.html')

>>>>>>> Stashed changes
