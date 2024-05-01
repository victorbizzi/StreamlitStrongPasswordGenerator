import string
import secrets


def generate_strong_password(len=10):
    char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(char) for _ in range(len))