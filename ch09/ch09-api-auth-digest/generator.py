import secrets
import string
import random

nonce = secrets.token_urlsafe()
print(nonce)
opaque = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
print(opaque)