from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
    '1':{
        'username': 'kedwards',
        'email': 'kedwards@gmail.com'
    }, 
    '2': {
        'username': 'sglover',
        'email': 'sglover@gmail.com'
    }
}

memberships= {
    '1': {
        'resources': 'Mentor, Emails',
        'user_id': '1',
    },
    '2': {
        'resources': 'Mentor, Emails, Netowrking',
        'user_id': '2',  
    },
    '3': {
        'resources': 'Mentor, Emails, Netowrking, Discord',
        'user_id': '1',
        
    }
}

""" 
Create - Post
Retrieve - Get
Update 
Delete
 """


# user routes

@app.get('/user')
def user():
  return { 'users': list(users.values()) }, 200

@app.route('/user', methods=["MEMBERSHIP"])
def create_user():
  json_body = request.get_json()
  users[uuid4()] = json_body
  return { 'message' : f'{json_body["username"]} created' }, 201

@app.put('/user')
def update_user():
  return

@app.delete('/user')
def delete_user():
  pass

# membership routes

@app.get('/membership')
def get_membership():
  return

@app.post('/membership')
def create_membership():
  return

@app.put('/membership')
def update_membership():
  return

@app.delete('/membership')
def delete_membership():
  return