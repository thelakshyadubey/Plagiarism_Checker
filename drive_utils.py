# 🔹 drive_sync.py

import os
import mimetypes
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import io

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'
FOLDER_NAME = 'DistributedPlagiarismChecker'
SCOPES = ['https://www.googleapis.com/auth/drive']

# 1. Authenticate and connect to Google Drive
def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

# 2. Create or fetch the shared folder
def get_or_create_project_folder(service, folder_name=FOLDER_NAME):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed = false"
    results = service.files().list(q=query, fields="files(id)").execute()
    folders = results.get('files', [])

    if folders:
        return folders[0]['id']
    
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(body=file_metadata, fields='id').execute()
    print(f"📁 Created Drive folder '{folder_name}' (ID: {folder['id']})")
    return folder['id']

# 3. Upload file into that folder
def upload_file(filename):
    service = authenticate()
    folder_id = get_or_create_project_folder(service)

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    mimetype = mimetypes.guess_type(filepath)[0]

    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }
    media = MediaFileUpload(filepath, mimetype=mimetype)

    uploaded = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"✅ Uploaded {filename} to folder (ID: {uploaded.get('id')})")

# 4. Download all peer files (except yours) from the folder
def download_peer_files(exclude_filename):
    service = authenticate()
    folder_id = get_or_create_project_folder(service)

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    query = f"'{folder_id}' in parents and mimeType='text/x-python' and trashed = false"
    results = service.files().list(q=query, pageSize=100, fields="files(id, name)").execute()
    items = results.get('files', [])

    print("📥 Syncing peer files from Google Drive:")
    for item in items:
        filename = item['name']
        if filename == exclude_filename:
            continue  # Skip your own file

        request = service.files().get_media(fileId=item['id'])
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        # Always re-download (fresh copy)
        with open(filepath, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()

        print(f"⬇️ Downloaded {filename}")
