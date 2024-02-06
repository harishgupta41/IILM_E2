from flask import Flask, render_template, request, redirect
import mysql.connector
import uuid

mydb = mysql.connector.connect(
    host="localhost",
    database="harry",
    username="harry",
    password="dl3san3581"
)
cursor = mydb.cursor()

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "hello world!"

@app.route('/login')
def login():
    return render_template('login.html',title='harry')

@app.route('/login_user',methods=['POST'])
def login_user():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['passwd']
        cursor.execute('select * from ')
        return redirect('/')