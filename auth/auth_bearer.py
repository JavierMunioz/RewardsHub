from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from auth.auth_handler import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="Invalid credentials")
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    return payload