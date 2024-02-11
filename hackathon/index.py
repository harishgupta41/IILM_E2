
import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from flask import Flask, render_template, request, redirect, make_response, jsonify,json
import requests
import mysql.connector
from user_methods import hash_sha_256



mydb = mysql.connector.connect(
    host="localhost",
    database="study",
    user="harry",
    password="dl3san3581"
)
cursor = mydb.cursor()

load_dotenv()

app=Flask(__name__)
app.secret_key = 'secretkeyfordungeon'

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN= os.environ.get('TWILIO_AUTH_TOKEN')
VERIFY_SERVICE_SID= os.environ.get('VERIFY_SERVICE_SID')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="home")

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['passwd']
        cursor.execute('select * from students where username="{0}" and password="{1}"'.format(username,hash_sha_256(password)))
        data=cursor.fetchall()
        if(data):
            resp=make_response(redirect('/'))
            resp.set_cookie('user',username)
            return resp
        else:
            return redirect('/')

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if request.method=="POST":
        data=[]
        data.append(request.form['fname'])
        data.append(request.form['email'])
        data.append(request.form['phone'])
        data.append(request.form['username'])
        data.append(request.form['password'])
        password=request.form['password']
        cnfm_password=request.form['cnfmpassword']
        print(jsonify(data))
        if password!=cnfm_password:
            return redirect('/')
        else:
            send_verification(data[2])
            return jsonify(data=data), redirect('/verify_otp')

@app.route('/verify_otp')
def verify_otp():
    response = requests.post('http://localhost:5000/user_signup')
    if response.status_code == 200:
        json_data = response.json()
        data = json_data.get('data', [])
    # data=request.json()
    print(data)
    # # print(type(data))
    # if request.method=="POST":
    #     rec_otp=request.form['rec_otp']
    #     if check_verification_token(data['phone'], rec_otp):
    #         cursor.execute('insert into students values ("{0}","{1}","{2}","{3}","{4}")'.format(data['username'],data['fname'],data['email'],hash_sha_256(data['password']),data['phone']))
    #         mydb.commit()
    #         return render_template('access.html',title="success")
    #     else:
    #         return redirect('/')
        
def send_verification(phone):
    client.verify \
        .services(VERIFY_SERVICE_SID) \
        .verifications \
        .create(to=phone, channel='sms')

def check_verification_token(phone, token):
    check = client.verify \
        .services(VERIFY_SERVICE_SID) \
        .verification_checks \
        .create(to=phone, code=token)    
    return check.status == 'approved'
        
@app.route('/courses_offered')
def courses_offered():
    return render_template('courses.html',title='courses-offered')

@app.route('/help_center')
def help_center():
    return render_template('help.html',title="help-center")

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('user', '', max_age=0)
    return response

if __name__=="__main__":
    app.run(debug=True)