from flask import Flask, render_template, request, redirect, make_response
import mysql.connector
from user_methods import hash_sha_256

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
        cursor.execute('select * from students where username="{0}" and password="{1}"'.format(username,password))
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
        print(request.form[0])
        fullname=request.form['fname']
        email=request.form['email']
        phone=request.form['phone']
        username=request.form['username']
        password=request.form['password']
        cnfm_password=request.form['cnfmpassword']
        if password!=cnfm_password:
            return redirect('/')
        else:
            cursor.execute('insert into students values ("{0}","{1}","{2}","{3}","{4}")'.format(username,fullname,email,hash_sha_256(password),phone))
            mydb.commit()
            return render_template('access.html',title="registration-success!")

@app.route('/help_center')
def help_center():
    return render_template('help.html',title="help-center")

@app.route('/logout')
def logout():
    response = make_response(render_template('logout.html',title='logging-out'))
    response.set_cookie('user', '', max_age=0)
    return response

if __name__=="__main__":
    app.run(debug=True)