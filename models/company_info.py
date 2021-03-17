from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import BYTEA
from .company import Company

Base = declarative_base()

class CompanyInfo(Base):
    __tablename__ = 'company_info'
    __table_args__ = {'schema':'appointment'}
    company_id = Column(Integer, ForeignKey(Company.id), primary_key=True)
    rnc = Column(String)
    email = Column(String)
    tel = Column(String)
    address = Column(String)
    webpage = Column(String)
    social_networking = Column(String)
    logo = Column(BYTEA)
