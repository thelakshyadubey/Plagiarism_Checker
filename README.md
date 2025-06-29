# Distributed Code Plagiarism Checker

This project is a distributed code plagiarism detection system implemented as a Flask web application. It allows users to upload Python files, which are then compared against peer submissions stored in a shared Google Drive folder using abstract syntax tree (AST)-based comparison.

---

## Key Features

* Web-based file upload interface (drag and drop supported)
* Google Drive synchronization for peer file access
* AST-based structural comparison to identify code similarity
* Clear, percentage-based plagiarism report
* Frontend designed using HTML, CSS, and Jinja2 templating
* Modular architecture for easy maintenance and enhancement

---

## Directory Structure

```
plag_checker_web/
├── app.py                 # Flask application (main entry point)
├── drive_utils.py         # Google Drive authentication and sync logic
├── ast_compare.py         # AST-based code comparison logic
├── templates/
│   ├── upload.html        # File upload user interface
│   └── results.html       # Plagiarism results display
├── static/
│   └── styles/
│       └── styles.css     # Custom frontend styling
├── uploads/               # Temporary folder for uploaded files
├── downloads/             # Folder for downloaded peer files
├── credentials.json       # Google OAuth2 credentials (not version controlled)
├── token.pickle           # Saved user authentication token (not version controlled)
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
```

---

## How It Works

1. The user uploads a `.py` file using the web interface.
2. The file is stored locally in the `uploads/` directory.
3. The application uploads the file to a shared Google Drive folder.
4. All peer `.py` files from the same folder are downloaded to `downloads/`.
5. Each peer file is compared to the uploaded file using AST-based structural comparison.
6. The similarity scores are displayed in a report format on the web interface.

---

## AST-Based Comparison Overview

The comparison uses Python’s built-in `ast` module to parse and compare the syntax trees of each program. This method focuses on code structure rather than formatting, comments, or variable names, enabling more accurate detection of logical similarity.

```python
import ast
import difflib

tree1 = ast.parse(code1)
tree2 = ast.parse(code2)
similarity = difflib.SequenceMatcher(None, ast.dump(tree1), ast.dump(tree2)).ratio()
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/thelakshyadubey/Plagiarism_Checker.git
cd Plagiarism_Checker
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Python Dependencies

Install all required packages using the `requirements.txt` file:

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

If any issues arise during installation (especially with NumPy), make sure your pip and build tools are up to date.

---

### 4. Configure Google Drive API

1. Create OAuth credentials via [Google Cloud Console](https://console.cloud.google.com/).
2. Download the `credentials.json` file and place it in the root of the project.
3. When prompted on first run, sign in with your Google account. A `token.pickle` file will be generated to store your session.
4. These files must **not be shared or committed to version control**.

---

### 5. Run the Application

Start the Flask development server:

```bash
python app.py
```

Then open your browser and navigate to:

```
http://localhost:6000
```

You can now upload `.py` files and view similarity results.

---

## Deployment

To deploy this application on platforms such as Render, Railway, or Replit:

* Ensure `credentials.json` and `token.pickle` are securely stored using the platform’s secret management tools.
* Set the startup command as:

```bash
python app.py
```

* Ensure appropriate environment variables or file mounts are configured for Google Drive authentication.

---

## Example Output

The plagiarism result is displayed as a list of peer files along with their corresponding similarity scores. Example:

```
friend1.py → 42.17% similar
friend2.py → 100.00% similar
```

---

## Security and Version Control

The following files and folders should be excluded from your Git repository:

```
# .gitignore
token.pickle
credentials.json
__pycache__/
*.pyc
.env
.vscode/
```

---

## Author
Lakshya Dubey

---

## Preview
![image](https://github.com/user-attachments/assets/180d5f46-2fcb-4aca-a307-c1e1baf82efd)
![image](https://github.com/user-attachments/assets/a865fd49-0d5c-4e2e-8142-7e60ddc5b0a4)
![image](https://github.com/user-attachments/assets/c18218aa-ebbc-4fd0-b051-37f628b0e364)
![image](https://github.com/user-attachments/assets/8c906d94-d587-4fdd-af2e-b7810fc95277)
