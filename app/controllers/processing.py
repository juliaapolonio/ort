ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}


# Function to see if file format is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

