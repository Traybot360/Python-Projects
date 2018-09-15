from flask import Flask
app = Flask('app')

#landing
@app.route('/')
def landing():
  return 'Welcome'

#login
@app.route('/login')
def login():
  return 'login'

#register
@app.route('/register')
def regiter():
  return 'register'

#frogot
@app.route('/frogot')
def frogot():
  return 'frogot'
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
