import re
from flask import Flask, redirect,render_template, request,redirect,session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from main import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///user.db"
app.config['SQLALCHEMY_BINDS']={"farmer":"sqlite:///farmer.db"}
user=SQLAlchemy(app)
app.secret_key="mmmmm"

class users(user.Model):
    aadhar=user.Column(user.Integer,primary_key=True)
    name=user.Column(user.String(100),nullable=True)
    region=user.Column(user.String(300),nullable=True)
    mail=user.Column(user.String(100),nullable=True)

    # date_time=user.Column(user.DateTime,default=datetime.utcnow)
    state=user.Column(user.String(50),nullable=True)
    # region=user.Column(user.Integer,nullable=True)
    phn=user.Column(user.Integer,nullable=True)
    crop=user.Column(user.String(100),nullable=True)
    password=user.Column(user.String(100),nullable=True)

class farmer(user.Model):
    __bind_key__ = 'farmer'
    aadhar=user.Column(user.Integer,primary_key=True)
    mail=user.Column(user.String(100),nullable=True)
    name=user.Column(user.String(100),nullable=True)
    region=user.Column(user.String(300),nullable=True)
    # date_time=user.Column(user.DateTime,default=datetime.utcnow)
    state=user.Column(user.String(50),nullable=True)
    # region=user.Column(user.Integer,nullable=True)
    phn=user.Column(user.Integer,nullable=True)
    password=user.Column(user.String(100),nullable=True)
    crop=user.Column(user.String(100),nullable=True)



@app.route("/")
def main():
    return render_template("index.html")

@app.route("/fregister",methods=["GET","POST"])
def farmer_register():
   if request.method=="POST" :
    nam=request.form["name"]
    ph=request.form["phn"]
    email=request.form["emai"]
 
    adar=request.form["Adhar"]
    stat=request.form["state"]
    
    p=request.form["pass"]
    reg=request.form["reg"]
    farm=farmer(name=nam,phn=ph,state=stat,mail=email,password=p,aadhar=adar,region=reg)
    user.session.add(farm)
    user.session.commit()
    sh=farmer.query.all()
    send_email(email,nam)

    return redirect("/")
   else:
       return render_template("signupFarmer.html") 

@app.route("/uregister",methods=["GET","POST"])
def user_register():
    if  request.method=="POST" :
        nam=request.form["name"]
        ph=request.form["phn"]
        email=request.form["emai"]
        adar=request.form["Adhar"]
        stat=request.form["state"]
        p=request.form["pass"]
        reg=request.form["reg"]
        cr=request.form["crop"]
        send_email(email,nam)

        far=users(name=nam,phn=ph,state=stat,mail=email,password=p,aadhar=adar,region=reg,crop=cr)
        user.session.add(far)
        user.session.commit()

        return redirect("/")
    else:
        return render_template("signupUser.html") 

@app.route("/flogin" ,methods=["GET","POST"])
def farmer_login():
    if request.method=="POST":
        pas=request.form["pass"]
        us=request.form["emai"]
        todo=farmer.query.filter_by(password=pas).first()

        if todo==None:
            return "<h1>401</h1> Wrong password"
        else:
             return render_template("intro.html",todo=todo)
    else:
        return render_template("loginFarmer.html")

@app.route("/agora")
def ago():
    return render_template("nischay.html")

@app.route("/llogin",methods=["GET","POST"])
def lanlord_login():
    if request.method=="POST":
        pas=request.form["pass"]
        us=request.form["emai"]
        todo=users.query.filter_by(password=pas).first()

        if todo==None:
            return "<h1>401</h1> Wrong password"
        else:
             return render_template("intro.html",todo=todo)
    else:
            return render_template("loginUser.html")

@app.route("/landlord")
def landlord():
    user= users.query.all()
    return render_template("lanlord.html",user=user)

@app.route("/charts")
def charts():
    return render_template("charts.html")


if __name__=="__main__":
    app.run(debug=True)
