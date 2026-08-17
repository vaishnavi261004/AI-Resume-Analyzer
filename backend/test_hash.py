
from apps.services.auth.hash import hash_password, verify_password

password = "mypassword"

hashed = hash_password(password)

print("Hashed Password:", hashed)

print("Verification:", verify_password(password, hashed))