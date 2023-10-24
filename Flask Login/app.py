from flask import Flask, render_template, request, redirect, url_for, flash, session
import csv

app = Flask(__name__)
app.secret_key = 'secret_key'

def check_credentials(username, password):
    with open('Flask Login\\users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
        return False

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            session['loggedin'] = True
            return redirect(url_for('home'))
        else:
            flash('Login inválido!')
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)