import base64
import json
import hmac
import hashlib

token = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VyX2lkIjogMSwgInVzZXJuYW1lIjogImFkbWluIn0.QblWreyn3p9q3UYUE1HYAejJac_gup7nZEwlcuMXJcw"
secret = b"supersecretkey"

header_b64, payload_b64, signature_b64 = token.split(".")

def decode_base64url(data):
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding).decode()

header = json.loads(decode_base64url(header_b64))
payload = json.loads(decode_base64url(payload_b64))

print("Header:",header)
print("Payload:",payload)

msg = f"{header_b64}.{payload_b64}".encode()
expected_sig = base64.urlsafe_b64encode(
    hmac.new(secret, msg, hashlib.sha256).digest()
).decode().rstrip("=")

if expected_sig == signature_b64:
    print("\n Success!!! 签名验证成功!JWT未被篡改")
else:
    print("\n Error!!! 签名验证失败!Token已被修改")