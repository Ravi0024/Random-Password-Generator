import random
import string
length=int(input("How much would be the length of the Password: "))
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:

password = generate_password(length)
print("Generated Password:", password)
