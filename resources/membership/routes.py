from flask import request
from uuid import uuid4

from app import app
from db import memberships, users

# membership routes

@app.get('/membership')
def get_memberships():
  return { 'memberships': list(memberships.values()) }

@app.get('/membership/<membership_id>')
def get_membership(membership_id):
  try:
    return {'membership': memberships[membership_id]}, 200
  except KeyError:
    return {'message': "Invalid Membership"}, 400

@app.post('/membership')
def create_membership():
  membership_data = request.get_json()
  user_id = membership_data['user_id']
  if user_id in users:
    memberships[uuid4()] = membership_data
    return { 'message': "Membership Created" }, 201
  return { 'message': "Invalid User"}, 401

@app.put('/membership/<membership_id>')
def update_membership(membership_id):
  try:
    membership = memberships[membership_id]
    membership_data = request.get_json()
    if membership_data['user_id'] == membership['user_id']:
      membership['body'] = membership_data['body']
      return { 'message': 'Membership Updated' }, 202
    return {'message': "Unauthorized"}, 401
  except:
    return {'message': "Invalid Membership Id"}, 400

@app.delete('/membership/<membership_id>')
def delete_membership(membership_id):
  try:
    del memberships[membership_id]
    return {"message": "Membership Deleted"}, 202
  except:
    return {'message':"Invalid Membership"}, 400