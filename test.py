"""
Created on 2024/4/9 11:00 
Author: Shuijing
Description: 
"""
import secrets
import string


def generate_random_string(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))


random_string = generate_random_string(8)
print(random_string)

