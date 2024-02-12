from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
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
      return membership 
    abort(400, message='Invalid Membership')

  @jwt_required
  @bp.arguments(MembershipSchema)
  def put(self, membership_data ,membership_id):
    membership = MembershipModel.query.get(membership_id)
    if membership and membership.user_id == get_jwt_identity():
      membership.body = membership_data['body']
      membership.commit()
      return {'message': 'membership updated'}, 201
    return {'message': "Invalid Membership Id"}, 400

  @jwt_required
  def delete(self, membership_id):
    membership = MembershipModel.query.get(membership_id)
    if membership and membership.user_id == get_jwt_identity():
      membership.delete()
      return {"message": "Membership Deleted"}, 202
    return {'message':"Invalid Membership"}, 400

@bp.route('/')
class MembershipList(MethodView):

  @bp.response(200, MembershipSchema(many = True))
  def get(self):
    return MembershipModel.query.all()
  
  @jwt_required
  @bp.arguments(MembershipSchema)
  def membership(self, membership_data):
    try:
      membership = MembershipModel()
      membership.user_id = get_jwt_identity()
      membership.body = membership_data['body']
      membership.commit()
      return { 'message': "Membership Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401