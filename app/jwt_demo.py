import base64
import json
import hmac
import hashlib

header = {"alg": "HS256", "typ":"JWT"}
header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")

payload = {"user_id": 1, "username": "admin"}
payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")

secret = b"supersecretkey"
sign_input = f"{header_b64}.{payload_b64}".encode()
signature = hmac.new(secret, sign_input, hashlib.sha256).digest()
signature_b64 = base64.urlsafe_b64encode(signature).decode().rstrip("=")

jwt_token = f"{header_b64}.{payload_b64}.{signature_b64}"

print("生成的JWT：")
print(jwt_token)