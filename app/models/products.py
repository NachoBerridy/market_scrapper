from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(String(50), nullable=False)
    market = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)


DATABASE_URL = 'sqlite:///products.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
