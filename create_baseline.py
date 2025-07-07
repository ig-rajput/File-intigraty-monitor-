import os
import hashlib
import json

def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def generate_baseline(directory):
    baseline = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                baseline[filepath] = hash_file(filepath)
            except Exception as e:
                print(f"Failed to hash {filepath}: {e}")
    return baseline

def save_baseline(baseline, filename='baseline.json'):
    with open(filename, 'w') as f:
        json.dump(baseline, f, indent=4)

directory = '/your/folder/path'  # change this to your folder path
baseline_data = generate_baseline(directory)
save_baseline(baseline_data)
print("✅ Baseline saved.")
