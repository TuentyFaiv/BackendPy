# SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# App
from app.libs.database import Base

class Item(Base):
  __tablename__ = "items"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(50), index=True)
  description = Column(String(500), index=True)
  owner_id = Column(Integer, ForeignKey("users.id"))
  owner = relationship("User", back_populates="items")