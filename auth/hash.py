import bcrypt


def hash(password):
    password = password.encode()

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password, salt)

    return hashed

def verify_hash(password, hash):
    is_ = bcrypt.checkpw(password.encode(), bytes(hash.encode()))
    return is_