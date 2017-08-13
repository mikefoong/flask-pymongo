# Flask Login

from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

# Setting up the application
app.config['HOST'] ='127.0.0.1'                   # Change this to 0.0.0.0 if you wwant it to be accessible to external IPs
app.config['DEBUG'] = True
app.config['MONGO_USERNAME'] = "mikefoong"
app.config['MONGO_PASSWORD'] = "more2Life"        # Need to figure out a more secure way to connect to mongoDB without exposing ClearText passwords
#app.config['MONGO_AUTH_SOURCE'] = "admin"
app.config['MONGO_DBNAME'] = 'pymongo_test'
#app.config['MONGO_URI'] = 'mongodb://mikefoong:more2Life@127.0.0.1:27107/pymongo_test'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login')
def login():
    return ''

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({ 'name' : request.form['username'] })

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'], bcrypt.genSalt())
            users.insert({ 'name' : request.form['username'], password : hashpass })
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'pysecret'
    app.run()
