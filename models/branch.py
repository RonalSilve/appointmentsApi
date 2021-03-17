from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from .company import Company

Base = declarative_base()

class Branch(Base):
    __tablename__ = 'branches'
    __table_args__=(
            PrimaryKeyConstraint(
                'company_id','id'),
            {'schema':'appointment'},
            )
    company_id = Column(Integer, ForeignKey(Company.id))
    id = Column(Integer)
    name = Column(String)
