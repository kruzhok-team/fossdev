import hashlib

def make_id(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()[:16]