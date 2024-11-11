from pydantic import BaseModel

class AssignedRewardBase(BaseModel):
    amount_allocated : int
    

class AssignedRewardCreate(AssignedRewardBase):
    reward_id : int
    admin_id : int
    event_id : int


class AssignedRewardOut(AssignedRewardBase):
    id : int