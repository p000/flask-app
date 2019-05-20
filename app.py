#author Pushpahas

from flask import Flask, render_template, redirect, url_for, request, g
# ADD YOUR MODULES HERE AS SHOWN IN EXTRA EXAMPLE
from extra import extra
import sqlite3
import hashlib

app = Flask(__name__)

def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)


@app.route('/example', methods=['GET', 'POST'])
def example():
    error = None
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        completion = extra.Extra.add(a, b)
        if completion ==False:
            error = 'Invalid Inputs. Please try again.'
        else:
			return render_template('extra.html', error=error)


@app.route('/secret')
def secret():
    return "You have successfully logged in"

if __name__ == '__main__':
    app.run(debug=True)