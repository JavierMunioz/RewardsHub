from sqlalchemy import update
from core.database import SessionLocal
from fastapi import HTTPException
from models.event import Rewards, AssignedReward, EventAssigned, Participants
from models.user import Users
from schemas.rewards import RewardsCreate
from schemas.participants import ParticipantsBase
from schemas.assigned_reward import AssignedRewardCreate


def create_reward_s(reward_client: RewardsCreate):


   db = SessionLocal()
   reward = db.query(Rewards).filter(Rewards.name == reward_client.name).first()
   
   if reward:
      raise HTTPException(status_code=400, detail="This reward already exists.")
   
   try: 
      reward_db = Rewards(name=reward_client.name, description=reward_client.description)
      
      db.add(reward_db)
      db.commit()
      db.refresh(reward_db)

      db.close()
   except:
      db.close()
      raise HTTPException(status_code=400, detail="Error, the user was not created.")

   return reward_db


def assigned_reward_s(assigned_reward : AssignedRewardCreate):
    db = SessionLocal()
    assignereward_db = db.query(AssignedReward).filter((AssignedReward.admin_id == assigned_reward.admin_id) & (AssignedReward.event_id == assigned_reward.event_id) & (AssignedReward.reward_id == assigned_reward.reward_id)).first()
    
    if assigned_reward.amount_allocated < 1:
        raise HTTPException(detail="The amount must be greater than 0.", status_code=400)

    if assignereward_db:
        raise HTTPException(status_code=400, detail="This reward is already assigned to this administrator.")
        
    try:
        assignereward_db = AssignedReward(amount_allocated=assigned_reward.amount_allocated,
                                          reward_id=assigned_reward.reward_id,
                                          admin_id=assigned_reward.admin_id,
                                          event_id=assigned_reward.event_id)
        
        db.add(assignereward_db)
        db.commit()
        db.refresh(assignereward_db)
        db.close()

    except:
        db.close()
        raise HTTPException(status_code=400, detail="Error, the event was not created.")
    
    return assignereward_db

def assigned_win_s(assigned_win: ParticipantsBase , user_client):
    db = SessionLocal()
    
    user_db = db.query(Users).filter(Users.username == user_client["sub"]).first()
    event_db = db.query(EventAssigned).filter(EventAssigned.admin_id == user_db.id).first()

    if not event_db or not user_db:
        raise HTTPException(status_code=400, detail="Admin is not event") 
    
    reward_db = db.query(AssignedReward).filter((AssignedReward.admin_id == user_db.id) & (AssignedReward.event_id == event_db.id)).first()

    if not reward_db:
        raise HTTPException(status_code=400, detail="Not reward assigned")
    
    if not reward_db.amount_allocated > 0:
        raise HTTPException(status_code=400, detail="Amount error")

    try:
        participant = Participants(identification=assigned_win.identification, 
                                   claim=False, 
                                   event_id=event_db.id, 
                                   reward_id=assigned_win.reward_id)

        
        db.add(participant)
        db.execute(
            update(AssignedReward).
            where(AssignedReward.id == reward_db.id).
            values(amount_allocated=(reward_db.amount_allocated - 1)))
        db.commit()
        db.refresh(participant)
        db.close()

    except:
        db.close()
        raise HTTPException(status_code=400, detail="Error, Winner not assigned.")

    return participant

def assigned_reward_list_s(user_client):
    db = SessionLocal()

    admin_db = db.query(Users).filter(Users.username == user_client["sub"]).first()
    
    if not admin_db:
        raise HTTPException(status_code=400, detail="Admin not exists.")
    
    all_assigned = db.query(AssignedReward).filter(AssignedReward.admin_id == admin_db.id).all()

    rewards = []
    
    for i in all_assigned:
        reward = db.query(Rewards).filter(Rewards.id == i.reward_id).first()
        rewards.append({
            "reward_name": reward.name,
            "reward_id": i.reward_id,
            "amount_allocated": i.amount_allocated 
        })

    db.close()

    return rewards