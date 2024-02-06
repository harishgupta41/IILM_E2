from flask import Flask, render_template, request, redirect
import mysql.connector
import uuid

mydb = mysql.connector.connect(
    host="localhost",
    database="harry",
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

# @app.route('/user_login',methods=['GET','POST'])
# def user_login():
#     if request.method=='POST':
#         username=request.form['username']
#         password=request.form['passwd']
#         cursor.execute('select * from ')
#         return redirect('/')

@app.route('/signup')
def signup():
    return render_template('signup.html',title="signup")


if __name__=="__main__":
    app.run(debug=True)