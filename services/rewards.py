from core.database import SessionLocal
from fastapi import HTTPException
from models.event import Rewards, AssignedReward
from schemas.rewards import RewardsCreate
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
   