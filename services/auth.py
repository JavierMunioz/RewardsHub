from auth.hash import verify_hash
from core.database import SessionLocal
from models.user import Roles, Users
from fastapi import HTTPException
from auth.auth_handler import create_access_token

def login_s(user, password):
    db = SessionLocal()
    user_db = db.query(Users).filter(Users.username == user).first()

    if not user_db:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    if not verify_hash(password=password, hash=user_db.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    rol = user_db.rol.id

    db.close()
    
    return {"access_token": create_access_token({"sub": user_db.username,
                                                 "rol": rol,
                                                 "email": user_db.email}), 
            "token_type": "bearer"}

        