from flask import request
from uuid import uuid4
from flask.views import MethodView

from schemas import MembershipSchema
from db import memberships, users
from . import bp
# memmbership routes

@bp.route('/<memebrship_id>')
class Membership(MethodView):

  @bp.response(200, MembershipSchema)
  def get(self, membership_id):
    try:
      return memberships[membership_id]
    except KeyError:
      return {'message': "Invalid Membership"}, 400

  @bp.arguments(MembershipSchema)
  def put(self, membership_data ,membership_id):
    try:
      membership = memberships[membership_id]
      if membership_data['user_id'] == membership['user_id']:
        membership['body'] = membership_data['body']
        return { 'message': 'Membership Updated' }, 202
      return {'message': "Unauthorized"}, 401
    except:
      return {'message': "Invalid Membership Id"}, 400

  def delete(self, membership_id):
    try:
      del memberships[membership_id]
      return {"message": "Membership Deleted"}, 202
    except:
      return {'message':"Invalid Method"}, 400

@bp.route('/')
class MembershipList(MethodView):

  @bp.response(200, MembershipSchema(many = True))
  def get(self):
    return  list(memberships.values())
  
  @bp.arguments(MembershipSchema)
  def membership(self, membership_data):
    user_id = membership_data['user_id']
    if user_id in users:
      memberships[uuid4()] = membership_data
      return { 'message': "Membership Created" }, 201
    return { 'message': "Invalid User"}, 401