from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Date

from ..database import db
from ..mixins import CRUDModel


class Task(CRUDModel):
    __tablename__ = 'tasks'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    TaskName = Column(String, nullable=False, index=True)
    Description = Column(String, nullable=False, index=True)

