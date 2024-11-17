from fastapi import APIRouter, Depends, Form
from auth.auth_bearer import get_current_user
from services.rewards import assigned_reward_list_s, create_reward_s, assigned_reward_s, assigned_win_s
from schemas.rewards import RewardsCreate
from schemas.assigned_reward import AssignedRewardCreate
from schemas.participants import ParticipantsBase

router = APIRouter(prefix='/rewards', tags=['rewards'])

@router.post('/create')
async def create(reward : RewardsCreate):
    return create_reward_s(reward)

@router.post('/assigned')
async def assigned(assigned_event : AssignedRewardCreate):
    return assigned_reward_s(assigned_event)

@router.post('/assigned_win')
async def assigned(assigned_win : ParticipantsBase, current_user: dict = Depends(get_current_user)):
    return assigned_win_s(assigned_win, current_user)

@router.get('/assigned_reward_list')
async def assigned_reward_list(current_user: dict = Depends(get_current_user)):
    return assigned_reward_list_s(current_user)