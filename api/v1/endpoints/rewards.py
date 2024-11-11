from fastapi import APIRouter, Form
from services.rewards import create_reward_s, assigned_reward_s
from schemas.rewards import RewardsCreate
from schemas.assigned_reward import AssignedRewardCreate

router = APIRouter(prefix='/rewards', tags=['rewards'])

@router.post('/create')
async def create(reward : RewardsCreate):
    return create_reward_s(reward)

@router.post('/assigned')
async def assigned(assigned_event : AssignedRewardCreate):
    return assigned_reward_s(assigned_event)