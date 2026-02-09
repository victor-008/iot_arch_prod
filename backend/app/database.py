from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    "postgresql://postgres:postgres@db:5432/iot"
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
