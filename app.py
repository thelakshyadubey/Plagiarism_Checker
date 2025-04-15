from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import drive_utils
from ast_compare import compare_with_all_peers  # Assuming your core compare logic is modularized
from ast_compare import compare_with_all_peers


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("🔁 Route hit!")  # Add this line for debug

    if request.method == 'POST':
        if 'codefile' not in request.files:
            return "No file part"
        file = request.files['codefile']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Sync to Google Drive
            drive_utils.upload_file(filename)
            drive_utils.download_peer_files(filename)

            # Run plagiarism check
            results = compare_with_all_peers(filename)  # Should return list of matches/similarity

            return render_template('results.html', filename=filename, results=results)

    return render_template('upload.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=6000)
