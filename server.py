import json

# import flask modules
# Request - gets details for the request
# Flask - creates the flask app
from flask import Flask, request

# import flask_cors modules
# CORS - enable Cross Origin Resource Sharing
from flask_cors import CORS

# Connect to MongoDB
from credentials import mongodb_parameters
params = mongodb_parameters()
from pymongo import MongoClient

# Setup client and database
client = MongoClient(params['dblink'])
db = client[params['database_name']]

# Create the app and enable CORS
app = Flask(__name__)
CORS(app)

@app.route('/register')
def register():

    reg = {
        'name': request.args.get('name'),
        'email': request.args.get('email'),
        'password': request.args.get('pass')
    }
    print(reg)

    db.login.insert_one(reg)
    return 'Good'

@app.route('/login')
def login():

    uname = request.args.get('email')
    password = request.args.get('pass')

    val = db.login.find_one({'email': uname})

    if val['password'] == password:
        return 'Good'
    return 'Bad'

if __name__ == '__main__':
    app.run()
