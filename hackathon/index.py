from flask import Flask, render_template, request, redirect
import mysql.connector
# import uuid

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

@app.route('/login')
def login():
    return render_template('login.html',title="login")

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['passwd']
        # cursor.execute('select * from ')
        return redirect('/')

@app.route('/signup')
def signup():
    return render_template('signup.html',title="signup")

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if request.method=="POST":
        fullname=request.form['fname']
        email=request.form['email']
        phone=request.form['phone']
        username=request.form['username']
        # userid=uuid.uuid4().hex
        
        return redirect('/')


if __name__=="__main__":
    app.run(debug=True)