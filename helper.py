import random
import string

def generate_random_string(length=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return generate_random_string(length, chars)

def generate_user_data():
    return {
        "email": f"user_{generate_random_string(8)}@example.com",
        "password": generate_password(),
        "name": f"User {generate_random_string(5)}"
    }