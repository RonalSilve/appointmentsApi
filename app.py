from flask import Flask
from sqlalchemy import create_engine
from models.company import Company
from models.company_info import CompanyInfo
from models.branch import Branch
from models.branch_info import BranchInfo

app = Flask(__name__)
engine = create_engine('postgres://ecsgbphobnwxid:ff797852b3ff9b64722de63803b9fc7fc0586fed4ef7f300fa6f93363b749f40@ec2-3-87-180-131.compute-1.amazonaws.com:5432/dfqf4josj7ak7l')

Company.__table__.create(bind=engine, checkfirst=True)
Branch.__table__.create(bind=engine, checkfirst=True)
BranchInfo.__table__.create(bind=engine, checkfirst=True)
CompanyInfo.__table__.create(bind=engine, checkfirst=True)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
