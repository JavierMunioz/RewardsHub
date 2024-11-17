from pydantic import BaseModel

class ParticipantsBase(BaseModel):
    identification: str
    reward_id: int
    

class ParticipantsCreate(ParticipantsBase):
    claim: bool
    event_id: int
    

class ParticipantsOut(ParticipantsBase):
    id : int