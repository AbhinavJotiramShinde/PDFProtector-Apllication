from flask import Flask, render_template, request, send_from_directory, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import PyPDF2

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # needed for flash messages

UPLOAD_FOLDER = 'uploads'
PROTECTED_FOLDER = 'protected'
ALLOWED_EXTENSIONS = {'pdf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROTECTED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROTECTED_FOLDER'] = PROTECTED_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_password_protected_pdf(input_pdf, output_pdf, password):
    """Encrypt a PDF with the given password."""
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)
        with open(output_pdf, 'wb') as out_file:
            writer.write(out_file)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['pdf_file']
        password = request.form.get('password')

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if not password:
            flash('Password is required')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            protected_filename = f"protected_{filename}"
            output_path = os.path.join(app.config['PROTECTED_FOLDER'], protected_filename)

            try:
                create_password_protected_pdf(input_path, output_path, password)
            except Exception as e:
                flash(f'Error: {e}')
                return redirect(request.url)

            return redirect(url_for('download_file', filename=protected_filename))
        else:
            flash('Invalid file type. Only PDF allowed.')
            return redirect(request.url)
    return render_template('index.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROTECTED_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
