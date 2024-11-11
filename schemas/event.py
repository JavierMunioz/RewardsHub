from pydantic import BaseModel

class EventBase(BaseModel):
    name : str
    description : str  


class EventCreate(EventBase):
    pass


class EventOut(EventBase):
    id : int