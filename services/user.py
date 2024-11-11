from models.user import Users
from schemas.user import UserCreate
from core.database import SessionLocal
from fastapi import HTTPException
from auth.hash import hash

def create_user_s(user_client: UserCreate):


   db = SessionLocal()
   user = db.query(Users).filter(Users.username == user_client.username).first()
   user2 = db.query(Users).filter(Users.email == user_client.email).first()
   
   if user or user2:
      raise HTTPException(status_code=400, detail="This user already exists.")
   
   try: 
      user_db = Users(username=user_client.username,
                     password=hash(user_client.password),
                     email=user_client.email,
                     rol_id=user_client.rol_id)
      
      db.add(user_db)
      db.commit()
      db.refresh(user_db)

      db.close()
   except:
      db.close()
      raise HTTPException(status_code=400, detail="Error, the user was not created.")

   return user_db
   