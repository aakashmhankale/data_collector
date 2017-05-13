from flask import Flask,render_template,request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
#from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


#app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:lifeisgood123@localhost/heightcollector'
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://klqlblnzcqwsum:84c1c5fc082aa05d0277c8486a7310d9d8881975983f6b90fc58592f42f8c9ca@ec2-184-73-199-72.compute-1.amazonaws.com:5432/d8eg8d2qsaqskj?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email,height):
        self.email=email
        self.height=height

@app.route("/")
def index():
    return render_template("index.html")  #go to temp folder and het index.html

@app.route("/success",methods=["POST"])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email==email).count()==0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height)
            count=db.session.query(Data.height).count()
            send_email(email,height,average_height,count)
            return render_template("success.html")
    return render_template("index.html",
    text="Email address already used please use different email address!!!")
        # data=Data(email,height)
        # db.session.add(data)
        # db.session.commit()
        # return render_template("success.html")

if __name__=="__main__":  #if script is executed app will execute following lines
    app.debug=True
    app.run()
