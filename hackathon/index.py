from flask import Flask, render_template, request, redirect, make_response, jsonify
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
        data=[]
        data.append(request.form['fname'])
        data.append(request.form['email'])
        data.append(request.form['phone'])
        data.append(request.form['username'])
        data.append(request.form['password'])
        password=request.form['password']
        cnfm_password=request.form['cnfmpassword']
        print(data)
        if password!=cnfm_password:
            return redirect('/')
        else:
            return jsonify(data),redirect('/verify_otp')

@app.route('/verify_otp')
def verify_otp():
    data=request.get_json()
    print(data)
    gen_otp=getOTPapi(data[2])
    if request.method=="POST":
        rec_otp=request.form['rec_otp']
        if gen_otp!=rec_otp:
            return redirect('/')
        else:
            cursor.execute('insert into students values ("{0}","{1}","{2}","{3}","{4}")'.format(data[3],data[0],data[1],hash_sha_256(data[4]),data[3]))
            mydb.commit()
            return redirect('/')
        
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