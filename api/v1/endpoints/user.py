from fastapi import APIRouter, Depends
from auth.auth_bearer import get_current_user
from schemas.user import UserCreate
from services.user import create_user_s

router = APIRouter(prefix='/user', tags=['user'])
#, current_user: dict = Depends(get_current_user)
@router.post('/create')
async def create_user(user: UserCreate):
    return create_user_s(user)