from sqlalchemy import Column, String, Float, Boolean, Text, ARRAY, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
import uuid
from database import Base

class ProfileDB(Base):
    __tablename__ = "profiles"
    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))

    # Relationship: One User can have many Products
    products = relationship("ProductDB", back_populates="seller", cascade="all, delete-orphan")


class ProductDB(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    images = Column(ARRAY(String), default=[])
    is_sold = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))

    seller = relationship("ProfileDB", back_populates="products")
