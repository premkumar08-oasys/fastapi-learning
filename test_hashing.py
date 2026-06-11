from utils.hashing import hash_password
from utils.hashing import verify_password

password = "prem123"

hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)

result = verify_password(
    "prem123",
    hashed
)

print("Verified:", result)