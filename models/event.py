from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from core.database import Base
from sqlalchemy.orm import relationship


class AssignedReward(Base):
    __tablename__ = "assigned_reward"

    id = Column(Integer, primary_key=True, index=True)
    amount_allocated =  Column(Integer, nullable=False, index=True)
    reward_id = Column(Integer, ForeignKey('rewards.id'))
    admin_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    reward = relationship('Rewards', back_populates="reward")
    admin = relationship('Users', back_populates="admin")
    event = relationship('Events', back_populates="event")   


class Rewards(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(150), nullable=True)

    participants = relationship("Participants", back_populates="reward")
    reward = relationship("AssignedReward", back_populates="reward")  


class EventAssigned(Base):
    __tablename__ = "event_asingned"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(ForeignKey('events.id'))
    admin_id = Column(ForeignKey('users.id'))

    event = relationship("Events", back_populates="eventt")
    admin = relationship("Users", back_populates="adminn")
    

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(150), nullable=True)

    participants = relationship("Participants", back_populates="event")
    event = relationship("AssignedReward", back_populates="event") 
    eventt = relationship("EventAssigned", back_populates="event")


class Participants(Base):  
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    identification = Column(String(100), nullable=False, index=True)  
    claim = Column(Boolean, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'))
    reward_id = Column(Integer, ForeignKey('rewards.id'))

    reward = relationship("Rewards", back_populates="participants")
    event = relationship("Events", back_populates="participants")  


