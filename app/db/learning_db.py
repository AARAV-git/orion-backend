# app/db/learning_db.py
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, PickleType
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

DATABASE_URL = "sqlite:///./learner.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class LearningFeedback(Base):
    __tablename__ = "learning_feedback"

    id = Column(Integer, primary_key=True, index=True)
    features = Column(PickleType)      # Patient features
    ai_score = Column(Float)
    doctor_score = Column(Float)
    delta = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


def get_learning_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
