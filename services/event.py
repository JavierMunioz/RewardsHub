from fastapi import HTTPException
from models.event import Events, EventAssigned
from schemas.assigned_event import AssignedEventCreate
from schemas.event import EventCreate
from core.database import SessionLocal

def create_event_s(event_client: EventCreate):
   
    
    db = SessionLocal()
    event = db.query(Events).filter(Events.name == event_client.name).first()
    
    if event:
        raise HTTPException(status_code=400, detail="This event already exists.")
    
    try:
        event_db = Events(name=event_client.name, 
                        description=event_client.description)
        
        db.add(event_db)
        db.commit()
        db.refresh(event_db)
        db.close()
    except:
        db.close()
        raise HTTPException(status_code=400, detail="Error, the event was not created.")
    
    return event_db


def assigned_event_s(assignedevent_client : AssignedEventCreate):
    db = SessionLocal()
    assignedevent = db.query(EventAssigned).filter(EventAssigned.admin_id == assignedevent_client.admin_id).first()
    
    if assignedevent:
        raise HTTPException(status_code=400, detail="This administrator is already assigned to this event.")
    
    try:
        assignedevent_db = EventAssigned( admin_id=assignedevent_client.admin_id, 
                                         event_id=assignedevent_client.event_id)
        
        db.add(assignedevent_db)
        db.commit()
        db.refresh(assignedevent_db)
        db.close()
    except:
        db.close()
        raise HTTPException(status_code=400, detail="Error, the event was not created.")
    
    return assignedevent

def list_event_s():
    db = SessionLocal()

    all_event = db.query(Events).all()
    

    db.close()
    
    return [i for i in all_event]