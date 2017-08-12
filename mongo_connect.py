from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MONGO_USERNAME'] = "mikefoong"
app.config['MONGO_PASSWORD'] = "more2Life"
#app.config['MONGO_AUTH_SOURCE'] = "admin"
app.config['MONGO_DBNAME'] = 'pymongo_test'
#app.config['MONGO_URI'] = 'mongodb://mikefoong:more2Life@127.0.0.1:27107/pymongo_test'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name' : 'Michael'})
    return 'Added User!'
	
if __name__ == '__main__':
    app.run()
