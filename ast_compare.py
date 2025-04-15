# # ast_compare.py

# import ast
# import os
# import difflib

# def read_file(path):
#     with open(path, 'r', encoding='utf-8') as file:
#         return file.read()

# def get_ast_structure(code):
#     try:
#         tree = ast.parse(code)
#         return ast.dump(tree)
#     except SyntaxError as e:
#         print(f"Syntax error in file: {e}")
#         return ""

# def compare_ast(file1_path, file2_path):
#     code1 = read_file(file1_path)
#     code2 = read_file(file2_path)

#     ast1 = get_ast_structure(code1)
#     ast2 = get_ast_structure(code2)

#     similarity = difflib.SequenceMatcher(None, ast1, ast2).ratio()
#     return round(similarity * 100, 2)  # Percentage

# def run_comparisons(my_file_path, download_folder='downloads/'):
#     results = []
#     for filename in os.listdir(download_folder):
#         if filename.endswith(".py") and filename != os.path.basename(my_file_path):
#             compare_path = os.path.join(download_folder, filename)
#             score = compare_ast(my_file_path, compare_path)
#             results.append({
#                 "compared_with": filename,
#                 "similarity_score": f"{score}%"
#             })

#     return results




# 🔹 ast_compare/compare.py

import os
from ast import parse, walk
from difflib import SequenceMatcher

def read_code(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def compute_similarity(code1, code2):
    return round(SequenceMatcher(None, code1, code2).ratio() * 100, 2)

def compare_with_all_peers(filename):
    upload_path = os.path.join('uploads', filename)
    peer_folder = 'downloads'
    results = []

    try:
        my_code = read_code(upload_path)
    except Exception as e:
        return [f"❌ Failed to read uploaded file: {e}"]

    for peer_file in os.listdir(peer_folder):
        peer_path = os.path.join(peer_folder, peer_file)
        if peer_file == filename or not peer_file.endswith('.py'):
            continue
        try:
            peer_code = read_code(peer_path)
            similarity = compute_similarity(my_code, peer_code)
            results.append(f"{peer_file} → {similarity}% similar")
        except Exception as e:
            results.append(f"{peer_file} → ❌ Error reading/comparing: {e}")

    return results
