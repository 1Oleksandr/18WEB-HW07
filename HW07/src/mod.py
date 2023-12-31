from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, event
from sqlalchemy.orm import relationship, declarative_base

from src.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True, nullable=False)
    password = Column(String(30))


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)


@event.listens_for(Todo, 'before_update')
def update_updated_at(mapper, conn, target):
    target.updated_at = func.now()


Base.metadata.create_engine()  # create_all.engine()
