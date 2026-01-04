import random
import string
import secrets
from faker import Faker

char = string.ascii_letters + string.digits + "#@$%!?"
print("".join(secrets.choice(char) for _ in range(10)))
print(random.randint(0, 10))

fake = Faker()
print(fake.name())
