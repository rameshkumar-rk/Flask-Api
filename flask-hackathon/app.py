from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Float
import os
from flask_marshmallow import Marshmallow
app = Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'package.db')
db=SQLAlchemy(app)
ma=Marshmallow(app)
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created")

@app.route('/')
def home():
   return 'TCS Hackathon'

@app.route('/addPackage',methods=['GET'])
def add_package():
        city = request.form.get('city')
        days = request.form.get('days')
        price=request.form.get('price')

        new_package = Package(
                            city=city,
                            days=days,
                            price=price)

        db.session.add(new_package)
        db.session.commit()
        return jsonify(message="You added a Pacakage"), 201

@app.route('/viewpackage')
def viewpackage():
   pass
@app.route('/deletepackage')
def deletepackage():
   pass
@app.route('/updatepakage')
def updatepakage():
   pass


class Package(db.Model):
    __tablename__ = 'packages'
    package_id = Column(Integer, primary_key=True)
    city = Column(String)
    days = Column(Integer)
    price = Column(Integer)
    
class PackageSchema(ma.Schema):
    class Meta:
        fields = ('package-id','city','days','price')

if __name__=='__main__':
    app.run()

