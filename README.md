# PDFProtector-Application
A simple Flask web application that allows you to upload a PDF and download a password-protected version of it.  Built using Flask and PyPDF2.

## ✨ Features
- Upload any valid PDF file through a web browser.
- Set a **custom password** to protect the PDF.
- Instantly **download the encrypted PDF**.

---

## 🗂 Project Structure
pdf-protector/
├─ app.py # Flask application
├─ templates/
│ └─ index.html # Web form for uploading and password entry
├─ uploads/ # Temporary storage for uploaded PDFs
├─ protected/ # Password-protected PDFs are saved here
└─ README.md # Project documentation

yaml
Copy code

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/yourusername/pdf-protector.git
cd pdf-protector

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies

pip install flask PyPDF2
▶️ Usage
Start the Flask Server:
python app.py
By default the app runs at:
http://127.0.0.1:5000/

Steps:
Open the URL in your browser.
Upload a PDF file.
Enter the password you want to set.
Click Protect PDF to download the password-protected version.

⚙️ Configuration
Uploads folder: uploads/
Protected PDFs folder: protected/
You can change these folders in app.py:

UPLOAD_FOLDER = 'uploads'
PROTECTED_FOLDER = 'protected'
Modules / Libraries Used
Module	Type	Purpose
Flask	Third-party	Web framework to create the web server and handle requests.
PyPDF2	Third-party	Reads and writes PDFs, and applies password encryption.
werkzeug.utils.secure_filename	Built into Flask	Safely stores uploaded files with a secure name.
os	Built-in	Handles file paths and creates upload folders
