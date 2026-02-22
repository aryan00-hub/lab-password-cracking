from zipfile import ZipFile

ZIP_NAME = "whitehouse_secrets.zip"
PASSWORD_FILE = "Ashley-Madison.txt"

# Load passwords
with open(PASSWORD_FILE, "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(passwords)} passwords.")

# Try each password
with ZipFile(ZIP_NAME) as zf:
    for i, pw in enumerate(passwords, start=1):

        # Show progress every 10000 tries
        if i % 10000 == 0:
            print(f"Trying #{i}: {pw}")

        try:
            zf.extractall(pwd=pw.encode("ascii", errors="ignore"))
            print("\n✅ PASSWORD FOUND:", pw)
            break
        except Exception:
            pass
        