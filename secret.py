import secrets
import string

def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = "".join(secrets.choice(characters) for _ in range(length) )
    return secret_key

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(secret_key)