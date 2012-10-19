from crawler import Repository
from sqlalchemy import Column, Integer, String

class Person(Repository.Base):
    __tablename__ = 'Person'

    Id = Column(Integer, primary_key=True)
    Name = Column(String)

    def __init__(self, Name = None):
        self.Name = Name

    def __repr__(self):
        return "<Person('%s', '%s')>" % (self.Id, self.Name)
