from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Sweet(Base):
    __tablename__ = "sweets"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
