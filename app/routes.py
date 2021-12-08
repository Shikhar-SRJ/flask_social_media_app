import re
from flask.templating import render_template
from flask import app,request
from models import *
import hashlib





@app.route("/")
def index():
    return render_template('#')


@app.route('/registersuccess', methods = ["POST"])
def registersuccess():
    
    if request.method == "POST":
       
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = User( name = name, email = email,password = hashedPassword)       
        db.session.add(entry)
        db.session.commit()

        return render_template('#')


@app.route('/loginsuccess',methods = ["POST"])
def Aloginsuccess():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = db.session.query(User).filter(User.email == email, User.password == hashedPassword)
        for row in result:
            if len(row.email)!= 0:       
                print("welcome",row.name)
                return render_template('#',data=row.name)
        data = "wrong credentials"
        return render_template('#', data=data)




@app.route("/datapost", methods = ["POST"])
def datapost():
    body=request.form.get("body")
    timestamp = request.form.get("timestamp")
    user_id = request.form.get("user_id")

    entry=Post(body=body, timestamp=timestamp, user_id=user_id)
    db.session.add(entry)
    db.session.commit()

    return render_template("#")


if __name__ == "__main__":
    app.run(debug=True, port=3001)