from fastapi import APIRouter, Form
from services.auth import login_s

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return login_s(password=password, user=username)