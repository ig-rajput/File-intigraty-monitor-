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

def load_baseline(filename='baseline.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def monitor_changes(directory, baseline):
    print("🔍 Monitoring for changes...")
    current = generate_baseline(directory)

    for path, hash_value in current.items():
        if path not in baseline:
            print(f"[+] New file added: {path}")
        elif baseline[path] != hash_value:
            print(f"[!] File modified: {path}")

    for path in baseline:
        if path not in current:
            print(f"[-] File deleted: {path}")

directory = '/your/folder/path'  # change this to your folder path
loaded_baseline = load_baseline()
monitor_changes(directory, loaded_baseline)
