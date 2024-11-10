import os
from fastapi import FastAPI
from api.v1.endpoints import user, auth
from core.database import init_db

app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)

@app.get('/', tags=['home'])
async def home():
    return {"Welcome" :  "this a home"}

if __name__ == "__main__":
    init_db()
    os.system("uvicorn main:app --reload")