import bcrypt


def encrypt_password(clean_password: str) -> bytes:
    password_bytes: bytes = clean_password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hash: bytes = bcrypt.hashpw(password_bytes, salt)
    print(f"Generated hash: {hash}")
    return hash


