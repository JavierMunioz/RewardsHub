from fastapi import APIRouter, Form
from schemas.event import EventCreate
from services.event import create_event_s, assigned_event_s, list_event_s
from schemas.assigned_event import AssignedEventCreate

router = APIRouter(prefix='/event', tags=['event'])

@router.post('/create')
async def create(event : EventCreate):
    return create_event_s(event)

@router.post('/assigned')
async def assigned(assigned_event : AssignedEventCreate):
    return assigned_event_s(assigned_event)

@router.get('/all')
async def list_event():
    return list_event_s()