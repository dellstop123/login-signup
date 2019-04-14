from flask import Flask,render_template, redirect, url_for, request
from os import environ
app= Flask(__name__)

@app.route("/a")
def home() :
    return "<h2><a href = /index> Login </a></h2>"

@app.route('/index')
def index():
   score= 30
   return render_template('index.html',marks = score)

@app.route('/signup')  
def sign_up() :
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)  

if __name__ == '__main__':
    app.run(debug = True)
    