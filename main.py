# 🔹 main.py

from drive_utils import upload_file, download_peer_files
from ast_compare import run_comparisons
import os
import json

# Set your file name
my_file = 'lakshya.py'

# Ensure required folders exist
os.makedirs('uploads', exist_ok=True)
os.makedirs('downloads', exist_ok=True)
os.makedirs('results', exist_ok=True)

# Step 1: Upload your file to Google Drive
upload_file(my_file)

# Step 2: Download all peer files (excluding your own) from Drive
download_peer_files(exclude_filename=my_file)

# Step 3: Run AST-based comparison
results = run_comparisons(os.path.join('uploads', my_file))

# Step 4: Print and save results
print("\n📊 Plagiarism Check Results:")
for r in results:
    print(f"Compared with: {r['compared_with']} → Similarity: {r['similarity_score']}")

with open(f'results/{my_file}_results.json', 'w') as f:
    json.dump(results, f, indent=4)
