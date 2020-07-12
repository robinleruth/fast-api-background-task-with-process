from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

from app.infrastructure.db import Base


class SomeTable(Base):
    __tablename__ = 'SomeTable'

    id = Column(Integer, primary_key=True)
    info = Column(String)

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<SomeTable {} {}>".format(str(self.id), self.info)
