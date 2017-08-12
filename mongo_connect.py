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
    user.insert({'name' : 'Michael', 'language':'python'})
    user.insert({'name' : 'Kelly', 'language':'C'})
    user.insert({'name' : 'John', 'language':'Java'})
    user.insert({'name' : 'Cedric', 'language':'Haskell'})
    return 'Added User!'
	
@app.route('/find')
def find():
    user = mongo.db.users
    cedric = user.find_one({'name':'Cedric'})
    return 'You found ' + cedric['name'] + '. His favourite language is ' + cedric['language']

@app.route('/update')
def update():
    user = mongo.db.users
    john = user.find_one({'name':'John'})
    john['language'] = 'JavaScript'
    user.save(john)
    return 'Updated John!!'

@app.route('/delete')
def delete():
    user = mongo.db.users
    kelly = user.find_one({'name':'Kelly'})
    user.remove(kelly)
    return 'Removed Kelly!'


if __name__ == '__main__':
    app.run()
