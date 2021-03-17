from sqlalchemy import Column, Integer, String,PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import BYTEA
from .branch import Branch

Base = declarative_base()

class BranchInfo(Base):
    __tablename__ = 'branch_info'
    __table_args__=(
            PrimaryKeyConstraint(
                'company_id','branch_id'),
            ForeignKeyConstraint(
                ["company_id", "branch_id"],
                [Branch.company_id, Branch.id],
                name="fk_branches_id"
                ),
            {'schema':'appointment'},
            )

    company_id = Column(Integer)
    branch_id = Column(Integer)
    rnc = Column(String)
    email = Column(String)
    tel = Column(String)
    address = Column(String)
    webpage = Column(String)
    social_networking = Column(String)
    logo = Column(BYTEA)
