from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import pbkdf2_hmac
import bcrypt

# هش پسورد کاربران
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password: str, password_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash)

# ساخت کلید AES منحصر به فرد برای هر کاربر
def derive_key(password: str, salt: bytes) -> bytes:
    return pbkdf2_hmac('sha256', password.encode(), salt, 100_000, dklen=32)

# AES-GCM
def encrypt(plaintext: str, key: bytes):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return ciphertext, cipher.nonce

def decrypt(ciphertext: bytes, nonce: bytes, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()
