from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import MembershipModel
from schemas import MembershipSchema, MembershipSchemaNested

from . import bp
# memmbership routes

@bp.route('/<memebrship_id>')
class Membership(MethodView):

  @bp.response(200, MembershipSchemaNested)
  def get(self, membership_id):
    membership = MembershipModel.query.get(membership_id)
    if membership:
      print(membership.author)
      return membership 
    abort(400, message='Invalid Membership')

  @bp.arguments(MembershipSchema)
  def put(self, membership_data ,membership_id):
    membership = MembershipModel.query.get(membership_id)
    if membership:
      membership.body = membership_data['body']
      membership.commit()
      return {'message': 'membership updated'}, 201
    return {'message': "Invalid Membership Id"}, 400

  def delete(self, membership_id):
    membership = MembershipModel.query.get(membership_id)
    if membership:
      membership.delete()
      return {"message": "Membership Deleted"}, 202
    return {'message':"Invalid Membership"}, 400

@bp.route('/')
class MembershipList(MethodView):

  @bp.response(200, MembershipSchema(many = True))
  def get(self):
    return MembershipModel.query.all()
  
  @bp.arguments(MembershipSchema)
  def membership(self, membership_data):
    try:
      membership = MembershipModel()
      membership.user_id = membership_data['user_id']
      membership.body = membership_data['membership']
      membership.commit()
      return { 'message': "Membership Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401