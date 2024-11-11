from pydantic import BaseModel

class AssignedEventBase(BaseModel):
    pass    

class AssignedEventCreate(AssignedEventBase):
    admin_id : int
    event_id : int


class AssignedEventOut(AssignedEventBase):
    id : int