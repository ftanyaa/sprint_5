import random
import string


def generate_email():
    return f"tatsiana_filimonenka_34-35_{random.randint(100,999)}@gmail.com"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
