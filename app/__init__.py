from flask import Flask


app = Flask(__name__)
UPLOAD_FOLDER = 'app/static/data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 's3cr3t'
app.config["DEBUG"] = True


from app.controllers import default, processing

