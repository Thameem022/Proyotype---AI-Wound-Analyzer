import re

def is_valid_email(email):
    """ Validate email format using regex """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def is_strong_password(password):
    """ Validate password strength (Min 8 chars, at least 1 letter & 1 number) """
    return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)
