import os
import pathlib
from app import *
from flask import render_template
from flask import  request, make_response
from app.models import  *
import hashlib


@app.route('/')
def index():
    return render_template('index.html')

# login routes here
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginsuccess', methods=['POST'])
def loginSucess():
    if request.method == 'POST':
        username = request.form.get('userName')
        password = request.form.get('password')
        #hashing the input and comparing the hash
        # hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        # hashedPassword = hashedPassword.hexdigest()
        result = db.session.query(User).filter(User.username==username, User.password_hash==password)
        for row in result:
            if (len(row.username)!=0 and len(row.password_hash)!=0):
                print(row.username)
                print(row.password_hash)
                # return render_template('profile.html')
                return f"Hello {row.username}! <br/> <a href='/'><button>Logout</button></a>"
    return render_template('login.html', error='could not verify')


# register routes
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/registersuccess', methods=["POST"])
def registerSuccess():
    # app.logger.info('Info level log')
    # app.logger.warning('Warning level log')
    if request.method == "POST":
        username = request.form.get('userName')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if confirm_password == password:
            #hashing the password before storing
            # hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
            # hashedPassword = hashedPassword.hexdigest()
            entry = User(username=username,email=email,password_hash=password)
            db.session.add(entry)
            db.session.commit()
            print('register successfull')
    return render_template('login.html')



@app.route('/sentMail')
def sentMail(userMail):
    msg = Message(
                'reset app password',
                sender ='noreply@gmail.com',
                recipients ={userMail},
                body = '''Hello Flask message sent from Flask-Mail '''
                )
    mail.send(msg)
    print('email has been send')
    return 'Sent'

@app.route('/forgetPassword')
def forgetPassword():
    return render_template('forgetPassword.html')

@app.route('/reset' ,methods=['GET','POST'])
def reset():
    email = request.form.get('email')
    result = db.session.query(User).filter(User.email==email).first()
    print(result)
    sentMail('rohits8853@gmail.com')
    if  result:
        return render_template('login.html');
    return render_template('forgetPassword.html' ,error='ERROR: Please enter registerd email')

