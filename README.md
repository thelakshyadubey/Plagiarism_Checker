# 🔍 Distributed Code Plagiarism Checker (Web App)

This project is a **distributed code plagiarism checker** built with Python, Flask, Google Drive API, and AST (Abstract Syntax Tree) comparison logic. It allows students to upload their `.py` files and checks for similarity with peer submissions stored on Google Drive.

> 💡 Originally developed for the **Distributed Computing Course** at NMIMS as a practical demonstration of file distribution, cloud sync, and plagiarism detection using compiler-level code comparison techniques.

---

## 📂 Project Structure

```bash
plag_checker_web/
├── app.py                 # Flask web app (main entry point)
├── drive_utils.py         # Handles Google Drive authentication and syncing
├── ast_compare.py         # Compares files using AST-based similarity
├── templates/
│   ├── upload.html        # File upload UI
│   └── results.html       # Plagiarism result UI
├── static/
│   └── styles/
│       └── styles.css     # Custom CSS styling
├── .gitignore             # Ensures sensitive files are not pushed
├── README.md              # Project documentation
🚀 Features
📤 Upload Python file from web UI

☁️ Sync peer files from Google Drive

🧠 Detect plagiarism using AST-based logic (structure-aware)

✅ Report similarity % with visual results (red = plagiarized, green = safe)

🎨 Responsive frontend with drag & drop support

🔐 Token and credentials securely excluded

📌 Technologies Used
Flask (Python Web Framework)

Google Drive API (google-api-python-client, oauth2client)

AST Module (ast + difflib) for code comparison

HTML + CSS (Drag & drop upload interface)

Jinja2 (Flask templating)

Git for version control

VS Code + GitHub for collaboration

🛠️ How It Works
User uploads a .py file from the frontend.

Flask handles the request and:

Saves the file locally

Uploads it to Google Drive

Syncs peer files from a shared Google Drive folder

Each file is parsed into an Abstract Syntax Tree using ast module

Structural similarity is calculated between each peer file and the uploaded one

Similarity scores are shown on the results page

🧠 AST-Based Comparison Logic
We use Python's built-in ast module to parse code into its syntax tree, ignoring variable names, formatting, and comments.

This gives structure-aware comparison rather than raw text matching

Uses difflib.SequenceMatcher on ast.dump() representations

python
Copy
Edit
tree1 = ast.parse(code1)
tree2 = ast.parse(code2)
similarity = difflib.SequenceMatcher(None, ast.dump(tree1), ast.dump(tree2)).ratio()
🔒 Sensitive File Handling (.gitignore)
To prevent leakage of credentials or tokens, the following files are ignored from version control:

bash
Copy
Edit
# .gitignore
token.pickle
credentials.json
__pycache__/
*.pyc
.env
.vscode/
✅ Setup Instructions (Local)
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/plagiarism-checker-web.git
cd plagiarism-checker-web
2. Create & Activate a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt isn't created, you can install manually:

bash
Copy
Edit
pip install flask google-api-python-client oauth2client
4. Add Your Google Drive Credentials
Place your credentials.json and token.pickle in the project root.

These files are required to sync with Google Drive.

Do not upload them to GitHub.

5. Run the Web App
bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

🌐 Deploying the App
To deploy on platforms like Render, Replit, or Railway:

Upload your source code (excluding sensitive files)

Use environment variables or secret file uploads for credentials

Set the start command to python app.py

📸 Screenshots
![image](https://github.com/user-attachments/assets/c651b23f-fa4a-4416-8f1d-033899b29bdc)
![image](https://github.com/user-attachments/assets/3463be02-64fb-495c-931e-9d6685831352)
![image](https://github.com/user-attachments/assets/363d4dff-264e-42c0-9123-e7ccea796ce6)

Results Page

🧾 License
This project is developed as part of academic coursework at NMIMS and is open-source for learning and educational purposes.

🙋‍♂️ Author
Lakshya Dubey
B.Tech Computer Engineering
Email: lakshya.dubey@example.com

