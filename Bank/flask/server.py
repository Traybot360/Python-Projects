from flask import Flask, render_template, request
import json

app = Flask('app')

#landing
@app.route('/')
def landing():
  return 'Welcome'

#login
@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == "POST": 
    if request.form["user"] == "nick":
      print("good job yout logged in!")
  return render_template('login.html')
  


#register
@app.route('/register')
def regiter():
  return 'register'

#forget
@app.route('/forgot')
def forgot():
  return 'forgot'
#about
@app.route('/about')
def about():
  return 'about'
#contact
@app.route('/contact')
def contact():
  return 'contact'
#account
@app.route('/account')
def account():
  return 'account'
#transaction
@app.route('/transaction')
def transaction():
  return 'transaction'
#user
@app.route('/user')
def user():
  return 'user'
#search
@app.route('/search')
def search():
  return 'search'


app.run(host='0.0.0.0', port=8080)
