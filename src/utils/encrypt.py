import bcrypt


def encrypt_password(clean_password: str) -> bytes:
    password_bytes: bytes = clean_password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hash: bytes = bcrypt.hashpw(password_bytes, salt)
    print(f'Generated hash: {hash}')
    return hash


def check_password(
    provided_password: str, stored_password_hash: bytes
) -> bool:
    provided_password_bytes: bytes = provided_password.encode('utf-8')
    result: bool = bcrypt.checkpw(
        provided_password_bytes, stored_password_hash
    )
    return result
