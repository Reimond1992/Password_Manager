# Password Manager CLI

A **professional password manager** built in Python, using AES-256 encryption and SQLite, ready for use and development.

## Features
- AES-256 encryption for each user
- User password hashing with bcrypt
- Secure password storage in SQLite
- Simple CLI using Click
- Add / View / Delete passwords
- Ready for internationalization (i18n)

## Installation

Clone the repository:

```bash
git clone https://github.com/username/password_manager.git
cd password_manager
Create and activate a Python virtual environment (recommended):

Windows PowerShell:

python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
Windows CMD:

python -m venv venv
venv\Scripts\activate.bat
Linux / macOS:

python3 -m venv venv
source venv/bin/activate
Install required packages:

pip install -r requirements.txt
Database Initialization
Before using the CLI, initialize the SQLite database:

python -c "from password_manager import db; db.init_db()"
This will create the necessary tables: users and passwords.

Usage
Register a new user
python -m password_manager.cli register
Prompts for a username and password.

Password is securely hashed and stored with a unique salt.

AES-256 key is generated later when logging in.

Login and manage passwords
python -m password_manager.cli login
Prompts for your username and password.

If correct, an AES-256 key is derived from your password and salt.

A menu will appear:

--- Menu ---
1. Add Password
2. View Passwords
3. Delete Password
4. Logout
Choose:
Options:

Add Password → Store a new service password (encrypted with AES-256)

View Passwords → List all stored passwords (decrypted in memory)

Delete Password → Remove a password entry

Logout → Exit the CLI

Note: AES-256 keys are only generated in memory during login. They are not stored on disk. You must remember your master password; otherwise, saved passwords cannot be decrypted.

Security Notes
User passwords are never stored in plain text, only as bcrypt hashes.

Each user has a unique salt for AES-256 key derivation.

Closing the program removes the AES key from memory.

To prevent data loss, consider secure backups of the database (without storing keys).