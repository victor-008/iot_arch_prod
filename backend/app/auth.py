from jose import jwt
from .config import JWT_SECRET

def create_token(device_id):
    return jwt.encode({"device":device_id}, JWT_SECRET)

def verify_token(token):
    return jwt.decode(token, JWT_SECRET)