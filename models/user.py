from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum('Admin', 'EventAdmin', 'User', name='role_types'), nullable=False)  
    descripcion = Column(String(100), nullable=True)
    

    users = relationship("Users", back_populates="rol")  


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), index=True, nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), index=True, unique=True, nullable=False)
    rol_id = Column(Integer, ForeignKey('roles.id'))  
    
    rol = relationship("Roles", back_populates="users")  
    admin = relationship("AssignedReward", back_populates="admin")
    adminn = relationship("EventAssigned", back_populates="admin")

   