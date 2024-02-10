from flask import Flask, render_template, request, redirect, make_response
import mysql.connector
from user_methods import hash_sha_256, getOTPapi

mydb = mysql.connector.connect(
    host="localhost",
    database="study",
    user="harry",
    password="dl3san3581"
)
cursor = mydb.cursor()

app=Flask(__name__)

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
        # print(request.form)
        data=[]
        data.append(request.form['fname'])
        data.append(request.form['email'])
        data.append(request.form['phone'])
        # fullname=request.form['fname']
        # email=request.form['email']
        # phone=request.form['phone']
        print(data)
        return redirect('/set_username')

        
        if password!=cnfm_password:
            return redirect('/')
        else:
            # getOTPapi(phone)
            cursor.execute('insert into students values ("{0}","{1}","{2}","{3}","{4}")'.format(username,fullname,email,hash_sha_256(password),phone))
            mydb.commit()
            return render_template('access.html',title="registration-success!")

@app.route('/set_username')
def set_username():
    # name = request.args.get('name')
    fullname=request.args.get('fname')
    email=request.args.get('email')
    phone=request.args.get('phone')
    username=request.form['username']
    password=request.form['password']
    cnfm_password=request.form['cnfmpassword']

# @app.route('/otp_verification',methods=['GET','POST'])
# def otp_verification():
#     if request.method=="POST":
#         number=request.form['phone']
#         val=getOTPapi(number)
#         if val

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