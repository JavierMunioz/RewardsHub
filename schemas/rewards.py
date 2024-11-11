from pydantic import BaseModel

class RewardsBase(BaseModel):
    name : str
    description : str


class RewardsCreate(RewardsBase):
    pass


class RewardsOut(RewardsBase):
    id : int