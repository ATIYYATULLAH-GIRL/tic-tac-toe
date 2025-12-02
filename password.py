import random, string
chars=string.ascii_letters + string.digits
length = 12
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)