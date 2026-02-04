import random
import string

def generate_email():
    return "test_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@mail.com"

REGISTER_URL = "https://stellarburgers.education-services.ru/register"
