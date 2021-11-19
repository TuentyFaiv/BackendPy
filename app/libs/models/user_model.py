# SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# App
from app.libs.database import Base

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String(100), unique=True, index=True, )
  hashed_password = Column(String(100))
  is_active = Column(Boolean, default=True)
  items = relationship("Item", back_populates="owner")