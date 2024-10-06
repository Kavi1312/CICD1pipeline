import requests
import os

# Set your repository details
GITHUB_API_URL = "https://api.github.com/repos/yourusername/html-cicd-demo/commits"
LOCAL_HASH_FILE = "/tmp/last_commit_hash.txt"

def get_latest_commit():
    response = requests.get(GITHUB_API_URL)
    if response.status_code == 200:
        latest_commit = response.json()[0]['sha']
        return latest_commit
    return None

def save_latest_commit(commit_hash):
    with open(LOCAL_HASH_FILE, 'w') as f:
        f.write(commit_hash)

def read_last_commit():
    if os.path.exists(LOCAL_HASH_FILE):
        with open(LOCAL_HASH_FILE, 'r') as f:
            return f.read().strip()
    return None

if __name__ == "__main__":
    latest_commit = get_latest_commit()
    last_commit = read_last_commit()

    if latest_commit != last_commit:
        print("New commit found! Deploying code...")
        save_latest_commit(latest_commit)
        os.system("/path/to/deploy_code.sh")
    else:
        print("No new commits.")